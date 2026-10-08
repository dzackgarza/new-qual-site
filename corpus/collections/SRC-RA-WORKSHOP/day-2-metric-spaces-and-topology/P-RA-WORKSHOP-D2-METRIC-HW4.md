---
schema: qual/card@1
id: P-RA-WORKSHOP-D2-METRIC-HW4
kind: problem
title: The parallelogram law for inner-product norms (warm-up)
classification:
  areas:
  - real-analysis
  topics:
  - Norms
  - Hilbert Spaces
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-25
---

::: {.problem}
Show that an inner product space satisfies the parallelogram law with its induced norm:
$$
\lVert x+y\rVert^2+\lVert x-y\rVert^2=2\lVert x\rVert^2+2\lVert y\rVert^2.
$$
(For simplicity, you may assume that this is an inner product space over $\mathbb R$.)
:::

::: {.solution}
<1>1. For all $x,y$ in a real inner product space,
\[
\lVert x+y\rVert^2=\lVert x\rVert^2+2\langle x,y\rangle+\lVert y\rVert^2,
\qquad
\lVert x-y\rVert^2=\lVert x\rVert^2-2\langle x,y\rangle+\lVert y\rVert^2.
\]

::: {.proof}
Expand $\langle x+y,x+y\rangle$ and $\langle x-y,x-y\rangle$ by bilinearity. The equality $\langle y,x\rangle=\langle x,y\rangle$ combines the two cross terms in each expression, and $\langle v,v\rangle=\lVert v\rVert^2$ identifies the diagonal terms.
:::

<1>2. The parallelogram identity holds:
\[
\boxed{\lVert x+y\rVert^2+\lVert x-y\rVert^2=2\lVert x\rVert^2+2\lVert y\rVert^2}.
\]

::: {.proof}
Add the two equalities in step <1>1. The terms $2\langle x,y\rangle$ and $-2\langle x,y\rangle$ cancel.
:::

<1>3. Q.E.D.

::: {.proof}
Step <1>2 is the required identity for arbitrary $x$ and $y$.
:::
:::
