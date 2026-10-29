---
schema: qual/card@1
id: E-BQBZI
kind: problem
title: $\norm{f}_p\to\norm{f}_\infty$ as $p\to\infty$ on finite measure spaces
classification:
  areas:
  - real-analysis
  topics:
  - Lp Spaces
  - L∞
  - Limits
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-17
---

::: {.exercise}
Show that if $X \subseteq \RR$ is a measurable set with finite measure $\mu(X) < \infty$, then for any measurable function $f: X \to \CC$,
$$
\lim_{p \to \infty} \norm{f}_{L^p(X)} = \norm{f}_{L^\infty(X)}.
$$
:::

::: {.solution}
Write $\norm{\cdot}_p$ for $\norm{\cdot}_{L^p(X)}$ and $\norm{\cdot}_\infty$ for $\norm{\cdot}_{L^\infty(X)}$.
If $\mu(X) = 0$, every norm of $f$ is $0$, so assume $0 < \mu(X) < \infty$.

::: pf

::: {.pf-step #upper}

$\limsup_{p \to \infty} \norm{f}_p \le \norm{f}_\infty$.

::: pf-proof

The claim is trivial if $\norm{f}_\infty = \infty$.
Otherwise $\abs{f} \le \norm{f}_\infty$ almost everywhere on $X$, so
$$
\norm{f}_p = \qty{\int_X \abs{f}^p \, d\mu}^{1/p} \le \norm{f}_\infty\, \mu(X)^{1/p},
$$
and $\mu(X)^{1/p} \to 1$ as $p \to \infty$ because $0 < \mu(X) < \infty$.

:::

:::

::: {.pf-step #lower}

$\liminf_{p \to \infty} \norm{f}_p \ge \norm{f}_\infty$.

::: pf-proof

The claim is trivial if $\norm{f}_\infty = 0$.
Otherwise let $0 < \alpha < \norm{f}_\infty$ and $A_\alpha \coloneqq \theset{x \in X : \abs{f(x)} \ge \alpha}$.
By the definition of the essential supremum, $\mu(A_\alpha) > 0$, and $\mu(A_\alpha) \le \mu(X) < \infty$.
Then
$$
\norm{f}_p \ge \qty{\int_{A_\alpha} \abs{f}^p \, d\mu}^{1/p} \ge \alpha\, \mu(A_\alpha)^{1/p} \xrightarrow{p \to \infty} \alpha,
$$
so $\liminf_{p \to \infty} \norm{f}_p \ge \alpha$.
Taking the supremum over all such $\alpha$ gives the claim, also when $\norm{f}_\infty = \infty$.

:::

:::

::: pf-qed

Steps [](#upper){.pf-ref} and [](#lower){.pf-ref} give $\norm{f}_\infty \le \liminf_{p} \norm{f}_p \le \limsup_{p} \norm{f}_p \le \norm{f}_\infty$, so the limit exists and equals $\norm{f}_\infty$.

:::

:::

:::
