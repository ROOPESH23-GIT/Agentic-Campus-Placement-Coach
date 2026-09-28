#!/usr/bin/env python3
"""
CLI entry point for Agentic Campus Placement Coach.
"""
import argparse
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from src.orchestrator import CoachOrchestrator

def main():
    parser = argparse.ArgumentParser(description="Agentic Campus Placement Coach CLI")
    parser.add_argument("--resume", type=str, default="data/sample_resume.txt", help="Path to resume text file")
    parser.add_argument("--jd", type=str, default="data/sample_jd.txt", help="Path to Job Description file")
    args = parser.parse_args()

    if not os.path.exists(args.resume):
        print(f"Error: Resume file not found at {args.resume}")
        sys.exit(1)
    if not os.path.exists(args.jd):
        print(f"Error: JD file not found at {args.jd}")
        sys.exit(1)

    with open(args.resume, "r", encoding="utf-8") as f:
        resume_text = f.read()

    with open(args.jd, "r", encoding="utf-8") as f:
        jd_text = f.read()

    orchestrator = CoachOrchestrator()
    result = orchestrator.run_assessment(resume_text, jd_text)

    print("\n--- Assessment Summary ---")
    print(f"ATS Match Score: {result['analysis']['ats_score']}%")
    print(f"Matched Skills: {', '.join(result['analysis']['matched_skills'])}")
    print(f"Missing Skills: {', '.join(result['analysis']['missing_skills'])}")
    print(f"Overall Readiness Index: {result['overall_readiness_score']}/100\n")

if __name__ == "__main__":
    main()
