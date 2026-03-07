import sys
import os

# Ensure project root is in Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from dotenv import load_dotenv
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

from workflows.referral_workflow import build_workflow
from memory.conversation_memory import ConversationMemory
from tools.mcp.messaging_mcp import MessagingMCP


# Load environment variables
load_dotenv()

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

# Build LangGraph workflow
workflow = build_workflow()


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):

    user_input = update.message.text
    user_id = update.message.from_user.id

    print(f"\nUser {user_id}: {user_input}")

    user_input_lower = user_input.lower()

    try:

        # -------------------------------------------------
        # Messaging MCP Intent Detection
        # -------------------------------------------------

        if "message" in user_input_lower or "text" in user_input_lower:

            candidates = ConversationMemory.get_top_candidates(user_id, 2)

            if not candidates:
                await update.message.reply_text(
                    "No previous candidates found. Please search first."
                )
                return

            message = (
                "Hi! I came across your profile and would love to connect "
                "regarding referral opportunities."
            )

            sent_to = MessagingMCP.send_messages(candidates, message)

            response = "Messages sent to:\n\n"

            for name in sent_to:
                response += f"• {name}\n"

            await update.message.reply_text(response)

            return

        # -------------------------------------------------
        # Search + Ranking Workflow
        # -------------------------------------------------

        result = workflow.invoke({
            "user_input": user_input
        })

        matches = result.get("results", [])

        # Save results to memory
        ConversationMemory.save_results(
            user_id=user_id,
            query=user_input,
            results=matches
        )

        if not matches:
            await update.message.reply_text(
                "No matching professionals found."
            )
            return

        # Format response
        response = "Top Matches:\n\n"

        for r in matches[:5]:

            candidate = r["candidate"]

            response += (
                f"{candidate['name']}\n"
                f"Role: {candidate['role']}\n"
                f"City: {candidate['city']}\n"
                f"Score: {round(r['score'], 2)}\n\n"
            )

        await update.message.reply_text(response)

    except Exception as e:

        print("Error:", e)

        await update.message.reply_text(
            "Something went wrong while processing your request."
        )


def main():

    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(
        MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message)
    )

    print("\nTelegram bot running...\n")

    app.run_polling()


if __name__ == "__main__":
    main()