---
schema: qual/card@1
id: P-F12NA
kind: problem
title: $N(A^t A)=N(A)$
classification:
  areas:
  - prelim
  topics:
  - Matrices
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
---

::: {.problem}
Let $A$ be an $m \times n$ real matrix.
Write $A^t$ for the transpose of $A$, and $N(A)$ for the nullspace of $A$.
Prove that $N(A^t A) = N(A)$.
:::

::: {.solution}

No retained solution set covers this exercise: the card's own argument follows, with the two inclusions as separate steps and the norm identity used in the second.

Let $A$ be an $m\times n$ real matrix and $N(A)=\theset{x\in\RR^{n}\mid Ax=0}$.

::: pf

::: {.pf-step #easy}
$N(A)\subseteq N(A^{t}A)$.

::: pf-proof
If $x\in N(A)$ then $Ax=0$, so $A^{t}(Ax)=A^{t}0=0$, that is $A^{t}Ax=0$ and $x\in N(A^{t}A)$.
:::

:::

::: {.pf-step #hard}
$N(A^{t}A)\subseteq N(A)$.

::: pf-proof
Let $A^{t}Ax=0$. Multiplying on the left by $x^{t}$ gives $0=x^{t}A^{t}Ax=(Ax)^{t}(Ax)$, which is the squared euclidean norm of the vector $Ax$; a sum of squares of real numbers that vanishes has every term zero, so $Ax=0$ and $x\in N(A)$.
:::

:::

::: {.pf-qed}
The two inclusions of steps [](#easy){.pf-ref} and [](#hard){.pf-ref} give $N(A^{t}A)=N(A)$.
:::

:::

:::
