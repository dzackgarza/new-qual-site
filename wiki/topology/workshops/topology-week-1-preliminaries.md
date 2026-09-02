---
order: 19
title: "Topology Qual Prep Week 1: Point-Set"
---

# Topology Qual Prep Week 1: Point-Set

This page covers the point-set topology you need before algebraic topology.
The topics below are the standard qual material — definitions, key theorems, and the counterexamples that show where intuition breaks.

## Topics

- Topologies, open/closed/clopen, bases

- Continuity, homeomorphisms

- Subspaces, products, quotients

- Closures, retracts

- Metric spaces: complete, bounded

- Compactness

- Connectedness: path-connected, locally path-connected, totally disconnected

- Separation axioms: Hausdorff, regular, normal

- The tube lemma

- Common counterexamples (topologist's sine curve)

## Warmups

- State the axioms of a topology.

- What does it mean for a set to be open?
  Closed?
  [[E-YUGKU]] [[E-OIS5D]] [[E-EE4EE]] [[E-KJQUD]] [[E-FLVZU]] [[E-6W4WA]] [[E-XSXAZ]] [[E-ARJT3]] [[E-45N4G]]

## Exercises

- Prove Cantor's intersection theorem.

- Determine if the following subsets of $\RR$ are open, closed, both, or neither: [[P-MFWBK]] [[P-HPN6K]] [[P-N7RR5]] [[P-2V6GL]] [[P-3GOJI]] [[P-JAEYU]] [[P-FNJCM]] [[P-WXTVX]] [[P-NNHWB]] [[P-OTXNQ]] [[P-NJNNL]] [[P-SG462]] [[P-GAA3C]] [[P-YBQ3V]] [[P-ZQBPZ]] [[P-WHXWM]] [[P-TC2PJ]]

## The Tube Lemma

The tube lemma is the tool you reach for whenever a proof needs to "separate" a compact set from the rest of a product.
It says: if $Y$ is compact and $N$ is an open set in $X \times Y$ containing the slice $\{x_0\} \times Y$, then there exists an open neighborhood $U$ of $x_0$ in $X$ such that $U \times Y \subseteq N$.

The proof is elementary compactness: for each $y \in Y$, choose open sets $U_y \ni x_0$ and $V_y \ni y$ with $U_y \times V_y \subseteq N$.
The $V_y$ cover $Y$, so finitely many suffice: $V_{y_1}, \ldots, V_{y_k}$.
Set $U = \bigcap_{i=1}^k U_{y_i}$.
Then $U \times Y \subseteq N$.

### Typical qual questions

The tube lemma appears in qual problems in several disguises:

1. **Products of compact spaces are compact.** Use the tube lemma to reduce to the finite subcover case: cover $X \times Y$ by open sets, fix $x \in X$, the slice $\{x\} \times Y$ is compact, extract a finite subcover, then use the tube lemma to thicken each slice into a neighborhood that works for all of $Y$.

2. **Projections along compact fibers are closed maps.** If $p: X \times Y \to X$ is the projection and $Y$ is compact, then $p$ is a closed map.
   Given a closed $A \subseteq X \times Y$ and a point $x \notin p(A)$, the complement of $A$ is open and contains $\{x\} \times Y$.
   The tube lemma gives a neighborhood $U$ of $x$ with $U \times Y$ disjoint from $A$, so $U \cap p(A) = \emptyset$.

3. **Quotient maps and products with a locally compact factor.** While any quotient map $f: X \to Y$ satisfies $g \circ f \text{ continuous} \iff g \text{ continuous}$, products of quotient maps need not be quotient maps in general.
   If $Z$ is locally compact Hausdorff, then $f \times \operatorname{id}_Z: X \times Z \to Y \times Z$ is a quotient map.
   The tube lemma is the tool used to show that saturated open sets in $X \times Z$ project to open sets in $Y \times Z$.

## Qual Questions

::: {.remark}
The following are from the tube lemma worksheet.
Each problem asks you to apply the tube lemma or a compactness argument to a concrete situation.
:::

Tube lemma: ![](../../../assets/Workshops/Topology/_attachments/Pasted%20image%2020210520142907.png)

![](../../../assets/Workshops/Topology/_attachments/Pasted%20image%2020210520143017.png)

![](../../../assets/Workshops/Topology/_attachments/Pasted%20image%2020210520143456.png)

![](../../../assets/Workshops/Topology/_attachments/Pasted%20image%2020210520143537.png)

![](../../../assets/Workshops/Topology/_attachments/Pasted%20image%2020210520143652.png)
