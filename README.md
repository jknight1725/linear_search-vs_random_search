# linear_search_vs_random_search
Compare two simple algorithms to find a randomly generated number 

Worst case algo uses linear search to check all 1000 possible choices in order  e.g. (000, 001, 002...found it!)
We can expect to find the random number in n/2 time

Example report of linear search 
```
Number of Tries: 10000
Highest number of guess in a try: 1000
Lowest tries: 1
Number of Correct tries: 10000
Average number of tries: 4996477/10000: 499.6477 
```



Random case generates a random number and compares it to the originally generated random number e.g. (373, 492...found it!)
We can expect to find the random number in n time

Example report of random search
```
Number of Tries: 10000
Highest number of guess in a try: 5000
Lowest tries: 0
Number of Correct tries: 10000
Average number of tries: 10229285/10000: 1022.9285 
```
