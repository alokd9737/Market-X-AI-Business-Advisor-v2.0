import re


class BusinessAnalyzer:

    @staticmethod
    def analyze(question):

        text = question.lower()

        analysis = {

            "industry": None,

            "expansion": False,

            "distribution": False,

            "sales": False,

            "government": False,

            "manufacturing": False,

            "brand": False

        }

        if "distribution" in text:

            analysis["distribution"] = True

        if "sales" in text:

            analysis["sales"] = True

        if "government" in text:

            analysis["government"] = True

        if "factory" in text or "manufacturing" in text:

            analysis["manufacturing"] = True

        if "brand" in text:

            analysis["brand"] = True

        if "expand" in text or "market" in text:

            analysis["expansion"] = True

        return analysis
