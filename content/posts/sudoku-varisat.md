---
title: "Writing A Sudoku Solver using varisat in Rust"
date: 2020-04-12T17:07:25-05:00
draft: false
---

I have been using Rust professionally for almost six months now and have tried it on and off for more than one year now. In this post, I will be writing a Sudoku solver using the SAT solver, [`varisat`](https://crates.io/crates/varisat). 

## What is an SAT solver and why use it?

Peter Norvig has written an in-depth [article](https://norvig.com/sudoku.html) about the various strategies for writing sudoku solvers. While this was my original plan, I came across SAT solvers in this (video)[https://youtu.be/_GP9OpZPUYc?t=889] by Raymond Hettinger. Not having a computer science background meant that I had never heard of this before and was intrigued. This (video)[https://www.youtube.com/watch?v=x2XtpCn0-bM] by Martin Hořeňovský also helped me in understanding how to express a Sudoku puzzle as an SAT problem. There are many similarities between his C++ code and my Rust code. 

## Boolean Satisfiability Problem

According to Wikipedia, 

> the Boolean Satisfiability problem is the problem of determining if there exists an interpretation that satisfies a given Boolean formula.

What this means is that if you can express your problem as a collection of expressions of boolean variables evaluating to TRUE or FALSE, an SAT solver can tell you if your boolean variables should be TRUE or FALSE for these conditions to be satisfied (or that there is no solution if that s the case). 

Most SAT solvers (including `varisat`) require that the problems be expressed in the "Conjunctive-Normal Form" or CNF. This means that the expression should consist of a collection of clauses ANDed together, each of them containing one or more literals ORed with each other. For example:

```
X1 AND (X2 OR X3) AND (X4 OR X5)
```


## Sudoku as an SAT problem statement

A Sudoku puzzle can be expressed as a set of boolean expressions with `9x9x9 = 729` boolean variables. Each variable denotes whether a specific cell on the board has a specific value. The rules of sudoku can be expressed using these boolean variables and given to an SAT solver to obtain a solution. The boolean variable coresponding to a value in a row and column can be written as: `row*9*9 + col*9 + value`.

For example, if the puzzle has a "3" in row 0, column 4, the corresponding boolean variable would be the one with index `0*9*9 + 4*9 + (3 - 1) = 38`. The expression has `(3-1)` since we are using zero-based indexing. `1` on the board will correspond to `0` in the expression and so on.

## Rules of Sudoku as SAT expressions

In the following sections, the boolean variables representing row `R`, column `C` and value `V` will be denoted as `X[R,C,V]`. `R` and `C` both run from `0-8` and `V` goes from `1-9`

### 1. Each row has all numbers from 1..9 exactly once

Pseudo-code:
```
let formula = TRUE
for r in 0..9
{
    for v in 1..10
    {
        clause = X[r,0,v] OR X[r,1,v] ... OR X[r,8,v]
    }
    formula = formula AND clause
}
```

The corresponding Rust code using `varisat` is given below. The `iproduct` macro from the [`itertools`](https://crates.io/crates/itertools) crate is used here to simplify the iterations.

```rust
use varisat::Lit;
use itertools::iproduct;

// Initialize new instance of `Solver`
let mut solver = Solver::new();

for (row, value) in iproduct!(0..9, 0..9)
{
    let mut literals: Vec<Lit> = Vec::new();
    for col in 0..9 
    {
        literals.push(lit_from_value(row, col, value));
    }
    solver.add_clause(&literals);
}
```

### 2. Each column has all numbers from 1..9 exactly once

Pseudo-code:
```
let formula = TRUE
for c in 0..9
{
    for v in 1..10
    {
        clause = X[0,c,v] OR X[1,c,v] ... OR X[8,c,v]
    }
    formula = formula AND clause
}
```


### 3. Each "box" has all numbers from 1..9 exactly once

The logic here is a little more complicated than the last two as it involves iterating over "boxes" on the board rather than rows and columns.

Pseudo-code:
```
let formula = TRUE
for v in 1..10
{
    for box in boxes[0-9]
    {
        clause = FALSE
        for cell_row, cell_col in box
        {
            clause = clause OR X[cell_row,cell_col,v]
        }
        formula = formula AND clause
    }
}
```

### 4. Each cell should only hold one number

With just the first three rules, the SAT solver will give a solution where all the numbers are  in single cells within each "box" on the board. To avoid this, an additional constraint needs to be added that says that each cell can only have one number set to TRUE at any time.