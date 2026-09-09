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

Given a space $X$ and a path-connected subspace $A$ containing the basepoint $x_0$, show that the map $\pi_1(A, x_0) \to \pi_1(X, x_0)$ induced by the inclusion $A \hookrightarrow X$ is surjective iff every path in $X$ with endpoints in $A$ is homotopic to a path in $A$.

::: {.solution}
All homotopies of paths below are relative to their endpoints.

<1>1. Suppose the inclusion-induced map
\[
i_*:\pi_1(A,x_0)\to\pi_1(X,x_0)
\]
is surjective.
Let $\gamma$ be a path in $X$ from $x\in A$ to $y\in A$.
::: {.proof}
This fixes an arbitrary path of the type appearing in the desired path condition.
:::

<1>2. Choose paths $a$ in $A$ from $x_0$ to $x$ and $b$ in $A$ from $y$ to $x_0$.
Then
\[
\ell=a\cdot\gamma\cdot b
\]
is a loop in $X$ based at $x_0$.
::: {.proof}
The paths $a$ and $b$ exist because $A$ is path connected.
Their endpoints match those of $\gamma$, so the concatenation is defined and begins and ends at $x_0$.
:::

<1>3. There is a loop $c$ in $A$ based at $x_0$ such that
\[
[c]=[\ell]\in\pi_1(X,x_0).
\]
::: {.proof}
This is precisely surjectivity of $i_*$ applied to the class $[\ell]$.
:::

<1>4. The path $\gamma$ is homotopic relative to endpoints in $X$ to
\[
\bar a\cdot c\cdot\bar b,
\]
which lies entirely in $A$.
::: {.proof}
The equality in <1>3 means
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

<1>5. Thus surjectivity of $i_*$ implies the stated path condition.
::: {.proof}
The path $\gamma$ in <1>1 was arbitrary.
:::

<1>6. Conversely, suppose every path in $X$ whose endpoints lie in $A$ is homotopic relative to endpoints to a path in $A$.
Then $i_*$ is surjective.
::: {.proof}
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

<1>7. Hence the two conditions are equivalent.
::: {.proof}
The forward implication is <1>1--<1>5, and the reverse implication is <1>6.
:::
:::
