---
schema: qual/card@1
id: P-BERK77S-09
kind: problem
title: Every orientation-preserving orthogonal map of $\mathbb R^3$ has an axis
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
  note: The retained PDF confirms that A is a 3-by-3 real matrix; the extraction garbled the size.
- event: solution-written
  by: chatgpt
  date: 2026-09-21
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-21
  note: >-
    Orthogonality gives det A=±1, and the positive determinant hypothesis
    makes det A=1. Then det(A-I)=det(A^{-1}-I)=det(I-A)=-det(A-I) in odd
    dimension, so det(A-I)=0 and A fixes a nonzero vector.
---

::: {.problem}
Show that every rotation of $\mathbb R^3$ has an axis. More precisely, let $A$ be a real $3\times3$ matrix such that
\[
A^T=A^{-1},
\qquad \det A>0.
\]
Prove that there is a nonzero vector $v$ such that $Av=v$.
:::

::: {.solution}
<1>1. One has
$$
\det A=1.
$$

::: {.proof}
From
$$
A^T=A^{-1},
$$
taking determinants gives
$$
\det A
=
\det A^T
=
\det A^{-1}
=
\frac1{\det A}.
$$
Thus
$$
(\det A)^2=1.
$$
Since $\det A>0$ by hypothesis, $\det A=1$.
:::

<1>2. The determinant of $A-I$ satisfies
$$
\det(A-I)=-\det(A-I).
$$

::: {.proof}
Using invariance of the determinant under transpose,
$$
\det(A-I)
=
\det(A^T-I).
$$
Since $A^T=A^{-1}$,
$$
\det(A^T-I)
=
\det(A^{-1}-I).
$$
Factor
$$
A^{-1}-I=A^{-1}(I-A),
$$
so step <1>1 gives
$$
\det(A^{-1}-I)
=
\det(A^{-1})\det(I-A)
=
\det(I-A).
$$
Because the matrices are $3\times3$,
$$
\det(I-A)
=
\det(-(A-I))
=
(-1)^3\det(A-I)
=
-\det(A-I).
$$
Combining these equalities proves the claim.
:::

<1>3. The matrix $A-I$ is singular.

::: {.proof}
Step <1>2 gives
$$
2\det(A-I)=0.
$$
Over $\RR$, this implies
$$
\det(A-I)=0.
$$
Hence $A-I$ is singular.
:::

<1>4. There is a nonzero vector $v\in\RR^3$ such that
$$
\boxed{
Av=v.
}
$$

::: {.proof}
Since $A-I$ is singular by step <1>3, its kernel contains a nonzero vector
$v$. Then
$$
(A-I)v=0,
$$
which is equivalent to $Av=v$.
:::

<1>5. Q.E.D.

::: {.proof}
Step <1>4 gives the required axis direction.
:::
:::
