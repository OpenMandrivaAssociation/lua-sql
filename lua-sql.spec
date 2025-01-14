%define luaver 5.1
%define lualibdir %{_libdir}/lua/%{luaver}
%define luapkgdir %{_datadir}/lua/%{luaver}
%define oname luasql

Name:           lua-sql
Version:        2.6.0
Release:        1
Summary:        Database connectivity for the Lua programming language

Group:          Development/Other
License:        MIT
URL:            https://www.keplerproject.org/luasql/
Source0:        http://luaforge.net/frs/download.php/2686/%{oname}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot

BuildRequires:  lua >= %{luaver}, lua-devel >= %{luaver}
BuildRequires:  pkgconfig
BuildRequires:  sqlite3-devel >= 3.0
BuildRequires:  mysql-devel
BuildRequires:  postgresql-devel

Requires:       lua-sql-sqlite, lua-sql-mysql, lua-sql-postgresql, lua-sql-doc

%description
LuaSQL is a simple interface from Lua to a DBMS. This package of LuaSQL
supports MySQL, SQLite and PostgreSQL databases. You can execute arbitrary SQL
statements and it allows for retrieving results in a row-by-row cursor fashion.

%package doc
Summary:        Documentation for LuaSQL
Group:          Development/Other
Requires:       lua >= %{luaver}
%description doc
LuaSQL is a simple interface from Lua to a DBMS. This package contains the
documentation for LuaSQL.


%package sqlite
Summary:        SQLite database connectivity for the Lua programming language
Group:          Development/Other
Requires:       lua >= %{luaver}
%description sqlite
LuaSQL is a simple interface from Lua to a DBMS. This package provides access
to SQLite databases.


%package mysql
Summary:        MySQL database connectivity for the Lua programming language
Group:          Development/Other
Requires:       lua >= %{luaver}
%description mysql
LuaSQL is a simple interface from Lua to a DBMS. This package provides access
to MySQL databases.


%package postgresql
Summary:        PostgreSQL database connectivity for the Lua programming language
Group:          Development/Other
Requires:       lua >= %{luaver}
%description postgresql
LuaSQL is a simple interface from Lua to a DBMS. This package provides access
to PostgreSQL databases.


%prep
%setup -q -n %{oname}-%{version}


%build
%make_build DRIVER_INCS="`pkg-config --cflags sqlite3`" DRIVER_LIBS="`pkg-config --libs sqlite3`" DEFS="%{optflags}" sqlite3
%make_build DRIVER_INCS="" DRIVER_LIBS="-lpq" DEFS="%{optflags}" WARN= postgres
%make_build DRIVER_INCS="-I%{_prefix}/include/mysql -I%{_prefix}/include/mysql/server" DRIVER_LIBS="-L%{_libdir}/mysql -lmysqlclient" DEFS="%{optflags}" mysql


%install
rm -rf $RPM_BUILD_ROOT
%make_install PREFIX=%{buildroot}%{_prefix} LUA_LIBDIR=%{buildroot}%{lualibdir} LUA_DIR=%{buildroot}%{luapkgdir}


%clean
rm -rf $RPM_BUILD_ROOT


%files

%files doc
%defattr(-,root,root,-)
%doc README
%doc doc/us/*

%files sqlite
%defattr(-,root,root,-)
%dir %{lualibdir}/luasql
%{lualibdir}/luasql/sqlite3.so

%files mysql
%defattr(-,root,root,-)
%dir %{lualibdir}/luasql
%{lualibdir}/luasql/mysql.so

%files postgresql
%defattr(-,root,root,-)
%dir %{lualibdir}/luasql
%{lualibdir}/luasql/postgres.so


%changelog
* Thu Mar 17 2011 Oden Eriksson <oeriksson@mandriva.com> 2.1.1-7mdv2011.0
+ Revision: 645827
- relink against libmysqlclient.so.18

* Sat Jan 01 2011 Oden Eriksson <oeriksson@mandriva.com> 2.1.1-6mdv2011.0
+ Revision: 627256
- rebuilt against mysql-5.5.8 libs, again

* Thu Dec 30 2010 Oden Eriksson <oeriksson@mandriva.com> 2.1.1-5mdv2011.0
+ Revision: 626538
- rebuilt against mysql-5.5.8 libs

* Wed Dec 08 2010 Rémy Clouard <shikamaru@mandriva.org> 2.1.1-3mdv2011.0
+ Revision: 616184
- rebuild for the mass rebuild

* Mon Sep 14 2009 Thierry Vignaud <tv@mandriva.org> 2.1.1-2mdv2010.0
+ Revision: 439656
- rebuild

* Mon Dec 29 2008 Jérôme Soyer <saispo@mandriva.org> 2.1.1-1mdv2009.1
+ Revision: 320764
- Fix RPM Group
- Fix BR
- SPEC Cleanup
- import lua-sql


