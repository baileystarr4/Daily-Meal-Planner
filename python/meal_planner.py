from openai import OpenAI
import os
from dotenv import load_dotenv

class MealPlanner:
    def __init__(self, calories):
        self.calories = calories
        load_dotenv()
        self.client = OpenAI(api_key=os.getenv("API_KEY"))

    def get_meal_plan(self):
        response = self.client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "user", 
                "content": f"Give a {self.calories} calorie meal plan for one day. Include the calories, necessary ingredients, and a recipe for each meal."
                },
        ]
        )
        return response.choices[0].message.content
