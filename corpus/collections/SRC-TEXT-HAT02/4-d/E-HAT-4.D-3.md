---
schema: qual/card@1
id: E-HAT-4.D-3
kind: problem
title: Cohomology of Stiefel manifolds via Leray--Hirsch
classification:
  areas:
  - topology
  topics:
  - Fiber Bundles
  - Cohomology
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-30
- event: solution-reviewed
  by: claude
  date: 2026-11-19
  note: >-
    Structured into Lamport steps from the card's own prose. Supplied the two statements the prose
    used in a clause: that adding a trivial bundle leaves the positive-degree Chern classes of E
    unchanged, which is why the whole bundle E is stably trivial and not merely of vanishing top
    class; and the reason the vanishing Euler class gives both the class x restricting to a generator
    on each fibre and the splitting of the Gysin sequence into short exact sequences. Recorded the
    fibre dimensions 2(k-n+1)-1 = 2k-2n+1 and 4(k-n+1)-1 = 4k-4n+3 as computations rather than
    assertions, and the induction base V_1 = S^{2k-1} with the odd-degree argument for the vanishing
    of squares. The page numbers were then checked against the retained PDF at
    tmp/sources/hatcher-2002-algebraic-topology.pdf, printed page = PDF page - 9: Theorem 4D.1 on
    p. 432 (PDF 441), the Gysin sequence on p. 438 (PDF 447) and the identification of the Euler
    class with the top Chern class on p. 444 (PDF 453), each as cited.
- event: source-checked
  by: claude
  date: 2026-11-20
  note: >-
    Issue #184: the page locators in the card's text are removed; Theorem 4D.1 (Leray--Hirsch), the Gysin sequence of §4.D and Corollary 4D.3 are cited by
    number, and the Gysin sequence, which the book leaves unnumbered, by the section that
    states it, each read in `tmp/sources/hatcher-2002-algebraic-topology.md`. The earlier
    events keep their text (QUAL-11); these citations supersede their page locators. No step
    changes.

---

::: {.problem}
Use the Leray–Hirsch theorem as in Corollary 4D.3 to compute $H^*(V_n(\CC^k); \ZZ) \approx \Lambda_\ZZ[x_{2k-2n+1}, x_{2k-2n+3}, \ldots, x_{2k-1}]$ and similarly in the quaternionic case.
:::

::: {.solution}
This is Hatcher Exercise 4.D.3, computed as in Corollary 4D.3. No published solution set is transcribed: the argument is the card's own, and the numbered results are Hatcher's Theorem 4D.1 (Leray--Hirsch), the Gysin sequence (§4.D) and the identification of the Euler class with the top Chern class (§4.D).

::: pf

::: {.pf-step #bundle}
The projection $p\colon V_{n}(\CC^{k})\to V_{n-1}(\CC^{k})$ forgetting the last frame vector is a fibre bundle with fibre the unit sphere of a complex bundle $E$ of rank $k-n+1$, that fibre being $S^{2k-2n+1}$.

::: pf-proof
A point of $V_{n-1}(\CC^{k})$ is an orthonormal $(n-1)$-frame, and the fibre over it consists of the unit vectors orthogonal to those $n-1$ vectors, that is the unit sphere of the orthogonal complement, a complex vector space of dimension $k-(n-1)=k-n+1$. These complements fit together as a complex vector bundle $E$ over $V_{n-1}(\CC^{k})$, the orthogonal complement of the trivial bundle spanned by the frame, and the unit sphere of a complex bundle of rank $m$ has real dimension $2m-1$, here $2(k-n+1)-1=2k-2n+1$.
:::
:::

::: {.pf-step #trivial}
$E\oplus\underline{\CC}^{n-1}\cong\underline{\CC}^{k}$, so all Chern classes of $E$ vanish, in particular its Euler class $c_{k-n+1}(E)$.

::: pf-proof
The tautological $(n-1)$-frame trivializes the orthogonal complement of $E$: the sum of $E$ with the bundle spanned by the frame vectors is the trivial bundle $V_{n-1}(\CC^{k})\times\CC^{k}$. Adding a trivial bundle does not change Chern classes of positive degree, so $c_{i}(E)=0$ for $i\geq1$, and the Euler class, which is the top Chern class $c_{k-n+1}(E)$ of the oriented real bundle underlying $E$ (§4.D), vanishes.
:::
:::

::: {.pf-step #gysin}
There is a class $x_{2k-2n+1}\in H^{2k-2n+1}(V_{n}(\CC^{k});\ZZ)$ restricting to a generator of the cohomology of each fibre, and the Gysin sequence of the oriented sphere bundle splits into short exact sequences.

::: pf-proof
The Euler class is the obstruction to a class restricting to a generator on every fibre, so its vanishing produces such an $x$; this is read off the Gysin sequence of the oriented sphere bundle $S(E)\to V_{n-1}(\CC^{k})$ (§4.D), whose fibre sphere is $S^{2k-2n+1}$ and whose Euler class is zero by step [](#trivial){.pf-ref}. With the Euler class zero the multiplication by it in the Gysin sequence is the zero map, and the sequence breaks into short exact sequences $0\to H^{q}(V_{n-1})\to H^{q}(V_{n})\to H^{q-(2k-2n+1)}(V_{n-1})\to0$.
:::
:::

::: {.pf-step #hirsch}
$H^{*}(V_{n}(\CC^{k});\ZZ)$ is a free module over $H^{*}(V_{n-1}(\CC^{k});\ZZ)$ with basis $\{1,x_{2k-2n+1}\}$.

::: pf-proof
Leray--Hirsch (Theorem 4D.1) applies to a fibre bundle whose fibre cohomology is free on classes restricting to generators: here the fibre is a sphere, so its cohomology is free on $1$ and the generator, and step [](#gysin){.pf-ref} supplies a global class restricting to the generator. The theorem concludes that $H^{*}$ of the total space is free over $H^{*}$ of the base with those classes as a basis.
:::
:::

::: {.pf-step #complex}
$H^{*}(V_{n}(\CC^{k});\ZZ)\cong\Lambda_{\ZZ}[x_{2k-2n+1},x_{2k-2n+3},\dots,x_{2k-1}]$.

::: pf-proof
Induct on $n$ from $V_{1}(\CC^{k})=S^{2k-1}$, whose cohomology is the exterior algebra on one generator in degree $2k-1$, as in the computation of Corollary 4D.3. At each step step [](#hirsch){.pf-ref} multiplies the number of additive generators by two, adjoining a generator in degree $2k-2i+1$ for the step from $V_{i-1}$ to $V_{i}$. Each such generator has odd degree, so graded commutativity gives $x^{2}=-x^{2}$, that is $x^{2}=0$; together with freeness this says the products of distinct generators form an additive basis and the algebra is the exterior algebra on them.
:::
:::

::: {.pf-step #quaternionic}
In the quaternionic case $H^{*}(V_{n}(\quaternions^{k});\ZZ)\cong\Lambda_{\ZZ}[x_{4k-4n+3},x_{4k-4n+7},\dots,x_{4k-1}]$.

::: pf-proof
The same three inputs hold with $\CC$ replaced by $\quaternions$: the fibre of $V_{n}(\quaternions^{k})\to V_{n-1}(\quaternions^{k})$ is the unit sphere of a quaternionic bundle of rank $k-n+1$, of real dimension $4(k-n+1)-1=4k-4n+3$; that bundle is stably trivial by the frame decomposition, so its integral Euler class vanishes; and the fibre cohomology is again free on one generator, so the Gysin and Leray--Hirsch argument goes through unchanged, starting from $V_{1}(\quaternions^{k})=S^{4k-1}$ and adjoining one generator of degree $4k-4i+3$ at each step.
:::
:::
:::

:::
