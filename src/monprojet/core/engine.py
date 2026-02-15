from dataclasses import dataclass

@dataclass
class Result:
    ok: bool
    message: str

def run_job(payload: str) -> Result:
    payload = payload.strip()
    if not payload:
        return Result(ok=False, message="Payload vide")
    # TODO: remplace ici par la logique de ton projet
    return Result(ok=True, message=f"Reçu: {payload}")
