---
schema: qual/card@1
id: E-1XT8N
kind: problem
title: Continuity of the affine map in the uniform topology
classification:
  areas:
  - topology
  topics:
  - Continuous Functions
  - Metric Spaces
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Read against Munkres, Topology (2000), §20 Exercise 7, printed p. 127, referring to
    Exercise 8 of §19, with the uniform metric of printed p. 124; the stored statement is
    the printed one.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: "positron0802", "Solutions to Topology,
    Chapter 2" (1 January 2021), Exercise 20.7, PDF pp. 19-20. The uniform distance between
    the images is sup min{a_i |x_i - y_i|, 1}: bounded coefficients make the map continuous,
    an unbounded coefficient sequence destroys continuity at the origin by stretching a
    small constant sequence to uniform distance 1, and the two conditions on a_i and 1/a_i
    give the answer for the map and for its inverse. (tmp/sources/munkres-solutions-
    positron-ch2.pdf).
---

::: {.exercise}

Consider the map $h: \RR^\omega \to \RR^\omega$ defined in Exercise 8 of §19; give $\RR^\omega$ the uniform topology.
Under what conditions on the numbers $a_i$ and $b_i$ is $h$ continuous?
a homeomorphism?
:::

::: {.solution}
The complete published solution is **"positron0802", *Solutions to Topology, Chapter 2* (1 January 2021), Exercise 20.7, PDF pp. 19--20** (`tmp/sources/munkres-solutions-positron-ch2.pdf`); all three answers are theirs.

Recall $h(\mathbf{x})=(a_{1}x_{1}+b_{1},a_{2}x_{2}+b_{2},\dots)$ with $a_{i}>0$, so that $h$ is a bijection with $h^{-1}(\mathbf{y})=((y_{1}-b_{1})/a_{1},(y_{2}-b_{2})/a_{2},\dots)$, and that
$$
\bar\rho(h(\mathbf{x}),h(\mathbf{y}))=\sup_{i}\min\{a_{i}\abs{x_{i}-y_{i}},1\}.
$$

*If $(a_{i})$ is bounded, say $a_{i}\le M$, then $h$ is continuous.* Let $\mathbf{x}\in\RR^{\omega}$ and $\varepsilon>0$; put
$$
\delta=\min\big\{\varepsilon/M,\ 1/M\big\}>0,\qquad U=B_{\bar\rho}(\mathbf{x},\delta).
$$
For $\mathbf{y}\in U$ we have $\min\{\abs{x_{i}-y_{i}},1\}<\delta$ for all $i$, hence $\abs{x_{i}-y_{i}}<\delta$ and
$$
\min\{a_{i}\abs{x_{i}-y_{i}},1\}\le a_{i}\abs{x_{i}-y_{i}}<M\delta\le\varepsilon
$$
for all $i$, so $\bar\rho(h(\mathbf{x}),h(\mathbf{y}))<\varepsilon$. Hence $h(U)\subset B_{\bar\rho}(h(\mathbf{x}),\varepsilon)$ and $h$ is continuous.

*If $(a_{i})$ is unbounded, $h$ is not continuous at $\mathbf{0}$.* Take $0<\varepsilon<1$ and $V=B_{\bar\rho}(h(\mathbf{0}),\varepsilon)$. Let $\delta>0$ and pick $0<r<\delta$; the sequence $\mathbf{y}=(r,r,\dots)$ satisfies $\bar\rho(\mathbf{0},\mathbf{y})=r<\delta$. Since $(a_{i})$ is unbounded there is $N$ with $a_{N}r>1$, and then $\min\{a_{N}r,1\}=1$, so $\bar\rho(h(\mathbf{0}),h(\mathbf{y}))=\sup_{i}\min\{a_{i}r,1\}=1\not<\varepsilon$. Hence $h$ maps no ball at $\mathbf{0}$ into $V$.

*The same two arguments applied to $h^{-1}$, whose coordinate coefficients are $1/a_{i}>0$, show that $h^{-1}$ is continuous exactly when $(1/a_{i})$ is bounded*; note $b_{i}$ plays no role, since a translation is a homeomorphism of the uniform topology (the case $a_{i}=1$ for all $i$ above).

**Answer.** $h$ is continuous exactly when $(a_{i})$ is bounded, and $h$ is a homeomorphism exactly when both $(a_{i})$ and $(1/a_{i})$ are bounded, that is when the $a_{i}$ are bounded above and bounded away from $0$.
:::
