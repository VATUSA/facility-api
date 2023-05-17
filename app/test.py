from dotenv import load_dotenv
from app.helpers.moodle.MoodleHelper import MoodleHelper


load_dotenv()

data = MoodleHelper.get_all_courses()

print()
