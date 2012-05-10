Name:           tucnak2
Version:        2.48
Release:        1
Summary:        VHF contest logging program
Group:          Communications 
License:        GPLv2+
URL:            http://tucnak.nagano.cz/wiki/Main_Page
Source0:        http://tucnak.nagano.cz/%{name}-%{version}.tar.gz
Patch0:         missing_ftdi_header.patch
Patch1:         include_dir_ftdi-2.48.patch

BuildRequires:  SDL-devel, glib2-devel, libpng-devel, pkgconfig(sndfile)
BuildRequires:  gpm-devel, alsa-oss-devel, hamlib-devel, libusb-devel
BuildRequires:  desktop-file-utils,fftw-devel, automake pkgconfig(libftdi)
BuildRequires:  pkgconfig(libftdi)

%description
Tucnak2 is VHF/UHF/SHF log for hamradio contests. It supports multi
bands, free input, networking, voice and CW keyer, WWL database and
much more.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
sed -i -e "s/Encoding=UTF-8//g" -e "s/Categories=HamRadio/Categories=Network;HamRadio;/g" share/applications/%{name}.desktop

#all files must be UTF-8
recode()
{
        iconv -f "$2" -t utf-8 < "$1" > "${1}_"
        touch -r "$1" "${1}_"
        mv -f "${1}_" "$1"

}
recode TODO iso-8859-15

%build
autoreconf -fiv
%configure2_5x --with-sdl
make


%install
%makeinstall_std

chmod +x %{buildroot}%{_datadir}/%{name}/tac2tuc.pl
desktop-file-install \
        --dir %{buildroot}/%{_datadir}/applications   \
        %{buildroot}/%{_datadir}/applications/%{name}.desktop


%files
%doc AUTHORS ChangeLog COPYING README TODO
%doc doc/NAVOD.pdf doc/NAVOD.sxw
%doc data/*.html data/*.png
%{_bindir}/*
%{_datadir}/applications/*
%{_datadir}/pixmaps/*
%{_datadir}/%{name}
