---
schema: qual/card@1
id: P-G3BXN
kind: problem
title: Principal and prime ideals in $\CC[x,y]$
classification:
  areas:
  - algebra
  topics:
  - Principal Ideal Domains
  - Prime Ideals
  - Polynomials
relations: []
review: draft
audit:
- event: solution-written
  by: OpenAI
  date: 2026-09-09
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-09
---

::: problem
Is $\CC[x, y]$ a PID? Is \( \gens{ x, y }  \) a prime ideals in it?
:::


::: {.solution}
<1>1. The ring $\CC[x,y]$ is not a PID.
::: {.proof}
Consider the ideal
\[
(x,y).
\]
If it were principal, say $(x,y)=(f)$, then $f$ would divide both $x$ and $y$. Since $\CC[x,y]$ is a UFD and $x,y$ are nonassociate irreducibles, every common divisor of $x$ and $y$ is a unit. Thus $f$ would be a unit, forcing $(x,y)=\CC[x,y]$, contradiction because $1\notin(x,y)$.
:::

<1>2. The ideal $(x,y)$ is maximal, hence prime.
::: {.proof}
Evaluation at the origin gives a surjective homomorphism
\[
\CC[x,y]\to\CC,
\qquad
f(x,y)\mapsto f(0,0),
\]
whose kernel is exactly $(x,y)$. Therefore
\[
\CC[x,y]/(x,y)\cong\CC,
\]
a field. Hence $(x,y)$ is maximal and therefore prime.
:::
:::
