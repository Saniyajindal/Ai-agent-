import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
from database import ORDERS_DB
from tools import (
    get_order_details,
    check_return_eligibility,
    initiate_return,
    cancel_order,
    update_shipping_address,
    escalate_to_human
)

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

tools_list = [
    get_order_details,
    check_return_eligibility,
    initiate_return,
    cancel_order,
    update_shipping_address,
    escalate_to_human
]

SYSTEM_PROMPT = """
You are an intelligent e-commerce Customer Support Agent.
Guidelines:
1. Always look up the order details first when a customer inquires about an order.
2. Before initiating any return, verify eligibility using check_return_eligibility.
3. For cancellations, use cancel_order. Note that shipped or delivered orders cannot be cancelled directly.
4. For address updates, use update_shipping_address. Address can only be changed before the order is shipped.
5. If an order operation is not permitted by policy, politely explain the exact reason and offer escalation if requested.
6. Keep answers concise, factual, and polite. Never make assumptions without querying the tools.
"""

def run_agent_chat():
    chat = client.chats.create(
        model="gemini-3.8-flash",
        config=types.GenerateContentConfig(
            system_instruction=SYSTEM_PROMPT,
            tools=tools_list,
            temperature=0.2
        )
    )
    return chat