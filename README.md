# Grizzlies

A very simple and fast data analysis module for python. This project came to existence for the need of applying basic statistical analysis on datasets with more than 10000 entries. A couple long an monotonous university assignments were the motivator of this. Code is self-documenting and very clear.

## Installation

Grizzlies does not have [pip](https://pip.pypa.io/en/stable/) package right now. However, I can make one due to sufficient demand.

## Usage

```python
import grizzlies

# returns 3.0
grizzlies.average([1,2,3,4,5])

# returns 5
grizzlies.max([[1,2,3,4,5])

# returns 3
grizzlies.median([[1,2,3,4,5])

# returns 1.4142135623730951
grizzlies.stdev([1,2,3,4,5])

# returns [-2, -1, 0, 1, 2, 3, 3.75, 4]
grizzlies.extract([-2,-1,0,1,2,3,3.75,4,4.5,5],4.5,'ceil')

# returns [0, 1, 2, 3, 3.75, 4, 4.5, 5.0]
grizzlies..extract([-2,-1,0,1,2,3,3.75,4,4.5,5],0,'floor')
```

## Contributing
All contributions and pull requests are very welcome. For major changes or feature additions, please add well written comments to your commit.

## License
[GNU GPLv3](https://choosealicense.com/licenses/gpl-3.0/)
