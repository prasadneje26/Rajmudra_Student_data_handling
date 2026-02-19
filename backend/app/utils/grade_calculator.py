def calculate_grade(percentage: float) -> dict:
    """
    Calculates grade and pass/fail result based on percentage
    Returns dict: {"grade": str, "result": str}
    """
    if percentage >= 90:
        grade = "A+"
    elif percentage >= 75:
        grade = "A"
    elif percentage >= 60:
        grade = "B"
    elif percentage >= 50:
        grade = "C"
    else:
        grade = "F"

    result = "Pass" if percentage >= 50 else "Fail"
    return {"grade": grade, "result": result}
