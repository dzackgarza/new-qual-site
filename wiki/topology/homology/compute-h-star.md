---
title: Compute $H_*$
order: 0
problems:
  topics:
  - Homology
  - Mayer-Vietoris
  - Simplicial Homology
  - Relative Homology

---

# Compute $H_*$

Three methods, and again the presentation of the space decides.

## 1. Does it have a CW structure?

**Cellular homology.**
The chain groups are free on the cells, $C_n = \ZZ^{\#\text{n-cells}}$, and the boundary maps are computed by degree: the coefficient of a $(n-1)$-cell in $\partial$ of an $n\dash$cell is the degree of the composite attaching map onto that cell's quotient sphere.

This is the method for anything built from a polygon or given by a cell structure, and it is usually the fastest, since the chain complex is finite and small.
Two shortcuts that follow immediately:

- no cells in adjacent dimensions means every boundary map is zero, so $H_n$ is free on the $n\dash$cells -- this is why $\CP^n$ has homology $\ZZ$ in every even degree;
- $H_n = 0$ above the top cell dimension, and $H_0 = \ZZ$ for a connected space.

## 2. Does it split into two pieces?

**Mayer--Vietoris.**
For $X = A\union B$ with interiors covering,
\[
\cdots \to H_n(A\intersect B) \to H_n(A)\oplus H_n(B)\to H_n(X)\to H_{n-1}(A\intersect B)\to\cdots
.\]

The same decompositions that work for van Kampen work here, and this is the method when the space is a union rather than a cell complex: a sphere as two discs, a connected sum along a separating sphere, a torus as two cylinders.

## 3. Is it a pair, or a quotient?

**The long exact sequence of a pair**, together with $H_n(X, A)\cong \tilde H_n(X/A)$ for good pairs.
This is the method for a quotient: compute the pair instead, and read the quotient's reduced homology off the relative groups.

## Choosing between them

| The space is given as | Use |
| --- | --- |
| a cell complex, or a polygon with identifications | cellular |
| a union of two understood pieces | Mayer--Vietoris |
| a quotient $X/A$, or a pair | the long exact sequence |
| a product | Künneth |
| a covering space | transfer, or compute the base directly |

## Checks that catch errors

- $H_0 = \ZZ^{\#\text{components}}$, always.
- $H_1$ is the abelianization of $\pi_1$, so it can be checked against [[topology/fundamental-group/compute-pi-1|a fundamental group computation]].
- Euler characteristic: $\sum (-1)^n \rank H_n = \sum (-1)^n \#\ts{n\text{-cells}}$, computable two ways, and disagreement means an arithmetic slip.
- For a closed orientable $n\dash$manifold, $H_n = \ZZ$; for a closed non-orientable one, $H_n = 0$ and there is $\ZZ/2$ torsion in $H_{n-1}$.
  That last pair distinguishes the torus from the Klein bottle immediately.
