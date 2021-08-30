# SparseSort 🧮 

## In a nutshell 🥜
This simple script allows to order a sparse array moving only the entries greater than zero, leaving the zeros untouched. Let's see the following example:


Given 
```
[0.9, 0, 0, 0, 0.1, 0, 0, 0.7, 0, 0, 0.4]
```
we get this result:
```
[0.9, 0, 0, 0, 0.7, 0, 0, 0.4, 0, 0, 0.1]
```

If the input has no zeros, it behaves like an ordinary sorter. Here it is an example:

Given 
```
[1, 2, 3, 4, 5, 6, 7, 8, 9]
```
we get this result:
```
[9, 8, 7, 6, 5, 4, 3, 2, 1]
```

## Requirements:

- Python `> 3`

## Analysis

The worst case scenario is showed in the table below:

|          | Complexity |   |   |   |
|----------|:----------:|---|---|---|
| Temporal |   O(n^2)   |   |   |   |
| Spatial  |    O(n)    |   |   |   |
|          |            |   |   |   |


