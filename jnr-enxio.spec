Name:                jnr-enxio
Version:             0.19
Release:             2
Summary:             Unix sockets for Java
License:             ASL 2.0 and LGPLv3
URL:                 https://github.com/jnr/%{name}/
Source0:             https://github.com/jnr/%{name}/archive/%{name}-%{version}.tar.gz
Patch0:              0001-Add-enxio-classes-from-jnr-unixsocket.patch
BuildArch:           noarch
BuildRequires:       maven-local mvn(com.github.jnr:jnr-constants) mvn(com.github.jnr:jnr-ffi)
BuildRequires:       mvn(junit:junit) mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:       mvn(org.apache.maven.plugins:maven-source-plugin)
BuildRequires:       mvn(org.sonatype.oss:oss-parent:pom:)
%description
Unix sockets for Java.

%package javadoc
Summary:             Javadocs for %{name}
%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n %{name}-%{name}-%{version}
%patch0 -p1
find ./ -name '*.jar' -delete
find ./ -name '*.class' -delete
%pom_remove_plugin ":maven-javadoc-plugin"

%pom_add_plugin org.apache.maven.plugins:maven-surefire-plugin:2.22.0 . "
<configuration>
    <skipTests>true</skipTests>
</configuration>"

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%license LICENSE

%files javadoc -f .mfiles-javadoc
%license LICENSE

%changelog
* Mon Mar 28 2022 wujie <wujie@nj.iscas.ac.cn> - 0.19-2
- Fix build error

* Thu Jul 30 2020 Jeffery.Gao <gaojianxing@huawei.com> - 0.19-1
- Package init
