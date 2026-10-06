def recommend_courses(interests, skill_level, learning_preference, courses):

    recommendations = []

    for course in courses:

        score = 0

        # Interest match
        if course["interest"] in interests:
            score += 50

        # Skill level match
        if course["skill_level"] == skill_level:
            score += 30

        # Learning preference match
        if (
            course["learning_preference"] == learning_preference
            or course["learning_preference"] == "Both"
            or learning_preference == "Both"
        ):
            score += 20

        # Only include courses with a match
        if course["interest"] in interests:
            recommendations.append({
                "course": course,
                "score": score
            })

    # Highest score first
    recommendations.sort(
        key=lambda item: item["score"],
        reverse=True
    )

    return recommendations