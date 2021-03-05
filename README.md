# Python-Dropbox-Clone

Introduction. 
This is a rough and simple python server and client implementation that syncs the files in a source directory from the client to a destination directory on the server.
Overall with rough testing and implementation of basic functions, this project took between 3 to 4 hours to complete.

Currently, the client and server together are able to connect to each other, update modified files, upload new files and delete files in the destination directory based on changes in the client source directory.

Instructions

. Create destination directory for server.

. Change the port number in the server code to your desired number and change the 'fp' variable with the location of the intended destination directory.

. Run the server.

. Change both hostname (using IP address) and port number in the client code to match the address the server is listening on, then change the 'fp' variable with the intended source directory

. Run the client code.

. The client and server should then be able to syncronise the files in the source directory with the destination directory 


Improvements
Whilst the client and server work as intended, there are still quirks and optimisations that could be made if more time was spent on it. 

Method - Firstly, the client does not comminicate with the server to identify files that need modifying, deleting or uploading. Instead, a client side log list of communications with the server is used to keep track of the state of the server's destination directory.
Optimisation - As the server's state is essentially a black box, the client and server could instead communicate to each other which the state of each other's files to identify if an update, upload or deletion is needed. 

Method - The data structure implemented to keep track of the state of the files was a simple files list. This means that the time complexity is O(n), therefore the rate at which the client could keep the server up to date depends on the number of files in the source directory.
Optimisation - Using a more efficient data structure and search method, such as a hash map, may increase look up times. However, I believe a more effective method may be to set up asyncronouss or threaded functions to monitor the state of files and save requests as tasks to be asyncronisly executed. This may increase the rate at which changes in files are detected, and therefore, updated, uploaded or deleted in the destination directory. 

Method - Delays in strategic places where data would be sent to the server were placed for debug purposes as well as to allow time for data to be recieved by the server.
Optimisation - A simple fix to optimise this method would be to make the function of sending the data client side, and reviecing the data server side, asyncronous and using 'await' to allow time to ensure the server has recieved the data packets. This would moreover benefit files with larger sizes as they would need more time to be transmitted over the network

