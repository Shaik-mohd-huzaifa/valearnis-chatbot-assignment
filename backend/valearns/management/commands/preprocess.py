from typing import Any
from django.core.management.base import BaseCommand
from valearns.ML_models.preprocessing import preprocess_input


class Command(BaseCommand):
    help = "Pre Processing Function"

    def handle(self, *args: Any, **options: Any) -> str | None:
        print(preprocess_input("Tell me a Story of running rocks"))
