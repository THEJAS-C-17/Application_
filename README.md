# Application_
A Health Monitoring system developed using python
# Music and Nutrition Application

This is a Python-based application that combines two unique functionalities:  
1. **Music Management with Spotify API Integration**  
2. **Nutrition Calculation Based on User Details**

Built using **Tkinter** and **CustomTkinter** for the GUI, this project incorporates **Spotify API** to fetch user music data and provides **personalized nutrition guidance**.

---

## Key Features:
### **Music Management:**
- **Spotify Integration:**  
  The app integrates with Spotify API to fetch and process user music data.
- **Achievements System:**  
  Tracks and awards achievements for interacting with Spotify (e.g., saved tracks).
- **User Leveling System:**  
  Users gain experience points (XP) for each achievement, allowing them to level up.
- **Music Display:**  
  Displays saved Spotify tracks with detailed information (e.g., track name, artist).

### **Nutrition Guidance:**
- **User Input Details:**  
  Users can input their gender, weight, height, age, and activity level.
- **Calories and Macronutrient Calculation:**  
  - Calculates Basal Metabolic Rate (BMR) and total calories required based on activity level.  
  - Determines the optimal intake of protein, carbohydrates, and fats.
- **Personalized Recommendations:**  
  Provides detailed nutritional guidance, including calorie breakdown and macronutrient distribution.
- **Interactive GUI:**  
  User-friendly interface with inputs for personalized results.

---

## How It Works:
### **Login System:**
1. Users log in with a pre-set username and password.
2. Upon successful login, they are directed to a dashboard with options for:
   - Nutrition Calculation
   - Music Management

### **Music Integration Workflow:**
1. **Spotify Authorization:**  
   Connects to the user's Spotify account using OAuth2.
2. **Fetch Saved Tracks:**  
   Retrieves the 10 most recently saved tracks from the user's Spotify library.
3. **Achievements and Experience:**  
   - For every track, the app assigns an achievement.  
   - Users gain experience points (XP) for every achievement.

### **Nutrition Guidance Workflow:**
1. **Input Details:**  
   Users input their:
   - Gender  
   - Weight (kg)  
   - Height (cm)  
   - Age  
   - Activity Level (e.g., sedentary, active).
2. **BMR and Calorie Calculation:**  
   Calculates daily calorie needs based on the Harris-Benedict equation and activity multipliers.
3. **Macronutrient Breakdown:**  
   - Protein, carbohydrate, and fat distribution is calculated based on user-specific calorie needs.
4. **Output:**  
   Results are displayed in a new window with a background image for a better user experience.

---

## Technologies Used:
- **Python:** The core programming language for logic and GUI.
- **Tkinter/CustomTkinter:** For the graphical user interface.
- **Spotify API (Spotipy):** For fetching and processing user music data.
- **Pillow:** For handling and displaying images as window backgrounds.

---

## Screenshots:
1. **Login Screen:**  
   A secure and aesthetic login page for accessing the application.
2. **Dashboard:**  
   Options for either entering nutrition details or interacting with Spotify music.
3. **Nutrition Guidance Window:**  
   Displays user-specific nutrition recommendations, including calorie and macronutrient breakdown.
4. **Music Achievements:**  
   Displays Spotify track achievements and user experience progress.

---

## Future Enhancements:
- **User Authentication:**  
  Add a secure user authentication system with multiple user support.
- **Advanced Nutrition Features:**  
  - Recommendations for weight loss, maintenance, or gain.  
  - Integration with fitness tracking apps or APIs.
- **Improved Music Integration:**  
  - Add functionality for playlist creation and management via Spotify API.  
  - Include music visualization or analytics.
- **Gamification Features:**  
  - Introduce badges, challenges, and a leaderboard system.
- **Database Integration:**  
  Store user data (e.g., nutrition logs, achievements) persistently using SQLite.

---

## Why This Project?
This project is ideal for:
- **Learning:** A hands-on way to explore GUI design, Spotify API, and calculations in Python.
- **NLP and API Integration:** Understand how to use APIs to enhance application functionality.
- **Health and Lifestyle Applications:** A prototype for health and fitness-related software.
- **Gamification Principles:** Experience designing a leveling and achievement system.

---

## Project Structure:
1. **Login System:**  
   Secure access to the dashboard.
2. **Dashboard:**  
   Provides a central hub for navigation.
3. **Nutrition Module:**  
   - Input collection and validation.  
   - Calorie and macronutrient calculations.  
   - Results display with personalized recommendations.
4. **Music Module:**  
   - Spotify API integration.  
   - Achievements and leveling system.

---

Feel free to fork this repository, suggest enhancements, or contribute to its development!
