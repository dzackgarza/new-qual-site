---
schema: qual/card@1
id: P-J2D5B
kind: problem
title: Invariants of a dihedral action on $\mathbb{C}[x,y]$
classification:
  areas:
  - algebra
  topics:
  - Group Actions
  - Integral Extensions
  - Algebras
relations: []
review: draft
---

::: {.problem}
The dihedral group $G = \langle a,b \mid a^3=b^2=1, bab=a^{-1}\rangle$ acts on the $\mathbb{C}$-algebra $S = \mathbb{C}[x,y]$ by algebra automorphisms so that $$a\cdot x = \omega x, \qquad a\cdot y = \omega^{-1}y, \qquad b\cdot x = y,$$ where $\omega = e^{2\pi i/3}$.
Let $R := S^G$ be the invariant subalgebra.

a. Show that $R = \mathbb{C}[x^3+y^3, xy]$.
b. Show that $R \subseteq S$ is an integral extension.
c. Find an explicit monic polynomial $f(t) \in R[t]$ such that $f(x) = 0$.
:::

::: {.solution}
Put
$$
u=x^3+y^3,
\qquad
v=xy.
$$

<1>1. Both $u$ and $v$ are $G$-invariant.
::: {.proof}
Since $\omega^3=1$,
$$
a\cdot u=(\omega x)^3+(\omega^{-1}y)^3=u,
\qquad
a\cdot v=(\omega x)(\omega^{-1}y)=v.
$$
The element $b$ interchanges $x$ and $y$, so it fixes both $u$ and $v$. Hence
$$
\CC[u,v]\subseteq S^G.
$$
:::

<1>2. If
$$
z=\sum_{i,j}c_{ij}x^iy^j\in S^G,
$$
then $c_{ij}=0$ unless $i\equiv j\pmod3$, and $c_{ij}=c_{ji}$.
::: {.proof}
Invariance under $a$ gives
$$
z=a\cdot z
=\sum_{i,j}c_{ij}\omega^{i-j}x^iy^j.
$$
Linear independence of the monomials implies
$$
c_{ij}\ne0\Longrightarrow \omega^{i-j}=1
\Longrightarrow i\equiv j\pmod3.
$$

Invariance under $b$ gives
$$
z=b\cdot z
=\sum_{i,j}c_{ij}y^ix^j
=\sum_{i,j}c_{ji}x^iy^j,
$$
so $c_{ij}=c_{ji}$.
:::

<1>3. Every $G$-invariant polynomial lies in $\CC[u,v]$.
::: {.proof}
By step <1>2, an invariant polynomial is a linear combination of diagonal monomials
$$
x^iy^i=v^i
$$
and symmetric pairs
$$
x^iy^j+x^jy^i
$$
with $i>j$ and $i-j=3m$ for some $m\ge1$. Such a pair equals
$$
v^j(x^{3m}+y^{3m}).
$$

Set
$$
P_m=x^{3m}+y^{3m}.
$$
Then
$$
P_0=2,
\qquad
P_1=u,
$$
and, because $x^3$ and $y^3$ are the roots of
$$
T^2-uT+v^3,
$$
the power sums satisfy
$$
P_m=uP_{m-1}-v^3P_{m-2}
\qquad(m\ge2).
$$
Induction gives $P_m\in\CC[u,v]$ for every $m$. Therefore every invariant monomial combination from step <1>2 belongs to $\CC[u,v]$.
:::

<1>4. Hence
$$
\boxed{R=S^G=\CC[x^3+y^3,xy]}.
$$
::: {.proof}
Step <1>1 gives one inclusion and step <1>3 gives the reverse inclusion.
:::

<1>5. The extension $R\subseteq S$ is integral.
::: {.proof}
For arbitrary $z\in S$, define
$$
F_z(t)=\prod_{g\in G}(t-g\cdot z).
$$
This polynomial is monic. For every $h\in G$, applying $h$ to its coefficients merely permutes the factors because
$$
h\cdot(g\cdot z)=(hg)\cdot z.
$$
Thus all coefficients lie in $S^G=R$, so
$$
F_z(t)\in R[t].
$$
The factor corresponding to the identity shows $F_z(z)=0$. Hence every $z\in S$ is integral over $R$.
:::

<1>6. An explicit monic polynomial in $R[t]$ annihilating $x$ is
$$
\boxed{f(t)=t^6-(x^3+y^3)t^3+(xy)^3}.
$$
::: {.proof}
The $G$-orbit of $x$ is
$$
\{x,\omega x,\omega^2x,y,\omega y,\omega^2y\}.
$$
Therefore the orbit polynomial from step <1>5 is
$$
\begin{aligned}
f(t)
&=(t-x)(t-\omega x)(t-\omega^2x)
  (t-y)(t-\omega y)(t-\omega^2y)\\
&=(t^3-x^3)(t^3-y^3)\\
&=t^6-(x^3+y^3)t^3+x^3y^3\\
&=t^6-ut^3+v^3.
\end{aligned}
$$
By step <1>4, its coefficients lie in $R$, and clearly $f(x)=0$.
:::

<1>7. Q.E.D.
::: {.proof}
Step <1>4 proves part (a), step <1>5 proves part (b), and step <1>6 proves part (c).
:::
:::
