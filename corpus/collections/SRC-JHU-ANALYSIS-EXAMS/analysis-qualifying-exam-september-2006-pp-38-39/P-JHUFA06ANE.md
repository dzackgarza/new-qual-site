---
schema: qual/card@1
id: P-JHUFA06ANE
kind: problem
title: 'Closed subspaces of trigonometric polynomials in $C_0([0,\pi])$ are finite-dimensional'
classification:
  areas:
  - real-analysis
  topics:
  - Banach Spaces
  - Compactness
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-08
  note: Checked against Problem 5 of the JHU Analysis Qualifying Exam, September 2006, in the preserved exam collection.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-08
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
---

::: {.problem}
Let $X$ be the Banach space of continuous real-valued functions on $[0,\pi]$ that vanish at $0$ and $\pi$, with the supremum norm. Suppose $Y\subset X$ is a closed subspace and every element of $Y$ is a trigonometric polynomial. Prove that $Y$ is finite dimensional.
:::

::: {.solution}

No retained solution set covers this exercise: the card's own Baire-category argument follows, with the exhaustion, the closedness of the pieces and the conclusion as separate steps.

Let $X=C_{0}[0,\pi]$ be the Banach space of continuous real functions vanishing at $0$ and $\pi$, with the supremum norm, and let $Y\subseteq X$ be a closed subspace all of whose elements are trigonometric polynomials.

::: pf

::: {.pf-step #exhaust}
With $V_{N}=\operatorname{span}\theset{1,\sin x,\cos x,\dots,\sin Nx,\cos Nx}$ and $Y_{N}=Y\cap V_{N}$: each $V_{N}$ is finite dimensional, $Y=\bigcup_{N}Y_{N}$, and each $Y_{N}$ is closed in $Y$.

::: pf-proof
$V_{N}$ has dimension $2N+1$, and every finite-dimensional subspace of a normed space is complete, hence closed in $X$; so $Y_{N}$, the intersection of $Y$ with a closed set, is closed in $Y$. By hypothesis each $y\in Y$ is a trigonometric polynomial, say of degree $N$, so $y\in Y\cap V_{N}=Y_{N}$; conversely $Y_{N}\subseteq Y$.
:::

:::

::: {.pf-step #baire}
Some $Y_{N}$ has nonempty interior in $Y$.

::: pf-proof
$Y$ is a closed subset of the complete space $X$, hence a complete metric space, that is a Baire space; it is the countable union of the closed sets $Y_{N}$ by step [](#exhaust){.pf-ref}. By Baire's theorem some $Y_{N}$ contains a relative ball $B(y_{0},r)\cap Y$ with $r>0$.
:::

:::

::: {.pf-step #finite}
$Y=Y_{N}$ for such an $N$, so $Y$ is finite dimensional.

::: pf-proof
$Y_{N}$ is a linear subspace of $Y$ and contains $y_{0}$ together with $y_{0}+y$ for every $y\in Y$ with $\norm{y}<r$; hence it contains all $y\in Y$ with $\norm{y}<r$, by linearity (subtract $y_{0}$, which lies in $Y_{N}$). Since $Y_{N}$ is a linear subspace containing every $y\in Y$ of norm $<r$, homogeneity gives every $y\in Y$: if $y\ne0$ then $\frac{r}{2\norm{y}}y$ has norm $r/2<r$, so lies in $Y_{N}$, and multiplying by the scalar $2\norm{y}/r$ returns $y$. Thus $Y=Y_{N}$, of dimension at most $2N+1$.
:::

:::

::: {.pf-qed}
$Y$ is finite dimensional by steps [](#baire){.pf-ref} and [](#finite){.pf-ref}.
:::

:::

:::
