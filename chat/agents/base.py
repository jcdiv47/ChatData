# -*- coding:utf-8 -*-

from __future__ import annotations
from pydantic import BaseModel


class Agent:

    def __repr__(self):
        return f"{__class__.__name__}()"

    def run(self, *args, **kwargs):
        raise NotImplementedError

    def reassign(self, *args, **kwargs):
        raise NotImplementedError


class Task(BaseModel):
    name: str
    assignor: Agent | None
    assignee: Agent
    metadata: dict[str, str] = {}

    class Config:
        arbitrary_types_allowed = True
