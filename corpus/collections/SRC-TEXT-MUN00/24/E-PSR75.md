---
schema: qual/card@1
id: E-PSR75
kind: problem
title: Fixed points of continuous self-maps of the interval
classification:
  areas:
  - topology
  topics:
  - Connectedness
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Read against Munkres, Topology (2000), §24 Exercise 3, printed p. 158, with Theorem
    24.3; both the fixed point request and the question are stored as printed.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: "positron0802", "Solutions to Topology,
    Chapter 3" (1 January 2021), Exercise 24.3, PDF p. 4. f(x) - x changes sign on [0,1]
    unless an endpoint is fixed, and the halving maps on (0,1) and on [0,1) have no fixed
    point. (tmp/sources/munkres-solutions-positron-ch3.pdf).
---

::: {.exercise}

Let $f: X \to X$ be continuous.
Show that if $X = [0, 1]$, there is a point $x$ such that $f(x) = x$.
The point $x$ is called a fixed point of $f$.
What happens if $X$ equals $[0, 1)$ or $(0, 1)$?
:::

::: {.solution}
The complete published solution is **"positron0802", *Solutions to Topology, Chapter 3* (1 January 2021), Exercise 24.3, PDF p. 4** (`tmp/sources/munkres-solutions-positron-ch3.pdf`); the fixed-point argument and both counterexamples are theirs, with the second counterexample written with its formula.

Let $f:[0,1]\to[0,1]$ be continuous and put $g(x)=f(x)-x$. Then $g$ is continuous; if $f(0)=0$ or $f(1)=1$ we are done, and otherwise $f(0)>0$ and $f(1)<1$, so $g(0)>0>g(1)$. By the intermediate value theorem on the connected space $[0,1]$ there is $x\in(0,1)$ with $g(x)=0$, that is $f(x)=x$.

The hypothesis that the interval is closed is needed. On $(0,1)$ the map $x\mapsto x/2$ is continuous into $(0,1)$ with no fixed point: $x/2=x$ forces $x=0\notin(0,1)$. On $[0,1)$ the map $x\mapsto x/2+1/2$ is continuous into $[0,1)$ and has no fixed point: $x/2+1/2=x$ forces $x=1\notin[0,1)$.
:::
