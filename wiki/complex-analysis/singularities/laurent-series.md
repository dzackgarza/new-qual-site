---
title: Laurent series
order: 10
problems:
  topics:
  - Laurent Series
  - Principal Parts
  - Annuli
---

# Laurent series

A Taylor series expands a holomorphic function on a disc.
A Laurent series expands it on an annulus, and the price of the hole in the middle is the negative powers.

[[T-4XPWL]]

[[C-7S2CO]]

## The expansion belongs to the annulus, not to the function

This is the point that most often goes wrong.
A function has one Taylor series about a point, but *several* Laurent series, one for each annulus on which it is holomorphic, and they are genuinely different series.

:::{.example title="One function, two expansions"}
Take $f(z) = {1 \over z-1}$, holomorphic away from $z=1$, and expand about $z=0$.

On $\abs z < 1$, write it as a geometric series in $z$:
\[
{1\over z-1} = -{1\over 1-z} = -\sum_{k\geq 0} z^k
.\]

On $\abs z > 1$, the same manipulation must be arranged so the ratio is small.
Factor out the large term:
\[
{1\over z-1} = {1\over z}\cdot{1 \over 1 - z\inv} = \sum_{k \geq 1} z^{-k}
.\]

Both converge, both equal $f$, and neither is wrong.
Which one a problem wants is decided by which annulus the point of interest lies in.

:::

## How to compute one

Almost never by the coefficient integral.
The integral formula defines $c_k$ and is used to prove things about it; a computation manipulates known series instead.

- **Factor to make a geometric series.** Arrange the expression as ${1 \over 1 - u}$ with $\abs u < 1$ *on the annulus you want*, then expand.
  Which of $z$ and $z\inv$ plays the role of $u$ is exactly the choice of annulus above.

- **Multiply or compose known expansions.** For $f = g\cdot h$ with $g$ having a pole and $h$ holomorphic, expand $h$ as a Taylor series and multiply through by the finite principal part of $g$.

- **Divide by the leading behaviour.** For $f$ with a pole of order $N$ at $z_0$, the function $(z-z_0)^N f(z)$ is holomorphic there, so expand *that* as a Taylor series and shift the indices back by $N$.

- **Partial fractions.** A rational function splits into terms with one pole each, and each term is expanded separately on the annulus in question.

## Residues and singularity type

- The coefficient $c_{-1}$ is the residue, which is what [[complex-analysis/residues-and-contours/the-residue-theorem|the residue theorem]] integrates.

- The pattern of negative terms is the classification on [[complex-analysis/singularities/classifying-a-singularity|Classifying a singularity]] -- none, finitely many, or infinitely many.

## Exercises

[[FF-UQZNR]]

[[FF-5GLOZ]]
