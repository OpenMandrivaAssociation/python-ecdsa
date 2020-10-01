%define pypi_name ecdsa

Name:           python-ecdsa
Version:	0.16.0
Release:	1
Group:          Development/Python
Summary:        ECDSA cryptographic signature library (pure python)

License:        MIT
URL:            http://github.com/warner/python-ecdsa
Source0:	https://files.pythonhosted.org/packages/23/c3/81b0040f2976775d6685c3bb3748355bb2b725a9210a4ea50afc5a90e7d9/ecdsa-0.16.0.tar.gz
BuildArch:      noarch

BuildRequires:  python2-devel
BuildRequires:  python3-devel
BuildRequires:  python-setuptools
BuildRequires:  python2-setuptools


%description
This is an easy-to-use implementation of ECDSA cryptography
(Elliptic Curve Digital Signature Algorithm), implemented purely in Python,
released under the MIT license. With this library, you can quickly create
keypairs (signing key and verifying key), sign messages, and verify the
signatures. The keys and signatures are very short, making them easy to
handle and incorporate into other protocols.

%package -n     python2-%{pypi_name}
Summary:        ECDSA cryptographic signature library (pure python)
Group:          Development/Python


%description -n python2-%{pypi_name}
This is an easy-to-use implementation of ECDSA cryptography
(Elliptic Curve Digital Signature Algorithm), implemented purely in Python,
released under the MIT license. With this library, you can quickly create
keypairs (signing key and verifying key), sign messages, and verify the
signatures. The keys and signatures are very short, making them easy to
handle and incorporate into other protocols.

%prep
%setup -qc
mv %{pypi_name}-%{version} python2
cp -a python2 python3

%build
pushd python2
python2 setup.py build
popd
pushd python3
python3 setup.py build
popd

%install
pushd python3
python3 setup.py install --skip-build --root %{buildroot}
popd
pushd python2
python2 setup.py install --skip-build --root %{buildroot}
popd

%files -n python2-%{pypi_name}
%doc python2/README.md python2/LICENSE
%{python2_sitelib}/%{pypi_name}*

%files
%doc python3/README.md python3/LICENSE
%{python3_sitelib}/%{pypi_name}*
