Owner: Harisankar Krishna Swamy
License: Just tell Hari before you use any or part of this repo code from Hari at harisankar.krishna@outlook.com
Contents:
This repo contains Hari's implementations of data structures in Python.

Features to Implement:
----------------------
1) Thread Safety.
2) LinkedList currently has length attribute. Add __len__ too so that it is close to pythonic usage.
3) Tree needs a replace operation. This will come in handy when tree is used in hash buckets.
4) implement has_key for all ds with key, value pairs
4) Return a default value for ops on keys that are not present on a K,V store. raising ValueError is good but
   Python's own code in /usr/lib/python2.7/collections.py and /usr/lib/python2.7/_abcoll.py have ds[key] and
   also get(key, default = None). This seems better.


TESTING
=======
On command prompt type

python -m unittest discover tests
