from app.services.llm import LLMService


class ChatService:
    def __init__(self) -> None:
        self.llm_service = LLMService()

    async def process_message(
        self,
        question: str,
    ) -> str:
        answer = await self.llm_service.generate_response(
            question=question,
        )

        return answer
