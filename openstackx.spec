%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}
%{!?python_sitearch: %global python_sitearch %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib(1)")}
%define mod_name openstackx


Name:           openstackx
Version:        0.2
Release:        1%{?dist}
Url:            http://github.com/cloudbuilders/openstackx/
Summary:        Extension for openstack nova
License:        Apache 2.0
Vendor:         Grid Dynamics Consulting Services, Inc.
Group:          Development/Languages/Python
Source:         %{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  python-devel python-setuptools
BuildArch:      noarch
Requires:       python-prettytable python-httplib2 python-argparse


%description
Extension for openstack nova.


%prep
%setup -q -n %{name}-%{version}


%build
%__python setup.py build


%install
%__rm -rf %{buildroot}
%__python setup.py install -O1 --skip-build --prefix=%{_prefix} --root=%{buildroot}
mkdir -p %{buildroot}/var/lib/nova
mv %{buildroot}%{python_sitelib}/extensions %{buildroot}/var/lib/nova/extensions


%clean
%__rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%{python_sitelib}/%{mod_name}
%{python_sitelib}/%{mod_name}-*.egg-info
%{python_sitelib}/%{mod_name}-*nspkg.pth
/var/lib/nova/extensions


%changelog
