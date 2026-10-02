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
\[
A=
\begin{bmatrix}
2&-4\\
-1&-1
\end{bmatrix}.
\]
Find the characteristic polynomial of \(A\), then find its eigenvalues and associated eigenvectors.
:::

::: {.solution}
Use the convention \(\chi_A(\lambda)=\det(\lambda I-A)\).

<1>1. The characteristic polynomial is
\[
\boxed{\chi_A(\lambda)=\lambda^2-\lambda-6=(\lambda-3)(\lambda+2)}.
\]

::: {.proof}
Directly,
\[
\chi_A(\lambda)
=\det\begin{bmatrix}\lambda-2&4\\1&\lambda+1\end{bmatrix}
=(\lambda-2)(\lambda+1)-4
=\lambda^2-\lambda-6.
\]
Factoring gives the displayed form.
:::

<1>2. The eigenvalues are \(\boxed{3\text{ and }-2}\), with eigenspaces
\[
\boxed{E_3=\operatorname{span}\{(-4,1)\},\qquad E_{-2}=\operatorname{span}\{(1,1)\}}.
\]

::: {.proof}
By step <1>1, the eigenvalues are the roots \(3\) and \(-2\). For \(\lambda=3\),
\[
(A-3I)\begin{bmatrix}x\\y\end{bmatrix}=0
\quad\Longleftrightarrow\quad
x+4y=0,
\]
so the nonzero eigenvectors are the nonzero multiples of \((-4,1)\). For \(\lambda=-2\),
\[
(A+2I)\begin{bmatrix}x\\y\end{bmatrix}=0
\quad\Longleftrightarrow\quad
x-y=0,
\]
so the nonzero eigenvectors are the nonzero multiples of \((1,1)\).
:::

<1>3. Q.E.D.

::: {.proof}
Steps <1>1 and <1>2 give the characteristic polynomial, its eigenvalues, and all associated eigenvectors.
:::
:::
