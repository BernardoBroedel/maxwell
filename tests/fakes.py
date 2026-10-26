from langchain_core.language_models.fake_chat_models import GenericFakeChatModel


class FakeChatModel(GenericFakeChatModel):
    """Modelo falso que aceita bind_tools e devolve as mensagens pré-definidas em ordem."""

    def bind_tools(self, tools, **kwargs):
        return self
