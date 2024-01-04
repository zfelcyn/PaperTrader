import streamlit as st

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

# Number of times to run the selection process
num_iterations = 25

# Initialize a counter for each member
member_counter = {member['Name']: 0 for member in members_data}

# Display the title
st.title("Member Selection Events")

# Perform the selection process for a specified number of iterations
for i in range(num_iterations):
    selected_members = []

    # Select 2 freshmen until every member of the junior list has been selected
    if i < len([member for member in members_data if member['Grade'] == 'Junior']):
        selected_members.extend([member for member in members_data if member['Grade'] == 'Freshman'][i * 2 % 13:i * 2 % 13 + 2])
    else:
        # After every junior has been selected, start taking a third freshman
        selected_members.extend([member for member in members_data if member['Grade'] == 'Freshman'][i * 3 % 13:i * 3 % 13 + 3])

    # Select 1 junior
    selected_members.append([member for member in members_data if member['Grade'] == 'Junior'][i % 5])

    # Update the counters for each selected member
    for selected_member_list in selected_members:
        for selected_member in selected_member_list:
            member_counter[selected_member['Name']] += 1

    # Display the selected members for each iteration
    st.write(f"Iteration {i + 1}:\n{selected_members}")

# Display the final member selection statistics
st.write("\nMember Selection Statistics:")
for member, count in member_counter.items():
    st.write(f"{member}: {count} times")
