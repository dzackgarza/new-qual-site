---
schema: qual/card@1
id: P-TRIV-LA14
kind: problem
title: Orthogonality of real matrices with $(\det A)^2=1$
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Linear Algebra, Problem 14, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md.
---

::: {.problem}
Let $A$ be a real matrix with $(\det A)^2 = 1$. Give a conclusion about orthogonality of $A$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

Every real orthogonal matrix satisfies
$$
(\det A)^2=1.
$$


::: pf-proof

If $A$ is orthogonal, then
$$
A^TA=I.
$$
Taking determinants gives
$$
\det(A^T)\det A=1.
$$
Since
$$
\det(A^T)=\det A,
$$
one obtains
$$
(\det A)^2=1.
$$

:::

:::

::: {.pf-step #s1-2}

The converse is false in dimension at least $2$.


::: pf-proof

Consider
$$
A=
\begin{pmatrix}
2&0\\
0&1/2
\end{pmatrix}.
$$
Then
$$
\det A=1,
$$
so
$$
(\det A)^2=1.
$$
However,
$$
A^TA
=
\begin{pmatrix}
4&0\\
0&1/4
\end{pmatrix}
\neq I.
$$
Thus $A$ is not orthogonal.

:::

:::

::: {.pf-step #s1-3}

Therefore the hypothesis implies only
$$
\boxed{\det A=\pm1},
$$
not that $A$ is orthogonal.


::: pf-proof

The equation
$$
(\det A)^2=1
$$
has the two real solutions
$$
\det A=1
\qquad\text{or}\qquad
\det A=-1.
$$
Step [](#s1-2){.pf-ref} shows that this determinant condition alone does not imply
orthogonality.

:::

:::

::: {.pf-step #s1-4}

In dimension $1$, the condition does imply orthogonality.


::: pf-proof

A real $1\times1$ matrix has the form $(a)$. The condition $a^2=1$ gives
$a=\pm1$, and then
$$
A^TA=(a^2)=(1).
$$

:::

:::

::: pf-qed

Steps [](#s1-1){.pf-ref} through [](#s1-4){.pf-ref} give the precise relation between the determinant condition
and orthogonality.

:::

:::

:::
