from typing import Any

from langchain.callbacks.base import BaseCallbackHandler
from langchain.schema import AgentAction
from src.logger import get_logger

logger = get_logger(__file__)


class LoggerHandler(BaseCallbackHandler):
    def on_llm_start(self, serialized: dict[str, Any], prompts: list[str], **kwargs: Any) -> Any:
        logger.info(f"on_llm_start serialized: {serialized}")
        logger.info(f"on_llm_start prompts: {prompts}")

    def on_llm_new_token(self, token: str, **kwargs: Any) -> Any:
        msg = f"on_new_token {token}"
        logger.info(msg)

    def on_llm_error(self, error: Exception | KeyboardInterrupt, **kwargs: Any) -> Any:
        logger.error(error, exc_info=True)
        """Run when LLM errors."""

    def on_chain_start(self, serialized: dict[str, Any], inputs: dict[str, Any], **kwargs: Any) -> Any:
        logger.info(f"on_chain_start: serialized {serialized}")
        logger.info(f"on_chain_start: inputs {inputs}")

    def on_tool_start(self, serialized: dict[str, Any], input_str: str, **kwargs: Any) -> Any:
        logger.info(f"on_tool_start: serialized {serialized}")
        logger.info(f"on_tool_start: inputs {input_str}")

    def on_agent_action(self, action: AgentAction, **kwargs: Any) -> Any:
        logger.info(f"on_agent_action: action {action}")
        logger.info(f"on_agent_action: AgentAction {AgentAction}")
