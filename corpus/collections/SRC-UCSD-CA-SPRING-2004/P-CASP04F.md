---
schema: qual/card@1
id: P-CASP04F
kind: problem
title: "Interpolation by analytic functions with prescribed values and derivatives"
classification:
  areas:
  - complex-analysis
  topics:
  - Complex Analysis
relations: []
review: draft
---

::: {.problem}
Let $G$ be an open region in $\mathbb{C}$ and $\{z_n\}$ a sequence of distinct points in $G$ without limit points in $G$.
Suppose that for each $n$, you are given an integer $m_n$ and a sequence of complex numbers $\{w_{n,k}\}_{k=0}^{m_n}$.
Show that there is $f \in H(G)$ such that, for every $n$, $$f^{(k)}(z_n) = w_{n,k}, \quad k = 0, 1, \ldots, m_n.$$

Hint: First show that, given an integer $m$, complex numbers $w_k$ for $k = 1, \ldots, m$, a point $z = a$, and an analytic function $g$ which vanishes to order $m+1$ at $z = a$, then one can find a rational function $$S(z) = \sum_{k=1}^{m+1} \frac{b_k}{(z-a)^k}$$ such that the product $f(z) = S(z)g(z)$ has a removable singularity at $z = a$ and $f^{(k)}(a) = w_k$ for $k = 0, 1, \ldots, m$.
:::

::: {.solution}
By the Weierstrass theorem on prescribed zeros in a plane domain, choose
$g\in H(G)$ whose zero at each $z_n$ has exact order $m_n+1$ and which has no
other zeros forced by the construction.

Fix $n$. Write locally
\[
g(z)=(z-z_n)^{m_n+1}u_n(z),
\qquad u_n(z_n)\ne0.
\]
We claim that there are coefficients $b_{n,1},\dots,b_{n,m_n+1}$ such that
\[
S_n(z)=\sum_{j=1}^{m_n+1}\frac{b_{n,j}}{(z-z_n)^j}
\]
has the property that $S_ng$ extends holomorphically across $z_n$ with the
prescribed jet $w_{n,0},\dots,w_{n,m_n}$ there. Indeed, multiplication by the
unit $u_n$ is an invertible triangular linear operation on $m_n$-jets, while
the coefficients $b_{n,j}$ independently prescribe the coefficients of
powers $(z-z_n)^0,\dots,(z-z_n)^{m_n}$. Thus the required coefficients exist
uniquely.

Now apply the Mittag--Leffler theorem on $G$ to obtain a meromorphic function
$S$ whose principal part at each $z_n$ is $S_n$ and which has no other poles.
Set
\[
f=gS.
\]
At each $z_n$, the zero of $g$ cancels the pole of $S$, so $f$ has a
removable singularity there; away from the $z_n$ it is holomorphic. By the
choice of the principal part $S_n$, its removable extension satisfies
\[
f^{(k)}(z_n)=w_{n,k},
\qquad 0\le k\le m_n.
\]
Thus the extended function belongs to $H(G)$ and has all the required jets.
:::
