from phase7_1.project_engine import (
    ProjectEngine
)

resume_profile = {

    "projects": [

        "CNN Image Classification using OpenCV",

        "Library Management System",

        "Customer Churn Prediction using Machine Learning"

    ]
}

jd_profile = {

    "skills": [

        "computer vision",

        "deep learning",

        "machine learning"

    ]
}

result = (

    ProjectEngine()
    .analyze(

        resume_profile,

        jd_profile

    )

)

print(
    result
)