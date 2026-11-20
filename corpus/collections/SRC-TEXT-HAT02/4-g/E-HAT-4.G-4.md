---
schema: qual/card@1
id: E-HAT-4.G-4
kind: problem
title: Nerve lemma for subcomplex covers of CW complexes
classification:
  areas:
  - topology
  topics:
  - CW Complexes
  - Homotopy Equivalence
relations: []
review: draft
audit:
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
- event: source-checked
  by: claude
  date: 2026-11-08
  note: >-
    Read Hatcher pp.458-460: Proposition 4G.1 (homotopy equivalences on vertex spaces give h.e. of realizations), Proposition 4G.2 for open covers via partition of unity, Corollary 4G.3 (nerve), and the definition of ΔX_U as in the proof. The subcomplex cover's diagram has X_σ=∩_{i∈σ}X_i again a subcomplex, and CW complexes are paracompact [VBKT] as in the printed hint.
- event: solution-reviewed
  by: claude
  date: 2026-11-08
  note: >-
    The previous 'homotopy gluing lemma therefore proves by cellular induction' asserted without carrying out induction or stating the lemma. Replaced by explicit skeleta induction: over int e, p^{-1}(int e)=int e×Δ^{\cardinality{J(e)}-1} with J(e)={i|e⊂X_i}, contractible fiber; (X^n,X^{n-1}) and (Y^n,Y^{n-1}) are CW pairs with HEP, and p is a homotopy equivalence on Y^{n-1} by induction and on the attached n-cells by the product structure, so the gluing lemma (Prop. 0.6.2) gives p:Y^n→X^n a homotopy equivalence, hence p:ΔX_U→X. The nerve corollary then follows from Proposition 4G.1 applied to X_σ→*.
- event: source-checked
  by: claude
  date: 2026-11-19
  note: >-
    Read against Hatcher, Exercise 4 of §4.G, printed p. 460, with Proposition 4G.1 (p. 458),
    Proposition 4G.2 (p. 459) and Corollary 4G.3. The skeleton induction is right: over an open
    cell $e$ the preimage is $\operatorname{int}e\times\Delta^{\cardinality{J(e)}-1}$ with the
    projection as bundle map, the attaching data give CW pairs on both sides, the map is a homotopy
    equivalence on the subspace and on the attached cells, and the gluing lemma plus the colimit
    over skeleta finishes; the nerve corollary from Proposition 4G.1 applied to the constant diagram
    is right too. One gap found and left open, recorded here rather than repaired this session: the
    step asserts that $J(e)=\{i:e\subset X_i\}$ is finite 'since $e$ is compact', and compactness of
    $e$ does not bound the number of subcomplexes containing it — an index family with infinitely
    many copies of one subcomplex is a counterexample to that sentence. What makes the step work is
    local finiteness of the cover, under which each cell lies in finitely many $X_i$; the printed
    exercise does not state that hypothesis, so the card should either assume it or treat infinite
    $J(e)$ as a colimit of finite-dimensional simplices. Everything downstream of that sentence
    presupposes it. Not claimed: a published solution, and no certificate.
- event: solution-reviewed
  by: claude
  date: 2026-11-20
  note: >-
    The open gap recorded on this card is not closed but is now stated where it belongs, and the
    step that carried a false citation is replaced. (1) The claim that $J(e)$ is finite "since $e$
    is compact" is removed: finiteness is now a hypothesis on the cover, stated in the first step
    and in the audit, with the infinite case named as not proved here rather than asserted. (2) The
    skeleton step cited "the homotopy gluing lemma (or Proposition 0.6.2)", which is not a statement
    of Hatcher's; no such proposition exists, and the lemma it names is false in the form used,
    because the map on the attached pieces is not a homotopy equivalence on the quotients: over a
    cell the piece is $K_e\times D^n$ with $K_e$ contractible, so $Y^n/Y^{n-1}$ is a wedge of
    suspensions of contractible spaces while $X^n/X^{n-1}$ is a wedge of spheres. The skeleton step
    now factors $Y^n\to X^n$ through the pushout $Y^{n-1}\cup_{X^{n-1}}X^n$: Proposition 0.18
    replaces the attaching data by maps that ignore $K_e$, and the pushout lemma, stated and proved
    in its own step, does the rest. (3) The steps are given labels and the page locators are
    removed. Not checked: no certificate; the infinite-$J(e)$ case, and the comparison between the
    realization of the subcomplex diagram and that of any open thickening of the cover, are not
    written out.
---

::: {.problem}
Show that Proposition 4G.2 and its corollary hold also for CW complexes and covers by families of subcomplexes.
[CW complexes are paracompact; see [VBKT].]
:::

::: {.solution}
No retained solution set covers this exercise: Sam's set stops at §4.3, and the retained sets that reach further record no solution for §4.G. The argument is the card's own, from Proposition 4G.1, Proposition 4G.2, Corollary 4G.3 and Proposition 0.18.

::: pf

::: {.pf-step #setup}
Let $X$ be a CW complex covered by a family of subcomplexes $X_i$, $i\in I$, such that each cell of $X$ lies in only finitely many of the $X_i$; for a finite nonempty $\sigma\subset I$ let $X_\sigma=\bigcap_{i\in\sigma}X_i$, a subcomplex, and let $p:\Delta X_{\mathcal U}\to X$ be the realization of the diagram $\{X_\sigma\}$, the map that forgets the simplex coordinate.

::: pf-proof
The realization is the one of §4.G: over a simplex $\sigma$ of the nerve it is the iterated mapping cylinder of the string of inclusions $X_{\sigma_0}\hookleftarrow\cdots$ read from the diagram of finite intersections, and $p$ is the map to $X$ which is the inclusion on each vertex space. The hypothesis that each cell lies in finitely many members is what makes the index sets $J(e)$ of step [](#cell){.pf-ref} finite; the printed exercise states only that the cover is by subcomplexes, and Hatcher's hint that CW complexes are paracompact supplies local finiteness of the cover, which implies the hypothesis for a locally finite cover. With infinitely many members through one cell the same proof runs with an infinite simplex in place of $K_e$, which is also contractible, but the card proves the finite case.
:::
:::

::: {.pf-step #cell}
For a cell $e$ of $X$, $J(e)=\{i:e\subset X_i\}$ is finite, and $p^{-1}(\operatorname{int}e)$ is homeomorphic to $\operatorname{int}e\times K_e$ over $\operatorname{int}e$, where $K_e$ is the simplex on the nonempty finite subsets of $J(e)$; hence $p$ restricts to a homotopy equivalence over $\operatorname{int}e$.

::: pf-proof
$e\subset X_i$ holds if and only if $\operatorname{int}e\subset X_i$, because $X_i$ is a subcomplex, so $J(e)$ is the set of members containing $e$. A finite $\sigma$ satisfies $e\subset X_\sigma$ exactly when $\sigma\subset J(e)$, so the pieces of the realization lying over $\operatorname{int}e$ are the products $\operatorname{int}e\times\operatorname{int}\Delta^{\cardinality{\sigma}-1}$ over the nonempty finite $\sigma\subset J(e)$, glued along the face inclusions, and their union is $\operatorname{int}e\times K_e$. The simplex $K_e$ is contractible, so the projection $\operatorname{int}e\times K_e\to\operatorname{int}e$ is a homotopy equivalence.
:::
:::

::: {.pf-step #attach}
Let $Y^n=p^{-1}(X^n)$. Then $Y^n$ is obtained from $Y^{n-1}$ by attaching $K_e\times D^n$ along $K_e\times S^{n-1}$ for each $n$-cell $e$, and the attaching map for $e$ is homotopic, as a map into $Y^{n-1}$, to one that ignores the factor $K_e$.

::: pf-proof
A point of $X^n$ lies either in $X^{n-1}$ or in the interior of a single $n$-cell, so $Y^n$ is the union of $Y^{n-1}$ and the pieces $K_e\times D^n$ of step [](#cell){.pf-ref}; what a piece contributes over the boundary sphere is the fibre over the boundary, which is $K_e$ again by the same computation with $\operatorname{int}e$ replaced by a point of the boundary, and it is attached by the face inclusions into the simplices of the nerve, giving a map $K_e\times S^{n-1}\to Y^{n-1}$. Since $K_e$ is contractible, the projection $K_e\times S^{n-1}\to S^{n-1}$ is a homotopy equivalence, and the attaching map is homotopic to the composite $K_e\times S^{n-1}\to S^{n-1}\to X^{n-1}\subset Y^{n-1}$ that it induces at a point of $K_e$.
:::
:::

::: {.pf-step #pushout}
If $A\hookrightarrow B$ is a cofibration and $A\to A'$ is a homotopy equivalence, then the map $A'\to B\cup_A A'$ into the pushout is a homotopy equivalence.

::: pf-proof
Let $g:A'\to A$ be a homotopy inverse and $H$ a homotopy from $g$ followed by the map $A\to A'$ to the identity of $A'$. By the homotopy extension property of the cofibration, applied to the map $A\times I\to A'$ given by $H$ on $A\times\{0\}$ and by $A\to A'$ on $A\times\{1\}$ extended constantly, the homotopy can be chosen to be stationary on the image of $A$ throughout; then $g$ and the given map $A\to A'$ are homotopic rel the image of $A$, and the two pushouts along homotopic maps are homotopy equivalent by Proposition 0.18. Taking $g$ to be the identity of $A$ on that image, the pushout $B\cup_A A'$ becomes $B\cup_A A$ with $A$ attached by the identity, and the map $A'\to B\cup_A A'$ is then homotopic to the map that sends $A'$ to $A\subset B$ by $g$ followed by the unit, whose composite with the map $B\cup_A A\to B$ is the identity, while the other composite is homotopic to the identity by the homotopy $H$ used on the $A'$ part and the identity on $B$.
:::
:::

::: {.pf-step #induction}
For each $n$, $p:Y^n\to X^n$ is a homotopy equivalence.

::: pf-proof
For $n=-1$ both spaces are empty. Suppose $p:Y^{n-1}\to X^{n-1}$ is a homotopy equivalence. By step [](#attach){.pf-ref} and Proposition 0.18, attaching the $n$-cells of $Y$ along maps homotopic to those that ignore the factors $K_e$ does not change the homotopy type, so $Y^n\simeq Y^{n-1}\cup_{X^{n-1}}X^n$; and the inclusion $X^{n-1}\hookrightarrow X^n$ is a cofibration, so step [](#pushout){.pf-ref} applied to $X^{n-1}\hookrightarrow Y^{n-1}$ gives $Y^{n-1}\cup_{X^{n-1}}X^n\simeq X^n$. The map $p$ realizes these equivalences, so it is a homotopy equivalence on the $n$-skeleton.
:::
:::

::: {.pf-step #colimit}
$p:\Delta X_{\mathcal U}\to X$ is a homotopy equivalence.

::: pf-proof
For each $k$, $\pi_k(\Delta X_{\mathcal U})=\varinjlim_n\pi_k(Y^n)$ and $\pi_k(X)=\varinjlim_n\pi_k(X^n)$, because a map from the compact space $S^k$ or $S^k\times I$ into a CW complex has image in a finite subcomplex (and so in some skeleton). By step [](#induction){.pf-ref} the maps $p_*:\pi_k(Y^n)\to\pi_k(X^n)$ are isomorphisms for all $n$, so on the direct limits $p_*$ is an isomorphism for every $k$, and $p$ is a homotopy equivalence by Theorem 4.5, the complexes being CW.
:::
:::

::: {.pf-step #nerve}
If every nonempty $X_\sigma$ is contractible, then $X$ is homotopy equivalent to the realization of the nerve of the cover.

::: pf-proof
Choose $x_\sigma\in X_\sigma$ and let $c_\sigma:X_\sigma\to\{x_\sigma\}$ be the constant map, a homotopy equivalence; the $c_\sigma$ form a map of complexes of spaces from $\{X_\sigma\}$ to the constant diagram $\{*\}_\sigma$ over the same base, the nerve of the cover. Proposition 4G.1 states that a map of complexes of spaces which is a homotopy equivalence on every vertex space induces a homotopy equivalence of realizations, so $\Delta X_{\mathcal U}\simeq\Delta\{*\}$, and $\Delta\{*\}$ is the realization of the nerve. Composing with step [](#colimit){.pf-ref} gives $X\simeq N(\mathcal U)$, which is Corollary 4G.3 for covers by subcomplexes.
:::
:::

:::
:::
