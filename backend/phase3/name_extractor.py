import re

class NameExtractor:

    @staticmethod
    def extract(text):

        blacklist = {
            "objective",
            "professional summary",
            "summary",
            "profile",
            "education",
            "skills",
            "experience",
            "work experience",
            "projects",
            "technical skills",
            "academic projects",
         "projects",
           "work experience",
          "experience",
           "summer vacation",
           "certifications",
           "hobbies",
           "profile",
           "resume"

        }

        lines = text.split("\n")
        print("TOP LINES:")
        for line in lines[:15]:
          print(line)
        for line in lines:

           clean = line.strip()

           if clean.lower() in blacklist:
              continue

           if any(char.isdigit() for char in clean):
              continue

           words = clean.split()

           if len(words) < 2 or len(words) > 4:
               continue

           return clean.title()
        return "Unknown Candidate"