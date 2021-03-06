import pytest


def test_apt_config_file_permissions(host):
    conf = host.file('/etc/apt/apt.conf.d/80-test')

    assert conf.exists
    assert conf.is_file
    assert conf.user == 'root'
    assert conf.group == 'root'
    assert oct(conf.mode) == '0o644'


@pytest.mark.parametrize('param', [
    'APT::Archives::MaxAge "81";',
    'APT::Archives::MinAge "82";',
    'APT::Archives::MaxSize "83";'
])
def test_apt_config_file(host, param):
    conf = host.file('/etc/apt/apt.conf.d/80-test')

    assert conf.exists
    assert conf.is_file
    assert conf.contains(param)
