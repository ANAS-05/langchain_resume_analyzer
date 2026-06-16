from src.config import get_llm
from src.models import CandidateSummary, JobDescriptionSummary, MatchAnalysis
from src.prompts import CANDIDATE_EXTRACTION_PROMPT, JD_EXTRACTION_PROMPT, MATCH_ANALYSIS_PROMPT

class MatchEngine:
    """Orchestrates the extraction and comparison of resumes and job descriptions."""
    
    def __init__(self):
        # 1. Initialize the core LLM
        self.llm = get_llm()
        
        # 2. Bind Pydantic models to force strict JSON schema outputs
        candidate_llm = self.llm.with_structured_output(CandidateSummary)
        jd_llm = self.llm.with_structured_output(JobDescriptionSummary)
        match_llm = self.llm.with_structured_output(MatchAnalysis)
        
        # 3. Create LCEL Chains (Prompt + Structured LLM)
        self.candidate_chain = CANDIDATE_EXTRACTION_PROMPT | candidate_llm
        self.jd_chain = JD_EXTRACTION_PROMPT | jd_llm
        self.match_chain = MATCH_ANALYSIS_PROMPT | match_llm

    def analyze(self, resume_text: str, jd_text: str) -> dict:
        """
        Executes the three-step AI pipeline.
        
        Args:
            resume_text (str): Raw text from the candidate's PDF.
            jd_text (str): Raw text from the job description PDF.
            
        Returns:
            dict: A dictionary containing the parsed candidate, parsed JD, and final analysis.
        """
        print("Extracting candidate profile...")
        candidate_summary = self.candidate_chain.invoke({"resume_text": resume_text})
        
        print("Extracting job requirements...")
        jd_summary = self.jd_chain.invoke({"jd_text": jd_text})
        
        print("Performing match analysis...")
        # Convert the parsed Pydantic models to JSON strings to inject into the final prompt
        analysis_result = self.match_chain.invoke({
            "candidate_summary": candidate_summary.model_dump_json(indent=2),
            "jd_summary": jd_summary.model_dump_json(indent=2)
        })
        
        return {
            "candidate": candidate_summary,
            "job_description": jd_summary,
            "analysis": analysis_result
        }