import streamlit as st
st.set_page_config(
    page_title="Course Recommendation Expert System",
    page_icon="🎓",
    layout="wide"
)
st.markdown(
    """
    <style>
    .main {
        padding-top: 2rem;
    }

    .hero {
        padding: 2rem;
        border-radius: 20px;
        text-align: center;
        margin-bottom: 2rem;
        background: linear-gradient(135deg, #667eea, #764ba2);
        color: white;
    }

    .hero-icon {
        font-size: 3rem;
    }

    .hero h1 {
        color: white;
        margin-bottom: 0.5rem;
    }

    .hero p {
        font-size: 1.1rem;
        margin-bottom: 0;
    }
    </style>
    """,
    unsafe_allow_html=True
)
from knowledge_base import courses
from inference_engine import recommend_courses
st.sidebar.title("📘 About the System")

st.sidebar.write(
    "This Course Recommendation Expert System uses "
    "rule-based reasoning to suggest suitable courses."
)

st.sidebar.write(
    "**Inputs:** Interests, Skill Level, Learning Preference"
)

st.sidebar.write(
    "**Output:** Ranked Course Suggestions"
)

st.markdown(
    """
    <div class="hero">
        <div class="hero-icon">🎓</div>
        <h1>Course Recommendation Expert System</h1>
        <p>
            Discover courses that match your interests, skill level,
            and preferred learning style.
        </p>
    </div>
    """,
    unsafe_allow_html=True
)

st.write("Welcome to our Course Recommendation System!")
st.subheader("👤 Tell us about yourself")
st.write("Choose your preferences to receive personalized course suggestions.")

name = st.text_input("Enter your name")

if name:
    st.info(f"Welcome, {name}! Please select your preferences below.")

interests = st.multiselect(
    "Select your interests",
    [
        "Programming",
        "Web Development",
        "Data Science",
        "Cybersecurity",
        "Design"
    ]
)

skill_level = st.selectbox(
    "Select your skill level",
    [
        "Beginner",
        "Intermediate",
        "Advanced"
    ]
)
learning_preference = st.selectbox(
    "How do you prefer to learn?",
    [
        "Practical Projects",
        "Theory",
        "Both"
    ]
)

if st.button(
    "🎓 Get My Course Recommendations",
    type="primary",
    use_container_width=True
):

    if not interests:
        st.warning("Please select at least one interest.")

    else:
        recommended_courses = recommend_courses(
            interests,
            skill_level,
            learning_preference,
            courses
        )

        if recommended_courses:

            st.success("Recommended Courses:")
            st.write(f"Here are the best course suggestions for you, {name}😊.")

            for recommendation in recommended_courses:

                course = recommendation["course"]
                score = recommendation["score"]

                with st.container(border=True):

                    st.subheader("🎓 " + course["course"])

                    st.write("**Match Score:**", str(score) + "%")

                    st.progress(score / 100)

                    st.write("💡 **Why this course?**")
                    st.write(course["reason"])

        else:
            st.info(
                "No matching courses found. "
                "Please try different interests, skill level, "
                "or learning preference."
            )

st.divider()
st.subheader("Project Information")

st.write(
    "This project demonstrates a rule-based expert system "
    "for recommending courses according to a learner's preferences."
)
st.subheader("System Inputs")

st.write(
    "The system uses three inputs to generate course recommendations:"
)

st.write(
    "1. Interests – areas the learner is interested in."
)

st.write(
    "2. Skill Level – Beginner, Intermediate, or Advanced."
)

st.write(
    "3. Learning Preference – Practical Projects, Theory, or Both."
)
st.subheader("System Output")

st.write(
    "Based on the selected inputs, the system provides "
    "ranked course suggestions with match scores and reasons."
)
st.subheader("Knowledge Base")

st.write(
    "The knowledge base contains course rules defined using "
    "interest, skill level, learning preference, and course information."
)
st.subheader("How does the system work?")

st.write(
    "The system analyzes your interests, skill level, and learning preference "
    "using rule-based scoring. It then ranks the most suitable courses."
)

st.write(
    "Interest match = 50 points, "
    "Skill level match = 30 points, "
    "and Learning preference match = 20 points."
)
st.caption("Course Recommendation Expert System | Built with Python and Streamlit")