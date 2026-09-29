---
schema: qual/card@1
id: P-RASP18C
kind: problem
title: "Asymptotically parallel unit vectors converge"
classification:
  areas:
  - real-analysis
  topics:
  - Real Analysis
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
---

::: {.problem}
Let $H$ be a Hilbert space and $\{\xi_n\}_{n \geq 1}$ be a sequence of unit vectors in $H$ ($\|\xi_n\| = 1$ for all $n$).
Assume that:
$$\lim_{n,m \to \infty} \|\xi_n + \xi_m\| = 2.$$
Show that there exists $\xi \in H$ such that $\lim_{n \to \infty} \|\xi_n - \xi\| = 0$ (i.e. $\{\xi_n\}$ converges strongly in $H$).
:::

::: {.solution}
**Goal:** Prove that the sequence $\{\xi_n\}$ is Cauchy using the parallelogram law and Hilbert space completeness.

::: pf

::: pf-step
The Parallelogram Law:

::: pf-proof

::: pf-step
In any inner product space (and specifically in the Hilbert space $H$), every pair of vectors $u, v \in H$ satisfies the **Parallelogram Law**:
$$\|u + v\|^2 + \|u - v\|^2 = 2\|u\|^2 + 2\|v\|^2.$$
:::

::: pf-step
Setting $u = \xi_n$ and $v = \xi_m$:
$$\|\xi_n + \xi_m\|^2 + \|\xi_n - \xi_m\|^2 = 2\|\xi_n\|^2 + 2\|\xi_m\|^2.$$
:::

:::

:::

::: pf-step
Evaluating the Norm Difference $\|\xi_n - \xi_m\|$:

::: pf-proof

::: pf-step
Since each vector $\xi_n$ is a unit vector, $\|\xi_n\| = 1$ and $\|\xi_m\| = 1$ for all $n, m \ge 1$.
:::

::: pf-step
Substituting these into the right-hand side of the parallelogram law:
$$2\|\xi_n\|^2 + 2\|\xi_m\|^2 = 2(1)^2 + 2(1)^2 = 4.$$
:::

::: pf-step
Rearranging to solve for $\|\xi_n - \xi_m\|^2$:
$$\|\xi_n - \xi_m\|^2 = 4 - \|\xi_n + \xi_m\|^2.$$
:::

:::

:::

::: pf-step
Proof that $\{\xi_n\}$ is a Cauchy Sequence:

::: pf-proof

::: pf-step
We are given that $\lim_{n,m \to \infty} \|\xi_n + \xi_m\| = 2$.
:::

::: pf-step
Taking the limit of $\|\xi_n - \xi_m\|^2$ as $n, m \to \infty$:
$$\lim_{n, m \to \infty} \|\xi_n - \xi_m\|^2 = \lim_{n, m \to \infty} \left( 4 - \|\xi_n + \xi_m\|^2 \right) = 4 - (2)^2 = 4 - 4 = 0.$$
:::

::: pf-step
Therefore:
$$\lim_{n, m \to \infty} \|\xi_n - \xi_m\| = 0.$$
:::

::: pf-step
This proves that $\{\xi_n\}_{n \ge 1}$ is a **Cauchy sequence** in $H$.
:::

:::

:::

::: pf-step
Completeness of $H$ and Conclusion:

::: pf-proof

::: pf-step
Since $H$ is a Hilbert space, it is **complete** with respect to the norm metric.
:::

::: pf-step
Every Cauchy sequence in a complete metric space converges to a limit in the space.
:::

::: pf-step
Therefore, there exists $\xi \in H$ such that:
$$\lim_{n \to \infty} \|\xi_n - \xi\| = 0.$$
:::

::: pf-step
Furthermore, by continuity of the norm, $\|\xi\| = \lim_{n \to \infty} \|\xi_n\| = 1$, so $\xi$ is a unit vector.
:::

:::

:::

::: pf-qed
Conclusion:
$\{\xi_n\}$ converges strongly to some $\xi \in H$.
:::

:::
:::
