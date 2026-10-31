---
schema: qual/card@1
id: P-UGA-CA-SPRING-2005-4
kind: problem
title: Laurent expansions of $z/(1-z^2)$ about one and infinity
classification:
  areas:
  - complex-analysis
  topics:
  - Laurent Series
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-10-31
  note: Read complex-analysis Problem 4 in the checked-in extraction of the combined January 2005 exam.
---

::: {.problem}
State the Laurent-series existence theorem.
Find the Laurent series of
$z/(1-z^2)$ on $0<\abs{z-1}<1$
and on $1<\abs{z}<\infty$.
:::

::: {.solution}

If $f$ is holomorphic on
$r<\abs{z-a}<R$, it has a unique
Laurent expansion
$$
f(z)=\sum_{n\in\ZZ}c_n(z-a)^n,
\qquad
c_n=\frac{1}{2\pi i}
\int_{\abs{\zeta-a}=\rho}
\frac{f(\zeta)}{(\zeta-a)^{n+1}}\,d\zeta,
$$
where $r<\rho<R$. The series converges
absolutely and uniformly on each compact
subannulus.

Put $w=z-1$. Partial fractions give
$$
\frac{z}{1-z^2}
=-\frac{1}{2w}-\frac{1}{2(2+w)}
=-\frac{1}{2w}
-\frac14\sum_{n=0}^{\infty}
\left(-\frac w2\right)^n.
$$
The geometric series converges for
$\abs{w}<2$, hence on the requested
punctured disk $0<\abs{z-1}<1$.

For $\abs{z}>1$,
$$
\frac{z}{1-z^2}
=-\frac{z^{-1}}{1-z^{-2}}
=-\sum_{n=0}^{\infty}z^{-(2n+1)}.
$$
This is the Laurent series on the
requested exterior annulus.
:::
