from monprojet.core.engine import run_job

def test_run_job_empty():
    assert run_job("  ").ok is False

def test_run_job_ok():
    assert run_job("hello").ok is True
