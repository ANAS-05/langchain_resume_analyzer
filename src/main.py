import argparse
from pathlib import Path
from src.pdf_parser import extract_text_from_pdf
from src.match_engine import MatchEngine

def main():
    # 1. Set up the Command Line Interface
    parser = argparse.ArgumentParser(description="AI Candidate-Job Match Analyzer")
    parser.add_argument("--resume", type=str, required=True, help="Path to the candidate's resume PDF")
    parser.add_argument("--jd", type=str, required=True, help="Path to the job description PDF")
    
    args = parser.parse_args()
    resume_path = Path(args.resume)
    jd_path = Path(args.jd)

    # 2. Extract Text from PDFs
    print(f"📄 Loading Resume from {resume_path}...")
    try:
        resume_text = extract_text_from_pdf(resume_path)
    except Exception as e:
        print(f"❌ Error loading Resume: {e}")
        return

    print(f"📄 Loading Job Description from {jd_path}...")
    try:
        jd_text = extract_text_from_pdf(jd_path)
    except Exception as e:
        print(f"❌ Error loading Job Description: {e}")
        return

    # 3. Initialize and Run the AI Engine
    print("\n🧠 Initializing AI Match Engine...")
    engine = MatchEngine()

    print("⚙️  Analyzing... (This may take a few seconds)\n")
    results = engine.analyze(resume_text, jd_text)

    # 4. Display the Output
    print("\n" + "="*50)
    print("                ANALYSIS COMPLETE")
    print("="*50 + "\n")
    
    print("--- 👤 Extracted Candidate Profile ---")
    print(results["candidate"].model_dump_json(indent=2))
    
    print("\n--- 🏢 Extracted Job Requirements ---")
    print(results["job_description"].model_dump_json(indent=2))
    
    print("\n--- 🎯 Final Match Analysis ---")
    print(results["analysis"].model_dump_json(indent=2))

if __name__ == "__main__":
    main()