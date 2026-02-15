import argparse
from monprojet.config import AppConfig
from monprojet.logger import setup_logger
from monprojet.core.engine import run_job

def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(prog="mon_projet", description="Squelette CLI")
    p.add_argument("--payload", required=True, help="Entrée principale (texte)")
    p.add_argument("--log-level", default="INFO", help="DEBUG, INFO, WARNING, ERROR")
    return p

def main() -> int:
    args = build_parser().parse_args()
    cfg = AppConfig(log_level=args.log_level)
    log = setup_logger(level=cfg.log_level)

    log.info("Démarrage")
    res = run_job(args.payload)

    if res.ok:
        log.info(res.message)
        return 0
    log.error(res.message)
    return 1

if __name__ == "__main__":
    raise SystemExit(main())
