def test_nfs_package_is_installed(host):
    package = host.package("nfs-kernel-server")
    assert package.is_installed


def test_nfs_service(host):
    service = host.service("nfs-kernel-server")
    assert service.is_running
    assert service.is_enabled


def test_exports_file(host):
    exports = host.file("/etc/exports")
    assert exports.exists
    assert exports.contains("/mnt/data")


def test_default_export_directory(host):
    directory = host.file("/mnt/data")
    assert directory.exists
    assert directory.is_directory
    assert directory.user == "nobody"
    assert directory.group == "nogroup"
