---
schema: qual/card@1
id: P-BERK86S-15
kind: problem
title: Every Euclidean isometry of the plane is affine orthogonal
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-written
  by: chatgpt
  date: 2026-09-22
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-22
  note: >-
    Translated the isometry to fix the origin, recovered preservation of the
    Euclidean inner product from distances, and used the images of the
    standard basis to prove the translated map is linear and orthogonal.
---

::: {.problem}
Let $T:\mathbb R^2\to\mathbb R^2$ be an isometry for the Euclidean metric. Prove that
\[
T(x)=a+U(x)
\]
for some $a\in\mathbb R^2$ and some orthogonal linear transformation $U$.
:::

::: {.solution}
Set
$$
a\coloneqq T(0)
$$
and define
$$
U(x)\coloneqq T(x)-a.
$$

<1>1. The map $U:\RR^2\to\RR^2$ is an isometry satisfying
$$
U(0)=0.
$$

::: {.proof}
By definition,
$$
U(0)=T(0)-a=0.
$$
For $x,y\in\RR^2$,
$$
\norm{U(x)-U(y)}
=
\norm{T(x)-T(y)}
=
\norm{x-y},
$$
because $T$ is an isometry.
:::

<1>2. The map $U$ preserves the Euclidean inner product:
$$
\inner{U(x)}{U(y)}
=
\inner{x}{y}
$$
for all $x,y\in\RR^2$.

::: {.proof}
Step <1>1 gives
$$
\norm{U(x)}=\norm{x},
\qquad
\norm{U(y)}=\norm{y},
\qquad
\norm{U(x)-U(y)}=\norm{x-y}.
$$
Using the real polarization identity,
$$
2\inner{u}{v}
=
\norm{u}^2+\norm{v}^2-\norm{u-v}^2,
$$
we obtain
$$
\begin{aligned}
2\inner{U(x)}{U(y)}
&=
\norm{U(x)}^2+\norm{U(y)}^2-\norm{U(x)-U(y)}^2\\
&=
\norm{x}^2+\norm{y}^2-\norm{x-y}^2\\
&=
2\inner{x}{y}.
\end{aligned}
$$
:::

<1>3. If $e_1,e_2$ are the standard basis vectors and
$$
u_j\coloneqq U(e_j),
$$
then $(u_1,u_2)$ is an orthonormal basis of $\RR^2$.

::: {.proof}
By step <1>2,
$$
\inner{u_i}{u_j}
=
\inner{e_i}{e_j}
=
\delta_{ij}.
$$
Thus $u_1,u_2$ are orthonormal. Two orthonormal vectors in the
two-dimensional space $\RR^2$ form a basis.
:::

<1>4. For every
$$
x=x_1e_1+x_2e_2,
$$
one has
$$
U(x)=x_1u_1+x_2u_2.
$$

::: {.proof}
By step <1>2,
$$
\inner{U(x)}{u_j}
=
\inner{U(x)}{U(e_j)}
=
\inner{x}{e_j}
=
x_j
$$
for $j=1,2$. Since $(u_1,u_2)$ is an orthonormal basis by step <1>3,
the coordinates of $U(x)$ in that basis are precisely these inner
products. Hence
$$
U(x)=x_1u_1+x_2u_2.
$$
:::

<1>5. The map $U$ is linear and orthogonal.

::: {.proof}
Step <1>4 expresses $U$ as the linear map determined by
$$
U(e_1)=u_1,
\qquad
U(e_2)=u_2.
$$
Thus $U$ is linear. Its images of the standard orthonormal basis form the
orthonormal basis $(u_1,u_2)$ from step <1>3, so $U$ is an orthogonal
linear transformation.
:::

<1>6. Therefore
$$
\boxed{T(x)=a+U(x)}
$$
with $a\in\RR^2$ and $U$ orthogonal.

::: {.proof}
The definition of $U$ gives
$$
T(x)=a+U(x),
$$
and step <1>5 proves the required property of $U$.
:::

<1>7. Q.E.D.

::: {.proof}
Step <1>6 is the desired representation.
:::
:::
