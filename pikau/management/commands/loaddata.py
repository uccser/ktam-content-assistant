"""Module for the custom Django loaddata command."""

from django.core import management


class Command(management.base.BaseCommand):
    """Required command class for the custom Django loaddata command."""

    help = "Update all data from content folders for all applications"

    def handle(self, *args, **options):
        """Automatically called when the updatedata command is given."""
        management.call_command("loadfiles")
        management.call_command("loadpikau")
