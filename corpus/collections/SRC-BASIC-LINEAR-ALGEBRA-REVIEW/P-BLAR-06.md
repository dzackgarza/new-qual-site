---
schema: qual/card@1
id: P-BLAR-06
kind: problem
title: Characteristic polynomial, eigenvalues, and eigenvectors
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Review Problem 6 in the deterministic MinerU Flash extraction assets/attachments/Basic_Linear_Algebra_Review_extracted.md.
---

::: {.problem}
Let
$$
A=
\begin{bmatrix}
2&-4\\
-1&-1
\end{bmatrix}.
$$
Find the characteristic polynomial of $A$, then find its eigenvalues and associated eigenvectors.
:::

::: {.solution}
Use the convention $\chi_A(\lambda)=\det(\lambda I-A)$.

::: pf

::: {.pf-step #characteristic-polynomial}
The characteristic polynomial is
$$
\boxed{\chi_A(\lambda)=\lambda^2-\lambda-6=(\lambda-3)(\lambda+2)}.
$$

::: pf-proof
Directly,
$$
\chi_A(\lambda)
=\det\begin{bmatrix}\lambda-2&4\\1&\lambda+1\end{bmatrix}
=(\lambda-2)(\lambda+1)-4
=\lambda^2-\lambda-6.
$$
Factoring gives the displayed form.
:::

:::

::: pf-step
The eigenvalues are $\boxed{3\text{ and }-2}$, with eigenspaces
$$
\boxed{E_3=\operatorname{span}\{(-4,1)\},\qquad E_{-2}=\operatorname{span}\{(1,1)\}}.
$$

::: pf-proof
By [](#characteristic-polynomial){.pf-ref}, the eigenvalues are the roots $3$ and $-2$. For $\lambda=3$,
$$
(A-3I)\begin{bmatrix}x\\y\end{bmatrix}=0
\quad\Longleftrightarrow\quad
x+4y=0,
$$
so the nonzero eigenvectors are the nonzero multiples of $(-4,1)$. For $\lambda=-2$,
$$
(A+2I)\begin{bmatrix}x\\y\end{bmatrix}=0
\quad\Longleftrightarrow\quad
x-y=0,
$$
so the nonzero eigenvectors are the nonzero multiples of $(1,1)$.
:::

:::

:::

:::
