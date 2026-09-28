import re

class ResumeAnalyzerAgent:
    """
    Agent responsible for parsing resumes, extracting technical competencies,
    comparing against target job descriptions, and calculating ATS match score.
    """
    def __init__(self):
        self.name = "ResumeAnalyzer"
        self.core_skills_keywords = [
            "python", "javascript", "c++", "java", "sql", "postgresql", "mysql", "sqlite",
            "mongodb", "react", "node.js", "express", "flask", "django", "docker", "kubernetes",
            "aws", "gcp", "azure", "redis", "caching", "rest", "restful", "microservices",
            "git", "github", "linux", "algorithms", "data structures", "system design"
        ]

    def analyze(self, resume_text: str, jd_text: str) -> dict:
        resume_lower = resume_text.lower()
        jd_lower = jd_text.lower()

        # Identify skills present in resume
        candidate_skills = {
            skill for skill in self.core_skills_keywords
            if re.search(r'\b' + re.escape(skill) + r'\b', resume_lower)
        }

        # Identify skills required by JD
        required_skills = {
            skill for skill in self.core_skills_keywords
            if re.search(r'\b' + re.escape(skill) + r'\b', jd_lower)
        }

        matched_skills = candidate_skills.intersection(required_skills)
        missing_skills = required_skills.difference(candidate_skills)

        if required_skills:
            ats_score = int((len(matched_skills) / len(required_skills)) * 100)
        else:
            ats_score = 70

        return {
            "ats_score": ats_score,
            "matched_skills": sorted(list(matched_skills)),
            "missing_skills": sorted(list(missing_skills)),
            "candidate_total_skills": sorted(list(candidate_skills)),
            "strengths_summary": f"Strong in {', '.join(list(matched_skills)[:4])}",
            "gap_summary": f"Needs exposure to {', '.join(list(missing_skills)[:3])}"
        }
