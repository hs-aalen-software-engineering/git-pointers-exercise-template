"""
Automated tests for Git Pointers Exercise

This file uses hash-based verification to prevent students from easily
reading the correct answers. Answers are hashed with SHA256.
"""

import hashlib
import pytest
from answers import get_answers, validate_answers

# Salt used for hashing (makes rainbow table attacks harder)
_SALT = "git-pointers-exercise-template-2025"

# TODO: Fill in the SHA256 hashes for correct answers
# To generate a hash for an answer:
#   python -c "import hashlib; print(hashlib.sha256(b'1Agit-pointers-exercise-template-2025').hexdigest())"
# Format: "{question_number}{answer}{salt}"
# Example: For Q1 with answer "A": "1Agit-pointers-exercise-template-2025"
_ANSWER_HASHES = {
    1: "",  # Question 1: TODO - Add hash for correct answer
    2: "",  # Question 2: TODO - Add hash for correct answer
    3: "",  # Question 3: TODO - Add hash for correct answer
    4: "",  # Question 4: TODO - Add hash for correct answer
    5: "",  # Question 5: TODO - Add hash for correct answer
    6: "",  # Question 6: TODO - Add hash for correct answer
    7: "",  # Question 7: TODO - Add hash for correct answer
    8: "",  # Question 8: TODO - Add hash for correct answer
    9: "",  # Question 9: TODO - Add hash for correct answer
    10: "",  # Question 10: TODO - Add hash for correct answer
    11: "",  # Question 11: TODO - Add hash for correct answer
    12: "",  # Question 12: TODO - Add hash for correct answer
    13: "",  # Question 13: TODO - Add hash for correct answer
    14: "",  # Question 14: TODO - Add hash for correct answer
    15: "",  # Question 15: TODO - Add hash for correct answer
}


def _verify_answer(question_num: int, student_answer: str) -> bool:
    """
    Verify student answer by comparing hashes.

    Args:
        question_num: Question number (1-indexed)
        student_answer: Student's answer (A, B, C, or D)

    Returns:
        True if answer is correct, False otherwise
    """
    if not student_answer:
        return False

    # Create hash input: question number + answer + salt
    hash_input = f"{question_num}{student_answer.upper()}{_SALT}".encode()
    student_hash = hashlib.sha256(hash_input).hexdigest()

    expected_hash = _ANSWER_HASHES.get(question_num, "")
    return student_hash == expected_hash


def test_answers_are_valid():
    """Test that all answers are properly formatted."""
    is_valid, message = validate_answers()
    assert is_valid, message

def test_question_1():
    """Question 1"""
    student_answers = get_answers()
    assert _verify_answer(1, student_answers[1]), \
        "Incorrect answer for Question 1"

def test_question_2():
    """Question 2"""
    student_answers = get_answers()
    assert _verify_answer(2, student_answers[2]), \
        "Incorrect answer for Question 2"

def test_question_3():
    """Question 3"""
    student_answers = get_answers()
    assert _verify_answer(3, student_answers[3]), \
        "Incorrect answer for Question 3"

def test_question_4():
    """Question 4"""
    student_answers = get_answers()
    assert _verify_answer(4, student_answers[4]), \
        "Incorrect answer for Question 4"

def test_question_5():
    """Question 5"""
    student_answers = get_answers()
    assert _verify_answer(5, student_answers[5]), \
        "Incorrect answer for Question 5"

def test_question_6():
    """Question 6"""
    student_answers = get_answers()
    assert _verify_answer(6, student_answers[6]), \
        "Incorrect answer for Question 6"

def test_question_7():
    """Question 7"""
    student_answers = get_answers()
    assert _verify_answer(7, student_answers[7]), \
        "Incorrect answer for Question 7"

def test_question_8():
    """Question 8"""
    student_answers = get_answers()
    assert _verify_answer(8, student_answers[8]), \
        "Incorrect answer for Question 8"

def test_question_9():
    """Question 9"""
    student_answers = get_answers()
    assert _verify_answer(9, student_answers[9]), \
        "Incorrect answer for Question 9"

def test_question_10():
    """Question 10"""
    student_answers = get_answers()
    assert _verify_answer(10, student_answers[10]), \
        "Incorrect answer for Question 10"

def test_question_11():
    """Question 11"""
    student_answers = get_answers()
    assert _verify_answer(11, student_answers[11]), \
        "Incorrect answer for Question 11"

def test_question_12():
    """Question 12"""
    student_answers = get_answers()
    assert _verify_answer(12, student_answers[12]), \
        "Incorrect answer for Question 12"

def test_question_13():
    """Question 13"""
    student_answers = get_answers()
    assert _verify_answer(13, student_answers[13]), \
        "Incorrect answer for Question 13"

def test_question_14():
    """Question 14"""
    student_answers = get_answers()
    assert _verify_answer(14, student_answers[14]), \
        "Incorrect answer for Question 14"

def test_question_15():
    """Question 15"""
    student_answers = get_answers()
    assert _verify_answer(15, student_answers[15]), \
        "Incorrect answer for Question 15"

def test_calculate_score():
    """Calculate and display the final score."""
    student_answers = get_answers()
    correct_count = sum(
        1 for q in range(1, 16)
        if _verify_answer(q, student_answers[q])
    )

    percentage = (correct_count / 15) * 100

    print(f"\n{'='*50}")
    print(f"FINAL SCORE: {correct_count}/15 ({percentage:.1f}%)")
    print(f"{'='*50}")

    if correct_count >= 13:
        print("🏆 Excellent! You have a strong understanding!")
    elif correct_count >= 10:
        print("👍 Good understanding! Review key concepts.")
    elif correct_count >= 7:
        print("📖 Fair understanding. Please review the lecture.")
    else:
        print("🔄 Please review the lecture and try again.")

    print(f"{'='*50}\n")

    # This test always passes, but displays the score
    assert True
