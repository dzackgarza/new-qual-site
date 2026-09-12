---
schema: qual/card@1
id: P-TOP-WORKSHOP-D2-W3
kind: problem
title: Image of a path-connected space under a continuous map (verbatim warm-up)
classification:
  areas:
  - topology
  topics:
  - Connectedness
  - Continuity
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: >-
    Checked against the third warm-up in assets/attachments/Day_2_-_Connectedness_Problems.pdf.
    The source prints f(x), a point, where the intended image f(X) is clear.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: {.problem}
(Purdue ’10) Prove or disprove: If $X$ is path connected, and $f:X\to Y$ is continuous, then $f(x)$ is path connected.
:::

::: {.solution}
As printed, $f(x)$ denotes a single point, so the intended assertion is that the image $f(X)$ is path connected.
That assertion is true.

<1>1. Let $y_0,y_1\in f(X)$.
Choose $x_0,x_1\in X$ with
\[
f(x_0)=y_0,
\qquad
f(x_1)=y_1.
\]
::: {.proof}
This is the definition of membership in the image $f(X)$.
:::

<1>2. There exists a path
\[
\gamma:[0,1]\to X
\]
with $\gamma(0)=x_0$ and $\gamma(1)=x_1$.
::: {.proof}
The space $X$ is path connected.
:::

<1>3. The composite
\[
f\circ\gamma:[0,1]\to f(X)
\]
is a path from $y_0$ to $y_1$.
::: {.proof}
The composite is continuous because both $\gamma$ and $f$ are continuous, and its image lies in $f(X)$.
Moreover,
\[
(f\circ\gamma)(0)=f(x_0)=y_0,
\qquad
(f\circ\gamma)(1)=f(x_1)=y_1.
\]
:::

<1>4. Therefore $f(X)$ is path connected.
::: {.proof}
The points $y_0,y_1\in f(X)$ in <1>1 were arbitrary, and <1>3 constructs a path between them.
:::
:::
