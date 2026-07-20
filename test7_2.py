from phase7_2.experience_engine import (
    ExperienceEngine
)

resume_profile = {

    "experience_details": [

        "Python Developer at ABC Company",

        "AWS Cloud Intern",

        "Customer Support Executive"

    ]
}

jd_profile = {

    "skills": [

        "python",

        "aws",

        "docker",

        "machine learning"

    ]
}

result = (

    ExperienceEngine()
    .analyze(

        resume_profile,

        jd_profile

    )

)

print(
    result
)