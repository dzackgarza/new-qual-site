---
schema: qual/card@1
id: E-KKI5A
kind: problem
title: The countable chain of tangent circles
classification:
  areas:
  - topology
  topics:
  - Fundamental Group
relations: []
review: draft
---

::: {.exercise}

Let $S_n$ be the circle of radius $n$ in $\mathbb{R}^2$ whose center is at the point $(n, 0)$.
Let $Y$ be the subspace of $\mathbb{R}^2$ that is the union of these circles; let $p$ be their common point.

(a) Show that $Y$ is not homeomorphic to a countably infinite wedge $X$ of circles, nor to the space of Example 1.

(b) Show, however, that $\pi_1(Y, p)$ is a free group with $\ts{[f_n]}$ as a system of free generators, where $f_n$ is a loop representing a generator of $\pi_1(S_n, p)$.
:::

::: {.solution}
Let \(p=(0,0)\). The circle \(S_n\) has equation
\[
x^2+y^2=2nx.
\]

(a) The countably infinite wedge \(\bigvee_{n\ge1}S^1\), with the wedge topology, is not first countable at its wedge point (Exercise 4 of this section). The space \(Y\subset\mathbb R^2\) is metrizable, hence first countable. Therefore these spaces are not homeomorphic.

Example 1 of the section is the infinite earring formed by circles of radius \(1/n\). That space is bounded and closed in \(\mathbb R^2\), hence compact. By contrast, \(Y\) is unbounded: \((2n,0)\in S_n\) for every \(n\). Thus \(Y\) is not compact and cannot be homeomorphic to the infinite earring.

(b) For \(N\ge1\), put
\[
Y_N=S_1\cup\cdots\cup S_N.
\]
This is a finite wedge of circles, so
\[
\pi_1(Y_N,p)\cong F(f_1,\dots,f_N).
\]
The inclusions \(Y_N\hookrightarrow Y_{N+1}\) send these generators to the corresponding generators.

We claim every loop in \(Y\) is homotopic rel basepoint to a loop in some \(Y_N\). Let \(g:I\to Y\) be a loop. Its image is compact, hence bounded; choose \(R>0\) with
\[
g(I)\subset B_R(p).
\]
Choose \(N>R\). For \(n>N\), the intersection \(S_n\cap B_R(p)\) is a proper arc-neighborhood of \(p\) in \(S_n\), hence contractible to \(p\) within \(S_n\cap B_R(p)\). Indeed, on \(S_n\) the radial distance \(r\) from \(p\) satisfies \(r=2n\cos\theta\), so the condition \(r<R< n\) cuts out only the two short branches meeting at \(p\), together forming an arc.

Consequently each excursion of \(g\) into \(S_n-\{p\}\) for \(n>N\) can be contracted to \(p\). These contractions can be performed simultaneously. To check continuity at an accumulation time of excursions, use uniform continuity of \(g\): the parameter intervals of any infinite family of pairwise disjoint excursions have lengths tending to zero, hence the diameters of their images tend to zero; choose the arc contractions so that the distance to \(p\) never increases. Thus the resulting homotopy is continuous and produces a loop with image in \(Y_N\).

It follows that
\[
\pi_1(Y,p)=\bigcup_{N\ge1}\operatorname{im}\bigl(\pi_1(Y_N,p)\to\pi_1(Y,p)\bigr).
\]
It remains to see that no new relations appear. For each \(N\), define a retraction
\[
r_N:Y\to Y_N
\]
by the identity on \(Y_N\) and by sending every circle \(S_n\), \(n>N\), to \(p\). This is continuous: away from \(p\) only one circle is locally present, while at \(p\), every neighborhood of \(p\) in \(Y_N\) has preimage equal to that neighborhood together with all collapsed circles, hence contains a neighborhood of \(p\) in \(Y\). Therefore the inclusion-induced map
\[
\pi_1(Y_N,p)\to\pi_1(Y,p)
\]
is injective, since \((r_N)_*\) is a left inverse.

Hence \(\pi_1(Y,p)\) is the increasing union
\[
F(f_1)\subset F(f_1,f_2)\subset\cdots,
\]
which is the free group on the countable set \(\{[f_n]:n\ge1\}\). Thus
\[
\boxed{\pi_1(Y,p)\cong F([f_1],[f_2],\dots).}
\]
:::
