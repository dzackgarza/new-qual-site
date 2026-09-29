---
schema: qual/card@1
id: P-BERK83SU-06
kind: problem
title: Adding twice one oriented orthonormal basis to another preserves orientation
classification: {areas: [prelim], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
- event: solution-written
  by: chatgpt
  date: 2026-09-21
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-21
  note: >-
    Relative to the a-basis, the b-basis is represented by a matrix
    Q in SO(n), and the vectors a_i+2b_i are the columns of I+2Q.
    The eigenvalues of Q have modulus one; nonreal eigenvalues occur in
    conjugate pairs, and the multiplicity of -1 is even because det Q=1.
    Hence every spectral factor in det(I+2Q) contributes positively in
    pairs, so this determinant is positive.
---

::: {.problem}
Let $V$ be a real $n$-dimensional inner-product space. Two bases are said to have the same orientation when the corresponding change-of-basis matrix has positive determinant.

Suppose $(a_i)$ and $(b_i)$ are orthonormal bases with the same orientation. Prove that
\[
(a_i+2b_i)_{i=1}^n
\]
is again a basis of $V$, with the same orientation as $(a_i)$.
:::

::: {.solution}
Let $Q=(q_{ji})$ be the change-of-basis matrix determined by
$$
b_i=\sum_{j=1}^n q_{ji}a_j.
$$

::: pf

::: {.pf-step #s1}

The matrix $Q$ is orthogonal and
$$
\det Q=1.
$$

::: pf-proof

Because $(a_i)$ is orthonormal,
$$
\inner{b_i}{b_k}
=
\sum_{j=1}^n q_{ji}q_{jk}.
$$
Since $(b_i)$ is also orthonormal, this equals $\delta_{ik}$.
Therefore
$$
Q^TQ=I.
$$
Thus $Q$ is orthogonal, so
$$
(\det Q)^2=1.
$$
The two bases have the same orientation, so their change-of-basis
determinant is positive. Hence $\det Q=1$.

:::

:::

::: {.pf-step #s2}

Relative to the basis $(a_i)$, the vectors
$$
c_i=a_i+2b_i
$$
are the columns of
$$
C=I+2Q.
$$

::: pf-proof

Using the definition of $Q$,
$$
\begin{aligned}
c_i
&=
a_i+2b_i\\
&=
\sum_{j=1}^n
(\delta_{ji}+2q_{ji})a_j.
\end{aligned}
$$
Thus the $i$th coordinate column of $c_i$ is the $i$th column of
$I+2Q$.

:::

:::

::: {.pf-step #s3}

Every complex eigenvalue $\lambda$ of $Q$ satisfies
$$
\abs{\lambda}=1,
$$
and the nonreal eigenvalues occur in conjugate pairs.

::: pf-proof

If $Qv=\lambda v$ for a nonzero $v\in\CC^n$, then orthogonality of
$Q$ implies
$$
\norm{Qv}=\norm{v}.
$$
Hence
$$
\abs{\lambda}\norm{v}
=
\norm{\lambda v}
=
\norm{Qv}
=
\norm{v},
$$
so $\abs{\lambda}=1$. Since $Q$ has real entries, its characteristic
polynomial has real coefficients, and therefore every nonreal root
occurs together with its complex conjugate.

:::

:::

::: {.pf-step #s4}

The multiplicity of the eigenvalue $-1$ of $Q$ is even.

::: pf-proof

An orthogonal matrix is normal, hence diagonalizable over $\CC$.
Its determinant is the product of its eigenvalues, counted with
multiplicity. By step [](#s3){.pf-ref}, every nonreal conjugate pair
$\lambda,\overline\lambda$ contributes
$$
\lambda\overline\lambda
=
\abs{\lambda}^2
=1
$$
to that product. The eigenvalue $1$ also contributes $1$. If $m$ is
the multiplicity of $-1$, step [](#s1){.pf-ref} therefore gives
$$
1=\det Q=(-1)^m.
$$
Thus $m$ is even.

:::

:::

::: {.pf-step #s5}

One has
$$
\det(I+2Q)>0.
$$

::: pf-proof

Because $Q$ is diagonalizable over $\CC$, the eigenvalues of $I+2Q$
are $1+2\lambda$, where $\lambda$ ranges over the eigenvalues of $Q$.
For a nonreal conjugate pair
$\lambda,\overline\lambda$, the corresponding factors satisfy
$$
(1+2\lambda)(1+2\overline\lambda)
=
\abs{1+2\lambda}^2
>0.
$$
An eigenvalue $\lambda=1$ contributes the positive factor $3$. An
eigenvalue $\lambda=-1$ contributes the factor $-1$, and step [](#s4){.pf-ref}
shows that the number of these factors is even. Hence their total
product is positive. Therefore
$$
\det(I+2Q)>0.
$$

:::

:::

::: {.pf-step #s6}

The vectors $(a_i+2b_i)_{i=1}^n$ form a basis with the same
orientation as $(a_i)$.

::: pf-proof

By step [](#s2){.pf-ref}, their coordinate matrix relative to $(a_i)$ is $I+2Q$.
Step [](#s5){.pf-ref} gives
$$
\det(I+2Q)>0.
$$
In particular, this matrix is invertible, so its columns form a basis.
Its positive determinant says precisely that this basis has the same
orientation as $(a_i)$.

:::

:::

::: pf-qed

Step [](#s6){.pf-ref} is the required conclusion.

:::

:::

:::
