import pytest
from src.perf_monitor import analyze_performance

def test_leak_detection():
    result = analyze_performance("data/performance_leak.json")
    assert result["is_leaking"] is True
    assert result["max_mem"] == 240.8

def test_baseline_passes():
    result = analyze_performance("data/performance_baseline.json")
    assert result["is_leaking"] is False
    assert result["has_spike"] is False