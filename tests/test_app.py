from fastapi.testclient import TestClient

from src.app import app


client = TestClient(app)


def test_unregister_participant_removes_email_from_activity():
    signup_response = client.post(
        "/activities/Chess Club/signup?email=student@example.com"
    )
    assert signup_response.status_code == 200

    unregister_response = client.delete(
        "/activities/Chess Club/unregister?email=student@example.com"
    )
    assert unregister_response.status_code == 200
    assert "student@example.com" in unregister_response.text

    activities_response = client.get("/activities")
    assert activities_response.status_code == 200
    activity = activities_response.json()["Chess Club"]
    assert "student@example.com" not in activity["participants"]
