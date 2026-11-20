---
schema: qual/card@1
id: E-HAT-3.3-33
kind: problem
title: Boundary of contractible manifold is a homology sphere
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
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
- event: source-checked
  by: claude
  date: 2026-10-31
  note: Statement compared with Hatcher, Algebraic Topology, Section 3.3, Exercise 33; it matches the printed text.
- event: solution-reviewed
  by: claude
  date: 2026-10-31
  note: >-
    Read the argument: for contractible $M$, Lefschetz duality gives $H_i(M,\partial M)=\ZZ$ only
    for $i=n$, and the reduced long exact sequence of the pair then gives
    $\widetilde H_i(\partial M)=\ZZ$ only for $i=n-1$, including the case $n=1$.
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Rewritten as a Lamport structured proof of the argument above, with the two steps the
    prose left implicit made explicit: $M$ is orientable because a double cover of a simply
    connected space is trivial, and $\partial M$ is nonempty because a closed connected
    orientable $n$-manifold has $H_n=\ZZ$. Lefschetz duality is cited as Theorem 3.43,
    printed p. 254, in the case $A=\varnothing$; the reduced long exact sequence of the pair,
    printed p. 118, gives the isomorphism with the boundary's reduced homology. Statement
    re-read in Hatcher, §3.3 Exercise 33, printed p. 260. Not claimed: a retained solution
    set; the Hatcher sets in `tmp/sources` do not reach §3.3 Exercise 33, so the argument is
    the card's own.
---

::: {.problem}
Show that if $M$ is a compact contractible $n$-manifold then $\partial M$ is a homology $(n-1)$-sphere, that is, $H_i(\partial M; \ZZ) \approx H_i(S^{n-1}; \ZZ)$ for all $i$.
:::

::: {.solution}
The statement is Hatcher, *Algebraic Topology* (2002), §3.3 Exercise 33. No retained solution set covers this exercise — Guanyu Li's set stops at §3.3 Exercise 11 and Steven V. Sam's at Exercise 32, and no other set in `tmp/sources` reaches §3.3 — so the argument below is the card's own; it uses Lefschetz duality, Theorem 3.43, and the orientable double cover of §3.3.

Throughout $M$ is a compact contractible $n$-manifold with $n\ge1$, homology is taken with $\ZZ$ coefficients unless written otherwise, and $\widetilde H$ denotes reduced homology.

::: pf

::: {.pf-step #orientable}
$M$ is orientable.

::: pf-proof
Every manifold has an orientable two-sheeted covering space $\widehat M\to M$ (§3.3), and for $M$ connected that cover has either one or two components (Proposition 3.25). A covering space of a simply connected space is a disjoint union of copies of the base: over a point of $M$ the fibre has two points, the cover is connected and locally path connected, and its components are the images of the lifts of $M$ at each point of the fibre, each a homeomorphic copy of $M$ by the lifting criterion, Proposition 1.33. So $\widehat M$ is two copies of $M$, which is what orientability of $M$ means.
:::

:::

::: {.pf-step #contractible-cohomology}
$H^0(M;\ZZ)=\ZZ$ and $H^{j}(M;\ZZ)=0$ for $j>0$.

::: pf-proof
$M$ is contractible, hence path connected, so $H^0(M;\ZZ)=\ZZ$ and every cohomology group above degree $0$ vanishes: the identity factors through a point up to homotopy, and $H^j$ is a homotopy functor. Both $H^0(M;\ZZ)=\ZZ$ and $H^j(M;\ZZ)=0$ for $j>0$ are also the cohomology of a point.
:::

:::

::: {.pf-step #duality}
$H_i(M,\partial M;\ZZ)=\ZZ$ for $i=n$ and $0$ for $i\ne n$.

::: pf-proof
Apply Theorem 3.43 (Lefschetz duality) with $A=\varnothing$ and $B=\partial M$, which is the case the theorem calls Lefschetz duality: cap product with a fundamental class gives $H^{j}(M;\ZZ)\cong H_{n-j}(M,\partial M;\ZZ)$ for all $j$. A fundamental class exists because $M$ is compact and orientable, by step [](#orientable){.pf-ref}. By step [](#contractible-cohomology){.pf-ref} the left side is $\ZZ$ for $j=0$ and $0$ otherwise, so $H_i(M,\partial M;\ZZ)=\ZZ$ when $i=n-j=n$ and $0$ when $i\ne n$.
:::

:::

::: {.pf-step #les}
$\widetilde H_i(\partial M;\ZZ)=\ZZ$ for $i=n-1$ and $0$ otherwise.

::: pf-proof
The reduced homology of $M$ vanishes, since $M$ is contractible. The reduced long exact sequence of the pair $(M,\partial M)$ (§2.1) therefore reads
$$
0= \widetilde H_i(M)\longrightarrow H_i(M,\partial M)\xrightarrow{\ \partial\ } \widetilde H_{i-1}(\partial M)\longrightarrow \widetilde H_{i-1}(M)=0 ,
$$
so $\partial$ is an isomorphism $\widetilde H_{i-1}(\partial M;\ZZ)\cong H_i(M,\partial M;\ZZ)$ for every $i$. By step [](#duality){.pf-ref} the right side is $\ZZ$ for $i=n$ and $0$ otherwise; replacing $i-1$ by $i$ gives the claim.
:::

:::

::: {.pf-step #nonempty-boundary}
$\partial M\ne\varnothing$, and $H_0(\partial M;\ZZ)=\ZZ\oplus\widetilde H_0(\partial M;\ZZ)$.

::: pf-proof
If $\partial M$ were empty, $M$ would be a closed connected orientable $n$-manifold, so $H_n(M;\ZZ)\cong\ZZ$ (Theorem 3.26), contradicting the vanishing of the reduced homology of a contractible space in degree $n\ge1$. Hence $\partial M\ne\varnothing$, and a nonempty space has $H_0=\ZZ\oplus\widetilde H_0$ by the definition of reduced homology in degree $0$.
:::

:::

::: {.pf-step #sphere}
$\widetilde H_i(S^{n-1};\ZZ)=\ZZ$ for $i=n-1$ and $0$ otherwise.

::: pf-proof
For $n\ge2$ this is the standard computation of the homology of spheres (Theorem 2.1 and Exercise 2.1.15 and 114); for $n=1$ the sphere $S^0$ is two points, so $H_0=\ZZ^2$ and $\widetilde H_0=\ZZ$, which is the same description.
:::

:::

::: {.pf-step #conclusion}
$H_i(\partial M;\ZZ)\cong H_i(S^{n-1};\ZZ)$ for every $i$, that is, $\partial M$ is a homology $(n-1)$-sphere.

::: pf-proof
Combine step [](#les){.pf-ref} with step [](#sphere){.pf-ref}: $\widetilde H_i(\partial M)=\widetilde H_i(S^{n-1})$ for all $i$. In degree $0$, step [](#nonempty-boundary){.pf-ref} and step [](#sphere){.pf-ref} give $H_0(\partial M)=\ZZ\oplus\widetilde H_0(\partial M)$ and $H_0(S^{n-1})=\ZZ\oplus\widetilde H_0(S^{n-1})$, equal because the reduced groups agree; in degree $i\ne0$ the unreduced and reduced groups coincide. This includes $n=1$, where $\partial M$ is a nonempty compact $0$-manifold, hence two points, and $H_0(\partial M)=\ZZ^2=H_0(S^0)$.
:::

:::

:::
:::
