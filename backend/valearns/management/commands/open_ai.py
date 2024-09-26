from django.core.management.base import BaseCommand
from valearns.gpt_services import client


class Command(BaseCommand):
    help = "My OpenAI Command"

    def handle(self, *args, **kwargs):
        response = client.chat.completions.create(
            messages=[{"role": "user", "content": "Tell me a Joke"}],
            model="gpt-4o-2024-05-13",
        )
        print(response.choices[0].message.content)
        self.stdout.write("Running Function")
