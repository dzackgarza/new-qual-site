---
schema: qual/card@1
id: E-K9POS
kind: problem
title: Continuous images of limit points
classification:
  areas:
  - topology
  topics:
  - Continuous Functions
  - Limit Points
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Read against Munkres, Topology (2000), §18 Exercise 2, printed p. 111, with the
    definitions of limit point and of continuity in §17 and §18; the stored statement is the
    printed question.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: "positron0802", "Solutions to Topology,
    Chapter 2" (1 January 2021), Exercise 18.2, PDF p. 11. The counterexample is a constant
    map on X = R, continuous by Theorem 18.2, whose image has one point and so has no limit
    points. (tmp/sources/munkres-solutions-positron-ch2.pdf).
- event: solution-reviewed
  by: claude
  date: 2026-11-18
  note: >-
    Restructured into Lamport steps; checked the counterexample (a constant map from R, A =
    X, f(A) a singleton with no limit points) against Munkres §18 Exercise 2, printed p.
    111, and Theorem 18.1 and 18.2(a). positron0802, Exercise 18.2, PDF p. 11; Whitman,
    printed p. 179, agrees. The printed statement needed no repair.
---

::: {.exercise}

Suppose that $f: X \to Y$ is continuous.
If $x$ is a limit point of the subset $A$ of $X$, is it necessarily true that $f(x)$ is a limit point of $f(A)$?
:::

::: {.solution}
The published solution is **"positron0802", *Solutions to Topology, Chapter 2* (1 January 2021), Exercise 18.2, PDF p. 11** (`tmp/sources/munkres-solutions-positron-ch2.pdf`); the counterexample is theirs, and Whitman, printed p. 179, gives the same one.

::: pf

::: {.pf-step #constant}
Let $X=\RR$ with the usual topology, let $Y$ be a space with at least one point $y_{0}$, and let $f:X\to Y$ be the constant map $f(x)=y_{0}$. Then $f$ is continuous.

::: pf-proof
For any subset $V$ of $Y$, the preimage $f^{-1}(V)$ is $X$ if $y_{0}\in V$ and $\varnothing$ otherwise. Both $X$ and $\varnothing$ are open in $X$, so the preimage of every open set of $Y$ is open in $X$, which is the open set definition of continuity (Theorem 18.1). This is the case $f$ constant in Theorem 18.2.
:::

:::

::: {.pf-step #limit-points}
With $A=X$, each $x\in X$ is a limit point of $A$.

::: pf-proof
A point $x$ is a limit point of $A$ if every neighbourhood of $x$ meets $A$ in a point other than $x$. A neighbourhood of $x$ in $\RR$ contains an interval $(x-\epsilon,x+\epsilon)$ with $\epsilon>0$, and that interval contains a point $x+\epsilon/2$ of $A=X$ different from $x$.
:::

:::

::: {.pf-step #image}
$f(A)=\{y_{0}\}$ and $f(x)=y_{0}$ is not a limit point of $f(A)$.

::: pf-proof
Since $f$ is constant, $f(A)=\{y_{0}\}$. The set $Y-\{y_{0}\}$ is a neighbourhood of $y_{0}$ if $Y\ne\{y_{0}\}$, and if $Y=\{y_{0}\}$ then $Y$ itself is a neighbourhood; in either case there is a neighbourhood of $y_{0}$ meeting $f(A)$ only in $y_{0}$ itself, so no point of $f(A)$, and in particular $f(x)=y_{0}$, is a limit point of $f(A)$.
:::

:::

::: {.pf-step}
The answer is no: a continuous image of a limit point of $A$ need not be a limit point of $f(A)$.

::: pf-proof
Steps [](#constant){.pf-ref}, [](#limit-points){.pf-ref} and [](#image){.pf-ref} exhibit a continuous $f$ and a point $x$ that is a limit point of $A$ while $f(x)$ is not a limit point of $f(A)$. Continuity transmits membership in a closure, $f(\overline{A})\subset\overline{f(A)}$ (Theorem 18.1), and not the stronger property of being a limit point.
:::

:::

:::
:::
