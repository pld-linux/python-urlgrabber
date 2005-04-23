Summary:	A high-level cross-protocol url-grabber
Name:		python-urlgrabber
Version:	2.9.6
Release:	1
License:	LGPL
Group:		Development/Libraries
Source0:	urlgrabber-%{version}.tar.gz
# Source0-md5:	e4afa725cf63b2684019f92cd8255671
URL:		http://linux.duke.edu/projects/urlgrabber/
BuildArch:	noarch
Provides:	urlgrabber
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A high-level cross-protocol url-grabber for python supporting HTTP, FTP 
and file locations.  Features include keepalive, byte ranges, throttling,
authentication, proxies and more.

%prep
%setup -n urlgrabber-%{version}

%build
python setup.py build

%install
python setup.py install --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES

%clean
rm -rf $RPM_BUILD_ROOT

%files -f INSTALLED_FILES
%defattr(644,root,root,755)
