---
schema: qual/card@1
id: P-CAFA22F
kind: problem
title: "Polynomial minus exponential has infinitely many zeros"
classification:
  areas:
  - complex-analysis
  topics:
  - Complex Analysis
relations: []
review: draft
---

::: {.problem}
If $p \neq 0$ is a polynomial and $a \neq 0$ is a complex number, show that $p(z) - e^{az}$ has infinitely many zeros.
:::

::: {.solution}
Consider the meromorphic function
\[
F(z)=\frac{e^{az}}{p(z)}.
\]
At $\infty$, the function $F$ has an essential singularity: if it were
removable or a pole there, then $F$ would be rational, which is impossible
because $e^{az}$ is transcendental and $p$ is a nonzero polynomial.

By the Great Picard theorem, in every punctured neighborhood of $\infty$ the
function $F$ assumes every complex value, with at most one exception,
infinitely often. The value $0$ is omitted everywhere because $e^{az}$ never
vanishes. Therefore $0$ is the possible exceptional value, so $1$ is assumed
infinitely often.

At every point where $F(z)=1$ we have $p(z)\ne0$ and
\[
e^{az}=p(z).
\]
Hence $p(z)-e^{az}$ has infinitely many zeros.
:::
