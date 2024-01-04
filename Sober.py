import pandas as pd
import random

# Member data
members_data = [
    {'Name': 'Eli', 'Grade': 'Freshman'},
    {'Name': 'Malcolm', 'Grade': 'Freshman'},
    {'Name': 'Cody', 'Grade': 'Freshman'},
    {'Name': 'Gage', 'Grade': 'Freshman'},
    {'Name': 'Gannon', 'Grade': 'Freshman'},
    {'Name': 'Tpain', 'Grade': 'Freshman'},
    {'Name': 'Logan', 'Grade': 'Freshman'},
    {'Name': 'Nic', 'Grade': 'Freshman'},
    {'Name': 'Rex', 'Grade': 'Freshman'},
    {'Name': 'Spencer Mack', 'Grade': 'Freshman'},
    {'Name': 'Ryan', 'Grade': 'Freshman'},
    {'Name': 'Rigo', 'Grade': 'Freshman'},
    {'Name': 'Braeden', 'Grade': 'Freshman'},
    {'Name': 'Nate', 'Grade': 'Sophomore'},
    {'Name': 'Wynn', 'Grade': 'Sophomore'},
    {'Name': 'Beef', 'Grade': 'Sophomore'},
    {'Name': 'Salvy', 'Grade': 'Sophomore'},
    {'Name': 'Felcyn', 'Grade': 'Sophomore'},
    {'Name': 'Mullin', 'Grade': 'Sophomore'},
    {'Name': 'Shepard', 'Grade': 'Sophomore'},
    {'Name': 'Antonio', 'Grade': 'Sophomore'},
    {'Name': 'Dylan', 'Grade': 'Sophomore'},
    {'Name': 'Owen', 'Grade': 'Sophomore'},
    {'Name': 'Pfeifer', 'Grade': 'Sophomore'},
    {'Name': 'Ben', 'Grade': 'Junior'},
    {'Name': 'TJ', 'Grade': 'Junior'},
    {'Name': 'Keegan', 'Grade': 'Junior'},
    {'Name': 'Tony', 'Grade': 'Junior'},
    {'Name': 'Ray', 'Grade': 'Junior'},
    {'Name': 'Brenden', 'Grade': 'Junior'},
    {'Name': 'Meyer', 'Grade': 'Junior'},
    {'Name': 'Evan', 'Grade': 'Junior'},
    {'Name': 'Karl', 'Grade': 'Junior'}
]

# Create a DataFrame from the member data
df = pd.DataFrame(members_data)

# Number of times to run the selection process (adjusted for around 100 events)
num_iterations = 25

# Initialize a counter for each member
member_counter = {member['Name']: 0 for member in members_data}

# Perform the selection process for a specified number of iterations
for _ in range(num_iterations):
    selected_members = pd.DataFrame()
    
    # Select at least 2 freshmen
    selected_members = selected_members.append(df[df['Grade'] == 'Freshman'].sample(2))

    # Select 1 sophomore and 1 junior
    selected_members = selected_members.append(df[df['Grade'] == 'Sophomore'].sample(1))
    selected_members = selected_members.append(df[df['Grade'] == 'Junior'].sample(1))
    
    # Update the counter for each selected member
    for index, row in selected_members.iterrows():
        member_counter[row['Name']] += 1

# Save the selected members to an Excel file in the working directory
selected_members.to_excel('member_selection.xlsx', index=False)

# Display the final member selection statistics
print("Member Selection Statistics:")
for member, count in member_counter.items():
    print(f"{member}: {count} times")

print("\nExcel file 'member_selection.xlsx' saved in the working directory.")