---
schema: qual/card@1
id: E-76OHA
kind: problem
title: Discrete spaces are paracompact; images need not be
classification:
  areas:
  - topology
  topics:
  - Paracompactness
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    No complete published solution was located for this exercise, so the proof is checked line by line
    against the book and the search is recorded in the COMPLAINTS.md entry for §39--§42 of SRC-TEXT-MUN00.
    Searched: the sets listed in that entry --- Aleksey Zinger's MAT 530 sheets, the *Praying For Stockholm*
    posts, Moller's S38, the Riverside Math 205A solutions, Orellana, Doug's World, Whitman,
    "positron0802", "shenapse", "9beach", "kyp44", the seven further GitHub manuals, dbfin and Gardner's
    ETSU notes --- none of which solves this exercise.
    Checked against Munkres, Topology (2000), Section 41 Exercise 4, printed p. 260, with the discrete topology, the definition of paracompactness, and part (b) of Exercise 41.2 (card E-94C75) for the failure of paracompactness in the image. What was corrected: part (b) deduced the non-paracompactness of $S_\Omega=[0,\omega_1)$ from the general assertion that a paracompact countably compact Hausdorff space is compact, which the book does not prove and the card did not; the card now cites part (b) of Exercise 41.2, where the non-paracompactness of $S_\Omega$ is proved.
- event: solution-reviewed
  by: claude
  date: 2026-11-20
  note: >-
    Issue #169 correctness read, with the #184 citation repair. Part (a) is right: the singleton
    cover refines any open cover, and $\{p\}$ meets only itself in that cover, so it is a locally
    finite open refinement. Part (b) is right: with $Y=S_\Omega$ and $X$ the same set discrete,
    $X$ is paracompact by part (a) and the identity $X\to Y$ is continuous because $X$ is
    discrete, while $Y$ is not paracompact by Exercise 41.2(b). The step now also names the two
    numbered results behind that non-paracompactness, part (a) of Exercise 41.2 and Theorem 41.1.
    Citation by number: §41 Exercise 4, read in `tmp/sources/munkres-2000-topology.md`; the
    2026-11-10 event's page locator is superseded, its text kept as written (QUAL-11).
- event: solution-written
  by: claude
  date: 2026-11-20
  note: >-
    Thirteen steps asserted their claim with no justification and each now carries one: in part (a) the
    discreteness and closedness of singletons, the definition of the cover, the singleton refinement with
    its two properties, local finiteness at a point, and the assembly into paracompactness together with
    Hausdorffness; in part (b) the identification of $S_\Omega$, its non-paracompactness from part (b) of
    Exercise 41.2 through Theorem 41.1, the discrete space on the same underlying set, its paracompactness
    from part (a), and the continuity and surjectivity of the identity map. Checked while writing: the
    local finiteness argument needs the neighbourhood to be the singleton, which only the discrete
    topology supplies, and the map out of a discrete space is continuous for every target topology, which
    is why no property of the order topology on $Y$ is needed for continuity. The two container steps
    carried labels and now state the claim their proofs establish, and the literal "Q.E.D." at the end of
    the last step is gone because the filter supplies that label. Sources are cited by section and
    exercise number, Section 41 Exercise 4 of Munkres, Topology, with part (b) of Exercise 41.2 and
    Theorem 41.1; the page number in the earlier event of this card is superseded by these citations and
    is not to be relied on. QUAL-11 makes a dated event immutable, so it is left standing as the record of
    what that session wrote. The statement is unchanged.
---

::: {.exercise}

(a) Show that if $X$ has the discrete topology, then $X$ is paracompact.

(b) Show that if $f: X \to Y$ is continuous and $X$ is paracompact, the subspace $f(X)$ of $Y$ need not be paracompact.
:::

::: {.solution}

::: pf

::: {.pf-step #discrete-spaces-paracompact}
Every discrete space is Hausdorff and every open cover of it has a locally finite open refinement, so every discrete space is paracompact.

::: pf-proof

::: pf-step
In the discrete topology on $X$, every singleton $\{x\}$ is open and closed, so $X$ is Hausdorff.

::: pf-proof
In the discrete topology every subset is open, so each singleton $\{x\}$ is open, and it is also closed because its complement is the union of the other singletons and so is open. A space in which distinct points have disjoint open neighbourhoods is Hausdorff, and here the singletons themselves separate any two distinct points.
:::

:::

::: pf-step
Let $\mathcal{U} = \{U_\alpha\}_{\alpha \in J}$ be an arbitrary open cover of $X$.

::: pf-proof
An open cover is a family of open sets whose union is the whole space; the cover is indexed by the arbitrary set $J$, and no property of it is assumed beyond that.
:::

:::

::: pf-step
Consider the singleton collection $\mathcal{V} = \{\{x\} \mid x \in X\}$.

::: pf-proof
The collection of singletons is a legitimate family of subsets of $X$, one for each point, and it will be shown to be an open refinement.
:::

:::

::: pf-step
In the discrete topology, each $\{x\}$ is open, and $\bigcup_{x \in X} \{x\} = X$, so $\mathcal{V}$ is an open cover of $X$.

::: pf-proof
Each member of the family is open by the first step, and every point $x$ lies in the member $\{x\}$, so the union of the family is $X$; that is exactly the definition of an open cover.
:::

:::

::: pf-step
For each $x \in X$, since $\mathcal{U}$ covers $X$, there exists an index $\alpha \in J$ such that $x \in U_\alpha$. Thus $\{x\} \subseteq U_\alpha$, so $\mathcal{V}$ refines $\mathcal{U}$.

::: pf-proof
Since $\mathcal{U}$ covers $X$ there is a member containing $x$, and the only subset of that member containing $x$ and contained in $\{x\}$ is $\{x\}$ itself; so $\{x\} \subseteq U_\alpha$, which is what it means for $\mathcal{V}$ to refine $\mathcal{U}$: every member of $\mathcal{V}$ lies inside some member of $\mathcal{U}$.
:::

:::

::: pf-step
For any point $p \in X$, the open neighborhood $W = \{p\}$ intersects only one member of $\mathcal{V}$ (namely $\{p\}$ itself).

::: pf-proof
A family is locally finite when every point has a neighbourhood meeting only finitely many of its members. Here the neighbourhood $\{p\}$ is open, and it meets a member $\{x\}$ of $\mathcal{V}$ only when $x \in \{p\}$, that is only for the single member $\{p\}$.
:::

:::

::: pf-step
Thus $\mathcal{V}$ is a locally finite open refinement of $\mathcal{U}$, proving $X$ is paracompact.

::: pf-proof
The family $\mathcal{V}$ is an open cover of $X$ refining $\mathcal{U}$ and is locally finite, and $X$ is Hausdorff; a Hausdorff space every open cover of which has a locally finite open refinement is paracompact, so $X$ is paracompact. The empty cover of the empty space causes no exception, the condition being vacuous there.
:::

:::

:::

:::

::: pf-step
There is a paracompact space $X$ and a continuous map $f$ whose image $f(X)$ is not paracompact.

::: pf-proof

::: pf-step
Let $Y = S_\Omega = [0, \Omega)$ be the space of countable ordinals with the order topology.

::: pf-proof
$S_\Omega$ is the set of countable ordinals with the order topology, which is the space the exercise's part (b) needs as a non-paracompact space.
:::

:::

::: pf-step
$Y$ is not paracompact: this is part (b) of Exercise 41.2, proved on the card of [[E-94C75]], where $S_\Omega$ is shown not to be paracompact by exhibiting $S_\Omega \times \overline{S}_\Omega$ as a non-normal product of a paracompact space with a compact one. A paracompact $S_\Omega$ would make that product paracompact by part (a) of the exercise and normal by Theorem 41.1, contradicting its non-normality.

::: pf-proof
Part (b) of Exercise 41.2 establishes that $S_\Omega$ is not paracompact, and the argument on [[E-94C75]] records it: the product $S_\Omega \times \overline{S}_\Omega$ of a paracompact factor with a compact one is not normal, whereas Theorem 41.1 makes such a product normal whenever the paracompact factor is paracompact. The contradiction shows $S_\Omega$ is not paracompact, and the citation is to that part rather than to compactness, which the book does not prove of $S_\Omega$.
:::

:::

::: pf-step
Let $X = Y_d$ denote the set $[0, \omega_1)$ equipped with the discrete topology.

::: pf-proof
The same underlying set as $Y$, equipped with the discrete topology, is a topological space: the discrete topology is the family of all subsets, which contains the empty set and the whole set and is closed under unions and finite intersections.
:::

:::

::: pf-step
By step [](#discrete-spaces-paracompact){.pf-ref}, $X$ is paracompact.

::: pf-proof
Step [](#discrete-spaces-paracompact){.pf-ref} proves that every discrete space is paracompact, and $X$ carries the discrete topology by construction, so $X$ is paracompact.
:::

:::

::: pf-step
The identity map $f: X \to Y$ defined by $f(x) = x$ is continuous because the domain $X$ is discrete, and $f(X) = Y$ is surjective.

::: pf-proof
A map out of a discrete space is continuous for every topology on the target, because the preimage of any set is a subset of the discrete space and hence open. The identity map on the underlying set is surjective, so its image is all of $Y$.
:::

:::

::: pf-step
Thus $f(X) = Y$ is a continuous image of the paracompact space $X$ that fails to be paracompact.

::: pf-proof
Steps [](#discrete-spaces-paracompact){.pf-ref} and the two above give a paracompact $X$, a continuous surjection $f$ onto $Y$, and a $Y$ that is not paracompact; so $f(X) = Y$ is a continuous image of a paracompact space which is not paracompact.
:::

:::

:::

:::

:::

:::
