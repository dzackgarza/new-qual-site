---
schema: qual/card@1
id: P-BERK84S-13
kind: problem
title: Centralizer of a nonscalar 2-by-2 complex matrix
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against Problem 13 of the vendored Berkeley Preliminary Exam, Summer 1984.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Verified the cyclic-vector argument showing the centralizer is spanned by I and A.
---

::: {.problem}
Let A be a 2 $\times$ 2 matrix over C which is not a scalar multiple of the identity matrix I. Show that any 2 $\times$ 2 matrix X over C commuting with A has the form $X = \alpha I + \beta A$ , where $\alpha , \beta \in \mathbb { C }$
:::


::: {.solution}
<1>1. Since $A$ is not scalar, there is a vector $v\in\mathbb C^2$ such that $v$ and $Av$ are linearly independent.
::: {.proof}
Suppose instead that $Av\in\mathbb Cv$ for every nonzero $v$. Choose a basis $e_1,e_2$. Then
\[
Ae_1=\lambda e_1,
\qquad
Ae_2=\mu e_2
\]
for some $\lambda,\mu\in\mathbb C$. Since $e_1+e_2$ is also an eigenvector under the supposition,
\[
A(e_1+e_2)=\lambda e_1+\mu e_2
\]
must be a scalar multiple of $e_1+e_2$. Hence $\lambda=\mu$, so $A=\lambda I$, contradicting the hypothesis.

Therefore some $v$ has $v,Av$ linearly independent. Since the space has dimension $2$, the pair
\[
(v,Av)
\]
is a basis of $\mathbb C^2$.
:::

<1>2. Any matrix $X$ commuting with $A$ is of the form $\alpha I+\beta A$.
::: {.proof}
Let $X$ satisfy $XA=AX$. Using the basis from <1>1, write
\[
Xv=\alpha v+\beta Av
\]
for unique $\alpha,\beta\in\mathbb C$. Set
\[
Y=\alpha I+\beta A.
\]
Then
\[
Yv=\alpha v+\beta Av=Xv.
\]
Because both $X$ and $Y$ commute with $A$,
\[
Y(Av)=A(Yv)=A(Xv)=X(Av).
\]
Thus $X$ and $Y$ agree on the basis $v,Av$, so $X=Y$. Consequently
\[
\boxed{X=\alpha I+\beta A}.
\]
:::
:::
