# -*- coding:utf-8 -*-

from typing import Literal
from chat.agents.base import Agent


class ChatAgent(Agent):

    def __init__(self):
        pass

    @staticmethod
    def clean_up_mess(
            reason: Literal["not-query", "no-data"],
    ):
        explanations = {
            "not-query": """我作为商业决策分析小助手，暂时只能回答与数据有关的问题。""",
            "no-data": """十分抱歉，我们目前的数据可能暂时无法支持回答该问题。""",
        }
        if reason not in explanations:
            raise ValueError(f"`reason` should be one of {list(explanations.keys())}, got {reason} instead.")
        return explanations[reason].strip()

    def run(self, *args, **kwargs):
        pass

    def reassign(self):
        pass
