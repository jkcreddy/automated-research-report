from pydantic import BaseModel, Field

class ReportRequest(BaseModel):
    topic: str = Field(..., description="Research topic for the report")
    max_analysts: int = Field(default=3, ge=1, le=10, description="Number of analysts to involve")

class FeedbackRequest(BaseModel):
    thread_id: str
    feedback: str = ""

class LoginRequest(BaseModel):
    username: str = Field(..., description="Username for login")
    password: str = Field(..., description="Password for login")

class SignupRequest(BaseModel):
    username: str = Field(..., description="Username for signup")
    password: str = Field(..., description="Password for signup")

class ReportRequest(BaseModel):
    topic: str = Field(..., description="Topic for report generation")
    feedback: str | None = Field(None, description="Optional feedback from analyst")