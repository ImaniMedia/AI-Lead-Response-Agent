
# AI Lead Response Agent for Local Businesses (n8n + AI Agents Automation)

## Description
This project automates lead follow-ups for local businesses using AI Agents and n8n workflows.
It captures inquiries from websites, emails, or social media, responds instantly with a personalized message, and notifies the business owner.

## Features
- Detect new inquiries (Website Forms, LinkedIn, Email)
- Analyze intent and urgency using AI
- Auto-generate a personalized response
- Notify business owner via WhatsApp/Email
- No-code workflow with n8n

## Stack Used
- n8n (No-code automation platform)
- OpenAI API / Local LLMs
- Webhooks & API Integrations
- Node.js / Python for light scripting

## Workflow Overview
1. Lead submits an inquiry.
2. n8n captures it via webhook or email trigger.
3. AI Agent identifies lead's intent.
4. Generates and sends an immediate personalized response.
5. Notifies the business owner via WhatsApp.

## Result
- Faster response times = More booked clients
- Business owner focuses on core work while AI handles inquiries
- Simple and scalable automation setup

## Quick Start
1. Import `n8n-Workflow.json` into your n8n instance.
2. Set up your environment variables using `.env.example`.
3. Deploy the Python scripts in `agent_logic/`.
4. Configure API keys and endpoints in `integrations/` files.
5. Start n8n and watch your AI Agent handle leads instantly!

