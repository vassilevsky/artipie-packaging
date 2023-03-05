Name:      artipie
Version:   0.28.0
Release:   3
BuildArch: noarch
Summary:   Package repository and cache server
License:   MIT
URL:       https://www.artipie.com
Group:     Development/Tools/Other

Requires(pre): shadow-utils

%description
HTTP server supporting many package repository formats
(NPM, PyPi, Docker, RubyGems, etc),
some with caching proxy ability,
each running on its own path or port.

%install
install -m 0444 -D artipie.jar         %{buildroot}/opt/artipie/artipie.jar
install -m 0444 -D artipie.service     %{buildroot}%{_sysconfdir}/systemd/system/artipie.service
install -m 0444 -D artipie.yml         %{buildroot}%{_sysconfdir}/artipie/artipie.yml
install -m 0444 -D credentials.yml     %{buildroot}%{_sysconfdir}/artipie/credentials.yml
install -m 0444 -D readme-repos.txt    %{buildroot}%{_sysconfdir}/artipie/repos/readme.txt
install -m 0444 -D readme-packages.txt %{buildroot}%{_var}/artipie/repos/readme.txt
install -m 0444 -D readme-caches.txt   %{buildroot}%{_var}/cache/artipie/readme.txt

%files
        /opt/artipie
        %{_sysconfdir}/systemd/system/artipie.service
%config %{_sysconfdir}/artipie/artipie.yml
%config %{_sysconfdir}/artipie/credentials.yml
        %{_sysconfdir}/artipie
        %{_var}/artipie/repos
        %{_var}/cache/artipie

%pre
getent group  artipie > /dev/null || groupadd --system artipie
getent passwd artipie > /dev/null || useradd --system -g artipie -d %{_var}/artipie -s /sbin/nologin artipie
exit 0

%post
chown --recursive artipie:artipie %{_var}/artipie
chown --recursive artipie:artipie %{_var}/cache/artipie

%changelog
* Tue Jan 17 2023 Ilya Vassilevsky <vassilevsky@gmail.com> - 0.28.0-1
- First version of artipie package
