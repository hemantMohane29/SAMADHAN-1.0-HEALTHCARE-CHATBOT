"""Utility functions for the HealthGPT application."""

import html
from typing import Dict, List
import streamlit as st
from langchain_ollama import ChatOllama
from config import MODEL_CONFIG

def sanitize_message(text: str) -> str:
    """Sanitize message content and convert newlines to HTML line breaks."""
    sanitized = html.escape(text)
    return sanitized.replace('\n', '<br>')

def generate_healthcare_prompt(input_text: str, user_data: Dict) -> str:
    """Generate a healthcare-specific prompt with user context."""
    return (
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

def get_ai_response(input_text: str, user_data: Dict) -> str:
    """Generate AI response using the chat model."""
    try:
        model = ChatOllama(
            model=MODEL_CONFIG["name"],
            base_url=MODEL_CONFIG["base_url"]
        )
        prompt = generate_healthcare_prompt(input_text, user_data)
        response = model.invoke(prompt)
        return response.content
    except Exception as e:
        st.error(f"Error generating response: {str(e)}")
        return "I apologize, but I'm having trouble generating a response right now. Please try again in a moment."

def format_chat_message(message: Dict) -> str:
    """Format chat message with appropriate styling."""
    role = message["role"]
    content = message["content"]
    
    if role == "assistant":
        return f'<div class="chat-message assistant"><div class="avatar">🏥</div><div class="message">{content}</div></div>'
    else:
        return f'<div class="chat-message user"><div class="avatar">👤</div><div class="message">{content}</div></div>'

def validate_user_profile(profile: Dict) -> List[str]:
    """Validate user profile data and return list of errors if any."""
    errors = []
    required_fields = ["name", "age", "gender"]
    
    for field in required_fields:
        if not profile.get(field):
            errors.append(f"{field.capitalize()} is required")
    
    if profile.get("age"):
        try:
            age = int(profile["age"])
            if age < 0 or age > 120:
                errors.append("Age must be between 0 and 120")
        except ValueError:
            errors.append("Age must be a number")
            
    return errors
