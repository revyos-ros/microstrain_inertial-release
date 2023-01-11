%bcond_without tests
%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/humble/.*$
%global __requires_exclude_from ^/opt/ros/humble/.*$

Name:           ros-humble-microstrain-inertial-driver
Version:        3.0.0
Release:        1%{?dist}%{?release_suffix}
Summary:        ROS microstrain_inertial_driver package

License:        MIT
URL:            https://github.com/LORD-MicroStrain/microstrain_inertial
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-humble-diagnostic-aggregator
Requires:       ros-humble-diagnostic-updater
Requires:       ros-humble-geometry-msgs
Requires:       ros-humble-lifecycle-msgs
Requires:       ros-humble-mavros-msgs
Requires:       ros-humble-microstrain-inertial-msgs
Requires:       ros-humble-nav-msgs
Requires:       ros-humble-nmea-msgs
Requires:       ros-humble-rclcpp-lifecycle
Requires:       ros-humble-rosidl-default-runtime
Requires:       ros-humble-sensor-msgs
Requires:       ros-humble-std-msgs
Requires:       ros-humble-std-srvs
Requires:       ros-humble-tf2
Requires:       ros-humble-tf2-geometry-msgs
Requires:       ros-humble-tf2-ros
Requires:       ros-humble-ros-workspace
BuildRequires:  curl
BuildRequires:  git
BuildRequires:  jq
BuildRequires:  libcurl-devel
BuildRequires:  ros-humble-ament-cmake-gtest
BuildRequires:  ros-humble-ament-cpplint
BuildRequires:  ros-humble-diagnostic-updater
BuildRequires:  ros-humble-geometry-msgs
BuildRequires:  ros-humble-lifecycle-msgs
BuildRequires:  ros-humble-mavros-msgs
BuildRequires:  ros-humble-microstrain-inertial-msgs
BuildRequires:  ros-humble-nav-msgs
BuildRequires:  ros-humble-nmea-msgs
BuildRequires:  ros-humble-rclcpp-lifecycle
BuildRequires:  ros-humble-ros-environment
BuildRequires:  ros-humble-rosidl-default-generators
BuildRequires:  ros-humble-sensor-msgs
BuildRequires:  ros-humble-std-msgs
BuildRequires:  ros-humble-std-srvs
BuildRequires:  ros-humble-tf2
BuildRequires:  ros-humble-tf2-geometry-msgs
BuildRequires:  ros-humble-tf2-ros
BuildRequires:  ros-humble-ros-workspace
BuildRequires:  ros-humble-rosidl-typesupport-fastrtps-c
BuildRequires:  ros-humble-rosidl-typesupport-fastrtps-cpp
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}
Provides:       ros-humble-rosidl-interface-packages(member)

%if 0%{?with_weak_deps}
Supplements:    ros-humble-rosidl-interface-packages(all)
%endif

%description
The ros_mscl package provides a driver for the LORD/Microstrain inertial
products.

%prep
%autosetup -p1

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/humble/setup.sh" ]; then . "/opt/ros/humble/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake3 \
    -UINCLUDE_INSTALL_DIR \
    -ULIB_INSTALL_DIR \
    -USYSCONF_INSTALL_DIR \
    -USHARE_INSTALL_PREFIX \
    -ULIB_SUFFIX \
    -DCMAKE_INSTALL_PREFIX="/opt/ros/humble" \
    -DAMENT_PREFIX_PATH="/opt/ros/humble" \
    -DCMAKE_PREFIX_PATH="/opt/ros/humble" \
    -DSETUPTOOLS_DEB_LAYOUT=OFF \
    ..

%make_build

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/humble/setup.sh" ]; then . "/opt/ros/humble/setup.sh"; fi
%make_install -C obj-%{_target_platform}

%if 0%{?with_tests}
%check
# Look for a Makefile target with a name indicating that it runs tests
TEST_TARGET=$(%__make -qp -C obj-%{_target_platform} | sed "s/^\(test\|check\):.*/\\1/;t f;d;:f;q0")
if [ -n "$TEST_TARGET" ]; then
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/humble/setup.sh" ]; then . "/opt/ros/humble/setup.sh"; fi
CTEST_OUTPUT_ON_FAILURE=1 \
    %make_build -C obj-%{_target_platform} $TEST_TARGET || echo "RPM TESTS FAILED"
else echo "RPM TESTS SKIPPED"; fi
%endif

%files
/opt/ros/humble

%changelog
* Wed Jan 11 2023 Rob Fisher <rob.fisher@parker.com> - 3.0.0-1
- Autogenerated by Bloom

* Wed Nov 09 2022 Rob Fisher <rob.fisher@parker.com> - 2.7.1-1
- Autogenerated by Bloom

* Fri Sep 23 2022 Rob Fisher <rob.fisher@parker.com> - 2.7.0-1
- Autogenerated by Bloom

* Wed May 25 2022 Rob Fisher <rob.fisher@parker.com> - 2.6.0-1
- Autogenerated by Bloom

* Tue Apr 19 2022 Rob Fisher <rob.fisher@parker.com> - 2.5.1-2
- Autogenerated by Bloom

* Tue Feb 15 2022 Rob Fisher <rob.fisher@parker.com> - 2.5.1-1
- Autogenerated by Bloom

* Tue Feb 08 2022 Rob Fisher <rob.fisher@parker.com> - 2.5.0-2
- Autogenerated by Bloom

