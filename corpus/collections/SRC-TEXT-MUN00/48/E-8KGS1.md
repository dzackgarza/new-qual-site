---
schema: qual/card@1
id: E-8KGS1
kind: problem
title: Local Baireness implies Baireness
classification:
  areas:
  - topology
  topics:
  - Baire Spaces
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
- event: solution-written
  by: claude
  date: 2026-11-11
  note: >-
    Transcribed from the located published solution: "Solutions to exercises for Mathematics 205A" (University
    of California, Riverside, Fall 2014), Part 3, section "III.3: Implications of completeness", answer to
    Munkres §48 Exercise 4 (printed p. 299) on the set's own printed p. 6 (in tmp/sources/munkres-solutions-ucr-math205-gentop.pdf,
    PDF p. 47). Checked against Munkres, Topology (2000), §48 Exercise 4, printed p. 299, with Lemma 48.1 (the
    open-set formulation) and Lemma 48.4 (an open subspace of a Baire space is a Baire space). What was
    corrected: the card's first step had said that a point with a Baire neighbourhood N has "an open
    neighbourhood U_x contained in N" and then treated U_x as an open subspace of N and of X at once; it now
    takes an open set O of X with x in O contained in N, notes that O is open in N and hence Baire by Lemma
    48.4, and so obtains an open cover of X by Baire subspaces, which is what the argument uses. The rest is the
    set's: inside a cover member U, the traces of the closed nowhere dense sets of X are closed nowhere dense in
    U, and the Baire property of U produces a point of W cap U outside all of them. The card's closing
    references to two step labels that no step carried are replaced by the prose sentence that closes the
    argument.
- event: source-corrected
  by: claude
  date: 2026-11-19
  note: >-
    Rewrote the solution's frame on 2026-11-19, leaving every argument as it was.
    The three steps opened with run-in titles and "Proof:" lines instead of
    claims, the page cited no source, and the solution ended with a paragraph
    outside the proof repeating the conclusion. The steps are now labelled s1 to
    s3 with claims as their first paragraphs, the stray paragraph is gone, and the
    preamble names the published solution transcribed (the University of
    California, Riverside, Mathematics 205A set, Part 3, answer to §48 Exercise
    4, printed p. 6 of that set) and the pages checked in the book: the exercise
    on printed p. 299, Lemma 48.1 on printed p. 296 and Lemma 48.4 on printed
    p. 297. No statement, argument or citation changes.

---

::: {.exercise}

Show that if every point $x$ of $X$ has a neighborhood that is a Baire space, then $X$ is a Baire space.
[Hint: Use the open set formulation of the Baire condition.]
:::

::: {.solution}
The proof is the one in "Solutions to exercises for Mathematics 205A" (University of California, Riverside, Fall 2014), Part 3, answer to Munkres §48 Exercise 4, printed p. 6 of that set. The exercise is Munkres, *Topology* (2000), Section 48, Exercise 4; the open-set formulation of the Baire condition is Lemma 48.1, and the fact that an open subspace of a Baire space is Baire is Lemma 48.4.

::: pf

::: {.pf-step #s1}
Every point of $X$ has an open neighbourhood that is a Baire space in the subspace topology, so $X$ has an open cover by Baire subspaces.

::: pf-proof

::: pf-step

If a point $x \in X$ has a neighborhood $N$ that is a Baire space, there is an open set $O$ of $X$ with $x\in O\subseteq N$; then $O=O\cap N$ is open in the subspace $N$, so $O$ is an open subspace of the Baire space $N$ and is itself Baire.

:::

::: pf-step

So each point of $X$ has an open neighbourhood (in $X$) that is a Baire space in the subspace topology, by Lemma 48.4 (an open subspace of a Baire space is a Baire space).

:::

::: pf-step

Thus $X$ possesses an open covering $\mathcal{U} = \{U_\alpha\}_{\alpha \in J}$ such that each $U_\alpha$ is open in $X$ and is a Baire space in the subspace topology.

:::

:::

:::

::: {.pf-step #s2}
A space $Y$ is Baire exactly when, for every countable family of closed sets with empty interior and every non-empty open $W\subseteq Y$, the difference $W\setminus\bigcup_n A_n$ is non-empty.

::: pf-proof

::: pf-step

A topological space $X$ is a Baire space if and only if for every countable collection $\{A_n\}_{n=1}^\infty$ of closed subsets of $X$ each having empty interior ($\operatorname{Int}_X(A_n) = \varnothing$), and every non-empty open set $W \subseteq X$, the difference $W \setminus \bigcup_{n=1}^\infty A_n$ is non-empty.

:::

:::

:::

::: {.pf-step #s3}
$X$ is a Baire space.

::: pf-proof

::: pf-step

Let $\{A_n\}_{n=1}^\infty$ be a sequence of closed subsets of $X$ with $\operatorname{Int}_X(A_n) = \varnothing$ for all $n$, and let $W \subseteq X$ be an arbitrary non-empty open set.

:::

::: pf-step

Pick a point $x_0 \in W$.

:::

::: pf-step

Since $\mathcal{U}$ covers $X$, choose an open Baire set $U \in \mathcal{U}$ containing $x_0$.

:::

::: pf-step

The intersection $V = W \cap U$ is a non-empty open subset of $U$.

:::

::: pf-step

For each $n$, the set $F_n = A_n \cap U$ is closed in $U$.

:::

::: pf-step

Because $U$ is open in $X$, the interior in $U$ satisfies:
        $$\operatorname{Int}_U(F_n) = \operatorname{Int}_X(A_n) \cap U = \varnothing \cap U = \varnothing.$$

:::

::: pf-step

Since $U$ is a Baire space and $V$ is a non-empty open set in $U$, $V \not\subseteq \bigcup_{n=1}^\infty F_n$.

:::

::: pf-step

Thus there exists a point $y \in V$ such that $y \notin \bigcup_{n=1}^\infty F_n$.

:::

::: pf-step

Because $y \in V \subseteq U$, $y \notin F_n \implies y \notin A_n$ for all $n \ge 1$.

:::

::: pf-step

Since $y \in V \subseteq W$, we have $y \in W \setminus \bigcup_{n=1}^\infty A_n$.

:::

:::

:::

:::

:::
