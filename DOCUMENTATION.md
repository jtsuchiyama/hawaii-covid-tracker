# Documentation

# Breakdown of Programs
# app.py
When ran, it will update data.csv with today's count of COVID-19 cases in the entire state and all counties in Hawaii. Requires an account with Twilio. In phoneNumbers.txt, write the registered phone numbers, each of which is separated by a tab. Only include the numbers. In token.txt, write your Twilio account SID, authentication token, and Twilio phone number in that order. Separate each by a tab. 

# gui.py
When ran, it will display a GUI that allow the user to display the desired graph. 
- Duration Type: This field controls whether the graph displays the data from a range x to y or data from the last z amount of days (The variables which are controlled by editing the parameters at the very top).
- Datatype: This field controls whether the graph displays the total amount of cases or the change in the amount of cases from the previous entry.
- Checkboxes: Checking any of these fields will display the respective island data on the graph when 'Submit' is pressed

# Suggested Uses
# Daily COVID-SMS Notifications
- The program works accurately when it is app.py is ran every day. Either manually run the program daily or set it up the run automatically using the Task Scheduler feature on Windows
