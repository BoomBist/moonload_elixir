class settings:
    url = 'https://sourceforge.net/projects/boost/files/boost/1.63.0/boost_1_63_0.tar.gz'
    url2 = 'https://github.com/boostorg/boost/archive/boost-1.63.0.tar.gz'
    package = 'boost_1_63_0.tar.gz'
    name = 'Boost'
    desc = 'Boost is a set of libraries for the C++ programming language that provide support for tasks and structures such as linear algebra, pseudorandom number generation, multithreading, image processing, regular expressions, and unit testing'
class install:
    configure = 'cd boost_1_63_0 && ./bootstrap.sh'
    build = 'cd boost_1_63_0 && ./b2 install'

