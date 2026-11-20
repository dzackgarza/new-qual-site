---
schema: qual/card@1
id: E-HAT-4.K-2
kind: problem
title: Contractible fibers of a simplicial map
classification:
  areas:
  - topology
  topics:
  - Symmetric Products
  - Quasifibrations
  - Homotopy Equivalence
relations: []
review: draft
audit:
- event: solution-written
  by: claude
  date: 2026-11-20
  note: >-
    Converted from prose to numbered steps under #2, six of them, each with its proof, and the
    locator removed: the card cited "Proposition A.2 and the discussion of s complexes" with a page,
    and now names Proposition A.2 alone, the statement that a simplicial complex is a CW complex,
    which is what the Whitehead step needs. No retained solution set covers §4.K Exercise 2, so the
    card says the argument is the card's own and follows the exercise's printed hint. Two things the
    prose compressed are steps: the intersection behaviour of the open-star covers, and the reason a
    map between weakly contractible spaces is a weak equivalence. Not checked: no certificate, and
    Corollary 4K.2's own proof was not re-read in this pass.
- event: solution-reviewed
  by: claude
  date: 2026-11-19
  note: >-
    Read against Hatcher, Algebraic Topology (2002), §4.K Exercise 2, and against
    Corollary 4K.2 in the section's own text. The argument is the Quillen fibre lemma
    route: the open stars V_sigma of L cover L, their finite intersections are the stars
    V_rho of the simplex spanned by the sigma's, and the preimages U_rho cover K; each
    U_rho deformation retracts onto the fibre f^{-1}(x_rho) by collapsing barycentric
    coordinates onto the vertex of rho, so each restriction is a weak equivalence because
    the fibre is contractible, and Corollary 4K.2 gives that f is a weak equivalence;
    simplicial complexes have CW type, so Whitehead makes f a homotopy equivalence. One
    citation was wrong: the corollary was placed on printed p. 478, and the running head
    of the section puts it on printed p. 477. Statement unchanged.
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
- event: source-corrected
  by: claude
  date: 2026-11-01
  note: >-
    Statement repaired against Hatcher's printed text: the card had dropped printed matter
    (a bracketed hint or pointer, or a printed sentence) that an audit located by word-by-word
    comparison with tmp/hat/AT.txt, and that this session re-verified at the cited lines before
    applying the repair. The restored text is the printed wording and the mathematics of the
    statement is otherwise unchanged.
---

::: {.problem}
Show that a simplicial map $f: K \to L$ is a homotopy equivalence if $f^{-1}(x)$ is contractible for all $x \in L$. [Consider the cover of $L$ by open stars of simplices and the cover of $K$ by the preimages of these open stars.]
:::

::: {.solution}
No retained solution set covers §4.K Exercise 2, so the argument is the card's own; it follows the hint printed with the exercise and uses Corollary 4K.2, the cover lemma of §4.K, and the homology form of Whitehead's theorem, Corollary 4.33.

::: pf

::: {.pf-step #cover}
For a simplex $\sigma$ of $L$ let $V_\sigma$ be its open star and $U_\sigma=f^{-1}(V_\sigma)$; the $V_\sigma$ cover $L$, the $U_\sigma$ cover $K$, and a finite intersection of them is $V_\rho$ or $U_\rho$ for the simplex $\rho$ spanned by the union of the vertices.

::: pf-proof
The open stars of all simplices cover $L$, since a point of $L$ lies in the interior of a unique simplex $\tau$ and hence in $V_\sigma$ for every face $\sigma$ of $\tau$; taking preimages gives the cover of $K$. A nonempty finite intersection $\bigcap_iV_{\sigma_i}$ is the set of points whose interior simplex contains every $\sigma_i$, that is the union of the interiors of the simplices containing all the $\sigma_i$, which is $V_\rho$ for $\rho$ spanned by their vertices; preimages commute with intersections.
:::

:::

::: {.pf-step #star}
$V_\rho$ contracts to the barycentre $x_\rho$ of $\rho$.

::: pf-proof
Every point of $V_\rho$ lies in the interior of a simplex containing $\rho$, and that simplex is the join of $\rho$ with a face of the link; straight-line motion in barycentric coordinates towards $x_\rho$ therefore stays inside that simplex, hence inside $V_\rho$, and fixes $x_\rho$ throughout.
:::

:::

::: {.pf-step #fiber}
$U_\rho$ deformation retracts onto $f^{-1}(x_\rho)$.

::: pf-proof
Write a point of a simplex of $K$ in barycentric coordinates. For each vertex $w$ of its image simplex, the sum of the coordinates over the vertices mapping to $w$ is the $w$-coordinate of the image point. Move these sums linearly towards those of $x_\rho$, scaling all coordinates in each fibre of the vertex map by the same factor; the scaling is continuous because every coordinate over a vertex of $\rho$ has positive sum throughout $U_\rho$. At the end the image is $x_\rho$, and points already over $x_\rho$ are fixed. This is a deformation retraction of $U_\rho$ onto $f^{-1}(x_\rho)$.
:::

:::

::: {.pf-step #local}
The restriction $f\colon U_\rho\to V_\rho$ is a weak homotopy equivalence for every $\rho$.

::: pf-proof
The hypothesis makes $f^{-1}(x_\rho)$ contractible, so $U_\rho$ is contractible by step [](#fiber){.pf-ref} and $V_\rho$ is contractible by step [](#star){.pf-ref}. A map between weakly contractible spaces induces an isomorphism on every homotopy group and on $\pi_0$, so the restriction is a weak homotopy equivalence.
:::

:::

::: {.pf-step #global}
$f\colon K\to L$ is a weak homotopy equivalence.

::: pf-proof
This is Corollary 4K.2 applied to the open covers $\{U_\sigma\}$ and $\{V_\sigma\}$ of steps [](#cover){.pf-ref}: the lemma says that a map whose restrictions to the members of a numerable open cover, here a cover by open stars with intersections $V_\rho$, are weak equivalences is itself a weak equivalence, and step [](#local){.pf-ref} verifies the hypothesis.
:::

:::

::: {.pf-step}
A simplicial map whose every fibre is contractible is a homotopy equivalence.

::: pf-proof
Step [](#global){.pf-ref} makes $f$ a weak homotopy equivalence, and simplicial complexes are of CW type, each being a CW complex with one cell per simplex in the barycentric subdivision (Proposition A.2); the homology form of Whitehead's theorem, Corollary 4.33, then upgrades the weak equivalence to a homotopy equivalence.
:::

:::

:::

:::

