def test_docker_is_installed(host):
    package = host.package("nfs-kernel-server")
    assert package.is_installed

def test_docker_service(host):
    service = host.service("nfs-kernel-server")
    assert service.is_running
    assert service.is_enabled
