---
schema: qual/card@1
id: P-UCLAB15F-09
kind: problem
title: Nonnegative determinant of a real skew-symmetric matrix
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Transcribed from the retained UCLA Basic Examination, Fall 2015, `assets/attachments/basic-15F.pdf`; the PDF is image-only and the preserved extraction supplies the statement text.
---

::: {.problem}
Let $A$ be an $n\times n$ real matrix satisfying $A^T=-A$.
Prove that
\[
\det(A)\ge0.
\]
:::

::: {.solution}
View $A$ as a complex matrix acting on $\mathbb C^n$.

<1>1. Every eigenvalue of $A$ is purely imaginary.

::: {.proof}
Let
\[
Av=\lambda v,
\qquad
v\ne0,
\]
with $v\in\mathbb C^n$.
Using the standard Hermitian inner product,
\[
v^*Av
=
\lambda\,v^*v.
\]
Since $A$ is real and
\[
A^T=-A,
\]
one has
\[
A^*=A^T=-A.
\]
Therefore
\[
\overline{v^*Av}
=
v^*A^*v
=
-v^*Av.
\]
Thus
\[
v^*Av
\]
is purely imaginary.
Because
\[
v^*v>0
\]
is real, the identity
\[
v^*Av
=
\lambda\,v^*v
\]
forces
\[
\lambda
\]
to be purely imaginary.
:::

<1>2. The nonzero eigenvalues occur in conjugate pairs
\[
i\mu,\ -i\mu
\]
with $\mu\in\mathbb R\setminus\{0\}$.

::: {.proof}
The characteristic polynomial of $A$ has real coefficients.
Hence if $\lambda$ is a nonreal root, then its complex conjugate $\overline\lambda$ is also a root with the same algebraic multiplicity.
By step <1>1, every nonzero eigenvalue has the form
\[
i\mu
\]
with $\mu\in\mathbb R\setminus\{0\}$, and its conjugate is
\[
-i\mu.
\]
:::

<1>3. If $0$ is an eigenvalue of $A$, then
\[
\det(A)=0.
\]

::: {.proof}
A matrix is singular exactly when $0$ is an eigenvalue.
Thus the determinant vanishes.
:::

<1>4. If $0$ is not an eigenvalue, then
\[
\det(A)>0.
\]

::: {.proof}
By step <1>2, the eigenvalues can be grouped into conjugate pairs
\[
i\mu_j,\ -i\mu_j.
\]
The determinant is the product of the eigenvalues counted with algebraic multiplicity.
Each pair contributes
\[
(i\mu_j)(-i\mu_j)
=
\mu_j^2
>
0.
\]
Thus the full product is positive.
:::

<1>5. Therefore
\[
\boxed{\det(A)\ge0}.
\]

::: {.proof}
If $0$ is an eigenvalue, apply step <1>3.
Otherwise apply step <1>4.
These cases exhaust all possibilities.
:::

<1>6. Q.E.D.

::: {.proof}
Step <1>5 is the required conclusion.
:::
:::
