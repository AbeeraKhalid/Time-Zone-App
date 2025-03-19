#TIME ZONE APPLICATION...
import streamlit as st # type: ignore
from datetime import datetime
from zoneinfo import ZoneInfo

TIME_ZONES = [
    "UTC",
    "Asia/Karachi", 
    "Asia/Kolkata",
    "America/New_York",
    "Europe/London",
    "Asia/Tokyo",
    "Australia/Sydney",
    "America/Los_Angeles",
    "Europe/Berlin",
    "Asia/Dubai",
    "Asia/Shanghai",
    "Asia/Hong_Kong",
    "Asia/Singapore",
    "Asia/Bangkok",
    "Asia/Jakarta",
    "Asia/Manila",
]
    
st.title("⏰Time Zone App")# title For this application

# Create a multi-select dropdown 
selected_timezone = st.multiselect(
    "Select Timezones", TIME_ZONES, default=["UTC", "Asia/Karachi"]
)

st.subheader("⏱️Selected Timezones...")# Display current time for selected time zones

for tz in selected_timezone:
    # Get and format current time for each selected timezone with AM/PM
    current_time = datetime.now(ZoneInfo(tz)).strftime("%Y-%m-%d %I:%M:%S %p")
    # Display timezone and its current time
    st.write(f"**{tz}**: {current_time}")

# Create section for time conversion
st.subheader("⏳Convert Time Between Different Timezones")
# Create time input field with current time as default
current_time = st.time_input("Current Time", value=datetime.now().time())
# Dropdown to select source timezone
from_tz = st.selectbox("From Timezone", TIME_ZONES, index=0)
# Dropdown to select target timezone
to_tz = st.selectbox("To Timezone", TIME_ZONES, index=1)

# Button
if st.button("🏆Convert Time..."):
    # Combine today's date with input time and source timezone
    dt = datetime.combine(datetime.today(), current_time, tzinfo=ZoneInfo(from_tz))
    # Convert time to target timezone and format it with AM/PM
    converted_time = dt.astimezone(ZoneInfo(to_tz)).strftime("%Y-%m-%d %I:%M:%S %p")
    st.success(f"Converted Time in {to_tz}: {converted_time}")    # Display the converted time with success message
