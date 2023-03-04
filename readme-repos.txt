Here you can create configuration files for individual repositories.

For example:

vim /etc/artipie/repos/rubygems.yml


repo:
  type: gem
  storage:
    type: fs
    path: /var/artipie/repos/rubygems
  permissions:
    "*":
      - download
    ci:
      - upload


Full documentation:

https://github.com/artipie/artipie/wiki/Configuration-Repository
