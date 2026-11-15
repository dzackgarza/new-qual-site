---
schema: qual/card@1
id: E-GYVM8
kind: problem
title: Compactness characterized by subnets
classification:
  areas:
  - topology
  topics:
  - Nets
  - Compactness
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    No published set for this exercise was located. The sources searched, the pages they
    cover and the conclusion are recorded in COMPLAINTS.md under the entry for the net
    exercises of §29; the card's own proof is kept. The statement was read against Munkres,
    Topology (2000), §29 supplementary exercises on nets, printed pp. 187-188.
- event: solution-written
  by: claude
  date: 2026-11-15
  note: >-
    Transcribed from dbFin, "Supplementary Exercises*: Nets: Problem 10 Solution",
    https://dbfin.com/topology/munkres/chapter-3/supplementary-exercises-nets/problem-10-solution/,
    read 2026-11-15, text at tmp/sources/dbfin/supplementary-exercises-nets/problem-10.md, which
    follows the printed hint: the sets B_alpha = {x_beta : alpha <= beta} have the finite
    intersection property after taking closures, compactness gives a point of the intersection, and
    that point is an accumulation point; conversely the finite subsets of a family with the finite
    intersection property index a net whose accumulation point lies in every member. Three things
    are corrected, none of them mathematical: dbFin writes "let x be the intersection of the
    closures", where compactness gives only that the intersection is nonempty and one chooses a
    point of it; it writes "beta subset {k}" where the inclusion it uses is {k} subset beta; and its
    second direction ends at an accumulation point without saying that the lemma of Exercise 9
    turns one into a convergent subnet, which is how the card passes between the two forms. This
    supersedes the 2026-11-10 note above.
- event: source-corrected
  by: claude
  date: 2026-11-15
  note: >-
    The second direction now orders its index set by inclusion, where the transcription had reverse
    inclusion. The correction is mathematical, and it is dbFin's: under reverse inclusion two
    disjoint singletons of members of a family with the finite intersection property have no upper
    bound among the nonempty finite subsets, so the set so ordered is not directed, and the step
    that follows the construction takes a set containing {A}, which is the inclusion order. The
    inclusion order is what the argument uses and it is directed, the union of two nonempty finite
    subsets being one. Munkres' printed hint takes the other route, the collection of all finite
    intersections of members of the family ordered by reverse inclusion, which is directed by part
    (c) of the first exercise; that route is available and is not the one on the card. The
    2026-11-15 note above said that the three corrections it made to dbFin were "none of them
    mathematical"; that claim was wrong for this one and is corrected here.
---

::: {.exercise}

Theorem.
$X$ is compact if and only if every net in $X$ has a convergent subnet.

[Hint: To prove the implication $\Rightarrow$, let $B_\alpha = \theset{x_\beta \mid \alpha \preceq \beta}$ and show that $\theset{B_\alpha}$ has the finite intersection property. To prove $\Leftarrow$, let $\mathcal{A}$ be a collection of closed sets having the finite intersection property, and let $\mathcal{B}$ be the collection of all finite intersections of elements of $\mathcal{A}$, partially ordered by reverse inclusion.]
:::

::: {.solution}

::: pf

::: pf-step
If $X$ is compact, then every net in $X$ has an accumulation point.

::: pf-proof
Let $(x_\alpha)_{\alpha \in J}$ be a net. For $\alpha \in J$ put $B_\alpha = \theset{x_\beta \mid \alpha \preceq \beta}$, and let $F_\alpha = \overline{B_\alpha}$. The family $\theset{F_\alpha}$ has the finite intersection property: for $\alpha_1, \dots, \alpha_n \in J$ there is $\gamma \in J$ with $\alpha_i \preceq \gamma$ for each $i$, and then $x_\gamma \in B_{\alpha_1} \cap \dots \cap B_{\alpha_n} \subset F_{\alpha_1} \cap \dots \cap F_{\alpha_n}$. The sets $F_\alpha$ are closed and $X$ is compact, so $\bigcap_\alpha F_\alpha \ne \varnothing$; choose $x$ in it. Let $U$ be a neighborhood of $x$ and $\alpha \in J$. Since $x \in \overline{B_\alpha}$, the set $U$ meets $B_\alpha$, so there is $\beta \succeq \alpha$ with $x_\beta \in U$. Thus $x$ is an accumulation point of the net.
:::

:::

::: pf-step
If every net in $X$ has an accumulation point, then $X$ is compact.

::: pf-proof
Let $\mathcal{A}$ be a collection of closed subsets of $X$ with the finite intersection property; it suffices to show $\bigcap \mathcal{A} \ne \varnothing$. Let $K$ be the set of nonempty finite subsets of $\mathcal{A}$, ordered by inclusion, a directed set because the union of two finite subsets is a finite subset containing both. For $\alpha \in K$ the set $\bigcap_{A \in \alpha} A$ is a finite intersection of members of $\mathcal{A}$, hence nonempty; choose $x_\alpha$ in it. By hypothesis the net $(x_\alpha)$ has an accumulation point $x$. Let $A \in \mathcal{A}$ and let $U$ be a neighborhood of $x$. Since $x$ is an accumulation point and $\{A\} \in K$, there is $\alpha \in K$ with $\{A\} \subset \alpha$ and $x_\alpha \in U$. Then $x_\alpha \in \bigcap_{B \in \alpha} B \subset A$, so $U \cap A \ne \varnothing$. Thus $x$ lies in the closure of $A$, which is $A$; as $A$ was arbitrary, $x \in \bigcap \mathcal{A}$.
:::

:::

::: pf-step
$X$ is compact if and only if every net in $X$ has a convergent subnet. $\square$

::: pf-proof
If $X$ is compact, step 1 produces an accumulation point of any net and the lemma of the preceding exercise produces a subnet converging to it. Conversely if every net has an accumulation point, step 2 gives compactness, and every net then has a convergent subnet by the same lemma. So both conditions are equivalent to every net having an accumulation point.
:::

:::

:::

:::
