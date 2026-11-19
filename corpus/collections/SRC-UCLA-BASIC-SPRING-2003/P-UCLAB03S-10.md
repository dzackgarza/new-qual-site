---
schema: qual/card@1
id: P-UCLAB03S-10
kind: problem
title: A self-adjoint operator with trace-zero square vanishes
classification:
  areas: [prelim]
  topics:
  - Self-Adjoint Operators
  - Trace
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Problem 10 of the official UCLA Basic Examination, May 2003 PDF. The source calls $T$ hermitian on a real inner-product space and refers to a matrix in the "standard basis" although an arbitrary inner-product space has no distinguished standard basis; the invariant content is $\operatorname{tr}(T^2)=0$.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Gives a basis-independent proof using an arbitrary orthonormal basis and self-adjointness.
- event: solution-written
  by: claude
  date: 2026-11-19
  note: >-
    Lamport structure over the prose that was already there. The trace is computed in an orthonormal basis, the
    self-adjointness is used to move $T$ inside the inner product, and the vanishing of a sum of squares is
    what forces each $Te_i$ to vanish. Not checked: the UCLA problem set, which the collection retains as a
    problem file only; the statement is as transcribed on the card. No retained solution set covers the
    exercise, so the argument is the card's own. No statement repair.
---

::: {.problem}
Let $V$ be a finite-dimensional real inner-product space and let $T:V\to V$ be self-adjoint.
Suppose
$$
\operatorname{tr}(T^2)=0.
$$
Prove that $T$ is the zero operator.
:::

::: {.solution}
No retained solution set covers this exercise: the collection's provenance is the problem set alone, so the argument is the card's own. Let $V$ be a finite-dimensional real inner-product space, $T:V\to V$ self-adjoint, that is $\langle Tu,v\rangle=\langle u,Tv\rangle$ for all $u,v$, and suppose $\operatorname{tr}(T^2)=0$.

::: pf

::: {.pf-step #trace}
For every orthonormal basis $e_1,\dots,e_n$, $\operatorname{tr}(T^2)=\sum_{i=1}^{n}\langle T^2e_i,e_i\rangle$.

::: pf-proof
The trace of an operator is the sum of the diagonal entries of its matrix in any basis, and in an orthonormal basis the $(i,i)$ entry of the matrix of $T^2$ is $\langle T^2e_i,e_i\rangle$. The trace does not depend on the choice of basis.
:::

:::

::: {.pf-step #selfadjoint}
$\langle T^2e_i,e_i\rangle=\langle Te_i,Te_i\rangle=\norm{Te_i}^2$ for each $i$.

::: pf-proof
$T$ is self-adjoint, so $\langle T(Te_i),e_i\rangle=\langle Te_i,Te_i\rangle$ by moving $T$ to the other side of the inner product, using symmetry of $\langle\cdot,\cdot\rangle$ once. And $\langle Te_i,Te_i\rangle=\norm{Te_i}^2$ by the definition of the norm.
:::

:::

::: {.pf-step #zero}
$T=0$.

::: pf-proof
From steps [](#trace){.pf-ref} and [](#selfadjoint){.pf-ref}, $0=\operatorname{tr}(T^2)=\sum_i\norm{Te_i}^2$. A sum of non-negative real numbers is zero only when each term is zero, so $Te_i=0$ for every $i$; since $e_1,\dots,e_n$ span $V$, $Tv=0$ for every $v\in V$.
:::

:::

:::

:::
