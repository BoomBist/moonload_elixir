class settings:
    url = 'https://miniupnp.tuxfamily.org/files/download.php?file=miniupnpd-2.0.20161216.tar.gz'
    package = 'miniupnpd-2.0.20161216.tar.gz'
    name = 'MiniUPnP'
    foldername = 'miniupnpd-2.0.20161216'
    desc = 'The UPnP protocol is supported by most home adsl/cable routers and Microsoft Windows 2K/XP. The aim of the MiniUPnP project is to bring a free software solution to support the "Internet Gateway Device" part of the protocol.'
class install:
    configure = 'cd miniupnpd-2.0.20161216 && ./genconfig.sh'
    build = 'cd miniupnpd-2.0.20161216 && make -f Makefile.linux'