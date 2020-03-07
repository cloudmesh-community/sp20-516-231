# Multipass Brian Kegerreis sp20-516-231

## E.Multipass.1

```bash
$ multipass version
multipass 1.1.0
multipassd 1.1.0
```

Linux installation instructions do not need improvement

```bash
$ cms multipass images
+------------------+--------+-------------------------------+-----------+------------+--------------------+
| Name             | OS     | Release                       | Remote    | Version    | Alias              |
+------------------+--------+-------------------------------+-----------+------------+--------------------+
| 16.04            | Ubuntu | 16.04 LTS                     |           | 20200218.1 | ['xenial']         |
| 18.04            | Ubuntu | 18.04 LTS                     |           | 20200218   | ['bionic', 'lts']  |
| 19.10            | Ubuntu | 19.10                         |           | 20200211   | ['eoan']           |
| core             | Ubuntu | Core 16                       |           | 20200213   | ['core16']         |
| core18           | Ubuntu | Core 18                       |           | 20200210   | []                 |
| daily:20.04      | Ubuntu | 20.04 LTS                     | daily     | 20200305   | ['devel', 'focal'] |
| snapcraft:core   |        | Snapcraft builder for Core 16 | snapcraft | 20200221   | ['core16']         |
| snapcraft:core18 |        | Snapcraft builder for Core 18 | snapcraft | 20200221   | []                 |
+------------------+--------+-------------------------------+-----------+------------+--------------------+
```

## E.Multipass.2

Primary is a default instance that launches when a user executes certain multipass commands without a specified instance. This is usually based on the latest Ubuntu LTS but can be configured by the user.

## E.Multipass.3

Snapcraft is a tool to package snaps, which are applications that can be installed regardless of the user's Linux distribution or dependencies.

## E.Multipass.4

See https://github.com/cloudmesh-community/book/blob/master/bib/multipass.bib

## E.Multipass.5

## E.Multipass.6

## E.Multipass.7

```bash
$ multipass launch --name microk8s-vm --mem 4G --disk 40G
$ multipass exec microk8s-vm -- sudo snap install microk8s --classic
```

## E.Multipass.8

## E.Multipass.9

## E.Multipass.10


