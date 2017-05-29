Name:		pure-ftpd
Version:	1.0.46
Release:	1
Summary:	pure-ftpd server

License:	GPL
URL:		https://www.pureftpd.org
Source0:	ftp://ftp.pureftpd.org/pub/pure-ftpd/releases/pure-ftpd-1.0.46.tar.gz
Source1:	pure-ftpd

%description
https://www.pureftpd.org

%pre
useradd ftpuser
echo "ftpuser" | passwd ftpuser --stdin

%post
chkconfig --add pure-ftpd
/etc/init.d/pure-ftpd start

%preun
/etc/init.d/pure-ftpd stop

%postun
userdel ftpuser

%prep
%setup -q -n %{name}-%{version}

%build
%configure
make

%install
%make_install
mkdir $RPM_BUILD_ROOT/etc/init.d
install -m 755 %{SOURCE1} $RPM_BUILD_ROOT/etc/init.d/pure-ftpd


%files
/etc/pure-ftpd.conf
/usr/bin/pure-pw
/usr/bin/pure-pwconvert
/usr/bin/pure-statsdecode
/usr/sbin/pure-authd
/usr/sbin/pure-ftpd
/usr/sbin/pure-ftpwho
/usr/sbin/pure-mrtginfo
/usr/sbin/pure-quotacheck
/usr/sbin/pure-uploadscript
/usr/share/man/man8/pure-authd.8.gz
/usr/share/man/man8/pure-ftpd.8.gz
/usr/share/man/man8/pure-ftpwho.8.gz
/usr/share/man/man8/pure-mrtginfo.8.gz
/usr/share/man/man8/pure-pw.8.gz
/usr/share/man/man8/pure-pwconvert.8.gz
/usr/share/man/man8/pure-quotacheck.8.gz
/usr/share/man/man8/pure-statsdecode.8.gz
/usr/share/man/man8/pure-uploadscript.8.gz
/etc/init.d/pure-ftpd

