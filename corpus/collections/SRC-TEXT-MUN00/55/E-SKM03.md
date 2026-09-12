---
schema: qual/card@1
id: E-SKM03
kind: problem
title: Positive eigenvalues for nonnegative matrices
classification:
  areas:
  - topology
  topics:
  - Fundamental Group
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-10
---

::: {.exercise}

Show that if $A$ is a nonsingular 3 by 3 matrix having nonnegative entries, then $A$ has a positive real eigenvalue.
:::

::: {.solution}
Let
\[
\Delta^2=\{x=(x_1,x_2,x_3)\in\mathbb R^3:x_i\ge0,\ x_1+x_2+x_3=1\}
\]
be the standard \(2\)-simplex. Since \(A\) has nonnegative entries, \(Ax\) has nonnegative coordinates for every \(x\in\Delta^2\). Since \(A\) is nonsingular and \(x\ne0\), we also have \(Ax\ne0\). Hence
\[
s(x)=\sum_{i=1}^3(Ax)_i>0.
\]
Define
\[
F:\Delta^2\to\Delta^2,
\qquad
F(x)=\frac{Ax}{s(x)}.
\]
This map is continuous. By the Brouwer fixed-point theorem, there exists \(x\in\Delta^2\) with \(F(x)=x\). Therefore
\[
Ax=s(x)x.
\]
Thus \(x\ne0\) is an eigenvector of \(A\) with real eigenvalue
\[
\lambda=s(x)>0.
\]
Hence every nonsingular \(3\times3\) matrix with nonnegative entries has a positive real eigenvalue.
:::
