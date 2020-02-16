# Generated from sahara-0.0.17.gem by gem2rpm -*- rpm-spec -*-
%global gem_name sahara
%global vagrant_plugin_name sahara

Name: vagrant-%{gem_name}
Version: 0.0.17
Release: 1%{?dist}
BuildArch: noarch

Summary: Vagrant box creation
License: MIT
URL: http://github.com/jedi4ever/sahara/
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

BuildRequires: ruby(release)
BuildRequires: rubygems-devel >= 1.3.6
BuildRequires: ruby
BuildRequires: vagrant >= 1.9.1

Requires: vagrant >= 1.9.1

%description
Allows you to sandbox your vagrant.

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
gem unpack %{SOURCE0}
%setup -q -D -T -n  %{gem_name}-%{version}
gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec

%build
gem build %{gem_name}.gemspec
%vagrant_plugin_install

%install
rm -rf .%{vagrant_plugin_dir}/gems/%{gem_name}-%{version}/test

mkdir -p %{buildroot}%{vagrant_plugin_dir}
cp -a .%{vagrant_plugin_dir}/* \
       %{buildroot}%{vagrant_plugin_dir}/



%files
%dir %{vagrant_plugin_instdir}
%exclude %{vagrant_plugin_instdir}/.gitignore
%exclude %{vagrant_plugin_instdir}/vagrant-sahara.spec
%{vagrant_plugin_libdir}
%{vagrant_plugin_instdir}/locales
%exclude %{vagrant_plugin_cache}
%{vagrant_plugin_spec}

%files doc
%doc %{vagrant_plugin_docdir}
%{vagrant_plugin_instdir}/Gemfile
%doc %{vagrant_plugin_instdir}/README.md
%{vagrant_plugin_instdir}/Rakefile
%{vagrant_plugin_instdir}/sahara.gemspec

%changelog
* Sat Feb 08 2020 Jonathon Turel <jturel@gmail.com> - 0.0.17-1
- Initial package
