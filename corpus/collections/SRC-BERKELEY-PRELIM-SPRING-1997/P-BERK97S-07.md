---
schema: qual/card@1
id: P-BERK97S-07
kind: problem
title: $AB$ and $BA$ have the same eigenvalues but not the same eigenvectors
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
- event: solution-written
  by: chatgpt
  date: 2026-09-23
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-23
---

::: {.problem}
Let $A,B$ be endomorphisms of a finite-dimensional vector space $V$ over a field $K$. Prove or disprove:

1. Every eigenvector of $AB$ is also an eigenvector of $BA$.
2. Every eigenvalue of $AB$ is also an eigenvalue of $BA$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

Statement (1) is false.

::: pf-proof

Take $V=K^2$ with basis $e_1,e_2$, and define endomorphisms by
$$
A(e_1)=e_1,\qquad A(e_2)=0,
$$
and
$$
B(e_1)=e_2,\qquad B(e_2)=e_1.
$$
Then
$$
AB(e_1)=A(e_2)=0,
$$
so $e_1$ is an eigenvector of $AB$ with eigenvalue $0$. On the other hand,
$$
BA(e_1)=B(e_1)=e_2,
$$
which is not a scalar multiple of $e_1$. Thus $e_1$ is not an eigenvector of
$BA$.

:::

:::

::: {.pf-step #s2}

Every nonzero eigenvalue of $AB$ is an eigenvalue of $BA$.

::: pf-proof

Let $\lambda\neq 0$ be an eigenvalue of $AB$, and choose $0\neq v\in V$
such that
$$
ABv=\lambda v.
$$
Then $Bv\neq 0$, since otherwise $ABv=0$, contradicting
$\lambda v\neq 0$. Applying $B$ to the eigenvalue equation gives
$$
BA(Bv)
=
B(ABv)
=
\lambda Bv.
$$
Hence $Bv$ is a nonzero eigenvector of $BA$ with eigenvalue $\lambda$.

:::

:::

::: {.pf-step #s3}

If $0$ is an eigenvalue of $AB$, then $0$ is an eigenvalue of $BA$.

::: pf-proof

If $0$ is an eigenvalue of $AB$, then $AB$ is singular, so
$$
\det(AB)=0.
$$
By multiplicativity of the determinant,
$$
\det(BA)
=
\det(B)\det(A)
=
\det(A)\det(B)
=
\det(AB)
=
0.
$$
Thus $BA$ is singular and has a nonzero kernel. Therefore $0$ is an
eigenvalue of $BA$.

:::

:::

::: {.pf-step #s4}

Statement (2) is true.

::: pf-proof

Step [](#s2){.pf-ref} proves the claim for every nonzero eigenvalue of $AB$, and step
[](#s3){.pf-ref} proves it for the eigenvalue $0$.

:::

:::

::: pf-qed

Step [](#s1){.pf-ref} disproves statement (1), and step [](#s4){.pf-ref} proves statement (2).

:::

:::

:::
