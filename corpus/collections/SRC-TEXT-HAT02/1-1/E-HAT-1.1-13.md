---
schema: qual/card@1
id: E-HAT-1.1-13
kind: problem
title: Surjectivity of inclusion-induced map on $\pi_1$ iff paths in $X$ with endpoints in $A$ are homotopic to paths in $A$
classification:
  areas:
  - topology
  topics:
  - Fundamental Group
  - Subspaces
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 1.1, Exercise 13; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Closed an arbitrary endpoint-in-A path to a based loop using paths in A, applied surjectivity, and cancelled the auxiliary paths.
---

::: {.problem}
Given a space $X$ and a path-connected subspace $A$ containing the basepoint $x_0$, show that the map $\pi_1(A, x_0) \to \pi_1(X, x_0)$ induced by the inclusion $A \hookrightarrow X$ is surjective iff every path in $X$ with endpoints in $A$ is homotopic to a path in $A$.
:::

::: {.solution}
All homotopies of paths below are relative to their endpoints.

::: pf

::: {.pf-step #s1}

Suppose the inclusion-induced map
\[
i_*:\pi_1(A,x_0)\to\pi_1(X,x_0)
\]
is surjective.
Let $\gamma$ be a path in $X$ from $x\in A$ to $y\in A$.

::: pf-proof

This fixes an arbitrary path of the type appearing in the desired path condition.

:::

:::

::: {.pf-step #s2}

Choose paths $a$ in $A$ from $x_0$ to $x$ and $b$ in $A$ from $y$ to $x_0$.
Then
\[
\ell=a\cdot\gamma\cdot b
\]
is a loop in $X$ based at $x_0$.

::: pf-proof

The paths $a$ and $b$ exist because $A$ is path connected.
Their endpoints match those of $\gamma$, so the concatenation is defined and begins and ends at $x_0$.

:::

:::

::: {.pf-step #s3}

There is a loop $c$ in $A$ based at $x_0$ such that
\[
[c]=[\ell]\in\pi_1(X,x_0).
\]

::: pf-proof

This is precisely surjectivity of $i_*$ applied to the class $[\ell]$.

:::

:::

::: {.pf-step #s4}

The path $\gamma$ is homotopic relative to endpoints in $X$ to
\[
\bar a\cdot c\cdot\bar b,
\]
which lies entirely in $A$.

::: pf-proof

The equality in step [](#s3){.pf-ref} means
\[
a\cdot\gamma\cdot b\simeq c
\]
relative to the basepoint.
Concatenate this homotopy on the left by $\bar a$ and on the right by $\bar b$ to obtain
\[
\bar a\cdot a\cdot\gamma\cdot b\cdot\bar b
\simeq
\bar a\cdot c\cdot\bar b.
\]
The standard cancellation homotopies
\[
\bar a\cdot a\simeq c_x,
\qquad
b\cdot\bar b\simeq c_y
\]
reduce the left-hand side to $\gamma$ relative to its endpoints.
Every factor on the right lies in $A$, so the terminal path lies in $A$.

:::

:::

::: {.pf-step #s5}

Thus surjectivity of $i_*$ implies the stated path condition.

::: pf-proof

The path $\gamma$ in step [](#s1){.pf-ref} was arbitrary.

:::

:::

::: {.pf-step #s6}

Conversely, suppose every path in $X$ whose endpoints lie in $A$ is homotopic relative to endpoints to a path in $A$.
Then $i_*$ is surjective.

::: pf-proof

Let
\[
[\gamma]\in\pi_1(X,x_0)
\]
be arbitrary.
The loop $\gamma$ has both endpoints equal to $x_0\in A$, so by hypothesis it is homotopic relative to endpoints to a path $c$ in $A$.
Since the endpoints are fixed during the homotopy, $c$ is a loop in $A$ based at $x_0$.
Therefore
\[
i_*([c])=[\gamma].
\]
Every element of $\pi_1(X,x_0)$ is thus in the image of $i_*$.

:::

:::

::: pf-step

Hence the two conditions are equivalent.

::: pf-proof

The forward implication is steps [](#s1){.pf-ref}, [](#s2){.pf-ref}, [](#s3){.pf-ref}, [](#s4){.pf-ref} and [](#s5){.pf-ref}, and the reverse implication is step [](#s6){.pf-ref}.

:::

:::

:::

:::
