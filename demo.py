#!/usr/bin/env python3
"""
🎓 Agentic Campus Placement Coach - Live Demo Simulation
Runs an end-to-end multi-agent evaluation pipeline with clean console visualization.
"""
import sys
import os
import time

# Ensure src is on python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from src.orchestrator import CoachOrchestrator

def print_banner():
    print("=" * 65)
    print(" 🎓 AGENTIC CAMPUS PLACEMENT COACH - CSE UNDERGRADUATE EDITION")
    print("=" * 65)
    print(" Multi-Agent Collaboration: Resume Analyzer + Interviewer + Evaluator")
    print("-" * 65)

def main():
    print_banner()

    resume_path = os.path.join(os.path.dirname(__file__), "data", "sample_resume.txt")
    jd_path = os.path.join(os.path.dirname(__file__), "data", "sample_jd.txt")

    with open(resume_path, "r", encoding="utf-8") as f:
        resume_content = f.read()

    with open(jd_path, "r", encoding="utf-8") as f:
        jd_content = f.read()

    orchestrator = CoachOrchestrator()

    print("\n[Phase 1] 📄 ResumeAnalyzerAgent activating...")
    time.sleep(0.5)
    analysis = orchestrator.resume_agent.analyze(resume_content, jd_content)
    print(f"  ✓ ATS Compatibility Score: {analysis['ats_score']}%")
    print(f"  ✓ Key Strengths: {', '.join(analysis['matched_skills'])}")
    print(f"  ⚠ Missing Prerequisites: {', '.join(analysis['missing_skills'])}")

    print("\n[Phase 2] 💼 TechInterviewerAgent generating tailored questions...")
    time.sleep(0.5)
    questions = orchestrator.interviewer_agent.generate_interview(analysis, count=3)
    for i, q in enumerate(questions, 1):
        print(f"  [{q['category']} - {q['difficulty']}] Q{i}: {q['question']}")

    print("\n[Phase 3] ⚖️ FeedbackEvaluatorAgent scoring candidate answers...")
    time.sleep(0.5)
    mock_answers = {
        0: "I would use a Hash Map combined with a Doubly Linked List for O(1) lookups and pointer updates.",
        1: "Redis is an in-memory single-threaded key-value store that supports complex data structures and persistence.",
        2: "A Docker image is a read-only template with layers, while a container is a running instance."
    }

    evaluations = []
    for idx, q in enumerate(questions):
        ans = mock_answers[idx]
        ev = orchestrator.evaluator_agent.evaluate_response(q, ans)
        evaluations.append(ev)
        print(f"\n  Q: {q['question']}")
        print(f"  Candidate: \"{ans}\"")
        print(f"  Grade: {ev['score']}/10 | Verdict: {ev['verdict']}")
        print(f"  Pro-Tip: {ev['improvement_tip']}")

    print("\n[Phase 4] 🗺️ RoadmapGeneratorAgent formulating 30-Day Sprint...")
    time.sleep(0.5)
    roadmap = orchestrator.roadmap_agent.generate_roadmap(analysis['missing_skills'], evaluations)
    for week, tasks in roadmap.items():
        print(f"\n  📌 {week}:")
        for t in tasks:
            print(f"     • {t}")

    avg_score = sum(e['score'] for e in evaluations) / len(evaluations)
    readiness = int((analysis['ats_score'] * 0.4) + (avg_score * 10 * 0.6))
    print("\n" + "=" * 65)
    print(f" 🎯 OVERALL CAMPUS PLACEMENT READINESS INDEX: {readiness}/100")
    print("=" * 65)
    print("✨ Demo execution completed successfully!\n")

if __name__ == "__main__":
    main()
