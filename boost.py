class settings:
    url = 'https://sourceforge.net/projects/boost/files/boost/1.63.0/boost_1_63_0.tar.gz'
    package = 'boost_1_63_0.tar.gz'
    name = 'Boost'
    foldername = 'boost_1_63_0'
    desc = 'Boost is a set of libraries for the C++ programming language that provide support for tasks and structures such as linear algebra, pseudorandom number generation, multithreading, image processing, regular expressions, and unit testing'
class install:
    cd = 'cd boost_1_63_0'
    configure = './bootstrap.sh'
    build = './b2 install'
   # Tesing updates
