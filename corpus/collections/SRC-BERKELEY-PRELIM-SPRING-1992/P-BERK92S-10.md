---
schema: qual/card@1
id: P-BERK92S-10
kind: problem
title: Roots of the rank-one nilpotent matrix $E_{14}$
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
---

::: {.problem}
Let
\[
A=\begin{pmatrix}
0&0&0&1\\
0&0&0&0\\
0&0&0&0\\
0&0&0&0
\end{pmatrix}.
\]
For which positive integers $n$ does there exist a complex $4\times4$ matrix $X$ such that
\[
X^n=A?
\]
:::

::: {.solution}
Let $E_{ij}$ denote the matrix unit with a $1$ in position $(i,j)$.
Then $A=E_{14}$.

<1>1. Solutions exist for $n=1,2,3$.

::: {.proof}
For $n=1$, take $X=A$.

For $n=2$, take
$$
X=E_{12}+E_{24}.
$$
Using $E_{ij}E_{k\ell}=\delta_{jk}E_{i\ell}$ gives
$$
X^2=E_{12}E_{24}=E_{14}=A.
$$

For $n=3$, take
$$
X=E_{12}+E_{23}+E_{34}.
$$
Then
$$
X^2=E_{13}+E_{24},
\qquad
X^3=E_{14}=A.
$$
:::

<1>2. If $X^n=A$ for some positive integer $n$, then $X$ is
nilpotent.

::: {.proof}
Since $A^2=0$,
$$
X^{2n}=A^2=0.
$$
Thus $X$ is nilpotent.
:::

<1>3. No solution exists for $n\ge4$.

::: {.proof}
Every nilpotent endomorphism of a four-dimensional complex vector
space satisfies $X^4=0$; for example this follows from the
Cayley--Hamilton theorem, since its characteristic polynomial is
$t^4$. By step <1>2, any putative solution $X$ is nilpotent. Hence for
$n\ge4$,
$$
X^n=0,
$$
contradicting $X^n=A\ne0$.
:::

<1>4. The required positive integers are
$$
\boxed{n=1,2,3}.
$$

::: {.proof}
Step <1>1 gives existence for these three integers, and step <1>3
excludes every larger positive integer.
:::

<1>5. Q.E.D.

::: {.proof}
Step <1>4 is the complete classification.
:::
:::
