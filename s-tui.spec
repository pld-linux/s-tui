Summary:	Terminal-based CPU stress and monitoring utility
Name:		s-tui
Version:	1.1.3
Release:	4
License:	GPL v2+
Group:		Applications/System
#Source0Download: https://pypi.org/simple/s-tui/
Source0:	https://files.pythonhosted.org/packages/source/s/s-tui/%{name}-%{version}.tar.gz
# Source0-md5:	d385dab7d03d97cef3580e4d8ada8cd0
URL:		https://amanusk.github.io/s-tui/
BuildRequires:	python3-modules
BuildRequires:	python3-setuptools
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.720
Requires:	python3-devel-tools
Suggests:	stress
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Stress-Terminal UI, s-tui, monitors CPU temperature, frequency, power
and utilization in a graphical way from the terminal.

%prep
%setup -q

%{__sed} -E -i -e '1s,#!\s*/usr/bin/python(\s|$),#!%{__python3}\\1,' \
    s_tui/s_tui.py

%build
%py3_build

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md
%attr(755,root,root) %{_bindir}/s-tui
%{py3_sitescriptdir}/s_tui
%{py3_sitescriptdir}/s_tui-*-py*.egg-info
