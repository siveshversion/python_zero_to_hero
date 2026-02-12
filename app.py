import streamlit as st
from content import TOPICS
from utils import execute_code
from interview_questions import QUESTIONS

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
            selection = st.sidebar.radio("Go to", filtered_topics)
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
                
                # Code Editor
                code_input = st.text_area("Code", value=topic_content["example_code"], height=300)
                
                if st.button("Run Code"):
                    st.markdown("### Output")
                    output = execute_code(code_input)
                    st.code(output)
    
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
    st.sidebar.info("Built with Streamlit")

if __name__ == "__main__":
    main()
