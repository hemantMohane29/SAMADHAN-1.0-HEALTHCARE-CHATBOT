import streamlit as st
import datetime
from langchain_ollama import ChatOllama
import html

# Configure page settings
st.set_page_config(
    page_title="HealthGPT - Your AI Health Assistant",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Define generate_response function
def generate_response(input_text, user_data):
    model = ChatOllama(model="gpt-oss:120b-cloud", base_url="http://localhost:11434/")
    try:
        healthcare_prompt = (
            f"You are HealthGPT, an AI healthcare assistant. Provide accurate, concise healthcare-related responses.\n"
            f"User Details:\n"
            f"Name: {user_data['name']}\n"
            f"Age: {user_data['age']}\n"
            f"Gender: {user_data['gender']}\n"
            f"Conditions: {', '.join(user_data['conditions'])}\n"
            f"Medications: {', '.join(user_data['medications'])}\n"
            f"Allergies: {', '.join(user_data['allergies'])}\n"
            f"Last Checkup: {user_data['last_checkup']}\n"
            f"Question: {input_text}"
        )
        response = model.invoke(healthcare_prompt)
        return response.content 
    except Exception as e:
        return f"Error generating response: {e}"

# Modern UI Styling
st.markdown("""
    <style>
    /* Global Styles */
    :root {
        --primary-color: #3b82f6;
        --secondary-color: #1d4ed8;
        --accent-color: #60a5fa;
        --background-color: #0f172a;
        --surface-color: #1e293b;
        --text-color: #e2e8f0;
        --text-color-secondary: #94a3b8;
        --border-color: #334155;
        --hover-color: #2563eb;
    }

    .stApp {
        background: var(--background-color);
        color: var(--text-color);
    }

    /* Header Styles */
    .main-header {
        background: linear-gradient(135deg, var(--primary-color), var(--secondary-color));
        color: white;
        padding: 2rem;
        border-radius: 20px;
        margin-bottom: 2rem;
        text-align: center;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.3);
    }

    .main-header h1 {
        font-size: 2.5rem;
        margin-bottom: 0.5rem;
        font-weight: 700;
        text-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
    }

    .main-header p {
        font-size: 1.2rem;
        opacity: 0.9;
    }

    /* Sidebar Styling */
    section[data-testid="stSidebar"] {
        background-color: var(--surface-color);
        border-right: 1px solid var(--border-color);
    }

    .sidebar-content {
        padding: 1rem;
        background: var(--surface-color);
    }

    /* Chat Container Styling */
    .chat-container {
        background: var(--surface-color);
        border-radius: 20px;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
        margin: 1rem 0;
        padding: 1rem;
        overflow: hidden;
        max-width: 1200px;
        margin: 0 auto;
    }

    /* Message Wrapper Styling */
    .message-wrapper {
        display: flex;
        gap: 1rem;
        padding: 1.25rem;
        margin: 1rem 0;
        border-radius: 1rem;
        background: var(--surface-color);
        transition: all 0.3s ease;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    }

    .message-wrapper.user {
        margin-left: 2rem;
        background: linear-gradient(135deg, rgba(59, 130, 246, 0.1), rgba(37, 99, 235, 0.1));
        border-left: 4px solid var(--primary-color);
    }

    .message-wrapper.assistant {
        margin-right: 2rem;
        background: linear-gradient(135deg, rgba(16, 185, 129, 0.1), rgba(5, 150, 105, 0.1));
        border-left: 4px solid var(--secondary-color);
    }

    /* Message Icon */
    .message-icon {
        flex-shrink: 0;
        width: 40px;
        height: 40px;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 1.5rem;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.15);
        transition: all 0.3s ease;
    }

    .message-icon.user {
        background: linear-gradient(135deg, var(--primary-color), var(--accent-color));
    }

    .message-icon.assistant {
        background: linear-gradient(135deg, var(--secondary-color), var(--accent-color));
    }

    .message-wrapper:hover .message-icon {
        transform: scale(1.1);
    }

    /* Message Content */
    .message-content-wrapper {
        flex: 1;
        display: flex;
        flex-direction: column;
        gap: 0.5rem;
    }

    .message-header {
        display: flex;
        justify-content: space-between;
        align-items: center;
        color: var(--text-color-secondary);
        font-size: 0.875rem;
    }

    .message-role {
        font-weight: 600;
        color: var(--accent-color);
    }

    .message-time {
        font-size: 0.75rem;
        opacity: 0.7;
    }

    .message-content {
        color: var(--text-color);
        line-height: 1.6;
        font-size: 1rem;
        padding: 0.5rem;
        background: rgba(0, 0, 0, 0.1);
        border-radius: 0.5rem;
    }

    /* Typing Indicator */
    .typing-indicator {
        display: flex;
        gap: 0.5rem;
        padding: 1rem;
        align-items: center;
    }

    .typing-dot {
        width: 8px;
        height: 8px;
        background: var(--accent-color);
        border-radius: 50%;
        animation: bounce 1.5s infinite;
    }

    .typing-dot:nth-child(2) { animation-delay: 0.2s; }
    .typing-dot:nth-child(3) { animation-delay: 0.4s; }

    @keyframes bounce {
        0%, 60%, 100% { transform: translateY(0); }
        30% { transform: translateY(-6px); }
    }

    /* Chat Container */
    .main-content {
        max-width: 900px;
        margin: 0 auto;
        padding: 2rem;
        background: var(--background-color);
        border-radius: 1rem;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.2);
    }

    /* Animations */
    .message-wrapper {
        animation: slideIn 0.3s ease-out;
    }

    @keyframes slideIn {
        from {
            opacity: 0;
            transform: translateY(20px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }

    /* Input Area Styling */
    .stTextInput > div > div {
        position: relative !important;
    }

    .stTextInput > div > div > input {
        background-color: var(--surface-color) !important;
        color: var(--text-color) !important;
        border: 1px solid var(--border-color) !important;
        border-radius: 12px !important;
        padding-right: 45px !important;
        height: 48px !important;
        font-size: 1rem !important;
        width: 100% !important;
    }

    .stTextInput > div > div > input:focus {
        border-color: var(--primary-color) !important;
        box-shadow: 0 0 0 1px var(--primary-color) !important;
    }

    /* Send Icon Button */
    .send-button {
        position: absolute !important;
        right: 8px !important;
        top: 50% !important;
        transform: translateY(-50%) !important;
        background: transparent !important;
        border: none !important;
        width: 32px !important;
        height: 32px !important;
        padding: 6px !important;
        cursor: pointer !important;
        z-index: 999999 !important;
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
        border-radius: 8px !important;
        transition: all 0.2s ease !important;
    }

    .send-button:hover {
        background: rgba(59, 130, 246, 0.1) !important;
    }

    .send-button svg {
        width: 20px !important;
        height: 20px !important;
        fill: var(--primary-color) !important;
    }

    .send-button:hover svg {
        fill: var(--accent-color) !important;
    }

    /* Hide default button */
    .stButton {
        display: none !important;
    }

    /* Dashboard Cards */
    .dashboard-card {
        background: var(--surface-color);
        border: 1px solid var(--border-color);
        border-radius: 15px;
        padding: 1.5rem;
        margin-bottom: 1rem;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }

    .dashboard-card:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 12px rgba(0, 0, 0, 0.15);
        border-color: var(--primary-color);
    }

    /* Streamlit Element Overrides */
    .stSelectbox label,
    .stMultiSelect label {
        color: var(--text-color) !important;
    }

    .stSelectbox > div[data-baseweb="select"] > div,
    .stMultiSelect > div[data-baseweb="select"] > div {
        background-color: var(--surface-color) !important;
        border-color: var(--border-color) !important;
    }

    .stMarkdown {
        color: var(--text-color);
    }

    /* Scrollbar Styling */
    ::-webkit-scrollbar {
        width: 10px;
        height: 10px;
    }

    ::-webkit-scrollbar-track {
        background: var(--surface-color);
    }

    ::-webkit-scrollbar-thumb {
        background: var(--border-color);
        border-radius: 5px;
    }

    ::-webkit-scrollbar-thumb:hover {
        background: var(--primary-color);
    }

    /* Medical Disclaimer */
    .medical-disclaimer {
        background: rgba(59, 130, 246, 0.1);
        border-left: 4px solid var(--accent-color);
        padding: 1rem;
        margin: 1rem 0;
        border-radius: 0 10px 10px 0;
    }

    .medical-disclaimer p {
        color: var(--text-color-secondary);
        font-size: 0.9rem;
        margin: 0;
    }
    </style>
""", unsafe_allow_html=True)

# Initialize session state
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

# User data dictionary
user_data = {
    "name": "Guest",
    "age": "",
    "gender": "",
    "conditions": [],
    "medications": [],
    "allergies": [],
    "last_checkup": None
}

# Main header
st.markdown("""
    <div class="main-header">
        <h1>🏥 HealthGPT</h1>
        <p>Your Intelligent Healthcare Assistant</p>
    </div>
""", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.image("logo.png", caption="HealthGPT")
    
    st.markdown('<div class="sidebar-content">', unsafe_allow_html=True)
    st.header("👤 Patient Profile")
    
    user_data["name"] = st.text_input("Full Name:", "Guest")
    user_data["age"] = st.number_input("Age:", min_value=0, max_value=120, step=1)
    user_data["gender"] = st.selectbox("Gender:", ["Select", "Male", "Female", "Other"])
    
    st.subheader("📋 Medical History")
    user_data["conditions"] = st.multiselect(
        "Medical Conditions:",
        ["Diabetes", "Hypertension", "Heart Disease", "Asthma", "Cancer", "Depression", "Anxiety", "Other"]
    )
    
    medications = st.text_area("Current Medications:")
    user_data["medications"] = [med.strip() for med in medications.split("\n") if med.strip()]
    
    allergies = st.text_area("Allergies:")
    user_data["allergies"] = [allergy.strip() for allergy in allergies.split("\n") if allergy.strip()]
    
    user_data["last_checkup"] = st.date_input("Last Medical Checkup:", datetime.date.today())
    st.markdown('</div>', unsafe_allow_html=True)

# Main chat interface
st.markdown('<div class="main-content">', unsafe_allow_html=True)

# Patient Dashboard
with st.expander("📊 Patient Dashboard", expanded=False):
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown('<div class="dashboard-card">', unsafe_allow_html=True)
        st.markdown(f"### 👤 Basic Info")
        st.write(f"**Name:** {user_data['name']}")
        st.write(f"**Age:** {user_data['age']}")
        st.write(f"**Gender:** {user_data['gender']}")
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        st.markdown('<div class="dashboard-card">', unsafe_allow_html=True)
        st.markdown("### 🏥 Medical Conditions")
        for condition in user_data['conditions']:
            st.write(f"• {condition}")
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col3:
        st.markdown('<div class="dashboard-card">', unsafe_allow_html=True)
        st.markdown("### 💊 Medications")
        for med in user_data['medications']:
            st.write(f"• {med}")
        st.markdown('</div>', unsafe_allow_html=True)

def sanitize_message(text):
    """Sanitize message content and convert newlines to <br> tags"""
    # Escape HTML special characters
    text = html.escape(text)
    # Convert newlines to <br> tags
    text = text.replace('\n', '<br>')
    return text

# Initialize session state for chat history if it doesn't exist
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = [
        {
            "role": "assistant",
            "content": "Hi! I'm HealthGPT, your AI health assistant. How can I help you today? Feel free to ask any health-related questions."
        }
    ]

# Chat container
for message in st.session_state.chat_history:
    message_role = message["role"]
    message_content = message["content"]
    timestamp = datetime.datetime.now().strftime("%I:%M %p")
    
    st.markdown(f"""
        <div class="message-wrapper {message_role}">
            <div class="message-icon {message_role}">
                {("👤" if message_role == "user" else "🏥")}
            </div>
            <div class="message-content-wrapper">
                <div class="message-header">
                    <span class="message-role">{message_role.title()}</span>
                    <span class="message-time">{timestamp}</span>
                </div>
                <div class="message-content">
                    {message_content}
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)

# Add typing indicator when generating response
if 'generating_response' in st.session_state and st.session_state.generating_response:
    st.markdown("""
        <div class="message-wrapper assistant">
            <div class="message-icon assistant">🏥</div>
            <div class="message-content-wrapper">
                <div class="typing-indicator">
                    <div class="typing-dot"></div>
                    <div class="typing-dot"></div>
                    <div class="typing-dot"></div>
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

def process_input():
    """Process user input and generate response"""
    if st.session_state.user_input.strip():
        text = st.session_state.user_input
        st.session_state.user_input = ""
        
        # Add user message to chat history
        st.session_state.chat_history.append({
            "role": "user",
            "content": text
        })
        
        # Set generating response state
        st.session_state.generating_response = True
        
        # Generate and add assistant response
        response = generate_response(text, user_data)
        
        # Clear generating response state
        st.session_state.generating_response = False
        
        st.session_state.chat_history.append({
            "role": "assistant",
            "content": response
        })

# Text input with integrated send icon
text = st.text_input("Message HealthGPT...", key="user_input", on_change=process_input)

# JavaScript to inject send button
st.markdown("""
    <script>
        function injectSendButton() {
            // Remove any existing send buttons
            const existingButtons = document.querySelectorAll('.send-button');
            existingButtons.forEach(button => button.remove());
            
            // Find the input container
            const inputContainer = document.querySelector('.stTextInput > div > div');
            if (!inputContainer) return;
            
            // Create and inject the send button
            const sendButton = document.createElement('button');
            sendButton.className = 'send-button';
            sendButton.innerHTML = `
                <svg viewBox="0 0 24 24">
                    <path d="M2.01 21L23 12 2.01 3 2 10l15 2-15 2z"/>
                </svg>
            `;
            
            // Add click handler
            sendButton.onclick = function(e) {
                e.preventDefault();
                const input = document.querySelector('.stTextInput input');
                if (input && input.value.trim()) {
                    input.dispatchEvent(new KeyboardEvent('keydown', {
                        key: 'Enter',
                        code: 'Enter',
                        keyCode: 13,
                        which: 13,
                        bubbles: true
                    }));
                }
            };
            
            inputContainer.appendChild(sendButton);
        }

        // Initial injection
        setTimeout(injectSendButton, 100);

        // Re-inject on Streamlit rerender
        const observer = new MutationObserver(function(mutations) {
            if (!document.querySelector('.send-button')) {
                injectSendButton();
            }
        });

        observer.observe(document.body, {
            childList: true,
            subtree: true
        });
    </script>
""", unsafe_allow_html=True)

# Medical disclaimer
st.markdown("""
    <div class="medical-disclaimer">
        <p>⚕️ <b>Medical Disclaimer:</b> HealthGPT is an AI assistant and should not be used as a substitute for professional medical advice, diagnosis, or treatment. Always seek the advice of your physician or other qualified health provider.</p>
    </div>
""", unsafe_allow_html=True)
