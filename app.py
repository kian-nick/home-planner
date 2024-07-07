import streamlit as st
import json

# Function to load data
def load_data():
    try:
        with open('data.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {"idea_boards": []}

# Function to save data
def save_data(data):
    with open('data.json', 'w') as f:
        json.dump(data, f)

# Main app
def main():
    st.title("Home Planning Helper")

    # Load data
    data = load_data()

    # Sidebar for navigation
    page = st.sidebar.radio("Go to", ["Idea Boards", "Room Planner", "Budget Calculator"])

    if page == "Idea Boards":
        idea_boards(data)
    elif page == "Room Planner":
        room_planner()
    elif page == "Budget Calculator":
        budget_calculator()

    # Save data after any changes
    save_data(data)

# Idea Boards page
def idea_boards(data):
    st.header("Idea Boards")

    # Create new board
    with st.form("new_board"):
        title = st.text_input("Board Title")
        description = st.text_area("Board Description")
        if st.form_submit_button("Create Board"):
            data['idea_boards'].append({"title": title, "description": description})
            st.success(f"Board '{title}' created!")

    # Display existing boards
    for i, board in enumerate(data['idea_boards']):
        st.subheader(board['title'])
        st.write(board['description'])
        if st.button(f"Delete Board {i}"):
            data['idea_boards'].pop(i)
            st.experimental_rerun()

# Room Planner page (placeholder)
def room_planner():
    st.header("Room Planner")
    st.write("Room planner feature coming soon!")

# Budget Calculator page (placeholder)
def budget_calculator():
    st.header("Budget Calculator")
    st.write("Budget calculator feature coming soon!")

if __name__ == "__main__":
    main()