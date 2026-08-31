---
schema: qual/card@1
id: P-E53UO
kind: problem
title: Attaching a $2$-cell along homotopic maps yields homotopy-equivalent spaces
classification:
  areas:
  - topology
  topics:
  - Homotopy
  - Cell Complexes
  - Retracts
relations: []
review: draft
---

::: problem
8. **Main Idea**: Show that both spaces are a deformation retract of the same space.
   (See Hatcher, Proposition 0.18, p. 25)

Suppose we have the following maps

$$
f: S^1 \into X\\
g: S^1 \into X
$$

where $f \homotopic g$.
Then there exists a homotopy

$$H: S^1 \cross I \into X$$

such that $H(z, 0) = f(z)$ and $H(z,1) = g(z)$.

Then define
$$
P \definedas X \coprod_f B^2\\
Q \definedas X \coprod_g B^2
$$

We want to that $P$ and $Q$ are homotopy-equivalent.
In order to do so, we will construct a larger space which deformation retracts onto both $P$ and $Q$, which is a homotopy equivalence.

With $H$ in hand, we can define the space $R = X \coprod_H B^2 \cross I$, where we recognize $S^1 = \bd B^2$.
In particular, $S^1$ is a subspace of $B^2$.

Claim: Both $P$ and $Q$ are subspaces of $R$.
Since $H(z, 0) = f(z)$.
So considering $X \coprod_H B^2 \times \theset{0} \cong X \coprod_f B^2 = P$.
A similar argument holds at the point $1\in I$.
(*Not a strong argument*)

But note that $B^2 \cross I$ is a solid cylinder, and so can be deformation retracted onto the outer shell plus one of the "lids".
Formally, this would be given by $S^1 \times I \cup B^2 \cross \theset{p}$ for some $p\in [0,1]$.

Claim: choosing $p=0$ induces a deformation retract of $R$ onto $P$, and choosing $p=1$ induces a deformation retract of $R$ onto $Q$.

Proof: We construct the deformation retraction of $R$ onto $P$ explicitly; the case $p = 1$ is identical.

The space $R = X \coprod_H B^2 \times I$ is obtained from $X$ by attaching the solid cylinder $B^2 \times I$ along the map $H: S^1 \times I \to X$ on its lateral boundary $S^1 \times I$.
The cylinder $B^2 \times I$ deformation retracts onto the union of its lateral boundary and one lid:
\[
S^1 \times I \cup B^2 \times \theset{0}.
\]
Concretely, the map $r: B^2 \times I \to S^1 \times I \cup B^2 \times \theset{0}$ given by radial projection of each slice $B^2 \times \theset{t}$ onto its boundary circle $S^1 \times \theset{t}$, followed by sliding the resulting point down to the lid $B^2 \times \theset{0}$ along the $I$-coordinate, is a deformation retraction: it fixes $S^1 \times I \cup B^2 \times \theset{0}$ pointwise, and it is homotopic to the identity through the family that interpolates the radial projection.

This retraction is compatible with the attaching map $H$: on the lateral boundary $S^1 \times I$ it is the identity, so it descends to a well-defined map $\bar r: R \to R$ that fixes $X$ and the attached lid $B^2 \times \theset{0}$.
The image of $\bar r$ is exactly $X \coprod_H (B^2 \times \theset{0})$, and since $H(z, 0) = f(z)$, this is precisely $P = X \coprod_f B^2$.
The homotopy from $r$ to the identity likewise descends to a homotopy from $\bar r$ to the identity of $R$, so $P$ is a deformation retract of $R$.

The same construction with the lid $B^2 \times \theset{1}$ (using $H(z, 1) = g(z)$) shows $Q = X \coprod_g B^2$ is a deformation retract of $R$.

Since $P$ and $Q$ are both deformation retracts of the same space $R$, they are homotopy equivalent to $R$, hence homotopy equivalent to each other.
:::
