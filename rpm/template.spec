%bcond_without tests
%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/iron/.*$
%global __requires_exclude_from ^/opt/ros/iron/.*$

Name:           ros-iron-microstrain-inertial-driver
Version:        3.2.0
Release:        1%{?dist}%{?release_suffix}
Summary:        ROS microstrain_inertial_driver package

License:        MIT
URL:            https://github.com/LORD-MicroStrain/microstrain_inertial
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-iron-diagnostic-aggregator
Requires:       ros-iron-diagnostic-updater
Requires:       ros-iron-geometry-msgs
Requires:       ros-iron-lifecycle-msgs
Requires:       ros-iron-mavros-msgs
Requires:       ros-iron-microstrain-inertial-msgs
Requires:       ros-iron-nav-msgs
Requires:       ros-iron-nmea-msgs
Requires:       ros-iron-rclcpp-lifecycle
Requires:       ros-iron-rosidl-default-runtime
Requires:       ros-iron-sensor-msgs
Requires:       ros-iron-std-msgs
Requires:       ros-iron-std-srvs
Requires:       ros-iron-tf2
Requires:       ros-iron-tf2-geometry-msgs
Requires:       ros-iron-tf2-ros
Requires:       ros-iron-ros-workspace
BuildRequires:  curl
BuildRequires:  git
BuildRequires:  jq
BuildRequires:  libcurl-devel
BuildRequires:  ros-iron-ament-cmake-gtest
BuildRequires:  ros-iron-ament-cpplint
BuildRequires:  ros-iron-diagnostic-updater
BuildRequires:  ros-iron-geometry-msgs
BuildRequires:  ros-iron-lifecycle-msgs
BuildRequires:  ros-iron-mavros-msgs
BuildRequires:  ros-iron-microstrain-inertial-msgs
BuildRequires:  ros-iron-nav-msgs
BuildRequires:  ros-iron-nmea-msgs
BuildRequires:  ros-iron-rclcpp-lifecycle
BuildRequires:  ros-iron-ros-environment
BuildRequires:  ros-iron-rosidl-default-generators
BuildRequires:  ros-iron-sensor-msgs
BuildRequires:  ros-iron-std-msgs
BuildRequires:  ros-iron-std-srvs
BuildRequires:  ros-iron-tf2
BuildRequires:  ros-iron-tf2-geometry-msgs
BuildRequires:  ros-iron-tf2-ros
BuildRequires:  ros-iron-ros-workspace
BuildRequires:  ros-iron-rosidl-typesupport-fastrtps-c
BuildRequires:  ros-iron-rosidl-typesupport-fastrtps-cpp
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}
Provides:       ros-iron-rosidl-interface-packages(member)

%if 0%{?with_weak_deps}
Supplements:    ros-iron-rosidl-interface-packages(all)
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
if [ -f "/opt/ros/iron/setup.sh" ]; then . "/opt/ros/iron/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake3 \
    -UINCLUDE_INSTALL_DIR \
    -ULIB_INSTALL_DIR \
    -USYSCONF_INSTALL_DIR \
    -USHARE_INSTALL_PREFIX \
    -ULIB_SUFFIX \
    -DCMAKE_INSTALL_PREFIX="/opt/ros/iron" \
    -DAMENT_PREFIX_PATH="/opt/ros/iron" \
    -DCMAKE_PREFIX_PATH="/opt/ros/iron" \
    -DSETUPTOOLS_DEB_LAYOUT=OFF \
    ..

%make_build

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/iron/setup.sh" ]; then . "/opt/ros/iron/setup.sh"; fi
%make_install -C obj-%{_target_platform}

%if 0%{?with_tests}
%check
# Look for a Makefile target with a name indicating that it runs tests
TEST_TARGET=$(%__make -qp -C obj-%{_target_platform} | sed "s/^\(test\|check\):.*/\\1/;t f;d;:f;q0")
if [ -n "$TEST_TARGET" ]; then
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/iron/setup.sh" ]; then . "/opt/ros/iron/setup.sh"; fi
CTEST_OUTPUT_ON_FAILURE=1 \
    %make_build -C obj-%{_target_platform} $TEST_TARGET || echo "RPM TESTS FAILED"
else echo "RPM TESTS SKIPPED"; fi
%endif

%files
/opt/ros/iron

%changelog
* Thu Dec 21 2023 Rob Fisher <rob.fisher@parker.com> - 3.2.0-1
- Autogenerated by Bloom

* Tue Jul 25 2023 Rob Fisher <rob.fisher@parker.com> - 3.1.0-1
- Autogenerated by Bloom

* Thu Apr 20 2023 Rob Fisher <rob.fisher@parker.com> - 3.0.1-3
- Autogenerated by Bloom

* Tue Mar 21 2023 Rob Fisher <rob.fisher@parker.com> - 3.0.1-2
- Autogenerated by Bloom

