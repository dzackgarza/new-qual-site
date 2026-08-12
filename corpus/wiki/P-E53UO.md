---
schema: qual/card@1
id: P-E53UO
kind: problem
title: "Main Idea: Show that both spaces are a deformation retract\u2026"
classification:
  areas:
  - topology
  topics: []
relations: []
review: draft
---

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

Proof: ?
