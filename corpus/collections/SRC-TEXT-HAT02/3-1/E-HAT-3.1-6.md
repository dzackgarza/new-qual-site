---
schema: qual/card@1
id: E-HAT-3.1-6
kind: problem
title: Simplicial cohomology of the torus, $\mathbb{RP}^2$, and the Klein bottle
classification:
  areas:
  - topology
  topics:
  - Cohomology
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 3.1, Exercise 6; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Verified the cochain, exact-sequence, and universal-coefficient calculations directly.
---

::: {.problem}
(a) Directly from the definitions, compute the simplicial cohomology groups of $S^1 \times S^1$ with $\mathbb{Z}$ and $\mathbb{Z}_2$ coefficients, using the $\Delta$-complex structure given in §2.1.

(b) Do the same for $\mathbb{RP}^2$ and the Klein bottle.
:::

::: {.solution}
We compute directly from the cellular/simplicial cochain complexes obtained by dualizing the displayed $\Delta$-complex chain complexes.

<1>1. For the torus, with one vertex, edges $a,b,c$, and two $2$-simplices $U,L$, choose orientations so that
\[
\partial U=a+b-c,\qquad \partial L=a+b-c.
\]
Thus for coefficients in an abelian group $G$,
\[
C^0=G,\qquad C^1=G^3,\qquad C^2=G^2,
\]
with
\[
\delta^0=0,
\qquad
\delta^1(x,y,z)=(x+y-z,x+y-z).
\]
::: {.proof}
This is the dual of the simplicial boundary maps in the standard two-triangle $\Delta$-complex on the torus.
:::

<1>2. Hence for $G=\mathbb Z$ or $\mathbb Z_2$,
\[
H^0(T^2;G)\cong G,
\qquad
H^1(T^2;G)\cong G^2,
\qquad
H^2(T^2;G)\cong G.
\]
::: {.proof}
The kernel of $\delta^1$ is given by one equation $x+y-z=0$, hence is isomorphic to $G^2$. Its image is the diagonal subgroup $\{(t,t):t\in G\}$ of $G^2$, whose quotient is isomorphic to $G$.
:::

<1>3. For $\mathbb{RP}^2$, choose the standard $\Delta$-complex with vertices $v,w$, edges $a,b,c$, and faces $U,L$, with
\[
\partial a=\partial b=w-v,\qquad \partial c=0,
\]
and
\[
\partial U=-a+b+c,\qquad \partial L=a-b+c.
\]
Thus
\[
\delta^0(s,t)=(t-s,t-s,0)
\]
and
\[
\delta^1(p,q,r)=(-p+q+r,p-q+r).
\]
::: {.proof}
These are obtained by evaluating cochains on the displayed simplicial boundaries.
:::

<1>4. With integral coefficients,
\[
\boxed{H^0(\mathbb{RP}^2;\mathbb Z)=\mathbb Z,\quad
H^1(\mathbb{RP}^2;\mathbb Z)=0,\quad
H^2(\mathbb{RP}^2;\mathbb Z)=\mathbb Z_2.}
\]
::: {.proof}
The kernel of $\delta^0$ is the diagonal copy of $\mathbb Z$, so $H^0\cong\mathbb Z$. If $\delta^1(p,q,r)=0$, subtracting and adding the two equations gives $2r=0$, hence $r=0$ and $p=q$. Thus
\[
\ker\delta^1=\mathbb Z(1,1,0)=\operatorname{im}\delta^0,
\]
so $H^1=0$. The matrix of $\delta^1$ has rank two and its $2\times2$ minors have greatest common divisor $2$, so its image has index $2$ in $\mathbb Z^2$. Hence $H^2\cong\mathbb Z_2$.
:::

<1>5. With $\mathbb Z_2$ coefficients,
\[
\boxed{H^i(\mathbb{RP}^2;\mathbb Z_2)\cong\mathbb Z_2\quad(i=0,1,2).}
\]
::: {.proof}
Modulo $2$, $\delta^0$ has rank one and $\delta^1$ has rank one, with
\[
\delta^1(p,q,r)=(p+q+r,p+q+r).
\]
Thus $\dim\ker\delta^1=2$ and $\dim\operatorname{im}\delta^0=1$, giving one-dimensional $H^1$. The cokernel of $\delta^1$ is also one-dimensional, giving $H^2\cong\mathbb Z_2$.
:::

<1>6. For the Klein bottle, choose orientations in the standard two-triangle $\Delta$-complex so that all three edges are loops and
\[
\partial U=a+b-c,
\qquad
\partial L=a-b+c.
\]
Then
\[
\delta^0=0,
\qquad
\delta^1(p,q,r)=(p+q-r,p-q+r).
\]
::: {.proof}
All vertices are identified, so the boundary of every edge is zero. Dualizing the two face boundaries gives the displayed coboundary.
:::

<1>7. Therefore
\[
\boxed{H^0(K;\mathbb Z)=\mathbb Z,\quad H^1(K;\mathbb Z)=\mathbb Z,\quad H^2(K;\mathbb Z)=\mathbb Z_2.}
\]
::: {.proof}
The equations $p+q-r=0$ and $p-q+r=0$ imply $2p=0$, hence $p=0$ and $q=r$. Thus $\ker\delta^1\cong\mathbb Z$. The $2\times2$ minors of the matrix of $\delta^1$ have gcd $2$, so its image has index $2$ in $\mathbb Z^2$, giving $H^2\cong\mathbb Z_2$.
:::

<1>8. With $\mathbb Z_2$ coefficients,
\[
\boxed{H^0(K;\mathbb Z_2)=\mathbb Z_2,\quad H^1(K;\mathbb Z_2)=(\mathbb Z_2)^2,\quad H^2(K;\mathbb Z_2)=\mathbb Z_2.}
\]
::: {.proof}
Modulo $2$, both components of $\delta^1$ are $p+q+r$, so $\delta^1$ has rank one. Since $\delta^0=0$, the kernel has dimension two and the cokernel dimension one.
:::
:::
