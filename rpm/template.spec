Name:           ros-indigo-graspdb
Version:        1.1.5
Release:        0%{?dist}
Summary:        ROS graspdb package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/graspdb
Source0:        %{name}-%{version}.tar.gz

Requires:       libpqxx-devel
Requires:       ros-indigo-geometry-msgs
Requires:       ros-indigo-rail-pick-and-place-msgs
Requires:       ros-indigo-roscpp
Requires:       ros-indigo-roscpp-serialization
Requires:       ros-indigo-sensor-msgs
Requires:       ros-indigo-tf2
BuildRequires:  libpqxx-devel
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-geometry-msgs
BuildRequires:  ros-indigo-rail-pick-and-place-msgs
BuildRequires:  ros-indigo-roscpp
BuildRequires:  ros-indigo-roscpp-serialization
BuildRequires:  ros-indigo-sensor-msgs
BuildRequires:  ros-indigo-tf2

%description
Grasp Training SQL Database Client Library

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Wed Apr 29 2015 Russell Toris <rctoris@wpi.edu> - 1.1.5-0
- Autogenerated by Bloom

* Mon Apr 27 2015 Russell Toris <rctoris@wpi.edu> - 1.1.4-0
- Autogenerated by Bloom

* Tue Apr 14 2015 Russell Toris <rctoris@wpi.edu> - 1.1.3-0
- Autogenerated by Bloom

* Fri Apr 10 2015 Russell Toris <rctoris@wpi.edu> - 1.1.2-0
- Autogenerated by Bloom

* Mon Apr 06 2015 Russell Toris <rctoris@wpi.edu> - 1.1.1-0
- Autogenerated by Bloom

* Fri Apr 03 2015 Russell Toris <rctoris@wpi.edu> - 1.1.0-0
- Autogenerated by Bloom

* Tue Mar 31 2015 Russell Toris <rctoris@wpi.edu> - 1.0.4-0
- Autogenerated by Bloom

* Tue Mar 31 2015 Russell Toris <rctoris@wpi.edu> - 1.0.3-0
- Autogenerated by Bloom

* Mon Mar 30 2015 Russell Toris <rctoris@wpi.edu> - 1.0.2-0
- Autogenerated by Bloom

* Fri Mar 27 2015 Russell Toris <rctoris@wpi.edu> - 1.0.1-0
- Autogenerated by Bloom

* Fri Mar 27 2015 Russell Toris <rctoris@wpi.edu> - 1.0.0-0
- Autogenerated by Bloom

