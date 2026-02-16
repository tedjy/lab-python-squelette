def test_import_package():
    import src.monprojet  # noqa: F401


def test_import_main():
    from src.monprojet.main import main  # noqa: F401
