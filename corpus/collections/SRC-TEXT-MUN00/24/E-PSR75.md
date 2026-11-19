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
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Restructured the prose solution into Lamport steps. The statement was checked against Munkres, *Topology* (2000), §24 Exercise 3, printed p. 158, all three questions matching the printed text. The argument is transcribed from the retained set: "positron0802", *Solutions to Topology, Chapter 3* (1 January 2021), Exercise 24.3, PDF p. 4. Checked: $g(0)>0>g(1)$ when neither endpoint is fixed, and that the two counterexample maps land in their domains with $x=0$ resp. $x=1$ the only formal solutions.
---

::: {.exercise}

Let $f: X \to X$ be continuous.
Show that if $X = [0, 1]$, there is a point $x$ such that $f(x) = x$.
The point $x$ is called a fixed point of $f$.
What happens if $X$ equals $[0, 1)$ or $(0, 1)$?
:::

::: {.solution}
The complete published solution is **"positron0802", *Solutions to Topology, Chapter 3* (1 January 2021), Exercise 24.3, PDF p. 4** (`tmp/sources/munkres-solutions-positron-ch3.pdf`); the fixed-point argument and both counterexamples are theirs, with the second counterexample written with its formula. The statement is Munkres, *Topology* (2000), §24 Exercise 3, printed p. 158.

::: pf

::: {.pf-step #ivt}
A continuous $f:[0,1]\to[0,1]$ has a fixed point.

::: pf-proof
If $f(0)=0$ or $f(1)=1$ then that endpoint is fixed. Otherwise $f(0)>0$ and $f(1)<1$; put $g(x)=f(x)-x$, continuous on $[0,1]$ with $g(0)=f(0)>0>f(1)-1=g(1)$. By the intermediate value theorem there is $x\in(0,1)$ with $g(x)=0$, that is $f(x)=x$.
:::
:::

::: {.pf-step #open}
On $(0,1)$ there is a continuous self-map with no fixed point.

::: pf-proof
The map $x\mapsto x/2$ takes $(0,1)$ into $(0,1)$ and is continuous; $x/2=x$ forces $x=0$, which is not in $(0,1)$.
:::
:::

::: {.pf-step #halfopen}
On $[0,1)$ there is a continuous self-map with no fixed point.

::: pf-proof
The map $x\mapsto x/2+1/2$ takes $[0,1)$ into $[1/2,1)\subset[0,1)$ and is continuous; $x/2+1/2=x$ forces $x=1$, which is not in $[0,1)$.
:::
:::

::: {.pf-step}
$[0,1]$ has the fixed point property and neither $[0,1)$ nor $(0,1)$ does.

::: pf-proof
Steps [](#ivt){.pf-ref}, [](#open){.pf-ref} and [](#halfopen){.pf-ref} give the three assertions.
:::
:::

:::
:::
