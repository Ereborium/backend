from fastapi.testclient import TestClient


def test_read_example(client: TestClient):
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"msg": "example"}
