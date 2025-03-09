import streamlit as st
import random
import string

COMMON_PASSWORDS = [
    "password", "123456", "123456789", "qwerty", "abc123",
    "password123", "111111", "letmein", "welcome", "admin"
]

SPECIAL_CHARACTERS = "!@#$%^&*()_-+=<>?/|}{~:]"
MIN_LENGTH = 8

st.set_page_config(page_title="Advanced Password Strength Meter", layout="centered")

st.title("🔐 Advanced Password Strength Meter")
st.write("Check your password strength and get suggestions to improve it!")

# Password Input
password = st.text_input("Enter your password", type="password")

# Password Strength Evaluation Function
def evaluate_password(password: str) -> (int, str, list):
    score = 0
    suggestions = []

    # Check length
    if len(password) >= MIN_LENGTH:
        score += 1
    else:
        suggestions.append(f"Make your password at least {MIN_LENGTH} characters long.")
    
    # Check for uppercase and lowercase
    if any(c.islower() for c in password) and any(c.isupper() for c in password):
        score += 1
    else:
        suggestions.append("Include both uppercase and lowercase letters.")
    
    # Check for digits
    if any(c.isdigit() for c in password):
        score += 1
    else:
        suggestions.append("Add at least one digit (0-9).")
    
    # Check for special characters
    if any(c in SPECIAL_CHARACTERS for c in password):
        score += 1
    else:
        suggestions.append("Include special characters (!@#$%^&*).")
    
    # Check against common passwords
    if password.lower() not in COMMON_PASSWORDS:
        score += 1
    else:
        suggestions.append("Avoid using common passwords like 'password123' or 'qwerty'.")

    # Determine strength level
    if score <= 2:
        strength = "Weak"
        st.error("Your password is weak. Try the following suggestions:")
    elif score <= 4:
        strength = "Moderate"
        st.warning("Your password is moderate. Consider the suggestions below:")
    else:
        strength = "Strong"
        st.success("Your password is strong!")

    return score, strength, suggestions

# Password Evaluation
if password:
    score, strength, suggestions = evaluate_password(password)
    
    st.write(f"**Password Strength:** {strength} (Score: {score}/5)")
    
    if suggestions:
        st.write("### Suggestions to Improve Your Password:")
        for suggestion in suggestions:
            st.write(f"- {suggestion}")

def generate_password(length: int = 12) -> str:
    if length < MIN_LENGTH:
        length = MIN_LENGTH
    
    characters = string.ascii_letters + string.digits + SPECIAL_CHARACTERS
    return ''.join(random.choice(characters) for i in range(length))

# Password Generator
st.markdown("---")
st.write("### Need a Strong Password?")
password_length = st.slider("Select Password Length", 8, 32, 12)
if st.button("Generate Strong Password"):
    generated_password = generate_password(password_length)
    st.text_input("Generated Password", generated_password, type="default")

if password:
    st.markdown("---")
    st.write("### Password Strength Meter")
    st.progress(score / 5)