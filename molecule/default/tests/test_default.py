"""Role testing files using testinfra."""
import os
import pytest


@pytest.mark.parametrize("service", [
    "systemd-journal-remote",
    "systemd-journal-upload"
    ])
def test_systemd_journal_services_running(host, service):
    """
    Validate that expected journal-remote services are running
    """
    assert host.service(service).is_enabled
    assert host.service(service).is_running

