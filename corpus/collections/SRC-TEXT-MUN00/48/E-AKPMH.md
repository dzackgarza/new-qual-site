---
schema: qual/card@1
id: E-AKPMH
kind: problem
title: The irrationals are a Baire space
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
    No complete published solution of Munkres §48 Exercise 6 (printed p. 299) was located; the sets searched are listed in the
    COMPLAINTS.md entry for §43--§50 of SRC-TEXT-MUN00. Checked line by line against the book: the irrationals
    are the intersection of the countably many open dense sets R - {q_n}, and the criterion of Lemma 48.1 is
    applied in R, which is a Baire space by Theorem 48.2, to the countable family consisting of the dense open
    sets W_k of the subspace and the sets R - {q_n}. What was corrected: the card asserted that an open set of R
    whose trace on the irrationals is dense there must be dense in R, which is true but is a step of the
    argument, and it is now proved: an open interval missed by W_k would give a nonempty relatively open piece of
    the irrationals disjoint from V_k. The final step, that a set dense in R and contained in the irrationals is
    dense in the irrationals, is the definition of the subspace topology.
- event: source-checked
  by: claude
  date: 2026-11-15
  note: >-
    Searched outside the checkout (issue #144). Yougi, *Munkres Topology Solution: Chapter 8* (Nocturne blog,
    2025-07-10, https://hexo.yougi.top/2025/07/10/Munkres-Topology-Solution-Chapter-8/, text at
    tmp/sources/yougi-2025-munkres-chapter-8.md), answers Munkres §48 Exercise 6 (printed p. 299) at its Ex.
    48.6 with the single reduction "$\RR\setminus\QQ$ is a $G_\delta$ subset of $\RR$", which is the
    exercise's content only after Ex. 48.5 is applied: the post does not write the countable family whose
    intersection the irrationals are, and it does not say which theorem makes a $G_\delta$ set of a complete
    metric space Baire. The card supplies both, enumerating the rationals and applying Lemma 48.1 in $\RR$
    directly, so no part of the card depends on the post. Math StackExchange 3316496, "Yes/No : Is irrational
    number $(\QQ^c)$ are baires space?" (2019-08-12), asks this exercise and has no answer at all, the text
    kept at tmp/sources/mse-3316496-munkres-48-6.md. Murayama's selection stops at Chapter 4, dbFin has no
    Chapter 8 page, and no course page or repository outside the checkout was found carrying this exercise;
    the queries of this pass are in the COMPLAINTS.md entry for §43--§50.
- event: solution-written
  by: claude
  date: 2026-11-20
  note: >-
    The nine leaf steps of the two parts asserted their claim with no proof body; each now carries one. No
    claim is changed: the representation of the irrationals as the intersection of the sets $\RR\setminus\{q_n\}$,
    the passage from a dense open subset of the subspace to a dense open subset of $\RR$, the countability of the
    combined family and the application of Lemma 48.1 in the complete metric space $\RR$ all stand as they were.
    Cited by number only: Lemma 48.1 (a space is Baire exactly when every countable intersection of dense open
    sets is dense) and Theorem 48.2 ($\RR$ is a Baire space). Checked: that $\{q_n\}$ is closed in the metric space
    $\RR$ and its complement dense, that the two intersections agree, and that a subset of a dense subspace that
    is dense in the whole space is dense in the subspace.
---

::: {.exercise}

Show that the irrationals are a Baire space.
:::

::: {.solution}
Let $\irrationals = \RR \setminus \QQ$ with the subspace topology.

::: pf

::: pf-step
Representation of $\irrationals$ as a $G_\delta$ subset of $\RR$:

::: pf-proof

::: pf-step
Enumerate the countable set of rational numbers as $\QQ = \{q_n\}_{n=1}^\infty$.

::: pf-proof
$\QQ$ is countable: the integers are countable, and $\QQ$ is the image of $\ZZ\times\NN_{>0}$ under $(a,b)\mapsto a/b$, a countable set mapping onto a countable set. Enumerating that image and deleting repetitions gives the displayed list.
:::

:::

::: pf-step
For each $n \ge 1$, the singleton $\{q_n\}$ is closed in $\RR$, so $U_n = \RR \setminus \{q_n\}$ is an open and dense subset of $\RR$.

::: pf-proof
Points are closed in a metric space: the complement of $\{q_n\}$ is the union of the open balls of radius $\abs{x-q_n}$ about the other points, hence open. So $U_n$ is open. It is dense because every nonempty open interval $(a,b)$ with $a<b$ contains a rational, by the density of $\QQ$ in $\RR$, and that rational lies in $U_n$ as soon as it differs from $q_n$ — and if the only rational in the interval were $q_n$ itself, take a smaller subinterval avoiding it.
:::

:::

::: pf-step
The subspace of irrational numbers is:
$$\irrationals = \RR \setminus \QQ = \bigcap_{n=1}^\infty U_n.$$

::: pf-proof
A real number $x$ lies in every $U_n$ exactly when $x\ne q_n$ for every $n$, that is exactly when $x$ is not rational. So the intersection is the set of irrationals, and the second display is the definition of $\irrationals$.
:::

:::

:::

:::

::: {.pf-step #s2}
Verification of the dense open intersection condition:

::: pf-proof

::: pf-step
Let $\{V_k\}_{k=1}^\infty$ be a countable sequence of dense open subsets of the subspace $\irrationals$.

::: pf-proof
The family is an arbitrary countable family of subsets of $\irrationals$ that are open in the subspace and dense in it. It suffices to show that its intersection is dense in $\irrationals$, since that is the condition of Lemma 48.1 for a Baire space.
:::

:::

::: pf-step
Since each $V_k$ is open in $\irrationals$, there exists an open set $W_k \subseteq \RR$ such that $V_k = W_k \cap \irrationals$.

::: pf-proof
That is the definition of the subspace topology: the open sets of $\irrationals$ are exactly the intersections with $\irrationals$ of the open sets of $\RR$.
:::

:::

::: pf-step
The open set $W_k$ is dense in $\RR$: if it missed a nonempty open interval $I$, then $I\cap\irrationals$ would be a nonempty relatively open subset of $\irrationals$ disjoint from $V_k=W_k\cap\irrationals$, contradicting density of $V_k$ in $\irrationals$ (which is dense in $\RR$).

::: pf-proof
Suppose $W_k\cap I=\varnothing$ for a nonempty open interval $I$. The set $I\cap\irrationals$ is open in the subspace and nonempty because the irrationals are dense in $\RR$ and $I$ is a nonempty open subset of $\RR$; and $(I\cap\irrationals)\cap V_k\subseteq I\cap W_k=\varnothing$. A dense subset of $\irrationals$ meets every nonempty relatively open subset, so this contradicts the density of $V_k$.
:::

:::

::: pf-step
The combined collection $\{W_k\}_{k=1}^\infty \cup \{U_n\}_{n=1}^\infty$ is a countable family of open and dense subsets of $\RR$.

::: pf-proof
Each $W_k$ is open in $\RR$ by step 2.2 and dense by step 2.3; each $U_n$ is open and dense by step 1.2. A union of two countable families is countable.
:::

:::

::: pf-step
By the Baire category theorem, the complete metric space $\RR$ is a Baire space, so the countable intersection:
$$\bigcap_{k=1}^\infty W_k \cap \bigcap_{n=1}^\infty U_n = \left(\bigcap_{k=1}^\infty W_k\right) \cap \irrationals = \bigcap_{k=1}^\infty V_k$$
is dense in $\RR$.

::: pf-proof
$\RR$ is a complete metric space, hence a Baire space by Theorem 48.2, and by Lemma 48.1 the intersection of countably many dense open subsets of a Baire space is dense. Step 2.4 gives the countability. For the two equalities: the first uses step 1.3, and the second uses $W_k\cap\irrationals=V_k$ from step 2.2 together with the distributivity of intersection over the family, $(\bigcap_kW_k)\cap\irrationals=\bigcap_k(W_k\cap\irrationals)$.
:::

:::

::: pf-step
Since this intersection lies in $\irrationals$ and is dense in $\RR$, it is dense in the subspace $\irrationals$.

::: pf-proof
Let $D=\bigcap_kV_k$, a subset of $\irrationals$ dense in $\RR$, and let $O$ be a nonempty open subset of $\irrationals$. Then $O=G\cap\irrationals$ for some open $G\subseteq\RR$ by step 2.2, and $G\ne\varnothing$ because $O\ne\varnothing$; density of $D$ in $\RR$ gives a point of $D\cap G\subseteq D\cap O$. So $D$ meets every nonempty open subset of the subspace, which is density there.
:::

:::

:::

:::

::: pf-qed
By step [](#s2){.pf-ref}, every countable intersection of dense open subsets of $\irrationals$ is dense in $\irrationals$.

::: pf-proof
Steps 2.1 to 2.6 take an arbitrary countable family of dense open subsets of $\irrationals$ and show its intersection dense there; by Lemma 48.1 that is the defining property of a Baire space, so $\irrationals$ is Baire.
:::

:::

:::

:::
