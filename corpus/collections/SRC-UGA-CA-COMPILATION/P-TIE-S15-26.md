---
schema: qual/card@1
id: P-TIE-S15-26
kind: problem
title: Maximum modulus principle inside a closed contour
classification:
  areas:
  - complex-analysis
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-12
  note: Checked against the retained Questions_from_Tie.pdf compilation, section Spring 2015, question 26.
---

::: {.problem}
Let $\Omega$ be a simply connected open set, and let $\gamma$ be a simple closed contour in $\Omega$ enclosing a bounded region $U$ anticlockwise.
Let $f \colon \Omega \to \CC$ be a holomorphic function with $\abs{f(z)} \leq M$ for all $z \in \gamma$. Prove that $\abs{f(z)} \leq M$ for all $z \in U$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

The bounded Jordan interior $U$ of $\gamma$ is contained in $\Omega$.


::: pf-proof

For a simply connected region $\Omega\subset\CC$, every simple closed curve contained in $\Omega$ bounds a region contained in $\Omega$. Equivalently, the winding number of such a curve about every point outside $\Omega$ is zero. Since $\gamma$ is positively oriented and has winding number $1$ about every point of its bounded Jordan interior, no point of $U$ can lie outside $\Omega$. Hence
$$
U\subset\Omega.
$$

:::

:::

::: {.pf-step #s1-2}

The function $f$ is holomorphic on a neighborhood of $\overline U$.


::: pf-proof

By step [](#s1-1){.pf-ref},
$$
U\subset\Omega,
$$
and by hypothesis
$$
\gamma=\partial U\subset\Omega.
$$
Thus
$$
\overline U
=
U\cup\gamma
\subset
\Omega.
$$
Since $\Omega$ is open, every point of the compact set $\overline U$ has a neighborhood contained in $\Omega$. Hence $f$ is holomorphic on an open neighborhood of $\overline U$.

:::

:::

::: {.pf-step #s1-3}

One has
$$
\max_{z\in\overline U}\abs{f(z)}
=
\max_{z\in\gamma}\abs{f(z)}.
$$


::: pf-proof

By step [](#s1-2){.pf-ref}, $f$ is holomorphic on a neighborhood of $\overline U$, so it is continuous on $\overline U$. The compactness of $\overline U$ implies that $\abs f$ attains its maximum there.

If a maximum were attained at an interior point of $U$ and $f$ were nonconstant, the strong maximum modulus principle would be violated. If $f$ is constant, the equality is immediate. Therefore in all cases the maximum on $\overline U$ is attained on the boundary
$$
\partial U=\gamma.
$$

:::

:::

::: {.pf-step #s1-4}

For every $z\in U$,
$$
\boxed{\abs{f(z)}\le M.}
$$


::: pf-proof

By step [](#s1-3){.pf-ref},
$$
\abs{f(z)}
\le
\max_{\zeta\in\gamma}\abs{f(\zeta)}.
$$
The boundary hypothesis gives
$$
\abs{f(\zeta)}\le M
$$
for every $\zeta\in\gamma$. Hence
$$
\abs{f(z)}\le M.
$$

:::

:::

::: pf-qed

Step [](#s1-4){.pf-ref} is the required conclusion.

:::

:::

:::
