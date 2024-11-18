# Motivation Application to Track Streaks

This Python-based application is designed to help users track their progress and stay motivated by monitoring their streaks for a single task. The app provides an easy-to-use interface to log task completion and displays the current streak count, reinforcing daily habits and goal consistency.

## Motivation Behind the Project

Motivation is what drives us to excel in many aspects of life. With enough motivation, humans can achieve remarkable advancements. Historically, most technological innovations were spurred by the need to strengthen military forces, with survival being a powerful motivator.
<br>
However, in modern times, people often lose motivation quickly, which can hinder progress and slow down improvements. I discovered an effective method for maintaining motivation: the challenge. Humans thrive on challenges, which is why we find games so engaging. In games, the more difficult the challenge, the more invested people become in overcoming it.
<br>
Inspired by this idea, I wondered: Why not introduce a challenge into my own life to excel? I realized that commitment could be achieved by maintaining a streak of consistent effort in the same area. For example, I wanted to improve my skills in learning English, developing my mindset, and coding, in addition to learning embedded systems and front-end development. While a timetable helps plan out activities, it's the streak system that ensures I stick to it.
<br>
I experienced this first-hand when I committed to using language-learning apps like Duolingo and Elevated every day. The streak system not only kept me motivated but also helped me build consistency. Humans tend to value what they can preserve, and a streak—though simple—provides that sense of continuity and achievement.
<br>
Thus, I decided to build a project that tracks such streaks. The app is a GUI application programmed in Python, designed to track streaks and reward users visually as they reach certain milestones. The data is stored locally in a text file on the device, which acts as the backend for the application. The app does not require an internet connection—it simply reads the date from the device and processes it to keep the streak count.
<br>
By creating this application, I aim to help users build habits and maintain motivation, one streak at a time.
<br>

## Current Features:


- Streak Tracking:

- Tracks the number of consecutive days a user completes a task, starting with a count of 1.
- Automatically updates the streak count when the user logs their activity.

- Database Management:

- Saves the streak data in a local text file (database.txt) and creates a backup (backupdatabase.txt).
- If no existing data is found, initializes the streak with a count of 1 and the current date.
- Ensures data persistence through file-based storage, allowing the app to retain streak information even after closing and reopening.

- Log Display:

- Displays a list of dates when the user successfully logged in and completed the task.
- Updates the log with the current date each time the user logs a streak.
- Shows the current streak count and updates it after each successful login.

- User Interface (UI):

- Built using PyQt5, offering an intuitive graphical interface for logging and viewing streaks.
- Displays a list of all logged dates and updates the streak count dynamically.

- Backup and Recovery:

- Uses a backup database file to ensure that user data is not lost, even if the main database file is damaged or deleted.

## Future Work:
- Track Multiple Task Streaks:
- Extend the application to track streaks for multiple tasks simultaneously.
- Allow users to add, edit, and remove tasks, each with its own streak counter.
- Provide a detailed summary of all tasks, showing streaks for each one.

- Visual Enhancements:
- Add visual rewards like animations, badges, and motivational messages as the streaks increase.
- Unlock features and rewards at certain streak milestones (e.g., after 5 days, 10 days, etc.).

- Notification System:

- Implement daily reminders or push notifications to encourage users to log their streaks and keep their tasks on track.
AI Integration:

- Add an AI-driven chatbot to interact with the user and offer personalized motivational advice.
- Use AI to suggest improvements or adjust tasks based on the user’s activity trends.

- Data Insights:

- Provide insights or analytics to help users understand their streak patterns (e.g., average streak length, longest streak).
- Display motivational messages based on the streaks, such as congratulating the user for maintaining a long streak or encouraging them to start over if they miss a day.

- Gamification Features:

- Implement achievements and trophies for users to unlock based on their streaks.
- Provide a leader board or comparison feature to compare user progress with others.

- Mobile and Cloud Integration (Long-term):

- Consider implementing mobile app versions for easier access and tracking on the go.
- Enable cloud syncing to store streak data across devices, allowing users to access their progress from anywhere.

- Optimization:

- Optimize the file I/O operations for improved performance, especially when handling large amounts of streak data.
- Investigate the potential for using a more robust database solution (like SQLite) for better data management as the app grows in complexity.


## Installation

1. Clone or download the repository.
2. Ensure you have Python 3.x and PyQt5 installed.
3. Run the main.py script to launch the application.

```bash
git clone <repository-url>
cd Motivation-App
python main.py
```
## Requirements
- Python 3.x
- PyQt5
## Future Updates
Stay tuned for future updates and features as we continue to enhance the app!


<!-- ## Project:

Motivation is what drive us to excel in many thing. With enough motivation, mankind can achieve stunning development in many aspects of life. 
Most of technological advancement was done due to need to strengthen military forces as survival is best motivation. 
Nowadays, people often lose motivation quickly making improvements slow down. I discovered another way of keeping this motivation high. Humans love challenges. This is found often in games which is about tasks that you are assigned to do with a challenges. The harder the challenge is, the more engaged are the people who play this game. Therefore, why can't I introduce a challenge to myself to excel ?
I found that commitment can be achieved by making streak of working days on same topic for instance, I want to learn English , improve my mindset and learn coding in addition to learning fields like Embedded System and Front-end development. Time table is great idea but what will help me stick to this time table ? Only streak system will do. I found that when I committed myself to learning English using Duolingo and use Elevated app day by day. Humans love to preserve things what if these things was a streak, meaningless but help achieve high level skills. So, I decided to work on project which is an GUI Application programmed using Python which track streak and give visual reward as streak reach certain numbers. Data will be saved in txt file locally in the device which will act as backend to this project. No internet connection is need just read date from device and save it in txt file and process it. -->
