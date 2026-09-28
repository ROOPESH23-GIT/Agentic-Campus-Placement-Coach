class MockInterviewerAgent:
    """
    Agent responsible for generating targeted interview questions based on
    skill gaps and candidate strengths identified in the resume analysis.
    """
    def __init__(self):
        self.name = "MockInterviewer"
        self.question_bank = {
            "redis": {
                "question": "How does Redis achieve low latency, and when would you choose Redis over Memcached for an LRU cache?",
                "category": "System Design & Caching",
                "difficulty": "Medium",
                "expected_keywords": ["in-memory", "single-threaded", "event loop", "data structures", "persistence", "lru"]
            },
            "docker": {
                "question": "Explain the difference between a Docker Image and a Docker Container, and how layered file systems optimize build times.",
                "category": "DevOps & Deployment",
                "difficulty": "Easy-Medium",
                "expected_keywords": ["image", "container", "layer", "unionfs", "read-only", "runtime", "cache"]
            },
            "algorithms": {
                "question": "How would you implement an LRU (Least Recently Used) cache with O(1) get and put operations?",
                "category": "Data Structures & Algorithms",
                "difficulty": "Medium-Hard",
                "expected_keywords": ["hash map", "doubly linked list", "o(1)", "pointers", "eviction"]
            },
            "system design": {
                "question": "Describe how you would design a URL shortener service (like bit.ly) to handle 10,000 requests per second.",
                "category": "High-Level System Design",
                "difficulty": "Medium",
                "expected_keywords": ["base62", "hashing", "database", "load balancer", "caching", "collisions"]
            },
            "postgresql": {
                "question": "What is the difference between Clustered and Non-Clustered indexing in relational databases, and what causes an index scan vs index seek?",
                "category": "DBMS & Storage",
                "difficulty": "Medium",
                "expected_keywords": ["b-tree", "disk", "row pointer", "leaf node", "index scan", "seek"]
            }
        }

    def generate_interview(self, analysis_result: dict, count: int = 3) -> list:
        selected_questions = []
        missing = analysis_result.get("missing_skills", [])
        matched = analysis_result.get("matched_skills", [])

        # Priority 1: Target missing skills first
        for skill in missing:
            if skill in self.question_bank and len(selected_questions) < count:
                selected_questions.append(self.question_bank[skill])

        # Priority 2: Core DSA / System Design
        for key in ["algorithms", "system design"]:
            if key in self.question_bank and len(selected_questions) < count:
                if self.question_bank[key] not in selected_questions:
                    selected_questions.append(self.question_bank[key])

        # Priority 3: Fallback questions
        for skill in matched:
            if skill in self.question_bank and len(selected_questions) < count:
                if self.question_bank[skill] not in selected_questions:
                    selected_questions.append(self.question_bank[skill])

        return selected_questions
