---
order: 19
title: "Topology Qual Prep Week 1: Point-Set"
---

# Topology Qual Prep Week 1: Point-Set

Point-set topology used in algebraic topology: definitions, theorems, and counterexamples.

## Topics

- Topologies, open, closed, and clopen sets, bases

- Continuity, homeomorphisms

- Subspaces, products, quotients

- Closures, retracts

- Metric spaces: completeness, boundedness

- Compactness

- Connectedness: path-connected, locally path-connected, totally disconnected

- Separation axioms: Hausdorff, regular, normal

- The tube lemma

- Common counterexamples, such as the topologist's sine curve

## Warmups

- State the axioms of a topology.

- What does it mean for a set to be open?
  Closed?
  [[E-YUGKU]] [[E-OIS5D]] [[E-EE4EE]] [[E-KJQUD]] [[E-FLVZU]] [[E-6W4WA]] [[E-XSXAZ]] [[E-ARJT3]] [[E-45N4G]]

## Exercises

- Prove Cantor's intersection theorem.

- Determine if the following subsets of $\RR$ are open, closed, both, or neither: [[P-MFWBK]] [[P-HPN6K]] [[P-N7RR5]] [[P-2V6GL]] [[P-3GOJI]] [[P-JAEYU]] [[P-FNJCM]] [[P-WXTVX]] [[P-NNHWB]] [[P-OTXNQ]] [[P-NJNNL]] [[P-SG462]] [[P-GAA3C]] [[P-YBQ3V]] [[P-ZQBPZ]] [[P-WHXWM]] [[P-TC2PJ]]

## The tube lemma

::: {.theorem title="Tube lemma"}
Let $X$ and $Y$ be spaces with $Y$ compact, let $x_0\in X$, and let $N\subseteq X \times Y$ be open with $\ts{x_0} \times Y\subseteq N$.
Then there is an open neighborhood $U$ of $x_0$ in $X$ with $U \times Y \subseteq N$.

:::

::: {.proof}
For each $y \in Y$, choose open sets $U_y \ni x_0$ and $V_y \ni y$ with $U_y \times V_y \subseteq N$.
The $V_y$ cover $Y$, so finitely many $V_{y_1}, \ldots, V_{y_k}$ cover $Y$ by compactness.
Set $U \coloneqq \bigcap_{i=1}^k U_{y_i}$, an open neighborhood of $x_0$.
For $(x,y)\in U\times Y$, choose $i$ with $y\in V_{y_i}$; then $(x,y)\in U_{y_i}\times V_{y_i}\subseteq N$.

:::

::: {.example title="Applications of the tube lemma"}
\envlist

1. **Products of compact spaces are compact.** Let $X$ and $Y$ be compact and $\mathcal U$ an open cover of $X\times Y$. For each $x \in X$, the compact slice $\ts{x} \times Y$ is covered by finitely many members of $\mathcal U$, whose union $N_x$ contains a tube $W_x\times Y$ by the tube lemma. Finitely many $W_{x_1},\ldots,W_{x_m}$ cover $X$, and the finitely many members of $\mathcal U$ used for $N_{x_1},\ldots,N_{x_m}$ cover $X\times Y$.

2. **Projections along compact factors are closed maps.** If $Y$ is compact, the projection $p\colon X \times Y \to X$ is closed.
   Given a closed $A \subseteq X \times Y$ and $x \notin p(A)$, the complement of $A$ is open and contains $\ts{x} \times Y$.
   The tube lemma gives a neighborhood $U$ of $x$ with $U \times Y$ disjoint from $A$, so $U \cap p(A) = \emptyset$.

3. **Products of quotient maps with a locally compact factor.** A product of quotient maps need not be a quotient map.
   If $f\colon X \to Y$ is a quotient map and $Z$ is locally compact Hausdorff, then $f \times \operatorname{id}_Z\colon X \times Z \to Y \times Z$ is a quotient map; the proof uses compact neighborhoods in $Z$ and the tube lemma to show that the image of a saturated open subset of $X \times Z$ is open in $Y \times Z$.

:::

## Worksheet problems

Problems from the tube lemma worksheet:

![Tube lemma worksheet, problem 1](../../../assets/Workshops/Topology/_attachments/Pasted%20image%2020210520142907.png)

![Tube lemma worksheet, problem 2](../../../assets/Workshops/Topology/_attachments/Pasted%20image%2020210520143017.png)

![Tube lemma worksheet, problem 3](../../../assets/Workshops/Topology/_attachments/Pasted%20image%2020210520143456.png)

![Tube lemma worksheet, problem 4](../../../assets/Workshops/Topology/_attachments/Pasted%20image%2020210520143537.png)

![Tube lemma worksheet, problem 5](../../../assets/Workshops/Topology/_attachments/Pasted%20image%2020210520143652.png)
