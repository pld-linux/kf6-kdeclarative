#
# Conditional build:
%bcond_with	tests		# build with tests
%define		kdeframever	6.14
%define		qtver		5.15.2
%define		kfname		kdeclarative

Summary:	Integration of QML and KDE work spaces
Name:		kf6-%{kfname}
Version:	6.14.0
Release:	1
License:	LGPL v2.1+
Group:		X11/Libraries
Source0:	https://download.kde.org/stable/frameworks/%{kdeframever}/%{kfname}-%{version}.tar.xz
# Source0-md5:	28909eaeb864dbf762ceac989e9da424
URL:		http://www.kde.org/
BuildRequires:	Qt6Core-devel >= %{qtver}
BuildRequires:	Qt6DBus-devel >= %{qtver}
BuildRequires:	Qt6Gui-devel >= %{qtver}
BuildRequires:	Qt6Network-devel >= %{qtver}
BuildRequires:	Qt6Qml-devel >= %{qtver}
BuildRequires:	Qt6Quick-devel >= %{qtver}
BuildRequires:	Qt6ShaderTools-devel
BuildRequires:	Qt6Test-devel >= %{qtver}
BuildRequires:	Qt6Widgets-devel >= %{qtver}
BuildRequires:	Qt6Xml-devel >= %{qtver}
BuildRequires:	cmake >= 3.16
BuildRequires:	gettext-devel
BuildRequires:	kf6-attica-devel >= %{version}
BuildRequires:	kf6-extra-cmake-modules >= %{version}
BuildRequires:	kf6-kauth-devel >= %{version}
BuildRequires:	kf6-kbookmarks-devel >= %{version}
BuildRequires:	kf6-kcodecs-devel >= %{version}
BuildRequires:	kf6-kcompletion-devel >= %{version}
BuildRequires:	kf6-kconfig-devel >= %{version}
BuildRequires:	kf6-kconfigwidgets-devel >= %{version}
BuildRequires:	kf6-kcoreaddons-devel >= %{version}
BuildRequires:	kf6-kdbusaddons-devel >= %{version}
BuildRequires:	kf6-kglobalaccel-devel >= %{version}
BuildRequires:	kf6-kguiaddons-devel >= %{version}
BuildRequires:	kf6-ki18n-devel >= %{version}
BuildRequires:	kf6-kiconthemes-devel >= %{version}
BuildRequires:	kf6-kio-devel >= %{version}
BuildRequires:	kf6-kitemviews-devel >= %{version}
BuildRequires:	kf6-kjobwidgets-devel >= %{version}
BuildRequires:	kf6-kpackage-devel >= %{version}
BuildRequires:	kf6-kservice-devel >= %{version}
BuildRequires:	kf6-ktextwidgets-devel >= %{version}
BuildRequires:	kf6-kwidgetsaddons-devel >= %{version}
BuildRequires:	kf6-kwindowsystem-devel >= %{version}
BuildRequires:	kf6-kxmlgui-devel >= %{version}
BuildRequires:	kf6-solid-devel >= %{version}
BuildRequires:	kf6-sonnet-devel >= %{version}
BuildRequires:	libepoxy-devel
BuildRequires:	ninja
BuildRequires:	qt6-shadertools
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	kf6-dirs
#Obsoletes:	kf5-%{kfname} < %{version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		qt6dir		%{_libdir}/qt6

%description
KDeclarative provides integration of QML and KDE work spaces.

%package devel
Summary:	Header files for %{kfname} development
Summary(pl.UTF-8):	Pliki nagłówkowe dla programistów używających %{kfname}
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	kf6-kconfig-devel
Requires:	kf6-kpackage-devel
#Obsoletes:	kf5-%{kfname}-devel < %{version}

%description devel
Header files for %{kfname} development.

%description devel -l pl.UTF-8
Pliki nagłówkowe dla programistów używających %{kfname}.

%prep
%setup -q -n %{kfname}-%{version}

%build
%cmake -B build \
	-G Ninja \
	%{!?with_tests:-DBUILD_TESTING=OFF} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON

%ninja_build -C build

%if %{with tests}
%ninja_build -C build test
%endif


%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

%find_lang %{kfname}6

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f %{kfname}6.lang
%defattr(644,root,root,755)
%doc README.md
%ghost %{_libdir}/libKF6CalendarEvents.so.6
%attr(755,root,root) %{_libdir}/libKF6CalendarEvents.so.*.*
%dir %{_libdir}/qt6/qml/org/kde/draganddrop
%{_libdir}/qt6/qml/org/kde/draganddrop/draganddropplugin.qmltypes
%{_libdir}/qt6/qml/org/kde/draganddrop/kde-qmlmodule.version
%attr(755,root,root) %{_libdir}/qt6/qml/org/kde/draganddrop/libdraganddropplugin.so
%{_libdir}/qt6/qml/org/kde/draganddrop/qmldir
%dir %{_libdir}/qt6/qml/org/kde/graphicaleffects
%{_libdir}/qt6/qml/org/kde/graphicaleffects/BadgeEffect.qml
%{_libdir}/qt6/qml/org/kde/graphicaleffects/Lanczos.qml
%{_libdir}/qt6/qml/org/kde/graphicaleffects/graphicaleffects.qmltypes
%{_libdir}/qt6/qml/org/kde/graphicaleffects/kde-qmlmodule.version
%attr(755,root,root) %{_libdir}/qt6/qml/org/kde/graphicaleffects/libgraphicaleffects.so
%{_libdir}/qt6/qml/org/kde/graphicaleffects/qmldir
%dir %{_libdir}/qt6/qml/org/kde/kquickcontrols
%{_libdir}/qt6/qml/org/kde/kquickcontrols/ColorButton.qml
%{_libdir}/qt6/qml/org/kde/kquickcontrols/KeySequenceItem.qml
%{_libdir}/qt6/qml/org/kde/kquickcontrols/qmldir
%dir %{_libdir}/qt6/qml/org/kde/kquickcontrolsaddons
%{_libdir}/qt6/qml/org/kde/kquickcontrolsaddons/kde-qmlmodule.version
%{_libdir}/qt6/qml/org/kde/kquickcontrolsaddons/kquickcontrolsaddonsplugin.qmltypes
%attr(755,root,root) %{_libdir}/qt6/qml/org/kde/kquickcontrolsaddons/libkquickcontrolsaddonsplugin.so
%{_libdir}/qt6/qml/org/kde/kquickcontrolsaddons/qmldir
%dir %{_libdir}/qt6/qml/org/kde/private/kquickcontrols
%attr(755,root,root) %{_libdir}/qt6/qml/org/kde/private/kquickcontrols/libkquickcontrolsprivateplugin.so
%{_libdir}/qt6/qml/org/kde/private/kquickcontrols/qmldir
%ghost %{_libdir}/libkquickcontrolsprivate.so.0
%attr(755,root,root) %{_libdir}/libkquickcontrolsprivate.so.*.*
%{_libdir}/qt6/qml/org/kde/kquickcontrols/kde-qmlmodule.version
%{_libdir}/qt6/qml/org/kde/kquickcontrols/kquickcontrols.qmltypes
%{_libdir}/qt6/qml/org/kde/kquickcontrols/libkquickcontrols.so
%{_libdir}/qt6/qml/org/kde/private/kquickcontrols/kde-qmlmodule.version
%{_libdir}/qt6/qml/org/kde/private/kquickcontrols/kquickcontrolsprivate.qmltypes


%files devel
%defattr(644,root,root,755)
%{_includedir}/KF6/KDeclarative
%{_libdir}/cmake/KF6Declarative
%{_libdir}/libKF6CalendarEvents.so
