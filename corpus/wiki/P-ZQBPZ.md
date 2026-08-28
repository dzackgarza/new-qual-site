---
schema: qual/card@1
id: P-ZQBPZ
kind: problem
title: Closed sets covering a connected space with connected intersection are connected
classification:
  areas:
  - topology
  topics:
  - Point-Set Topology
  - Closure
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

::: problem
Let $X$ be a connected space and $A,B\subseteq X$ closed subsets with $X=A\cup B$ and $A\cap B$ connected.
Show that $A$ and $B$ are connected.

![](../../assets/Workshops/Topology/_attachments/Pasted%20image%2020210520145810.png)
:::

::: {.solution}
**Goal.** For connected $X = A \cup B$ with $A, B$ closed and $A \cap B$ connected, show $A$ and $B$ are connected.

<1>1. Suppose $A$ is disconnected.
Proof: assume for contradiction.

<1>2. Then $A = C \cup D$ with $C, D$ nonempty, disjoint, and closed in $A$ (hence closed in $X$, since $A$ is closed).
Proof: a disconnected space is a union of two nonempty disjoint closed subsets.

<1>3. $A \cap B$ is connected, so it lies entirely in $C$ or entirely in $D$.
Proof: $A \cap B = (C \cap B) \cup (D \cap B)$ is a union of two disjoint closed sets; since $A \cap B$ is connected, one of them is empty, so $A \cap B \subseteq C$ or $A \cap B \subseteq D$.

<1>4. WLOG $A \cap B \subseteq C$.
Proof: relabel if necessary.

<1>5. Then $X = (C \cup B) \cup D$ is a union of two disjoint nonempty closed sets.
<2>1. $C \cup B$ and $D$ are disjoint.
Proof: $C \cap D = \emptyset$ and $B \cap D = \emptyset$ (since $A \cap B \subseteq C$ and $D \subseteq A$).
<2>2. $C \cup B$ and $D$ are closed.
Proof: $C, D$ are closed in $X$, and $B$ is closed, so $C \cup B$ is closed.
<2>3. Both are nonempty.
Proof: $C \neq \emptyset$ and $D \neq \emptyset$.
<2>4. $X = (C \cup B) \cup D$.
Proof: $X = A \cup B = (C \cup D) \cup B = (C \cup B) \cup D$.

<1>6. This contradicts $X$ being connected.
Proof: $X$ is a union of two disjoint nonempty closed sets.

<1>7. Hence $A$ is connected; by symmetry, $B$ is connected.
Proof: the same argument with $A$ and $B$ swapped.

<1>8. Q.E.D.
Proof: <1>7 is the claim.
:::
