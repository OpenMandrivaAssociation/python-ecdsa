%define pypi_name ecdsa

Name:           python-ecdsa
Version:	0.19.0
Release:	1
Group:          Development/Python
Summary:        ECDSA cryptographic signature library (pure python)

License:        MIT
URL:            https://github.com/warner/python-ecdsa
Source0:	https://files.pythonhosted.org/packages/source/e/ecdsa/ecdsa-%{version}.tar.gz
BuildArch:      noarch

BuildSystem:	python
BuildRequires:  python3-devel
BuildRequires:  python-setuptools

# Not really, but let's get rid of py2 cruft
Obsoletes:	python2-%{pypi_name} < %{EVRD}

%description
This is an easy-to-use implementation of ECDSA cryptography
(Elliptic Curve Digital Signature Algorithm), implemented purely in Python,
released under the MIT license. With this library, you can quickly create
keypairs (signing key and verifying key), sign messages, and verify the
signatures. The keys and signatures are very short, making them easy to
handle and incorporate into other protocols.

%files
%doc README.md LICENSE
%{python3_sitelib}/%{pypi_name}*
