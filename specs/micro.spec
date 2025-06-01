%global debug_package %{nil}

# set to nil when packaging a release, 
# or the long commit tag for the specific git branch
%global commit_tag %{nil}

# set with the commit date only if commit_tag not nil 
# git version (i.e. master) in format date +Ymd
%if "%{commit_tag}" != "%{nil}"
%global commit_date %(git show -s --date=format:'%Y%m%d' %{commit_tag})
%endif

# repack non-release git branches as .xz with the commit date
# in the following format <name>-<version>-<commit_date>.xz
# the short commit tag should be 7 characters long

Name:           micro
Version:        2.0.14
Release:	      %{?commit_date:~0.%{commit_date}.}1
Summary:        A modern and intuitive terminal-based text editor
Group:          Utilities
License:        MIT
URL:            https://micro-editor.github.io/

# change the source URL depending on if the package is a release version or a git version
%if "%{commit_tag}" != "%{nil}"
Source0:        https://github.com/<org_name>/<project_name>/archive/%{commit_tag}.tar.gz#/%{name}-%{version}.xz
%else
Source0:        https://github.com/zyedidia/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.bz2
%endif

BuildRequires: golang-bin
BuildRequires: make

%prep
%autosetup -p1

%build
%make_build build

%install
mkdir -p %{buildroot}%{_bindir}
mv micro %{buildroot}%{_bindir}

%description
micro is a terminal-based text editor that aims to be easy to use and intuitive, 
while also taking advantage of the capabilities of modern terminals.

%files
%license LICENSE LICENSE-THIRD-PARTY
%doc README.md
%{_bindir}/micro

