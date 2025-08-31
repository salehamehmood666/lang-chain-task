import os
from dotenv import load_dotenv
from secure_config import load_secure_config

# Load environment variables from .env file
load_dotenv()

# Load secure configuration
secure_config = load_secure_config()

class Config:
    """Configuration class to manage environment variables"""
    
    # Database Configuration
    DATABASE_URL = os.getenv('DATABASE_URL', 'sqlite:///app.db')
    DATABASE_HOST = os.getenv('DATABASE_HOST', 'localhost')
    DATABASE_PORT = int(os.getenv('DATABASE_PORT', 5432))
    DATABASE_NAME = os.getenv('DATABASE_NAME', 'mydb')
    DATABASE_USER = os.getenv('DATABASE_USER', 'user')
    DATABASE_PASSWORD = os.getenv('DATABASE_PASSWORD', 'password')
    
    # API Configuration
    API_KEY = os.getenv('API_KEY')
    API_SECRET = os.getenv('API_SECRET')
    API_BASE_URL = os.getenv('API_BASE_URL', 'https://api.example.com')
    API_VERSION = os.getenv('API_VERSION', 'v1')
    
    # LLM API Keys
    OPENAI_API_KEY = secure_config['OPENAI_API_KEY']
    GOOGLE_API_KEY = secure_config['GOOGLE_API_KEY']
    
    # Application Configuration
    DEBUG = os.getenv('DEBUG', 'False').lower() == 'true'
    ENVIRONMENT = os.getenv('ENVIRONMENT', 'development')
    LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO')
    SECRET_KEY = os.getenv('SECRET_KEY', 'default-secret-key')
    
    # External Services
    REDIS_URL = os.getenv('REDIS_URL', 'redis://localhost:6379')
    REDIS_HOST = os.getenv('REDIS_HOST', 'localhost')
    REDIS_PORT = int(os.getenv('REDIS_PORT', 6379))
    
    # Email Configuration
    SMTP_HOST = os.getenv('SMTP_HOST', 'smtp.gmail.com')
    SMTP_PORT = int(os.getenv('SMTP_PORT', 587))
    SMTP_USER = os.getenv('SMTP_USER')
    SMTP_PASSWORD = os.getenv('SMTP_PASSWORD')
    
    # File Storage
    UPLOAD_PATH = os.getenv('UPLOAD_PATH', '/uploads')
    MAX_FILE_SIZE = int(os.getenv('MAX_FILE_SIZE', 10485760))

# Create a config instance
config = Config()

def get_env_vars():
    """Get all environment variables as a dictionary"""
    return {
        'database': {
            'url': config.DATABASE_URL,
            'host': config.DATABASE_HOST,
            'port': config.DATABASE_PORT,
            'name': config.DATABASE_NAME,
            'user': config.DATABASE_USER,
            'password': config.DATABASE_PASSWORD
        },
        'api': {
            'key': config.API_KEY,
            'secret': config.API_SECRET,
            'base_url': config.API_BASE_URL,
            'version': config.API_VERSION
        },
        'app': {
            'debug': config.DEBUG,
            'environment': config.ENVIRONMENT,
            'log_level': config.LOG_LEVEL,
            'secret_key': config.SECRET_KEY
        },
        'redis': {
            'url': config.REDIS_URL,
            'host': config.REDIS_HOST,
            'port': config.REDIS_PORT
        },
        'email': {
            'host': config.SMTP_HOST,
            'port': config.SMTP_PORT,
            'user': config.SMTP_USER,
            'password': config.SMTP_PASSWORD
        },
        'storage': {
            'upload_path': config.UPLOAD_PATH,
            'max_file_size': config.MAX_FILE_SIZE
        }
    } 