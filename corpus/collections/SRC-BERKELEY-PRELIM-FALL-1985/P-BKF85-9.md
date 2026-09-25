---
schema: qual/card@1
id: P-BKF85-9
kind: problem
title: Maximize Euclidean norm on a quadratic level set
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Problem 9 in the deterministic MinerU Flash extraction assets/attachments/Fall85_extracted.md; Flash drops the third coordinate from the displayed column vector, while the same sentence states $v\in\mathbb R^3$ and $v^t=(x,y,z)$, forcing $v=(x,y,z)^t$.
---

::: {.problem}
Let
\[
A=\frac16
\begin{pmatrix}
13&-5&-2\\
-5&13&-2\\
-2&-2&10
\end{pmatrix}
\]
and let
\[
v=\begin{pmatrix}x\\y\\z\end{pmatrix}\in\mathbb R^3.
\]
As $v$ ranges over the set satisfying
\[
v^TAv=1,
\]
show that $\|v\|$ is bounded and determine its least upper bound.
:::

::: {.solution}
<1>1. The vectors
$$
u_1=(1,1,1)^T,
\qquad
u_2=(1,1,-2)^T,
\qquad
u_3=(1,-1,0)^T
$$
are pairwise orthogonal eigenvectors of $A$ with eigenvalues $1$, $2$, and $3$, respectively.

::: {.proof}
Direct multiplication gives
$$
Au_1=u_1,
\qquad
Au_2=2u_2,
\qquad
Au_3=3u_3.
$$
Also
$$
u_1^Tu_2=1+1-2=0,
\qquad
u_1^Tu_3=1-1=0,
\qquad
u_2^Tu_3=1-1=0.
$$
Since these are three nonzero orthogonal vectors in $\RR^3$, they form an orthogonal basis.
:::

<1>2. For every $v\in\RR^3$,
$$
v^TAv\geq\norm{v}_2^2.
$$

::: {.proof}
Let
$$
e_j\coloneqq\frac{u_j}{\norm{u_j}_2},
\qquad
j=1,2,3.
$$
By step <1>1, $e_1,e_2,e_3$ is an orthonormal eigenbasis. Write
$$
v=c_1e_1+c_2e_2+c_3e_3.
$$
Then
$$
v^TAv
=
c_1^2+2c_2^2+3c_3^2
\geq
c_1^2+c_2^2+c_3^2
=
\norm{v}_2^2.
$$
:::

<1>3. Every $v$ satisfying $v^TAv=1$ obeys
$$
\norm{v}_2\leq1.
$$

::: {.proof}
Step <1>2 gives
$$
1=v^TAv\geq\norm{v}_2^2.
$$
Taking square roots yields the bound.
:::

<1>4. The bound in step <1>3 is attained.

::: {.proof}
Take
$$
v_0\coloneqq\frac1{\sqrt3}(1,1,1)^T.
$$
Then $\norm{v_0}_2=1$, and step <1>1 gives
$$
Av_0=v_0.
$$
Therefore
$$
v_0^TAv_0=v_0^Tv_0=1.
$$
Thus $v_0$ belongs to the prescribed level set and has norm $1$.
:::

<1>5. The least upper bound of $\norm{v}_2$ on the level set $v^TAv=1$ is
$$
\boxed{1}.
$$

::: {.proof}
Step <1>3 shows that $1$ is an upper bound, while step <1>4 shows that it is achieved. Hence it is the maximum and therefore the least upper bound.
:::

<1>6. Q.E.D.

::: {.proof}
Step <1>5 gives the required bound and its least upper bound.
:::
:::
