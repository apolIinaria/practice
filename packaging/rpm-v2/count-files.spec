Name:           count-files
Version:        2.0
Release:        1%{?dist}
Summary:        Script to count regular files in /etc
License:        MIT
URL:            https://github.com/apolIinaria/practice
Source0:        %{name}-%{version}.tar.gz
BuildArch:      noarch
Requires:       bash
Requires:       coreutils
Requires:       findutils

%description
A Bash script that counts the number of regular files
in the /etc directory, excluding directories and symbolic links.
Version 2.0 includes config file, man page and extended statistics.

%prep
%setup -q

%pre
echo "Installing count-files..."
mkdir -p /etc/count-files

%post
echo "count-files installed successfully"

%install
mkdir -p %{buildroot}%{_mandir}/man1
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}/etc/count-files
install -m 755 count_files.sh %{buildroot}%{_bindir}/count_files
install -m 644 count_files.1 %{buildroot}%{_mandir}/man1/count_files.1
install -m 644 conf/count-files.conf %{buildroot}/etc/count-files/count-files.conf

%files
%{_bindir}/count_files
%{_mandir}/man1/count_files.1.gz
/etc/count-files/count-files.conf

%changelog
* Thu Dec 18 2025 apolIinaria <pnovomlynets@gmail.com> - 2.0-1
- Version 2.0: added config file, man page, pre/post scripts
