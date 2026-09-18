---
schema: qual/card@1
id: P-AGH3121EMBDIMSEMI
kind: problem
title: Embedding dimension is upper semicontinuous
classification:
  areas:
  - algebraic-geometry
  topics:
  - Semicontinuity
  - Embedding Dimension
  - Schemes of Finite Type
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-18
  note: >-
    Read Exercise III.12.1 and wrote the Jacobian-minor proof independently before comparing it with an
    external solution transcription. The cotangent-space identification was cross-checked against Stacks
    Project Tag 0B28, and matrix-rank openness against Tag 05GD.
- event: solution-written
  by: chatgpt
  date: 2026-09-18
---

::: {.problem}
Let $Y$ be a scheme of finite type over an algebraically closed field $k$.
Show that the function
\[
\varphi(y) = \dim_k (\mfm_y / \mfm_y^2)
\]
is upper semicontinuous on the set of closed points of $Y$.
:::

::: {.solution}
<1>1. It is enough to prove the assertion on an affine neighbourhood
$$
U=\Spec A
$$
of an arbitrary closed point $y\in Y$.

::: {.proof}
Upper semicontinuity is local on the source. Since $Y$ is of finite type
over $k$, every point has an affine neighbourhood of finite type over $k$.
Thus it suffices to prove the required upper semicontinuity on the closed
points of each such affine open.
:::

<1>2. Write
$$
A=k[x_1,\ldots,x_N]/I,
\qquad
I=(f_1,\ldots,f_r).
$$
For every closed point $z\in U$, let
$$
J(z)=
\left(
\frac{\partial f_i}{\partial x_j}(z)
\right)_{\substack{1\le i\le r\\1\le j\le N}}.
$$
Then
$$
\boxed{
\varphi(z)=N-\operatorname{rank}J(z).
}
$$

::: {.proof}
Because $k$ is algebraically closed and $A$ is of finite type over $k$,
the residue field of every closed point $z$ is $k$. Let
$$
\mathfrak n_z=(x_1-a_1,\ldots,x_N-a_N)
\subseteq k[x_1,\ldots,x_N]
$$
be the maximal ideal corresponding to $z=(a_1,\ldots,a_N)$, and let
$\mfm_z$ be the maximal ideal of $A_z$.

The conormal sequence for
$$
k[x_1,\ldots,x_N]\longrightarrow A
$$
and base change to $k(z)=k$ gives a right-exact sequence
$$
I/I^2\otimes_A k
\longrightarrow
k^N
\longrightarrow
\Omega_{A/k}\otimes_A k
\longrightarrow0.
$$
The class of $f_i$ maps to
$$
df_i(z)
=
\sum_{j=1}^N
\frac{\partial f_i}{\partial x_j}(z)\,dx_j.
$$
Since the $f_i$ generate $I$, the image of the first arrow is the row
space of $J(z)$. Hence
$$
\dim_k\bigl(\Omega_{A/k}\otimes_A k\bigr)
=
N-\operatorname{rank}J(z).
$$

At a $k$-rational point, the cotangent-space identification gives
$$
\mfm_z/\mfm_z^2
\cong
\Omega_{A/k}\otimes_A k.
$$
Therefore
$$
\varphi(z)
=
\dim_k(\mfm_z/\mfm_z^2)
=
N-\operatorname{rank}J(z),
$$
as claimed.
:::

<1>3. For every integer $q$, the subset of closed points
$$
\{z\in U:\varphi(z)\ge q\}
$$
is closed in the subspace of closed points of $U$.

::: {.proof}
By step <1>2,
$$
\varphi(z)\ge q
\quad\Longleftrightarrow\quad
\operatorname{rank}J(z)\le N-q.
$$
For
$$
0\le N-q<\min\{r,N\},
$$
the latter condition says precisely that every
$(N-q+1)\times(N-q+1)$ minor of the matrix
$$
J=
\left(
\frac{\partial f_i}{\partial x_j}
\right)
$$
vanishes at $z$. These minors are regular functions on $U$, so their
common zero locus is closed. If $N-q<0$, the set is empty; if
$N-q\ge\min\{r,N\}$, it is all of $U$. Thus the assertion holds for every
$q$.
:::

<1>4. The function
$$
\varphi(y)=\dim_k(\mfm_y/\mfm_y^2)
$$
is upper semicontinuous on the closed points of $Y$.

::: {.proof}
For an integer-valued function, upper semicontinuity is equivalent to the
closedness of every superlevel set
$$
\{y:\varphi(y)\ge q\}.
$$
Step <1>3 proves this on every affine neighbourhood from step <1>1.
Since the property is local, it holds on all of $Y$.
:::

<1>5. Q.E.D.

::: {.proof}
Step <1>4 is the required upper semicontinuity.
:::
:::
