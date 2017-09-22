### installation dlib sur ubuntu aller sur la home page chercher le paquet ensuite
# l'extraire 

tar xvjf dlib-19.4.tar.bz2
cd dlib-19.4/python_examples/
mkdir build
cd build
cmake ../../tools/python
cmake --build . --config Release --target install
cd ..
ls -l dlib.so 
