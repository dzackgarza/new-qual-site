---
schema: qual/card@1
id: P-CHAVAN-CA-3-3
kind: problem
title: An analytic square root without an analytic logarithm
classification: {areas: [complex-analysis], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
---

::: {.problem}
Let
\[
\Omega=\mathbb C\setminus[-1,1],
\qquad
f(z)=z^2-1,
\]
and define
\[
g(z)=|f(z)|^{1/2}
\exp\!\left(\frac{i}{2}\bigl(\arg(z-1)+\arg(z+1)\bigr)\right),
\]
where $\arg$ is the principal argument.

1. Show that $g$ is well-defined and continuous on $\Omega$ and satisfies $g^2=f$.

2. Show that $g$ is analytic on $\Omega$.

3. Show that $f$ has no analytic logarithm on $\Omega$.
:::
