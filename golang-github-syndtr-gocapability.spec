#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : golang-github-syndtr-gocapability
Version  : 2c00daeb6c3b45114c80ac44119e7b8801fdd852
Release  : 1
URL      : https://github.com/syndtr/gocapability/archive/2c00daeb6c3b45114c80ac44119e7b8801fdd852.tar.gz
Source0  : https://github.com/syndtr/gocapability/archive/2c00daeb6c3b45114c80ac44119e7b8801fdd852.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-2-Clause
BuildRequires : go

%description
No detailed description available

%prep
%setup -q -n gocapability-2c00daeb6c3b45114c80ac44119e7b8801fdd852

%build

%install
gopath="/usr/lib/golang"
library_path="github.com/syndtr/gocapability"
rm -rf %{buildroot}
install -d -p %{buildroot}${gopath}/src/${library_path}/
for file in $(find . -iname "*.go" -o -iname "*.h" -o -iname "*.c") ; do
     echo ${file}
     install -d -p %{buildroot}${gopath}/src/${library_path}/$(dirname $file)
     cp -pav $file %{buildroot}${gopath}/src/${library_path}/$file
done


%files
%defattr(-,root,root,-)
/usr/lib/golang/src/github.com/syndtr/gocapability/capability/capability.go
/usr/lib/golang/src/github.com/syndtr/gocapability/capability/capability_linux.go
/usr/lib/golang/src/github.com/syndtr/gocapability/capability/capability_noop.go
/usr/lib/golang/src/github.com/syndtr/gocapability/capability/capability_test.go
/usr/lib/golang/src/github.com/syndtr/gocapability/capability/enum.go
/usr/lib/golang/src/github.com/syndtr/gocapability/capability/enum_gen.go
/usr/lib/golang/src/github.com/syndtr/gocapability/capability/enumgen/gen.go
/usr/lib/golang/src/github.com/syndtr/gocapability/capability/syscall_linux.go
