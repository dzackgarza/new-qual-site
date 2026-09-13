---
schema: qual/card@1
id: P-AGH276RRPROBLEM
kind: problem
title: The Riemann-Roch problem for multiples of a divisor
classification:
  areas:
  - algebraic-geometry
  topics:
  - Linear Systems
  - Hilbert Polynomials
  - Ample Divisors
relations: []
review: draft
---

::: problem
Let $X$ be a nonsingular projective variety over an algebraically closed field, and let $D$ be a divisor on $X$.
For any $n > 0$ consider the complete linear system $\abs{nD}$.
The **Riemann-Roch problem** is to determine $\dim \abs{nD}$ as a function of $n$, and in particular its behavior for large $n$.

If $\mcl$ is the corresponding invertible sheaf, then $\dim \abs{nD} = \dim \Gamma(X, \mcl^n) - 1$, so an equivalent problem is to determine $\dim \Gamma(X, \mcl^n)$ as a function of $n$.

a. Show that if $D$ is very ample, and if $X \injects \PP^n_k$ is the corresponding embedding in projective space, then for all sufficiently large $n$ we have $\dim \abs{nD} = P_X(n) - 1$, where $P_X$ is the Hilbert polynomial of $X$.
Thus in this case $\dim \abs{nD}$ is a polynomial function of $n$ for $n$ large.

b. If $D$ corresponds to a torsion element of $\Pic X$ of order $r$, then $\dim \abs{nD} = 0$ if $r \divides n$ and $-1$ otherwise.
In this case the function is periodic of period $r$.

It follows from the general Riemann-Roch theorem that $\dim \abs{nD}$ is a polynomial function for $n$ large whenever $D$ is an ample divisor.
In the case of algebraic surfaces, Zariski has shown for any effective divisor $D$ that there is a finite set of polynomials $P_1, \ldots, P_r$ such that for all sufficiently large $n$, $\dim \abs{nD} = P_{i(n)}(n)$, where $i(n) \in \ts{1, \ldots, r}$ is a function of $n$.
:::
