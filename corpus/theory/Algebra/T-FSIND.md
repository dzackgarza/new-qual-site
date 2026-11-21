---
schema: qual/card@1
id: T-FSIND
kind: theorem
title: The Frobenius--Schur theorem and the three types of irreducible representations
slogan: 'a real-valued character is realizable over $\RR$ exactly when the invariant bilinear form is symmetric'
classification:
  areas:
  - algebra
  topics:
  - Character Theory
  - Real Representations
relations: []
review: draft
---

::: {.theorem}
Let $\rho\colon G\to\GL(V)$ be an irreducible representation of a finite group over $\CC$ with character $\chi$.
Then $\chi$ takes real values if and only if $V$ has a nondegenerate $G$-invariant bilinear form, and $\rho$ is realizable over $\RR$ if and only if $V$ has a nondegenerate symmetric $G$-invariant bilinear form.
Such a form, when it exists, is unique up to homothety, and it is either symmetric or alternating; it is symmetric exactly when the representation is realizable over $\RR$.

So an irreducible representation over $\CC$ is of exactly one of three types: its character is not real-valued; its character is real-valued and the representation is realizable over $\RR$; or its character is real-valued, the representation is not realizable over $\RR$, and its restriction of scalars to $\RR$ has the quaternions as commuting algebra.

This is [@Ser77, sec. 13.2, Theorem 31 and Proposition 38].
:::

::: {.remark}
Irreducibility is needed for the uniqueness of the form and for the symmetric-alternating dichotomy.
For the representation $1\oplus1$ of a finite group on $\CC^2$, the invariant bilinear forms are all bilinear forms on $\CC^2$: the symmetric forms with matrices $\operatorname{diag}(1,1)$ and $\operatorname{diag}(1,2)$ are nondegenerate and are not homothetic, and the form with matrix $\begin{pmatrix}1&1\\0&1\end{pmatrix}$ is nondegenerate and is neither symmetric nor alternating.
:::
