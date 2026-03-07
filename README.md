# LOCAY_REFERRALS

An **Agentic AI system for location-aware professional networking** that discovers nearby professionals, evaluates referral compatibility using LLM reasoning, and initiates real-world outreach via messaging.

The system is deployed as a Telegram bot and orchestrated using a LangGraph agent workflow.

---

## Problem

Professional networking is often random and inefficient.  
When developers travel or work remotely, they lack a structured way to discover relevant professionals nearby for referrals or informal meetups.

Traditional job platforms focus on **job listings**, not **real-world professional connections**.

---

## Solution

LOCAY_REFERRALS is an **AI-driven networking agent** that:

1. Accepts natural language queries from users via Telegram.
2. Discovers nearby professionals from a structured database.
3. Uses an LLM to evaluate compatibility between the user and potential contacts.
4. Ranks candidates based on compatibility scores.
5. Generates contextual outreach messages.
6. Sends real emails to initiate professional conversations.

The system is orchestrated using **LangGraph**, enabling modular agent workflows.

---

## Example Query


I'm in Pune this weekend. Find backend engineers at product companies.


Agent response:


Top Matches:

Rahul Sharma – Backend Engineer – Product Company

Amit Kulkarni – Backend Engineer – Startup

Neha Gupta – Backend Engineer – SaaS Product


Follow-up command:


Send message to first two people


The agent then sends personalized emails to those professionals.

---

## System Architecture


Telegram User
│
▼
Telegram Bot Interface
│
▼
LangGraph Agent Workflow
│
├── Query Parsing
├── MongoDB Professional Search
├── LLM Compatibility Engine
├── Ranking Engine
└── Messaging MCP
│
▼
Email Sent via SMTP


---

## Agent Workflow


User Query
│
▼
Parse Location + Role
│
▼
Search MongoDB Professionals
│
▼
LLM Compatibility Evaluation
│
▼
Ranking Engine
│
▼
Display Top Matches
│
▼
User Approval
│
▼
Messaging MCP
│
▼
Send Email


---

## Tech Stack

| Layer | Technology |
|------|-------------|
| Agent Orchestration | LangGraph |
| LLM Integration | OpenRouter |
| Backend | Python |
| Database | MongoDB Atlas |
| Messaging Interface | Telegram Bot API |
| Deployment | Render |
| Email Integration | SMTP |
| Data Layer | Synthetic professional profiles |

---

## Project Structure


locay_referrals/
│
├── agents/ # Agent logic
├── workflows/ # LangGraph workflow
├── services/
│ ├── compatibility_engine.py
│ ├── ranking_engine.py
│
├── tools/
│ ├── search_professionals_tool.py
│ └── mcp/
│ └── messaging_mcp.py
│
├── database/
│ ├── mongo_client.py
│ └── professional_repository.py
│
├── telegram_interface/
│ └── telegram_bot.py
│
├── memory/
│ └── conversation_memory.py
│
├── data_generation/
│ ├── generate_profiles.py
│ └── insert_profiles.py
│
├── main.py
├── requirements.txt
└── .python-version


---

## Features

- Natural language networking queries
- Location-aware professional discovery
- LLM-powered compatibility scoring
- Autonomous candidate ranking
- Messaging MCP for real-world outreach
- Telegram conversational interface
- Cloud deployment

---

## Deployment Architecture


Telegram
│
▼
Render Web Service
│
▼
LangGraph Agent
│
▼
MongoDB Atlas
│
▼
LLM Compatibility Engine
│
▼
Ranking Engine
│
▼
Messaging MCP
│
▼
SMTP Email


---

## Running Locally

Install dependencies:


pip install -r requirements.txt


Run the Telegram bot:


python telegram_interface/telegram_bot.py


---

## Environment Variables


TELEGRAM_BOT_TOKEN=
OPENROUTER_API_KEY=
MONGO_URI=
SMTP_SERVER=
SMTP_PORT=
SMTP_EMAIL=
SMTP_PASSWORD=


---

## Future Improvements

- Redis conversation memory
- Smart intent classification
- Real LinkedIn integrations
- Calendar scheduling MCP
- Multi-agent workflow architecture
- Vector search for semantic profile matching

---

## Author

Nischal Mogalapalli  
Automation Engineer transitioning into **Agentic AI Systems Engineering**

---
Flowchart for Your YouTube Video

You can explain the system using this flow.

User sends message in Telegram
        │
        ▼
Telegram Bot receives query
        │
        ▼
LangGraph Agent Workflow starts
        │
        ▼
Query Parser extracts
(city, role, company tier)
        │
        ▼
MongoDB Atlas search
        │
        ▼
Candidate profiles returned
        │
        ▼
LLM Compatibility Engine
evaluates user vs candidate
        │
        ▼
Ranking Engine selects top matches
        │
        ▼
Bot returns top candidates
        │
        ▼
User approves outreach
        │
        ▼
Messaging MCP sends email
High-Level Architecture Diagram
                +--------------------+
                | Telegram User      |
                +----------+---------+
                           |
                           ▼
                 +------------------+
                 | Telegram Bot     |
                 +---------+--------+
                           |
                           ▼
                 +------------------+
                 | LangGraph Agent  |
                 +---------+--------+
                           |
        +------------------+------------------+
        |                                     |
        ▼                                     ▼
+---------------+                    +----------------------+
| MongoDB Atlas |                    | LLM Compatibility    |
| Professional  |                    | Engine               |
| Profiles      |                    +----------------------+
+---------------+                                |
        |                                         |
        +----------------+------------------------+
                         ▼
                +--------------------+
                | Ranking Engine     |
                +---------+----------+
                          |
                          ▼
                 +-------------------+
                 | Messaging MCP     |
                 +---------+---------+
                           |
                           ▼
                     +-----------+
                     | Email     |
                     +-----------+
