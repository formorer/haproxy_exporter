Name:           haproxy_exporter   
Version:        0.7.0
Release:        1%{?dist}
Summary:        haproxy_exporter for prometheus
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Source0:        haproxy_exporter
Source1:        haproxy_exporter.service
License:        GPL


%description
Prometheus Exporter for haproxy metrics 

%install
mkdir -p $RPM_BUILD_ROOT/usr/bin
mkdir -p $RPM_BUILD_ROOT/lib/systemd/system/
pwd
install -m 755 %{_sourcedir}/haproxy_exporter $RPM_BUILD_ROOT/usr/bin
install -m 644 %{_sourcedir}/haproxy_exporter.service $RPM_BUILD_ROOT/lib/systemd/system/

%files
/lib/systemd/system/haproxy_exporter.service
/usr/bin/haproxy_exporter

%doc



%changelog
