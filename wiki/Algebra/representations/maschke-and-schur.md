---
title: Maschke and Schur
order: 10
problems:
  topics:
  - Representation Theory
  - Group Rings
  - Convolution
  - Function Spaces
---

# Maschke and Schur

Two theorems, and between them they reduce every question about a complex representation of a finite group to linear algebra on the irreducibles.

[[D-FHUV5]]

## Maschke

[[T-PIO2B]]

:::{.remark title="What it buys, and what it costs"}
Maschke says every representation of a finite $G$ over a field of characteristic not dividing $\size G$ is a direct sum of irreducibles.
So $\CC[G]$ is semisimple and the category of representations is as simple as it could be: no extensions to compute, and a representation is determined by its multiplicities.

Both hypotheses are load-bearing.
Over $\FF_p$ with $p \divides \size G$ it fails: the regular representation of $\ZZ/p$ over $\FF_p$ is indecomposable but not irreducible.
For infinite $G$ it fails too, which is why the theory over $\ZZ$ or in characteristic $p$ is a different subject.

The proof is averaging: take any complement, average the projection onto it over $G$, and the result is $G\dash$equivariant.
Dividing by $\size G$ is where the characteristic hypothesis enters, and it is the only place.

:::

## Schur

[[T-YHH3M]]

:::{.remark title="The two statements"}
For irreducible $V, W$:

- a $G\dash$map $V\to W$ is either zero or an isomorphism;
- over $\CC$, a $G\dash$map $V\to V$ is a scalar.

The second needs algebraic closure, since it is proved by taking an eigenvalue: $f - \lambda I$ is a $G\dash$map with nontrivial kernel, hence zero.

Everything computational follows from this.
The centre of $\CC[G]$ acts on each irreducible by a scalar, which is what makes character values class functions; and $\Hom_G(V,W)$ has dimension $0$ or $1$, which is what makes the orthogonality relations orthogonality relations.

:::

## What they give together

$\CC[G] \cong \bigoplus_i \End(V_i) \cong \bigoplus_i \Mat_{d_i}(\CC)$ over the irreducibles $V_i$, so
\[
\size G = \sum_i d_i^2
,\]
and the number of irreducibles equals the number of conjugacy classes.
Those two facts determine the degrees outright for small groups, which is how a character table is started.
