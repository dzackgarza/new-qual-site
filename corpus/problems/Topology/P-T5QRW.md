---
schema: qual/card@1
id: P-T5QRW
kind: problem
title: Regular covering spaces and a non-regular cover of $\Theta$
classification:
  areas:
  - topology
  topics:
  - Covering Spaces
  - Group Actions
  - Fundamental Group
relations: []
review: draft
---

::: {.problem}
a.
What is the definition of a **regular** (or Galois) covering space?

b.
State, without proof, a criterion in terms of the fundamental group for a covering map $p : \tilde X \to X$ to be regular.

c.  
Let $\Theta$ be the topological space formed as the union of a circle and its diameter (so this space looks exactly like the letter $\Theta$). 
Give an example of a covering space of $\Theta$ that is not regular.
:::

::: {.solution}
<1>1. A connected covering $p:\widetilde X\to X$ is regular (Galois) if its deck-transformation group acts transitively on each fiber.
::: {.proof}
Equivalently, for any two points of the same fiber there is a deck transformation carrying one to the other.
:::

<1>2. If $X$ is path connected, locally path connected, and semilocally simply connected, the connected cover corresponding to a subgroup $H\le\pi_1(X,x_0)$ is regular iff $H$ is normal in $\pi_1(X,x_0)$.
::: {.proof}
This is the standard subgroup criterion in covering-space theory.
:::

<1>3. For $\Theta$, choose free generators $a,b$ of
$$\pi_1(\Theta)\cong F_2$$
and take the connected covering corresponding to the subgroup $H=\langle a\rangle$.
::: {.proof}
The graph $\Theta$ is homotopy equivalent to a wedge of two circles, hence has free fundamental group of rank $2$. The subgroup-covering correspondence produces a connected graph covering for every subgroup.
:::

<1>4. This covering is not regular.
::: {.proof}
The subgroup $H=\langle a\rangle$ is not normal in $F_2$: for example $bab^{-1}\notin\langle a\rangle$. By <1>2, the corresponding cover is nonregular.
:::
:::
