import streamlit as st
import pandas as pd
from agent import run_agent_chat
from database import ORDERS_DB

st.set_page_config(
    page_title="Order Operations AI Agent",
    page_icon="📦",
    layout="wide"
)

st.title("📦 E-Commerce Autonomous Support Agent")
st.caption("Powered by Gemini Tool-Calling & Deterministic Business Policies")

# Initialize Chat in session state
if "chat" not in st.session_state:
    st.session_state.chat = run_agent_chat()

if "messages" not in st.session_state:
    st.session_state.messages = []

# --- Sidebar: Live Database View ---
with st.sidebar:
    st.header("📊 Live Orders Database")
    st.caption("Jab agent koi action lega, yahan data real-time update hoga.")
    
    db_records = list(ORDERS_DB.values())
    df = pd.DataFrame(db_records)[["order_id", "item_name", "status", "return_status", "delivery_date"]]
    st.dataframe(df, use_container_width=True, hide_index=True)

    st.divider()
    st.markdown("**Test Scenarios:**")
    st.markdown("- *'Where is my order ORD-102?'*")
    st.markdown("- *'Return ORD-101 because it is defective.'*")
    st.markdown("- *'Can I return ORD-103?'*")

    if st.button("Clear Conversation", use_container_width=True):
        st.session_state.messages = []
        st.session_state.chat = run_agent_chat()
        st.rerun()

# --- Main Chat Area ---
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

user_input = st.chat_input("Ask about an order, initiate return, or track shipment...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    with st.chat_message("assistant"):
        with st.spinner("Agent is reasoning and executing tools..."):
            try:
                response = st.session_state.chat.send_message(user_input)
                agent_reply = response.text
                st.markdown(agent_reply)
                st.session_state.messages.append({"role": "assistant", "content": agent_reply})
                st.rerun()
            except Exception as e:
                st.error(f"Error: {e}")