Name:      artipie
Version:   0.28.0
Release:   7
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
install -m 0444 -D artipie.service     %{buildroot}/usr/lib/systemd/system/artipie.service
install -m 0444 -D artipie.yml         %{buildroot}%{_sysconfdir}/artipie/artipie.yml

mkdir -p %{buildroot}%{_sysconfdir}/artipie/repos.d
mkdir -p %{buildroot}%{_var}/artipie
mkdir -p %{buildroot}%{_var}/cache/artipie

%files
        /opt/artipie
        /usr/lib/systemd/system/artipie.service
%config %{_sysconfdir}/artipie/artipie.yml
%dir    %{_sysconfdir}/artipie/repos.d
%dir    %{_var}/artipie
%dir    %{_var}/cache/artipie
%ghost  %{_var}/log/artipie.log

%pre
getent group  artipie > /dev/null || groupadd --system artipie
getent passwd artipie > /dev/null || useradd --system -g artipie -d %{_var}/artipie -s /sbin/nologin artipie
exit 0

%post
chown --recursive artipie:artipie %{_var}/artipie
chown --recursive artipie:artipie %{_var}/cache/artipie

%changelog
* Sun Mar 12 2023 Ilya Vassilevsky <vassilevsky@gmail.com> - 0.28.0-7
- Moved SystemD unit file to /usr/lib
- Removed unnecessary files

* Sun Mar 5 2023 Ilya Vassilevsky <vassilevsky@gmail.com> - 0.28.0-4
- First version of artipie package
