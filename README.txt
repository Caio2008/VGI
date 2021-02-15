In the file extract_node.py you must put in line 18, in the variable "entra" the path of your 'input file'.
You must create a .txt file with two columns: the indication "node" and the identifier node OSM, as shown in the example below.

node 837037430
node 837037439

In line 57, in the variable "saida", you must indicate the path of your output file that will be created.
As in the example below, the output .txt file will have three columns:
id: OSM node identifier
n_edi: indicates the number of times the node has been edited
n_usu: indicates how many contributors made edits to the node.

id n_edi n_usu
4645800 10 6
4645802 16 12
__________________________________________________________________________________________________________


In the file extract_way.py you must put in line 18, in the variable "entra" the path of your 'input file'.
You must create a .txt file with one column: the OSM identifier for the way, as shown in the example below.

175517611
28827347
28827348

In line 57, in the variable "saida", you must indicate the path of the output file that will be created.
As in the example below, the output .txt file will have three columns:
id: OSM way identifier
version: indicates the number of times the way has been edited
user: indicates how many contributors made edits to the way.

id version user
175517611 5 5
28827347 6 4