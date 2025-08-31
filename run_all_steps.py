#!/usr/bin/env python3
"""
Complete Workflow: Steps 1, 2, and 3
Runs all three steps in sequence for the complete meeting workflow
"""

from step1_meeting_schedule import MeetingScheduleGenerator, MeetingDetails
from step2_staff_email import StaffEmailGenerator
from step3_mom_template import MOMTemplateGenerator
import os
from datetime import datetime

def run_complete_workflow():
    """Run all three steps in sequence"""
    
    print("🎯 Complete Meeting Workflow: Steps 1, 2, and 3")
    print("=" * 60)
    
    try:
        # Step 1: Generate Meeting Schedule
        print("\n📅 STEP 1: Generating Meeting Schedule (OpenAI)")
        print("-" * 50)
        
        # Initialize Step 1
        schedule_generator = MeetingScheduleGenerator()
        
        # Create meeting details
        meeting = MeetingDetails(
            date="2024-02-25",
            time="10:00 AM",
            agenda="Q1 Strategy Review, Budget Planning, Team Performance Assessment, New Project Proposals",
            attendees=["John Smith (CEO)", "Sarah Johnson (CTO)", "Mike Davis (CFO)", "Lisa Brown (HR Manager)"],
            location="Board Room",
            duration="2 hours",
            organizer="John Smith"
        )
        
        # Generate meeting schedule
        meeting_schedule = schedule_generator.generate_schedule(meeting)
        schedule_generator.print_schedule(meeting_schedule)
        schedule_generator.save_schedule(meeting_schedule, "complete_workflow_schedule.txt")
        
        # Step 2: Generate Staff Email
        print("\n📧 STEP 2: Generating Staff Email (Gemini)")
        print("-" * 50)
        
        # Initialize Step 2
        email_generator = StaffEmailGenerator()
        
        # Generate staff email
        staff_email = email_generator.generate_staff_email(meeting_schedule, meeting.attendees)
        email_generator.print_email(staff_email)
        email_generator.save_email(staff_email, "complete_workflow_email.txt")
        
        # Step 3: Generate MOM Template
        print("\n📝 STEP 3: Generating MOM Template (OpenAI)")
        print("-" * 50)
        
        # Initialize Step 3
        mom_generator = MOMTemplateGenerator()
        
        # Generate MOM template
        mom_template = mom_generator.generate_mom_template(meeting_schedule, meeting.agenda)
        mom_generator.print_template(mom_template)
        mom_generator.save_template(mom_template, "complete_workflow_mom_template.txt")
        
        # Summary
        print("\n🎉 COMPLETE WORKFLOW SUMMARY")
        print("=" * 60)
        print("✅ Step 1: Meeting Schedule generated (OpenAI)")
        print("✅ Step 2: Staff Email generated (Gemini)")
        print("✅ Step 3: MOM Template generated (OpenAI)")
        print("\n📁 All documents saved in 'output/' folder:")
        print("   - complete_workflow_schedule.txt")
        print("   - complete_workflow_email.txt")
        print("   - complete_workflow_mom_template.txt")
        
        print("\n🎯 Workflow completed successfully!")
        print("The secretary now has all necessary documents for the meeting.")
        
    except Exception as e:
        print(f"❌ Error in workflow: {e}")
        print("Please check your API keys in the .env file")

if __name__ == "__main__":
    run_complete_workflow() 