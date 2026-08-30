---
schema: qual/card@1
id: P-UU43Q
kind: problem
title: Path-independence of $\int_C (x+y^3)\,dx+(e^y+3xy^2)\,dy$
classification:
  areas:
  - prelim
  topics:
  - Line Integrals
relations: []
review: draft
audit:
- event: solution-written
  by: Codex 5.3 Spark Extra High
  date: 2026-08-30
---

::: {.problem}
Prove that the line integral $\displaystyle\int_C (x+y^3)\,dx + (e^y+3xy^2)\,dy$ is path-independent; i.e., it depends only on the endpoints of $C$.
:::

::: solution
**Goal:** Check exactness via equal mixed partials and write a potential function.

<1> Let
    $$
    M(x,y)=x+y^3,\qquad N(x,y)=e^y+3xy^2.
    $$
    Then
    $$
    \frac{\partial M}{\partial y}=3y^2,\qquad
    \frac{\partial N}{\partial x}=3y^2.
    $$
    Since the domain is $\mathbb R^2$, which is simply connected, equality of mixed partials implies exactness.

<1> Integrate $M$ in $x$:
    $$
    F(x,y)=\frac{x^2}{2}+xy^3+h(y).
    $$
    Differentiate in $y$ and compare with $N$:
    $$
    \frac{\partial F}{\partial y}=3xy^2+h'(y)=e^y+3xy^2
    \implies h'(y)=e^y.
    $$
    So $h(y)=e^y$ (up to a constant).

<1> Therefore $F(x,y)=\frac{x^2}{2}+xy^3+e^y$ satisfies
    $dF=M\,dx+N\,dy$, and
    $$
    \int_C (x+y^3)\,dx+(e^y+3xy^2)\,dy=F(\text{end})-F(\text{start}).
    $$
    The integral depends only on endpoints.

Authored by **Codex 5.3 Spark Extra High**.
:::
