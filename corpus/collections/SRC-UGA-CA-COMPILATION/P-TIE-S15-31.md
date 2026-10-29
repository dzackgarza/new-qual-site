---
schema: qual/card@1
id: P-TIE-S15-31
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
  note: Checked against the retained Questions_from_Tie.pdf compilation, section Spring 2015, question 31.
---

::: {.problem}
Let Ω be a simply connected open set and let γ be a simple closed contour in Ω and enclosing a bounded region U anticlockwise.
Let $f : \Omega \longrightarrow \CC$ be a holomorphic function and $| f ( z ) | \leq M$ for all $z \in \gamma$ . Prove that $| f ( z ) | \leq M$ for all $z \in U$
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

The bounded region $U$ enclosed by $\gamma$ satisfies
$$
U\subset\Omega.
$$


::: pf-proof

Because $\Omega$ is simply connected, every simple closed curve contained in $\Omega$ bounds its Jordan interior inside $\Omega$. Equivalently, every point outside $\Omega$ has winding number $0$ with respect to $\gamma$, whereas every point of $U$ has winding number $1$ because $\gamma$ is positively oriented. Hence no point of $U$ can lie outside $\Omega$.

:::

:::

::: pf-step

The function $f$ is holomorphic on a neighborhood of $\overline U$.


::: pf-proof

By step [](#s1-1){.pf-ref},
$$
U\subset\Omega,
$$
and by hypothesis
$$
\partial U=\gamma\subset\Omega.
$$
Thus
$$
\overline U\subset\Omega.
$$
Since $\Omega$ is open, $f$ is holomorphic on an open neighborhood of the compact set $\overline U$.

:::

:::

::: {.pf-step #s1-3}

One has
$$
\max_{\overline U}\abs f
=
\max_{\gamma}\abs f.
$$


::: pf-proof

The continuous function $\abs f$ attains its maximum on the compact set $\overline U$. If $f$ is nonconstant, the strong maximum modulus principle forbids an interior maximum. If $f$ is constant, the equality is immediate. Hence in every case the maximum over $\overline U$ is attained on the boundary
$$
\gamma=\partial U.
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
The hypothesis gives
$$
\abs{f(\zeta)}\le M
$$
for every $\zeta\in\gamma$. Therefore
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
