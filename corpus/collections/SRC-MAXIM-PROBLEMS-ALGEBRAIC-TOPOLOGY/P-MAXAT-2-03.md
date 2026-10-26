---
schema: qual/card@1
id: P-MAXAT-2-03
kind: problem
title: Maxim algebraic topology 2.3
classification:
  areas: [topology]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against section 2, problem 3 of the retained Laurentiu Maxim Problems in Algebraic Topology PDF.
---

::: {.problem}
Show that $V _ { n } ( \mathbb { R } ^ { \infty } ) , V _ { n } ( \mathbb { C } ^ { \infty } ) , V _ { n } ( \mathbb { H } ^ { \infty } )$ are contractible.
:::

Let $\mathbb F$ denote any of $\mathbb R,\mathbb C,\mathbb H$, and write
\[
V_n(\mathbb F^m)
\]
for the Stiefel manifold of orthonormal $n$-frames in $\mathbb F^m$. The infinite Stiefel manifold is the direct limit
\[
V_n(\mathbb F^\infty)=\bigcup_{m\geq n}V_n(\mathbb F^m)
\]
under the standard coordinate inclusions.

::: pf

::: pf-step

There is a fiber bundle
\[
S^{d(m-n+1)-1}
\longrightarrow V_n(\mathbb F^m)
\longrightarrow V_{n-1}(\mathbb F^m),
\]
where
\[
d=\dim_{\mathbb R}\mathbb F\in\{1,2,4\}.
\]


::: pf-proof

Send an orthonormal $n$-frame $(v_1,\ldots,v_n)$ to its first $n-1$ vectors. Over a fixed $(n-1)$-frame, the last vector may be any unit vector in the orthogonal complement of its span. That complement has $\mathbb F$-dimension $m-n+1$, hence real dimension $d(m-n+1)$, and its unit sphere is $S^{d(m-n+1)-1}$. Local orthonormal trivializations give the bundle structure.

:::

:::

::: pf-step

For each fixed $n$ and $k\geq0$, there exists $m_0$ such that
\[
\pi_k(V_n(\mathbb F^m))=0
\qquad(m\geq m_0).
\]


::: pf-proof

Induct on $n$. For $n=1$,
\[
V_1(\mathbb F^m)=S^{dm-1},
\]
whose $\pi_k$ vanishes when $dm-1>k$. For the induction step, use the long exact homotopy sequence of the bundle in step <1>1. For sufficiently large $m$, the fiber sphere has dimension greater than $k+1$, so both $\pi_k$ and $\pi_{k-1}$ of the fiber vanish. By the induction hypothesis, $\pi_k(V_{n-1}(\mathbb F^m))=0$ for sufficiently large $m$. Exactness then gives $\pi_k(V_n(\mathbb F^m))=0$.

:::

:::

::: pf-step

Every continuous map from a compact space into $V_n(\mathbb F^\infty)$ has image contained in some finite stage $V_n(\mathbb F^m)$.


::: pf-proof

The direct limit is taken with the weak topology of the nested finite-dimensional Stiefel manifolds. A compact subset of this CW-type direct limit meets only finitely many cells, hence lies in a finite stage. In particular, the compact image of a sphere or disk is contained in some $V_n(\mathbb F^m)$.

:::

:::

::: pf-step

Therefore
\[
\pi_k(V_n(\mathbb F^\infty))=0
\qquad\text{for every }k\geq0.
\]


::: pf-proof

Let $f:S^k\to V_n(\mathbb F^\infty)$. By step <1>3 its image lies in some finite stage $V_n(\mathbb F^m)$. Enlarge $m$ if necessary until step <1>2 applies. The composite of $f$ with this larger-stage inclusion is null-homotopic there, hence null-homotopic in the direct limit. Thus every homotopy class vanishes. The case $k=0$ also shows path connectedness.

:::

:::

::: pf-step

The space $V_n(\mathbb F^\infty)$ has the homotopy type of a CW complex.


::: pf-proof

Each finite Stiefel manifold admits a CW structure compatible, after subdivision if necessary, with the standard inclusions, and their direct limit is a CW-type space. Equivalently, the infinite Stiefel manifold is the total space of the standard universal principal classical-group bundle and has CW type.

:::

:::

::: pf-step

Hence $V_n(\mathbb F^\infty)$ is contractible.


::: pf-proof

By step <1>4 all homotopy groups vanish, and by step <1>5 the space has CW type. The map to a point is therefore a weak homotopy equivalence, so Whitehead's theorem makes it a homotopy equivalence. Thus the space is contractible.

:::

:::

::: pf-step

Applying step <1>6 to $\mathbb F=\mathbb R,\mathbb C,\mathbb H$ gives
\[
\boxed{
V_n(\mathbb R^\infty),\quad
V_n(\mathbb C^\infty),\quad
V_n(\mathbb H^\infty)
\text{ are contractible}.}
\]


::: pf-proof

The proof used only the real dimension $d=1,2,4$ of the scalar division algebra, so it applies uniformly to all three cases.

:::

:::

::: pf-qed

Step <1>7 is the required conclusion.

:::

:::
