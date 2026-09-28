class RoadmapGeneratorAgent:
    """
    Agent responsible for synthesizing placement preparation deficiencies into
    a customized 30-day engineering sprint roadmap.
    """
    def __init__(self):
        self.name = "RoadmapGenerator"

    def generate_roadmap(self, missing_skills: list, eval_results: list) -> dict:
        plan = {
            "Week 1: Core Fundamentals & Data Structures": [
                "Master Hash Tables, Two Pointers, and Binary Search patterns on LeetCode/CodeChef.",
                "Review time and space complexity proofs for sorting and tree traversals."
            ],
            "Week 2: System Design & Microservice Basics": [
                "Study horizontal vs vertical scaling, load balancers, and CAP theorem.",
                "Implement a simple distributed cache or rate limiter in Python."
            ],
            "Week 3: Tech Stack & Database Deep Dive": [
                "Practice SQL index optimizations, transaction isolation levels, and ACID compliance.",
                f"Close resume gaps by studying: {', '.join(missing_skills) if missing_skills else 'NoSQL vs SQL benchmarks'}."
            ],
            "Week 4: Mock Interviews & Behavioral Mastery": [
                "Practice answering behavioral questions using the STAR framework (Situation, Task, Action, Result).",
                "Perform live timed mock interviews on System Design and Core CS Subjects."
            ]
        }
        return plan
