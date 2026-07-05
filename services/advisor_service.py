from services.business_analyzer import BusinessAnalyzer
analysis = BusinessAnalyzer.analyze(question)
from ai.knowledge import KnowledgeBase
from ai.groq_client import GroqClient
from components.executive_metrics import executive_metrics

executive_metrics()


class AdvisorService:

    def __init__(self):

        self.kb = KnowledgeBase()

        self.llm = GroqClient()

    def generate_advisory(
        self,
        question,
        industry,
        geography,
        company_size,
        diagnostics=None,
    ):

        query = f"""
Industry:
{industry}

Geography:
{geography}

Company Size:
{company_size}

Business Question:
{question}
"""

        context, sources = self.kb.search(query)

        answer = self.llm.ask(
            question=query,
            context=context,
            diagnostics=diagnostics,
        )

        return {
            "answer": answer,
            "sources": sources,
            "context": context,
        }
