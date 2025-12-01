import pytest
from django.urls import reverse, resolve
from django.urls.exceptions import NoReverseMatch
from S4_ERP.urls import urlpatterns

@pytest.mark.django_db
def test_admin_url():
    """
    Teste que l'URL de l'admin est correctement configurée.
    """
    path = reverse('admin:index')
    assert resolve(path).view_name == 'admin:index'

@pytest.mark.django_db
def test_reactivation_url():
    """
    Teste que l'URL de réactivation est correctement incluse.
    """
    try:
        path = reverse('reactivation:index')  # Assurez-vous que 'index' est une vue valide dans reactivation.urls
        assert resolve(path).namespace == 'reactivation'
    except NoReverseMatch:
        pytest.fail("L'URL de réactivation n'est pas correctement configurée.")

@pytest.mark.django_db
def test_invalid_url():
    """
    Teste qu'une URL invalide lève une exception NoReverseMatch.
    """
    with pytest.raises(NoReverseMatch):
        reverse('invalid:url')

@pytest.mark.parametrize("url_name", [
    ('admin:index'),
    ('reactivation:index'),  # Assurez-vous que 'index' est une vue valide dans reactivation.urls
])
@pytest.mark.django_db
def test_url_resolves(url_name):
    """
    Teste que les URL valides sont résolues correctement.
    """
    path = reverse(url_name)
    assert resolve(path).view_name == url_name

@pytest.mark.parametrize("url_name", [
    ('nonexistent:url'),
    ('another:invalid'),
])
@pytest.mark.django_db
def test_url_no_reverse_match(url_name):
    """
    Teste que les URL invalides lèvent une exception NoReverseMatch.
    """
    with pytest.raises(NoReverseMatch):
        reverse(url_name)