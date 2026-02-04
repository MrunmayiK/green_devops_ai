from app import workload

def test_workload():
    result = workload()
    assert result > 0
