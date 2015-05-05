Name:           ros-indigo-rail-pick-and-place-tools
Version:        1.1.6
Release:        0%{?dist}
Summary:        ROS rail_pick_and_place_tools package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/rail_pick_and_place_tools
Source0:        %{name}-%{version}.tar.gz

Requires:       boost-devel
Requires:       ros-indigo-actionlib
Requires:       ros-indigo-graspdb
Requires:       ros-indigo-rail-grasp-collection
Requires:       ros-indigo-rail-pick-and-place-msgs
Requires:       ros-indigo-rail-recognition
Requires:       ros-indigo-roscpp
Requires:       ros-indigo-rviz
Requires:       ros-indigo-std-srvs
BuildRequires:  boost-devel
BuildRequires:  ros-indigo-actionlib
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-graspdb
BuildRequires:  ros-indigo-rail-pick-and-place-msgs
BuildRequires:  ros-indigo-roscpp
BuildRequires:  ros-indigo-rviz
BuildRequires:  ros-indigo-std-srvs

%description
RViz Plugins for Collecting Grasps and Generating Models

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
* Tue May 05 2015 David Kent <davidkent@wpi.edu> - 1.1.6-0
- Autogenerated by Bloom

* Wed Apr 29 2015 David Kent <davidkent@wpi.edu> - 1.1.5-0
- Autogenerated by Bloom

* Mon Apr 27 2015 David Kent <davidkent@wpi.edu> - 1.1.4-0
- Autogenerated by Bloom

* Tue Apr 14 2015 David Kent <davidkent@wpi.edu> - 1.1.3-0
- Autogenerated by Bloom

* Fri Apr 10 2015 David Kent <davidkent@wpi.edu> - 1.1.2-0
- Autogenerated by Bloom

* Mon Apr 06 2015 David Kent <davidkent@wpi.edu> - 1.1.1-0
- Autogenerated by Bloom

* Fri Apr 03 2015 David Kent <davidkent@wpi.edu> - 1.1.0-0
- Autogenerated by Bloom

* Tue Mar 31 2015 David Kent <davidkent@wpi.edu> - 1.0.4-0
- Autogenerated by Bloom

* Tue Mar 31 2015 David Kent <davidkent@wpi.edu> - 1.0.3-0
- Autogenerated by Bloom

* Mon Mar 30 2015 David Kent <davidkent@wpi.edu> - 1.0.2-0
- Autogenerated by Bloom

* Fri Mar 27 2015 David Kent <davidkent@wpi.edu> - 1.0.1-0
- Autogenerated by Bloom

* Fri Mar 27 2015 David Kent <davidkent@wpi.edu> - 1.0.0-0
- Autogenerated by Bloom

