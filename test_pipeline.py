from services.ats_pipeline import (
    ATSPipeline
)

output = (

    ATSPipeline.run(

        "cv (1).pdf",

        "sample_data_scientist_jd.pdf"

    )

)

print(

    output[
        "result"
    ]
)