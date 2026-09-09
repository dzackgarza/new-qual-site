---
schema: qual/card@1
id: P-TOPF02A
kind: problem
title: "Covering space of the figure-eight by the grid in the plane"
classification:
  areas:
  - topology
  topics:
  - Covering Spaces
  - Fundamental Group
relations: []
review: draft
---

::: problem
Let $E = \mathbb{R} \times \mathbb{Z} \cup \mathbb{Z} \times \mathbb{R}$ be the subset of the plane whose points have at least one of the coordinates an integer.
Let $S^1 \vee S^1 \subset \mathbb{R}^2 \times \mathbb{R}^2$ be the one-point union of circles.
Define $p : E \to S^1 \vee S^1$ by
$$
p(x, y) = (e^{2\pi i x}, e^{2\pi i y}).
$$

(a) Verify that $p$ is a covering space map.

(b) Let $\sigma : (I, 0) \to (E, (0, 0))$ be the loop which traverses the unit square $I \times \{0, 1\} \cup \{0, 1\} \times I$ once counterclockwise.
Prove that $p \sigma$ is the commutator of the two loops of the figure-eight.

(c) Prove that $p_* : \pi_1(E, (0, 0)) \to \pi_1(S^1 \vee S^1, (1, 1))$ is a monomorphism.
Show that this implies that $\pi_1(S^1 \vee S^1, (1, 1))$ is not abelian.
:::

::: {.solution}
<1>1. Away from the wedge point, $p:E\to S^1\vee S^1$ is locally a disjoint union of homeomorphisms.
::: {.proof}
A point in the interior of one circle of $S^1\vee S^1$ has a small arc neighborhood avoiding the wedge point. Its preimage consists of disjoint open intervals lying in horizontal grid lines (for the first circle) or vertical grid lines (for the second circle), and $p$ restricts on each interval to the usual exponential-coordinate homeomorphism onto the arc.
:::

<1>2. The wedge point also has an evenly covered neighborhood.
::: {.proof}
Choose sufficiently short open arcs $A_1,A_2\subset S^1$ about $1$, and let
$$
U=(A_1\times\{1\})\cup(\{1\}\times A_2)\subset S^1\vee S^1.
$$
For every lattice point $(m,n)\in\mathbb Z^2$, the component of $p^{-1}(U)$ containing $(m,n)$ is a small cross made from one horizontal and one vertical interval through $(m,n)$. Different lattice points give disjoint crosses, and $p$ maps each cross homeomorphically onto $U$.
:::

<1>3. Hence $p$ is a covering map.
::: {.proof}
Steps <1>1 and <1>2 provide an evenly covered neighborhood of every point of the figure-eight.
:::

<1>4. Let $a$ be the loop around the first circle and $b$ the loop around the second. Then
$$
[p\circ\sigma]=aba^{-1}b^{-1}.
$$
::: {.proof}
Traversing the unit square counterclockwise from $(0,0)$ gives: bottom edge from $(0,0)$ to $(1,0)$ maps to $a$; right edge maps to $b$; the top edge is traversed from $(1,1)$ to $(0,1)$ and maps to $a^{-1}$; the left edge maps to $b^{-1}$. Concatenating gives the commutator.
:::

<1>5. The induced homomorphism
$$
p_*:\pi_1(E,(0,0))\to\pi_1(S^1\vee S^1,(1,1))
$$
is injective.
::: {.proof}
Every covering map induces an injective homomorphism on fundamental groups. Concretely, if a loop in $E$ projects to a null-homotopic loop, lift a null-homotopy starting from that loop; uniqueness of lifts contracts the original loop.
:::

<1>6. The class $[\sigma]$ is nontrivial in $\pi_1(E,(0,0))$.
::: {.proof}
The space $E$ is a graph with vertices $\mathbb Z^2$ and unit horizontal and vertical edges. The loop $\sigma$ is the boundary of one square in this graph. Its cellular $1$-cycle is the nonzero sum of those four oriented edges, and the graph has no $2$-cells, so this cycle is nonzero in $H_1(E;\mathbb Z)$. Therefore $[\sigma]$ cannot be null-homotopic.
:::

<1>7. Thus $\pi_1(S^1\vee S^1)$ is nonabelian.
::: {.proof}
By <1>5--<1>6, $p_*[\sigma]\ne1$. By <1>4 this element is the commutator $aba^{-1}b^{-1}$. In an abelian group every commutator is trivial, so the fundamental group cannot be abelian.
:::
:::

