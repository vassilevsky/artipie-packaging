Name:      artipie
Version:   0.28.0
Release:   1
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
install -m 0444 -d artipie.jar %{buildroot}/opt/artipie
install -m 0444 -d artipie.service %{buildroot}%{_sysconfdir}/systemd/system
install -m 0444 -d artipie.yml %{buildroot}%{_sysconfdir}/artipie
install -m 0444 -d credentials.yml %{buildroot}%{_sysconfdir}/artipie
install -m 0444 -d readme-repos.txt %{buildroot}%{_sysconfdir}/artipie/repos/readme.txt
install -g artipie -o artipie -m 0444 -d readme-packages.txt %{buildroot}%{_var}/artipie/repos/readme.txt
install -g artipie -o artipie -m 0444 -d readme-caches.txt %{buildroot}%{_var}/cache/artipie/readme.txt

%files
/opt/artipie
%{_sysconfdir}/systemd/system/artipie.service
%config %{_sysconfdir}/artipie/artipie.yml
%config %{_sysconfdir}/artipie/credentials.yml
%{_sysconfdir}/artipie
%{_var}/artipie/repos
%ghost %{_var}/cache/artipie

%pre
getent group  artipie > /dev/null || groupadd --system artipie
getent passwd artipie > /dev/null || useradd --system -g artipie -d %{_var}/artipie -s /sbin/nologin artipie
exit 0

%changelog
* Tue Jan 17 2023 Ilya Vassilevsky <vassilevsky@gmail.com> - 0.28.0-1
- First version of artipie package
