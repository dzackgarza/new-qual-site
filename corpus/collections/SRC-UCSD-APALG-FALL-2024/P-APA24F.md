---
schema: qual/card@1
id: P-APA24F
kind: problem
title: A unitary representation is irreducible iff every nonzero vector is cyclic
classification:
  areas:
  - applied-algebra
  topics:
  - Representation Theory
relations: []
review: draft
---

::: problem
Let $(V, \varphi)$ be a finite-dimensional unitary representation of a finite group $G$.
A vector $v \in V$ is said to be cyclic if $\{\varphi(g)v : g \in G\}$ spans $V$.
Prove that $(V, \varphi)$ is irreducible if and only if every nonzero vector in $V$ is cyclic.
:::

::: {.solution}
For \(v\in V\), define its cyclic subspace
\[
W_v:=\operatorname{span}\{\varphi(g)v:g\in G\}.
\]

<1>1. For every \(v\in V\), the subspace \(W_v\) is \(G\)-invariant.
::: {.proof}
If \(h\in G\), then for each generator \(\varphi(g)v\) of \(W_v\),
\[
\varphi(h)\varphi(g)v=\varphi(hg)v\in W_v.
\]
Hence \(\varphi(h)W_v\subseteq W_v\) for every \(h\in G\), so \(W_v\) is \(G\)-invariant.
:::

<1>2. If \(V\) is irreducible, then every nonzero \(v\in V\) is cyclic.
::: {.proof}
Let \(0\ne v\in V\). Then \(v=\varphi(e)v\in W_v\), so \(W_v\ne0\). By <1>1, \(W_v\) is \(G\)-invariant. Irreducibility therefore forces
\[
W_v=V.
\]
Thus the orbit of \(v\) spans \(V\), so \(v\) is cyclic.
:::

<1>3. Conversely, if every nonzero vector is cyclic, then \(V\) is irreducible.
::: {.proof}
Let \(0\ne W\subseteq V\) be a \(G\)-invariant subspace. Choose \(0\ne v\in W\). Since \(W\) is invariant,
\[
\varphi(g)v\in W
\qquad(g\in G),
\]
so \(W_v\subseteq W\). By hypothesis, \(v\) is cyclic, hence \(W_v=V\). Therefore
\[
V=W_v\subseteq W\subseteq V,
\]
so \(W=V\). Thus \(V\) has no nonzero proper invariant subspace and is irreducible.
:::

<1>4. Hence \((V,\varphi)\) is irreducible if and only if every nonzero vector in \(V\) is cyclic.
::: {.proof}
Combine <1>2 and <1>3.
:::
:::
