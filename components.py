"""UI components for the HealthGPT application."""

import streamlit as st
from typing import Dict, List, Callable
from utils import validate_user_profile

def render_sidebar(user_data: Dict, on_profile_update: Callable) -> None:
    """Render the sidebar with user profile information."""
    with st.sidebar:
        st.title("User Profile")
        
        # User information form
        with st.form("user_profile"):
            name = st.text_input("Name", value=user_data.get("name", ""))
            age = st.text_input("Age", value=user_data.get("age", ""))
            gender = st.selectbox(
                "Gender",
                options=["", "Male", "Female", "Other"],
                index=0 if not user_data.get("gender") else ["", "Male", "Female", "Other"].index(user_data["gender"])
            )
            
            # Multi-select fields
            conditions = st.multiselect(
                "Medical Conditions",
                options=["Diabetes", "Hypertension", "Asthma", "Heart Disease", "Other"],
                default=user_data.get("conditions", [])
            )
            
            medications = st.multiselect(
                "Current Medications",
                options=["None", "Blood Pressure", "Diabetes", "Asthma", "Other"],
                default=user_data.get("medications", [])
            )
            
            allergies = st.multiselect(
                "Allergies",
                options=["None", "Penicillin", "Pollen", "Nuts", "Other"],
                default=user_data.get("allergies", [])
            )
            
            last_checkup = st.date_input(
                "Last Medical Checkup",
                value=None if not user_data.get("last_checkup") else user_data["last_checkup"]
            )
            
            if st.form_submit_button("Update Profile"):
                updated_profile = {
                    "name": name,
                    "age": age,
                    "gender": gender,
                    "conditions": conditions,
                    "medications": medications,
                    "allergies": allergies,
                    "last_checkup": last_checkup
                }
                
                errors = validate_user_profile(updated_profile)
                if errors:
                    for error in errors:
                        st.error(error)
                else:
                    on_profile_update(updated_profile)
                    st.success("Profile updated successfully!")

def render_chat_interface() -> str:
    """Render the chat interface and return user input."""
    # Chat interface
    st.markdown('<div class="chat-container" id="chat-container"></div>', unsafe_allow_html=True)
    
    # Text input with send button
    text = st.text_input(
        "Message HealthGPT...",
        key="user_input",
        placeholder="Type your health-related question here..."
    )
    
    return text

def render_chat_history(chat_history: List[Dict]) -> None:
    """Render the chat history with proper formatting."""
    chat_html = ""
    for message in chat_history:
        if message["role"] == "assistant":
            avatar = "🏥"
            css_class = "assistant"
        else:
            avatar = "👤"
            css_class = "user"
            
        chat_html += f'''
            <div class="chat-message {css_class}">
                <div class="avatar">{avatar}</div>
                <div class="message">{message["content"]}</div>
            </div>
        '''
    
    st.markdown(chat_html, unsafe_allow_html=True)
