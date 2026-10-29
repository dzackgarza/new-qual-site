---
schema: qual/card@1
id: E-IVHVW
kind: problem
title: A self-map of $\DD$ is bounded by the Blaschke product of its zeros
classification:
  areas:
  - complex-analysis
  topics:
  - Blaschke Factors
  - Schwarz Lemma
  - Zeros
  - Maximum Modulus Principle
relations: []
review: draft
audit:
- event: source-corrected
  by: Claude Opus 5.5
  date: 2026-10-29
  note: The source reads "Let f:D -> D with {a_k}_{k <= n} the zeros of f in D" and leaves psi_a undefined; the statement adds that f is holomorphic, counts the zeros with multiplicity, and defines psi_a.
---

::: {.exercise}
Let $f: \DD\to \DD$ be holomorphic, and let $a_1,\ldots,a_n$ be zeros of $f$ in $\DD$, listed with multiplicity.
For $a\in\DD$, let $\psi_a(z)\coloneqq{a-z\over1-\bar az}$.
Show that
$$
\abs{f(z)}\leq \prod_{k\leq n} \abs{ \psi_{a_k}(z) }
.$$
:::

::: {.solution}
Let $\Psi \coloneqq \prod_{k\leq n} \psi_{a_k}$.

::: pf

::: {.pf-step #quotient}
$g\coloneqq f/\Psi$ extends to a holomorphic function on $\DD$.

::: pf-proof
Each zero of $\Psi$ in $\DD$ is a zero of $f$ of at least the same order, so the singularities of $g$ are removable.
:::

:::

::: {.pf-step #boundary}
$m(r)\coloneqq\min_{\abs z=r}\abs{\Psi(z)}\to1$ as $r\to1^-$.

::: pf-proof
$\Psi$ is continuous on $\overline\DD$ with $\abs{\Psi} = 1$ on $\abs{z} = 1$, so this follows from uniform continuity of $\abs\Psi$ on $\overline\DD$.
:::

:::

::: pf-step
$\abs{f(z)}\le\abs{\Psi(z)}$ for $z\in\DD$.

::: pf-proof
Fix $z\in\DD$. For $\abs z<r<1$ with $m(r)>0$, the maximum modulus principle for the function $g$ of step [](#quotient){.pf-ref} on $\abs\zeta\le r$ and $\abs f<1$ give
$$
\abs{g(z)}\le\max_{\abs\zeta=r}{ \abs{f(\zeta)} \over \abs{\Psi(\zeta)} } \leq {1\over m(r)}
,$$
which tends to $1$ as $r\to1^-$ by step [](#boundary){.pf-ref}. Hence $\abs{g(z)}\le1$.
:::

:::

:::

:::
