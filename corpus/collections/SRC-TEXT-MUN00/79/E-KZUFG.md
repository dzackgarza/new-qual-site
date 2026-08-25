---
schema: qual/card@1
id: E-KZUFG
kind: exercise
title: Covering maps of topological groups lift the group structure
classification:
  areas:
  - topology
  topics:
  - Covering Spaces
  - Topological Groups
relations: []
review: draft
---

::: {.exercise title="Munkres §79.6"}

Prove the following.

Theorem.
Let $G$ be a topological group with multiplication operation $m: G \times G \to G$ and identity element $e$.
Assume $p: \overline{G} \to G$ is a covering map.
Given $\tilde{e}$ with $p(\tilde{e}) = e$, there is a unique multiplication operation on $\overline{G}$ that makes it into a topological group such that $\tilde{e}$ is the identity element and $p$ is a homomorphism.

(a) Let $I: G \to G$ be the map $I(g) = g^{-1}$.
Show there exist unique maps $\overline{m}: \overline{G} \times \overline{G} \to \overline{G}$ and $\overline{I}: \overline{G} \to \overline{G}$ with $\overline{m}(\tilde{e} \times \tilde{e}) = \tilde{e}$ and $\overline{I}(\tilde{e}) = \tilde{e}$ such that $p \circ \overline{m} = m \circ (p \times p)$ and $p \circ \overline{I} = I \circ p$.

(b) Show the maps $\overline{G} \to \overline{G}$ given by $\tilde{g} \to \overline{m}(\tilde{e} \times \tilde{g})$ and $\tilde{g} \to \overline{m}(\tilde{g} \times \tilde{e})$ equal the identity map of $\overline{G}$.
[Hint: Use the uniqueness part of Lemma 79.1.]

(c) Show the maps $\overline{G} \to \overline{G}$ given by $\tilde{g} \to \overline{m}(\tilde{g} \times \overline{I}(\tilde{g}))$ and $\tilde{g} \to \overline{m}(\overline{I}(\tilde{g}) \times \tilde{g})$ map $\overline{G}$ to $\tilde{e}$.

(d) Show the maps $\overline{G} \times \overline{G} \times \overline{G} \to \overline{G}$ given by

$$
\tilde{g} \times \tilde{g}' \times \tilde{g}'' \to \overline{m}(\tilde{g} \times \overline{m}(\tilde{g}' \times \tilde{g}''))
$$

$$
\tilde{g} \times \tilde{g}' \times \tilde{g}'' \to \overline{m}(\overline{m}(\tilde{g} \times \tilde{g}') \times \tilde{g}'')
$$

are equal.

(e) Complete the proof.
:::
