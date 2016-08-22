import pytest

def test_apt_config_file_permissions(File):
    conf = File('/etc/apt/apt.conf.d/80-test')

    assert conf.exists
    assert conf.is_file
    assert conf.user == 'root'
    assert conf.group == 'root'
    assert oct(conf.mode) == '0644'

@pytest.mark.parametrize('param', [
    ('APT::Archives::MaxAge "81";'),
    ('APT::Archives::MinAge "82";'),
    ('APT::Archives::MaxSize "83";')
])
def test_apt_config_file(File, param):
    conf = File('/etc/apt/apt.conf.d/80-test')

    assert conf.exists
    assert conf.is_file
    assert conf.contains(param)
