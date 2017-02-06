class settings:
    url = 'https://download.qt.io/archive/qt/4.8/4.8.0/qt-everywhere-opensource-src-4.8.0.tar.gz'
    url2 = 'http://ftp.psu.ru/programming/qt/archive/qt/4.8/4.8.0/qt-everywhere-opensource-src-4.8.0.tar.gz'
    package = 'qt-everywhere-opensource-src-4.8.0.tar.gz'
    name = 'QT4 Libraries'
    foldername = 'qt-everywhere-opensource-src-4.8.0'
    desc = 'Qt is used for developing multi-platform applications and graphical user interfaces (GUIs)'
class install:
    configure = 'cd qt-everywhere-opensource-src-4.8.0 && ./configure'
    build = 'cd qt-everywhere-opensource-src-4.8.0 && sudo make install'
