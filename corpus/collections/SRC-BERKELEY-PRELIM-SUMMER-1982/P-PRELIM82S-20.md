---
schema: qual/card@1
id: P-PRELIM82S-20
kind: problem
title: Local invertibility of the matrix-squaring map at $I_2$ and $\operatorname{diag}(1,-1)$
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
  note: Visually checked Problem 20 on PDF page 4 of the retained Summer 1982 preliminary exam; the extracted first matrix was corrupted, but the PDF clearly shows the identity matrix.
- event: solution-written
  by: chatgpt
  date: 2026-09-21
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-21
  note: >-
    The derivative of the squaring map at X is H -> XH+HX. At I_2
    this is 2H, hence invertible, so the inverse function theorem gives
    a local inverse. At J=diag(1,-1), the distinct matrices
    [[1,t],[0,-1]] converge to J and all square to I_2, so f is not
    injective on any neighborhood of J and cannot have a local inverse.
---

::: {.problem}
Let $M_{2\times2}(\mathbb R)$ be the four-dimensional vector space of real $2\times2$ matrices and define
\[
f:M_{2\times2}(\mathbb R)\to M_{2\times2}(\mathbb R),
\qquad
f(X)=X^2.
\]

1. Show that $f$ has a local inverse near
   \[
   X=\begin{pmatrix}1&0\\0&1\end{pmatrix}.
   \]

2. Show that $f$ does not have a local inverse near
   \[
   X=\begin{pmatrix}1&0\\0&-1\end{pmatrix}.
   \]
:::

::: {.solution}
Write
$$
I_2=
\begin{pmatrix}
1&0\\
0&1
\end{pmatrix},
\qquad
J=
\begin{pmatrix}
1&0\\
0&-1
\end{pmatrix}.
$$

<1>1. For every $X,H\in M_2(\RR)$,
$$
Df_X(H)=XH+HX.
$$

::: {.proof}
One has
$$
\begin{aligned}
f(X+H)-f(X)
&=
(X+H)^2-X^2\\
&=
XH+HX+H^2.
\end{aligned}
$$
For any matrix norm on the finite-dimensional space $M_2(\RR)$,
$$
\norm{H^2}
\leq
C\norm{H}^2
=
o(\norm{H})
$$
for some constant $C$. Hence the linear part of the increment is
$H\mapsto XH+HX$.
:::

<1>2. Item 1: the derivative of $f$ at $I_2$ is invertible.

::: {.proof}
By step <1>1,
$$
Df_{I_2}(H)
=
I_2H+HI_2
=
2H.
$$
Thus $Df_{I_2}$ is scalar multiplication by $2$ on the four-dimensional
real vector space $M_2(\RR)$, with inverse $K\mapsto K/2$.
:::

<1>3. Item 1: the map $f$ has a local inverse near $I_2$.

::: {.proof}
The map $f$ is polynomial and hence continuously differentiable.
Step <1>2 shows that its derivative at $I_2$ is an isomorphism.
The inverse function theorem therefore gives neighborhoods $U$ of
$I_2$ and $V$ of
$$
f(I_2)=I_2
$$
such that
$$
f|_U:U\longrightarrow V
$$
is a diffeomorphism. In particular, $f$ has a local inverse near
$I_2$.
:::

<1>4. For every $t\in\RR$, define
$$
X_t=
\begin{pmatrix}
1&t\\
0&-1
\end{pmatrix}.
$$
Then
$$
X_t^2=I_2.
$$

::: {.proof}
Direct multiplication gives
$$
X_t^2
=
\begin{pmatrix}
1&t\\
0&-1
\end{pmatrix}
\begin{pmatrix}
1&t\\
0&-1
\end{pmatrix}
=
\begin{pmatrix}
1&0\\
0&1
\end{pmatrix}
=
I_2.
$$
:::

<1>5. Item 2: the map $f$ is not injective on any neighborhood of $J$.

::: {.proof}
One has
$$
X_0=J
$$
and
$$
X_t\longrightarrow J
$$
as $t\to0$. Therefore every neighborhood $U$ of $J$ contains some
$X_t$ with $t\neq0$. For such $t$,
$$
X_t\neq J,
$$
but step <1>4 gives
$$
f(X_t)=I_2=f(J).
$$
Hence $f|_U$ is not injective.
:::

<1>6. Item 2: the map $f$ does not have a local inverse near $J$.

::: {.proof}
If a local inverse existed near $J$, then $f$ would be injective on
some neighborhood of $J$. Step <1>5 shows that this is impossible.
:::

<1>7. Therefore
$$
\boxed{
f\text{ is locally invertible at }I_2
\text{ but not at }\operatorname{diag}(1,-1)
}.
$$

::: {.proof}
The first assertion is step <1>3 and the second is step <1>6.
:::

<1>8. Q.E.D.

::: {.proof}
Step <1>7 answers both items.
:::
:::
