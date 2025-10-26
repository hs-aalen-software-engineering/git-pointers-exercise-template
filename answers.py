"""
Git Pointers Exercise - Answer Submission

Instructions:
1. Fill in your answers for all 15 questions below
2. Each answer should be "A", "B", "C", or "D"
3. Commit and push your changes
4. GitHub Actions will automatically grade your submission

Example:
    answers = {
        1: "A",
        2: "D",
        3: "B",
        # ... and so on
    }
"""

# Student Information (optional)
student_name = "Your Name Here"
student_id = "Your Student ID Here"

# Your Answers (fill in all 15 questions)
answers = {
    1: "",  # Question 1
    2: "",  # Question 2
    3: "",  # Question 3
    4: "",  # Question 4
    5: "",  # Question 5
    6: "",  # Question 6
    7: "",  # Question 7
    8: "",  # Question 8
    9: "",  # Question 9
    10: "",  # Question 10
    11: "",  # Question 11
    12: "",  # Question 12
    13: "",  # Question 13
    14: "",  # Question 14
    15: "",  # Question 15
}

# Do not modify below this line
# ================================

def get_answers():
    """
    Returns the student's answers.
    Used by the autograding system.
    """
    return answers

def validate_answers():
    """
    Validates that all answers are filled in and properly formatted.
    """
    valid_options = {"A", "B", "C", "D"}

    if len(answers) != 15:
        return False, f"Expected 15 answers, found {len(answers)}"

    for q_num in range(1, 16):
        if q_num not in answers:
            return False, f"Missing answer for question {q_num}"

        answer = answers[q_num]
        if not isinstance(answer, str):
            return False, f"Question {q_num}: Answer must be a string"

        if answer.upper() not in valid_options:
            return False, f"Question {q_num}: Answer must be A, B, C, or D (found: '{answer}')"

    return True, "All answers are properly formatted"

if __name__ == "__main__":
    is_valid, message = validate_answers()
    if is_valid:
        print("✅ " + message)
        print(f"\nYour answers:")
        for q, ans in sorted(answers.items()):
            print(f"  Question {q:2d}: {ans}")
    else:
        print("❌ " + message)
        exit(1)
