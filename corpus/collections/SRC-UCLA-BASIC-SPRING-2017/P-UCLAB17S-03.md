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

::: pf

::: {.pf-step #s1-1}

Since $M$ is orthogonal and symmetric,
$$
\boxed{M^2=I}.
$$


::: pf-proof

Orthogonality gives
$$
M^TM=I.
$$
Symmetry gives
$$
M^T=M.
$$
Therefore
$$
M^2=I.
$$

:::

:::

::: {.pf-step #s1-2}

Every eigenvalue of $M$ is either
$$
\boxed{1}
\qquad\text{or}\qquad
\boxed{-1}.
$$


::: pf-proof

Let
$$
Mv=\lambda v
$$
with
$$
v\ne0.
$$
Applying step [](#s1-1){.pf-ref},
$$
v
=
M^2v
=
\lambda^2v.
$$
Hence
$$
\lambda^2=1,
$$
so
$$
\lambda=\pm1.
$$

:::

:::

::: {.pf-step #s1-3}

Because $M$ is symmetric, it has an orthonormal basis of eigenvectors.


::: pf-proof

Apply the spectral theorem for real symmetric matrices.

:::

:::

::: {.pf-step #s1-4}

If $M$ is positive definite, then every eigenvalue of $M$ is positive.


::: pf-proof

Let
$$
Mv=\lambda v
$$
with
$$
v\ne0.
$$
Positive definiteness gives
$$
v^TMv>0.
$$
But
$$
v^TMv
=
\lambda\norm{v}_2^2.
$$
Since
$$
\norm{v}_2^2>0,
$$
one has
$$
\lambda>0.
$$

:::

:::

::: {.pf-step #s1-5}

Therefore, if $M$ is positive definite,
$$
\boxed{M=I}.
$$


::: pf-proof

By step [](#s1-2){.pf-ref}, every eigenvalue is $\pm1$.
By step [](#s1-4){.pf-ref}, every eigenvalue is positive.
Thus every eigenvalue equals $1$.

By step [](#s1-3){.pf-ref}, $M$ is orthogonally diagonalizable.
Its diagonal form is therefore
$$
I,
$$
so
$$
M=I.
$$
This proves part (a).

:::

:::

::: {.pf-step #s1-6}

If $M$ is only positive semidefinite, every eigenvalue satisfies
$$
\lambda\ge0.
$$


::: pf-proof

For an eigenvector $v$,
$$
v^TMv
=
\lambda\norm{v}_2^2.
$$
Positive semidefiniteness gives
$$
v^TMv\ge0.
$$
Since
$$
\norm{v}_2^2>0,
$$
one gets
$$
\lambda\ge0.
$$

:::

:::

::: {.pf-step #s1-7}

The conclusion does not change:
$$
\boxed{M=I}
$$
also under positive semidefiniteness.


::: pf-proof

Step [](#s1-2){.pf-ref} gives
$$
\lambda\in\{-1,1\}.
$$
Step [](#s1-6){.pf-ref} rules out $-1$.
Thus all eigenvalues are again $1$.
Using the orthonormal eigenbasis from step [](#s1-3){.pf-ref} gives
$$
M=I.
$$

:::

:::

::: pf-qed

Step [](#s1-5){.pf-ref} proves part (a), and step [](#s1-7){.pf-ref} answers part (b).

:::

:::

:::
