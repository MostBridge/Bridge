from candidate.factories import create_favorites
from candidate.utils.db_command import CommandCreateObjects as BaseCommand


class Command(BaseCommand):
    """Создание тестовой профессии."""

    def _generate(self, amount: int):
        create_favorites(amount)
