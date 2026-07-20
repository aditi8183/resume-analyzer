from logger import logger

from phase4.skill_matcher import (
    SkillMatcher
)

from phase4.keyword_matcher import (
    KeywordMatcher
)

from phase4.gap_analyzer import (
    GapAnalyzer
)

from phase4.score_calculator import (
    ScoreCalculator
)

from phase4.recommendation_engine import (
    RecommendationEngine
)

from phase4.job_level_detector import (
    JobLevelDetector
)

from phase4.education_matcher import (
    EducationMatcher
)

from phase4.certification_matcher import (
    CertificationMatcher
)


class Matcher:

    def match(

        self,

        resume_profile,
        jd_profile

    ):
        print("MATCHER RECEIVED JD PROFILE")
        print(jd_profile)
        print(type(jd_profile))
        print("JD SKILLS =", jd_profile.get("skills"))
        print("RESUME PROFILE KEYS:", resume_profile.keys())
        print("JD PROFILE KEYS:", jd_profile.keys())

        print("RESUME SKILLS:", resume_profile.get("skills"))
        print("JD SKILLS:", jd_profile.get("skills"))
        try:
          skill_result =SkillMatcher.match(

                resume_profile[
                    "skills"
                ],

                jd_profile[
                    "skills"
                ]

            )
        except Exception as e:
           print("SKILL MATCH ERROR:", e)
           raise

        

        keyword_result = (

            KeywordMatcher
            .match(

                resume_profile[
                    "keywords"
                ],

                jd_profile[
                    "keywords"
                ]

            )

        )

        gap_result = (

            GapAnalyzer
            .analyze(

                resume_profile[
                    "experience"
                ],

                jd_profile[
                    "experience"
                ],

                skill_result[
                    "missing"
                ]

            )

        )

        education_result = (

            EducationMatcher
            .match(

                resume_profile.get(
                    "education",
                    []
                )

            )

        )
        print(
            "EDUCATION RESULT:",
              education_result
        )

        certification_result = (

            CertificationMatcher
            .match(

                resume_profile.get(
                    "certifications",
                    []
                )

            )

        )

        score_result = (

            ScoreCalculator
            .calculate(

                skill_result[
                    "score"
                ],

                keyword_result[
                    "score"
                ],

                gap_result[
                    "gap"
                ],

                len(

                    skill_result[
                        "critical_missing"
                    ]

                ),

                education_result[
                    "education_score"
                ],

                certification_result[
                    "certification_score"
                ]

            )

        )

        recommendations = (

            RecommendationEngine
            .generate(

                skill_result[
                    "missing"
                ],

                gap_result[
                    "critical_missing"
                ],

                gap_result[
                    "gap"
                ]

            )

        )

        job_level = (

            JobLevelDetector
            .detect(

                jd_profile[
                    "experience"
                ]

            )

        )

        logger.info(
            "Phase 4 completed"
        )

        return {

            "scores": {

                "skill_score":
                    score_result[
                        "skill_score"
                    ],

                "keyword_score":
                    score_result[
                        "keyword_score"
                    ],

                "experience_score":
                    score_result[
                        "experience_score"
                    ],

                "education_score":
                    score_result[
                        "education_score"
                    ],

                "certification_score":
                    score_result[
                        "certification_score"
                    ],

                "ats_score":
                    score_result[
                        "ats_score"
                    ],

                "fit_level":
                    score_result[
                        "fit_level"
                    ]

            },

            "matching": {

                "matched_skills":
                    skill_result[
                        "matched"
                    ],
                "matched_keywords":
                    keyword_result[
                      "matched"
                    ],

                "matched_degree":
                    education_result[
                        "matched_degree"
                    ],

                "matched_certifications":
                    certification_result[
                        "matched_certifications"
                    ]

            },

            "gaps": {

                "missing_skills":
                    skill_result[
                        "missing"
                    ],
                "missing_keywords":
                    keyword_result[
                       "missing"
                    ],

                "critical_missing":
                   list(
                       set(
                   
                    skill_result[
                        "critical_missing"
                    ]
                       )
                   ),

                "experience_gap":
                    gap_result[
                        "gap"
                    ]

            },

            "job_level":
                job_level,

            "recommendations":
                recommendations

        }