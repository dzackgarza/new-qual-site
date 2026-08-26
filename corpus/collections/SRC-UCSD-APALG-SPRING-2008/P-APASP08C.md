---
schema: qual/card@1
id: P-APASP08C
kind: problem
title: "Character of a permutation representation, orbits, and double cosets"
classification:
  areas:
  - applied-algebra
  topics:
  - Representation Theory
  - Group Actions
  - Character Theory
relations: []
review: draft
---

::: problem
Let $\Gamma$ act on a family $\mathcal{F}$, and let $\chi$ be the character of the permutation representation resulting from this action.

**(a)** Show that the multiplicity of the trivial representation in this representation is equal to the number of orbits of $\mathcal{F}$ under the action of $\Gamma$.

**(b)** Show that the integer $\langle \chi, \chi \rangle$ counts the number of orbits in the action of $\Gamma$ on the family of ordered pairs
$$
\mathcal{F} \times \mathcal{F} = \bigl\{ (f, g) : f, g \in \mathcal{F} \bigr\}.
$$

**(c)** Suppose that $\Gamma$ acts transitively on $\mathcal{F}$.
Let $f_0$ be an element of $\mathcal{F}$, $H$ be its stabilizer, and let
$$
\Gamma = H\tau_1 H + H\tau_2 H + \cdots + H\tau_k H
$$
be the double coset decomposition of $\Gamma$ resulting from the equivalence relation
$$
\gamma_1 \sim_H \gamma_2 \quad\Longleftrightarrow\quad \gamma_2 = h'\gamma_1 h'' \quad\text{(for some } h', h'' \in H\text{)}.
$$
Show that in this case $\langle \chi, \chi \rangle_\Gamma = k$.
Hint: Use part (b).
:::
