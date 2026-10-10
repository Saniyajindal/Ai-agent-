# 📦 E-Commerce Autonomous Support & Order Operations Agent

An autonomous AI agent built from scratch using Python, Google Gemini (Tool Calling), and Streamlit. The agent handles customer support inquiries, enforces business policies deterministically, updates order states in real time, and escalates edge cases to human representatives.

---

## 🎯 Problem Statement
E-commerce support teams spend substantial time on repetitive order queries—checking tracking statuses, validating return windows, processing cancellations, and modifying addresses. Traditional chatbots rely on static rule trees or hallucinate answers, while raw LLMs lack the ability to take actions.

This project bridges that gap by combining:
1. **LLM Reasoning (Gemini):** Understands natural language user intent and decides which tools to invoke.
2. **Deterministic Code/Tools:** Executes strict business policies (e.g., 7-day return window, cancellation restrictions for dispatched items).
3. **Live State Mutation:** Updates database records dynamically with real-time UI reflection.

---

## 🚀 Key Features

* **Order Status & Tracking:** Queries mock database records and retrieves item, shipment, and delivery details.
* **Policy-Enforced Returns:** Evaluates delivery date against the 7-day return window; initiates return workflows only for eligible orders.
* **Order Cancellation:** Allows cancellation for orders in `PROCESSING` state; blocks cancellation once items are marked `SHIPPED`.
* **Shipping Address Updates:** Updates delivery destination prior to dispatch; restricts modifications on in-transit or delivered orders.
* **Human-in-the-Loop Escalation:** Creates support tickets and escalates when automated policies cannot resolve the customer's request.
* **Interactive Web Dashboard:** Real-time chat interface paired with a live-updating database sidebar built in Streamlit.

---

## 🏗️ Architecture & Agent Workflow
