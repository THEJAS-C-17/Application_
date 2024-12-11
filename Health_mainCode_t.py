#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from tkinter import Tk, Toplevel, Label, Entry, Button, messagebox
from customtkinter import CTk, CTkFrame, CTkButton, CTkLabel, CTkEntry
from PIL import Image, ImageTk
import spotipy
from spotipy.oauth2 import SpotifyOAuth

def set_background(window, image_path):
    image = Image.open(image_path)
    photo = ImageTk.PhotoImage(image)
    label = Label(window, image=photo)
    label.image = photo
    label.place(x=0, y=0, relwidth=1, relheight=1)

class User:
    def __init__(self, name):
        self.name = name
        self.level = 1
        self.experience = 0
        self.achievements = {}

    def earn_experience(self, exp):
        self.experience += exp
        if self.experience >= 100:
            self.level_up()

    def level_up(self):
        self.level += 1
        self.experience -= 100
        print(f"Congratulations, {self.name}! You've reached Level {self.level}.")

    def add_achievement(self, achievement):
        if achievement not in self.achievements:
            self.achievements[achievement] = 1
        else:
            self.achievements[achievement] += 1


class MusicApp:
    def __init__(self):
        self.users = {}
        self.sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id='YOUR_CLIENT_ID',
                                                            client_secret='YOUR_CLIENT_SECRET',
                                                            redirect_uri='YOUR_REDIRECT_URI',
                                                            scope='user-library-read'))

    def add_user(self, user):
        self.users[user.name] = user

    def process_spotify_input(self, user):
        results = self.sp.current_user_saved_tracks(limit=10)
        for idx, item in enumerate(results['items']):
            track = item['track']
            achievement = f"Saved track: {track['name']} by {', '.join([artist['name'] for artist in track['artists']])}"
            user.add_achievement(achievement)
            user.earn_experience(20)  # User gains 20 experience points for each saved track

    def display_user_info(self, user):
        print(f"User: {user.name}")
        print(f"Level: {user.level}")
        print(f"Experience: {user.experience}")
        print("Achievements:")
        for achievement, count in user.achievements.items():
            print(f"- {achievement}: {count}")

def start_music_app():
    app = MusicApp()

    # Create a default user (optional)
    default_user = User("Default User")
    app.add_user(default_user)

    # Process Spotify input for the default user
    app.process_spotify_input(default_user)

    # Display user information
    app.display_user_info(default_user)

def calculate_nutrition():
    user_details_window = Toplevel()
    user_details_window.geometry("400x300+500+300")
    user_details_window.title("Enter Details")

    # Load and set background image for nutrition calculation window
    set_background(user_details_window, "../../Downloads/black_image.jpeg")#add image for third layout

    Label(user_details_window, text="Gender (male/female):").pack()
    gender_entry = Entry(user_details_window)
    gender_entry.pack()

    Label(user_details_window, text="Weight (kg):").pack()
    weight_entry = Entry(user_details_window)
    weight_entry.pack()

    Label(user_details_window, text="Height (cm):").pack()
    height_entry = Entry(user_details_window)
    height_entry.pack()

    Label(user_details_window, text="Age (years):").pack()
    age_entry = Entry(user_details_window)
    age_entry.pack()

    Label(user_details_window, text="Activity Level :").pack()
    activity_entry = Entry(user_details_window)
    activity_entry.pack()

    def calculate():
        gender = gender_entry.get().lower()
        weight_kg = float(weight_entry.get())
        height_cm = float(height_entry.get())
        age = int(age_entry.get())
        activity_level = activity_entry.get().lower()

        if gender == "male":
            bmr = calculate_bmr_male(weight_kg, height_cm, age)
        elif gender == "female":
            bmr = calculate_bmr_female(weight_kg, height_cm, age)
        else:
            messagebox.showerror("Error", "Invalid input for gender.")
            return

        activity_levels = ["sedentary", "lightly active", "moderately active", "very active", "extra active"]
        if activity_level in activity_levels:
            total_calories = calculate_calories(bmr, activity_level)
        else:
            messagebox.showerror("Error", "Invalid input for activity level.")
            return

        protein, carbs, fats = calculate_macros(total_calories, weight_kg)

        nutrition_window = Toplevel()
        nutrition_window.geometry("400x300+500+300")
        nutrition_window.title("Nutrition Guidance")

        # Load and set background image for nutrition guidance window
        set_background(nutrition_window, "../../Downloads/openart-image_EHfGehhC_1711264316750_raw.jpg")#last photo

        Label(nutrition_window, text=f"Total Calories per day: {round(total_calories, 2)}").pack()
        Label(nutrition_window, text=f"Protein: {round(protein,2)} grams").pack()
        Label(nutrition_window, text=f"Carbohydrates: {round(carbs, 2)} grams").pack()
        Label(nutrition_window, text=f"Fats: {round(fats, 2)} grams").pack()

    Button(user_details_window, text="Calculate Nutrition", command=calculate).pack()

def calculate_bmr_male(weight_kg, height_cm, age):
    bmr = (10 * weight_kg) + (6.25 * height_cm) - (5 * age) + 5
    return bmr

def calculate_bmr_female(weight_kg, height_cm, age):
    bmr = (10 * weight_kg) + (6.25 * height_cm) - (5 * age) + 161
    return bmr

def calculate_calories(bmr, activity_level):
    activity_multipliers = {
        "sedentary": 1.2,
        "lightly active": 1.375,
        "moderately active": 1.55,
        "very active": 1.725,
        "extra active": 1.9
    }
    return bmr * activity_multipliers[activity_level]

def calculate_macros(calories, weight_kg):
    protein_ratio = 0.8  # grams per kg - minimum
    carbs_ratio = 0.5  # percentage of daily calories
    fats_ratio = 0.35  # percentage of daily calories

    protein = protein_ratio * weight_kg
    carbs = (calories * carbs_ratio) / 4
    fats = (calories * fats_ratio) / 9

    return protein, carbs, fats

def login():
    username = "thejas"
    password = "12345"
    if username_entry.get() == username and password_entry.get() == password:
        messagebox.showinfo(title="Login Success", message="You successfully logged in.")
        show_dashboard()
    else:
        messagebox.showerror(title="Error", message="Invalid login.")

def show_dashboard():
    dashboard_window = Toplevel()
    dashboard_window.geometry("925x500+300+200")
    dashboard_window.title("Dashboard ")

    # Load and set background image for dashboard window
    set_background(dashboard_window, "side_image.jpeg")

    dashboard_frame = CTkFrame(master=dashboard_window, fg_color="grey", width=10, height=10)
    dashboard_frame.pack(fill="both", expand=True)

    CTkButton(master=dashboard_frame, text="Enter the details", command=calculate_nutrition).pack(expand=True, pady=50)
    CTkButton(master=dashboard_frame, text="MUSIC", command=start_music_app).pack(expand=True, pady=30)

# Main program
if __name__ == "__main__":
    app = CTk()
    app.geometry("925x500+300+200")
    app.title("Login")

    # Load and set background image for login window
    set_background(app, "../../Downloads/openart-image_0kG7c_Ny_1711263424778_raw.jpg")#1st background image set

    frame_3 = CTkFrame(master=app, fg_color="grey", width=10, height=10)
    frame_3.place(relx=0.5, rely=0.5, anchor="center")

    CTkLabel(master=frame_3, text="Login", font=("Arial Bold", 30), justify="left").pack(expand=True, pady=(80, 15))
    username_entry = CTkEntry(master=frame_3, placeholder_text="Enter your username", width=150)
    username_entry.pack(expand=True, pady=15, padx=20)
    password_entry = CTkEntry(master=frame_3, placeholder_text="Enter your password", width=150)
    password_entry.pack(expand=True, pady=15, padx=20)
    CTkButton(master=frame_3, text="Login", command=login).pack(expand=True, fill="both", pady=(80, 15), padx=60)

    app.mainloop()


