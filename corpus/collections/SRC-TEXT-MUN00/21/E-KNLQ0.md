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
---

::: {.exercise}

Let $X$ be a set, and let $f_n: X \to \RR$ be a sequence of functions.
Let $\bar{\rho}$ be the uniform metric on the space $\RR^X$.
Show that the sequence $(f_n)$ converges uniformly to the function $f: X \to \RR$ if and only if the sequence $(f_n)$ converges to $f$ as elements of the metric space $(\RR^X, \bar{\rho})$.
:::

::: {.solution}
The complete published solution is **"positron0802", *Solutions to Topology, Chapter 2* (1 January 2021), Exercise 21.7, PDF p. 25** (`tmp/sources/munkres-solutions-positron-ch2.pdf`); both directions are theirs.

Recall $\bar\rho(f,g)=\sup_{x\in X}\min\{\abs{f(x)-g(x)},1\}$ on $\RR^{X}$.

*Uniform convergence implies convergence in the uniform metric.* Suppose $f_{n}\to f$ uniformly: given $\varepsilon>0$ there is $N$ with $\abs{f_{n}(x)-f(x)}<\varepsilon/2$ for all $x\in X$ and $n\ge N$. Then for $n\ge N$, since $\varepsilon/2<1$ once $\varepsilon<2$,
$$
\bar\rho(f,f_{n})=\sup_{x}\min\{\abs{f(x)-f_{n}(x)},1\}\le\varepsilon/2<\varepsilon,
$$
so $f_{n}\to f$ in $(\RR^{X},\bar\rho)$.

*Convergence in the uniform metric implies uniform convergence.* Suppose $\bar\rho(f,f_{n})\to0$ and let $\varepsilon>0$; choose $0<\varepsilon'<\min\{1,\varepsilon\}$ and then $N$ with $\bar\rho(f,f_{n})<\varepsilon'$ for $n\ge N$. For $n\ge N$ and every $x\in X$, $\min\{\abs{f(x)-f_{n}(x)},1\}<\varepsilon'<1$, so $\min$ may be dropped and $\abs{f(x)-f_{n}(x)}<\varepsilon'<\varepsilon$. As $\varepsilon$ and $x$ were arbitrary, $f_{n}\to f$ uniformly.
:::
