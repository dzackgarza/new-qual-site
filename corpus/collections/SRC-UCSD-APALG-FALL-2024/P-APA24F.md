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

::: {.problem}
Let $(V, \varphi)$ be a finite-dimensional unitary representation of a finite group $G$.
A vector $v \in V$ is said to be cyclic if $\{\varphi(g)v : g \in G\}$ spans $V$.
Prove that $(V, \varphi)$ is irreducible if and only if every nonzero vector in $V$ is cyclic.
:::

::: {.solution}

For \(v\in V\), define its cyclic subspace
\[
W_v:=\operatorname{span}\{\varphi(g)v:g\in G\}.
\]

::: pf

::: {.pf-step #wv-is-invariant}
For every \(v\in V\), the subspace \(W_v\) is \(G\)-invariant.

::: pf-proof
If \(h\in G\), then for each generator \(\varphi(g)v\) of \(W_v\),
\[
\varphi(h)\varphi(g)v=\varphi(hg)v\in W_v.
\]
Hence \(\varphi(h)W_v\subseteq W_v\) for every \(h\in G\), so \(W_v\) is \(G\)-invariant.
:::

:::

::: {.pf-step #irreducible-implies-cyclic}
If \(V\) is irreducible, then every nonzero \(v\in V\) is cyclic.

::: pf-proof
Let \(0\ne v\in V\). Then \(v=\varphi(e)v\in W_v\), so \(W_v\ne0\). By step [](#wv-is-invariant){.pf-ref}, \(W_v\) is \(G\)-invariant. Irreducibility therefore forces
\[
W_v=V.
\]
Thus the orbit of \(v\) spans \(V\), so \(v\) is cyclic.
:::

:::

::: {.pf-step #cyclic-implies-irreducible}
Conversely, if every nonzero vector is cyclic, then \(V\) is irreducible.

::: pf-proof
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

:::

::: pf-step
Hence \((V,\varphi)\) is irreducible if and only if every nonzero vector in \(V\) is cyclic.

::: pf-proof
Combine steps [](#irreducible-implies-cyclic){.pf-ref} and [](#cyclic-implies-irreducible){.pf-ref}.
:::

:::

:::

:::
