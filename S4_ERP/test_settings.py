import pytest
import os
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables for testing
load_dotenv()

# Assuming the settings.py is in the same directory as this test file
SETTINGS_MODULE_PATH = Path(__file__).resolve(strict=True).parent / 'S4_ERP/settings.py'

def test_base_dir():
    """Test if BASE_DIR is correctly set."""
    expected_base_dir = SETTINGS_MODULE_PATH.parent.parent
    from S4_ERP.settings import BASE_DIR
    assert BASE_DIR == expected_base_dir, f"Expected BASE_DIR to be {expected_base_dir}, but got {BASE_DIR}"

def test_installed_apps():
    """Test if all required apps are installed."""
    from S4_ERP.settings import INSTALLED_APPS
    expected_apps = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'comptable',
        'reactivation',
    ]
    for app in expected_apps:
        assert app in INSTALLED_APPS, f"Expected {app} to be in INSTALLED_APPS"

def test_middleware():
    """Test if all required middleware are present."""
    from S4_ERP.settings import MIDDLEWARE
    expected_middleware = [
        'django.middleware.security.SecurityMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
    ]
    for middleware in expected_middleware:
        assert middleware in MIDDLEWARE, f"Expected {middleware} to be in MIDDLEWARE"

def test_root_urlconf():
    """Test if ROOT_URLCONF is correctly set."""
    from S4_ERP.settings import ROOT_URLCONF
    expected_urlconf = 'S4_ERP.urls'
    assert ROOT_URLCONF == expected_urlconf, f"Expected ROOT_URLCONF to be {expected_urlconf}, but got {ROOT_URLCONF}"

def test_load_dotenv():
    """Test if environment variables are loaded correctly."""
    assert 'DJANGO_SECRET_KEY' in os.environ, "Expected 'DJANGO_SECRET_KEY' to be in environment variables"
    assert 'DATABASE_URL' in os.environ, "Expected 'DATABASE_URL' to be in environment variables"

@pytest.mark.parametrize("env_var", [
    "DJANGO_SECRET_KEY",
    "DATABASE_URL",
])
def test_missing_env_vars(monkeypatch, env_var):
    """Test behavior when critical environment variables are missing."""
    monkeypatch.delenv(env_var, raising=False)
    load_dotenv()  # Reload to ensure the variable is missing
    assert env_var not in os.environ, f"Expected {env_var} to be missing from environment variables"