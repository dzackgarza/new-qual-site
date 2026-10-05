---
schema: qual/card@1
id: P-UCLAB12-08
kind: problem
title: Isotropic subspaces of a nondegenerate Hermitian form have dimension at most $n/2$
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
---

::: {.problem}
Let H be an n by n Hermitian matrix with non-zero determinant.
Use H to define an Hermitian form [,] by the formula: for x, y in $\mathbb { C } ^ { n }$ (column vectors!), $[ x , y ] = { ^ { t } \overline { { x } } } H y$ , where, as usual, the bar over x denotes complex conjugation and the t denotes transpose.
Let W be a complex subspace of $\mathbb { C } ^ { n }$ such that $[ { w _ { 1 } } , { w _ { 2 } } ] = 0$ for all $w _ { 1 }$ and $w _ { 2 }$ in $W$ Show that dimW $\leq n / 2$ Give also for each n an example of an H for which dim $W = n / 2$ if n is even, or dim $W = ( n - 1 ) / 2$ if n is odd.
:::

::: {.solution}
Let
\[
[x,y]=\overline{x}^{\,t}Hy
\]
and, for a subspace $U\subseteq\mathbb C^n$, define
\[
U^\perp
=
\{v\in\mathbb C^n:[u,v]=0\text{ for every }u\in U\}.
\]

<1>1. The Hermitian form $[\ ,\ ]$ is nondegenerate.

::: {.proof}
Suppose
\[
[x,y]=0
\]
for every $x\in\mathbb C^n$.
Then
\[
\overline{x}^{\,t}Hy=0
\]
for every $x$, so
\[
Hy=0.
\]
Since $\det H\ne0$, the matrix $H$ is invertible, hence $y=0$.
Thus the form is nondegenerate.
:::

<1>2. For every subspace $U\subseteq\mathbb C^n$,
\[
\dim U^\perp=n-\dim U.
\]

::: {.proof}
Define
\[
\Phi:\mathbb C^n\to U^*
\]
by
\[
\Phi(v)(u)=[u,v].
\]
Then
\[
\ker\Phi=U^\perp.
\]

The map $\Phi$ is onto. Indeed, let $\ell\in U^*$. Extend $\ell$ to a linear functional
\[
\widetilde\ell\in(\mathbb C^n)^*.
\]
By nondegeneracy from step <1>1, the map
\[
\mathbb C^n\to(\mathbb C^n)^*,
\qquad
v\mapsto[x\mapsto[x,v]]
\]
is injective, hence bijective because both spaces have dimension $n$. Therefore there exists $v$ such that
\[
\widetilde\ell(x)=[x,v]
\]
for every $x$, and in particular
\[
\ell(u)=[u,v]
\]
for $u\in U$. Thus $\Phi$ is surjective.

Rank-nullity now gives
\[
n
=
\dim U^\perp+\dim U^*
=
\dim U^\perp+\dim U.
\]
:::

<1>3. The hypothesis on $W$ implies
\[
W\subseteq W^\perp.
\]

::: {.proof}
If $w\in W$, then for every $u\in W$ the hypothesis gives
\[
[u,w]=0.
\]
Thus $w\in W^\perp$.
:::

<1>4. One has
\[
\boxed{\dim W\le\frac n2}.
\]

::: {.proof}
By step <1>3,
\[
\dim W\le\dim W^\perp.
\]
By step <1>2,
\[
\dim W^\perp=n-\dim W.
\]
Hence
\[
\dim W\le n-\dim W,
\]
so
\[
2\dim W\le n.
\]
:::

<1>5. Suppose $n=2m$. Let
\[
H=
\begin{pmatrix}
0&I_m\\
I_m&0
\end{pmatrix},
\qquad
W=\mathbb C^m\oplus0.
\]
Then $\det H\ne0$, the matrix $H$ is Hermitian, and
\[
\dim W=m=\frac n2.
\]

::: {.proof}
The matrix $H$ is real symmetric, hence Hermitian.
Also
\[
H^2=I_{2m},
\]
so $H$ is invertible.

If
\[
w_1=(u_1,0),
\qquad
w_2=(u_2,0)
\]
belong to $W$, then
\[
Hw_2=(0,u_2),
\]
and therefore
\[
[w_1,w_2]
=
(\overline{u_1}^{\,t},0)(0,u_2)
=0.
\]
Thus $W$ is totally isotropic and has the maximal permitted dimension $m$.
:::

<1>6. Suppose $n=2m+1$. Let
\[
H=
\begin{pmatrix}
0&I_m&0\\
I_m&0&0\\
0&0&1
\end{pmatrix},
\qquad
W=\mathbb C^m\oplus0\oplus0.
\]
Then $\det H\ne0$, $H$ is Hermitian, and
\[
\dim W=m=\frac{n-1}{2}.
\]

::: {.proof}
Again $H$ is real symmetric.
Its square is the identity, so it is invertible.
The same computation as in step <1>5 shows that the form vanishes identically on $W\times W$.
The dimension of $W$ is $m=(n-1)/2$.
:::

<1>7. Q.E.D.

::: {.proof}
Step <1>4 proves the dimension bound, and steps <1>5--<1>6 give examples attaining the largest possible dimension in even and odd dimensions.
:::
:::
