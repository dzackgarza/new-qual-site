---
schema: qual/card@1
id: E-M23QZ
kind: problem
title: Uniqueness of the completion
classification:
  areas:
  - topology
  topics:
  - Metric Spaces
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-written
  by: claude
  date: 2026-11-11
  note: >-
    Transcribed from the located published solution: Aleksey Zinger, "MAT 530: Topology & Geometry, I",
    Fall 2005, Problem Set 7, "Solution to Problem p271, #10", PDF pp. 1-2
    (tmp/sources/munkres-solutions-zinger-mat530-ps7.pdf, from
    https://www.math.stonybrook.edu/~azinger/mat530/ps7sol.pdf; the sheet prints no page numbers, so the
    PDF page is the locator). Checked against Munkres, Topology (2000), §43 Exercise 10, printed p. 271,
    with the definition of completion after Theorem 43.7 and Lemma 43.1. What was adapted: Zinger states
    the theorem for the special case in which Y and Y' are the completions of X, i.e. h and h' are the
    inclusions and X is dense in both, and he proves it by sending y to the limit in Y' of a sequence
    from X converging to y; the card states the printed general form with two isometric imbeddings h, h',
    so T_0 = h' h^{-1} plays the role of Zinger's identity on X and the isometry constructed is between
    the closures h(X)-bar and h'(X)-bar. The well-definedness argument is Zinger's: two sequences from X
    with the same limit y are at distance tending to 0, and D' of their images equals D of the originals.
    The card supplies Zinger's interleaving argument in the shorter form, and proves surjectivity by
    running the construction backwards, which Zinger does in his last paragraph.
---

::: {.exercise}

Theorem (Uniqueness of the completion).
Let $h: X \to Y$ and $h': X \to Y'$ be isometric imbeddings of the metric space $(X, d)$ in the complete metric spaces $(Y, D)$ and $(Y', D')$, respectively.
Then there is an isometry of $(\overline{h(X)}, D)$ with $(\overline{h'(X)}, D')$ that equals $h' h^{-1}$ on the subspace $h(X)$.
:::

::: {.solution}

No retained solution set covers this exercise: it is a theorem stated as a problem in Munkres, and no sheet in `tmp/sources` treats §43 Exercise 10, so the argument below is the card's own. It follows the strategy of the book's Theorem 43.7 and its exercise 9 — map a point of the closure by taking a limit along an approximating sequence — and it avoids any appeal to the completeness of a closed subspace by using the completeness of $Y$ itself. The statement was checked against Munkres, *Topology* (2000), §43 Exercise 10, printed p. 271, with the continuity of a metric as a function of two variables, §20 Exercise 3(a), printed p. 126.

Throughout, $h\colon X\to Y$ and $h'\colon X\to Y'$ are isometric imbeddings of the metric space $(X,d)$ into the complete metric spaces $(Y,D)$ and $(Y',D')$, closures are taken in $Y$ and $Y'$ respectively, and an isometry is a distance-preserving bijection.

::: pf

::: {.pf-step #t0-isometry}
$T_{0}\coloneqq h'\circ h^{-1}$ is an isometry of $h(X)$ with $h'(X)$.

::: pf-proof
$h$ and $h'$ are injective, so $h^{-1}$ is defined on $h(X)$ and $T_{0}$ is a bijection of $h(X)$ with $h'(X)$. For $x_{1},x_{2}\in X$ one has $D(h(x_{1}),h(x_{2}))=d(x_{1},x_{2})=D'(h'(x_{1}),h'(x_{2}))$ because both imbeddings preserve distances, so $T_{0}$ preserves distances and is an isometry.
:::

:::

::: {.pf-step #extend}
For each $y\in\overline{h(X)}$ and each sequence $x_{n}$ with $h(x_{n})\to y$, the sequence $h'(x_{n})$ converges in $Y'$, its limit depends only on $y$, and that limit lies in $\overline{h'(X)}$.

:::: pf-proof

::: {.pf-step #cauchy}
$h'(x_{n})$ is a Cauchy sequence in $Y'$.

::: pf-proof
$h(x_{n})$ converges, hence is Cauchy in $Y$: for $\varepsilon>0$ there is $N$ with $D(h(x_{m}),h(x_{n}))<\varepsilon$ for $m,n\geq N$. Since $D'(h'(x_{m}),h'(x_{n}))=D(h(x_{m}),h(x_{n}))$ for all $m,n$, the same $N$ witnesses that $h'(x_{n})$ is Cauchy.
:::

:::

::: {.pf-step #limit}
$h'(x_{n})$ converges, and its limit lies in $\overline{h'(X)}$.

::: pf-proof
$Y'$ is complete, so the Cauchy sequence converges to some $y'\in Y'$. Every $h'(x_{n})$ lies in $h'(X)$, and a limit of points of a set lies in its closure, so $y'\in\overline{h'(X)}$.
:::

:::

::: {.pf-step #independent}
If also $h(z_{n})\to y$, then $\lim h'(z_{n})=\lim h'(x_{n})$.

::: pf-proof
Both $h(x_{n})$ and $h(z_{n})$ converge to $y$ in the metric space $Y$, so $D(h(x_{n}),h(z_{n}))\to0$ by the triangle inequality $D(h(x_{n}),h(z_{n}))\leq D(h(x_{n}),y)+D(y,h(z_{n}))$; hence $D'(h'(x_{n}),h'(z_{n}))\to0$. If the two image sequences converged to distinct points, some $\varepsilon>0$ would separate those limits, and then $D'(h'(x_{n}),h'(z_{n}))\geq\varepsilon$ for large $n$, a contradiction. Limits in a metric space are unique, so the two limits agree.
:::

:::

::::

:::

::: {.pf-step #definition}
The formula $T(y)\coloneqq\lim_{n}h'(x_{n})$, for $h(x_{n})\to y$, defines a function $T\colon\overline{h(X)}\to\overline{h'(X)}$.

::: pf-proof
Every point of the closure is the limit of a sequence from $h(X)$: this is the sequence lemma, Lemma 21.2 (printed p. 130), whose converse holds in the metrizable space $Y$. So a sequence $x_{n}$ as required exists for each $y$; step [](#extend){.pf-ref} shows the value is a point of $\overline{h'(X)}$ and does not depend on the sequence chosen.
:::

:::

::: {.pf-step #isometry}
$T$ preserves distances.

::: pf-proof
Let $y,z\in\overline{h(X)}$ and choose $h(x_{n})\to y$, $h(z_{n})\to z$. The metric $D'$ is continuous as a function of two variables (§20 Exercise 3(a), printed p. 126), so passing to the limit in $D'(h'(x_{n}),h'(z_{n}))$ gives $D'(T(y),T(z))=\lim_{n}D'(h'(x_{n}),h'(z_{n}))$; then
$$
D'(T(y),T(z))=\lim_{n}D(h(x_{n}),h(z_{n}))=D(y,z),
$$
using $D'(h'(x_{n}),h'(z_{n}))=D(h(x_{n}),h(z_{n}))$ and again the continuity of the metric $D$ at the pair $(y,z)$.
:::

:::

::: {.pf-step #surjective}
$T$ is surjective.

::: pf-proof
Let $y'\in\overline{h'(X)}$ and choose $x_{n}$ with $h'(x_{n})\to y'$. Then $h'(x_{n})$ is Cauchy, and $D(h(x_{m}),h(x_{n}))=D'(h'(x_{m}),h'(x_{n}))$ makes $h(x_{n})$ Cauchy in $Y$; since $Y$ is complete that sequence converges to some $y\in Y$, which lies in $\overline{h(X)}$ because its terms do. By the definition of $T$, $T(y)=\lim_{n}h'(x_{n})=y'$.
:::

:::

::: pf-step
Therefore $T$ is an isometry of $(\overline{h(X)},D)$ with $(\overline{h'(X)},D')$ that equals $h'h^{-1}$ on $h(X)$.

::: pf-proof
Steps [](#definition){.pf-ref}, [](#isometry){.pf-ref} and [](#surjective){.pf-ref} make $T$ a distance-preserving bijection, hence an isometry. For $y=h(x)\in h(X)$ the constant sequence $x_{n}=x$ converges to $y$, so $T(h(x))=\lim_{n}h'(x)=h'(x)=h'h^{-1}(h(x))$ by step [](#t0-isometry){.pf-ref}. Hence $T$ extends $h'h^{-1}$, as required.
:::

:::

:::

:::
