from database.professional_repository import ProfessionalRepository


class SearchProfessionalsTool:

    @staticmethod
    def run(city=None, role=None, company_tier=None, limit=5):

        results = ProfessionalRepository.find_professionals(
            city=city,
            role=role,
            company_tier=company_tier,
            limit=limit
        )

        formatted = []

        for r in results:
            formatted.append({
                "name": r.get("name"),
                "email": r.get("email"),  # ⭐ ADD THIS LINE
                "role": r.get("role"),
                "city": r.get("city"),
                "company": r.get("company"),
                "company_tier": r.get("company_tier"),
                "tech_stack": r.get("tech_stack"),
                "experience": r.get("years_experience")
            })

        return formatted