import os
from dotenv import load_dotenv

load_dotenv()

# --- DO NOT MODIFY THE BELOW SECTION ---

# =================================================================
# 1. CORE SYSTEM CONFIGURATION (Do Not Modify)
# =================================================================
SUPABASE_URL: str = os.environ.get("SUPABASE_URL")
SUPABASE_SERVICE_ROLE_KEY: str = os.environ.get("SUPABASE_SERVICE_ROLE_KEY")
SUPABASE_TABLE_NAME: str = "jobs"
SUPABASE_CUSTOMIZED_RESUMES_TABLE_NAME = "customized_resumes"
SUPABASE_STORAGE_BUCKET="personalized_resumes"
SUPABASE_RESUME_STORAGE_BUCKET="resumes"
SUPABASE_BASE_RESUME_TABLE_NAME = "base_resume"
BASE_RESUME_PATH = "resume.json"

# API keys — set only the key(s) needed for your chosen provider.
LLM_API_KEY = os.environ.get("LLM_API_KEY") or os.environ.get("GEMINI_API_KEY") or os.environ.get("GEMINI_FIRST_API_KEY")

# =================================================================
# 2. USER PREFERENCES (Editable)
# =================================================================

# --- LLM Settings ---
# Use any model supported by LiteLLM (gemini, openai/gpt-4o-mini, groq/llama-3.3-70b-versatile)
# Full list of supported models & naming: https://docs.litellm.ai/docs/providers
LLM_MODEL = "gemini"

# --- Search Configuration ---
LINKEDIN_SEARCH_QUERIES = [
    "SDE 1",
    "Software Engineer",
    "Backend Engineer",
    "Backend Developer",
    "Python Developer",
    "Machine Learning Engineer",
    "AI Engineer",
    "Generative AI Engineer",
    "Applied AI Engineer"
]

LINKEDIN_LOCATION = "Bengaluru, Karnataka, India"
LINKEDIN_GEO_ID = 102713980

LINKEDIN_JOB_TYPE = "F"
LINKEDIN_JOB_POSTING_DATE = "r86400"
LINKEDIN_F_WT = 3

CAREERS_FUTURE_SEARCH_QUERIES = [
    "Software Engineer",
    "Backend Developer",
    "Backend Engineer",
    "Application Developer",
    "Associate Software Engineer",
    "Python Developer",
    "Machine Learning Engineer",
    "AI Engineer",
    "Generative AI Engineer"
]

CAREERS_FUTURE_SEARCH_CATEGORIES = ["Information Technology"]
CAREERS_FUTURE_SEARCH_EMPLOYMENT_TYPES = ["Full Time"]

# --- Processing Limits ---
SCRAPING_SOURCES = ["linkedin"] # "linkedin", "careers_future"
JOBS_TO_SCORE_PER_RUN = 5
JOBS_TO_CUSTOMIZE_PER_RUN = 1
MAX_JOBS_PER_SEARCH = {
    "linkedin": 2,
    "careers_future": 10,
}

# --- Targeting Filters ---
FILTER_FOR_JUNIOR_ROLES = True
FILTER_FOR_STARTUP_SIGNALS = True
FILTER_OUT_LARGE_COMPANIES = True

JUNIOR_ROLE_KEYWORDS = [
    "sde 1",
    "associate",
    "junior",
    "entry level",
    "fresher",
    "graduate",
    "new grad",
    "apprentice",
    "0-2 years",
    "0 to 2 years",
    "1 year",
    "2 years",
]

SENIOR_ROLE_KEYWORDS = [
    "senior",
    "staff",
    "principal",
    "lead",
    "manager",
    "director",
    "architect",
    "head of",
    "vp",
    "vice president",
    "7+ years",
    "8+ years",
    "10+ years",
]

STARTUP_SIGNAL_KEYWORDS = [
    "startup",
    "early-stage",
    "early stage",
    "seed stage",
    "seed-funded",
    "series a",
    "series b",
    "series c",
    "founding engineer",
    "0 to 1",
    "zero to one",
    "fast-paced",
    "fast paced",
    "small team",
    "lean team",
    "build from scratch",
    "ownership",
]

LARGE_COMPANY_BLOCKLIST = [
    "google",
    "microsoft",
    "amazon",
    "meta",
    "apple",
    "netflix",
    "uber",
    "linkedin",
    "salesforce",
    "oracle",
    "sap",
    "ibm",
    "intel",
    "adobe",
    "servicenow",
    "atlassian",
    "walmart",
    "deloitte",
    "accenture",
    "infosys",
    "tcs",
    "wipro",
    "hcl",
    "cognizant",
    "capgemini",
]

# =================================================================
# 3. ADVANCED SYSTEM SETTINGS (Modify with Caution)
# =================================================================
LLM_MAX_RPM = 10
LLM_MAX_RETRIES = 3
LLM_RETRY_BASE_DELAY = 10
LLM_DAILY_REQUEST_BUDGET = 0
LLM_REQUEST_DELAY_SECONDS = 8

LINKEDIN_MAX_START = 1 
REQUEST_TIMEOUT = 30
MAX_RETRIES = 3
RETRY_DELAY_SECONDS = 15

JOB_EXPIRY_DAYS = 30
JOB_CHECK_DAYS = 3
JOB_DELETION_DAYS = 60
JOB_CHECK_LIMIT = 50
ACTIVE_CHECK_TIMEOUT = 20
ACTIVE_CHECK_MAX_RETRIES = 2
ACTIVE_CHECK_RETRY_DELAY = 10
