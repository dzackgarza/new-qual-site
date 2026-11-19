---
schema: qual/card@1
id: E-HAT-3.2-1
kind: problem
title: Cup product structure on closed orientable surfaces
classification:
  areas:
  - topology
  topics:
  - Cohomology
  - Cup Product
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 3.2, Exercise 1; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
- event: source-checked
  by: claude
  date: 2026-10-31
  note: Statement compared with Hatcher, Algebraic Topology, Section 3.2, Exercise 1; it matches the printed text.
- event: solution-reviewed
  by: claude
  date: 2026-10-31
  note: >-
    Read the computation: $q^*$ carries the two generators of each $H^1(T_i)$ to $a_i,b_i$ and
    $q^*(u_i)=u$ because the composite of $q$ with the retraction onto $T_i$ has degree one, so
    naturality turns $x_i\smile y_i=u_i$ into $a_i\smile b_j=\delta_{ij}u$; on the torus
    $x_i^2=y_i^2=0$, and products of classes on different summands vanish, which gives the
    remaining relations. Since $H^k(M_g)=0$ for $k>2$ these relations describe the whole ring.
- event: solution-reviewed
  by: claude
  date: 2026-11-07
  note: >-
    Statement matches Exercise 1 (p.228). Rechecked the computation: q^* identifies the generators of H^1(T_i) with a_i,b_i and q^*(u_i) = u because r_i q has degree 1, so naturality of the cup product turns x_i y_i = u_i into a_i b_i = u; products from distinct summands vanish. The vanishing is now proved by the relative cup product of p.209 in the pairs (W,T_j) and (W,T_i) rather than asserted, and naturality is cited to Proposition 3.10 p.210. Not covered: the g = 0 case is stated separately, and no torus computation is redone, the exercise assuming it.
- event: solution-written
  by: claude
  date: 2026-11-19
  note: >-
    Restructured into a structured proof under #2, the retained Sam solution left as the source of the
    argument as the card already recorded. Re-checked: $g=0$ has $H^*$ concentrated in degrees $0,2$
    with vanishing products; the quotient $M_g\to\bigvee T_i$ collapses the joining genus-$0$
    surface, and the composite with the retraction onto $T_i$ has degree $1$, so $q^*$ carries
    $x_i,y_i$ to $a_i,b_i$ and $u_i$ to $u$; the torus ring is the assumed input; the vanishing of
    products supported on distinct summands is the relative cup product argument; and the six
    products follow by naturality. Added: the symplectic basis as an explicit step, the degree
    computation behind $q^*(u_i)=u$, and the observation that no room remains above degree $2$, so the
    listed products determine the ring. No defect found in the statement, §3.2 Exercise 1 on printed
    p. 228.
---

::: {.problem}
Assuming as known the cup product structure on the torus $S^1 \times S^1$, compute the cup product structure in $H^*(M_g)$ for $M_g$ the closed orientable surface of genus $g$ by using the quotient map from $M_g$ to a wedge sum of $g$ tori.
:::

::: {.solution}
The argument is that of the retained published solution, Steven V. Sam, *Solutions to Algebraic Topology* (2008), §3.2 Exercise 1, printed p. 13 (`tmp/sources/hatcher-solutions-sam-2008.pdf`): the quotient from $M_g$ to the wedge of $g$ tori, naturality of the cup product, and the vanishing of products supported on distinct summands via the relative cup product.

::: pf

::: {.pf-step #sphere}
For $g=0$, $H^*(S^2;\ZZ)$ is $\ZZ$ in degrees $0$ and $2$ with the square of the degree-$2$ class equal to $0$.

::: pf-proof
$S^2$ has the cohomology of the suspension of $S^1$, namely $\ZZ$ in degrees $0$ and $2$ and $0$ otherwise, and every cup product of positive-degree classes lands in $H^4(S^2)=0$.
:::

:::

::: {.pf-step #setup}
For $g\ge1$ there is a symplectic basis $a_1,b_1,\ldots,a_g,b_g$ of $H^1(M_g;\ZZ)$, an orientation class $u$ generating $H^2(M_g;\ZZ)\cong\ZZ$, and a quotient map $q\colon M_g\to W=\bigvee_{i=1}^gT_i$ collapsing a genus-zero subsurface joining the $g$ punctured tori to the wedge point.

::: pf-proof
$M_g$ is the union of $g$ punctured tori joined by a genus-$0$ surface with $g$ boundary components; collapsing that surface to a point identifies its boundary circles with one another, and the quotient is the wedge of the $g$ closed tori. The symplectic basis is the standard one: the $a_i,b_i$ are carried by the standard loops and pair by $a_i\cdot b_j=\delta_{ij}$, $a_i\cdot a_j=b_i\cdot b_j=0$.
:::

:::

::: {.pf-step #pullbacks}
With $x_i,y_i$ the degree-one generators of $H^1(T_i)$ and $u_i$ the orientation class of $T_i$, one has $q^*(x_i)=a_i$, $q^*(y_i)=b_i$ and $q^*(u_i)=u$.

::: pf-proof
On $H^1$ the map $q^*$ is injective on each summand $H^1(T_i)$ and carries the two generators to the corresponding surface loops $a_i,b_i$, since the composition of $q$ with the retraction $W\to T_i$ is the collapse of the complementary tori, which is degree $1$ on the $i$-th torus and therefore induces an isomorphism on $H^1$ of that summand. For degree $2$ the same composition has degree $1$, so $q^*(u_i)=u$.
:::

:::

::: {.pf-step #torus-ring}
On each torus, $x_i\smile y_i=u_i$, $y_i\smile x_i=-u_i$ and $x_i^2=y_i^2=0$.

::: pf-proof
This is the assumed cup product structure on $S^1\times S^1$: $H^*(T^2)=\Lambda(x,y)$ with $x\smile y$ the orientation class, the product being graded commutative, so $x\smile y=-y\smile x$, and $x^2=y^2=0$ because $x,y$ have odd degree.
:::

:::

::: {.pf-step #distinct-summands}
If $i\ne j$ then every product of a class pulled back from $T_i$ with one pulled back from $T_j$ vanishes.

::: pf-proof
Let $\alpha=q^*\alpha'$ and $\beta=q^*\beta'$ with $\alpha'\in H^*(T_i)$, $\beta'\in H^*(T_j)$ and $i\ne j$. The restriction of $\alpha$ to $T_j$ is zero, so $\alpha$ lifts to a class in the relative group $H^*(W,T_j;R)$ by the long exact sequence of the pair (p. 200). The relative cup product (p. 209) of a class relative to $T_i$ with one relative to $T_j$ lands in $H^*(W,T_i\cup T_j;R)=H^*(W,W;R)=0$, and naturality of the cup product (Proposition 3.10, p. 210) identifies that product with $\alpha\smile\beta$. Hence $\alpha\smile\beta=0$.
:::

:::

::: {.pf-step}
$\boxed{a_i\smile b_j=\delta_{ij}u,\qquad b_i\smile a_j=-\delta_{ij}u,\qquad a_i\smile a_j=b_i\smile b_j=0}$.

::: pf-proof
For $i=j$, step [](#torus-ring){.pf-ref} together with step [](#pullbacks){.pf-ref} gives $a_i\smile b_i=q^*(x_i\smile y_i)=q^*(u_i)=u$ and $b_i\smile a_i=-u$, while $a_i^2=b_i^2=q^*(0)=0$. For $i\ne j$, step [](#distinct-summands){.pf-ref} gives all four products zero. Since $H^k(M_g;\ZZ)=0$ for $k>2$, these relations together with the unit of $H^0$ determine the whole ring; the case $g=0$ is step [](#sphere){.pf-ref}.
:::

:::

:::
:::
