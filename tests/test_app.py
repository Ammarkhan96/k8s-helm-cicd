from app.app import app

def test_home():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200
    assert response.json["application"] == "Day 8 Helm Kubernetes CI/CD"

def test_health():
    client = app.test_client()
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json["status"] == "healthy"

def test_ready():
    client = app.test_client()
    response = client.get("/ready")
    assert response.status_code == 200
    assert response.json["status"] == "ready"
