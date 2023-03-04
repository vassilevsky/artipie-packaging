Here you can create subdirectories for caches.
Then specify them in caches configs.

For example:

mkdir /var/cache/artipie/docker-proxy

vim /etc/artipie/repos/docker-proxy.yml


repo:
  type: docker-proxy
  remotes:
    - url: registry-1.docker.io
      cache:
        storage:
          type: fs
          path: /var/cache/artipie/docker-proxy


Full documentation:

https://github.com/artipie/artipie/wiki/Configuration-Repository
