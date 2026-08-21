---
schema: qual/card@1
id: S-IXVV7
kind: solution
title: Solution to P-DLFQC
classification:
  areas:
  - algebra
  topics:
  - Geometry
  - Commutative Algebra
  - Maximal Ideals
relations:
- kind: solves
  target: P-DLFQC
review: draft
---

::: {.solution}
**(a)** NSS: There are mutually inverse, inclusion-reversing bijections $$V: \{\text{radical ideals of }F[X]\} \leftrightarrow \{\text{closed subsets of }X\} : I$$ given by $V(J) = \{x\in X \mid f(x)=0\ \forall f\in J\}$ and $I(S) = \{f\in F[X] \mid f(x)=0\ \forall x\in S\}$.

For the second part, we need to show $\overline S = X \iff I(S) = (0)$.

Claim: $\overline S = V(I(S))$.

Proof.
$S \subseteq V(I(S))$ closed, hence $\overline S \subseteq V(I(S))$.
If $S \subseteq V(J)$ for $J = \sqrt J$, $V(I(S)) \subseteq V(I(V(J))) = V(J)$.
This shows $V(I(S)) \subseteq \overline S$.

Hence, $\overline S = X \iff V(I(S)) = X \iff I(S) = I(X) = (0)$.

**(b)** There are several proofs.
All should note somewhere that $F[X\times Y] = F[X]\otimes F[Y]$ by definition of product.

Say $\theta \in F[X\times Y]$ is zero on $S\times T$.
RTP $\theta=0$.
Write $\theta = \sum_i f_i\otimes g_i \in F[X]\otimes F[Y]$, $f_i$'s linearly independent.
For any $t\in T$, $\sum_i f_ig_i(t) \in F[X]$ is zero on $S$, hence zero as $S$ is dense in $X$.
As $f_i$'s are linearly independent, this implies $g_i(t)=0$ for all $t\in T$, so $g_i=0$ as $T$ is dense in $Y$.
Therefore $\theta=0$.

**(c)** This follows from (b) by induction on $n$ as $\mathbb{Z}$ is dense in $F$ (being infinite!).
:::
