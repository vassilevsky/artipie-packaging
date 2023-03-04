Here you can create subdirectories for each repository.
Repository files can be stored there.

For example:

mkdir /var/artipie/repos/rubygems

vim /etc/artipie/repos/rubygems.yml


repo:
  type: gem
  storage:
    type: fs
    path: /var/artipie/repos/rubygems


Full documentation:

https://github.com/artipie/artipie/wiki/Configuration-Repository
