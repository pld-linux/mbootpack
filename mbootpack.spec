Summary:	Packaging Linux kernel and modules as a single file
Summary(pl):	Pakowanie j±dra Linuksa i modu³ów do pojedynczego pliku
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
VMM, Linux kernel and initrd), and packages them up as a single file
that looks like a bzImage Linux kernel. The aim is to allow you to
boot multiboot kernels (in particular, Xen) using bootloaders that
don't support multiboot (i.e. pretty much anything except GRUB and
SYSLINUX).

%description -l pl
To narzêdzie bierze j±dro multiboot i modu³y (np. xenowy VMM, j±dro
Linuksa i initrd) i pakuje je jako pojedynczy plik wygl±daj±cy jak
j±dro Linuksa bzImage. Celem jest umo¿liwienie uruchamiania j±der
multiboot (w szczególno¶ci Xena) przy u¿yciu bootloaderów nie
obs³uguj±cych multiboot (czyli prawie wszystkich z wyj±tkiem GRUB-a i
SYSLINUKSA).

%prep
%setup -q

%build
%{__make} \
	CFLAGS="%{rpmcflags}" \
	LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sbindir}

install %{name} $RPM_BUILD_ROOT%{_sbindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%attr(755,root,root) %{_sbindir}/mbootpack
