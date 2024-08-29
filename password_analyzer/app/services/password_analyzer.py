import re
from zxcvbn import zxcvbn

def analyze_password(password: str):
    # Basic checks
    length = len(password)
    has_uppercase = bool(re.search(r'[A-Z]', password))
    has_lowercase = bool(re.search(r'[a-z]', password))
    has_digit = bool(re.search(r'\d', password))
    has_special = bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password))

    # Calculate base score
    score = 0
    if length >= 8:
        score += 1
    if length >= 12:
        score += 1
    if has_uppercase:
        score += 1
    if has_lowercase:
        score += 1
    if has_digit:
        score += 1
    if has_special:
        score += 1

    # Use zxcvbn for advanced analysis
    zxcvbn_result = zxcvbn(password)
    
    # Combine scores (zxcvbn score is 0-4)
    final_score = min(score + zxcvbn_result['score'], 10)

    # Generate feedback
    feedback = []
    if length < 8:
        feedback.append("Password is too short. Use at least 8 characters.")
    if not has_uppercase:
        feedback.append("Include uppercase letters.")
    if not has_lowercase:
        feedback.append("Include lowercase letters.")
    if not has_digit:
        feedback.append("Include numbers.")
    if not has_special:
        feedback.append("Include special characters.")

    # Add zxcvbn feedback
    feedback.extend(zxcvbn_result['feedback']['suggestions'])

    return {
        "score": final_score,
        "strength": get_strength_label(final_score),
        "feedback": feedback
    }

def get_strength_label(score):
    if score < 3:
        return "Very Weak"
    elif score < 5:
        return "Weak"
    elif score < 7:
        return "Moderate"
    elif score < 9:
        return "Strong"
    else:
        return "Very Strong"