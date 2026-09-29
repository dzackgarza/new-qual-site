---
schema: qual/card@1
id: E-2STPW
kind: problem
title: Nulhomotopic maps of the circle have fixed and antipodal points
classification:
  areas:
  - topology
  topics:
  - Fundamental Group
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
---

::: {.exercise}

Show that if $h: S^1 \to S^1$ is nulhomotopic, then $h$ has a fixed point and $h$ maps some point $x$ to its antipode $-x$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

Degree of nullhomotopic maps:
    Since $h: S^1 \to S^1$ is nullhomotopic (homotopic to a constant map), the induced map on fundamental groups $h_*: \pi_1(S^1) \to \pi_1(S^1)$ is the zero homomorphism, so the winding number (topological degree) satisfies $\deg(h) = 0$.

:::

::: pf-step

Existence of a fixed point:
    There exists $x_0 \in S^1$ such that $h(x_0) = x_0$.
    *Proof:*

::: pf-proof

::: pf-step

Suppose for contradiction that $h(x) \neq x$ for all $x \in S^1$.

:::

::: pf-step

Then for all $x \in S^1$ and $t \in [0, 1]$, the convex combination $(1-t)h(x) + t(-x) \neq 0$.
        (If $(1-t)h(x) = tx$, taking norms gives $1-t = t \implies t = 1/2 \implies h(x) = x$, a contradiction).

:::

::: pf-step

Define the straight-line homotopy $H: S^1 \times [0, 1] \to S^1$ by:
        $$H(x, t) = \frac{(1-t)h(x) - tx}{\|(1-t)h(x) - tx\|}.$$

:::

::: pf-step

$H$ is a continuous homotopy between $h(x)$ and the antipodal map $a(x) = -x$.

:::

::: pf-step

The antipodal map $a(x) = -x$ on $S^1$ is homotopic to the identity via the rotation homotopy $R_t(x) = e^{i\pi t} x$, so $\deg(a) = \deg(\operatorname{id}_{S^1}) = 1 \neq 0$.

:::

::: pf-step

Since homotopy preserves degree, $\deg(h) = \deg(a) = 1$, strictly contradicting $\deg(h) = 0$ from step [](#s1){.pf-ref}.

:::

::: pf-step

Thus there must exist $x_0 \in S^1$ such that $h(x_0) = x_0$.

:::

:::

:::

::: pf-step

Existence of an antipodal point:
    There exists $x_1 \in S^1$ such that $h(x_1) = -x_1$.
    *Proof:*

::: pf-proof

::: pf-step

Suppose for contradiction that $h(x) \neq -x$ for all $x \in S^1$.

:::

::: pf-step

Then for all $x \in S^1$ and $t \in [0, 1]$, $(1-t)h(x) + tx \neq 0$.
        (If $(1-t)h(x) = -tx$, taking norms gives $1-t = t \implies t = 1/2 \implies h(x) = -x$, a contradiction).

:::

::: pf-step

Define the straight-line homotopy $K: S^1 \times [0, 1] \to S^1$ by:
        $$K(x, t) = \frac{(1-t)h(x) + tx}{\|(1-t)h(x) + tx\|}.$$

:::

::: pf-step

$K$ is a continuous homotopy between $h$ and the identity map $\operatorname{id}_{S^1}$.

:::

::: pf-step

Thus $\deg(h) = \deg(\operatorname{id}_{S^1}) = 1$, again strictly contradicting $\deg(h) = 0$.

:::

::: pf-step

Thus there must exist $x_1 \in S^1$ such that $h(x_1) = -x_1$.

:::

:::

:::

:::

    Steps [](#s2){.pf-ref} and [](#s3){.pf-ref} give the fixed point and the point sent to its antipode.
:::
