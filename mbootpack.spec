Summary:	mbootpack takes kernel and modules (e.g. a Xen VMM, linux kernel and initrd), and packages them up as a single file
Name:		mbootpack
Version:	0.4a
Release:	0.1
License:	GPL v2
Group:		Applications/System
Source0:	http://www.tjd.phlegethon.org/software/%{name}-%{version}.tar.gz
# Source0-md5:	2fe9e314ac69f7d9b771d5d91a3154a5
URL:		http://www.tjd.phlegethon.org/software/#mbootpack
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a tool that takes a multiboot kernel and modules (e.g. a Xen
VMM, linux kernel and initrd), and packages them up as a single file
that looks like a bzImage linux kernel. The aim is to allow you to
boot multiboot kernels (in particular, Xen) using bootloaders that
don't support multiboot (i.e. pretty much anything except GRUB and
SYSLINUX).

%prep
%setup -q

%build
%{__make} \
	CFLAGS="%{rpmcflags}" \
	LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT
# create directories if necessary
install -d $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sbindir}

install %{name} $RPM_BUILD_ROOT%{_sbindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%attr(755,root,root) %{_sbindir}/mbootpack
