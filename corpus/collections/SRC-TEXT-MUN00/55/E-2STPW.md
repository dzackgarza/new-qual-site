---
schema: qual/card@1
id: E-2STPW
kind: exercise
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

::: solution
**Goal:** Prove that every nullhomotopic continuous self-map $h: S^1 \to S^1$ must possess a fixed point ($h(x_0) = x_0$) and an antipodal point ($h(x_1) = -x_1$).

<1>1. Degree of nullhomotopic maps:
    Since $h: S^1 \to S^1$ is nullhomotopic (homotopic to a constant map), the induced map on fundamental groups $h_*: \pi_1(S^1) \to \pi_1(S^1)$ is the zero homomorphism, so the winding number (topological degree) satisfies $\deg(h) = 0$.

<1>2. Existence of a fixed point:
    There exists $x_0 \in S^1$ such that $h(x_0) = x_0$.
    *Proof:*
    <2>1. Suppose for contradiction that $h(x) \neq x$ for all $x \in S^1$.
    <2>2. Then for all $x \in S^1$ and $t \in [0, 1]$, the convex combination $(1-t)h(x) + t(-x) \neq 0$.
        (If $(1-t)h(x) = tx$, taking norms gives $1-t = t \implies t = 1/2 \implies h(x) = x$, a contradiction).
    <2>3. Define the straight-line homotopy $H: S^1 \times [0, 1] \to S^1$ by:
        $$H(x, t) = \frac{(1-t)h(x) - tx}{\|(1-t)h(x) - tx\|}.$$
    <2>4. $H$ is a continuous homotopy between $h(x)$ and the antipodal map $a(x) = -x$.
    <2>5. The antipodal map $a(x) = -x$ on $S^1$ is homotopic to the identity via the rotation homotopy $R_t(x) = e^{i\pi t} x$, so $\deg(a) = \deg(\operatorname{id}_{S^1}) = 1 \neq 0$.
    <2>6. Since homotopy preserves degree, $\deg(h) = \deg(a) = 1$, strictly contradicting $\deg(h) = 0$ from <1>1.
    <2>7. Thus there must exist $x_0 \in S^1$ such that $h(x_0) = x_0$.

<1>3. Existence of an antipodal point:
    There exists $x_1 \in S^1$ such that $h(x_1) = -x_1$.
    *Proof:*
    <2>1. Suppose for contradiction that $h(x) \neq -x$ for all $x \in S^1$.
    <2>2. Then for all $x \in S^1$ and $t \in [0, 1]$, $(1-t)h(x) + tx \neq 0$.
        (If $(1-t)h(x) = -tx$, taking norms gives $1-t = t \implies t = 1/2 \implies h(x) = -x$, a contradiction).
    <2>3. Define the straight-line homotopy $K: S^1 \times [0, 1] \to S^1$ by:
        $$K(x, t) = \frac{(1-t)h(x) + tx}{\|(1-t)h(x) + tx\|}.$$
    <2>4. $K$ is a continuous homotopy between $h$ and the identity map $\operatorname{id}_{S^1}$.
    <2>5. Thus $\deg(h) = \deg(\operatorname{id}_{S^1}) = 1$, again strictly contradicting $\deg(h) = 0$.
    <2>6. Thus there must exist $x_1 \in S^1$ such that $h(x_1) = -x_1$.

<1>4. Conclusion:
    Every nullhomotopic self-map of $S^1$ has both a fixed point and an antipodal point. Q.E.D.
:::
