---
schema: qual/card@1
id: E-HAT-3.1-6
kind: problem
title: Simplicial cohomology of the torus, $\RP^2$, and the Klein bottle
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
- event: source-checked
  by: claude
  date: 2026-10-31
  note: Statement compared with Hatcher, Algebraic Topology, Section 3.1, Exercise 6; it matches the printed text.
- event: solution-reviewed
  by: claude
  date: 2026-10-31
  note: >-
    Recomputed all six answers from the dualized $\Delta$-complex complexes. For the torus
    $\ker\delta^1$ is one linear equation and $\operatorname{im}\delta^1$ the diagonal, giving
    $G,G^2,G$. For $\RP^2$ and the Klein bottle the matrices are $[[-1,1,1],[1,-1,1]]$ and
    $[[1,1,-1],[1,-1,1]]$, whose $2\times2$ minors have gcd $2$, giving $\ZZ,0,\ZZ_2$ and
    $\ZZ,\ZZ,\ZZ_2$; over $\ZZ_2$ both have rank one, giving $\ZZ_2$ in every degree. The boundary
    formulas used are the ones printed for these $\Delta$-complexes in §2.1.
- event: solution-reviewed
  by: claude
  date: 2026-11-07
  note: >-
    Statement matches Exercise 6 (p.205). All six answers recomputed from the dual complexes: torus H^0=G, H^1=G^2, H^2=G; RP^2 integral Z, 0, Z/2 and mod 2 all Z/2; Klein bottle integral Z, Z, Z/2 and mod 2 Z/2, Z/2^2, Z/2. Cross-checked each against Theorem 3.2 (p.195). Boundary formulas are now cited: Example 2.3 p.106 for the torus, Example 2.4 p.106 for RP^2, the figure on p.102 for the Klein bottle (which the book does not compute). Not covered: nothing about the higher-dimensional surfaces.
---

::: {.problem}
(a) Directly from the definitions, compute the simplicial cohomology groups of $S^1 \times S^1$ with $\ZZ$ and $\ZZ_2$ coefficients, using the $\Delta$-complex structure given in §2.1.

(b) Do the same for $\RP^2$ and the Klein bottle.
:::

::: {.solution}
We compute directly from the cellular/simplicial cochain complexes obtained by dualizing the displayed $\Delta$-complex chain complexes.

::: pf

::: pf-step

For the torus, with one vertex, edges $a,b,c$, and two $2$-simplices $U,L$, choose orientations so that
$$
\partial U=a+b-c,\qquad \partial L=a+b-c.
$$
Thus for coefficients in an abelian group $G$,
$$
C^0=G,\qquad C^1=G^3,\qquad C^2=G^2,
$$
with
$$
\delta^0=0,
\qquad
\delta^1(x,y,z)=(x+y-z,x+y-z).
$$

::: pf-proof

The $\Delta$-complex structure is the one obtained from a square as on Hatcher p.102, and Example 2.3 (p.106) prints $\partial_2 U = a+b-c = \partial_2 L$ for it. The displayed $\delta^1$ is its dual in the sense of p.191.

:::

:::

::: pf-step

Hence for $G=\ZZ$ or $\ZZ_2$,
$$
H^0(T^2;G)\cong G,
\qquad
H^1(T^2;G)\cong G^2,
\qquad
H^2(T^2;G)\cong G.
$$

::: pf-proof

The kernel of $\delta^1$ is given by one equation $x+y-z=0$, hence is isomorphic to $G^2$. Its image is the diagonal subgroup $\{(t,t):t\in G\}$ of $G^2$, whose quotient is isomorphic to $G$.

:::

:::

::: pf-step

For $\RP^2$, choose the standard $\Delta$-complex with vertices $v,w$, edges $a,b,c$, and faces $U,L$, with
$$
\partial a=\partial b=w-v,\qquad \partial c=0,
$$
and
$$
\partial U=-a+b+c,\qquad \partial L=a-b+c.
$$
Thus
$$
\delta^0(s,t)=(t-s,t-s,0)
$$
and
$$
\delta^1(p,q,r)=(-p+q+r,p-q+r).
$$

::: pf-proof

These are obtained by evaluating cochains on the boundaries of Example 2.4 (p.106), which prints $\partial_2 U = -a+b+c$, $\partial_2 L = a-b+c$ and $\operatorname{im}\partial_1 = \ZZ(w-v)$, so that $\partial a = \partial b = w-v$ and $\partial c = 0$ (the same example notes that $a-b$ and $c$ form a basis of $\ker\partial_1$).

:::

:::

::: pf-step

With integral coefficients,
$$
\boxed{H^0(\RP^2;\ZZ)=\ZZ,\quad
H^1(\RP^2;\ZZ)=0,\quad
H^2(\RP^2;\ZZ)=\ZZ_2.}
$$

::: pf-proof

The kernel of $\delta^0$ is the diagonal copy of $\ZZ$, so $H^0\cong\ZZ$. If $\delta^1(p,q,r)=0$, subtracting and adding the two equations gives $2r=0$, hence $r=0$ and $p=q$. Thus
$$
\ker\delta^1=\ZZ(1,1,0)=\operatorname{im}\delta^0,
$$
so $H^1=0$. The matrix of $\delta^1$ has rank two and its $2\times2$ minors have greatest common divisor $2$, so its image has index $2$ in $\ZZ^2$. Hence $H^2\cong\ZZ_2$.

:::

:::

::: pf-step

With $\ZZ_2$ coefficients,
$$
\boxed{H^i(\RP^2;\ZZ_2)\cong\ZZ_2\quad(i=0,1,2).}
$$

::: pf-proof

Modulo $2$, $\delta^0$ has rank one and $\delta^1$ has rank one, with
$$
\delta^1(p,q,r)=(p+q+r,p+q+r).
$$
Thus $\dim\ker\delta^1=2$ and $\dim\operatorname{im}\delta^0=1$, giving one-dimensional $H^1$. The cokernel of $\delta^1$ is also one-dimensional, giving $H^2\cong\ZZ_2$.

:::

:::

::: pf-step

For the Klein bottle, choose orientations in the standard two-triangle $\Delta$-complex so that all three edges are loops and
$$
\partial U=a+b-c,
\qquad
\partial L=a-b+c.
$$
Then
$$
\delta^0=0,
\qquad
\delta^1(p,q,r)=(p+q-r,p-q+r).
$$

::: pf-proof

All vertices are identified, so the boundary of every edge is zero. The boundary formulas are read off the Klein bottle in the figure on p.102, which the book does not compute: with the two triangles oriented as stated, $\partial U = a+b-c$ and $\partial L = a-b+c$, and dualizing them as on p.191 gives the displayed coboundary.

:::

:::

::: pf-step

Therefore
$$
\boxed{H^0(K;\ZZ)=\ZZ,\quad H^1(K;\ZZ)=\ZZ,\quad H^2(K;\ZZ)=\ZZ_2.}
$$

::: pf-proof

The equations $p+q-r=0$ and $p-q+r=0$ imply $2p=0$, hence $p=0$ and $q=r$. Thus $\ker\delta^1\cong\ZZ$. The $2\times2$ minors of the matrix of $\delta^1$ have gcd $2$, so its image has index $2$ in $\ZZ^2$, giving $H^2\cong\ZZ_2$.

:::

:::

::: pf-step

With $\ZZ_2$ coefficients,
$$
\boxed{H^0(K;\ZZ_2)=\ZZ_2,\quad H^1(K;\ZZ_2)=(\ZZ_2)^2,\quad H^2(K;\ZZ_2)=\ZZ_2.}
$$

::: pf-proof

Modulo $2$, both components of $\delta^1$ are $p+q+r$, so $\delta^1$ has rank one. Since $\delta^0=0$, the kernel has dimension two and the cokernel dimension one. Every answer on this card agrees with Theorem 3.2 (p.195), which computes $H^n$ of a complex of free abelian groups from $\operatorname{Hom}(H_n,\ZZ)$ and $\operatorname{Ext}(H_{n-1},\ZZ)$: for $\RP^2$ one gets $H^1=0$ and $H^2=\Ext(\ZZ_2,\ZZ)=\ZZ_2$ with $\ZZ$ coefficients, $H^1=\Hom(\ZZ_2,\ZZ_2)=\ZZ_2$ and $H^2=\Ext(\ZZ_2,\ZZ_2)=\ZZ_2$ with $\ZZ_2$ coefficients, and likewise for the Klein bottle with $H_1=\ZZ\oplus\ZZ_2$.

:::

:::

:::

:::
