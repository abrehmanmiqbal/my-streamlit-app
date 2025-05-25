import streamlit as st
from utils import generate_tasks, generate_nodes, simulate_mobility
from blockchain import Blockchain
from scheduler import schedule_tasks

st.set_page_config(page_title="VFCN Scheduler", layout="wide")

st.title("🚗 Mobility Aware Blockchain Enabled Task Scheduler")
st.markdown("### A Final Year Project combining AI, Blockchain, and Smart Scheduling for Vehicular Fog Computing")

# Session State
if 'tasks' not in st.session_state:
    st.session_state.tasks = generate_tasks()
if 'nodes' not in st.session_state:
    st.session_state.nodes = generate_nodes()
if 'blockchain' not in st.session_state:
    st.session_state.blockchain = Blockchain()

# Simulate Mobility
if st.button("📍 Simulate Mobility"):
    simulate_mobility(st.session_state.nodes)
    st.success("🚗 Nodes moved successfully!")

# Display Nodes
st.markdown("## 🛰️ Fog Nodes (After Mobility)")
with st.expander("Click to View Node Details"):
    st.table([vars(node) for node in st.session_state.nodes])

# Display Tasks
st.markdown("## 📋 Incoming Tasks")
with st.expander("Click to View Task List"):
    st.table([vars(task) for task in st.session_state.tasks])

# Handle Secure Tasks
for task in st.session_state.tasks:
    if task.is_secure:
        best_node = max(st.session_state.nodes, key=lambda x: x.credibility)
        st.session_state.blockchain.add_secure_task(task, credibility=best_node.credibility)

# Schedule Tasks
assignments = schedule_tasks(st.session_state.tasks, st.session_state.nodes)
st.markdown("## ⚙️ Task Assignments")
st.dataframe([{
    'Task': a[0],
    'Assigned Node': a[1],
    'Estimated Time': f"{a[2]:.2f} sec"
} for a in assignments])

# Show Blockchain
st.markdown("## 🔐 Blockchain Ledger (For Secure Tasks)")
for i, block in enumerate(st.session_state.blockchain.chain, start=1):
    with st.expander(f"Block #{i}"):
        st.json(block)

# Footer
st.markdown("---")
st.markdown("**Developed by: ABD | DUET Final Year Project | Supervised by: [Engr. Raheela Shah]**")
