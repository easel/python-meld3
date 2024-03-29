%{!?python_sitearch: %global python_sitearch %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib(1)")}
Summary: HTML/XML templating system for Python
Name: python-meld3
Version: 0.6.7
Release: 4%{?dist}

License: ZPLv2.1
Group: Development/Languages
URL: http://www.plope.com/software/meld3/
Source0: http://pypi.python.org/packages/source/m/meld3/meld3-%{version}.tar.gz
# The current meld3 tarball leaves this out by mistake
# https://github.com/Supervisor/meld3/raw/0.6.7/meld3/cmeld3.c -- AKA:
# https://github.com/Supervisor/meld3/raw/bafd959fc2e389f46786a6b3174d50f9963fe967/meld3/cmeld3.c
Patch0: python-meld3-0.6.7-missing-src-file.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%if 0%{?rhel} && 0%{?rhel} <= 5
BuildRequires:  python-elementtree
Requires: python-elementtree
%endif

BuildRequires: python-devel


%description
meld3 is an HTML/XML templating system for Python 2.3+ which keeps template
markup and dynamic rendering logic separate from one another. See
http://www.entrian.com/PyMeld for a treatise on the benefits of this pattern.

%prep
%setup -q -n meld3-%{version}
%patch0 -p1 -b .missing-src-file

%build
export USE_MELD3_EXTENSION_MODULES=True
CFLAGS="%{optflags}" %{__python} setup.py build

%install
rm -rf %{buildroot}
export USE_MELD3_EXTENSION_MODULES=True
%{__python} setup.py install --skip-build --root %{buildroot}
sed -i s'/^#!.*//' $( find %{buildroot}/%{python_sitearch}/meld3/ -type f)
chmod 0755 %{buildroot}/%{python_sitearch}/meld3/cmeld3.so

%check
%{__python} meld3/test_meld3.py

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc README.txt COPYRIGHT.txt LICENSE.txt CHANGES.txt
%{python_sitearch}/meld3/
%{python_sitearch}/*

%changelog

%changelog
* Tue Apr 05 2011 Nils Philippsen - 0.6.7-4
- patch in missing cmeld3.c file instead of indiscriminately (over-)writing it
- don't use macros for system executables (except python)

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Nov 19 2010 Toshio Kuratomi <toshio@fedoraproject.org> - 0.6.7-1
- Update to solve a crasher bug on python-2.7:
  https://bugzilla.redhat.com/show_bug.cgi?id=652890
- Fix missing cmeld3.c file in the upstream tarball (upstream was notified).

* Thu Jul 22 2010 David Malcolm <dmalcolm@redhat.com> - 0.6.5-2
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Tue Apr 13 2010 Nils Philippsen <nils@redhat.com> - 0.6.5-1
- version 0.6.5
- drop obsolete etree patch

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 0.6.4-2
- Rebuild for Python 2.6

* Tue Feb 28 2008 Toshio Kuratomi <toshio@fedoraproject.org> 0.6.4-1
- Update to 0.6.4.
- Fix python-2.5 elementtree problem.

* Tue Feb 12 2008 Mike McGrath <mmcgrath@redhat.com> 0.6.3-3
- Rebuild for gcc43

* Mon Jan 7 2008 Toshio Kuratomi <a.badger@gmail.com> 0.6.3-2
- Fix include egginfo when created.

* Wed Oct 17 2007 Toshio Kuratomi <a.badger@gmail.com> 0.6.3-1
- Update to 0.6.3 (Fix memory leaks).
- Update license tag.

* Wed Aug 22 2007 Mike McGrath <mmcgrath@redhat.com> 0.6-3
- Release bump for rebuild

* Thu Apr 26 2007 Mike McGrath <mmcgrath@redhat.com> 0.6-2.1
- Fix requires on python-elementtree for python-2.5.  (elementtree is included
  in python-2.5)

* Sun Apr 22 2007 Mike McGrath <mmcgrath@redhat.com> 0.6-2
- Patch suggested in #153247

* Fri Apr 20 2007 Mike McGrath <mmcgrath@redhat.com> 0.6-1
- Initial packaging

