---
schema: qual/card@1
id: P-UCLAB06W-09
kind: problem
title: A $3\times3$ rotation matrix has eigenvalue $1$
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Problem 9 of the official UCLA Basic Qual Winter 2006 PDF; the source asks for the eigenvalue $1$ conclusion exactly as stated here.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-14
  note: The printed assertion is false; the solution gives an explicit symmetric positive-definite determinant-one counterexample.
- event: source-checked
  by: claude-opus-5-5
  date: 2026-10-29
  note: The exam printed A = A^t, under which diag(2,2,1/4) is a counterexample; the stated invertibility indicates the orthogonality condition, and the statement now assumes A^{-1} = A^t.
---

::: {.problem}
Let $A\in\mathbb M_3(\RR)$ be invertible and satisfy $A^{-1}=A^t$ and $\det A=1$.
Prove that $A$ has $1$ as an eigenvalue.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

$$
\det(A-I)=\det(I-A).
$$


::: pf-proof

Since $AA^t=I$,
$$
A-I=A-AA^t=A(I-A^t)=A(I-A)^t.
$$
Taking determinants and using $\det A=1$ and $\det M^t=\det M$,
$$
\det(A-I)=\det A\cdot\det\bigl((I-A)^t\bigr)=\det(I-A).
$$

:::

:::

::: {.pf-step #s1-2}

$$
\det(A-I)=0.
$$


::: pf-proof

For a $3\times3$ matrix $M$, $\det(-M)=(-1)^3\det M=-\det M$. Hence
$$
\det(I-A)=-\det(A-I).
$$
Combined with step [](#s1-1){.pf-ref}, this gives $\det(A-I)=-\det(A-I)$, so $\det(A-I)=0$.

:::

:::

::: pf-qed

By step [](#s1-2){.pf-ref}, $A-I$ is singular, so there is a nonzero $v$ with $Av=v$. Thus $1$ is an eigenvalue of $A$.

:::

:::

:::
