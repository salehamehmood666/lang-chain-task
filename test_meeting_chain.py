#!/usr/bin/env python3
"""
Test script for Meeting Chain
Demonstrates the LLM chains for meeting tasks
"""

from meeting_chain import MeetingChain, MeetingInfo

def test_meeting_chain():
    """Test the meeting chain with sample data"""
    
    print("🎯 Testing Meeting Chain")
    print("=" * 50)
    
    try:
        # Initialize the chain
        print("🔧 Initializing Meeting Chain...")
        chain = MeetingChain()
        print("✅ Meeting Chain initialized successfully!")
        
        # Create a test meeting
        test_meeting = MeetingInfo(
            date="2024-02-20",
            time="2:00 PM",
            agenda="Project Kickoff Meeting, Team Introduction, Timeline Discussion, Resource Allocation",
            attendees=["Project Manager", "Team Lead", "Senior Developer", "QA Engineer", "Designer"],
            location="Conference Room A",
            duration="1.5 hours",
            organizer="Project Manager"
        )
        
        print(f"\n📋 Test Meeting Details:")
        print(f"Date: {test_meeting.date}")
        print(f"Time: {test_meeting.time}")
        print(f"Agenda: {test_meeting.agenda}")
        print(f"Attendees: {', '.join(test_meeting.attendees)}")
        print(f"Location: {test_meeting.location}")
        
        # Process the meeting through all chains
        print("\n🔄 Processing meeting through LLM chains...")
        results = chain.process_meeting(test_meeting)
        
        # Print results
        chain.print_results(results)
        
        # Save results
        print("\n💾 Saving results...")
        chain.save_results(results, "test_meeting")
        
        print("\n🎉 Test completed successfully!")
        print("Check the 'output' folder for generated documents.")
        
    except Exception as e:
        print(f"❌ Error during test: {e}")
        print("Please make sure your API keys are properly configured in the .env file")

if __name__ == "__main__":
    test_meeting_chain() 