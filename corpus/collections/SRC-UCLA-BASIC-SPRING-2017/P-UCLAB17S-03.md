---
schema: qual/card@1
id: P-UCLAB17S-03
kind: problem
title: Positive orthogonal symmetric matrices
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
  note: Checked against the vendored UCLA Basic Examination, Spring 2017, `assets/attachments/basic-17S.pdf`.
---

::: {.problem}
Let $M$ be a real matrix that is both orthogonal and symmetric.

(a) Prove that if $M$ is positive definite, then $M=I$.

(b) Does the conclusion change if $M$ is only positive semidefinite?
:::

::: {.solution}
<1>1. Since $M$ is orthogonal and symmetric,
\[
\boxed{M^2=I}.
\]

::: {.proof}
Orthogonality gives
\[
M^TM=I.
\]
Symmetry gives
\[
M^T=M.
\]
Therefore
\[
M^2=I.
\]
:::

<1>2. Every eigenvalue of $M$ is either
\[
\boxed{1}
\qquad\text{or}\qquad
\boxed{-1}.
\]

::: {.proof}
Let
\[
Mv=\lambda v
\]
with
\[
v\ne0.
\]
Applying step <1>1,
\[
v
=
M^2v
=
\lambda^2v.
\]
Hence
\[
\lambda^2=1,
\]
so
\[
\lambda=\pm1.
\]
:::

<1>3. Because $M$ is symmetric, it has an orthonormal basis of eigenvectors.

::: {.proof}
Apply the spectral theorem for real symmetric matrices.
:::

<1>4. If $M$ is positive definite, then every eigenvalue of $M$ is positive.

::: {.proof}
Let
\[
Mv=\lambda v
\]
with
\[
v\ne0.
\]
Positive definiteness gives
\[
v^TMv>0.
\]
But
\[
v^TMv
=
\lambda\|v\|_2^2.
\]
Since
\[
\|v\|_2^2>0,
\]
one has
\[
\lambda>0.
\]
:::

<1>5. Therefore, if $M$ is positive definite,
\[
\boxed{M=I}.
\]

::: {.proof}
By step <1>2, every eigenvalue is $\pm1$.
By step <1>4, every eigenvalue is positive.
Thus every eigenvalue equals $1$.

By step <1>3, $M$ is orthogonally diagonalizable.
Its diagonal form is therefore
\[
I,
\]
so
\[
M=I.
\]
This proves part (a).
:::

<1>6. If $M$ is only positive semidefinite, every eigenvalue satisfies
\[
\lambda\ge0.
\]

::: {.proof}
For an eigenvector $v$,
\[
v^TMv
=
\lambda\|v\|_2^2.
\]
Positive semidefiniteness gives
\[
v^TMv\ge0.
\]
Since
\[
\|v\|_2^2>0,
\]
one gets
\[
\lambda\ge0.
\]
:::

<1>7. The conclusion does not change:
\[
\boxed{M=I}
\]
also under positive semidefiniteness.

::: {.proof}
Step <1>2 gives
\[
\lambda\in\{-1,1\}.
\]
Step <1>6 rules out $-1$.
Thus all eigenvalues are again $1$.
Using the orthonormal eigenbasis from step <1>3 gives
\[
M=I.
\]
:::

<1>8. Q.E.D.

::: {.proof}
Step <1>5 proves part (a), and step <1>7 answers part (b).
:::
:::
