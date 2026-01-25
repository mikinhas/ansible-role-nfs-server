# Ansible Role: NFS Server

Installs and configures an NFS server on Ubuntu systems.

## Requirements

- Ansible >= 2.16

## Supported Platforms

- Ubuntu 22.04 (Jammy)
- Ubuntu 24.04 (Noble)

## Role Variables

Available variables with their default values (see [defaults/main.yml](defaults/main.yml)):

```yaml
# List of NFS exports
nfs_server_exports:
  - path: /mnt/data
    client: "192.168.1.0/24"
    options: "rw,sync,no_root_squash,no_subtree_check"
    owner: nobody
    group: nogroup
    mode: "0777"
```

Each export requires:

- `path`: Directory to share
- `client`: Subnet or host allowed to access
- `options`: NFS export options
- `owner`: Owner of the directory
- `group`: Group of the directory
- `mode`: Permissions of the directory

## Example Playbook

### Single export

```yaml
- hosts: nfs_servers
  roles:
    - role: mikinhas.nfs_server
      vars:
        nfs_server_exports:
          - path: /srv/nfs/share
            client: "10.0.0.0/24"
            options: "rw,sync,no_root_squash,no_subtree_check"
            owner: nobody
            group: nogroup
            mode: "0777"
```

### Multiple exports

```yaml
- hosts: nfs_servers
  roles:
    - role: mikinhas.nfs_server
      vars:
        nfs_server_exports:
          - path: /srv/nfs/data
            client: "10.0.0.0/24"
            options: "rw,sync,no_subtree_check"
            owner: nobody
            group: nogroup
            mode: "0755"
          - path: /srv/nfs/backup
            client: "10.0.1.0/24"
            options: "rw,sync,no_root_squash"
            owner: root
            group: root
            mode: "0700"
```

## License

MIT

## Author

Michael MACHADO
