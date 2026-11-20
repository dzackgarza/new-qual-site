---
schema: qual/card@1
id: E-HAT-3.3-30
kind: problem
title: Boundary of orientable manifold is orientable
classification:
  areas:
  - topology
  topics:
  - Poincaré Duality
  - Manifolds
  - Cohomology
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 3.3, Exercise 30; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
- event: source-checked
  by: claude
  date: 2026-10-31
  note: Statement compared with Hatcher, Algebraic Topology, Section 3.3, Exercise 30; it matches the printed text.
- event: solution-reviewed
  by: claude
  date: 2026-10-31
  note: >-
    Read the argument: in a collar the local orientation module of $M$ splits as the tensor product
    of the local orientation module of $\partial M$ with the orientation module of the interval
    factor, and dividing by the interval generator gives boundary orientations that agree on
    overlaps.
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Lamport structure for the boundary orientation, which is what Queue D asks for on this card, together with one change of argument. The prose began from a collar of the boundary; the exercise does not assume compactness, and Hatcher's collar theorem (Proposition 3.42, printed p. 253) is stated for compact manifolds and appears later in the book, so the argument now runs from a boundary chart, which the definition of a manifold with boundary supplies. The identification H_n(M, M-x;R) = H_{n-1}(dM, dM-x;R) is now a step with its excision, chart and cross-product pieces named (Theorem 3.18, printed p. 241), the generator statement is proved from the R-linearity of that isomorphism, and the passage of local consistency to the boundary is a step rather than a sentence. The definition of R-orientation for a manifold with boundary that the proof uses is stated in the lead. No retained set covers this exercise; the card says so. Statement unchanged: Hatcher §3.3 Exercise 30, printed p. 260.
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Lamport structure for the boundary orientation, which is what Queue D asks for on this card. The argument is the card's own (no retained set reaches exercise 30, and the card says so) and is the contraction of the interior orientation with the normal direction, written as three steps: the product isomorphism along the collar, the extraction of the boundary generator with its independence of the normal parameter, and the transfer of local consistency. Two things the prose left implicit are now stated. First, the definition of R-orientability used is the one for the interior, since H_n(M, M-y;R) vanishes at boundary points themselves (already for M = [0, 1)), so the local classes are taken at collar points above the boundary. Second, the collar is named as an external input rather than assumed: Hatcher proves it for compact manifolds (Proposition 3.42, printed p. 253) and remarks that paracompact ones follow; in general it is Brown's collaring theorem. No statement repair: the exercise is Hatcher §3.3 Exercise 30, printed p. 260.
---

::: {.problem}
Show that the boundary of an $R$-orientable manifold is also $R$-orientable.
:::

::: {.solution}
No retained solution set covers this exercise: the Hatcher sets in the checkout reach §3.3 in Li (exercises 3, 4, 8, 10, 11, 17, 18, 25), Sam (8, 17, 32) and Stanford 215C Set 4 (21, 22, 24), and none holds exercise 30. The argument is the card's own, checked against Hatcher, *Algebraic Topology* (2002), §3.3 Exercise 30.

Throughout, $M$ is an $n$-manifold with boundary and *$R$-orientable* means that its interior carries an $R$-orientation in the sense of §3.3: a function $y\mapsto\mu_y$ on the interior points with $\mu_y$ a generator of $H_n(M,M-\{y\};R)$ and the local consistency that every $y$ has a neighbourhood $U$ and a class in $H_n(M,M-\overline U;R)$ restricting to $\mu_z$ for all $z\in U$. The one external input is a collar of the boundary, $c:\partial M\times[0,\varepsilon)\to M$, with $c(x,0)=x$: Hatcher proves that a compact manifold with boundary has one (Proposition 3.42) and remarks that the same construction gives collars for paracompact manifolds; for an arbitrary manifold with boundary it is Brown's collaring theorem.

::: pf

::: {.pf-step #product}
For $x\in\partial M$ and $0<t<\varepsilon$ the collar gives an isomorphism
$$
H_n\bigl(M,M-\{c(x,t)\};R\bigr)\;\cong\;H_{n-1}\bigl(\partial M,\partial M-\{x\};R\bigr)\otimes_R H_1\bigl((0,\varepsilon),(0,\varepsilon)-\{t\};R\bigr),
$$
natural in $(x,t)$.

::: pf-proof
The collar is a homeomorphism onto an open neighbourhood of $\partial M$ carrying $\partial M\times\{0\}$ to $\partial M$, so near $c(x,t)$ the pair $(M,M-\{c(x,t)\})$ is homeomorphic to the product of the pairs $(\partial M,\partial M-\{x\})$ and $((0,\varepsilon),(0,\varepsilon)-\{t\})$; excision replaces $M$ by that neighbourhood, and the relative cross product computes the homology of the product pair $(X\times Y,\,A\times Y\cup X\times B)$ from the homology of the pairs $(X,A)$ and $(Y,B)$ with $X=\partial M$, $A=\partial M-\{x\}$, $Y=(0,\varepsilon)$, $B=(0,\varepsilon)-\{t\}$, whose $A\times Y\cup X\times B$ is exactly the complement of $c(x,t)$; Hatcher states the relative cross product for CW pairs in Theorem 3.18, in cohomology, the homology statement used here being its counterpart, and its hypothesis on finite generation is met because the second factor is an open interval. All the maps used are induced by the collar and by inclusions of smaller collar neighbourhoods, which is the naturality claimed.
:::

:::

::: {.pf-step #generator}
The increasing coordinate on $(0,\varepsilon)$ singles out a generator $\nu_t$ of $H_1((0,\varepsilon),(0,\varepsilon)-\{t\};R)$, the classes $\nu_t$ for different $t$ corresponding under the inclusions; writing the given orientation class as $\mu_x^{\partial}\otimes\nu_t$ defines $\mu_x^{\partial}\in H_{n-1}(\partial M,\partial M-\{x\};R)$, which is a generator and does not depend on $t$.

::: pf-proof
$H_1((0,\varepsilon),(0,\varepsilon)-\{t\};R)\cong R$ is generated by the class of a $1$-simplex running from a point below $t$ to a point above it, and the increasing coordinate gives such a class canonically; the inclusions $(0,\varepsilon)-\{t\}\hookrightarrow(0,\varepsilon)$ relate the classes for different $t$ by the identity on this generator. Since $\mu_{c(x,t)}$ is a generator of $H_n(M,M-\{c(x,t)\};R)$ and the isomorphism of step [](#product){.pf-ref} is $R$-linear with second factor $R$, the first factor is $\cong R$ and $\mu_x^{\partial}$ generates it: the map $R\to H_{n-1}(\partial M,\partial M-\{x\};R)$, $1\mapsto\mu_x^{\partial}$, becomes surjective after tensoring with the identity on the second factor, hence is surjective. Independence of $t$ is the compatibility of the $\nu_t$ just recorded together with the local consistency of the orientation of $M$ along the collar line $t\mapsto c(x,t)$.
:::

:::

::: {.pf-step #consistency}
The classes $\mu_x^{\partial}$ are locally consistent on $\partial M$, so $x\mapsto\mu_x^{\partial}$ is an $R$-orientation of $\partial M$.

::: pf-proof
Let $x\in\partial M$ and let $B$ be a ball around $x$ in $\partial M$ so small that $B\times[0,\varepsilon)\subset\partial M\times[0,\varepsilon)$ lies inside the collar and the orientation of $M$ is carried by a single class over the corresponding neighbourhood of $M$, say $\mu\in H_n(M,M-\overline{B\times[0,\varepsilon/2)};R)$ restricting to $\mu_{c(y,s)}$ for all $(y,s)$ in that set. Write each restricted class as $\mu_y^{\partial}\otimes\nu_s$ by step [](#generator){.pf-ref}, with $\nu_s$ the fixed generator of the interval factor; then the coefficient $\mu_y^{\partial}$ is independent of $s$, and the class $\mu$ corresponds under step [](#product){.pf-ref} for the product $B\times(0,\varepsilon)$ to a single class in $H_{n-1}(\partial M,\partial M-\overline B;R)$ restricting to $\mu_y^{\partial}$ for every $y\in B$. So every point of $\partial M$ has a neighbourhood in $\partial M$ carrying one class that restricts to the local classes there, which is local consistency. Hence $\partial M$ carries an $R$-orientation and is $R$-orientable.
:::

:::

:::
:::
