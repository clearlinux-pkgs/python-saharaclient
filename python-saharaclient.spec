#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : python-saharaclient
Version  : 0.8.0
Release  : 16
URL      : http://tarballs.openstack.org/python-saharaclient/python-saharaclient-0.8.0.tar.gz
Source0  : http://tarballs.openstack.org/python-saharaclient/python-saharaclient-0.8.0.tar.gz
Summary  : Client library for Sahara API
Group    : Development/Tools
License  : Apache-2.0
Requires: python-saharaclient-bin
Requires: python-saharaclient-python
BuildRequires : Babel-python
BuildRequires : Jinja2
BuildRequires : Pygments
BuildRequires : Sphinx-python
BuildRequires : cliff-python
BuildRequires : cmd2-python
BuildRequires : coverage-python
BuildRequires : discover-python
BuildRequires : docutils-python
BuildRequires : extras
BuildRequires : fixtures-python
BuildRequires : flake8-python
BuildRequires : funcsigs-python
BuildRequires : futures-python
BuildRequires : hacking
BuildRequires : httplib2
BuildRequires : iso8601-python
BuildRequires : jsonschema-python
BuildRequires : linecache2-python
BuildRequires : markupsafe-python
BuildRequires : mccabe
BuildRequires : mccabe-python
BuildRequires : mox3-python
BuildRequires : msgpack-python-python
BuildRequires : netaddr
BuildRequires : netifaces-python
BuildRequires : nose-python
BuildRequires : oslo.config
BuildRequires : oslo.context-python
BuildRequires : oslo.i18n-python
BuildRequires : oslo.log-python
BuildRequires : oslo.serialization-python
BuildRequires : oslo.utils-python
BuildRequires : oslosphinx-python
BuildRequires : oslotest-python
BuildRequires : pbr
BuildRequires : pep8
BuildRequires : pip
BuildRequires : pluggy
BuildRequires : prettytable
BuildRequires : py-python
BuildRequires : pyflakes-python
BuildRequires : pyparsing-python
BuildRequires : pytest
BuildRequires : python-dev
BuildRequires : python-keystoneclient-python
BuildRequires : python-mimeparse-python
BuildRequires : python-mock
BuildRequires : python-neutronclient-python
BuildRequires : python-novaclient-python
BuildRequires : python-subunit
BuildRequires : python-swiftclient-python
BuildRequires : pytz-python
BuildRequires : requests
BuildRequires : requests-mock-python
BuildRequires : setuptools
BuildRequires : simplejson
BuildRequires : six
BuildRequires : stevedore
BuildRequires : tempest-lib-python
BuildRequires : testrepository-python
BuildRequires : testscenarios
BuildRequires : testtools
BuildRequires : tox
BuildRequires : traceback2-python
BuildRequires : unittest2-python
BuildRequires : virtualenv

%description
Compiled against Hadoop 1.2.1
$ mkdir wordcount_classes
$ javac -classpath /usr/share/hadoop/hadoop-core-1.2.1.jar:/usr/share/hadoop/lib/commons-cli-1.2.jar -d wordcount_classes WordCount.java
$ jar -cvf edp-java.jar -C wordcount_classes/ .

%package bin
Summary: bin components for the python-saharaclient package.
Group: Binaries

%description bin
bin components for the python-saharaclient package.


%package python
Summary: python components for the python-saharaclient package.
Group: Default

%description python
python components for the python-saharaclient package.


%prep
%setup -q -n python-saharaclient-0.8.0

%build
python2 setup.py build -b py2

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
python2 setup.py test || :
%install
rm -rf %{buildroot}
python2 setup.py build -b py2 install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/sahara

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*