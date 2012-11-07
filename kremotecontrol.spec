Name:       kremotecontrol
Summary:    KDE Frontend for the LIRC Suite
Version: 4.9.3
Release: 1
Group:      Accessibility
License:    GPLv2 and LGPLv2 and GPLD
URL:        http://www.kde.org/applications/utilities/kremotecontrol/
Source0:    ftp://ftp.kde.org/pub/kde/stable/%{version}/src/%name-%{version}.tar.xz

BuildRequires: kdebase4-workspace-devel >= 2:%version
BuildRequires: libxi-devel
BuildRequires:  pkgconfig(xtst)
Requires:  kdebase4-runtime
Conflicts: kdeutils4-core < 4.5.72
Suggests:  kremotecontrol-handbook

%description
KRemoteControl is a KDE frontend for the Linux Infrared Remote Control system 
(LIRC).
It consist of two parts: a systemtray applet and a configuration module.

%files
%_kde_bindir/krcdnotifieritem
%_kde_libdir/kde4/kcm_remotecontrol.so
%_kde_libdir/kde4/kded_kremotecontroldaemon.so
%_kde_libdir/kde4/plasma_engine_kremoteconrol.so
%_kde_libdir/kde4/kremotecontrol_lirc.so
%_kde_services/kremotecontrolbackends/kremotecontrol_lirc.desktop
%_kde_servicetypes/kremotecontrolmanager.desktop
%_kde_applicationsdir/krcdnotifieritem.desktop
%_kde_appsdir/kremotecontrol/
%_kde_appsdir/kremotecontroldaemon/
%_kde_iconsdir/*/*/actions/krcd_flash.*
%_kde_iconsdir/*/*/actions/krcd_off.*
%_kde_iconsdir/*/*/apps/krcd.*
%_kde_iconsdir/*/*/devices/infrared-remote.*
%_kde_services/kcm_remotecontrol.desktop
%_kde_services/kded/kremotecontroldaemon.desktop
%_kde_services/plasma-engine-kremotecontrol.desktop

#------------------------------------------------------------------------------

%package -n kremotecontrol-handbook
Summary: kremotecontrol Handbook
Conflicts: kremotecontrol < 4.7.1
BuildArch: noarch
Group: Books/Other
%description -n kremotecontrol-handbook
KRemoteControl is a KDE frontend for the Linux Infrared Remote Control system 
(LIRC). It consist of two parts: a systemtray applet and a configuration module.

This package provides kremotecontrol handbook.

%files -n kremotecontrol-handbook
%doc AUTHORS ChangeLog COPYING COPYING.LIB README TODO
%docdir %_kde_docdir
%_kde_docdir/HTML/en/kcontrol/kremotecontrol/

#------------------------------------------------------------------------------

%define kremotecontrol_major 1
%define libkremotecontrol %mklibname kremotecontrol %{kremotecontrol_major}
%define oldlibkremotecontrol  %mklibname libkremotecontrol 1

%package -n %libkremotecontrol
Summary: Runtime library for kremotecontrol
Group: System/Libraries
Obsoletes: %oldlibkremotecontrol < 4.7.90

%description -n %libkremotecontrol
KRemoteControl is a KDE frontend for the Linux Infrared Remote Control system 
(LIRC). It consist of two parts: a systemtray applet and a configuration module.

This package provides the runtime library for kremotecontrol.

%files -n %libkremotecontrol
%_kde_libdir/liblibkremotecontrol.so.%{kremotecontrol_major}*

#------------------------------------------------------------------------------

%package devel
Summary: Devel stuff for %{name}
Group: Development/KDE and Qt
Requires: kdelibs4-devel >= 2:%{version}
Requires: %libkremotecontrol = %version-%release
Conflicts: kdeutils4-devel < 4.7.90
%description devel
KRemoteControl is a KDE frontend for the Linux Infrared Remote Control system 
(LIRC). It consist of two parts: a systemtray applet and a configuration module.

This package contains header files needed if you wish to build applications
based on %{name}.

%files devel
%_kde_libdir/liblibkremotecontrol.so

#------------------------------------------------------------------------------

%prep
%setup -q
%apply_patches

%build
%cmake_kde4 -DKDE4_ENABLE_FINAL=ON
%make

%install
rm -fr %buildroot
%makeinstall_std -C build
