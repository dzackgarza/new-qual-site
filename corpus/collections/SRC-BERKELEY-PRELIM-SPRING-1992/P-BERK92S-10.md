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

::: pf

::: {.pf-step #s1}

Solutions exist for $n=1,2,3$.

::: pf-proof

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

:::

::: {.pf-step #s2}

If $X^n=A$ for some positive integer $n$, then $X$ is
nilpotent.

::: pf-proof

Since $A^2=0$,
$$
X^{2n}=A^2=0.
$$
Thus $X$ is nilpotent.

:::

:::

::: {.pf-step #s3}

No solution exists for $n\ge4$.

::: pf-proof

Every nilpotent endomorphism of a four-dimensional complex vector
space has characteristic polynomial $t^4$, so the Cayley--Hamilton
theorem gives $X^4=0$. By step [](#s2){.pf-ref}, any putative solution $X$ is nilpotent. Hence for
$n\ge4$,
$$
X^n=0,
$$
contradicting $X^n=A\ne0$.

:::

:::

::: {.pf-step #s4}

The required positive integers are
$$
\boxed{n=1,2,3}.
$$

::: pf-proof

Step [](#s1){.pf-ref} gives existence for these three integers, and step [](#s3){.pf-ref}
excludes every larger positive integer.

:::

:::

::: pf-qed

Step [](#s4){.pf-ref} is the complete classification.

:::

:::

:::
