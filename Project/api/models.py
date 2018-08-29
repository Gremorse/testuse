from typing import Any

from django.db import models

# Create your models here.

class NewUser(object):
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __setattr__(self, name: str, value: Any) -> None:
        super().__setattr__(name, value)

    def __getattribute__(self, name: str) -> Any:
        return super().__getattribute__(name)

