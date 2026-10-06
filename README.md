# 🎓 Course Recommendation Expert System

## Project Description

The Course Recommendation Expert System is a rule-based application developed using Python and Streamlit.

It recommends suitable courses based on a learner's:

- Interests
- Skill Level
- Learning Preference

## Features

- Multiple interest selection
- Beginner, Intermediate, and Advanced skill levels
- Practical Projects, Theory, and Both learning preferences
- Rule-based course recommendation
- Match score for each recommendation
- Explanation for why a course is recommended
- Interactive Streamlit user interface

## How the System Works

The system uses a knowledge base containing course information and a rule-based inference engine.

The recommendation score is calculated using:

- Interest match = 50 points
- Skill level match = 30 points
- Learning preference match = 20 points

The courses are then ranked according to their match score.

## Technologies Used

- Python
- Streamlit
- Git
- GitHub

## Project Structure

```text
CourseRecommendation/
├── .streamlit/
│   └── config.toml
├── app.py
├── knowledge_base.py
├── inference_engine.py
├── requirements.txt
└── .gitignore
