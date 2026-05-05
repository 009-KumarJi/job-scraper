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
    "SDE 1 Backend",
    "SDE I",
    "SDEI",
    "SDE1",
    "Software Development Engineer I",
    "Software Developer Engineer I",
    "Software Engineer I",
    "Software Developer I",
    "Junior Software Engineer",
    "Junior Software Developer",
    "Entry Level Software Engineer",
    "Entry Level Software Developer",
    "Graduate Software Engineer",
    "Graduate Software Developer",
    "New Grad Software Engineer",
    "Associate Software Engineer",
    "Associate Software Developer",
    "Founding Engineer",
    "Founding Software Engineer",
    "Founding Backend Engineer",
    "Software Engineer Intern",
    "Backend Engineer Intern",
    "Machine Learning Intern",
    "AI Intern",
    "Software Engineer",
    "Software Developer",
    "Product Engineer",
    "Platform Engineer",
    "Systems Engineer",
    "Application Developer",
    "Backend Engineer",
    "Backend Developer",
    "Backend Software Engineer",
    "Backend Software Developer",
    "Backend Application Developer",
    "Junior Backend Engineer",
    "Junior Backend Developer",
    "Associate Backend Engineer",
    "Associate Backend Developer",
    "Entry Level Backend Engineer",
    "Entry Level Backend Developer",
    "Software Engineer Backend",
    "Python Developer",
    "Python Engineer",
    "Python Backend Developer",
    "Django Developer",
    "FastAPI Developer",
    "Flask Developer",
    "API Developer",
    "API Engineer",
    "Microservices Engineer",
    "Distributed Systems Engineer",
    "Cloud Engineer",
    "DevOps Engineer",
    "Site Reliability Engineer",
    "Infrastructure Engineer",
    "Data Engineer",
    "Analytics Engineer",
    "AI/ML Engineer",
    "Machine Learning Engineer",
    "Junior Machine Learning Engineer",
    "Associate Machine Learning Engineer",
    "Entry Level Machine Learning Engineer",
    "Machine Learning Developer",
    "Applied Machine Learning Engineer",
    "ML Engineer",
    "AI Engineer",
    "Junior AI Engineer",
    "Associate AI Engineer",
    "Applied AI Engineer",
    "Generative AI Engineer",
    "GenAI Engineer",
    "Prompt Engineer",
    "AI Application Engineer",
    "AI Product Engineer",
    "RAG Engineer",
    "LLM Engineer",
    "LLM Application Engineer",
    "NLP Engineer",
    "Computer Vision Engineer",
    "Node.js Developer",
    "Node.js Engineer",
    "Backend Node.js Developer",
    "Express.js Developer",
    "Java Developer",
    "Java Backend Developer",
    "Spring Boot Developer",
    "Go Developer",
    "Golang Developer",
    "Go Backend Developer",
    "Rust Developer",
    "C++ Developer",
]

LINKEDIN_LOCATION = "Bengaluru"
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
    "Generative AI Engineer",
    "Applied AI Engineer"
]

CAREERS_FUTURE_SEARCH_CATEGORIES = ["Information Technology"]
CAREERS_FUTURE_SEARCH_EMPLOYMENT_TYPES = ["Full Time"]

# --- Processing Limits ---
SCRAPING_SOURCES = ["linkedin"] # "linkedin", "careers_future"
JOBS_TO_SCORE_PER_RUN = 5
JOBS_TO_CUSTOMIZE_PER_RUN = 1
MAX_JOBS_PER_SEARCH = {
    "linkedin": 15
}

# --- Targeting Filters ---
FILTER_FOR_JUNIOR_ROLES = True
FILTER_FOR_STARTUP_SIGNALS = False
FILTER_OUT_LARGE_COMPANIES = True
FILTER_STRICT_LOCATION = True
FILTER_FETCH_MULTIPLIER = 5
MAX_FILTER_CANDIDATES_PER_QUERY = 30
MIN_TARGET_MATCH_SCORE = 4

STRICT_LOCATION_KEYWORDS = [
    "bengaluru",
    "bangalore",
    "hsr layout",
    "koramangala",
    "whitefield",
]

TARGET_ROLE_KEYWORDS = [
    "backend",
    "back end",
    "python",
    "software engineer",
    "software developer",
    "application developer",
    "sde",
    "associate software engineer",
    "machine learning",
    "ml engineer",
    "ai engineer",
    "applied ai",
    "generative ai",
    "genai",
    "llm",
    "rag",
]

EXCLUDED_ROLE_KEYWORDS = [
    "frontend",
    "front end",
    "react developer",
    "ui developer",
    "ux developer",
    "web designer",
    "graphic designer",
    "ios developer",
    "android developer",
    "flutter developer",
    "qa engineer",
    "test engineer",
    "salesforce developer",
    "support engineer",
]

PREFERRED_ROLE_KEYWORDS = [
    "backend engineer",
    "backend developer",
    "python developer",
    "software engineer backend",
    "machine learning engineer",
    "ai engineer",
    "generative ai engineer",
    "applied ai engineer",
    "llm engineer",
    "founding engineer",
]

PREFERRED_WORKPLACE_KEYWORDS = [
    "remote",
    "hybrid",
]

REMOTE_WORKPLACE_KEYWORDS = [
    "remote",
    "work from home",
    "wfh",
]

HYBRID_WORKPLACE_KEYWORDS = [
    "hybrid",
]

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

BLACKLISTED_COMPANIES = [
    "scoutit"
]

LARGE_COMPANY_BLOCKLIST.extend(BLACKLISTED_COMPANIES)

# =================================================================
# 3. ADVANCED SYSTEM SETTINGS (Modify with Caution)
# =================================================================
LLM_MAX_RPM = 10
LLM_MAX_RETRIES = 3
LLM_RETRY_BASE_DELAY = 10
LLM_DAILY_REQUEST_BUDGET = 0
LLM_REQUEST_DELAY_SECONDS = 8

# LinkedIn pagination uses offsets of 0, 10, 20, ...
# 20 means the scraper can inspect the first 3 result pages.
LINKEDIN_MAX_START = 20
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
