---
schema: qual/card@1
id: P-APAS24G
kind: problem
title: Averaging projector onto the $G$-invariant subspace
classification:
  areas:
  - applied-algebra
  topics:
  - Representation Theory
  - Inner Product Spaces
relations: []
review: draft
---

::: problem
Let $(V,\varphi)$ be a finite-dimensional unitary representation of a finite group $G$.
State the definition of the space $V^G$ of $G$-invariant vectors in $V$, and prove that
\[
P=\frac{1}{|G|}\sum_{g\in G}\varphi(g)
\]
is the orthogonal projection of $V$ onto $V^G$.
:::

::: solution
The invariant subspace is
\[
V^G=\{v\in V:\varphi(g)v=v\text{ for every }g\in G\}.
\]
Set
\[
P=\frac1{|G|}\sum_{g\in G}\varphi(g).
\]
For every $h\in G$,
\[
\varphi(h)P
=\frac1{|G|}\sum_{g\in G}\varphi(hg)
=P,
\]
because $g\mapsto hg$ permutes $G$. Therefore $Pv\in V^G$ for every $v$, so
\[
\operatorname{im}P\subseteq V^G.
\]
Conversely, if $v\in V^G$, then
\[
Pv=\frac1{|G|}\sum_{g\in G}v=v.
\]
Thus
\[
\operatorname{im}P=V^G
\]
and $P^2=P$.

It remains to show orthogonality. Since the representation is unitary,
\[
\varphi(g)^*=\varphi(g^{-1}).
\]
Hence
\[
P^*
=\frac1{|G|}\sum_{g\in G}\varphi(g^{-1})
=P,
\]
because inversion permutes $G$. Thus $P$ is a self-adjoint idempotent, hence the orthogonal projection onto its image. Therefore
\[
\boxed{P\text{ is the orthogonal projection of }V\text{ onto }V^G.}
\]
:::
