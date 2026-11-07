---
schema: qual/card@1
id: E-HAT-2.2-42
kind: problem
title: Finite group of homeomorphisms of graph injects into $GL_n(\ZZ)$ acting on $H_1$
classification:
  areas:
  - topology
  topics:
  - Homology
  - Graphs
  - Group Actions
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
- event: source-checked
  by: claude
  date: 2026-10-31
  note: Statement compared with Hatcher, Algebraic Topology, Section 2.2, Exercise 42.
- event: solution-reviewed
  by: claude
  date: 2026-10-31
  note: >-
    Read the argument in full. The topologically defined vertex set, the points with no Euclidean
    neighbourhood, is the set of vertices of valence at least three and is preserved by every
    homeomorphism; $g_*=\mathrm{id}$ forces $g$ to fix each circle, since $g_\#z_C=\pm z_{g(C)}$
    and $z_C=-z_C$ would need $2=0$; every circle contains a vertex fixed by $g$, found from a
    circle through an edge at a vertex of valence at least three; an invariant circle is then fixed
    vertex by vertex and edge by edge; each bridge is determined by the partition of circles that
    cutting it induces, which also fixes its endpoints; and finite order together with an
    increasing self-map of each open edge forces the identity. The $\ZZ_2$ example is the theta
    graph, where the reflection reverses every edge and so acts as $-\mathrm{id}$, which is the
    identity on $H_1(\cdot;\ZZ_2)$ although $g$ is not the identity.
- event: solution-written
  by: claude
  date: 2026-11-08
  note: >-
    Replaces the independently assembled circle-and-bridge proof with a complete published
    argument. Andrew Putman, The action on homology of finite groups of automorphisms of surfaces
    and graphs, Theorem 3.1, pp.4-5, proves the integral statement by quotient Euler
    characteristics. Jean-Pierre Serre, Bounds for the orders of the finite subgroups of G(k),
    Section 1.2, Lemma 1, printed p.5, proves that the kernel of GL_n(Z) to GL_n(Z/mZ) is
    torsion-free for m>=3, which reduces the modular statement to Putman's theorem. The theta
    graph gives the explicit m=2 counterexample. The earlier loop-edge correction was valid but is
    no longer needed by this different proof; DeMason p.80 explicitly says his argument is not
    fully fleshed and is not used as a completion source.
- event: solution-reviewed
  by: claude
  date: 2026-11-08
  note: >-
    Read Hatcher p.159 and the complete Putman and Serre arguments. In Putman's no-fixed-edge
    case, if p is prime and v_0 counts fixed vertices, the quotient has v vertices and e edges,
    while the original graph has p(v-v_0)+v_0 vertices and pe edges. Equality of Euler
    characteristics gives v-e=v_0, contradicting rank at least two. The general case collapses a
    maximal forest in the fixed subgraph and deletes fixed loops to reach that case. For m>2 a
    finite-order g_* congruent to the identity modulo m is itself the integral identity by Serre,
    so Putman applies. The m=2 theta-graph reflection acts as -1=1 on H_1 with Z_2 coefficients
    but is not the identity.
- event: solution-reviewed
  by: claude
  date: 2026-11-08
  note: >-
    Statement matches Exercise 42 as printed on p. 159, all three parts. The strategy was checked
    end to end: g_* = id over R with 2 nonzero forces every circle to be preserved with its
    orientation, bridges to be preserved, and then every edge and vertex to be fixed, so a
    finite-order g is the identity. Defect repaired: the graph-structure step claimed that each
    component of X minus V has closure adding two vertices, which is false for a loop edge — the
    wedge of two circles satisfies the hypotheses (n = 2, no valence-1 vertex) and has two loop
    edges — and it now says one or two points, with the loop case named. Added: Theorem 2.35
    p. 139 and Exercise 17 p. 157 for the naturality used when passing to the cellular chain map,
    and a note that 2 nonzero in R is used only in the circle step, which is what distinguishes
    m > 2 from m = 2. The m = 2 counterexample was checked: the circle with a chord is a theta
    graph with n = 2, the reflection reverses each edge and acts as -1 = 1 on H_1 with Z_2
    coefficients. What is not covered: the tree lemma and the partition argument are checked but
    not formalized; no certificate.
---

::: {.problem}
Let $X$ be a finite connected graph having no vertex that is the endpoint of just one edge, and suppose that $H_1(X; \ZZ)$ is free abelian of rank $n > 1$, so the group of automorphisms of $H_1(X; \ZZ)$ is $GL_n(\ZZ)$, the group of invertible $n \times n$ matrices with integer entries whose inverse matrix also has integer entries.
Show that if $G$ is a finite group of homeomorphisms of $X$, then the homomorphism $G \to GL_n(\ZZ)$ assigning to $g: X \to X$ the induced homomorphism $g_*: H_1(X; \ZZ) \to H_1(X; \ZZ)$ is injective.
Show the same result holds if the coefficient group $\ZZ$ is replaced by $\ZZ_m$ with $m > 2$.
What goes wrong when $m = 2$?
:::

::: {.solution}
Use **Andrew Putman, *The action on homology of finite groups of automorphisms of surfaces and graphs*, Theorem 3.1, pp. 4--5** (`tmp/sources/putman-finite-order-homology.pdf`) for integral homology, and **Jean-Pierre Serre, *Bounds for the orders of the finite subgroups of $G(k)$*, §1.2, Lemma 1, printed p. 5** (`tmp/sources/serre-bounds-finite-subgroups.pdf`) for modular coefficients.

::: pf

::: {.pf-step #integral}
If $g:X	o X$ is a homeomorphism of finite order and $g_*=\operatorname{id}$ on $H_1(X;\ZZ)$, then $g=\operatorname{id}_X$.

::: pf-proof
This is exactly Putman's Theorem 3.1. Its two other hypotheses are automatic here: $X$ has no valence-$1$ vertex, and its first integral homology has rank $n>1$, so the exceptional rank-$1$ condition is not needed. For completeness, Putman's argument is as follows.

Subdivide so that $g$ is simplicial and flips no edge, and replace $g$ by a power of prime order $p$. First suppose that $g$ fixes no edge. Since $g_*=\operatorname{id}$ on $H_1(X;\QQ)$, Proposition 1.1 of Putman's note gives $\chi(X)=\chi(X/G)$, where $G=\langle g
angle$. Let $v_0$ be the number of fixed vertices of $X$, and let $v$ and $e$ be the numbers of vertices and edges of $X/G$. All other vertex and edge orbits have size $p$. Hence $X$ has $p(v-v_0)+v_0$ vertices and $pe$ edges. Therefore
$$
v-e=\chi(X/G)=\chi(X)=p(v-v_0)+v_0-pe,
$$
so $(p-1)(v-e)=(p-1)v_0$ and $v-e=v_0$. But $\chi(X)=1-n<0$, hence $v-e<0\le v_0$, a contradiction.

In the general case, let $X^{\mathrm{fix}}$ be the fixed subgraph. Collapse a maximal forest in $X^{\mathrm{fix}}$ to a point. The quotient is homotopy equivalent to $X$, and $g$ still acts simplicially of order $p$ without flipping an edge. Every fixed edge in this quotient is a loop. Delete those fixed loops. The induced homeomorphism on the resulting subgraph now has no fixed edge, so the preceding calculation applies and forces the identity. Therefore $g=\operatorname{id}_X$.
:::

:::

::: {.pf-step #modular}
The homomorphism $G	o\operatorname{Aut}H_1(X;\ZZ_m)$ is injective for every $m>2$.

::: pf-proof
Choose a basis of $H_1(X;\ZZ)\cong\ZZ^n$. If $g_*$ is the identity on $H_1(X;\ZZ_m)$, then the integral matrix $A$ of $g_*$ satisfies $A\equiv I\pmod m$. Serre's Lemma 1 in §1.2 says that the kernel of
$$
GL_n(\ZZ)\longrightarrow GL_n(\ZZ/m\ZZ)
$$
is torsion-free for $m\ge3$. Since $g$ has finite order, $A$ has finite order and therefore $A=I$. Step [](#integral){.pf-ref} gives $g=\operatorname{id}_X$.
:::

:::

::: pf-step
The homomorphism $G	o GL_n(\ZZ)$ is injective.

::: pf-proof
This is step [](#integral){.pf-ref} applied to each element of the finite group $G$.
:::

:::

::: {.pf-step #modtwo}
For $m=2$, injectivity can fail because $-1=1$ in $\ZZ_2$.

::: pf-proof
Let $X\subset\RR^2$ be the unit circle together with the chord $[-1,1]	imes\{0\}$. It is a theta graph with vertices $(\pm1,0)$ and three edges, so $n=3-2+1=2$, and no vertex has valence $1$. Let
$$
g(x,y)=(-x,y),\qquad G=\{\operatorname{id},g\}.
$$
Orient every edge from $(-1,0)$ to $(1,0)$. Then $g$ sends each oriented edge to itself with reversed orientation. Hence $g_\#=-\operatorname{id}$ on cellular $1$-chains, so $g_*=-\operatorname{id}$ on $H_1(X;\ZZ)$, but on $H_1(X;\ZZ_2)$,
$$
g_*=-\operatorname{id}=\operatorname{id},
$$
although $g\neq\operatorname{id}_X$. This is precisely the orientation-reversal possibility excluded in the modular step when $m>2$.
:::

:::

:::
:::
