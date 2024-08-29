from app.services import password_analyzer

def test_password_strength():
    result = password_analyzer.analyze("password123")
    assert result["score"] < 5  # Weak password
    
    result = password_analyzer.analyze("P@ssw0rd123!")
    assert result["score"] > 7  # Strong password