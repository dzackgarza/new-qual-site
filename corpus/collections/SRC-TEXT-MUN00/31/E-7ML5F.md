---
schema: qual/card@1
id: E-7ML5F
kind: problem
title: Separation axioms under refinement of topologies
classification:
  areas:
  - topology
  topics:
  - Separation Axioms
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
    Transcribed from the located published solutions: Ana Emilia de Orellana, "Solutions -
    Topology Munkres", Section 31 Exercise 4, printed p. 32
    (tmp/sources/munkres-solutions-anadeore.pdf), and "Doug's World", "Munkres - Topology -
    Chapter 4 Solutions" (30 August 2017), Problem 31.4, printed pp. 4-5
    (tmp/sources/munkres-solutions-dougsworld-ch4.pdf); checked against Munkres, Topology (2000),
    Section 31 Exercise 4, printed p. 199, Example 31.1 (printed p. 197: R_K is Hausdorff and not
    regular) and Example 31.2 (printed p. 198: R_l is normal). The six answers are those of the two
    sets: a finer topology inherits Hausdorffness from a coarser one and nothing else transfers in
    either direction. What was corrected: Orellana's R_K example for the failure of normality under
    passing to a finer topology reads "the K-topology is neither regular nor normal", which is
    correct but is asserted without the implication normal => regular that makes R_K a witness;
    the card states that implication (a normal space is regular because its one-point sets are
    closed). Doug's World's normal case is stated for R rather than argued; the card keeps the
    example and the reason.
- event: solution-written
  by: claude
  date: 2026-11-19
  note: >-
    Every step now carries a pf-proof: the three containers state why their subclaims suffice, and the 7
    leaf steps that asserted a claim with no justification each carry a sentence deriving it. One
    argument was corrected rather than merely justified: the backward failure of normality read "the
    cofinite topology is not normal (it is not even Hausdorff)", which is a non-sequitur, since normal
    together with T_1 implies Hausdorff and so cannot be refuted by failing Hausdorffness. The step now
    separates the two closed sets {x} and {y} directly: disjoint open sets would put one of them inside
    the finite complement of the other, hence finite and open, hence empty. The same direct argument is
    now given for the backward failure of regularity, which had been asserted without one. Checked
    against Munkres, Topology (2000), section 31 Exercise 4, printed p. 199, with Example 31.1 (p. 197,
    R_K Hausdorff and not regular) and Example 31.2 (p. 198); the transcription of the two published
    solutions recorded in the 2026-11-10 event is unchanged. Nothing in the statement was changed.
---

::: {.exercise}

Let $X$ and $X'$ denote a single set under two topologies $\mathcal{T}$ and $\mathcal{T}'$, respectively; assume that $\mathcal{T}' \supset \mathcal{T}$.
If one of the spaces is Hausdorff (or regular, or normal), what does that imply about the other?
:::

::: {.solution}

::: pf

::: pf-step
Hausdorff property ($T_2$):
- If $(X, \mathcal{T})$ is Hausdorff, then $(X, \mathcal{T}')$ is Hausdorff.
- If $(X, \mathcal{T}')$ is Hausdorff, $(X, \mathcal{T})$ need not be Hausdorff.

::: pf-proof
The subclaims prove the one implication that does hold and exhibit a counterexample to the other.

::: pf-step
**Forward preservation:** Suppose $(X, \mathcal{T})$ is Hausdorff. For any distinct $x \neq y \in X$, there exist disjoint open sets $U, V \in \mathcal{T}$ with $x \in U$ and $y \in V$. Since $\mathcal{T} \subset \mathcal{T}'$, $U, V \in \mathcal{T}'$, so $(X, \mathcal{T}')$ is Hausdorff.

::: pf-proof
The sets $U$ and $V$ separate the two points and are open in the finer topology because every member of $\mathcal{T}$ is a member of $\mathcal{T}'$.
:::

:::

::: pf-step
**Backward failure:** The discrete topology $\mathcal{T}'$ on an infinite set $X$ is Hausdorff, but the coarser cofinite topology $\mathcal{T}$ on $X$ is not Hausdorff.

::: pf-proof
The discrete topology separates any two points by the singletons. In the cofinite topology two non-empty open sets have finite complements, so their intersection has finite complement and is therefore non-empty; no two disjoint non-empty open sets exist, and $X$ is infinite.
:::

:::

:::

:::

::: pf-step
Regular property ($T_3$):
Neither direction holds:
- $(X, \mathcal{T})$ regular does NOT imply $(X, \mathcal{T}')$ is regular.
- $(X, \mathcal{T}')$ regular does NOT imply $(X, \mathcal{T})$ is regular.

::: pf-proof
The two failures are exhibited by different pairs of topologies, one using the $K$-topology on $\RR$ and one using the cofinite topology.

::: pf-step
**Forward failure:** The standard Euclidean topology $\mathcal{T}$ on $\RR$ is regular (and metric). The $K$-topology $\mathcal{T}' = \mathcal{T}_K$ is strictly finer than $\mathcal{T}$, but $(\RR, \mathcal{T}_K)$ is not regular because the closed set $K = \{1/n \mid n \in \ZZ_+\}$ and the point $0 \notin K$ cannot be separated by disjoint open sets in $\mathcal{T}_K$.

::: pf-proof
This is Example 31.1 of Munkres: $\RR_K$ is Hausdorff but not regular, the witness being the closed set $K$ and the point $0$, which admit no disjoint open neighbourhoods.
:::

:::

::: pf-step
**Backward failure:** The discrete topology $\mathcal{T}'$ on an infinite set $X$ is regular, but the coarser cofinite topology $\mathcal{T}$ is not regular.

::: pf-proof
The discrete topology is regular because every set is open, so a point and a closed set avoiding it are separated by themselves. In the cofinite topology, let $x\neq y$; a closed set is finite, so an open set containing $y$ has finite complement, and a disjoint open set containing $x$ would lie in that finite complement, hence be finite and open, hence empty. So the point $x$ and the closed set $\{y\}$ are not separated.
:::

:::

:::

:::

::: pf-step
Normal property ($T_4$):
Neither direction holds:
- $(X, \mathcal{T})$ normal does NOT imply $(X, \mathcal{T}')$ is normal.
- $(X, \mathcal{T}')$ normal does NOT imply $(X, \mathcal{T})$ is normal.

::: pf-proof
The two failures use the same pair of topologies as the regular case, with the implication normal implies regular supplying the first.

::: pf-step
**Forward failure:** The standard Euclidean topology $\mathcal{T}$ on $\RR$ is normal, but the strictly finer $K$-topology $\mathcal{T}_K$ is not even regular, and therefore not normal.

::: pf-proof
$\RR$ with the Euclidean topology is metrizable, and every metrizable space is normal. A normal space is regular, because its one-point sets are closed and the separation axiom for a point and a disjoint closed set is the defining one; since $\RR_K$ is not regular by the preceding container, it is not normal.
:::

:::

::: pf-step
**Backward failure:** The discrete topology $\mathcal{T}'$ on an infinite set $X$ is normal, but the coarser cofinite topology $\mathcal{T}$ is not normal.

::: pf-proof
The discrete topology is normal because every subset is open, so disjoint closed sets are separated by themselves. In the cofinite topology, let $x\neq y$ and consider the disjoint closed sets $\{x\}$ and $\{y\}$: if $U\ni x$ and $V\ni y$ were disjoint open sets, then $V\subseteq X\setminus U$, a finite set, so $V$ would be finite and open, hence empty, contradicting $y\in V$. So those two closed sets are not separated and the topology is not normal. Note that this topology is $T_1$ — its one-point sets are closed — so the failure is a genuine failure of normality and not a failure of the $T_1$ condition.
:::

:::

:::

:::

::: pf-step
Summary Table of Implications:
- **Hausdorff:** Coarser $\implies$ Finer (yes); Finer $\implies$ Coarser (no).
- **Regular:** Coarser $\implies$ Finer (no); Finer $\implies$ Coarser (no).
- **Normal:** Coarser $\implies$ Finer (no); Finer $\implies$ Coarser (no).

::: pf-proof
The four entries record what the three preceding containers prove: the one implication that holds, for the Hausdorff property, and the five counterexamples that refute the others.
:::

:::

:::

:::
