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

Maschke decomposes finite complex representations into irreducibles; Schur determines the Hom and End spaces between irreducibles.

[[D-FHUV5]]

## Maschke

[[T-PIO2B]]

:::{.remark title="Statement, hypotheses, and proof"}
Maschke says every representation of a finite $G$ over a field of characteristic not dividing $\size G$ is a direct sum of irreducibles.
Thus $\CC[G]$ is semisimple, and a finite-dimensional complex representation is determined up to isomorphism by its irreducible multiplicities.

Both hypotheses are load-bearing.
Over $\FF_p$ with $p \divides \size G$ it fails: the regular representation of $\ZZ/p$ over $\FF_p$ is indecomposable but not irreducible.
For infinite $G$ it can fail as well; integral and modular representation theory therefore require non-semisimple methods.

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

Conjugate elements of $G$ act by similar matrices, so characters are class functions. For irreducibles over $\CC$, Schur gives
$\dim \Hom_G(V,W)=0$ for $V\not\cong W$ and $\dim \End_G(V)=1$; together with Maschke, this is the input to the character orthogonality and multiplicity formulas.

:::

## What they give together

$\CC[G] \cong \bigoplus_i \End(V_i) \cong \bigoplus_i \Mat_{d_i}(\CC)$ over the irreducibles $V_i$, so
\[
\size G = \sum_i d_i^2
,\]
and the number of irreducibles equals the number of conjugacy classes.
Those two facts determine the degrees outright for small groups, which is how a character table is started.
