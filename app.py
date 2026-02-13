import streamlit as st
from content import TOPICS
from utils import execute_code
from interview_questions import QUESTIONS

from code_editor import code_editor

def update_selection(new_topic):
    st.session_state.topic_selection = new_topic

def main():
    st.set_page_config(
        page_title="Python Zero to Hero",
        page_icon="🐍",
        layout="wide",
        initial_sidebar_state="expanded"
    )

    # Hide Streamlit Style
    hide_st_style = """
            <style>
            footer {visibility: hidden;}
            </style>
            """
    st.markdown(hide_st_style, unsafe_allow_html=True)

    st.title("🐍 Python Zero to Hero")

    # Sidebar Navigation - Mode Selection
    st.sidebar.title("Navigation")
    app_mode = st.sidebar.radio("Choose Mode", ["Learn Python", "Interview Questions"])

    if app_mode == "Learn Python":
        st.markdown("### Learn Python interactive & easy!")
        st.sidebar.markdown("---")
        
        # Search & Navigation
        st.sidebar.header("Topics")
        search_query = st.sidebar.text_input("Search Topics", placeholder="e.g. OOP, Lists...").lower()
        
        all_topics = list(TOPICS.keys())
        filtered_topics = []
        for t in all_topics:
            if (search_query in t.lower() or 
                search_query in TOPICS[t]["theory"].lower() or 
                search_query in TOPICS[t]["example_code"].lower()):
                filtered_topics.append(t)
        
        if not filtered_topics:
            st.sidebar.warning("No topics found.")
            # Default to first available or show nothing/message
            topic_content = {"title": "Not Found", "theory": "### No matching topic found.", "example_code": "# Try searching for something else"}
            selection = None
        else:
            # Determine index for navigation
            # Use session state to handle programmatically setting the selection via buttons
            if "topic_selection" not in st.session_state:
                st.session_state.topic_selection = filtered_topics[0]

            # Ensure the current selection is valid for the current filtered list
            if st.session_state.topic_selection not in filtered_topics:
                 st.session_state.topic_selection = filtered_topics[0]

            selection = st.sidebar.radio("Go to", filtered_topics, key="topic_selection")
            topic_content = TOPICS[selection]

        if selection:
            # Main Content Area
            col1, col2 = st.columns([1, 1])

            with col1:
                st.header(topic_content["title"])
                st.markdown(topic_content["theory"])

            with col2:
                st.header("Interactive Code Editor")
                st.markdown("Edit the code below and click **Run** to see the output.")
                
                # Code Editor with Line Numbers
                response_dict = code_editor(
                    topic_content["example_code"],
                    lang="python",
                    height=[15, 30],
                    theme="default",
                    buttons=[],
                    options={"showLineNumbers": True, "wrap": True}
                )
                
                if response_dict['type'] == "submit" and len(response_dict['text']) != 0:
                     code_input = response_dict['text']
                else:
                     code_input = response_dict['text']

                # We keep the external run button for now as per plan, but code_editor can also have buttons.
                # However, code_editor returns the current state of code in 'text'.
                
                if st.button("Run Code"):
                    st.markdown("### Output")
                    # Use the code from the editor. If modified, response_dict['text'] holds the new code.
                    output = execute_code(code_input if code_input else topic_content["example_code"])
                    st.code(output)

            # --- Navigation Buttons ---
            st.markdown("---")
            nav_col1, nav_col2, nav_col3 = st.columns([1, 8, 1])
            
            current_index = filtered_topics.index(selection)
            
            with nav_col1:
                if current_index > 0:
                    st.button("← Previous", on_click=update_selection, args=(filtered_topics[current_index - 1],))
            
            with nav_col3:
                if current_index < len(filtered_topics) - 1:
                    st.button("Next →", on_click=update_selection, args=(filtered_topics[current_index + 1],))
    
    elif app_mode == "Interview Questions":
        st.markdown("### 🎓 Python Interview Questions")
        st.markdown("Test your knowledge with these frequently asked interview questions.")
        
        # Filter by category
        categories = ["All"] + sorted(list(set(q["category"] for q in QUESTIONS)))
        selected_category = st.sidebar.selectbox("Filter by Difficulty", categories)
        
        filtered_questions = QUESTIONS
        if selected_category != "All":
            filtered_questions = [q for q in QUESTIONS if q["category"] == selected_category]
        
        st.info(f"Showing {len(filtered_questions)} questions ({selected_category})")
        
        for i, q in enumerate(filtered_questions):
            with st.expander(f"Q{i+1}: {q['question']} ({q['category']})"):
                st.markdown(f"**Answer:** {q['answer']}")

    # Footer
    st.sidebar.markdown("---")

if __name__ == "__main__":
    main()
