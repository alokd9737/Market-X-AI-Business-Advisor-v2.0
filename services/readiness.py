from dataclasses import dataclass


@dataclass
class ReadinessResult:

    score: int

    maturity: str

    color: str

    recommendations: list


class ReadinessEngine:

    @staticmethod
    def calculate(values):

        score = round(sum(values) / len(values))

        if score >= 85:

            return ReadinessResult(

                score,

                "Excellent",

                "green",

                [

                    "Accelerate expansion",

                    "Focus on execution",

                    "Scale distribution"

                ]

            )

        elif score >= 70:

            return ReadinessResult(

                score,

                "Good",

                "orange",

                [

                    "Strengthen sales capability",

                    "Improve planning",

                    "Optimize GTM"

                ]

            )

        elif score >= 50:

            return ReadinessResult(

                score,

                "Average",

                "red",

                [

                    "Improve internal processes",

                    "Strengthen leadership",

                    "Improve market understanding"

                ]

            )

        return ReadinessResult(

            score,

            "Needs Improvement",

            "red",

            [

                "Business transformation required",

                "Develop strategy",

                "Build sales capability"

            ]

        )
