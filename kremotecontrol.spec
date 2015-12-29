Name:		kremotecontrol
Summary:	KDE Frontend for the LIRC Suite
Version:	15.12.0
Release:	2
Group:		Graphical desktop/KDE
License:	GPLv2 and LGPLv2 and GPLD
URL:		http://www.kde.org/applications/utilities/kremotecontrol/
Source0:	http://download.kde.org/stable/applications/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xi)
BuildRequires:	pkgconfig(xtst)
BuildRequires:	kdelibs4-devel
Requires:	kdebase4-runtime
Obsoletes:	%{name}-devel < 4.11.0
Conflicts:	kdeutils4-core < 4.5.72

%description
KRemoteControl is a KDE frontend for the Linux Infrared Remote Control system
(LIRC).
It consist of two parts: a systemtray applet and a configuration module.

%files
%doc AUTHORS COPYING COPYING.LIB README TODO
%{_bindir}/krcdnotifieritem
%{_libdir}/kde4/kcm_remotecontrol.so
%{_libdir}/kde4/kded_kremotecontroldaemon.so
%{_libdir}/kde4/plasma_engine_kremoteconrol.so
%{_libdir}/kde4/kremotecontrol_lirc.so
%{_datadir}/kde4/services/kremotecontrolbackends/kremotecontrol_lirc.desktop
%{_datadir}/kde4/servicetypes/kremotecontrolmanager.desktop
%{_datadir}/applications/kde4/krcdnotifieritem.desktop
%{_datadir}/apps/kremotecontrol/
%{_datadir}/apps/kremotecontroldaemon/
%{_iconsdir}/*/*/actions/krcd_flash.*
%{_iconsdir}/*/*/actions/krcd_off.*
%{_iconsdir}/*/*/apps/krcd.*
%{_iconsdir}/*/*/devices/infrared-remote.*
%{_datadir}/kde4/services/kcm_remotecontrol.desktop
%{_datadir}/kde4/services/kded/kremotecontroldaemon.desktop
%{_datadir}/kde4/services/plasma-engine-kremotecontrol.desktop
%doc %{_docdir}/HTML/en/kcontrol/kremotecontrol/

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
%{_libdir}/liblibkremotecontrol.so.%{kremotecontrol_major}*

#------------------------------------------------------------------------------

%prep
%setup -q

%build
%cmake_kde4 -DCMAKE_MINIMUM_REQUIRED_VERSION=2.6
%make

%install
%makeinstall_std -C build

# We don't need it because there are no devel headers anyway
rm -f %{buildroot}%{_kde_libdir}/liblibkremotecontrol.so

