%{!?python_sitearch: %define python_sitearch %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib(1)")}
Summary: An HTML/XML templating system for Python
Name: python-meld3
Version: 0.6
Release: 2%{?dist}

License: ZPL
Group: Development/Languages
URL: http://www.plope.com/software/meld3/
Source: http://www.plope.com/software/meld3/meld3-%{version}.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

Requires: python-elementtree
BuildRequires: python-devel


%description
meld3 is an HTML/XML templating system for Python 2.3+ which keeps template
markup and dynamic rendering logic separate from one another. See
http://www.entrian.com/PyMeld for a treatise on the benefits of this pattern.

%prep
%setup -q -n meld3-%{version}

%build
CFLAGS="%{optflags}" %{__python} setup.py build

%install
%{__rm} -rf %{buildroot}
%{__python} setup.py install --skip-build --root %{buildroot}
%{__sed} -i s'/^#!.*//' $( find %{buildroot}/%{python_sitearch}/meld3/ -type f)

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc README.txt
%{python_sitearch}/meld3/

%changelog
* Sun Apr 22 2007 Mike McGrath <mmcgrath@redhat.com> 0.6-2
- Patch suggested in #153247

* Fri Apr 20 2007 Mike McGrath <mmcgrath@redhat.com> 0.6-1
- Initial packaging

