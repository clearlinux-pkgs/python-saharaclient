#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xFC43F0EE211DFED8 (infra-root@openstack.org)
#
Name     : python-saharaclient
Version  : 2.2.1
Release  : 47
URL      : http://tarballs.openstack.org/python-saharaclient/python-saharaclient-2.2.1.tar.gz
Source0  : http://tarballs.openstack.org/python-saharaclient/python-saharaclient-2.2.1.tar.gz
Source99 : http://tarballs.openstack.org/python-saharaclient/python-saharaclient-2.2.1.tar.gz.asc
Summary  : Python client library for Sahara
Group    : Development/Tools
License  : Apache-2.0
Requires: python-saharaclient-license = %{version}-%{release}
Requires: python-saharaclient-python = %{version}-%{release}
Requires: python-saharaclient-python3 = %{version}-%{release}
Requires: Babel
Requires: keystoneauth1
Requires: osc-lib
Requires: oslo.i18n
Requires: oslo.log
Requires: oslo.serialization
Requires: oslo.utils
Requires: pbr
Requires: python-openstackclient
Requires: requests
Requires: six
BuildRequires : Babel
BuildRequires : buildreq-distutils3
BuildRequires : keystoneauth1
BuildRequires : osc-lib
BuildRequires : oslo.i18n
BuildRequires : oslo.log
BuildRequires : oslo.serialization
BuildRequires : oslo.utils
BuildRequires : pbr
BuildRequires : python-openstackclient
BuildRequires : requests
BuildRequires : six

%description
========================
Team and repository tags
========================
.. image:: https://governance.openstack.org/tc/badges/python-saharaclient.svg
:target: https://governance.openstack.org/tc/reference/tags/index.html

%package license
Summary: license components for the python-saharaclient package.
Group: Default

%description license
license components for the python-saharaclient package.


%package python
Summary: python components for the python-saharaclient package.
Group: Default
Requires: python-saharaclient-python3 = %{version}-%{release}

%description python
python components for the python-saharaclient package.


%package python3
Summary: python3 components for the python-saharaclient package.
Group: Default
Requires: python3-core

%description python3
python3 components for the python-saharaclient package.


%prep
%setup -q -n python-saharaclient-2.2.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1561733060
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/python-saharaclient
cp LICENSE %{buildroot}/usr/share/package-licenses/python-saharaclient/LICENSE
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/python-saharaclient/LICENSE

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
