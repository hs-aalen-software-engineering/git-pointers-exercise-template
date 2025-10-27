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
    1: "0a821a594fb9948199763532e800b20187e071083126e088676d4d975a0d6bd6",  # Question 1
    2: "d4c0cc80f4ace2cb8c1180a674d25194c9f093f9e3e25f2e60a83845298095c3",  # Question 2
    3: "25d18f41ce136783a221659bf1c0e05034ce2d5df10f851e88bb5ba41742c534",  # Question 3
    4: "3bd430174ae82f0f0fa2b2de589bd19dafb0a1992e75629bd689256304f225d5",  # Question 4
    5: "52d263bc03730e3c697275eb154c420b387a71a70e38202ad312d0ff8d028457",  # Question 5
    6: "5caced78aec30b64a341647b90199d46115a021ce540787042a72dd081073802",  # Question 6
    7: "abe8f01c7210829f7f49ca6761e90fb291f6be6ebac8e17974453079409cf145",  # Question 7
    8: "3406038041ce68623e3a6f89c0177ff45f38283c72822fca94b8feb451b44772",  # Question 8
    9: "48d707ea37d1f8a9a7d0c77ff000a8bdacdd93e262bd77b1247195e6fc387b0a",  # Question 9
    10: "d13e352541355e33c73dce9f44da24a2922bf8a1660ea26598ed58ac7760b42a",  # Question 10
    11: "3dbea71e02f64ec034745488527d48a649ceba810eaf324534f72505ed6db330",  # Question 11
    12: "eff0127871f31c02a25a1f5174007e29089adc69f0fa90f204dd4b104654ed77",  # Question 12
    13: "70f6a3f308c067ecfb8b8772c24d8f1928031cdcda00724fb8448538b9272bff",  # Question 13
    14: "63b0fa90bf4525dd0be0412385eb2f04bc30f3ea3d64a0dbd96e1bd109f51d3c",  # Question 14
    15: "ed69d7717e3d9bd5cf275bd76412ab803b4f8d338cd673d1686934184879cf12",  # Question 15
    16: "f468de3fc870ca38f30731769a1814b45ad8173d628b7f0a6d18567c534e1532",  # Question 16
    17: "d587740416b2ec3d67c9b873c43e78b4ec9a9f8f06d04dcf23ddeeaf54a56eb2",  # Question 17
    18: "c44abbbaf05ca88f28560a4e93ab5887f5871e027cf20cb6edfcf91273d797ce",  # Question 18
    19: "6df7ee43838424074f6aee866be3a8e240122c9180c4bca979cb8e5b362990ae",  # Question 19
    20: "4c27698304d785a9caeeda6a51b4d748b79338f8514aba523298c2a420c97c8a",  # Question 20
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

def test_question_16():
    """Question 16"""
    student_answers = get_answers()
    assert _verify_answer(16, student_answers[16]), \
        "Incorrect answer for Question 16"

def test_question_17():
    """Question 17"""
    student_answers = get_answers()
    assert _verify_answer(17, student_answers[17]), \
        "Incorrect answer for Question 17"

def test_question_18():
    """Question 18"""
    student_answers = get_answers()
    assert _verify_answer(18, student_answers[18]), \
        "Incorrect answer for Question 18"

def test_question_19():
    """Question 19"""
    student_answers = get_answers()
    assert _verify_answer(19, student_answers[19]), \
        "Incorrect answer for Question 19"

def test_question_20():
    """Question 20"""
    student_answers = get_answers()
    assert _verify_answer(20, student_answers[20]), \
        "Incorrect answer for Question 20"

def test_calculate_score():
    """Calculate and display the final score."""
    student_answers = get_answers()
    correct_count = sum(
        1 for q in range(1, 21)
        if _verify_answer(q, student_answers[q])
    )

    percentage = (correct_count / 20) * 100

    print(f"\n{'='*50}")
    print(f"FINAL SCORE: {correct_count}/20 ({percentage:.1f}%)")
    print(f"{'='*50}")

    if correct_count >= 17:
        print("🏆 Excellent! You have a strong understanding!")
    elif correct_count >= 14:
        print("👍 Good understanding! Review key concepts.")
    elif correct_count >= 10:
        print("📖 Fair understanding. Please review the lecture.")
    else:
        print("🔄 Please review the lecture and try again.")

    print(f"{'='*50}\n")

    # This test always passes, but displays the score
    assert True
