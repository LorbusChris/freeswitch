Name:		freeswitch
Summary:	FreeSWITCH open source telephony platform
License:	MPL1.1
Version:	1.10.2
Release:	1%{?dist}
URL:		http://www.freeswitch.org/
Source0:	https://github.com/signalwire/freeswitch/archive/v%{version}.tar.gz
Source1:	modules.conf.fedora

# TODO(lorbus)
# Add bundled Provides
BuildRequires: alsa-lib-devel
BuildRequires: apr-devel
BuildRequires: apr-util-devel
BuildRequires: autoconf
BuildRequires: autoconf-archive
BuildRequires: automake
BuildRequires: bison
BuildRequires: codec2-devel
BuildRequires: curl-devel
BuildRequires: db4-devel
BuildRequires: e2fsprogs-devel
BuildRequires: gcc-c++
BuildRequires: gdbm-devel
BuildRequires: gnutls-devel
BuildRequires: hiredis-devel
BuildRequires: ImageMagick-devel
BuildRequires: ladspa-devel
BuildRequires: ldns-devel
BuildRequires: libjpeg-devel
BuildRequires: libmemcached-devel
BuildRequires: libogg-devel
BuildRequires: librabbitmq-devel
BuildRequires: libsndfile-devel
BuildRequires: libsrtp-devel
BuildRequires: libtheora-devel
BuildRequires: libtiff-devel
BuildRequires: libtool >= 1.5.17
BuildRequires: libvpx-devel
BuildRequires: libvorbis-devel
BuildRequires: libxml2-devel
BuildRequires: libyaml-devel
BuildRequires: lua-devel
BuildRequires: ncurses-devel
BuildRequires: net-snmp-devel
BuildRequires: openssl-devel >= 1.0.1e
BuildRequires: opus-devel
BuildRequires: pcre-devel 
BuildRequires: perl
BuildRequires: perl-ExtUtils-Embed
BuildRequires: pkgconfig
BuildRequires: portaudio-devel
BuildRequires: python
BuildRequires: python-devel
BuildRequires: redis-devel
BuildRequires: sofia-sip-devel
BuildRequires: soundtouch-devel >= 1.7.1
BuildRequires: spandsp-devel
BuildRequires: speex-devel
BuildRequires: speexdsp-devel
BuildRequires: sqlite-devel
BuildRequires: unixODBC-devel
BuildRequires: which
BuildRequires: yasm
BuildRequires: zlib-devel
Requires: alsa-lib
Requires: libogg
Requires: libvorbis
Requires: curl
Requires: ncurses
Requires: pcre
Requires: speex
Requires: speexdsp
Requires: sqlite
Requires: libtiff
Requires: openssl >= 1.0.1e
Requires: unixODBC
Requires: libjpeg
Requires: db4
Requires: gdbm
Requires: zlib
Requires: libtiff
Requires: libtheora
Requires: libxml2
Requires: libsndfile

%description
FreeSWITCH is an open source telephony platform designed to facilitate the creation of voice 
and chat driven products scaling from a soft-phone up to a soft-switch.  It can be used as a 
simple switching engine, a media gateway or a media server to host IVR applications using 
simple scripts or XML to control the callflow. 

We support various communication technologies such as SIP, H.323 and GoogleTalk making 
it easy to interface with other open source PBX systems such as sipX, OpenPBX, Bayonne, YATE or Asterisk.

We also support both wide and narrow band codecs making it an ideal solution to bridge legacy 
devices to the future. The voice channels and the conference bridge module all can operate 
at 8, 16 or 32 kilohertz and can bridge channels of different rates.

FreeSWITCH runs on several operating systems including Windows, Max OS X, Linux, BSD and Solaris 
on both 32 and 64 bit platforms.

Our developers are heavily involved in open source and have donated code and other resources to 
other telephony projects including sipXecs, OpenSER, Asterisk, CodeWeaver and OpenPBX.


%package devel
Summary:  Development package for FreeSWITCH open source telephony platform
Requires: %{name} = %{version}-%{release}

%description devel
FreeSWITCH development files


# Application Modules
%package application-abstraction
Summary:  FreeSWITCH mod_abstraction
Requires: %{name} = %{version}-%{release}

%description application-abstraction
Provide an abstraction to FreeSWITCH API calls

%package application-bert
Summary:  FreeSWITCH bert module
Requires: %{name} = %{version}-%{release}

%description application-bert
Provides an application that generates and captures a milliwatt tone
and prints an error rate at the end. It also provides ESL events that
can be used to load-test equipment and detect if there are audio gaps
in some of the sessions. It only works with the PCMU codec.

%package application-blacklist
Summary:  FreeSWITCH blacklist module
Requires: %{name} = %{version}-%{release}

%description application-blacklist
Provide black/white listing of various fields used for routing calls in 
FreeSWITCH

%package application-callcenter
Summary:  FreeSWITCH mod_callcenter Call Queuing Application
Requires: %{name} = %{version}-%{release}

%description application-callcenter
Provide Automated Call Distribution capabilities for FreeSWITCH

%package application-cidlookup
Summary:  FreeSWITCH mod_cidlookup 
Requires: %{name} = %{version}-%{release}

%description application-cidlookup
Provide FreeSWITCH access to third party CallerID Name Databases via HTTP

%package application-commands
Summary:  FreeSWITCH mod_commands
Requires: %{name} = %{version}-%{release}

%description application-commands
mod_commands processes the FreeSWITCH API commands.

%package application-curl
Summary:  FreeSWITCH mod_curl
Requires: %{name} = %{version}-%{release}

%description application-curl
Provide FreeSWITCH dialplan access to CURL

%package application-db
Summary:  FreeSWITCH mod_db
Requires: %{name} = %{version}-%{release}

%description application-db
mod_db implements an API and dialplan interface to a database backend for 
FreeSWITCH.  The database can either be in sqlite or ODBC.  It also provides 
support for group dialing and provides database backed limit interface. 

%package application-directory
Summary:  FreeSWITCH mod_directory
Requires: %{name} = %{version}-%{release}

%description application-directory
Provides FreeSWITCH mod_directory, a dial by name directory application. 

%package application-distributor
Summary:  FreeSWITCH mod_distributor
Requires: %{name} = %{version}-%{release}

%description application-distributor
Provides FreeSWITCH mod_distributor, a simple round-robbin style distribution 
to call gateways.

%package application-dptools
Summary:  FreeSWITCH mod_dptools
Requires: %{name} = %{version}-%{release}

%description application-dptools
FreeSWITCH Dialplan tools to provide the apps (commands)
to process call sessions in XML dialplans.


%package application-easyroute
Summary:  FreeSWITCH mod_easyroute
Requires: %{name} = %{version}-%{release}

%description application-easyroute
Provides FreeSWITCH mod_easyroute, a simple, easy to use DB Backed DID routing 
Engine. Uses ODBC to connect to the DB of your choice.

%package application-enum
Summary:  FreeSWITCH mod_enum
Requires: %{name} = %{version}-%{release}

%description application-enum
Provides FreeSWITCH mod_enum, a ENUM dialplan, with API and Dialplan extensions 
supporting ENUM lookups.

%package application-esf
Summary:  FreeSWITCH mod_esf
Requires: %{name} = %{version}-%{release}

%description application-esf
Provides FreeSWITCH mod_esf, Extra Sip Functionality such as Multicast Support

%package application-expr
Summary:  FreeSWITCH mod_expr
Requires: %{name} = %{version}-%{release}

%description application-expr
Provides FreeSWITCH mod_expr, implements Brian Allen Vanderburg's ExprEval 
expression evaluation library for FreeSWITCH.

%package application-fifo
Summary:  FreeSWITCH mod_fifo
Requires: %{name} = %{version}-%{release}

%description application-fifo
Provides FreeSWITCH mod_fifo, a parking-like app which allows you to make 
custom call queues

%package application-fsk
Summary:  FreeSWITCH mod_fsk
Requires: %{name} = %{version}-%{release}

%description application-fsk
Provides FreeSWITCH mod_fsk, a module to send and receive information via 
Frequency-shift keying

%package application-fsv
Summary:  FreeSWITCH mod_fsv
Requires: %{name} = %{version}-%{release}

%description application-fsv
Provides FreeSWITCH mod_fsk, implements functions to record and play back video

%package application-hash
Summary:  FreeSWITCH mod_hash
Requires: %{name} = %{version}-%{release}

%description application-hash
Provides FreeSWITCH mod_hash, implements an API and application interface for 
manipulating a hash table. It also provides a limit backend.

%package application-hiredis
Summary:  FreeSWITCH mod_hiredis
Requires: %{name} = %{version}-%{release}

%description application-hiredis
Provides FreeSWITCH mod_hiredis which implements an interface for running
basic redis commands on configured servers and also deprecated old
mod_redis implementing the limit backend.

%package application-httapi
Summary:  FreeSWITCH mod_httapi
Requires: %{name} = %{version}-%{release}

%description application-httapi
Provides FreeSWITCH mod_httapi, provides an HTTP based Telephony API using a 
standard FreeSWITCH application interface as well as a cached http file format 
interface

%package application-http-cache
Summary:  FreeSWITCH mod_http_cache
Requires: %{name} = %{version}-%{release}

%description application-http-cache
Provides FreeSWITCH mod_http_cache, allows one to make a HTTP GET request to 
cache a document. The primary use case is to download and cache audio files 
from a web server. 

%package application-ladspa
Summary:  FreeSWITCH mod_ladspa
Requires: %{name} = %{version}-%{release}

%description application-ladspa
Provides FreeSWITCH mod_ladspa, a module that allows to use Linux
Audio Developer's Simple Plugin API inside freeswitch in realtime.

%package application-lcr
Summary:  FreeSWITCH mod_lcr
Requires: %{name} = %{version}-%{release}

%description application-lcr
Provides FreeSWITCH mod_lcr, provide basic Least Cost Routing Services

%package application-memcache
Summary:  FreeSWITCH mod_memcache
Requires: %{name} = %{version}-%{release}

%description application-memcache
Provides FreeSWITCH mod_memcache, implements an API interface to memcached which
is a "high-performance, distributed memory object caching system, generic in 
nature, but intended for use in speeding up dynamic web applications by 
alleviating database load." 

%package application-nibblebill
Summary:  FreeSWITCH mod_nibblebill
Requires: %{name} = %{version}-%{release}

%description application-nibblebill
Provides FreeSWITCH mod_nibblebill, provides a credit/debit module for 
FreeSWITCH to allow real-time debiting of credit or cash from a database 
while calls are in progress.

%package application-oreka
Summary:  FreeSWITCH mod_oreka
Requires: %{name} = %{version}-%{release}

%description application-oreka
Provides FreeSWITCH mod_oreka, a module for media recording with Oreka

%package application-prefix
Summary:  FreeSWITCH mod_prefix
Requires: %{name} = %{version}-%{release}

%description application-prefix
Provides mod_prefix, longest-prefix match in-memory data store
for FreeSWITCH

%package application-redis
Summary:  FreeSWITCH mod_redis
Requires: %{name} = %{version}-%{release}

%description application-redis
Provides FreeSWITCH mod_redis, access to the redis key value pair db system from
FreeSWITCH

%package application-rss
Summary:  FreeSWITCH mod_rss
Requires: %{name} = %{version}-%{release}

%description application-rss
Provides FreeSWITCH mod_rss, edisrse and read an XML based RSS feed, then read
the entries aloud via a TTS engine

%package application-sms
Summary:  FreeSWITCH mod_sms
Requires: %{name} = %{version}-%{release}

%description application-sms
Provides FreeSWITCH mod_sms, provide a way to route messages in freeswitch, 
potentially allowing one to build a powerful chatting system like in XMPP using 
using SIP SIMPLE on SIP clients

%package application-snapshot
Summary:  FreeSWITCH mod_snapshot
Requires: %{name} = %{version}-%{release}

%description application-snapshot
Provides FreeSWITCH mod_snapshot, allows recording a sliding window of audio 
and taking snapshots to disk. 

%package application-sonar
Summary:  FreeSWITCH mod_sonar
Requires: %{name} = %{version}-%{release}

%description application-sonar
Provides FreeSWITCH mod_sonar which allows to ping a remote server with a tone
and wait for the echo back to check for possible network problems.

%package application-soundtouch
Summary:  FreeSWITCH mod_soundtouch
Requires: %{name} = %{version}-%{release}

%description application-soundtouch
Provides FreeSWITCH mod_soundtouch, uses the soundtouch library, which can do
pitch shifting and other audio effects, so you can pipe the audio of a call
(or any other channel audio) through this module and achieve those effects. You
can specifically adjust pitch, rate, and tempo.

%package application-spandsp
Summary:  FreeSWITCH mod_spandsp
Requires: %{name} = %{version}-%{release}

%description application-spandsp
Provides FreeSWITCH mod_spandsp. The family of modules including mod_fax,
mod_t38gateway, and the mod_voipcodecs have now been merged into one
module called mod_spandsp which takes advantage of all the DSP features
found in the spandsp library including T.38 endpoint and gateway
functionality.

%package application-spy
Summary:  FreeSWITCH mod_spy
Requires: %{name} = %{version}-%{release}

%description application-spy
Provides FreeSWITCH mod_spy, implements userspy application which provides 
persistent eavesdrop on all channels bridged to a certain user

%package application-stress
Summary:  FreeSWITCH mod_stress
Requires: %{name} = %{version}-%{release}

%description application-stress
Provides FreeSWITCH mod_stress. mod_stress attempts to detect stress in a 
person's voice and generates FreeSWITCH events based on that data. 

%package application-translate
Summary:  FreeSWITCH mod_translate
Requires: %{name} = %{version}-%{release}

%description application-translate
Provide an number translation to FreeSWITCH API calls

%package application-valet_parking
Summary:  FreeSWITCH mod_valet_parking
Requires: %{name} = %{version}-%{release}

%description application-valet_parking
Provides FreeSWITCH mod_valet_parking. Provides 'Call Parking' in the switch
as opposed to on the phone and allows for a number of options to handle call
retrieval

%package application-video_filter
Summary:  FreeSWITCH video filter bugs
Requires: %{name} = %{version}-%{release}

%description application-video_filter
Provide a chromakey video filter media bug

%package application-vmd
Summary:  FreeSWITCH mod_vmd
Requires: %{name} = %{version}-%{release}

%description application-vmd
VMD stands for "Voice Mail Detection" and mod_vmd is designed to detect the beep
sound at the end of voicemail or answering machine greetings. This is useful in
cases where you wish to leave a recorded message on the recipient's message
system but don't want to have the pregnant pause that is common when using
wait_for_silence.

%package application-voicemail
Summary:  FreeSWITCH mod_voicemail
Requires: %{name} = %{version}-%{release}

%description application-voicemail
Provides FreeSWITCH mod_voicemail. Implements Voicemail Application 

%package application-voicemail-ivr
Summary:  FreeSWITCH mod_voicemail_ivr
Requires: %{name} = %{version}-%{release}

%description application-voicemail-ivr
Provides FreeSWITCH mod_voicemail_ivr. Provides a custimizable audio navigation 
system for backend voicemail systems


# ASR TTS Modules
%package asrtts-tts-commandline
Summary:  FreeSWITCH mod_tts_commandline
Requires: %{name} = %{version}-%{release}

%description asrtts-tts-commandline
Provides FreeSWITCH mod_tts_commandline, Run a command line and play the 
output file.

%package asrtts-unimrcp
Summary:  FreeSWITCH mod_unimrcp
Requires: %{name} = %{version}-%{release}

%description asrtts-unimrcp
Provides FreeSWITCH mod_unimrcp, allows communication with Media Resource 
Control Protocol (MRCP) servers


# Codec Modules
%package codec-passthru-amr
Summary:   Pass-through AMR Codec support for FreeSWITCH open source telephony platform
Requires:  %{name} = %{version}-%{release}
Conflicts: codec-amr

%description codec-passthru-amr
Pass-through AMR Codec support for FreeSWITCH open source telephony platform

%package codec-passthru-amrwb
Summary:   Pass-through AMR WideBand Codec support for FreeSWITCH open source telephony platform
Requires:  %{name} = %{version}-%{release}
Conflicts: codec-amrwb

%description codec-passthru-amrwb
Pass-through AMR WideBand Codec support for FreeSWITCH open source telephony platform

%package codec-codec2
Summary:  Codec2 Narrow Band Codec support for FreeSWITCH open source telephony platform
Requires: %{name} = %{version}-%{release}

%description codec-codec2
CODEC2 narrow band codec support for FreeSWITCH open source telephony platform.
CODEC2 was created by the developers of Speex.

%package codec-dahdi
Summary:  DAHDI codec support for FreeSWITCH open source telephony platform.
Requires: %{name} = %{version}-%{release}

%description codec-dahdi
%{summary}.

%package codec-passthru-g723_1
Summary:   Pass-through g723.1 Codec support for FreeSWITCH open source telephony platform
Requires:  %{name} = %{version}-%{release}
Conflicts: codec-g723_1

%description codec-passthru-g723_1
Pass-through g723.1 Codec support for FreeSWITCH open source telephony platform

%package codec-h26x
Summary:  H.263/H.264 Video Codec support for FreeSWITCH open source telephony platform
Requires: %{name} = %{version}-%{release}

%description codec-h26x
H.263/H.264 Video Codec support for FreeSWITCH open source telephony platform

%package codec-isac
Summary:  iSAC Codec support for FreeSWITCH open source telephony platform
Requires: %{name} = %{version}-%{release}

%description codec-isac
iSAC Codec support for FreeSWITCH open source telephony platform

%package codec-mp4v
Summary:  MP4V Video Codec support for FreeSWITCH open source telephony platform
Requires: %{name} = %{version}-%{release}

%description codec-mp4v
MP4V Video Codec support for FreeSWITCH open source telephony platform

%package codec-opus
Summary:  Opus Codec support for FreeSWITCH open source telephony platform
Requires: %{name} = %{version}-%{release}

%description codec-opus
OPUS Codec support for FreeSWITCH open source telephony platform

%package codec-theora
Summary:  Theora Video Codec support for FreeSWITCH open source telephony platform
Requires: %{name} = %{version}-%{release}

%description codec-theora
Theora Video Codec support for FreeSWITCH open source telephony platform.


# Database Modules
%package database-mariadb
Summary:       MariaDB native support for FreeSWITCH
Requires:      %{name} = %{version}-%{release}
Requires:      mariadb-connector-c
BuildRequires: mariadb-connector-c-devel

%description database-mariadb
MariaDB native support for FreeSWITCH.

%package database-pgsql
Summary:       PostgreSQL native support for FreeSWITCH
Requires:      %{name} = %{version}-%{release}
Requires:      postgresql-libs
BuildRequires: postgresql-devel

%description database-pgsql
PostgreSQL native support for FreeSWITCH.


# Dialplan Modules
%package dialplan-directory
Summary:       FreeSWITCH dialplan directory module
Requires:      %{name} = %{version}-%{release}

%description dialplan-directory
%{summary}.

%package dialplan-xml
Summary:       FreeSWITCH dialplan XML module
Requires:      %{name} = %{version}-%{release}

%description dialplan-xml
%{summary}.


# Endpoint Modules
%package endpoint-alsa
Summary:       Alsa endpoint support for FreeSWITCH open source telephony platform
Requires:      %{name} = %{version}-%{release}

%description endpoint-alsa
Alsa endpoint support for FreeSWITCH open source telephony platform.

%package endpoint-dingaling
Summary:       Dingaling endpoint support for FreeSWITCH open source telephony platform
Requires:      %{name} = %{version}-%{release}

%description endpoint-dingaling
mod_dingaling is a generic xmpp registration that can be used for
Google talk or any other XMPP integration.

%package endpoint-loopback
Summary:       Loopback endpoint support for FreeSWITCH open source telephony platform
Requires:      %{name} = %{version}-%{release}

%description endpoint-loopback
The Loopback special channel emulates an endpoint to route a call back
into the start of the specified dialplan.

%package endpoint-portaudio
Summary:       PortAudio endpoint support for FreeSWITCH open source telephony platform
Requires:      %{name} = %{version}-%{release}

%description endpoint-portaudio
PortAudio endpoint support for FreeSWITCH open source telephony platform.

%package endpoint-rtc
Summary:  RTC Endpoint support for FreeSWITCH open source telephony platform
Requires: %{name} = %{version}-%{release}

%description endpoint-rtc
mod_rtc supports media streaming used by WebRTC and mod_verto

%package endpoint-rtmp
Summary:  RTPM Endpoint support for FreeSWITCH open source telephony platform
Requires: %{name} = %{version}-%{release}

%description endpoint-rtmp
RTMP Endpoint support for FreeSWITCH open source telephony platform. Allows FreeSWITCH
to be used from a RTMP client. See http://wiki.freeswitch.org/wiki/Mod_rtmp#Flex_Client
for the OpenSouce FreeSWITCH backed Client.

%package endpoint-sofia
Summary:  Sofia endpoint support for FreeSWITCH open source telephony platform
Requires: %{name} = %{version}-%{release}

%description endpoint-sofia
mod_sofia is the SIP endpoint implemented by FreeSWITCH.

%package endpoint-verto
Summary:  Verto endpoint support for FreeSWITCH open source telephony platform
Requires: %{name} = %{version}-%{release}

%description endpoint-verto
Verto protocol support for FreeSWITCH open source telephony platform.


# Event Handler Modules
%package event-amqp
Summary:       AMQP support for the FreeSWITCH open source telephony platform
Requires:      %{name} = %{version}-%{release}

%description event-amqp
mod_amqp gives FreeSWITCH the ability to send events through an AMQP server
like RabbitMQ and listen for api commands.

%package event-cdr-csv
Summary:       Call Details Records Logger using text generation templates for the FreeSWITCH open source telephony platform
Requires:      %{name} = %{version}-%{release}

%description event-cdr-csv
Call Details Records Logger using text generation templates for FreeSWITCH.

%package event-cdr-pg-csv
Summary:       PostgreSQL Call Details Records Logger for the FreeSWITCH open source telephony platform
Requires:      %{name} = %{version}-%{release}
Requires:      postgresql-libs
BuildRequires: postgresql-devel

%description event-cdr-pg-csv
PostgreSQL Call Details Records Logger for FreeSWITCH.

%package event-cdr-sqlite
Summary:  SQLite CDR Logger for the FreeSWITCH open source telephony platform
Requires: %{name} = %{version}-%{release}

%description event-cdr-sqlite
SQLite CDR Logger for FreeSWITCH.

%package event-multicast
Summary:       Multicast Event System for the FreeSWITCH open source telephony platform
Requires:      %{name} = %{version}-%{release}

%description event-multicast
mod_event_multicast sends FreeSWITCH events from the machine via multicast to a
configurable address/port combination. Other hosts can be configured to listen
for these events and parse them, potentially also triggering events to happen on
those hosts.

%package event-socket
Summary:       Socket Module for the FreeSWITCH open source telephony platform
Requires:      %{name} = %{version}-%{release}

%description event-socket
mod_event_socket is a TCP-based interface to control FreeSWITCH, and it operates in two modes,
inbound and outbound. (These terms are relative to FreeSWITCH).

%package event-format-cdr
Summary:  JSON and XML Logger for the FreeSWITCH open source telephony platform
Requires: %{name} = %{version}-%{release}

%description event-format-cdr
JSON and XML Logger for the FreeSWITCH open source telephony platform

%package event-json-cdr
Summary:  JSON CDR Logger for the FreeSWITCH open source telephony platform
Requires: %{name} = %{version}-%{release}

%description event-json-cdr
JSON CDR Logger for FreeSWITCH.

%package event-kazoo
Summary:       Kazoo Module for the FreeSWITCH open source telephony platform
Requires:      %{name} = %{version}-%{release}
Requires:      erlang
BuildRequires: erlang

%description event-kazoo
Kazoo Module for FreeSWITCH.

%package event-odbc-cdr
Summary:  ODBC CDR Logger for the FreeSWITCH open source telephony platform
Requires: %{name} = %{version}-%{release}

%description event-odbc-cdr
Insert channel variables directly into database after call ends.


# Media Format Modules
%package format-imagick
Summary:  ImageMagick support for the FreeSWITCH open source telephony platform
Requires: %{name} = %{version}-%{release}

%description format-imagick
%{summary}.

%package format-local-stream
Summary:  Local File Streamer for the FreeSWITCH open source telephony platform
Requires: %{name} = %{version}-%{release}

%description format-local-stream
Local File Streamer for FreeSWITCH. It streams files from a directory and 
multiple channels connected to the same stream will hear the same (looped) 
file playback .. similar to a shoutcast stream. Useful for Music-on-hold type 
scenarios. 

%package format-native-file
Summary:  Native Media File support for the FreeSWITCH open source telephony platform
Requires: %{name} = %{version}-%{release}

%description format-native-file
The native file module is designed to make it easy to play sound files where no
transcoding is necessary. The default FreeSWITCH sound files are in wav format.
Generally, these require transcoding when being played to callers. However, if
a native format sound file is available then FreeSWITCH can use it. 

%package format-png
Summary:  PNG file support for the FreeSWITCH open source telephony platform
Requires: %{name} = %{version}-%{release}

%description format-png
%{summary}.

%package format-portaudio-stream
Summary:  PortAudio Media Steam support for the FreeSWITCH open source telephony platform
Requires: %{name} = %{version}-%{release}

%description format-portaudio-stream
Portaudio Streaming interface Audio for FreeSWITCH

%package format-shell-stream
Summary:  Implements Media Steaming from arbitrary shell commands for the FreeSWITCH open source telephony platform
Requires: %{name} = %{version}-%{release}

%description format-shell-stream
Mod shell stream is a FreeSWITCH module to allow you to stream audio from an 
arbitrary shell command. You could use it to read audio from a database, from 
a soundcard, etc. 

%package format-shout
Summary:       Implements Media Steaming from arbitrary shell commands for the FreeSWITCH open source telephony platform
Requires:      %{name} = %{version}-%{release}
Requires:      libshout >= 2.2.2
Requires:      libmpg123 >= 1.20.1
Requires:      lame
BuildRequires: libshout-devel >= 2.2.2
BuildRequires: libmpg123-devel >= 1.20.1
BuildRequires: lame-devel

%description format-shout
Mod Shout is a FreeSWITCH module to allow you to stream audio from MP3s or a i
shoutcast stream.

%package format-sndfile
Summary:  Sndfile support for the FreeSWITCH open source telephony platform
Requires: %{name} = %{version}-%{release}

%description format-sndfile
%{summary}.

%package format-tone-stream
Summary:  Implements TGML Tone Generation for the FreeSWITCH open source telephony platform
Requires: %{name} = %{version}-%{release}

%description format-tone-stream
%{summary}.


# Programming Language Modules
%package lua
Summary:  Lua support for the FreeSWITCH open source telephony platform
Requires: %{name} = %{version}-%{release}

%description lua
%{summary}.

%package perl
Summary:  Perl support for the FreeSWITCH open source telephony platform
Requires: %{name} = %{version}-%{release}
Requires: perl

%description perl
%{summary}.

%package yaml
Summary:  YAML support for the FreeSWITCH open source telephony platform
Requires: %{name} = %{version}-%{release}

%description yaml
%{summary}.


# Logger Modules
%package logger-console
Summary:  Console logger for FreeSWITCH
Requires: %{name} = %{version}-%{release}

%description logger-console
%{summary}.

%package logger-graylog2
Summary:  GELF logger for Graylog2 and Logstash
Requires: %{name} = %{version}-%{release}

%description logger-graylog2
GELF logger for Graylog2 and Logstash

%package logger-logfile
Summary:  Logfile logger for FreeSWITCH
Requires: %{name} = %{version}-%{release}

%description logger-logfile
%{summary}.

%package logger-syslog
Summary:  Syslog logger for FreeSWITCH
Requires: %{name} = %{version}-%{release}

%description logger-syslog
%{summary}.


# Say Modules
%package lang-de
Summary:  Provides German language dependend modules and speech config for the FreeSWITCH Open Source telephone platform.
Requires: %{name} = %{version}-%{release}

%description lang-de
German language phrases module and directory structure for say module and voicemail

%package lang-en
Summary:  Provides English language dependand modules and speech config for the FreeSWITCH Open Source telephone platform.
Requires: %{name} = %{version}-%{release}

%description lang-en
English language phrases module and directory structure for say module and voicemail

%package lang-es
Summary:  Provides Spanish language dependend modules and speech config for the FreeSWITCH Open Source telephone platform.
Requires: %{name} = %{version}-%{release}

%description lang-es
Spanish language phrases module and directory structure for say module and voicemail

%package lang-es-ar
Summary:  Provides Argentinian Spanish language dependend modules and speech config for the FreeSWITCH Open Source telephone platform.
Requires: %{name} = %{version}-%{release}

%description lang-es-ar
Argentinian Spanish language phrases module and directory structure for say module and voicemail

%package lang-fa
Summary:  Provides Farsi language dependend modules and speech config for the FreeSWITCH Open Source telephone platform.
Requires: %{name} = %{version}-%{release}

%description lang-fa
Farsi language phrases module and directory structure for say module and voicemail

%package lang-fr
Summary:  Provides French language dependend modules and speech config for the FreeSWITCH Open Source telephone platform.
Requires: %{name} = %{version}-%{release}

%description lang-fr
French language phrases module and directory structure for say module and voicemail

%package lang-he
Summary:  Provides Hebrew language dependend modules and speech config for the FreeSWITCH Open Source telephone platform.
Requires: %{name} = %{version}-%{release}

%description lang-he
Hebrew language phrases module and directory structure for say module and voicemail

%package lang-hr
Summary:  Provides Croatian language dependend modules and speech config for the FreeSWITCH Open Source telephone platform.
Requires: %{name} = %{version}-%{release}

%description lang-hr
Croatian language phrases module and directory structure for say module and voicemail

%package lang-hu
Summary:  Provides Hungarian language dependend modules and speech config for the FreeSWITCH Open Source telephone platform.
Requires: %{name} = %{version}-%{release}

%description lang-hu
Hungarian language phrases module and directory structure for say module and voicemail

%package lang-it
Summary:  Provides Italian language dependend modules and speech config for the FreeSWITCH Open Source telephone platform.
Requires: %{name} = %{version}-%{release}

%description lang-it
Italian language phrases module and directory structure for say module and voicemail

%package lang-ja
Summary:  Provides Japanese language dependend modules and speech config for the FreeSWITCH Open Source telephone platform.
Requires: %{name} = %{version}-%{release}

%description lang-ja
Japanese language phrases module and directory structure for say module and voicemail

%package lang-nl
Summary:  Provides Dutch language dependend modules and speech config for the FreeSWITCH Open Source telephone platform.
Requires: %{name} = %{version}-%{release}

%description lang-nl
Dutch language phrases module and directory structure for say module and voicemail

%package lang-pl
Summary:  Provides Polish language dependend modules and speech config for the FreeSWITCH Open Source telephone platform.
Requires: %{name} = %{version}-%{release}

%description lang-pl
Polish language phrases module and directory structure for say module and voicemail

%package lang-pt
Summary:  Provides Portugese language dependend modules and speech config for the FreeSWITCH Open Source telephone platform.
Requires: %{name} = %{version}-%{release}

%description lang-pt
Portugese language phrases module and directory structure for say module and voicemail

%package lang-ru
Summary:  Provides Russian language dependand modules and speech config for the FreeSWITCH Open Source telephone platform.
Requires: %{name} = %{version}-%{release}

%description lang-ru
Russian language phrases module and directory structure for say module and voicemail

%package lang-sv
Summary:  Provides Swedish language dependend modules and speech config for the FreeSWITCH Open Source telephone platform.
Requires: %{name} = %{version}-%{release}

%description lang-sv
Swedish language phrases module and directory structure for say module and voicemail

%package lang-th
Summary:  Provides Thai language dependend modules and speech config for the FreeSWITCH Open Source telephone platform.
Requires: %{name} = %{version}-%{release}

%description lang-th
Thai language phrases module and directory structure for say module and voicemail

%package lang-zh
Summary:  Provides Chinese language dependend modules and speech config for the FreeSWITCH Open Source telephone platform.
Requires: %{name} = %{version}-%{release}

%description lang-zh
Chinese language phrases module and directory structure for say module and voicemail


# Timer Modules
%package timer-posix
Summary:  Provides posix timer for the FreeSWITCH Open Source telephone platform.
Requires: %{name} = %{version}-%{release}

%description timer-posix
Provides posix timer for the FreeSWITCH Open Source telephone platform.

%package timer-timerfd
Summary:  Provides Linux Timerfs based timer for the FreeSWITCH Open Source telephone platform.
Requires: %{name} = %{version}-%{release}

%description timer-timerfd
Provides Linux Timerfs based timer for the FreeSWITCH Open Source telephone 
platform.


# XML INT Modules
%package xml-cdr
Summary:  Provides XML CDR interface for the FreeSWITCH Open Source telephone platform.
Requires: %{name} = %{version}-%{release}

%description xml-cdr
Provides XML CDR interface for the FreeSWITCH Open Source telephone platform.

%package xml-curl
Summary:  Provides XML Curl interface for the FreeSWITCH Open Source telephone platform.
Requires: %{name} = %{version}-%{release}

%description xml-curl
Provides XML Curl interface for the FreeSWITCH Open Source telephone platform.
Pull dynamic XML configs for FreeSWITCH over HTTP.

%package xml-rpc
Summary:  Provides XML-RPC interface for the FreeSWITCH Open Source telephone platform.
Requires: %{name} = %{version}-%{release}

%description xml-rpc
Provides XML-RPC interface for the FreeSWITCH Open Source telephone platform.

%package xml-scgi
Summary:  Provides XML-SCGI interface for the FreeSWITCH Open Source telephone platform.
Requires: %{name} = %{version}-%{release}

%description xml-scgi
Provides XML-SCGI interface for the FreeSWITCH Open Source telephone platform.


# FreeSWITCH basic config module
%package config-vanilla
Summary:  Basic vanilla config set for the FreeSWITCH Open Source telephone platform.
Requires: %{name} = %{version}-%{release}
Requires: freeswitch-application-abstraction
Requires: freeswitch-application-blacklist
Requires: freeswitch-application-callcenter
Requires: freeswitch-application-cidlookup
Requires: freeswitch-application-curl
Requires: freeswitch-application-db
Requires: freeswitch-application-directory
Requires: freeswitch-application-distributor
Requires: freeswitch-application-easyroute
Requires: freeswitch-application-enum
Requires: freeswitch-application-esf
Requires: freeswitch-application-expr
Requires: freeswitch-application-fifo
Requires: freeswitch-application-fsk
Requires: freeswitch-application-fsv
Requires: freeswitch-application-hash
Requires: freeswitch-application-httapi
Requires: freeswitch-application-http-cache
Requires: freeswitch-application-lcr
Requires: freeswitch-application-limit
Requires: freeswitch-application-memcache
Requires: freeswitch-application-nibblebill
Requires: freeswitch-application-redis
Requires: freeswitch-application-rss
Requires: freeswitch-application-sms
Requires: freeswitch-application-snapshot
Requires: freeswitch-application-soundtouch
Requires: freeswitch-application-spy
Requires: freeswitch-application-stress
Requires: freeswitch-application-valet_parking
Requires: freeswitch-application-video_filter
Requires: freeswitch-application-voicemail
Requires: freeswitch-application-voicemail-ivr
Requires: freeswitch-codec-passthru-amr
Requires: freeswitch-codec-passthru-g723_1
Requires: freeswitch-codec-h26x
Requires: freeswitch-database-pgsql
Requires: freeswitch-format-local-stream
Requires: freeswitch-format-native-file
Requires: freeswitch-format-portaudio-stream
Requires: freeswitch-format-tone-stream
Requires: freeswitch-lang-en

%description config-vanilla
Basic vanilla config set for the FreeSWITCH Open Source telephone platform.


%prep
%setup -q


%build
# Do not register for ClueCon during build
touch noreg

cp %{SOURCE1} ./modules.conf

export VERBOSE=yes
export ACLOCAL_FLAGS="-I /usr/share/aclocal"

export CFLAGS="%{optflags} -Wno-error=stringop-truncation"

./bootstrap.sh
autoreconf --force --install

%configure -C \
--disable-core-libedit-support \
--disable-static \
--enable-core-odbc-support \
--enable-core-pgsql-support \
--enable-system-lua \
--enable-system-xmlrpc-c \
--enable-threads \
--enable-timerfd-wrapper \
--with-certsdir=%{_sysconfdir}/pki/tls \
--with-dbdir=%{_localstatedir}/lib/%{name}/db \
--with-devrandom=/dev/random \
--with-erlang \
--with-grammardir=%{_datadir}/%{name}/grammar \
--with-htdocsdir=%{_datadir}/%{name}/htdocs \
--with-imagesdir=%{_localstatedir}/lib/%{name}/images \
--with-logfiledir=/var/log/%{name} \
--with-modinstdir=%{_libdir}/%{name}/mod \
--with-odbc \
--with-openssl \
--with-pkgconfigdir=%{_datadir}/%{name}/pkgconfig \
--with-recordingsdir=%{_localstatedir}/lib/%{name}/recordings \
--with-rundir=%{_rundir}/%{name} \
--with-scriptdir=%{_datadir}/%{name}/scripts \
--with-soundsdir=%{_datadir}/%{name}/sounds \

%{__make}


%install
%{__make} DESTDIR=%{buildroot} install

%{__mkdir} -p %{buildroot}%{_prefix}/log
%{__mkdir} -p %{buildroot}/var/log/%{name}
%{__mkdir} -p %{buildroot}%{_rundir}/%{name}
%{__install} -Dpm 0644 build/freeswitch.service %{buildroot}%{_unitdir}/freeswitch.service
%{__install} -Dpm 0644 build/freeswitch-tmpfiles.conf %{buildroot}%{_tmpfilesdir}/freeswitch.conf
%{__install} -D -m 744 build/freeswitch.sysconfig %{buildroot}/etc/sysconfig/freeswitch
%{__install} -D -m 644 build/freeswitch.monitrc %{buildroot}/etc/monit.d/freeswitch.monitrc

%{__rm} -f %{buildroot}/%{_libdir}/%{name}/mod/ftmod_sangoma_ss7*
%{__rm} -f %{buildroot}/%{_libdir}/%{name}/mod/ftmod_sangoma_isdn*


%pre
# TODO(lorbus) sysusers format and macro
if ! /usr/bin/id freeswitch &>/dev/null; then
	/usr/sbin/useradd -r -g freeswitch -s /bin/false -c "The FreeSWITCH Open Source Telephony Platform" -d %{_localstatedir}/lib/%{name} freeswitch || \
		%logmsg "Unexpected error adding user \"freeswitch\". Aborting installation."
fi


%post
%tmpfiles_create freeswitch
%systemd_post freeswitch.service


%preun
%systemd_preun freeswitch.service


%postun
# TODO(lorbus) sysusers format and macro
%systemd_postun_with_restart freeswitch.service
if [ $1 -eq 0 ]; then
    userdel freeswitch || %logmsg "User \"freeswitch\" could not be deleted."
fi


%files
# Basic Directory Structure
%dir %attr(0750, freeswitch, freeswitch) %{_localstatedir}/lib/%{name}
%dir %attr(0750, freeswitch, freeswitch) %{_localstatedir}/lib/%{name}/db
%dir %attr(0750, freeswitch, freeswitch) %{_localstatedir}/lib/%{name}/images
%dir %attr(0750, freeswitch, freeswitch) %{_localstatedir}/log/%{name}
%dir %attr(0750, freeswitch, freeswitch) %{_rundir}/%{name}
%dir %attr(0750, freeswitch, freeswitch) %{_sysconfdir}/%{name}
%dir %attr(0755, -, -) %{_datadir}/%{name}/grammar
%dir %attr(0755, -, -) %{_datadir}/%{name}/htdocs
%dir %attr(0755, -, -) %{_datadir}/%{name}/scripts
%dir %attr(0755, -, -) %{_datadir}/%{name}/fonts/
# Config Directory Structure
%dir %attr(0750, freeswitch, freeswitch) %{_sysconfdir}/%{name}/autoload_configs
%dir %attr(0750, freeswitch, freeswitch) %{_sysconfdir}/%{name}/dialplan
%dir %attr(0750, freeswitch, freeswitch) %{_sysconfdir}/%{name}/dialplan/default
%dir %attr(0750, freeswitch, freeswitch) %{_sysconfdir}/%{name}/dialplan/public
%dir %attr(0750, freeswitch, freeswitch) %{_sysconfdir}/%{name}/dialplan/skinny-patterns/
%dir %attr(0750, freeswitch, freeswitch) %{_sysconfdir}/%{name}/directory
%dir %attr(0750, freeswitch, freeswitch) %{_sysconfdir}/%{name}/directory/default
%dir %attr(0750, freeswitch, freeswitch) %{_sysconfdir}/%{name}/jingle_profiles
%dir %attr(0750, freeswitch, freeswitch) %{_sysconfdir}/%{name}/lang
%dir %attr(0750, freeswitch, freeswitch) %{_sysconfdir}/%{name}/mrcp_profiles
%dir %attr(0750, freeswitch, freeswitch) %{_sysconfdir}/%{name}/sip_profiles
%dir %attr(0750, freeswitch, freeswitch) %{_sysconfdir}/%{name}/sip_profiles/external
%dir %attr(0750, freeswitch, freeswitch) %{_sysconfdir}/%{name}/sip_profiles/external-ipv6
# Other Files
%config(noreplace) %{_datadir}/%{name}/htdocs/*
%{_unitdir}/freeswitch.service
%{_tmpfilesdir}/freeswitch.conf
%config(noreplace) /etc/sysconfig/freeswitch
%config(noreplace) /etc/monit.d/freeswitch.monitrc
# CLI
%attr(0755,-,-) %{_bindir}/fs_cli
%{_libdir}/libfreeswitch*.so*


%files devel
%{_datadir}/%{name}/pkgconfig/*
%{_includedir}/*.h
%{_includedir}/test/*.h


%files config-vanilla
%config(noreplace) %attr(0640, freeswitch, freeswitch) %{_sysconfdir}/%{name}/*.tpl
%config(noreplace) %attr(0640, freeswitch, freeswitch) %{_sysconfdir}/%{name}/*.ttml
%config(noreplace) %attr(0640, freeswitch, freeswitch) %{_sysconfdir}/%{name}/*.xml
%config(noreplace) %attr(0640, freeswitch, freeswitch) %{_sysconfdir}/%{name}/extensions.conf
%config(noreplace) %attr(0640, freeswitch, freeswitch) %{_sysconfdir}/%{name}/mime.types
%config(noreplace) %attr(0640, freeswitch, freeswitch) %{_sysconfdir}/%{name}/autoload_configs/abstraction.conf.xml
%config(noreplace) %attr(0640, freeswitch, freeswitch) %{_sysconfdir}/%{name}/autoload_configs/acl.conf.xml
%config(noreplace) %attr(0640, freeswitch, freeswitch) %{_sysconfdir}/%{name}/autoload_configs/alsa.conf.xml
%config(noreplace) %attr(0640, freeswitch, freeswitch) %{_sysconfdir}/%{name}/autoload_configs/amqp.conf.xml
%config(noreplace) %attr(0640, freeswitch, freeswitch) %{_sysconfdir}/%{name}/autoload_configs/amr.conf.xml
%config(noreplace) %attr(0640, freeswitch, freeswitch) %{_sysconfdir}/%{name}/autoload_configs/amrwb.conf.xml
%config(noreplace) %attr(0640, freeswitch, freeswitch) %{_sysconfdir}/%{name}/autoload_configs/av.conf.xml
%config(noreplace) %attr(0640, freeswitch, freeswitch) %{_sysconfdir}/%{name}/autoload_configs/avmd.conf.xml
%config(noreplace) %attr(0640, freeswitch, freeswitch) %{_sysconfdir}/%{name}/autoload_configs/blacklist.conf.xml
%config(noreplace) %attr(0640, freeswitch, freeswitch) %{_sysconfdir}/%{name}/autoload_configs/callcenter.conf.xml
%config(noreplace) %attr(0640, freeswitch, freeswitch) %{_sysconfdir}/%{name}/autoload_configs/cdr_csv.conf.xml
%config(noreplace) %attr(0640, freeswitch, freeswitch) %{_sysconfdir}/%{name}/autoload_configs/cdr_mongodb.conf.xml
%config(noreplace) %attr(0640, freeswitch, freeswitch) %{_sysconfdir}/%{name}/autoload_configs/cdr_pg_csv.conf.xml
%config(noreplace) %attr(0640, freeswitch, freeswitch) %{_sysconfdir}/%{name}/autoload_configs/cdr_sqlite.conf.xml
%config(noreplace) %attr(0640, freeswitch, freeswitch) %{_sysconfdir}/%{name}/autoload_configs/cepstral.conf.xml
%config(noreplace) %attr(0640, freeswitch, freeswitch) %{_sysconfdir}/%{name}/autoload_configs/cidlookup.conf.xml
%config(noreplace) %attr(0640, freeswitch, freeswitch) %{_sysconfdir}/%{name}/autoload_configs/conference_layouts.conf.xml
%config(noreplace) %attr(0640, freeswitch, freeswitch) %{_sysconfdir}/%{name}/autoload_configs/conference.conf.xml
%config(noreplace) %attr(0640, freeswitch, freeswitch) %{_sysconfdir}/%{name}/autoload_configs/console.conf.xml
%config(noreplace) %attr(0640, freeswitch, freeswitch) %{_sysconfdir}/%{name}/autoload_configs/curl.conf.xml
%config(noreplace) %attr(0640, freeswitch, freeswitch) %{_sysconfdir}/%{name}/autoload_configs/db.conf.xml
%config(noreplace) %attr(0640, freeswitch, freeswitch) %{_sysconfdir}/%{name}/autoload_configs/dialplan_directory.conf.xml
%config(noreplace) %attr(0640, freeswitch, freeswitch) %{_sysconfdir}/%{name}/autoload_configs/dingaling.conf.xml
%config(noreplace) %attr(0640, freeswitch, freeswitch) %{_sysconfdir}/%{name}/autoload_configs/directory.conf.xml
%config(noreplace) %attr(0640, freeswitch, freeswitch) %{_sysconfdir}/%{name}/autoload_configs/distributor.conf.xml
%config(noreplace) %attr(0640, freeswitch, freeswitch) %{_sysconfdir}/%{name}/autoload_configs/easyroute.conf.xml
%config(noreplace) %attr(0640, freeswitch, freeswitch) %{_sysconfdir}/%{name}/autoload_configs/enum.conf.xml
%config(noreplace) %attr(0640, freeswitch, freeswitch) %{_sysconfdir}/%{name}/autoload_configs/erlang_event.conf.xml
%config(noreplace) %attr(0640, freeswitch, freeswitch) %{_sysconfdir}/%{name}/autoload_configs/event_multicast.conf.xml
%config(noreplace) %attr(0640, freeswitch, freeswitch) %{_sysconfdir}/%{name}/autoload_configs/event_socket.conf.xml
%config(noreplace) %attr(0640, freeswitch, freeswitch) %{_sysconfdir}/%{name}/autoload_configs/fax.conf.xml
%config(noreplace) %attr(0640, freeswitch, freeswitch) %{_sysconfdir}/%{name}/autoload_configs/fifo.conf.xml
%config(noreplace) %attr(0640, freeswitch, freeswitch) %{_sysconfdir}/%{name}/autoload_configs/format_cdr.conf.xml
%config(noreplace) %attr(0640, freeswitch, freeswitch) %{_sysconfdir}/%{name}/autoload_configs/graylog2.conf.xml
%config(noreplace) %attr(0640, freeswitch, freeswitch) %{_sysconfdir}/%{name}/autoload_configs/hash.conf.xml
%config(noreplace) %attr(0640, freeswitch, freeswitch) %{_sysconfdir}/%{name}/autoload_configs/hiredis.conf.xml
%config(noreplace) %attr(0640, freeswitch, freeswitch) %{_sysconfdir}/%{name}/autoload_configs/httapi.conf.xml
%config(noreplace) %attr(0640, freeswitch, freeswitch) %{_sysconfdir}/%{name}/autoload_configs/http_cache.conf.xml
%config(noreplace) %attr(0640, freeswitch, freeswitch) %{_sysconfdir}/%{name}/autoload_configs/ivr.conf.xml
%config(noreplace) %attr(0640, freeswitch, freeswitch) %{_sysconfdir}/%{name}/autoload_configs/java.conf.xml
%config(noreplace) %attr(0640, freeswitch, freeswitch) %{_sysconfdir}/%{name}/autoload_configs/kazoo.conf.xml
%config(noreplace) %attr(0640, freeswitch, freeswitch) %{_sysconfdir}/%{name}/autoload_configs/lcr.conf.xml
%config(noreplace) %attr(0640, freeswitch, freeswitch) %{_sysconfdir}/%{name}/autoload_configs/local_stream.conf.xml
%config(noreplace) %attr(0640, freeswitch, freeswitch) %{_sysconfdir}/%{name}/autoload_configs/logfile.conf.xml
%config(noreplace) %attr(0640, freeswitch, freeswitch) %{_sysconfdir}/%{name}/autoload_configs/memcache.conf.xml
%config(noreplace) %attr(0640, freeswitch, freeswitch) %{_sysconfdir}/%{name}/autoload_configs/modules.conf.xml
%config(noreplace) %attr(0640, freeswitch, freeswitch) %{_sysconfdir}/%{name}/autoload_configs/mongo.conf.xml
%config(noreplace) %attr(0640, freeswitch, freeswitch) %{_sysconfdir}/%{name}/autoload_configs/msrp.conf.xml
%config(noreplace) %attr(0640, freeswitch, freeswitch) %{_sysconfdir}/%{name}/autoload_configs/nibblebill.conf.xml
%config(noreplace) %attr(0640, freeswitch, freeswitch) %{_sysconfdir}/%{name}/autoload_configs/opal.conf.xml
%config(noreplace) %attr(0640, freeswitch, freeswitch) %{_sysconfdir}/%{name}/autoload_configs/oreka.conf.xml
%config(noreplace) %attr(0640, freeswitch, freeswitch) %{_sysconfdir}/%{name}/autoload_configs/osp.conf.xml
%config(noreplace) %attr(0640, freeswitch, freeswitch) %{_sysconfdir}/%{name}/autoload_configs/pocketsphinx.conf.xml
%config(noreplace) %attr(0640, freeswitch, freeswitch) %{_sysconfdir}/%{name}/autoload_configs/portaudio.conf.xml
%config(noreplace) %attr(0640, freeswitch, freeswitch) %{_sysconfdir}/%{name}/autoload_configs/post_load_modules.conf.xml
%config(noreplace) %attr(0640, freeswitch, freeswitch) %{_sysconfdir}/%{name}/autoload_configs/pre_load_modules.conf.xml
%config(noreplace) %attr(0640, freeswitch, freeswitch) %{_sysconfdir}/%{name}/autoload_configs/presence_map.conf.xml
%config(noreplace) %attr(0640, freeswitch, freeswitch) %{_sysconfdir}/%{name}/autoload_configs/python.conf.xml
%config(noreplace) %attr(0640, freeswitch, freeswitch) %{_sysconfdir}/%{name}/autoload_configs/redis.conf.xml
%config(noreplace) %attr(0640, freeswitch, freeswitch) %{_sysconfdir}/%{name}/autoload_configs/rss.conf.xml
%config(noreplace) %attr(0640, freeswitch, freeswitch) %{_sysconfdir}/%{name}/autoload_configs/rtmp.conf.xml
%config(noreplace) %attr(0640, freeswitch, freeswitch) %{_sysconfdir}/%{name}/autoload_configs/sangoma_codec.conf.xml
%config(noreplace) %attr(0640, freeswitch, freeswitch) %{_sysconfdir}/%{name}/autoload_configs/shout.conf.xml
%config(noreplace) %attr(0640, freeswitch, freeswitch) %{_sysconfdir}/%{name}/autoload_configs/skinny.conf.xml
%config(noreplace) %attr(0640, freeswitch, freeswitch) %{_sysconfdir}/%{name}/autoload_configs/smpp.conf.xml
%config(noreplace) %attr(0640, freeswitch, freeswitch) %{_sysconfdir}/%{name}/autoload_configs/sms_flowroute.conf.xml
%config(noreplace) %attr(0640, freeswitch, freeswitch) %{_sysconfdir}/%{name}/autoload_configs/sndfile.conf.xml
%config(noreplace) %attr(0640, freeswitch, freeswitch) %{_sysconfdir}/%{name}/autoload_configs/sofia.conf.xml
%config(noreplace) %attr(0640, freeswitch, freeswitch) %{_sysconfdir}/%{name}/autoload_configs/spandsp.conf.xml
%config(noreplace) %attr(0640, freeswitch, freeswitch) %{_sysconfdir}/%{name}/autoload_configs/switch.conf.xml
%config(noreplace) %attr(0640, freeswitch, freeswitch) %{_sysconfdir}/%{name}/autoload_configs/syslog.conf.xml
%config(noreplace) %attr(0640, freeswitch, freeswitch) %{_sysconfdir}/%{name}/autoload_configs/timezones.conf.xml
%config(noreplace) %attr(0640, freeswitch, freeswitch) %{_sysconfdir}/%{name}/autoload_configs/translate.conf.xml
%config(noreplace) %attr(0640, freeswitch, freeswitch) %{_sysconfdir}/%{name}/autoload_configs/tts_commandline.conf.xml
%config(noreplace) %attr(0640, freeswitch, freeswitch) %{_sysconfdir}/%{name}/autoload_configs/unicall.conf.xml
%config(noreplace) %attr(0640, freeswitch, freeswitch) %{_sysconfdir}/%{name}/autoload_configs/unimrcp.conf.xml
%config(noreplace) %attr(0640, freeswitch, freeswitch) %{_sysconfdir}/%{name}/autoload_configs/v8.conf.xml
%config(noreplace) %attr(0640, freeswitch, freeswitch) %{_sysconfdir}/%{name}/autoload_configs/verto.conf.xml
%config(noreplace) %attr(0640, freeswitch, freeswitch) %{_sysconfdir}/%{name}/autoload_configs/voicemail_ivr.conf.xml
%config(noreplace) %attr(0640, freeswitch, freeswitch) %{_sysconfdir}/%{name}/autoload_configs/voicemail.conf.xml
%config(noreplace) %attr(0640, freeswitch, freeswitch) %{_sysconfdir}/%{name}/autoload_configs/vpx.conf.xml
%config(noreplace) %attr(0640, freeswitch, freeswitch) %{_sysconfdir}/%{name}/autoload_configs/xml_cdr.conf.xml
%config(noreplace) %attr(0640, freeswitch, freeswitch) %{_sysconfdir}/%{name}/autoload_configs/xml_curl.conf.xml
%config(noreplace) %attr(0640, freeswitch, freeswitch) %{_sysconfdir}/%{name}/autoload_configs/xml_rpc.conf.xml
%config(noreplace) %attr(0640, freeswitch, freeswitch) %{_sysconfdir}/%{name}/autoload_configs/xml_scgi.conf.xml
%config(noreplace) %attr(0640, freeswitch, freeswitch) %{_sysconfdir}/%{name}/autoload_configs/zeroconf.conf.xml
# Chatplans
%config(noreplace) %attr(0640, freeswitch, freeswitch) %{_sysconfdir}/%{name}/chatplan/default.xml
# Dialplans
%config(noreplace) %attr(0640, freeswitch, freeswitch) %{_sysconfdir}/%{name}/dialplan/*.xml
%config(noreplace) %attr(0640, freeswitch, freeswitch) %{_sysconfdir}/%{name}/dialplan/default/*.xml
%config(noreplace) %attr(0640, freeswitch, freeswitch) %{_sysconfdir}/%{name}/dialplan/public/*.xml
%config(noreplace) %attr(0640, freeswitch, freeswitch) %{_sysconfdir}/%{name}/dialplan/skinny-patterns/20-Demo.xml
%config(noreplace) %attr(0640, freeswitch, freeswitch) %{_sysconfdir}/%{name}/dialplan/skinny-patterns/20-Local_extension.xml
%config(noreplace) %attr(0640, freeswitch, freeswitch) %{_sysconfdir}/%{name}/dialplan/skinny-patterns/90-External.xml
%config(noreplace) %attr(0640, freeswitch, freeswitch) %{_sysconfdir}/%{name}/dialplan/skinny-patterns/99-Default_Drop.xml
# Fonts
%config(noreplace) %attr(0640, freeswitch, freeswitch) %{_datadir}/freeswitch/fonts/*.ttf
%config(noreplace) %attr(0640, freeswitch, freeswitch) %{_datadir}/freeswitch/fonts/OFL.txt
%config(noreplace) %attr(0640, freeswitch, freeswitch) %{_datadir}/freeswitch/fonts/README.fonts
# User Directories
%config(noreplace) %attr(0640, freeswitch, freeswitch) %{_sysconfdir}/%{name}/directory/*.xml
%config(noreplace) %attr(0640, freeswitch, freeswitch) %{_sysconfdir}/%{name}/directory/default/*
# IVR Menues
%config(noreplace) %attr(0640, freeswitch, freeswitch) %{_sysconfdir}/%{name}/ivr_menus/*.xml
# Sip Profiles
%config(noreplace) %attr(0640, freeswitch, freeswitch) %{_sysconfdir}/%{name}/sip_profiles/*.xml
%config(noreplace) %attr(0640, freeswitch, freeswitch) %{_sysconfdir}/%{name}/sip_profiles/external/*.xml
%config(noreplace) %attr(0640, freeswitch, freeswitch) %{_sysconfdir}/%{name}/sip_profiles/external-ipv6/*.xml
# Other Protocol Profiles
%config(noreplace) %attr(0640, freeswitch, freeswitch) %{_sysconfdir}/%{name}/jingle_profiles/*.xml
%config(noreplace) %attr(0640, freeswitch, freeswitch) %{_sysconfdir}/%{name}/mrcp_profiles/*.xml
%config(noreplace) %attr(0640, freeswitch, freeswitch) %{_sysconfdir}/%{name}/skinny_profiles/internal.xml


# Application Packages Modules
%files application-abstraction
%{_libdir}/%{name}/mod/mod_abstraction.so*

%files application-bert
%{_libdir}/%{name}/mod/mod_bert.so*

%files application-blacklist
%{_libdir}/%{name}/mod/mod_blacklist.so*

%files application-callcenter
%{_libdir}/%{name}/mod/mod_callcenter.so*

%files application-cidlookup
%{_libdir}/%{name}/mod/mod_cidlookup.so*

%files application-commands
%{_libdir}/%{name}/mod/mod_commands.so*

%files application-curl
%{_libdir}/%{name}/mod/mod_curl.so*

%files application-db
%{_libdir}/%{name}/mod/mod_db.so*

%files application-directory
%{_libdir}/%{name}/mod/mod_directory.so*

%files application-distributor
%{_libdir}/%{name}/mod/mod_distributor.so*

%files application-dptools
%{_libdir}/%{name}/mod/mod_dptools.so*

%files application-easyroute
%{_libdir}/%{name}/mod/mod_easyroute.so*

%files application-enum
%{_libdir}/%{name}/mod/mod_enum.so*

%files application-esf
%{_libdir}/%{name}/mod/mod_esf.so*

%files application-expr
%{_libdir}/%{name}/mod/mod_expr.so*

%files application-fifo
%{_libdir}/%{name}/mod/mod_fifo.so*

%files application-fsk
%{_libdir}/%{name}/mod/mod_fsk.so*

%files application-fsv
%{_libdir}/%{name}/mod/mod_fsv.so*

%files application-hash
%{_libdir}/%{name}/mod/mod_hash.so*

%files application-hiredis
%{_libdir}/%{name}/mod/mod_hiredis.so*

%files application-httapi
%{_libdir}/%{name}/mod/mod_httapi.so*

%files application-http-cache
%{_libdir}/%{name}/mod/mod_http_cache.so*

%files application-ladspa
%{_libdir}/%{name}/mod/mod_ladspa.so*

%files application-lcr
%{_libdir}/%{name}/mod/mod_lcr.so*

%files application-memcache
%{_libdir}/%{name}/mod/mod_memcache.so*

%files application-nibblebill
%{_libdir}/%{name}/mod/mod_nibblebill.so*

%files application-oreka
%{_libdir}/%{name}/mod/mod_oreka.so*

%files application-prefix
%{_libdir}/%{name}/mod/mod_prefix.so*

%files application-redis
%{_libdir}/%{name}/mod/mod_redis.so*

%files application-rss
%{_libdir}/%{name}/mod/mod_rss.so*

%files application-sms
%{_libdir}/%{name}/mod/mod_sms.so*

%files application-snapshot
%{_libdir}/%{name}/mod/mod_snapshot.so*

%files application-sonar
%{_libdir}/%{name}/mod/mod_sonar.so*

%files application-soundtouch
%{_libdir}/%{name}/mod/mod_soundtouch.so*

%files application-spandsp
%{_libdir}/%{name}/mod/mod_spandsp.so*

%files application-spy
%{_libdir}/%{name}/mod/mod_spy.so*

%files application-stress
%{_libdir}/%{name}/mod/mod_stress.so*

%files application-translate
%{_libdir}/%{name}/mod/mod_translate.so*

%files application-valet_parking
%{_libdir}/%{name}/mod/mod_valet_parking.so*

%files application-video_filter
%{_libdir}/%{name}/mod/mod_video_filter.so*

%files application-vmd
%{_libdir}/%{name}/mod/mod_vmd.so*

%files application-voicemail
%{_libdir}/%{name}/mod/mod_voicemail.so*

%files application-voicemail-ivr
%{_libdir}/%{name}/mod/mod_voicemail_ivr.so*


# ASR TTS Modules
%files asrtts-tts-commandline
%{_libdir}/%{name}/mod/mod_tts_commandline.so*

%files asrtts-unimrcp
%{_libdir}/%{name}/mod/mod_unimrcp.so*


# Codec Modules
%files codec-passthru-amr
%{_libdir}/%{name}/mod/mod_amr.so*

%files codec-passthru-amrwb
%{_libdir}/%{name}/mod/mod_amrwb.so*

%files codec-codec2
%{_libdir}/%{name}/mod/mod_codec2.so*

%files codec-dahdi
%{_libdir}/%{name}/mod/mod_dahdi_codec.so*

%files codec-passthru-g723_1
%{_libdir}/%{name}/mod/mod_g723_1.so*

%files codec-h26x
%{_libdir}/%{name}/mod/mod_h26x.so*

%files codec-isac
%{_libdir}/%{name}/mod/mod_isac.so*

%files codec-mp4v
%{_libdir}/%{name}/mod/mod_mp4v.so*

%files codec-opus
%{_libdir}/%{name}/mod/mod_opus.so*
%config(noreplace) %attr(0640, freeswitch, freeswitch) %{_sysconfdir}/%{name}/autoload_configs/opus.conf.xml

%files codec-theora
%{_libdir}/%{name}/mod/mod_theora.so*


# Database Modules
%files database-mariadb
%{_libdir}/%{name}/mod/mod_mariadb.so*

%files database-pgsql
%{_libdir}/%{name}/mod/mod_pgsql.so*


# Dialplan Modules
%files dialplan-directory
%{_libdir}/%{name}/mod/mod_dialplan_directory.so*

%files dialplan-xml
%{_libdir}/%{name}/mod/mod_dialplan_xml.so*


# Endpoint Modules
%files endpoint-alsa
%{_libdir}/%{name}/mod/mod_alsa.so*

%files endpoint-dingaling
%{_libdir}/%{name}/mod/mod_dingaling.so*

%files endpoint-loopback
%{_libdir}/%{name}/mod/mod_portaudio.so*

%files endpoint-rtc
%{_libdir}/%{name}/mod/mod_rtc.so*

%files endpoint-rtmp
%{_libdir}/%{name}/mod/mod_rtmp.so*

%files endpoint-sofia
%{_libdir}/%{name}/mod/mod_sofia.so*

%files endpoint-verto
%{_libdir}/%{name}/mod/mod_verto.so*


# Event Handler Modules
%files event-amqp
%{_libdir}/%{name}/mod/mod_amqp.so*

%files event-cdr-csv
%{_libdir}/%{name}/mod/mod_cdr_csv.so*

%files event-cdr-pg-csv
%{_libdir}/%{name}/mod/mod_cdr_pg_csv.so*

%files event-cdr-sqlite
%{_libdir}/%{name}/mod/mod_cdr_sqlite.so*

%files event-multicast
%{_libdir}/%{name}/mod/mod_event_multicast.so*

%files event-socket
%{_libdir}/%{name}/mod/mod_event_socket.so*

%files event-format-cdr
%{_libdir}/%{name}/mod/mod_format_cdr.so*

%files event-json-cdr
%{_libdir}/%{name}/mod/mod_json_cdr.so*

%files event-kazoo
%{_libdir}/%{name}/mod/mod_kazoo.so*

%files event-odbc-cdr
%{_libdir}/%{name}/mod/mod_odbc_cdr.so*

# Format Modules
%files format-imagick
%{_libdir}/%{name}/mod/mod_imagick.so*

%files format-local-stream
%{_libdir}/%{name}/mod/mod_local_stream.so*

%files format-native-file
%{_libdir}/%{name}/mod/mod_native_file.so*

%files format-png
%{_libdir}/%{name}/mod/mod_png.so*

%files format-portaudio-stream
%{_libdir}/%{name}/mod/mod_portaudio_stream.so*

%files format-shell-stream
%{_libdir}/%{name}/mod/mod_shell_stream.so*

%files format-shout
%{_libdir}/%{name}/mod/mod_shout.so*

%files format-sndfile
%{_libdir}/%{name}/mod/mod_sndfile.so*

%files format-tone-stream
%{_libdir}/%{name}/mod/mod_tone_stream.so*


# Programming Language Modules
%files lua
%{_libdir}/%{name}/mod/mod_lua*.so*
%config(noreplace) %attr(0640, freeswitch, freeswitch) %{_sysconfdir}/%{name}/autoload_configs/lua.conf.xml

%files perl
%{_libdir}/%{name}/mod/mod_perl*.so*
%{_prefix}/perl/*
%config(noreplace) %attr(0640, freeswitch, freeswitch) %{_sysconfdir}/%{name}/autoload_configs/perl.conf.xml

%files yaml
%{_libdir}/%{name}/mod/mod_yaml*.so*


# Logger Modules
%files logger-console
%{_libdir}/%{name}/mod/mod_console.so*

%files logger-graylog2
%{_libdir}/%{name}/mod/mod_graylog2.so*

%files logger-logfile
%{_libdir}/%{name}/mod/mod_logfile.so*

%files logger-syslog
%{_libdir}/%{name}/mod/mod_syslog.so*


# Language Modules
%files lang-de
%dir %attr(0750, freeswitch, freeswitch) %{_sysconfdir}/%{name}/lang/de
%dir %attr(0750, freeswitch, freeswitch) %{_sysconfdir}/%{name}/lang/de/demo
%dir %attr(0750, freeswitch, freeswitch) %{_sysconfdir}/%{name}/lang/de/vm
%config(noreplace) %attr(0640, freeswitch, freeswitch) %{_sysconfdir}/%{name}/lang/de/*.xml
%config(noreplace) %attr(0640, freeswitch, freeswitch) %{_sysconfdir}/%{name}/lang/de/*/*.xml
%{_libdir}/%{name}/mod/mod_say_de.so*

%files lang-en
%dir %attr(0750, freeswitch, freeswitch) %{_sysconfdir}/%{name}/lang/en
%dir %attr(0750, freeswitch, freeswitch) %{_sysconfdir}/%{name}/lang/en/demo
%dir %attr(0750, freeswitch, freeswitch) %{_sysconfdir}/%{name}/lang/en/vm
%dir %attr(0750, freeswitch, freeswitch) %{_sysconfdir}/%{name}/lang/en/dir
%dir %attr(0750, freeswitch, freeswitch) %{_sysconfdir}/%{name}/lang/en/ivr
%config(noreplace) %attr(0640, freeswitch, freeswitch) %{_sysconfdir}/%{name}/lang/en/*.xml
%config(noreplace) %attr(0640, freeswitch, freeswitch) %{_sysconfdir}/%{name}/lang/en/*/*.xml
%{_libdir}/%{name}/mod/mod_say_en.so*

%files lang-es
%dir %attr(0750, freeswitch, freeswitch) %{_sysconfdir}/%{name}/lang/es
%dir %attr(0750, freeswitch, freeswitch) %{_sysconfdir}/%{name}/lang/es/demo
%dir %attr(0750, freeswitch, freeswitch) %{_sysconfdir}/%{name}/lang/es/vm
%config(noreplace) %attr(0640, freeswitch, freeswitch) %{_sysconfdir}/%{name}/lang/es/*.xml
%config(noreplace) %attr(0640, freeswitch, freeswitch) %{_sysconfdir}/%{name}/lang/es/*/*.xml
%{_libdir}/%{name}/mod/mod_say_es.so*

%files lang-es-ar
%{_libdir}/%{name}/mod/mod_say_es_ar.so*

%files lang-fa
%{_libdir}/%{name}/mod/mod_say_fa.so*

%files lang-fr
%dir %attr(0750, freeswitch, freeswitch) %{_sysconfdir}/%{name}/lang/fr
%dir %attr(0750, freeswitch, freeswitch) %{_sysconfdir}/%{name}/lang/fr/demo
%dir %attr(0750, freeswitch, freeswitch) %{_sysconfdir}/%{name}/lang/fr/vm
%config(noreplace) %attr(0640, freeswitch, freeswitch) %{_sysconfdir}/%{name}/lang/fr/*.xml
%config(noreplace) %attr(0640, freeswitch, freeswitch) %{_sysconfdir}/%{name}/lang/fr/*/*.xml
%{_libdir}/%{name}/mod/mod_say_fr.so*

%files lang-he
%dir %attr(0750, freeswitch, freeswitch) %{_sysconfdir}/%{name}/lang/he/
%dir %attr(0750, freeswitch, freeswitch) %{_sysconfdir}/%{name}/lang/he/demo
%dir %attr(0750, freeswitch, freeswitch) %{_sysconfdir}/%{name}/lang/he/vm
%config(noreplace) %attr(0640, freeswitch, freeswitch) %{_sysconfdir}/%{name}/lang/he/*.xml
%config(noreplace) %attr(0640, freeswitch, freeswitch) %{_sysconfdir}/%{name}/lang/he/*/*.xml
%{_libdir}/%{name}/mod/mod_say_he.so*

%files lang-hr
%dir %attr(0750, freeswitch, freeswitch) %{_sysconfdir}/%{name}/lang/hr/
%dir %attr(0750, freeswitch, freeswitch) %{_sysconfdir}/%{name}/lang/hr/demo
%dir %attr(0750, freeswitch, freeswitch) %{_sysconfdir}/%{name}/lang/hr/vm
%config(noreplace) %attr(0640, freeswitch, freeswitch) %{_sysconfdir}/%{name}/lang/hr/*.xml
%config(noreplace) %attr(0640, freeswitch, freeswitch) %{_sysconfdir}/%{name}/lang/hr/*/*.xml
%{_libdir}/%{name}/mod/mod_say_hr.so*

%files lang-hu
%dir %attr(0750, freeswitch, freeswitch) %{_sysconfdir}/%{name}/lang/hu/
%dir %attr(0750, freeswitch, freeswitch) %{_sysconfdir}/%{name}/lang/hu/demo
%dir %attr(0750, freeswitch, freeswitch) %{_sysconfdir}/%{name}/lang/hu/vm
%config(noreplace) %attr(0640, freeswitch, freeswitch) %{_sysconfdir}/%{name}/lang/hu/*.xml
%config(noreplace) %attr(0640, freeswitch, freeswitch) %{_sysconfdir}/%{name}/lang/hu/*/*.xml
%{_libdir}/%{name}/mod/mod_say_hu.so*

%files lang-it
%dir %attr(0750, freeswitch, freeswitch) %{_sysconfdir}/%{name}/lang/it/
%dir %attr(0750, freeswitch, freeswitch) %{_sysconfdir}/%{name}/lang/it/demo
%dir %attr(0750, freeswitch, freeswitch) %{_sysconfdir}/%{name}/lang/it/vm
%config(noreplace) %attr(0640, freeswitch, freeswitch) %{_sysconfdir}/%{name}/lang/it/*.xml
%config(noreplace) %attr(0640, freeswitch, freeswitch) %{_sysconfdir}/%{name}/lang/it/*/*.xml
%{_libdir}/%{name}/mod/mod_say_it.so*

%files lang-ja
%dir %attr(0750, freeswitch, freeswitch) %{_sysconfdir}/%{name}/lang/ja/
%dir %attr(0750, freeswitch, freeswitch) %{_sysconfdir}/%{name}/lang/ja/demo
%dir %attr(0750, freeswitch, freeswitch) %{_sysconfdir}/%{name}/lang/ja/vm
%config(noreplace) %attr(0640, freeswitch, freeswitch) %{_sysconfdir}/%{name}/lang/ja/*.xml
%config(noreplace) %attr(0640, freeswitch, freeswitch) %{_sysconfdir}/%{name}/lang/ja/*/*.xml
%{_libdir}/%{name}/mod/mod_say_ja.so*

%files lang-nl
%dir %attr(0750, freeswitch, freeswitch) %{_sysconfdir}/%{name}/lang/nl/
%dir %attr(0750, freeswitch, freeswitch) %{_sysconfdir}/%{name}/lang/nl/demo
%dir %attr(0750, freeswitch, freeswitch) %{_sysconfdir}/%{name}/lang/nl/vm
%config(noreplace) %attr(0640, freeswitch, freeswitch) %{_sysconfdir}/%{name}/lang/nl/*.xml
%config(noreplace) %attr(0640, freeswitch, freeswitch) %{_sysconfdir}/%{name}/lang/nl/*/*.xml
%{_libdir}/%{name}/mod/mod_say_nl.so*

%files lang-pl
%dir %attr(0750, freeswitch, freeswitch) %{_sysconfdir}/%{name}/lang/pl/
%dir %attr(0750, freeswitch, freeswitch) %{_sysconfdir}/%{name}/lang/pl/demo
%dir %attr(0750, freeswitch, freeswitch) %{_sysconfdir}/%{name}/lang/pl/vm
%config(noreplace) %attr(0640, freeswitch, freeswitch) %{_sysconfdir}/%{name}/lang/pl/*.xml
%config(noreplace) %attr(0640, freeswitch, freeswitch) %{_sysconfdir}/%{name}/lang/pl/*/*.xml
%{_libdir}/%{name}/mod/mod_say_pl.so*

%files lang-pt
%dir %attr(0750, freeswitch, freeswitch) %{_sysconfdir}/%{name}/lang/pt
%dir %attr(0750, freeswitch, freeswitch) %{_sysconfdir}/%{name}/lang/pt/demo
%dir %attr(0750, freeswitch, freeswitch) %{_sysconfdir}/%{name}/lang/pt/vm
%config(noreplace) %attr(0640, freeswitch, freeswitch) %{_sysconfdir}/%{name}/lang/pt/*.xml
%config(noreplace) %attr(0640, freeswitch, freeswitch) %{_sysconfdir}/%{name}/lang/pt/*/*.xml
%{_libdir}/%{name}/mod/mod_say_pt.so*

%files lang-ru
%dir %attr(0750, freeswitch, freeswitch) %{_sysconfdir}/%{name}/lang/ru
%dir %attr(0750, freeswitch, freeswitch) %{_sysconfdir}/%{name}/lang/ru/demo
%dir %attr(0750, freeswitch, freeswitch) %{_sysconfdir}/%{name}/lang/ru/vm
%config(noreplace) %attr(0640, freeswitch, freeswitch) %{_sysconfdir}/%{name}/lang/ru/*.xml
%config(noreplace) %attr(0640, freeswitch, freeswitch) %{_sysconfdir}/%{name}/lang/ru/*/*.xml
%{_libdir}/%{name}/mod/mod_say_ru.so*

%files lang-sv
%dir %attr(0750, freeswitch, freeswitch) %{_sysconfdir}/%{name}/lang/sv
%dir %attr(0750, freeswitch, freeswitch) %{_sysconfdir}/%{name}/lang/sv/demo
%dir %attr(0750, freeswitch, freeswitch) %{_sysconfdir}/%{name}/lang/sv/vm
%config(noreplace) %attr(0640, freeswitch, freeswitch) %{_sysconfdir}/%{name}/lang/sv/*.xml
%config(noreplace) %attr(0640, freeswitch, freeswitch) %{_sysconfdir}/%{name}/lang/sv/vm/*.xml
%{_libdir}/%{name}/mod/mod_say_sv.so*

%files lang-th
%dir %attr(0750, freeswitch, freeswitch) %{_sysconfdir}/%{name}/lang/th
%dir %attr(0750, freeswitch, freeswitch) %{_sysconfdir}/%{name}/lang/th/demo
%dir %attr(0750, freeswitch, freeswitch) %{_sysconfdir}/%{name}/lang/th/vm
%config(noreplace) %attr(0640, freeswitch, freeswitch) %{_sysconfdir}/%{name}/lang/th/*.xml
%config(noreplace) %attr(0640, freeswitch, freeswitch) %{_sysconfdir}/%{name}/lang/th/vm/*.xml
%{_libdir}/%{name}/mod/mod_say_th.so*

%files lang-zh
%dir %attr(0750, freeswitch, freeswitch) %{_sysconfdir}/%{name}/lang/zh
%dir %attr(0750, freeswitch, freeswitch) %{_sysconfdir}/%{name}/lang/zh/demo
%dir %attr(0750, freeswitch, freeswitch) %{_sysconfdir}/%{name}/lang/zh/vm
%config(noreplace) %attr(0640, freeswitch, freeswitch) %{_sysconfdir}/%{name}/lang/zh/*.xml
%config(noreplace) %attr(0640, freeswitch, freeswitch) %{_sysconfdir}/%{name}/lang/zh/vm/*.xml
%{_libdir}/%{name}/mod/mod_say_zh.so*


# Timer Modules
%files timer-posix
%{_libdir}/%{name}/mod/mod_posix_timer.so*

%files timer-timerfd
%{_libdir}/%{name}/mod/mod_timerfd.so*


# XMLINT  Modules
%files xml-cdr
%{_libdir}/%{name}/mod/mod_xml_cdr.so*

%files xml-curl
%{_libdir}/%{name}/mod/mod_xml_curl.so*

%files xml-rpc
%{_libdir}/%{name}/mod/mod_xml_rpc.so*

%files xml-scgi
%{_libdir}/%{name}/mod/mod_xml_scgi.so*


%changelog
