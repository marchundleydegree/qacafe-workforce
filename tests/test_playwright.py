import re

import pytest
from playwright.sync_api import APIRequestContext, Playwright


BASE_URL = "http://127.0.0.1:5000"


@pytest.fixture
def api_request(playwright: Playwright):
    """Create an API request context for the tests."""

    context = playwright.request.new_context(
        base_url=BASE_URL
    )

    yield context

    context.dispose()


def test_get_employees(api_request: APIRequestContext):
    """Check that GET /employees returns successfully."""

    response = api_request.get("/employees")

    assert response.status == 200

    employees = response.json()
    assert isinstance(employees, list)


def test_post_employee(api_request: APIRequestContext):
    """Check that POST /employees creates an employee."""

    new_employee = {
        "name": "Test Employee",        
        "start_date": "2026-10-30",
        "location": "Somewhere",
        "role": "Person"
    }

    response = api_request.post(
        "/employees",
        data=new_employee
    )

    assert response.status == 201
    assert response.text() =="Employee added successfully"