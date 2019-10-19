# Storing-Large-Files-In-Mongo
Saving of large files in MongoDB using python

MongoDB stores all documents as BSON, a binary encoding of JSON format.The maximum BSON document size in MongoDB is 16 MB.
They might easily exceed the limit when we want to store large files like videos and songs.  

There modules like GridFS, which is a specification for storing and retrieving files that exceed the BSON-document size limit.
In this project I have approached the problem in a somewhat similar way, by breaking down the data into smaller chunks and then
storing each chunk as a seperate document with a unique Id, and then retrieving the data using the same.

The code is entirely pythonic in nature and uses common python libraries.

Libraries/Dependencies used:
1) pymongo
2) math
3) sys
4) numpy
5) pandas
6) uuid
7) datetime
8) json
