---
schema: qual/card@1
id: P-AGXVAREXSEGREQUADRIC
kind: problem
title: The Segre image of $\PP^1\cross \PP^1$ is a smooth quadric surface
classification:
  areas:
  - algebraic-geometry
  topics:
  - Segre Embedding
  - Quadric Surfaces
  - Projective Varieties
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-20
  note: >-
    Read Zaidenberg Exercise 8.5 in the recorded source. It gives the Segre
    map P^1 x P^1 -> P^3 in coordinates and asks that its image be the smooth
    quadric x_0x_3-x_1x_2=0.
- event: source-corrected
  by: chatgpt
  date: 2026-09-20
  note: >-
    Made the source's complex base field explicit on the standalone card.
- event: solution-written
  by: chatgpt
  date: 2026-09-20
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-20
  note: >-
    Checked both inclusions in the image computation via the rank-one matrix
    criterion and checked smoothness from the four projective partial
    derivatives.
---

::: {.problem}
Show that the image of the Segre embedding
$$
\sigma:\PP^1_\CC\cross\PP^1_\CC\longrightarrow\PP^3_\CC
$$
is the smooth quadric
$$
Q=V(x_0x_3-x_1x_2).
$$
:::

::: {.solution}
Write
$$
\sigma\bigl([a_0:a_1],[b_0:b_1]\bigr)
=
[a_0b_0:a_0b_1:a_1b_0:a_1b_1].
$$

<1>1. The image of $\sigma$ is contained in $Q$.

::: {.proof}
At a point of the image,
$$
\begin{aligned}
x_0x_3-x_1x_2
&=(a_0b_0)(a_1b_1)-(a_0b_1)(a_1b_0)\\
&=0.
\end{aligned}
$$
Hence
$$
\operatorname{im}\sigma\subseteq Q.
$$
:::

<1>2. Every point of $Q$ lies in the image of $\sigma$.

::: {.proof}
Let
$$
p=[x_0:x_1:x_2:x_3]\in Q.
$$
Form the matrix
$$
M_p
=
\begin{pmatrix}
x_0&x_1\\
x_2&x_3
\end{pmatrix}.
$$
Since
$$
\det M_p=x_0x_3-x_1x_2=0,
$$
the matrix has rank at most $1$. It is not the zero matrix because $p$ is a
projective point, so it has rank exactly $1$.

Therefore there are nonzero vectors
$$
\begin{pmatrix}a_0\\a_1\end{pmatrix},
\qquad
\begin{pmatrix}b_0&b_1\end{pmatrix}
$$
such that
$$
M_p
=
\begin{pmatrix}a_0\\a_1\end{pmatrix}
\begin{pmatrix}b_0&b_1\end{pmatrix}.
$$
Thus
$$
[x_0:x_1:x_2:x_3]
=
[a_0b_0:a_0b_1:a_1b_0:a_1b_1]
$$
and hence
$$
p
=
\sigma\bigl([a_0:a_1],[b_0:b_1]\bigr).
$$
So
$$
Q\subseteq\operatorname{im}\sigma.
$$
:::

<1>3. The Segre image is exactly the quadric:
$$
\boxed{
\operatorname{im}\sigma
=
V(x_0x_3-x_1x_2).
}
$$

::: {.proof}
Combine steps <1>1 and <1>2.
:::

<1>4. The quadric $Q$ is smooth.

::: {.proof}
Put
$$
F=x_0x_3-x_1x_2.
$$
Its partial derivatives are
$$
\frac{\partial F}{\partial x_0}=x_3,
\qquad
\frac{\partial F}{\partial x_1}=-x_2,
\qquad
\frac{\partial F}{\partial x_2}=-x_1,
\qquad
\frac{\partial F}{\partial x_3}=x_0.
$$
If all four partial derivatives vanished at a point of $Q$, then
$$
x_0=x_1=x_2=x_3=0,
$$
which is impossible in projective space. Hence $Q$ has no singular points.
Therefore $Q$ is smooth.
:::

<1>5. Q.E.D.

::: {.proof}
Step <1>3 identifies the image of the Segre embedding, and step <1>4 proves
that this image is a smooth quadric surface.
:::
:::
