from pydantic import BaseModel, Field
from typing import List

class CandidateSummary(BaseModel):
    """Extracted structured profile of a candidate from their resume."""
    name: str = Field(description="The full name of the candidate.")
    years_of_experience: float = Field(description="Total years of professional experience as a numerical value.")
    core_skills: List[str] = Field(description="List of key technical skills, languages, or tools mastered.")
    experience_summary: str = Field(description="A brief 2-3 sentence summary of their career highlights and background.")

class JobDescriptionSummary(BaseModel):
    """Extracted structured profile of a job description."""
    role_title: str = Field(description="The official title of the job position.")
    min_years_experience: float = Field(description="The minimum years of experience required for the role.")
    required_skills: List[str] = Field(description="List of mandatory technical skills, frameworks, or tools required.")
    preferred_skills: List[str] = Field(description="List of optional or preferred skills that are a plus.")

class MatchAnalysis(BaseModel):
    """The final analytical comparison between a candidate and a job description."""
    match_score: int = Field(description="An overall compatibility score from 0 to 100 based on strict criteria alignment.")
    matched_skills: List[str] = Field(description="Skills from the candidate's profile that perfectly align with the job requirements.")
    missing_skills: List[str] = Field(description="Required skills from the job description that the candidate is missing.")
    experience_fit_verdict: str = Field(description="An analytical verdict on whether the candidate's years of experience meet, exceed, or fall short of requirements, along with brief justification.")
    hiring_recommendation: str = Field(description="A definitive recommendation (e.g., 'Strong Proceed', 'Proceed with Caution', or 'Do Not Proceed') with a 2-sentence rationale.")