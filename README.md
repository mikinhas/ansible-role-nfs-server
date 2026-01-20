# Ansible Role: NFS Server

Installs and configures an NFS server on Debian/Ubuntu systems.

## Requirements

- Ansible >= 2.16
- Target OS: Debian/Ubuntu

## Role Variables

Available variables with their default values (see [defaults/main.yml](defaults/main.yml)):

```yaml
# Directory to share via NFS
nfs_server_directory: /mnt/data

# Owner and group of the shared directory
nfs_server_directory_owner: nobody
nfs_server_directory_group: nogroup

# Permissions of the shared directory
nfs_server_directory_mode: "0777"

# NFS export options
nfs_server_directory_options: "rw,sync,no_root_squash,no_subtree_check"

# Subnet allowed to access the NFS share
nfs_server_client_subnet: "192.168.1.0/24"
```

## Example Playbook

```yaml
- hosts: nfs_servers
  roles:
    - role: mikinhas.nfs_server
      vars:
        nfs_server_directory: /srv/nfs/share
        nfs_server_client_subnet: "10.0.0.0/24"
```

## License

MIT

## Author

Michael MACHADO
