%define module ecdsa

Name:		python-ecdsa
Version:	0.19.1
Release:	1
License:	MIT
Summary:	Pure python ECDSA signature/verification and ECDH key agreement
Group:		Development/Python
URL:		https://github.com/tlsfuzzer/python-ecdsa
Source0:	%{URL}/archive/%{name}-%{version}/%{name}-%{version}.tar.gz

BuildSystem:	python
BuildArch:	noarch
BuildRequires:	pkgconfig(python)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(six)
BuildRequires:	python%{pyver}dist(wheel)
Recommends:	python%{pyver}dist(gmpy2)

# Not really, but let's get rid of py2 cruft
Obsoletes:	python2-%{module} < %{EVRD}

%description
This is an easy-to-use implementation of ECDSA cryptography
(Elliptic Curve Digital Signature Algorithm), implemented purely in Python,
released under the MIT license. With this library, you can quickly create
keypairs (signing key and verifying key), sign messages, and verify the
signatures. The keys and signatures are very short, making them easy to
handle and incorporate into other protocols.

%prep -a
# Remove bundled egg-info
rm -rf src/%{module}.egg-info

%build -a
# Remove shebang from all non executable files
find ./ -type f -name "*.py" -perm 644 -exec sed -i -e '1{\@^#! %{_bindir}/env python@d}' {} \;

%files
%doc README.md
%license LICENSE
%{python3_sitelib}/%{module}
%{python3_sitelib}/%{module}-%{version}*.*-info
