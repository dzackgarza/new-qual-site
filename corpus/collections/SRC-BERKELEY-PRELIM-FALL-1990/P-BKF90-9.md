---
schema: qual/card@1
id: P-BKF90-9
kind: problem
title: Matrix of orthogonal projection onto a plane
classification: {areas: [prelim], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Problem 9 in the deterministic MinerU Flash extraction assets/attachments/Fall90_extracted.md.
- event: solution-written
  by: chatgpt
  date: 2026-09-25
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-25
  note: >-
    Wrote the plane as the orthogonal complement of the unit normal
    u=(a,b,c)^T and used the projection formula I-uu^T.
---

::: {.problem}
Let $(a,b,c)\in\mathbb R^3$ have length $1$, and let
\[
W=\{(x,y,z):ax+by+cz=0\}.
\]
Find, in the standard basis, the matrix of the orthogonal projection of $\mathbb R^3$ onto $W$.
:::

::: {.solution}
Let
$$
u\coloneqq
\begin{pmatrix}
a\\ b\\ c
\end{pmatrix}.
$$

::: pf

::: pf-step

One has
$$
W=u^\perp.
$$

::: pf-proof

For a vector
$$
v=
\begin{pmatrix}
x\\ y\\ z
\end{pmatrix},
$$
the condition $v\in W$ is exactly
$$
ax+by+cz=u^Tv=0,
$$
which says that $v$ is orthogonal to $u$.

:::

:::

::: {.pf-step #s2}

For every $v\in\RR^3$, the orthogonal projection of $v$ onto $W$ is
$$
P_W(v)=v-(u^Tv)u.
$$

::: pf-proof

Since $u$ has length $1$, the orthogonal projection of $v$ onto the line spanned by $u$ is
$$
(u^Tv)u.
$$
Subtracting that normal component from $v$ leaves the component in $u^\perp=W$.

:::

:::

::: {.pf-step #s3}

The standard-basis matrix of $P_W$ is
$$
\boxed{
\begin{pmatrix}
1-a^2&-ab&-ac\\
-ab&1-b^2&-bc\\
-ac&-bc&1-c^2
\end{pmatrix}}.
$$

::: pf-proof

By step [](#s2){.pf-ref},
$$
P_W(v)=(I-uu^T)v.
$$
Now
$$
uu^T=
\begin{pmatrix}
a^2&ab&ac\\
ab&b^2&bc\\
ac&bc&c^2
\end{pmatrix},
$$
so subtracting this matrix from the identity gives the displayed matrix.

:::

:::

::: pf-qed

Step [](#s3){.pf-ref} gives the requested matrix.

:::

:::

:::
