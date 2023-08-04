'''     hashing in python is an important method to store data in arrays and getting them quickly (mostly o(1))
        python use hashing in dictionary and sets
'''
'''        dictionary ,sets and hashmaps uses hashing to store data and accessing it quickly 
            by using a hash function to get the index and set the value 
            when you call to get the calue in main class it convert the key you passed to hash and get the index
            index =hashcode%len(arr)
'''

'''
            the main problem in hashing is collisions(different keys with different hashes refer to the same index)
            we can handle it by using chaining , propping or rehashing
'''
'''
            -chaining is used by making linked list in the array, so if you have two hashes refer to the same index 
            it get stored in the next element in the linked list(that's make the get method more than o(1))
            -propping is by adding 1 or skiping slots randomly to the index until it finds an empty element in the array
'''

