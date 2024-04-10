from typing import Any
from django.db import models


def is_value_present_in_db(value: Any, model: models, field: str) -> bool:
    return model.objects.filter(**dict({field: value})).first() is not None