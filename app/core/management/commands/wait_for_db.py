"""
Django command to wait for the database to be available."""
import time
from psycopg2 import OperationalError as psycopg2OpError
from django.db.utils import OperationalError
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """Django command to wait for the database."""

    def handle(self, *args, **options):
        """Entrypoint for the databases."""
        self.stdout.write('Waiting for database...')
        db_up = False
        while not db_up:
            try:
                self.check(databases=['default'])
                db_up = True
            except (psycopg2OpError, OperationalError):
                self.stdout.write('database not available, waiting 1 second....')
                time.sleep(1)
        self.stdout.write(self.style.SUCCESS('Database available!'))
