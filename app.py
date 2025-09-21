import streamlit as st
from commands import handle_command

st.title("🔹 PyTerminal Web Edition")

# Initialize command history in session state
if "history" not in st.session_state:
    st.session_state.history = []

# Use a form so input clears after submitting
with st.form(key="terminal_form", clear_on_submit=True):
    cmd = st.text_input("Enter command:")
    submit = st.form_submit_button("Run")

if submit and cmd:
    output = handle_command(cmd)
    st.session_state.history.append(f"> {cmd}\n{output}")

# Display terminal output
st.text_area("Terminal Output", value="\n".join(st.session_state.history), height=400)
