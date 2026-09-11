---
schema: qual/card@1
id: P-AGH2713NONPROJ
kind: problem
title: A complete nonprojective variety
classification:
  areas:
  - algebraic-geometry
  topics:
  - Complete Varieties
  - Picard Groups
  - Nodal Cubic
relations: []
review: draft
---

::: problem
Let $k$ be an algebraically closed field of characteristic $\neq 2$.
Let $C \subseteq \PP^2_k$ be the nodal cubic curve $y^2 z = x^3 + x^2 z$.
If $P_0 = (0, 0, 1)$ is the singular point, then $C - P_0$ is isomorphic to the multiplicative group $\GG_m = \Spec k[t, t\inv]$.
For each $a \in k$, $a \neq 0$, consider the translation of $\GG_m$ given by $t \mapsto at$.
This induces an automorphism of $C$ which we denote $\varphi_a$.
Now consider $C \times (\PP^1 - \ts{0})$ and $C \times (\PP^1 - \ts{\infty})$.
We glue their open subsets $C \times (\PP^1 - \ts{0, \infty})$ by the isomorphism
\[
\varphi: \gens{P, u} \mapsto \gens{\varphi_u(P), u}, \qquad P \in C,\ u \in \GG_m = \PP^1 - \ts{0, \infty}
.\]
Thus we obtain a scheme $X$, which is our example.
The projections to the second factor are compatible with $\varphi$, so there is a natural morphism $\pi: X \to \PP^1$.

a. Show that $\pi$ is a proper morphism, and hence that $X$ is a complete variety over $k$.

b. Show that
\[
\Pic(C \times \AA^1) \cong \GG_m \times \ZZ
\quad\text{and}\quad
\Pic(C \times (\AA^1 - \ts{0})) \cong \GG_m \times \ZZ \times \ZZ
.\]
   *Hint:* if $A$ is a domain and $*$ denotes the group of units, then $(A[u])^* \cong A^*$ and $(A[u, u\inv])^* \cong A^* \times \ZZ$.

c. Now show that the restriction map $\Pic(C \times \AA^1) \to \Pic(C \times (\AA^1 - \ts{0}))$ is of the form $\gens{t, n} \mapsto \gens{t, 0, n}$, and that the automorphism $\varphi$ of $C \times (\AA^1 - \ts{0})$ induces a map of the form $\gens{t, d, n} \mapsto \gens{t, d + n, n}$ on its Picard group.

d. Conclude that the image of the restriction map $\Pic X \to \Pic(C \times \ts{0})$ consists entirely of divisors of degree $0$ on $C$.
   Hence $X$ is not projective over $k$, and $\pi$ is not a projective morphism.
:::
