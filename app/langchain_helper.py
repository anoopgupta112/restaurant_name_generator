import google.generativeai as genai
from app.config import config

class RestaurantGenerator:
    def __init__(self):
        genai.configure(api_key=config.GEMINI_API_KEY)
        self.model = genai.GenerativeModel("gemini-1.5-flash")

    def generate_restaurant_name_and_items(self, cuisine):
        prompt_name = f"I want to open a restaurant for {cuisine} food. Suggest a fancy name for this."

        name_response = self.model.generate_content(prompt_name)
        restaurant_name = name_response.text.strip()

        prompt_menu = f"Suggest some menu items for {restaurant_name}. Return them as a comma-separated string."
        menu_response = self.model.generate_content(prompt_menu)
        menu_items = menu_response.text.strip()

        return {
            "restaurant_name": restaurant_name,
            "menu_items": menu_items
        }

if __name__ == "__main__":
    generator = RestaurantGenerator()
    response = generator.generate_restaurant_name_and_items("Italian")

    print("Restaurant Name:", response['restaurant_name'])
    print("Menu Items:", response['menu_items'].split(","))