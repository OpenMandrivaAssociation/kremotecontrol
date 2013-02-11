Name:		kremotecontrol
Summary:	KDE Frontend for the LIRC Suite
Version:	4.10.0
Release:	1
Group:		Graphical desktop/KDE
License:	GPLv2 and LGPLv2 and GPLD
URL:		http://www.kde.org/applications/utilities/kremotecontrol/
Source0:	ftp://ftp.kde.org/pub/kde/stable/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	kdebase4-workspace-devel
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xi)
Requires:	kdebase4-runtime
Conflicts:	kdeutils4-core < 4.5.72

%description
KRemoteControl is a KDE frontend for the Linux Infrared Remote Control system
(LIRC).
It consist of two parts: a systemtray applet and a configuration module.

%files
%doc AUTHORS ChangeLog COPYING COPYING.LIB README TODO
%{_kde_bindir}/krcdnotifieritem
%{_kde_libdir}/kde4/kcm_remotecontrol.so
%{_kde_libdir}/kde4/kded_kremotecontroldaemon.so
%{_kde_libdir}/kde4/plasma_engine_kremoteconrol.so
%{_kde_libdir}/kde4/kremotecontrol_lirc.so
%{_kde_services}/kremotecontrolbackends/kremotecontrol_lirc.desktop
%{_kde_servicetypes}/kremotecontrolmanager.desktop
%{_kde_applicationsdir}/krcdnotifieritem.desktop
%{_kde_appsdir}/kremotecontrol/
%{_kde_appsdir}/kremotecontroldaemon/
%{_kde_iconsdir}/*/*/actions/krcd_flash.*
%{_kde_iconsdir}/*/*/actions/krcd_off.*
%{_kde_iconsdir}/*/*/apps/krcd.*
%{_kde_iconsdir}/*/*/devices/infrared-remote.*
%{_kde_services}/kcm_remotecontrol.desktop
%{_kde_services}/kded/kremotecontroldaemon.desktop
%{_kde_services}/plasma-engine-kremotecontrol.desktop
%{_kde_docdir}/HTML/en/kcontrol/kremotecontrol/

#------------------------------------------------------------------------------

%define kremotecontrol_major 1
%define libkremotecontrol %mklibname kremotecontrol %{kremotecontrol_major}
%define oldlibkremotecontrol %mklibname libkremotecontrol 1

%package -n %{libkremotecontrol}
Summary:	Runtime library for kremotecontrol
Group:		System/Libraries
Obsoletes:	%{oldlibkremotecontrol} < 4.7.90

%description -n %{libkremotecontrol}
KRemoteControl is a KDE frontend for the Linux Infrared Remote Control system 
(LIRC).

It consist of two parts: a systemtray applet and a configuration module.

This package provides the runtime library for kremotecontrol.

%files -n %{libkremotecontrol}
%{_kde_libdir}/liblibkremotecontrol.so.%{kremotecontrol_major}*

#------------------------------------------------------------------------------

%package devel
Summary:	Devel stuff for %{name}
Group:		Development/KDE and Qt
Requires:	kdelibs4-devel
Requires:	%{libkremotecontrol} = %{EVRD}
Conflicts:	kdeutils4-devel < 4.7.90

%description devel
KRemoteControl is a KDE frontend for the Linux Infrared Remote Control system
(LIRC).

It consist of two parts: a systemtray applet and a configuration module.

This package contains header files needed if you wish to build applications
based on %{name}.

%files devel
%{_kde_libdir}/liblibkremotecontrol.so

#------------------------------------------------------------------------------

%prep
%setup -q

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build

%changelog
* Thu Feb 07 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 4.10.0-1
- New version 4.10.0

* Wed Dec 05 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 4.9.4-1
- New version 4.9.4

* Wed Nov 07 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 4.9.3-1
- New version 4.9.3

* Thu Oct 04 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 4.9.2-1
- New version 4.9.2

* Sat Sep 08 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 4.9.1-1
- New version 4.9.1

* Wed Aug 29 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 4.9.0-1
- New version 4.9.0
- Add pkgconfig(xi) to BuildRequires

* Sat Jul 07 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 4.8.95-1
- New version 4.8.95
- Add pkgconfig(x11) to BuildRequires

* Fri Jun 08 2012 Andrey Bondrov <bondrov@math.dvgu.ru> 4.8.4-69.1mib2010.2
- New version 4.8.4
- MIB (Mandriva International Backports)

* Fri May 04 2012 Andrey Bondrov <bondrov@math.dvgu.ru> 4.8.3-69.1mib2010.2
- New version 4.8.3
- MIB (Mandriva International Backports)

* Wed Apr 04 2012 Andrey Bondrov <bondrov@math.dvgu.ru> 4.8.2-69.1mib2010.2
- New version 4.8.2
- MIB (Mandriva International Backports)

* Wed Mar 07 2012 Andrey Bondrov <bondrov@math.dvgu.ru> 4.8.1-69.1mib2010.2
- New version 4.8.1
- MIB (Mandriva International Backports)

* Mon Feb 20 2012 Andrey Bondrov <bondrov@math.dvgu.ru> 4.8.0-69.1mib2010.2
+ Revision: 198350
- Backport from Mageia to Mandriva 2010.2 for MIB users
- Merge handbook back into main package
- MIB (Mandriva International Backports)

* Thu Jan 19 2012 mikala <mikala> 4.8.0-1.mga2
+ Revision: 198350
- Updating tarball to KDE 4.8.0
- Drop patch0 (merged upstream)

* Thu Jan 05 2012 mikala <mikala> 4.7.97-1.mga2
+ Revision: 191532
- Add patch0 from upstream to add missing add_definition() calls
- Update tarball to kde 4.7.97

* Fri Dec 23 2011 mikala <mikala> 4.7.95-1.mga2
+ Revision: 186273
- Update tarball to kde 4.7.95
- fix group

* Wed Dec 14 2011 mikala <mikala> 4.7.90-1.mga2
+ Revision: 181476
- imported package kremotecontrol

