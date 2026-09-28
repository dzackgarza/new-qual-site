---
schema: qual/card@1
id: P-APA24G
kind: problem
title: Averaging operator is the orthogonal projection onto $G$-invariants
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
Let $(V, \varphi)$ be a finite-dimensional unitary representation of a finite group $G$.
State the definition of the space $V^G$ of $G$-invariant vectors in $V$, and prove that
\[
P = \frac{1}{|G|} \sum_{g \in G} \varphi(g)
\]
is the orthogonal projection of $V$ onto $V^G$.
:::

::: {.solution}
The invariant subspace is
\[
V^G:=\{v\in V:\varphi(g)v=v\text{ for every }g\in G\}.
\]
Define
\[
P:=\frac1{|G|}\sum_{g\in G}\varphi(g).
\]

<1>1. The image of \(P\) is contained in \(V^G\).
::: {.proof}
Let \(v\in V\) and \(h\in G\). Then
\[
\varphi(h)Pv
=\frac1{|G|}\sum_{g\in G}\varphi(hg)v.
\]
As \(g\) runs through \(G\), so does \(hg\). Hence
\[
\varphi(h)Pv
=\frac1{|G|}\sum_{k\in G}\varphi(k)v
=Pv.
\]
Thus \(Pv\in V^G\).
:::

<1>2. The operator \(P\) acts as the identity on \(V^G\).
::: {.proof}
If \(v\in V^G\), then \(\varphi(g)v=v\) for every \(g\in G\). Therefore
\[
Pv=\frac1{|G|}\sum_{g\in G}v=v.
\]
:::

<1>3. Consequently \(P^2=P\) and \(\operatorname{im}P=V^G\).
::: {.proof}
By <1>1, \(Pv\in V^G\) for every \(v\), and by <1>2, \(P\) is the identity on \(V^G\). Hence
\[
P^2v=P(Pv)=Pv.
\]
Thus \(P^2=P\). Also <1>1 gives \(\operatorname{im}P\subseteq V^G\), while <1>2 gives \(V^G\subseteq\operatorname{im}P\), because \(v=Pv\) for every invariant \(v\).
:::

<1>4. The operator \(P\) is self-adjoint.
::: {.proof}
Because the representation is unitary,
\[
\varphi(g)^*=\varphi(g)^{-1}=\varphi(g^{-1}).
\]
Therefore
\[
P^*
=\frac1{|G|}\sum_{g\in G}\varphi(g)^*
=\frac1{|G|}\sum_{g\in G}\varphi(g^{-1}).
\]
Inversion permutes the elements of \(G\), so the final sum equals \(P\).
:::

<1>5. Hence \(P\) is the orthogonal projection of \(V\) onto \(V^G\).
::: {.proof}
By <1>3, \(P\) is an idempotent with image \(V^G\), and by <1>4 it is self-adjoint. A self-adjoint idempotent is the orthogonal projection onto its image. Explicitly, if \(u=Px\in\operatorname{im}P\) and \(w\in\ker P\), then
\[
\langle u,w\rangle
=\langle Px,w\rangle
=\langle x,Pw\rangle
=0.
\]
Thus \(\operatorname{im}P\perp\ker P\), so \(P\) is precisely the orthogonal projection onto \(V^G\).
:::
:::
