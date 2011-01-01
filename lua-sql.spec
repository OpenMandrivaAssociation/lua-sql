%define luaver 5.1
%define lualibdir %{_libdir}/lua/%{luaver}
%define luapkgdir %{_datadir}/lua/%{luaver}
%define oname luasql

Name:           lua-sql
Version:        2.1.1
Release:        %mkrel 6
Summary:        Database connectivity for the Lua programming language

Group:          Development/Other
License:        MIT
URL:            http://www.keplerproject.org/luasql/
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
make DRIVER_INCS="`pkg-config --cflags sqlite3`" DRIVER_LIBS="`pkg-config --libs sqlite3`" T=sqlite3 DEFS="%{optflags} -fPIC"
make DRIVER_INCS="" DRIVER_LIBS="-lpq" T=postgres DEFS="%{optflags} -fPIC" WARN=
make DRIVER_INCS="-I%{_prefix}/include/mysql" DRIVER_LIBS="-L%{_libdir}/mysql -lmysqlclient" T=mysql DEFS="%{optflags} -fPIC"


%install
rm -rf $RPM_BUILD_ROOT
make install PREFIX=$RPM_BUILD_ROOT%{_prefix} LUA_LIBDIR=$RPM_BUILD_ROOT%{lualibdir} LUA_DIR=$RPM_BUILD_ROOT%{luapkgdir} T=sqlite3
make install PREFIX=$RPM_BUILD_ROOT%{_prefix} LUA_LIBDIR=$RPM_BUILD_ROOT%{lualibdir} LUA_DIR=$RPM_BUILD_ROOT%{luapkgdir} T=postgres
make install PREFIX=$RPM_BUILD_ROOT%{_prefix} LUA_LIBDIR=$RPM_BUILD_ROOT%{lualibdir} LUA_DIR=$RPM_BUILD_ROOT%{luapkgdir} T=mysql


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
