---
schema: qual/card@1
id: E-HAT-3.3-17
kind: problem
title: Direct limits commute with homology
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
  note: Checked against Hatcher, Algebraic Topology, Section 3.3, Exercise 17; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
- event: source-checked
  by: claude
  date: 2026-10-31
  note: Statement compared with Hatcher, Algebraic Topology, Section 3.3, Exercise 17; it matches the printed text.
- event: solution-reviewed
  by: claude
  date: 2026-10-31
  note: >-
    Read the argument: an element of the limit that dies does so at a later stage, so exactness
    passes to the limit; then direct limits, being exact, commute with the kernels, images and
    cokernels in $0\to Z_n\to C_n\to B_{n-1}\to0$ and $0\to B_n\to Z_n\to H_n\to0$.
- event: source-checked
  by: claude
  date: 2026-11-07
  note: >-
    Added the published corroboration: Steven V. Sam, Solutions to Algebraic Topology (2008),
    SS3.3 Exercise 17, printed pp.15-16, proves the same statement by an explicit comparison map.
    Read it against this card: Sam's surjectivity and injectivity steps pass to a later stage of the
    directed system, which is the same device as the card's, and the two arguments agree. The
    printed page is cited because the file's cover sheet shifts the page index by one.
- event: source-checked
  by: claude
  date: 2026-11-07
  note: >-
    Second published solution located: Math 538 homework solutions, HMW 4 handwritten p.3 (PDF page
    19), whose proof is the card's own route (limit of exact sequences on representatives, then the
    three short exact sequences 0 -> Z_n -> C_n -> B_{n-1} -> 0, 0 -> Z_{n+1} -> C_{n+1} -> B_n -> 0
    and 0 -> B_n -> Z_n -> H_n -> 0). Both sets are now cited with page locators.

---

::: {.problem}
Show that a direct limit of exact sequences is exact.
More generally, show that homology commutes with direct limits: If $\{C_\alpha, f_{\alpha\beta}\}$ is a directed system of chain complexes, with the maps $f_{\alpha\beta}: C_\alpha \to C_\beta$ chain maps, then $H_n(\varinjlim C_\alpha) = \varinjlim H_n(C_\alpha)$.
:::

::: {.solution}
For a directed system of abelian groups, recall that
$$
\varinjlim A_\alpha
$$
is the disjoint union of the $A_\alpha$ modulo the relation that $a_\alpha$ and $a_\beta$ are equal when their images agree at some later stage.

Consider a directed system of exact sequences
$$
A_\alpha\xrightarrow{u_\alpha}B_\alpha\xrightarrow{v_\alpha}C_\alpha.
$$
Certainly $\operatorname{im}(\varinjlim u_\alpha)\subseteq\ker(\varinjlim v_\alpha)$. Conversely, let a class $[b_\alpha]$ map to zero in $\varinjlim C_\alpha$. Then for some $\beta\ge\alpha$, the image $b_\beta$ maps to zero in $C_\beta$. Exactness at stage $\beta$ gives $a_\beta\in A_\beta$ with
$$
u_\beta(a_\beta)=b_\beta.
$$
Thus $[b_\alpha]$ lies in the image of $\varinjlim A_\alpha$. Hence filtered direct limits preserve exact sequences.

Now let $C_\alpha$ be a directed system of chain complexes. Since direct limits are exact, they commute with kernels, images, and cokernels occurring in the short exact sequences
$$
0\to Z_n(C_\alpha)\to C_{\alpha,n}\to B_{n-1}(C_\alpha)\to0
$$
and
$$
0\to B_n(C_\alpha)\to Z_n(C_\alpha)\to H_n(C_\alpha)\to0.
$$
Therefore
$$
Z_n(\varinjlim C_\alpha)\cong\varinjlim Z_n(C_\alpha),
\qquad
B_n(\varinjlim C_\alpha)\cong\varinjlim B_n(C_\alpha),
$$
and taking the quotient gives
$$
\boxed{H_n(\varinjlim C_\alpha)\cong\varinjlim H_n(C_\alpha).}
$$

Compare Steven V. Sam, *Solutions to Algebraic Topology* (2008), §3.3 Exercise 17, printed pp.15--16: the same statement, proved there by exhibiting the comparison map between $\varinjlim H_n(C_\alpha)$ and $H_n(\varinjlim C_\alpha)$ and showing it injective and surjective by passing to a later stage. The card's route instead uses exactness of filtered direct limits for the second half, which is the first half of the same exercise. It is also solved in the Math 538 homework solutions, HMW 4, handwritten page 3 (PDF page 19 of `tmp/sources/hatcher-math538-homework4-solutions.pdf`), by exactly the card's route: exactness of the limit on representatives, then $0\to\lim Z_n\to C_n\to C_{n-1}$, $\operatorname{im}\partial_{n+1}=\lim B_n$ and $0\to\lim B_n\to\lim Z_n\to\lim H_n\to0$.
:::
