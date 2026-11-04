---
schema: qual/card@1
id: E-HAT-4.1-8
kind: problem
title: "Exactness of $\\pi_1$ sequence for pairs"
classification:
  areas:
  - topology
  topics:
  - Higher Homotopy Groups
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 4.1, Exercise 8; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: claude
  date: 2026-11-01
  note: >-
    Read line by line. Correct, in Hatcher's convention where a relative path has `u(0) = x_0` and
    `u(1) in A` and `partial[u] = [u(1)]`. At `pi_1(X,A,x_0)`: `[u]` is in the kernel exactly when `u(1)`
    lies in the component of `x_0` in `A`, and then a path `v` in `A` from `u(1)` back to `x_0` turns `u`
    into the loop `uv`, whose relative class is that of `u`; so the kernel is the image of
    `pi_1(X,x_0)`. At `pi_0(A,x_0)`: a component lies in the image of `partial` exactly when it is joined
    to `x_0` by a path in `X`, i.e. exactly when it maps to the distinguished component of `X`. Exactness
    as pointed sets follows. No correction was needed.
---

::: {.problem}
Show the sequence $\pi_1(X, x_0) \to \pi_1(X, A, x_0) \overset{\partial}{\longrightarrow} \pi_0(A, x_0) \to \pi_0(X, x_0)$ is exact.
:::

::: {.solution}
For $\pi_1(X,A,x_0)$, use relative paths $u:I\to X$ with $u(0)=x_0$ and $u(1)\in A$. The boundary map is
$$
\partial[u]=[u(1)]\in\pi_0(A,x_0).
$$

At $\pi_1(X,A,x_0)$: a relative class $[u]$ lies in $\ker\partial$ exactly when $u(1)$ is in the component of $x_0$ in $A$. Choose a path $v\subset A$ from $u(1)$ to $x_0$. Then the loop $uv$ maps to the same relative class as $u$. Hence
$$
\ker\partial=\operatorname{im}\bigl(\pi_1(X,x_0)\to\pi_1(X,A,x_0)\bigr).
$$

At $\pi_0(A,x_0)$: a component $C$ of $A$ lies in the image of $\partial$ exactly when there is a path in $X$ from $x_0$ to a point of $C$, which is exactly the condition that $C$ maps to the distinguished component of $X$. Hence
$$
\operatorname{im}\partial
=\ker\bigl(\pi_0(A,x_0)\to\pi_0(X,x_0)\bigr).
$$
Thus the displayed sequence is exact as a sequence of pointed sets.
:::
