---
schema: qual/card@1
id: P-AMD-6RPCGOV7
kind: problem
title: Presentation complex of a group
classification:
  areas:
  - topology
  topics:
  - Cell Complexes
  - Fundamental Group
  - Groups
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-25
- event: solution-written
  by: claude
  date: 2026-11-19
  note: >-
    Every step now carries a pf-proof: the three containers state why their subclaims suffice, the ten
    leaf steps that asserted a claim with no justification each carry a sentence deriving it, and the
    presentation G = <A | R> is now a step of the proof rather than a paragraph outside it. Both pf-qed
    blocks were removed: the one inside s3 and the one closing the proof each only referred back to
    earlier steps, which STYLE-08 forbids, and the last step of each level now carries the QED label. The
    mathematics is unchanged: the 1-skeleton is the wedge of one circle per generator with fundamental
    group F(A), each relator is realized by a loop spelled along those circles, and Hatcher's Proposition
    1.26 identifies the fundamental group of the 2-skeleton with F(A) modulo the normal closure of the
    attaching classes. Nothing in the statement was changed.
---

::: {.problem}
Given a group $G = <A : R>$, show how to construct a CW-complex $X$ such that $\pi_1(X) = G$.
:::

::: {.solution}

::: pf

::: pf-step
Let $G = \langle A \mid R \rangle$ with generator set $A$ and relator set $R$.

::: pf-proof
This is the presentation given: a presentation consists of a set of generators and a set of relators, each relator a word in the generators and their inverses.
:::

:::

::: {.pf-step #s1}
Construct the 0-skeleton $X^0$ and 1-skeleton $X^1$.

::: pf-proof
The subclaims build the 1-skeleton and identify its fundamental group.

::: pf-step
Set the 0-skeleton $X^0 = \{x_0\}$ to be a single vertex.

::: pf-proof
A single point is a CW complex of dimension $0$.
:::

:::

::: pf-step
For each generator $a \in A$, attach a 1-cell $e_a^1 = [0, 1]$ to $X^0$ by identifying both endpoints $0, 1 \in \partial e_a^1$ to the vertex $x_0$.

::: pf-proof
A 1-cell is a copy of $[0,1]$ attached along its boundary $S^0=\{0,1\}$ by a map into the 0-skeleton; sending both endpoints to $x_0$ is such a map.
:::

:::

::: pf-step
The 1-skeleton is the wedge sum of circles indexed by $A$: $$X^1 = \bigvee_{a \in A} S_a^1.$$

::: pf-proof
Identifying the two endpoints of an interval produces a circle, and all these circles share the single vertex $x_0$; their union is by definition the wedge.
:::

:::

::: pf-step
By the Seifert-van Kampen theorem, the fundamental group of $X^1$ is the free group on $A$: $$\pi_1(X^1, x_0) \cong F(A) = \langle A \mid \emptyset \rangle.$$

::: pf-proof
The wedge of circles indexed by $A$ has fundamental group the free product of one copy of $\ZZ$ per circle, which is the free group $F(A)$.
:::

:::

:::

:::

::: {.pf-step #s2}
Attach 2-cells to form the 2-skeleton $X = X^2$.

::: pf-proof
The subclaims encode each relator as a loop in the 1-skeleton and attach a 2-cell along it.

::: pf-step
Each relator $r \in R$ is a reduced word in the free group $F(A)$, say $r = a_{i_1}^{\epsilon_1} a_{i_2}^{\epsilon_2} \cdots a_{i_k}^{\epsilon_k}$ with $a_{i_j} \in A$ and $\epsilon_j \in \{\pm 1\}$.

::: pf-proof
A relator is by definition a word in the generators and their inverses, and it may be taken reduced because cancelling a pair $aa^{-1}$ does not change the element of $F(A)$ it represents.
:::

:::

::: pf-step
Define a continuous attaching map $\phi_r \colon \partial D^2 \cong S^1 \to X^1$ by parameterizing $S^1 = [0, 1] / (0 \sim 1)$ into $k$ equal subintervals $[(j-1)/k, j/k]$, and mapping the $j$-th subinterval to traverse the loop $e_{a_{i_j}}^1$ in the positive direction if $\epsilon_j = 1$ and in the reverse direction if $\epsilon_j = -1$.

::: pf-proof
The subintervals meet only at their endpoints, all of which map to $x_0$, so the piecewise definitions agree on the overlaps and give a continuous map of the circle; each subinterval is mapped along the characteristic map of the corresponding 1-cell.
:::

:::

::: pf-step
Under this definition, the loop $\phi_r$ represents the homotopy class $[\phi_r] = r \in \pi_1(X^1, x_0)$.

::: pf-proof
The loop traverses the 1-cells in the order and the directions of the letters of $r$, and $\pi_1(X^1,x_0)$ is free on those 1-cells, so its class is exactly that word.
:::

:::

::: pf-step
Attach a 2-cell $e_r^2 \cong D^2$ along $\phi_r$ for each relator $r \in R$: $$X = X^2 = X^1 \cup_{\{\phi_r\}_{r \in R}} \left( \bigsqcup_{r \in R} D_r^2 \right).$$

::: pf-proof
For each relator the attaching map is the loop built in the preceding subclaims, and the space displayed is by definition the result of adjoining those 2-cells to $X^1$ along them.
:::

:::

:::

:::

::: {.pf-step #s3}
Apply the cellular Seifert-van Kampen theorem to compute $\pi_1(X, x_0)$.

::: pf-proof
The subclaims apply the theorem on attaching 2-cells and identify the two ingredients of its quotient.

::: {.pf-step #s3-1}
By the standard theorem on fundamental groups of 2-dimensional CW complexes (e.g. Hatcher Proposition 1.26), attaching a family of 2-cells $\{e_r^2\}_{r \in R}$ along maps $\phi_r \colon \partial D^2 \to X^1$ induces an isomorphism: $$\pi_1(X, x_0) \cong \pi_1(X^1, x_0) / N,$$ where $N = \langle\langle [\phi_r] : r \in R \rangle\rangle$ is the normal subgroup of $\pi_1(X^1, x_0)$ generated by the homotopy classes of the attaching maps.

::: pf-proof
Hatcher's Proposition 1.26 states that attaching 2-cells along loops makes the inclusion of the 1-skeleton induce a surjection whose kernel is the normal subgroup generated by the classes of those loops; the first isomorphism theorem for groups turns that into the displayed isomorphism.
:::

:::

::: pf-step
By step [](#s1){.pf-ref}, $\pi_1(X^1, x_0) = F(A)$.

::: pf-proof
That is the identification of the fundamental group of the 1-skeleton made in the first container.
:::

:::

::: pf-step
By step [](#s2){.pf-ref}, $[\phi_r] = r \in F(A)$ for each $r \in R$, so $N = \langle\langle R \rangle\rangle$.

::: pf-proof
$N$ is generated by the classes $[\phi_r]$, which are the relators, so it is by definition the normal closure of $R$ in $F(A)$.
:::

:::

::: pf-step
Thus, $\pi_1(X, x_0) \cong F(A) / \langle\langle R \rangle\rangle \cong \langle A \mid R \rangle = G$.

::: pf-proof
Substituting the two identifications into the isomorphism of the first subclaim gives the quotient, and the group presented by $\langle A\mid R\rangle$ is by definition that quotient.
:::

:::

:::

:::

:::

:::
