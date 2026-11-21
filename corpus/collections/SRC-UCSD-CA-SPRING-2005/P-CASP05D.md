---
schema: qual/card@1
id: P-CASP05D
kind: problem
title: "Polynomial approximation for the reciprocal of a nonvanishing analytic function"
classification:
  areas:
  - complex-analysis
  topics:
  - Complex Analysis
relations: []
review: draft
audit:
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Restructured the prose solution into a Lamport proof and checked it: the open
    zero-free neighbourhood is built from min_K |f| > 0, 1/f is holomorphic on it, Runge's
    polynomial form uses the connected complement, A = max_K |f| is positive, and the
    approximation of 1/f within eps/A gives |fP - 1| <= eps. Added the empty-K case,
    which the prose did not treat and which the hypotheses allow. The collection's
    provenance is the examination paper only, so no retained solution set covers the
    exercise and the argument is the card's own.
---

::: {.problem}
Let $K \subset \CC$ be a compact set.
Assume that $\CC \setminus K$ is connected and $0 \notin K$.
Prove that for any analytic function $f$ in an open neighborhood of $K$ nowhere vanishing on $K$, and any $\epsilon > 0$, there exists a polynomial $P$, satisfying $$\abs{f(z)P(z) - 1} \leq \epsilon, \quad \forall z \in K.$$
:::

::: {.solution}
The collection's provenance is the examination paper alone, so no retained solution set covers this exercise; the argument is the card's own.

::: pf

::: {.pf-step}
It suffices to treat nonempty $K$.

::: pf-proof
If $K=\emptyset$ then every polynomial satisfies the required inequality, the supremum over the empty set being $0$, so take $P=0$; and the hypotheses $0\notin K$ and $\CC\setminus K=\CC$ connected hold in that case.
:::

:::

::: {.pf-step #neighbourhood}
There is an open set $U$ containing $K$, contained in the domain of $f$, on which $f$ has no zeros.

::: pf-proof
$z\mapsto\abs{f(z)}$ is continuous and positive on the nonempty compact set $K$, so $m\coloneqq\min_{z\in K}\abs{f(z)}>0$. Let $V$ be the domain of $f$, an open set containing $K$. Then $U\coloneqq\{z\in V:\abs{f(z)}>m/2\}$ is open, contains $K$, and $f$ does not vanish on it.
:::

:::

::: {.pf-step #reciprocal}
$g\coloneqq1/f$ is holomorphic on $U$.

::: pf-proof
$f$ is holomorphic and zero-free on the open set $U$, so its reciprocal is holomorphic there.
:::

:::

::: {.pf-step #runge}
For every $\eta>0$ there is a polynomial $P$ with $\sup_{z\in K}\abs{P(z)-g(z)}<\eta$.

::: pf-proof
This is Runge's theorem in its polynomial form: for a compact $K$ whose complement $\CC\setminus K$ is connected, every function holomorphic on an open neighbourhood of $K$ is the uniform limit on $K$ of polynomials. Step [](#reciprocal){.pf-ref} supplies $g$ holomorphic on the neighbourhood $U$ of $K$, and the hypothesis of connected complement is assumed.
:::

:::

::: {.pf-step #mass}
$A\coloneqq\max_{z\in K}\abs{f(z)}$ is finite and positive.

::: pf-proof
$\abs{f}$ is continuous on the nonempty compact $K$, so it attains a maximum. That maximum is positive because $f$ has no zeros on $K$.
:::

:::

::: {.pf-step}
For every $\varepsilon>0$ there is a polynomial $P$ with $\abs{f(z)P(z)-1}\le\varepsilon$ for all $z\in K$.

::: pf-proof
By step [](#mass){.pf-ref} the number $\eta\coloneqq\varepsilon/A$ is positive, so step [](#runge){.pf-ref} supplies a polynomial $P$ with $\sup_K\abs{P-g}<\eta$. For $z\in K$,
$$
\abs{f(z)P(z)-1}=\abs{f(z)}\abs{P(z)-\frac{1}{f(z)}}\le A\cdot\frac{\varepsilon}{A}=\varepsilon .
$$
:::

:::

:::
:::
