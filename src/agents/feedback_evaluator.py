class FeedbackEvaluatorAgent:
    """
    Agent responsible for grading student answers to technical questions,
    providing structured rubric feedback, and identifying knowledge gaps.
    """
    def __init__(self):
        self.name = "FeedbackEvaluator"

    def evaluate_response(self, question_data: dict, candidate_answer: str) -> dict:
        expected = [k.lower() for k in question_data.get("expected_keywords", [])]
        answer_lower = candidate_answer.lower()

        matched_keywords = [k for k in expected if k in answer_lower]
        coverage_ratio = len(matched_keywords) / len(expected) if expected else 0.5

        # Heuristic scoring
        if coverage_ratio >= 0.6:
            score = int(7 + (coverage_ratio * 3))
            verdict = "Excellent understanding with technical precision."
        elif coverage_ratio >= 0.3:
            score = int(4 + (coverage_ratio * 4))
            verdict = "Adequate conceptual grasp; needs to mention specific mechanics and complexity."
        else:
            score = 3
            verdict = "Answer is too brief or misses critical engineering fundamentals."

        score = min(10, max(1, score))

        missing_keywords = [k for k in expected if k not in matched_keywords]

        return {
            "question": question_data["question"],
            "score": score,
            "verdict": verdict,
            "matched_keywords": matched_keywords,
            "missing_keywords": missing_keywords,
            "improvement_tip": f"Consider explicitly discussing: {', '.join(missing_keywords[:2])} to demonstrate senior-level depth."
        }
