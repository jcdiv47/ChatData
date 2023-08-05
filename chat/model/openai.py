from __future__ import annotations
from typing import Optional, List, Dict
import requests
from tenacity import retry, wait_random_exponential, stop_after_attempt
from chat.common.config import OPENAI_API_KEY
from chat.common.const import OPENAI_MODEL


class ChatModel:

    def __init__(
            self,
            api_key: Optional[str] = None,
            model: Optional[str] = None,
    ):
        self.api_key = api_key if api_key is not None else OPENAI_API_KEY
        self.model = model if model is not None else OPENAI_MODEL
        self._temperature = 0
        self._max_tokens = 2048
        self.chat_completion_url = "https://api.openai.com/v1/chat/completions"

    @retry(wait=wait_random_exponential(min=1, max=40), stop=stop_after_attempt(3))
    def chat_completion_request(
            self,
            messages: List[Dict[str, str]],
            functions=None,
            function_call=None,
            temperature=None,
            max_tokens=None,
    ):
        headers = {
            "Content-Type": "application/json",
            "Authorization": "Bearer " + self.api_key,
        }
        json_data = {
            "model": self.model,
            "messages": messages,
            "temperature": temperature if temperature is not None else self._temperature,
            "max_tokens": max_tokens if max_tokens is not None else self._max_tokens,
        }
        if functions is not None:
            json_data.update({"functions": functions})
        if function_call is not None:
            json_data.update({"function_call": function_call})
        try:
            response = requests.post(
                self.chat_completion_url,
                headers=headers,
                json=json_data,
            )
            return response.json()
        except Exception as e:
            print("Unable to generate ChatCompletion response")
            print(f"Exception: {e}")
            return e
