---
schema: qual/card@1
id: E-A0UGQ
kind: problem
title: A function continuous at exactly one point
classification:
  areas:
  - topology
  topics:
  - Continuous Functions
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Read against Munkres, Topology (2000), §18 Exercise 6, printed p. 111; the stored
    statement is the printed request and the card answers it with one function and the proof
    that its set of continuity is a single point.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: Dan Whitman, "Topology, Second Edition
    by James Munkres: Solutions Manual" (30 November 2019), Exercise 18.6, printed p. 181.
    The function, zero on the rationals and the identity on the irrationals, is his, as is
    the epsilon-delta verification: continuous at 0 with delta = epsilon, and at x != 0 the
    point y chosen rational or irrational within delta of x forces |f(y)-f(x)| > |x|/2. The
    epsilon-delta definition is admissible here because it implies the open set definition
    by Exercise 18.1. (tmp/sources/munkres-solutions-whitman.pdf).
---

::: {.exercise}

Find a function $f: \RR \to \RR$ that is continuous at precisely one point.
:::

::: {.solution}
The complete published solution is **Dan Whitman, *Topology, Second Edition by James Munkres: Solutions Manual* (30 November 2019), Exercise 18.6, printed p. 181** (`tmp/sources/munkres-solutions-whitman.pdf`); the function and the proof are his.

Let
$$
f:\RR\longrightarrow\RR,\qquad
f(x)=\begin{cases}0,& x\in\QQ,\\ x,& x\notin\QQ.\end{cases}
$$
Then $f$ is continuous at $0$ and at no other point.

We use the $\varepsilon$-$\delta$ definition, which implies the open set definition by Exercise 18.1. Note $f(0)=0$.

*At $0$.* Given $\varepsilon>0$ take $\delta=\varepsilon$. If $\abs{y}<\delta$ and $y\in\QQ$ then $f(y)=0=f(0)$; if $y\notin\QQ$ then $\abs{f(y)-f(0)}=\abs{y}<\delta=\varepsilon$. So $f$ is continuous at $0$.

*At $x\ne0$.* Put $\varepsilon=\abs{x}/2>0$, and let $\delta>0$ be arbitrary. If $x\in\QQ$ choose $y\notin\QQ$ with $\abs{y-x}<\min(\varepsilon,\delta)$; then $f(x)=0$ and $f(y)=y$, and
$$
\abs{x}=\abs{x-y+y}\le\abs{x-y}+\abs{y}<\varepsilon+\abs{y}\quad\text{so}\quad \abs{f(y)-f(x)}=\abs{y}>\abs{x}-\varepsilon=\varepsilon .
$$
If $x\notin\QQ$ choose $y\in\QQ$ with $\abs{y-x}<\delta$; then $f(y)=0$ and $\abs{f(y)-f(x)}=\abs{x}=2\varepsilon>\varepsilon$. So for every $\delta>0$ there is $y$ with $\abs{y-x}<\delta$ and $\abs{f(y)-f(x)}>\varepsilon$, and $f$ is not continuous at $x$.

So $0$ is the one point of continuity. (The same answer is recorded by "positron0802", *Solutions to Topology, Chapter 2*, Exercise 18.6, PDF p. 11.)
:::
