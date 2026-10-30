---
schema: qual/card@1
id: P-LQEAV
kind: problem
title: $\norm{a}_{\ell^q}\le\norm{a}_{\ell^p}$ for $0<p<q\le\infty$
classification:
  areas:
  - real-analysis
  topics:
  - Lp Spaces
  - Norms
  - Series of Numbers
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-17
---

::: {.problem}
Show that for $0 < p < q \le \infty$,
$$
\norm{a}_{\ell^q} \le \norm{a}_{\ell^p}
$$
for any sequence $a = (a_j)_{j=1}^\infty \in \CC^\NN$, where $\norm{a}_{\ell^\infty} \coloneqq \sup_j \abs{a_j}$ and $\norm{a}_{\ell^r} \coloneqq \left(\sum_{j=1}^\infty \abs{a_j}^r\right)^{1/r}$ for $r < \infty$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}
If $q = \infty$, then $\norm{a}_{\ell^\infty} \le \norm{a}_{\ell^p}$.

::: pf-proof

::: pf-step
If $\norm{a}_{\ell^p} = \infty$, then the right-hand side of $\norm{a}_{\ell^\infty} \le \norm{a}_{\ell^p}$ is $\infty$, and every extended real number is $\le \infty$, so the inequality holds.

:::

::: pf-step
Assume $\norm{a}_{\ell^p} < \infty$. For every fixed index $k \ge 1$:
$$\abs{a_k}^p \le \sum_{j=1}^\infty \abs{a_j}^p = \norm{a}_{\ell^p}^p.$$

:::

::: pf-step
Taking the $(1/p)$-th power of both sides (since $t \mapsto t^{1/p}$ is strictly increasing on $[0, \infty)$):
$$\abs{a_k} \le \norm{a}_{\ell^p} \quad \text{for all } k \ge 1.$$

:::

::: pf-step
Taking the supremum over all $k \ge 1$:
$$\norm{a}_{\ell^\infty} = \sup_{k \ge 1} \abs{a_k} \le \norm{a}_{\ell^p}.$$

:::

:::

:::

::: {.pf-step #s2}
If $q < \infty$, then $\norm{a}_{\ell^q} \le \norm{a}_{\ell^p}$.

::: pf-proof

::: pf-step
If $\norm{a}_{\ell^p} = 0$, then $a_j = 0$ for all $j$, so $\norm{a}_{\ell^q} = 0 = \norm{a}_{\ell^p}$.

:::

::: pf-step
If $\norm{a}_{\ell^p} = \infty$, the inequality holds.

:::

::: pf-step
Assume $0 < \norm{a}_{\ell^p} < \infty$. Define the normalized sequence $b = (b_j)_{j=1}^\infty$ by $b_j = \frac{a_j}{\norm{a}_{\ell^p}}$.

:::

::: pf-step
The normalized sequence satisfies
$$\norm{b}_{\ell^p}^p = \sum_{j=1}^\infty \abs{b_j}^p = \sum_{j=1}^\infty \frac{\abs{a_j}^p}{\norm{a}_{\ell^p}^p} = 1.$$

:::

::: pf-step
In particular, for every index $j \ge 1$, $\abs{b_j}^p \le \sum_{k=1}^\infty \abs{b_k}^p = 1$, which implies $\abs{b_j} \le 1$.

:::

::: pf-step
Since $q > p > 0$ and $\abs{b_j} \le 1$, the exponent comparison gives
$$\abs{b_j}^q = \abs{b_j}^{q-p} \abs{b_j}^p \le 1^{q-p} \abs{b_j}^p = \abs{b_j}^p \quad \text{for every } j \ge 1.$$

:::

::: pf-step
Summing over all $j \ge 1$:
$$\norm{b}_{\ell^q}^q = \sum_{j=1}^\infty \abs{b_j}^q \le \sum_{j=1}^\infty \abs{b_j}^p = \norm{b}_{\ell^p}^p = 1.$$

:::

::: pf-step
Taking the $(1/q)$-th power gives $\norm{b}_{\ell^q} \le 1^{1/q} = 1$.

:::

::: pf-step
Multiplying both sides by the positive scalar $\norm{a}_{\ell^p}$:
$$\norm{a}_{\ell^q} = \norm{a}_{\ell^p} \norm{b}_{\ell^q} \le \norm{a}_{\ell^p} \cdot 1 = \norm{a}_{\ell^p}.$$

:::

:::

:::

::: pf-qed
Either $q = \infty$ or $p < q < \infty$, and steps [](#s1){.pf-ref} and [](#s2){.pf-ref} give the inequality in the two cases.
:::

:::

:::
