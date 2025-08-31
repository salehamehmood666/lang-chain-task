#!/usr/bin/env python3
"""
Demo script for the Meeting & Office Task Assistant
"""

from meeting_assistant import MeetingAssistant, MeetingDetails
from config import config

def demo_meeting_assistant():
    """Demonstrate the Meeting Assistant functionality"""
    
    print("🎯 Meeting & Office Task Assistant Demo")
    print("=" * 60)
    
    # Check API keys
    if not config.OPENAI_API_KEY or not config.GOOGLE_API_KEY:
        print("❌ Error: API keys not configured!")
        print("Please add your API keys to the .env file:")
        print("   OPENAI_API_KEY=your_openai_key_here")
        print("   GOOGLE_API_KEY=your_google_key_here")
        return
    
    # Initialize assistant
    print("🔧 Initializing Meeting Assistant...")
    assistant = MeetingAssistant()
    print("✅ Assistant initialized successfully!")
    
    # Example 1: Executive Meeting
    print("\n📋 Example 1: Executive Strategy Meeting")
    print("-" * 40)
    
    exec_meeting = MeetingDetails(
        date="2024-02-20",
        time="2:00 PM",
        agenda="Annual Strategy Review, Budget Allocation, Market Analysis, Competitive Positioning",
        attendees=["CEO", "CFO", "CTO", "VP Sales", "VP Marketing"],
        location="Board Room",
        duration="3 hours",
        organizer="CEO"
    )
    
    results1 = assistant.process_meeting_request(exec_meeting)
    assistant.print_results(results1)
    
    # Example 2: Team Meeting
    print("\n📋 Example 2: Development Team Meeting")
    print("-" * 40)
    
    team_meeting = MeetingDetails(
        date="2024-02-22",
        time="10:00 AM",
        agenda="Sprint Planning, Code Review Process, Bug Fixes, New Feature Development",
        attendees=["Team Lead", "Senior Developer", "Junior Developer", "QA Engineer", "Product Manager"],
        location="Development Lab",
        duration="1.5 hours",
        organizer="Team Lead"
    )
    
    results2 = assistant.process_meeting_request(team_meeting)
    assistant.print_results(results2)
    
    # Save all documents
    print("\n💾 Saving all documents...")
    assistant.save_documents(results1, "meeting_documents/executive_meeting")
    assistant.save_documents(results2, "meeting_documents/team_meeting")
    
    print("\n🎉 Demo completed successfully!")
    print("Check the 'meeting_documents' folder for saved files.")

def interactive_demo():
    """Interactive demo where user can input meeting details"""
    
    print("🎯 Interactive Meeting Assistant Demo")
    print("=" * 60)
    
    # Check API keys
    if not config.OPENAI_API_KEY or not config.GOOGLE_API_KEY:
        print("❌ Error: API keys not configured!")
        return
    
    # Initialize assistant
    assistant = MeetingAssistant()
    
    print("📝 Please provide meeting details:")
    print("-" * 30)
    
    # Get user input
    date = input("Date (YYYY-MM-DD): ").strip()
    time = input("Time (e.g., 2:00 PM): ").strip()
    agenda = input("Agenda: ").strip()
    location = input("Location (optional): ").strip() or "Conference Room"
    duration = input("Duration (optional): ").strip() or "1 hour"
    organizer = input("Organizer (optional): ").strip() or "Management"
    
    attendees_input = input("Attendees (comma-separated, optional): ").strip()
    attendees = [name.strip() for name in attendees_input.split(",")] if attendees_input else None
    
    # Create meeting details
    meeting_details = MeetingDetails(
        date=date,
        time=time,
        agenda=agenda,
        attendees=attendees,
        location=location,
        duration=duration,
        organizer=organizer
    )
    
    # Process the meeting
    print("\n🔄 Processing your meeting request...")
    results = assistant.process_meeting_request(meeting_details)
    
    # Show results
    assistant.print_results(results)
    
    # Save documents
    save_choice = input("\n💾 Save documents? (y/n): ").strip().lower()
    if save_choice == 'y':
        assistant.save_documents(results)
        print("✅ Documents saved successfully!")

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1 and sys.argv[1] == "--interactive":
        interactive_demo()
    else:
        demo_meeting_assistant() 