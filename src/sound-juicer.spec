Name:		sound-juicer
Summary:	Clean and lean CD ripper
Version:	2.28.1
Release:	1
License:	GPL
Group:		Applications/Multimedia
Source:		%{name}-%{version}.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-%{version}-root
Requires:	libmusicbrainz >= 2.0.1
Requires:	libgnomeui >= 2.0.0
Requires:	glib2 >= 2.0.0
Requires:	gstreamer >= 0.8.0
Requires:	GConf2 >= 2.0.0
Requires:	gstreamer-plugins-base >= 0.7.2
BuildRequires:	libmusicbrainz-devel >= 2.0.1
BuildRequires:	libgnomeui-devel >= 2.0.0
BuildRequires:	glib2-devel >= 2.0.0
BuildRequires:	gstreamer-devel >= 0.8.0
BuildRequires:	GConf2-devel >= 2.0.0
BuildRequires:  scrollkeeper >= 0.3.5

%description
GStreamer-based CD ripping tool. Saves audio CDs to Ogg Vorbis or FLAC.

%prep
%setup -q

%build

%configure

make

export GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1;
%makeinstall
unset GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL

# Clean out bad files
rm -rf $RPM_BUILD_ROOT%{_localstatedir}/scrollkeeper
# the icon-theme.cache should be in the icon-theme package
rm -rf $RPM_BUILD_ROOT/usr/share/icons/hicolor/icon-theme.cache

%find_lang sound-juicer

%clean
[ -n "$RPM_BUILD_ROOT" -a "$RPM_BUILD_ROOT" != / ] && rm -rf $RPM_BUILD_ROOT

%preun
export GCONF_CONFIG_SOURCE=`gconftool-2 --get-default-source` 
gconftool-2 --makefile-uninstall-rule %{_sysconfdir}/gconf/schemas/sound-juicer.schemas > /dev/null

%post
export GCONF_CONFIG_SOURCE=`gconftool-2 --get-default-source` 
gconftool-2 --makefile-install-rule %{_sysconfdir}/gconf/schemas/sound-juicer.schemas > /dev/null

%files -f sound-juicer.lang
%defattr(-, root, root)
%doc AUTHORS COPYING ChangeLog INSTALL README NEWS
%{_bindir}/sound-juicer
%{_sysconfdir}/gconf/schemas/sound-juicer.schemas
%{_datadir}/sound-juicer
%{_datadir}/applications/sound-juicer.desktop
%{_datadir}/icons/hicolor/16x16
%{_datadir}/icons/hicolor/22x22
%{_datadir}/icons/hicolor/24x24
%{_datadir}/icons/hicolor/32x32
%{_datadir}/icons/hicolor/48x48
%{_datadir}/icons/hicolor/scalable
%{_datadir}/gnome/help
%{_datadir}/omf
%{_datadir}/man/man1

%changelog
* Wed Jan 30 2008 Phil Long <plong@mitre.org>
- change .tar.gz to .tar.bz2
- fix the icons - remove /pixmaps/sound-juicer.png, add the new gnome 2.20 ones
- add the man file

* Sun Feb 29 2004 Christian Schaller <Uraeus@gnome.org>
- Add versioning to gstreamer req

* Fri Sep 27 2003 Christian Schaller <Uraeus@gnome.org>
- Replace req of gst-cdpara with gst-plugins as we now use standard RH packaging

* Tue Aug 26 2003 Christian Schaller <Uraeus@gnome.org>
- Add docs

* Wed Jul 09 2003 Christian Schaller <Uraeus@gnome.org>
- Update for latest CVS

* Tue Apr 22 2003 Frederic Crozat <fcrozat@mandrakesoft.com>
- Use more macros

* Sun Apr 20 2003 Ronald Bultje <rbultje@ronald.bitfreak.net>
- Make spec file for sound-juicer (based on netRB spec file)
