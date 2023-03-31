%bcond_without check
%global debug_package %{nil}

%global crate serde_derive

Name:           rust-%{crate}
Version:        1.0.125
Release:        2
Summary:        Macros 1.1 implementation of #[derive(Serialize, Deserialize)]

# Upstream license specification: MIT OR Apache-2.0
License:        MIT or ASL 2.0
URL:            https://crates.io/crates/serde_derive
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Macros 1.1 implementation of #[derive(Serialize, Deserialize)].}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%license LICENSE-MIT LICENSE-APACHE
%doc README.md crates-io.md
%{cargo_registry}/%{crate}-%{version}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages
which use "default" feature of "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{cargo_registry}/%{crate}-%{version}/Cargo.toml

%package     -n %{name}+deserialize_in_place-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+deserialize_in_place-devel %{_description}

This package contains library source intended for building other packages
which use "deserialize_in_place" feature of "%{crate}" crate.

%files       -n %{name}+deserialize_in_place-devel
%ghost %{cargo_registry}/%{crate}-%{version}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version_no_tilde} -p1
%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires

%build
%cargo_build

%install
%cargo_install

%if %{with check}
%check
%cargo_test
%endif
