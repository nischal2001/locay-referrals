from services.email_service import EmailService


class MessagingMCP:

    @staticmethod
    def send_messages(results):

        sent_to = []

        subject = "Quick connection regarding referral"

        for r in results:

            # Debug print
            print("DEBUG RESULT:", r)

            candidate = r.get("candidate")

            if not candidate:
                print("Candidate missing:", r)
                continue

            name = candidate.get("name")
            email = candidate.get("email")

            if not email:
                print(f"No email found for {name}")
                continue

            print(f"Sending email to {name} -> {email}")

            body = f"""
Hi {name},

I came across your profile while exploring professionals in {candidate.get('city')}.

Would love to connect regarding referral opportunities if you're open to it.

Best,
Locay Referrals
"""

            success = EmailService.send_email(email, subject, body)

            if success:
                sent_to.append(name)

        return sent_to