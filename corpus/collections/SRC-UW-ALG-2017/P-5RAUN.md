---
schema: qual/card@1
id: P-5RAUN
kind: problem
title: A finite simple group has no 2-dimensional irreducible complex representation
classification:
  areas:
  - algebra
  topics:
  - Groups
  - Representation Theory
relations: []
review: draft
audit:
- event: solution-written
  by: OpenAI
  date: 2026-09-10
---

::: {.problem}
Show that a finite simple group cannot have a 2-dimensional irreducible representation over $\mathbb C$.

> Hint: the determinant might prove useful.
:::


::: {.solution}
Suppose, for contradiction, that \(G\) is finite simple and that
\[
\rho:G\longrightarrow \GL(V),\qquad \dim_{\mathbb C}V=2,
\]
is irreducible.

First, \(
ho\) is faithful. Indeed, \(\ker\rho\trianglelefteq G\). Since \(G\) is simple, \(\ker\rho\) is either \(1\) or \(G\). The latter would make the representation trivial, hence reducible in dimension \(2\). Thus \(\ker\rho=1\).

Consider
\[
\det\rho:G\longrightarrow \mathbb C^\times.
\]
Its kernel is normal. If its kernel were trivial, then \(G\) would embed in the abelian group \(\mathbb C^\times\), so \(G\) would be abelian. A finite simple abelian group is cyclic of prime order, and every irreducible complex representation of an abelian group is \(1\)-dimensional, a contradiction. Hence
\[
\det\rho(g)=1\qquad\text{for every }g\in G.
\]
Thus \(
ho(G)\subseteq \SL_2(\mathbb C)\).

We now justify that \(2\mid |G|\). We use the standard character-degree divisibility argument, included here for completeness. Let \(\chi\) be an irreducible complex character of degree \(d=\chi(1)\). For each conjugacy class \(C\) with representative \(c\), the class sum
\[
z_C=\sum_{g\in C}g\in Z(\mathbb Z[G])
\]
acts on the irreducible representation by the scalar
\[
\omega_C=\frac{|C|\chi(c)}{d}.
\]
Because multiplication by \(z_C\) is an integral endomorphism of the finite free abelian group \(Z(\mathbb Z[G])\), Cayley--Hamilton shows that \(\omega_C\) is an algebraic integer. Character values are algebraic integers as well. Character orthogonality gives
\[
|G|=\sum_{g\in G}\chi(g)\chi(g^{-1})
=d^2+\sum_{C\ne\{1\}}|C|\chi(c)\chi(c^{-1}).
\]
Dividing by \(d\),
\[
\frac{|G|}{d}
=d+\sum_{C\ne\{1\}}\omega_C\chi(c^{-1}).
\]
The right side is an algebraic integer, while the left side is rational; hence \(|G|/d\in\mathbb Z\). Therefore \(d\mid |G|\). Applying this with \(d=2\) gives \(2\mid |G|\).

By Cauchy's theorem, \(G\) has an element \(t\) of order \(2\). Since
\[
\rho(t)^2=I,
\]
the matrix \(
ho(t)\) is diagonalizable with eigenvalues in \(\{1,-1\}\). Also
\[
\det\rho(t)=1.
\]
Therefore its two eigenvalues are either both \(1\) or both \(-1\). Faithfulness excludes \(
ho(t)=I\), because \(t\ne1\). Hence
\[
\rho(t)=-I.
\]
But \(-I\) is central in \(
ho(G)\). Since \(
ho\) is faithful, \(t\in Z(G)\). Thus \(Z(G)\ne1\). Simplicity forces \(Z(G)=G\), so \(G\) is abelian, again contradicting the existence of a \(2\)-dimensional irreducible complex representation.

Hence a finite simple group has no \(2\)-dimensional irreducible complex representation.
:::
