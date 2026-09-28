from .agents.resume_analyzer import ResumeAnalyzerAgent
from .agents.mock_interviewer import MockInterviewerAgent
from .agents.feedback_evaluator import FeedbackEvaluatorAgent
from .agents.roadmap_generator import RoadmapGeneratorAgent

class CoachOrchestrator:
    """
    Central Coordinator managing multi-agent workflow:
    Resume Analysis -> Question Formulation -> Response Evaluation -> Roadmap Synthesis.
    """
    def __init__(self):
        self.resume_agent = ResumeAnalyzerAgent()
        self.interviewer_agent = MockInterviewerAgent()
        self.evaluator_agent = FeedbackEvaluatorAgent()
        self.roadmap_agent = RoadmapGeneratorAgent()

    def run_assessment(self, resume_text: str, jd_text: str, candidate_answers: dict = None) -> dict:
        # Step 1: Resume Analysis
        analysis = self.resume_agent.analyze(resume_text, jd_text)

        # Step 2: Generate targeted questions
        questions = self.interviewer_agent.generate_interview(analysis, count=3)

        # Step 3: Evaluate candidate answers
        evaluations = []
        if candidate_answers is None:
            # Default answers for demo/simulation
            candidate_answers = {
                0: "I would use a Hash Map combined with a Doubly Linked List for O(1) lookups and pointer updates.",
                1: "Redis is an in-memory single-threaded key-value store that supports complex data structures and persistence.",
                2: "A Docker image is a read-only template with layers, while a container is a running instance."
            }

        for idx, q_data in enumerate(questions):
            ans = candidate_answers.get(idx, "I am not familiar with this topic.")
            ev = self.evaluator_agent.evaluate_response(q_data, ans)
            evaluations.append(ev)

        # Step 4: Synthesize 30-Day Preparation Roadmap
        roadmap = self.roadmap_agent.generate_roadmap(analysis["missing_skills"], evaluations)

        # Calculate Overall Readiness Score
        avg_eval_score = sum(e["score"] for e in evaluations) / len(evaluations) if evaluations else 5
        readiness_score = int((analysis["ats_score"] * 0.4) + (avg_eval_score * 10 * 0.6))

        return {
            "analysis": analysis,
            "questions": questions,
            "evaluations": evaluations,
            "roadmap": roadmap,
            "overall_readiness_score": readiness_score
        }
