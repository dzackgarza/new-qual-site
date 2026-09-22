---
schema: qual/card@1
id: P-BKF79-5
kind: problem
title: A real skew-symmetric matrix has even rank
classification: {areas: [prelim], topics: []}
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
    Interpreted A as the alternating form omega(u,v)=u^TAv. Its
    radical is ker A, so the induced form on the quotient has
    dimension rank A and is nondegenerate. A nondegenerate alternating
    form splits off nondegenerate two-planes inductively, forcing its
    dimension to be even.
---

::: {.problem}
Let $A$ be a real skew-symmetric matrix, so $A_{ij}=-A_{ji}$. Prove that $A$ has even rank.
:::

::: {.solution}
Let $A$ be an $n\times n$ matrix and let $V=\RR^n$.

<1>1. The bilinear form
$$
\omega:V\times V\longrightarrow\RR,
\qquad
\omega(u,v)=u^TAv,
$$
is alternating.

::: {.proof}
Since $A^T=-A$,
$$
\omega(v,u)
=
v^TAu
=
u^TA^Tv
=
-u^TAv
=
-\omega(u,v).
$$
Taking $u=v$ gives
$$
\omega(v,v)=-\omega(v,v),
$$
so $\omega(v,v)=0$ over $\RR$.
:::

<1>2. The radical of $\omega$ is exactly $\ker A$.

::: {.proof}
For $u\in V$,
$$
\omega(u,v)
=
u^TAv
=
-(Au)^Tv.
$$
Thus $\omega(u,v)=0$ for every $v\in V$ if and only if $Au=0$.
:::

<1>3. The form $\omega$ induces a nondegenerate alternating form
$\overline\omega$ on
$$
\overline V
\coloneqq
V/\ker A,
$$
and
$$
\dim\overline V=\operatorname{rank}A.
$$

::: {.proof}
Because $\ker A$ is the radical by step <1>2, changing either
representative by an element of $\ker A$ does not change the value of
$\omega$. Hence $\omega$ descends to the quotient. The induced form
has zero radical by construction, so it is nondegenerate. Finally,
rank-nullity gives
$$
\dim(V/\ker A)
=
\dim V-\dim\ker A
=
\operatorname{rank}A.
$$
:::

<1>4. Every finite-dimensional real vector space carrying a
nondegenerate alternating bilinear form has even dimension.

::: {.proof}
We argue by induction on the dimension. Dimension $0$ is even.

Let $W$ be nonzero and let $\beta$ be a nondegenerate alternating
form on $W$. Choose $0\neq v\in W$. By nondegeneracy, there exists
$w\in W$ such that
$$
\beta(v,w)\neq0.
$$
Set
$$
U=\operatorname{span}\{v,w\}.
$$
In the basis $(v,w)$, the matrix of $\beta|_U$ is
$$
\begin{pmatrix}
0&c\\
-c&0
\end{pmatrix},
\qquad
c=\beta(v,w)\neq0,
$$
so $\beta|_U$ is nondegenerate.

Let
$$
U^\perp
\coloneqq
\{x\in W:\beta(x,u)=0\text{ for every }u\in U\}.
$$
Because $\beta|_U$ is nondegenerate, every $x\in W$ has a unique
decomposition
$$
x=u+y,
\qquad
u\in U,
\quad
y\in U^\perp.
$$
Indeed, the map
$$
U\longrightarrow U^*,
\qquad
u\longmapsto\beta(u,-)|_U,
$$
is an isomorphism. Hence for each $x\in W$ there is a unique $u\in U$
such that
$$
\beta(u,-)|_U=\beta(x,-)|_U.
$$
Then $y=x-u$ lies in $U^\perp$. Uniqueness also shows
$U\cap U^\perp=\{0\}$.
Thus
$$
W=U\oplus U^\perp.
$$
Moreover, the restriction of $\beta$ to $U^\perp$ is nondegenerate:
if $y\in U^\perp$ is orthogonal to all of $U^\perp$, then it is
orthogonal to both summands of $W$, hence to all of $W$, so $y=0$.

Therefore
$$
\dim W
=
2+\dim U^\perp.
$$
By induction, $\dim U^\perp$ is even, so $\dim W$ is even.
:::

<1>5. The rank of $A$ is even.

::: {.proof}
By step <1>3, $\overline V$ carries a nondegenerate alternating form
and
$$
\dim\overline V=\operatorname{rank}A.
$$
Step <1>4 says that $\dim\overline V$ is even.
:::

<1>6. Q.E.D.

::: {.proof}
Step <1>5 is the required conclusion.
:::
:::
