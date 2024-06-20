```bash

Resume Builder

This project provides a Python script to generate a professional resume from user input. It collects user details, converts the information into Markdown format, and uses an API to convert the Markdown into a stylish PDF.

Features:
- Collect user details interactively
- Generate a Markdown formatted resume
- Convert Markdown to PDF using an online API
- Modern and clean CSS styling for the resume
- Option to include a profile picture

Requirements:
- Python 3.x
- requests library

# Clone the repository
Cloning the repository...
git clone https://github.com/socratis-01/resume-builder.git
cd resume-generator

# Install the required Python package
Installing required Python package...
pip install requests

# Run the script
Running the script...
python V1Builder.py

# Example of the interaction

Example of user interaction:

Enter your name: John Doe
Enter your email: john.doe@example.com
Enter your mobile number: +123456789
Enter the URL of your profile picture (optional): https://example.com/profile.jpg

Education:
Do you want to add education details? (yes/no): yes
Enter education level (e.g., Graduation(UG/PG), High School): Graduation
Enter the name of the Graduation institution: XYZ University
Enter the field of study at XYZ University: Computer Science
Enter passing year of Graduation at XYZ University: 2020
Enter your score (e.g., GPA/Percentage) of Graduation at XYZ University: 3.8

Skills:
Enter your skills (comma-separated): Python, Java, C++

Experience:
Enter your job role (or type 'done' to finish): Software Developer
Enter the company name: ABC Corp
Enter the description for 'Software Developer': Developed and maintained web applications

Projects:
Enter the project Title (or type 'done' to finish): Resume Generator
Enter the description for 'Resume Generator': A script to generate resumes from user input

Notes:
- Ensure the requests library is installed before running the script.
- You can customize the CSS styling in the cssfile variable within the script for a different look and feel.
```
