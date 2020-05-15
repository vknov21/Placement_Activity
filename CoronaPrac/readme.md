------------
INTRODUCTION
------------
* start_File.py is the main file to start with.
* It fetches the dataset from static URL to predict to the latest.
* The data is analysed on the basis of user input, either for 'World' or 'India'.

* There are different countries having cases >=100 and also "WORLD" included in it.
* The data is mapped in 10th degree polynomial.

* For the case of 'INDIA' the cases must be >=50.
* The data for corona virus cases is mapped in 4th degree polynomial, deaths is mapped in 2nd degree polynomial, cure is mapped in 3rd degree polynomial.

* The approximated graph is shown with the scattered no. of cases.

------------
REQUIREMENTS
------------
* 'requests' must be present in Ubuntu. Can be installed using 'pip install requests'
* Python compiler must be present with libraries as matplotlib, scikit-learn, numpy.

------------------
DIRECTIONS FOR USE
------------------
* The file can be accessed using 'python3 start_File.py'
* It is recommended to have Internet On to fetch the latest file from the server, but not necessary.
* The detailed instruction is provided with the running of file
