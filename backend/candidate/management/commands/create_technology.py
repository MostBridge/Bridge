from candidate.factories import create_technology
from candidate.utils.db_command import CommandCreateObjects as BaseCommand


class Command(BaseCommand):
    """Создание технологии профессии."""

    def _generate(self, amount: int):
        create_technology(amount)
