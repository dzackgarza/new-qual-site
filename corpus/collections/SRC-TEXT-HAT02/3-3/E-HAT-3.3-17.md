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
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Restructured as a Lamport proof of the argument already on the card, which is correct and
    follows the Math 538 homework solution the card cites (HMW 4, handwritten page 3): exactness
    of the filtered colimit on representatives, then commutation with kernels and images, then
    the short exact sequence 0 -> B_n -> Z_n -> H_n -> 0. Added: the representative criterion
    for a class to vanish (which the card used implicitly when it said 'for some beta >= alpha
    the image b_beta maps to zero'), the functoriality remark that the vanishing persists, and
    the separate derivations of the two identities Z_n(lim) = lim Z_n and B_n(lim) = lim B_n
    from exactness rather than from a single appeal to 'direct limits are exact'. The card's
    comparison with Steven V. Sam (2008), pp. 15-16 — who proves the same statement by
    exhibiting the comparison map and checking it injective and surjective — is kept in the
    preamble.

---

::: {.problem}
Show that a direct limit of exact sequences is exact.
More generally, show that homology commutes with direct limits: If $\{C_\alpha, f_{\alpha\beta}\}$ is a directed system of chain complexes, with the maps $f_{\alpha\beta}: C_\alpha \to C_\beta$ chain maps, then $H_n(\varinjlim C_\alpha) = \varinjlim H_n(C_\alpha)$.
:::

::: {.solution}
Throughout $\theset{A_{\alpha}, f_{\alpha\beta}}$ is a directed system of abelian groups over a directed set $\Lambda$, and $\varinjlim A_{\alpha}$ is the filtered colimit: the disjoint union of the $A_{\alpha}$ modulo the relation that $a_{\alpha} \in A_{\alpha}$ and $a_{\beta} \in A_{\beta}$ are equal when $f_{\alpha\gamma}(a_{\alpha}) = f_{\beta\gamma}(a_{\beta})$ for some $\gamma \ge \alpha, \beta$. The argument is the card's, and matches the two published treatments it cites: Steven V. Sam, *Solutions to Algebraic Topology* (2008), §3.3 Exercise 17, and the Math 538 homework solutions, HMW 4, handwritten page 3.

::: pf

::: {.pf-step #representatives}
A class $[a_{\alpha}]$ of $\varinjlim A_{\alpha}$ vanishes exactly when $f_{\alpha\beta}(a_{\alpha}) = 0$ for some $\beta \ge \alpha$.

::: pf-proof
By the description of the colimit, $[a_{\alpha}] = 0 = [0_{\gamma}]$ exactly when $f_{\alpha\gamma}(a_{\alpha}) = f_{\gamma\gamma}(0) = 0$ for some $\gamma \ge \alpha$; that is the stated condition with $\beta = \gamma$, and any $\beta \ge \gamma$ has $f_{\alpha\beta}(a_{\alpha}) = 0$ as well by functoriality.

:::

:::

::: {.pf-step #exact}
A filtered colimit of exact sequences $A_{\alpha} \xrightarrow{u_{\alpha}} B_{\alpha} \xrightarrow{v_{\alpha}} C_{\alpha}$ is exact at $\varinjlim B_{\alpha}$.

::: pf-proof
Write $u \coloneqq \varinjlim u_{\alpha}$ and $v \coloneqq \varinjlim v_{\alpha}$. Since $v u = \varinjlim (v_{\alpha}u_{\alpha}) = 0$, one has $\operatorname{im}u \subseteq \ker v$. Conversely let $[b_{\alpha}] \in \ker v$. By step [](#representatives){.pf-ref} applied to the class $v([b_{\alpha}]) = [v_{\alpha}(b_{\alpha})]$, there is $\beta \ge \alpha$ with $v_{\beta}\bigl(f_{\alpha\beta}(b_{\alpha})\bigr) = 0$, that is $f_{\alpha\beta}(b_{\alpha}) \in \ker v_{\beta}$. Exactness at stage $\beta$ gives $a_{\beta} \in A_{\beta}$ with $u_{\beta}(a_{\beta}) = f_{\alpha\beta}(b_{\alpha})$, hence $[b_{\alpha}] = [f_{\alpha\beta}(b_{\alpha})] = [u_{\beta}(a_{\beta})] = u([a_{\beta}])$ lies in $\operatorname{im}u$.

:::

:::

::: {.pf-step #kernel-image}
For a directed system of chain maps the colimit is a chain complex and $\ker$ and $\operatorname{im}$ are computed termwise after the limit: $Z_{n}(\varinjlim C_{\alpha}) = \varinjlim Z_{n}(C_{\alpha})$ and $B_{n}(\varinjlim C_{\alpha}) = \varinjlim B_{n}(C_{\alpha})$.

::: pf-proof
The colimit of the chain maps is a chain complex $\partial \coloneqq \varinjlim \partial^{\alpha}$. For each $\alpha$ the sequence $0 \to Z_{n}(C_{\alpha}) \to C_{\alpha,n} \xrightarrow{\partial^{\alpha}_{n}} C_{\alpha,n-1}$ is exact at the two left terms, so by step [](#exact){.pf-ref} the sequence $0 \to \varinjlim Z_{n}(C_{\alpha}) \to \varinjlim C_{\alpha,n} \xrightarrow{\partial_{n}} \varinjlim C_{\alpha,n-1}$ is exact; hence $\ker\partial_{n} = \varinjlim Z_{n}$, which is the first identity. For the second, $B_{n}$ is the image of $\partial_{n+1}$ and the colimit of the surjections $C_{\alpha,n+1} \to B_{n}(C_{\alpha})$ is the surjection $\varinjlim C_{\alpha,n+1} \to \varinjlim B_{n}(C_{\alpha})$ with the same image as $\partial_{n+1}$, namely $B_{n}(\varinjlim C_{\alpha})$; this is where exactness of the filtered colimit is used again, and it is the step the card performs by quoting the short exact sequences $0 \to Z_{n} \to C_{n} \to B_{n-1} \to 0$ and $0 \to B_{n} \to Z_{n} \to H_{n} \to 0$.

:::

:::

::: pf-step
$H_{n}(\varinjlim C_{\alpha}) \cong \varinjlim H_{n}(C_{\alpha})$.

::: pf-proof
For each $\alpha$ the sequence $0 \to B_{n}(C_{\alpha}) \to Z_{n}(C_{\alpha}) \to H_{n}(C_{\alpha}) \to 0$ is exact, so by step [](#exact){.pf-ref} its colimit $0 \to \varinjlim B_{n} \to \varinjlim Z_{n} \to \varinjlim H_{n} \to 0$ is exact. By step [](#kernel-image){.pf-ref} the first two terms are $B_{n}(\varinjlim C_{\alpha})$ and $Z_{n}(\varinjlim C_{\alpha})$, so the exact sequence identifies $\varinjlim H_{n}$ with the quotient $Z_{n}/B_{n}$ of the colimit complex, which is $H_{n}(\varinjlim C_{\alpha})$.

:::

:::

:::
:::
