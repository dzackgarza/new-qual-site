---
schema: qual/card@1
id: L-Y5KNM
kind: lemma
title: The minimal polynomial is the invariant factor of highest degree
classification:
  areas:
  - algebra
  topics:
  - Minimal and Characteristic Polynomials
  - Structure Theorem
  - Canonical Forms
relations: []
review: draft
---

::: {.lemma}
Let $k$ be a field, let $A\in\Mat_n(k)$, and let $f_1\divides f_2\divides\cdots\divides f_n$ be the invariant factors of $A$: the monic diagonal entries of the Smith normal form of $xI-A$ over $k[x]$.
Then the [[D-GK5SF|minimal polynomial]] of $A$ is
$$
\min_A(x)=f_n(x).
$$
:::

::: {.proof}
With $x$ acting as $A$, the $k[x]$-module $k^n$ is isomorphic to $\bigoplus_{j=1}^nk[x]/(f_j)$.
A polynomial $g$ satisfies $g(A)=0$ if and only if $g$ annihilates this module, that is, $f_j\divides g$ for every $j$; since $f_j\divides f_n$ for all $j$, this holds if and only if $f_n\divides g$.
So $f_n$ is the monic generator of the ideal of polynomials vanishing at $A$.
:::
