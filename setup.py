#!/usr/bin/env python3
"""
Setup Script for Meeting & Office Task Assistant
Helps users configure their API keys securely
"""

import os
import shutil
from pathlib import Path

def setup_environment():
    """Setup the environment for new users"""
    
    print("🎯 Meeting & Office Task Assistant Setup")
    print("=" * 50)
    
    # Check if .env file exists
    env_file = Path('.env')
    env_example = Path('.env.example')
    
    if not env_file.exists():
        if env_example.exists():
            print("📝 Creating .env file from template...")
            shutil.copy('.env.example', '.env')
            print("✅ .env file created!")
            print("\n🔑 Please edit the .env file and add your API keys:")
            print("   1. OPENAI_API_KEY=your_actual_openai_key")
            print("   2. GOOGLE_API_KEY=your_actual_google_key")
        else:
            print("❌ .env.example file not found!")
            return False
    else:
        print("✅ .env file already exists")
    
    # Check if virtual environment exists
    venv_path = Path('.venv')
    if not venv_path.exists():
        print("\n🐍 Creating virtual environment...")
        os.system('python3 -m venv .venv')
        print("✅ Virtual environment created!")
        print("\n🔧 Activate the virtual environment:")
        print("   source .venv/bin/activate  # On Linux/Mac")
        print("   .venv\\Scripts\\activate     # On Windows")
    else:
        print("✅ Virtual environment already exists")
    
    print("\n📦 Installing dependencies...")
    os.system('pip install -r requirements.txt')
    
    print("\n🎉 Setup complete!")
    print("\n📋 Next steps:")
    print("   1. Activate virtual environment: source .venv/bin/activate")
    print("   2. Add your API keys to .env file")
    print("   3. Test the system: python complete_workflow.py")
    
    return True

def check_api_keys():
    """Check if API keys are properly configured"""
    
    print("\n🔒 Checking API key configuration...")
    
    try:
        from secure_config import validate_api_keys
        return validate_api_keys()
    except ImportError:
        print("❌ Secure configuration not found. Please run setup first.")
        return False

if __name__ == "__main__":
    setup_environment()
    check_api_keys() 