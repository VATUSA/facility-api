from dotenv import load_dotenv
from app.helpers.moodle.MoodleHelper import MoodleHelper


load_dotenv()
categories = MoodleHelper.get_all_categories()
courses = MoodleHelper.get_all_courses()

for course in courses:
    quizzes = MoodleHelper.get_quizzes_by_courses(course.get('id'))
    print()
