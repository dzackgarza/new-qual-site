---
schema: qual/card@1
id: P-APAS20G
kind: problem
title: Haar average of a unitary representation is projection onto invariants
classification:
  areas:
  - applied-algebra
  topics:
  - Representation Theory
  - Inner Product Spaces
relations: []
review: draft
---

::: {.problem}
Let $(H,U)$ be a unitary representation of a compact group $G$.
Show that the operator
\[
P=\int_G U(g)\,dg
\]
is the orthogonal projection of $H$ onto the space of $G$-invariants in $H$.
:::

::: {.solution}
Normalize Haar measure so that \(\int_G dg=1\). For \(v\in H\), set
\[
Pv=\int_G U(g)v\,dg.
\]
For any \(h\in G\), left invariance of Haar measure gives
\[
U(h)Pv=\int_G U(hg)v\,dg=\int_G U(g)v\,dg=Pv.
\]
Thus \(Pv\) is \(G\)-invariant, so
\[
\operatorname{im}P\subseteq H^G.
\]
Conversely, if \(v\in H^G\), then \(U(g)v=v\) for every \(g\), and therefore
\[
Pv=\int_G v\,dg=v.
\]
Hence \(\operatorname{im}P=H^G\), and \(P\) acts as the identity on its image. In particular,
\[
P^2=P.
\]

It remains to prove orthogonality. Since \(U\) is unitary,
\[
U(g)^*=U(g)^{-1}=U(g^{-1}).
\]
Therefore, using invariance of Haar measure under inversion,
\[
P^*=\int_G U(g)^*\,dg
=\int_G U(g^{-1})\,dg
=\int_G U(g)\,dg=P.
\]
Thus \(P\) is a self-adjoint idempotent whose image is exactly \(H^G\). Hence \(P\) is the orthogonal projection of \(H\) onto the subspace of \(G\)-invariant vectors.
:::
