---
schema: qual/card@1
id: E-TVBUC
kind: problem
title: $\lim_{p\to\infty}\pnorm{f}{p}=\pnorm{f}{\infty}$ on a finite-measure space
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
Show that if $E \subseteq \RR^n$ is a measurable set with finite measure $\mu(E) < \infty$, then for any measurable function $f: E \to \CC$,
$$
\lim_{p \to \infty} \pnorm{f}{L^p(E)} = \pnorm{f}{L^\infty(E)}.
$$
:::

::: {.solution}

Write $\pnorm{f}{p} = \pnorm{f}{L^p(E)}$ and $\pnorm{f}{\infty} = \pnorm{f}{L^\infty(E)}$.
If $\mu(E) = 0$, then $\pnorm{f}{p} = 0 = \pnorm{f}{\infty}$ for all $p$, so assume $0 < \mu(E) < \infty$.

::: pf

::: {.pf-step #upper}

$\limsup_{p \to \infty} \pnorm{f}{p} \le \pnorm{f}{\infty}$.

::: pf-proof

There is nothing to prove if $\pnorm{f}{\infty} = \infty$.
Otherwise $\abs{f} \le \pnorm{f}{\infty}$ almost everywhere on $E$, so
$$
\pnorm{f}{p} = \left( \int_E \abs{f}^p \, d\mu \right)^{1/p} \le \pnorm{f}{\infty}\, \mu(E)^{1/p}.
$$
Since $0 < \mu(E) < \infty$, $\mu(E)^{1/p} \to 1$ as $p \to \infty$, and the bound follows.

:::

:::

::: {.pf-step #level-set}

If $0 < M < \pnorm{f}{\infty}$, then $\liminf_{p \to \infty} \pnorm{f}{p} \ge M$.

::: pf-proof

The set $A_M = \theset{x \in E \st \abs{f(x)} > M}$ has $\mu(A_M) > 0$ by the definition of the essential supremum, and $\mu(A_M) \le \mu(E) < \infty$.
Restricting the integral to $A_M$ gives
$$
\pnorm{f}{p} \ge \left( \int_{A_M} \abs{f}^p \, d\mu \right)^{1/p} \ge M\, \mu(A_M)^{1/p},
$$
and $\mu(A_M)^{1/p} \to 1$ as $p \to \infty$.

:::

:::

::: {.pf-step #lower}

$\liminf_{p \to \infty} \pnorm{f}{p} \ge \pnorm{f}{\infty}$.

::: pf-proof

If $\pnorm{f}{\infty} = 0$, the inequality is trivial.
Otherwise step [](#level-set){.pf-ref} applies to every $M$ with $0 < M < \pnorm{f}{\infty}$, and the supremum of these $M$ is $\pnorm{f}{\infty}$, finite or infinite.

:::

:::

::: pf-qed

Steps [](#upper){.pf-ref} and [](#lower){.pf-ref} give $\pnorm{f}{\infty} \le \liminf_{p\to\infty} \pnorm{f}{p} \le \limsup_{p\to\infty} \pnorm{f}{p} \le \pnorm{f}{\infty}$, so the limit exists and equals $\pnorm{f}{\infty}$.

:::

:::

:::
