# Password-Reconstructor
The program uses brute force method to reconstruct the password given by user
through two approaches:

1. Time complexity: O(N^2)
    ---> compares current parrword character with string of all available
        character using linear search
2. Time complexity: O(NlogN)
    ---> compares current parrword character with string of all available
        character using binary search( string is ascii sorted)

In addition, it also has option to show steps throught reconstruction with iteration count
so that user can compare two methods visually.
