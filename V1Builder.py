import requests
from typing import List, Dict

# CSS for styling the PDF
cssfile = """
body {
    font-family: Arial, sans-serif;
    padding: 20px;
    margin: 0;
}
h1 {
    color: MidnightBlue;
    text-align: center;
}
h3 {
    color: MidnightBlue;
    border-bottom: 1px solid #ddd;
    padding-bottom: 5px;
}
li {
    margin-top: 5px;
}
.container {
    max-width: 800px;
    margin: auto;
}
img {
    display: block;
    margin: 0 auto 20px;
    max-width: 150px;
    border-radius: 50%;
}
"""

def convert_markdown_to_pdf(markdown_content: str, Resume_file: str = "Resume.pdf", engine: str = "weasyprint"):
    """Convert Markdown content to PDF using an API."""
    url = "https://md-to-pdf.fly.dev"
    data = {
        'markdown': markdown_content,
        'css': cssfile,
        'engine': engine
    }

    response = requests.post(url, data=data)

    if response.status_code == 200:
        with open(Resume_file, 'wb') as f:
            f.write(response.content)
        print(f"PDF saved to {Resume_file}")
    else:
        print(f"Error {response.status_code}: {response.text}")

class Resume:
    def __init__(self, name: str, email: str, mobile: str, education: List[Dict], skills: str, experience: List[Dict], projects: List[Dict], achievements: List[str], activities: str, image_url: str = None):
        self.name = name
        self.email = email
        self.mobile = mobile
        self.education = education
        self.skills = skills
        self.experience = experience
        self.projects = projects
        self.achievements = achievements
        self.activities = activities
        self.image_url = image_url

    def generate_markdown(self) -> str:
        markdown_text = f"<div class='container'>\n"
        
        if self.image_url:
            markdown_text += f"<img src='{self.image_url}' alt='Profile Picture'>\n"
        
        markdown_text += f"<h1>{self.name}</h1>\n<p style='text-align:center;'>Email: {self.email} | Mobile: {self.mobile}</p>\n\n"
        
        markdown_text += "### Education\n\n"
        for edu in self.education:
            markdown_text += f"- {edu['level']}: {edu['institution']} | {edu['field']} | Score: {edu['score']} | {edu['duration']}.\n"
        
        markdown_text += "\n### Skills\n\n"
        markdown_text += f"{self.skills}\n"
        
        markdown_text += "\n### Experience\n\n"
        for exp in self.experience:
            markdown_text += f"- **{exp['job_role']}({exp['company_name']})**: {exp['description']}\n"
        
        markdown_text += "\n### Projects\n\n"
        for proj in self.projects:
            markdown_text += f"- **{proj['name']}**: {proj['description']}\n"
        
        markdown_text += "\n### Achievements\n\n"
        for ach in self.achievements:
            markdown_text += f"- {ach}\n"
        
        markdown_text += "\n### Other Activities\n\n"
        markdown_text += self.activities + '\n'
        
        markdown_text += "</div>\n"
        return markdown_text

def get_user_input() -> Resume:
    name = input("Enter your name: ")
    email = input("Enter your email: ")
    mobile = input("Enter your mobile number: ")
    image_url = input("Enter the URL of your profile picture (optional): ")

    education = []
    while True:
        edu_input = input("Do you want to add education details? (yes/no): ").lower()
        if edu_input != 'yes':
            break
        level = input("Enter education level (e.g., Graduation(UG/PG), High School): ")
        institution = input(f"Enter the name of the {level} institution: ")
        field = input(f"Enter the field of study at {institution}: ")
        duration = input(f"Enter passing year of {level} at {institution}: ")
        score = input(f"Enter your score (e.g., GPA/Percentage) of {level} at {institution}: ")
        education.append({"level": level, "institution": institution, "field": field, "duration": duration, "score": score})

    skills = input("\nEnter your skills (comma-separated): ")

    experience = []
    while True:
        job_role = input("Enter your job role (or type 'done' to finish): ")
        if job_role.lower() == 'done':
            break
        exp_company_name = input("Enter the company name: ")
        exp_description = input(f"Enter the description for '{job_role}': ")
        experience.append({"job_role": job_role, "company_name": exp_company_name, "description": exp_description})

    projects = []
    while True:
        proj_heading = input("Enter the project Title (or type 'done' to finish): ")
        if proj_heading.lower() == 'done':
            break
        proj_description = input(f"Enter the description for '{proj_heading}': ")
        projects.append({"name": proj_heading, "description": proj_description})

    achievements = []
    while True:
        ach_input = input("Enter an achievement detail (or type 'done' to finish): ")
        if ach_input.lower() == 'done':
            break
        achievements.append(ach_input)

    activities = input("Enter your other activities: ")
    return Resume(name, email, mobile, education, skills, experience, projects, achievements, activities, image_url)

if __name__ == "__main__":
    user_resume = get_user_input()
    markdown_text = user_resume.generate_markdown()
    convert_markdown_to_pdf(markdown_text)
