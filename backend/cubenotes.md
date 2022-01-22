# Notes
Measure how "likely" cube is (starting with EHDREC rank?)

Optimize through sequence of cuts, additions, and swaps

## CUT:
1. Choose 2 cards from cube:
    the top 2 most "surprising" cards (but with least votes)

2. Select 1 and remove from cube

## ADDITION:
1. Choose 2 cards from inv not in cube
    (random inv cards weighted by rank)

2. Select 1 and add to cube

## SWAP:
1. Choose card from inv (not in cube) and card in cube
    (same as addition)

2. Select one - if cube card, do nothing. otherwise remove cube card from cube and add inv card

