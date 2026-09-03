---
schema: qual/card@1
id: E-1CMTE
kind: problem
title: Paracompactness and topological completeness in the basics review
classification:
  areas:
  - topology
  topics:
  - Topological Spaces
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
---

::: {.exercise}

After studying Chapters 6 and 7, repeat Exercises 1–6 of the Supplementary Exercises (Review of the Basics) for the following properties:

(18) paracompact

(19) topologically complete

You should be able to answer all but one of the 340 questions involved in Exercises 1–6, and all but one of the 40 questions involved in Exercise 7. These two are unsolved; see the remark in Exercise 5 of §32.
:::

::: solution
**Goal:** Systematically establish the core topological behaviors (separation axioms, subspace inheritance, product preservation, and image properties) for (18) Paracompactness and (19) Topological Completeness (complete metrizability).

<1>1. Property (18): Paracompactness.
    *Definition:* A space $X$ is paracompact if it is Hausdorff and every open cover has an open locally finite refinement.
    *Key Theorems:*
    <2>1. Separation: Every paracompact Hausdorff space is regular and normal ($T_4$).
        *Proof:* If $\mathcal{A}$ is an open cover and $B \subseteq X$ is closed with $x \notin B$, local finiteness allows shrinking open coverings to disjoint open neighborhoods separating $x$ and $B$, and similarly separating disjoint closed sets $A$ and $B$ (Munkres Theorem 41.1).
    <2>2. Subspaces:
        - Closed subspaces of a paracompact space are paracompact: If $Y \subseteq X$ is closed and $\mathcal{U}$ is an open cover of $Y$, extend $\mathcal{U}$ to an open cover of $X$ by adjoining $X \setminus Y$. The restriction of its locally finite open refinement to $Y$ is locally finite.
        - Arbitrary subspaces of paracompact spaces need not be paracompact: The ordinal space $[0, \Omega]$ is compact (hence paracompact), but the open subspace $S_\Omega = [0, \Omega)$ is not paracompact (it is not Lindelöf, and not paracompact).
    <2>3. Products:
        - Finite products of paracompact spaces need not be paracompact: The Sorgenfrey line $\mathbb{R}_l$ is paracompact (and Lindelöf), but the Sorgenfrey plane $\mathbb{R}_l \times \mathbb{R}_l$ is not normal, hence not paracompact.
        - If $X$ is paracompact and $Y$ is compact, then $X \times Y$ is paracompact.
    <2>4. Metrizability & Compactness:
        - Every compact Hausdorff space is paracompact: a finite subcover is locally finite because each point meets at most finitely many members of the cover (indeed, at most all of them, and the cover is finite).
        - Every metrizable space is paracompact (Stone's Theorem, Munkres Theorem 41.4).

<1>2. Property (19): Topological Completeness (Complete Metrizability).
    *Definition:* A space $X$ is topologically complete if there exists a complete metric on $X$ that induces the topology of $X$.
    *Key Theorems:*
    <2>1. Baire Category Theorem: Every topologically complete space is a Baire space.
        *Proof:* In a complete metric space, every countable intersection of dense open sets is dense (Munkres Theorem 48.2).
    <2>2. Subspaces (Alexandrov's Theorem):
        - A subspace $Y$ of a completely metrizable space $X$ is topologically complete if and only if $Y$ is a $G_\delta$ set in $X$ (Munkres Theorem 43.7).
        - In particular, every closed subspace and every open subspace of a completely metrizable space is topologically complete.
        - Non-$G_\delta$ subspaces, such as $\mathbb{Q} \subset \mathbb{R}$, are not topologically complete.
    <2>3. Products:
        - A countable product $X = \prod_{n=1}^\infty X_n$ of topologically complete spaces is topologically complete under the metric $D(\mathbf{x}, \mathbf{y}) = \sum_{n=1}^\infty \frac{1}{2^n} \bar{d}_n(x_n, y_n)$ (Munkres Theorem 43.5).
        - Uncountable products of non-trivial metric spaces fail to be first-countable, hence are not metrizable.
    <2>4. Locally Compact Spaces:
        - Every locally compact Hausdorff space that is second-countable (or metrizable) is topologically complete (Munkres Theorem 43.6). Q.E.D.
:::
