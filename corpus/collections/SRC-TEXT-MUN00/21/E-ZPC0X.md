---
schema: qual/card@1
id: E-ZPC0X
kind: problem
title: Interchanging limits under uniform convergence
classification:
  areas:
  - topology
  topics:
  - Uniform Convergence
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Read against Munkres, Topology (2000), §21 Exercise 8, printed p. 134, with Theorem
    21.6; the stored statement is the printed one.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: "positron0802", "Solutions to Topology,
    Chapter 2" (1 January 2021), Exercise 21.8, PDF p. 25. The three-epsilon argument:
    uniform convergence bounds the distance from f_n(x_n) to f(x_n), continuity of the limit
    bounds the distance from f(x_n) to f(x), and the triangle inequality finishes.
    (tmp/sources/munkres-solutions-positron-ch2.pdf).
---

::: {.exercise}

Let $X$ be a topological space and let $Y$ be a metric space.
Let $f_n: X \to Y$ be a sequence of continuous functions.
Let $x_n$ be a sequence of points of $X$ converging to $x$.
Show that if the sequence $(f_n)$ converges uniformly to $f$, then $(f_n(x_n))$ converges to $f(x)$.
:::

::: {.solution}
The complete published solution is **"positron0802", *Solutions to Topology, Chapter 2* (1 January 2021), Exercise 21.8, PDF p. 25** (`tmp/sources/munkres-solutions-positron-ch2.pdf`); the three-epsilon argument is theirs.

Let $f_{n}\to f$ uniformly, each $f_{n}$ continuous, $x_{n}\to x$, and let $d$ be the metric of $Y$. We show $f_{n}(x_{n})\to f(x)$.

Let $V$ be a neighbourhood of $f(x)$ and choose $\varepsilon>0$ with $B_{d}(f(x),\varepsilon)\subset V$.

By uniform convergence there is $N_{1}$ with $d(f_{n}(t),f(t))<\varepsilon/2$ for all $t\in X$ and all $n\ge N_{1}$; in particular $d(f_{n}(x_{n}),f(x_{n}))<\varepsilon/2$ for $n\ge N_{1}$.

The limit $f$ is continuous (Theorem 21.6), or here simply: since the $f_{n}$ are continuous and the convergence is uniform, $f$ is continuous, so there is $N_{2}$ with $d(f(x_{n}),f(x))<\varepsilon/2$ for $n\ge N_{2}$.

For $n\ge N=\max\{N_{1},N_{2}\}$,
$$
d(f_{n}(x_{n}),f(x))\le d(f_{n}(x_{n}),f(x_{n}))+d(f(x_{n}),f(x))<\frac{\varepsilon}{2}+\frac{\varepsilon}{2}=\varepsilon,
$$
so $f_{n}(x_{n})\in B_{d}(f(x),\varepsilon)\subset V$. Hence $f_{n}(x_{n})\to f(x)$.
:::
