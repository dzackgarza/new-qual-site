---
schema: qual/card@1
id: E-HAT-2.1-7
kind: problem
title: $\Delta$-complex structure on $S^3$ with a single 3-simplex
classification:
  areas:
  - topology
  topics:
  - Homology
  - Simplicial Complexes
  - Spheres
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

::: {.problem}
Find a way of identifying pairs of faces of $\Delta^3$ to produce a $\Delta$-complex structure on $S^3$ having a single 3 simplex, and compute the simplicial homology groups of this $\Delta$-complex.
:::

::: {.solution}
Write $\Delta^3=[v_0,v_1]*[v_2,v_3]$ as the join of its two opposite edges. Pair the faces $[v_1,v_2,v_3]$ and $[v_0,v_2,v_3]$ by sending $v_1$ to $v_0$ and fixing $v_2,v_3$. Pair $[v_0,v_1,v_3]$ and $[v_0,v_1,v_2]$ by sending $v_3$ to $v_2$ and fixing $v_0,v_1$.

::: pf

::: {.pf-step #s1}

The face-paired quotient is homeomorphic to $S^3$.

::: pf-proof

The first pairing identifies the two endpoints of $[v_0,v_1]$ throughout its join with $[v_2,v_3]$. The second does the same for $[v_2,v_3]$. Thus the quotient is
$$
([v_0,v_1]/(v_0\sim v_1))*([v_2,v_3]/(v_2\sim v_3))
\cong S^1*S^1\cong S^3.
$$
The last homeomorphism sends the join class of $(z,w,t)$ to $(\sqrt{1-t}\,z,\sqrt{t}\,w)$ in the unit sphere of $\CC^2$.
The face pairings are affine and preserve vertex order on each paired face, so they also give the requested $\Delta$-complex structure.

:::

:::

::: {.pf-step #s2}

The quotient has two vertices $A=[v_0]=[v_1]$ and $B=[v_2]=[v_3]$, three edges $a=[v_0,v_1]$, $b=[v_2,v_3]$, $c=[v_0,v_2]$, two faces $P=[v_1,v_2,v_3]$, $Q=[v_0,v_1,v_3]$, and one $3$-simplex $\sigma$.

::: pf-proof

The face pairings identify the four edges joining one of $v_0,v_1$ to one of $v_2,v_3$, giving $c$. The opposite edges $a,b$ remain distinct. Each pair of faces gives one $2$-simplex.

:::

:::

::: {.pf-step #s3}

The simplicial boundary maps are
$$
\partial_3(\sigma)=0,\qquad
\partial_2(P)=b,\qquad
\partial_2(Q)=a,\qquad
\partial_1(a)=\partial_1(b)=0,\qquad
\partial_1(c)=B-A.
$$

::: pf-proof

With the chosen face orientations,
$$
\partial_3(\sigma)=P-P+Q-Q=0.
$$
The simplicial face formulas give
$$
\partial P=[v_2,v_3]-[v_1,v_3]+[v_1,v_2]=b-c+c=b
$$
and
$$
\partial Q=[v_1,v_3]-[v_0,v_3]+[v_0,v_1]=c-c+a=a.
$$
The edge boundaries follow from their endpoints.

:::

:::

::: {.pf-step #s4}

The simplicial homology groups are
$$
\boxed{H_0\cong H_3\cong\ZZ,\qquad H_1=H_2=0,\qquad H_k=0\ (k>3).}
$$

::: pf-proof

The chain groups in degrees $0$ through $3$ have ranks $2,3,2,1$. Step [](#s3){.pf-ref} shows that $\operatorname{im}\partial_1=\ZZ(B-A)$, $\ker\partial_1=\ZZ a\oplus\ZZ b=\operatorname{im}\partial_2$, $\ker\partial_2=0$, and $\ker\partial_3=\ZZ\sigma$. There are no higher simplices.

:::

:::

:::
:::
