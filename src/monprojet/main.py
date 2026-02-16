from monprojet.logging_conf import setup_logging
from squelette.src.monprojet.core.app import run


def main() -> int:
    setup_logging()
    run()
    return 0

print("Démarrage de l'application")
