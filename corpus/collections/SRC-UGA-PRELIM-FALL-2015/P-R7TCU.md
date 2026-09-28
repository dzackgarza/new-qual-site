---
schema: qual/card@1
id: P-R7TCU
kind: problem
title: A $3\times 3$ matrix with eigenvalues $-1,0,1$ satisfies $A^3=A$
classification:
  areas:
  - prelim
  topics:
  - Minimal and Characteristic Polynomials
  - Matrices
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-25
- event: solution-reviewed
  by: claude-opus-5
  date: 2026-09-16
  note: Replaced two overlapping solutions with one structured proof.
---

::: {.problem}
Suppose $A$ is a $3\times3$ matrix with real entries and eigenvalues $-1$, $0$, and $1$.
Prove that $A^3=A$.
:::

::: {.solution}
<1>1. The characteristic polynomial of $A$ is $p_A(x)=x^3-x$.
::: {.proof}
$p_A(x)=\det(xI-A)$ is monic of degree $3$, and its roots in $\mathbb C$ are the eigenvalues of $A$.
The three eigenvalues $-1,0,1$ are distinct, so they are all the roots, each simple, and $p_A(x)=(x+1)x(x-1)=x^3-x$.
:::

<1>2. $A^3=A$.
::: {.proof}
By the Cayley--Hamilton theorem $p_A(A)=0$, that is, $A^3-A=0$ by <1>1.
:::
:::
