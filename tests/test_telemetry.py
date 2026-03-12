import json
import pytest
from src.log_analyzer import parse_telemetry

def test_critical_logic_detection():
    # Load your practice data
    with open("data/telemetry.json", "r") as f:
        logs = json.load(f)
    
    uuids, failures = parse_telemetry(logs)
    
    # Assertions: This is what makes it a 'Test'
    assert "UUID-A1" in uuids
    assert "evt_003" in failures  # Verify we caught the high-conf failure