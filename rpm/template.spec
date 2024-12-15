%bcond_without tests
%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/jazzy/.*$
%global __requires_exclude_from ^/opt/ros/jazzy/.*$

Name:           ros-jazzy-microstrain-inertial-rqt
Version:        4.5.0
Release:        1%{?dist}%{?release_suffix}
Summary:        ROS microstrain_inertial_rqt package

License:        BSD
URL:            https://github.com/LORD-MicroStrain/microstrain_inertial
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-jazzy-geometry-msgs
Requires:       ros-jazzy-microstrain-inertial-msgs
Requires:       ros-jazzy-nav-msgs
Requires:       ros-jazzy-rclpy
Requires:       ros-jazzy-rqt-gui
Requires:       ros-jazzy-rqt-gui-py
Requires:       ros-jazzy-std-msgs
Requires:       ros-jazzy-ros-workspace
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  ros-jazzy-geometry-msgs
BuildRequires:  ros-jazzy-microstrain-inertial-msgs
BuildRequires:  ros-jazzy-nav-msgs
BuildRequires:  ros-jazzy-rclpy
BuildRequires:  ros-jazzy-ros-workspace
BuildRequires:  ros-jazzy-rqt-gui
BuildRequires:  ros-jazzy-rqt-gui-py
BuildRequires:  ros-jazzy-std-msgs
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}

%description
The microstrain_inertial_rqt package provides several RQT widgets to view the
status of Microstrain devices

%prep
%autosetup -p1

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jazzy/setup.sh" ]; then . "/opt/ros/jazzy/setup.sh"; fi
%py3_build

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jazzy/setup.sh" ]; then . "/opt/ros/jazzy/setup.sh"; fi
%py3_install -- --prefix "/opt/ros/jazzy"

%if 0%{?with_tests}
%check
# Look for a directory with a name indicating that it contains tests
TEST_TARGET=$(ls -d * | grep -m1 "\(test\|tests\)" ||:)
if [ -n "$TEST_TARGET" ] && %__python3 -m pytest --version; then
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jazzy/setup.sh" ]; then . "/opt/ros/jazzy/setup.sh"; fi
%__python3 -m pytest $TEST_TARGET || echo "RPM TESTS FAILED"
else echo "RPM TESTS SKIPPED"; fi
%endif

%files
/opt/ros/jazzy

%changelog
* Sun Dec 15 2024 Rob Fisher <rob.fisher@parker.com> - 4.5.0-1
- Autogenerated by Bloom

* Wed Oct 09 2024 Rob Fisher <rob.fisher@parker.com> - 4.4.0-1
- Autogenerated by Bloom

* Wed Jun 19 2024 Rob Fisher <rob.fisher@parker.com> - 4.3.0-2
- Autogenerated by Bloom

* Wed May 15 2024 Rob Fisher <rob.fisher@parker.com> - 4.3.0-1
- Autogenerated by Bloom

* Thu Apr 18 2024 Rob Fisher <rob.fisher@parker.com> - 4.2.0-2
- Autogenerated by Bloom

* Thu Apr 04 2024 Rob Fisher <rob.fisher@parker.com> - 4.2.0-1
- Autogenerated by Bloom

* Tue Apr 02 2024 Rob Fisher <rob.fisher@parker.com> - 4.1.0-1
- Autogenerated by Bloom

* Wed Mar 06 2024 Rob Fisher <rob.fisher@parker.com> - 3.2.1-2
- Autogenerated by Bloom

