---
schema: qual/card@1
id: P-UCTOP290-S12-1
kind: problem
title: "Cohomology ring of the torus via Poincaré duals of singular chains"
classification:
  areas:
  - topology
  topics:
  - Cohomology Ring
  - Poincaré Duality
relations: []
review: draft
---

::: problem
Glue two triangles together to make the torus $T = S^1 \times S^1$ as shown on the source sheet.
Write down singular chains $p, a, b, t$ representing generators of its homology groups in dimensions $0, 1, 1, 2$.
Now let $\alpha, \beta \in H^1$ be the Poincaré duals of $[a], [b] \in H_1$.
Show directly from the definition in singular (co)homology that $\alpha \cup \beta$ is a generator of $H^2$ and that the cohomology ring of $T$ is an exterior algebra on two generators of degree $1$.
:::

::: {.solution}
<1>1. Use the standard square model of the torus, triangulated by the diagonal from the lower-left to the upper-right corner. After the boundary identifications there is one vertex $p$, three oriented $1$-simplices $a,b,c$, and two oriented $2$-simplices $\sigma,\tau$ with
$$
\partial\sigma=a+b-c,
\qquad
\partial\tau=-a-b+c.
$$
::: {.proof}
Take $a$ to be the horizontal edge, $b$ the vertical edge, and $c$ the diagonal. For the lower-right triangle, the oriented boundary is $a+b-c$. For the upper-left triangle the top and left edges occur with the opposite boundary orientations, giving $-a-b+c$.
:::

<1>2. Thus
$$
[p]\in H_0(T),\qquad [a],[b]\in H_1(T),\qquad [t]:=[\sigma+\tau]\in H_2(T)
$$
are the standard generators, with
$$
H_0(T)\cong\mathbb Z,\quad H_1(T)\cong\mathbb Z[a]\oplus\mathbb Z[b],\quad H_2(T)\cong\mathbb Z[t].
$$
::: {.proof}
Both $a$ and $b$ are loops at the single vertex. Since $\partial(\sigma+\tau)=0$, $t=\sigma+\tau$ is a $2$-cycle. The standard cellular chain computation for this CW structure gives the displayed homology groups, and these classes generate them.
:::

<1>3. Define $1$-cocycles $\alpha,\beta$ by
$$
\alpha(a)=1,\quad \alpha(b)=0,\quad \alpha(c)=1,
$$
and
$$
\beta(a)=0,\quad \beta(b)=1,\quad \beta(c)=1.
$$
Then $[\alpha],[\beta]$ are the Poincaré-dual basis of $H^1(T;\mathbb Z)$ corresponding to $[b]$ and $-[a]$ up to the chosen orientation convention.
::: {.proof}
The cocycle conditions are
$$
\alpha(a+b-c)=1+0-1=0,
\qquad
\beta(a+b-c)=0+1-1=0,
$$
and the same for $\tau$. Their values on the homology basis $[a],[b]$ are respectively $(1,0)$ and $(0,1)$, so they form the dual basis of $H^1$; identifying this dual basis with Poincaré duals changes only the conventional signs/order determined by the orientation of $T$.
:::

<1>4. With the Alexander--Whitney definition of the singular cup product,
$$
(\alpha\smile\beta)(\sigma)
=\alpha([v_0v_1])\,\beta([v_1v_2])=1,
$$
while
$$
(\alpha\smile\beta)(\tau)=0.
$$
Hence
$$
\langle [\alpha]\smile[\beta],[t]\rangle=1.
$$
::: {.proof}
For an oriented singular $2$-simplex $[v_0v_1v_2]$, the Alexander--Whitney formula is
$$
(\alpha\smile\beta)([v_0v_1v_2])
=\alpha([v_0v_1])\beta([v_1v_2]).
$$
On $\sigma$, the first edge is $a$ and the second is $b$, giving $1\cdot1=1$. On $\tau$, the second edge is the negatively oriented horizontal edge, on which $\beta$ is zero. Summing over $t=\sigma+\tau$ gives $1$.
:::

<1>5. Therefore $[\alpha]\smile[\beta]$ is a generator of $H^2(T;\mathbb Z)$.
::: {.proof}
The group $H^2(T;\mathbb Z)\cong\mathbb Z$ is detected by evaluation on the fundamental class $[t]$. A class evaluating to $1$ is a generator.
:::

<1>6. The squares $[\alpha]^2$ and $[\beta]^2$ vanish and
$$
[\beta]\smile[\alpha]=-[\alpha]\smile[\beta].
$$
::: {.proof}
Integral cohomology is graded-commutative, so for a degree-$1$ class $x$ one has $x^2=-x^2$, hence $2x^2=0$. Since $H^2(T;\mathbb Z)$ is torsion-free, $x^2=0$. Graded commutativity also gives the displayed anticommutation relation.
:::

<1>7. Consequently
$$
\boxed{H^*(T;\mathbb Z)\cong\Lambda_{\mathbb Z}([\alpha],[\beta])}
$$
with both generators in degree $1$.
::: {.proof}
The groups have ranks $1,2,1$ in degrees $0,1,2$, respectively; <1>5 gives the nonzero product generating degree $2$, while <1>6 gives exactly the exterior-algebra relations.
:::
:::
