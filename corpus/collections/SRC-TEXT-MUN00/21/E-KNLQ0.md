---
schema: qual/card@1
id: E-KNLQ0
kind: problem
title: Uniform convergence as convergence in the uniform metric
classification:
  areas:
  - topology
  topics:
  - Uniform Convergence
  - Metric Spaces
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Read against Munkres, Topology (2000), §21 Exercise 7, printed p. 134, with the uniform
    metric of §20; the stored statement is the printed equivalence.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: "positron0802", "Solutions to Topology,
    Chapter 2" (1 January 2021), Exercise 21.7, PDF p. 25. Uniform convergence bounds the
    supremum of the pointwise distances, which is the uniform distance while it is below 1,
    and convergence in the uniform metric forces the pointwise distances below any epsilon
    once the distance itself is, so the two notions agree. (tmp/sources/munkres-solutions-
    positron-ch2.pdf).
- event: solution-reviewed
  by: claude
  date: 2026-11-18
  note: >-
    Restructured into Lamport steps; checked both implications between uniform convergence
    and convergence in the uniform metric, with the truncation at 1 handled explicitly in
    each direction. positron0802, Exercise 21.7, PDF p. 25. The printed statement needed no
    repair.
---

::: {.exercise}

Let $X$ be a set, and let $f_n: X \to \RR$ be a sequence of functions.
Let $\bar{\rho}$ be the uniform metric on the space $\RR^X$.
Show that the sequence $(f_n)$ converges uniformly to the function $f: X \to \RR$ if and only if the sequence $(f_n)$ converges to $f$ as elements of the metric space $(\RR^X, \bar{\rho})$.
:::

::: {.solution}
The published solution is **"positron0802", *Solutions to Topology, Chapter 2* (1 January 2021), Exercise 21.7** (`tmp/sources/munkres-solutions-positron-ch2.pdf`); both directions are theirs.

Recall that $\bar\rho(f,g)=\sup_{x\in X}\min\{\abs{f(x)-g(x)},1\}$ is the uniform metric on $\RR^{X}$, so that $\bar\rho(f,g)\le1$ always.

::: pf

::: {.pf-step #uniform-implies}
If $f_{n}\to f$ uniformly, then $f_{n}\to f$ in $(\RR^{X},\bar\rho)$.

::: pf-proof
Let $\varepsilon>0$. Uniform convergence gives $N$ with $\abs{f_{n}(x)-f(x)}<\varepsilon$ for every $x\in X$ and every $n\ge N$. For such $n$ and every $x$, $\min\{\abs{f_{n}(x)-f(x)},1\}\le\abs{f_{n}(x)-f(x)}<\varepsilon$, so $\bar\rho(f,f_{n})\le\varepsilon$. Hence $\bar\rho(f,f_{n})\to0$.
:::

:::

::: {.pf-step #metric-implies}
If $\bar\rho(f,f_{n})\to0$, then $f_{n}\to f$ uniformly.

::: pf-proof
Let $\varepsilon>0$ and put $\varepsilon'=\min\{\varepsilon,1\}/2$, so that $0<\varepsilon'<\min\{1,\varepsilon\}$. Choose $N$ with $\bar\rho(f,f_{n})<\varepsilon'$ for $n\ge N$. For $n\ge N$ and any $x\in X$ we then have $\min\{\abs{f_{n}(x)-f(x)},1\}<\varepsilon'<1$, which forces $\abs{f_{n}(x)-f(x)}<\varepsilon'$: if the minimum were $\abs{f_{n}(x)-f(x)}$ we are done, and it cannot be $1$. Hence $\abs{f_{n}(x)-f(x)}<\varepsilon$ for all $x$ and all $n\ge N$, which is uniform convergence.
:::

:::

::: {.pf-step}
The equivalence holds.

::: pf-proof
Steps [](#uniform-implies){.pf-ref} and [](#metric-implies){.pf-ref} are the two implications.
:::

:::

:::
:::
