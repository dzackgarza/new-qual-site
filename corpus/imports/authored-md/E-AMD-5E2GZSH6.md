---
schema: qual/card@1
id: E-AMD-5E2GZSH6
kind: exercise
title: Prove Burnside's theorem.
classification:
  areas:
  - algebra
  topics:
  - burnside-s-lemma
  - group-actions
relations: []
review: draft
---

::: {.exercise}
Prove Burnside's Orbit-Counting Lemma: If a finite group $G$ acts on a finite set $X$, then the number of orbits $|X/G|$ is given by:
$$
|X/G| = \frac{1}{|G|} \sum_{g \in G} |X^g|,
$$
where $X^g = \{x \in X \mid g \cdot x = x\}$ is the fixed point set of $g$.
:::

::: {.solution}
> **AI-Generated Solution** (Gemini 3.7 Flash)

Let $G$ be a finite group acting on a finite set $X$.
We count the cardinality of the set of fixed pairs:
$$
S = \{ (g, x) \in G \times X \mid g \cdot x = x \}
$$
in two different ways (double counting).

1. **Summing over group elements $g \in G$:**
   For a fixed $g \in G$, the number of elements $x \in X$ such that $(g, x) \in S$ is precisely the number of fixed points $|X^g|$.
   Therefore:
   $$
   |S| = \sum_{g \in G} |X^g|.
   $$

2. **Summing over set elements $x \in X$:**
   For a fixed $x \in X$, the number of elements $g \in G$ such that $(g, x) \in S$ is precisely the order of the stabilizer subgroup $|G_x|$.
   Therefore:
   $$
   |S| = \sum_{x \in X} |G_x|.
   $$

3. **Partitioning $X$ into Orbits:**
   Equating the two expressions for $|S|$:
   $$
   \sum_{g \in G} |X^g| = \sum_{x \in X} |G_x|.
   $$
   Let $\mathcal{O}_1, \mathcal{O}_2, \ldots, \mathcal{O}_k$ be the disjoint orbits of the action of $G$ on $X$, so $X = \bigsqcup_{i=1}^k \mathcal{O}_i$, with $k = |X/G|$.
   For each orbit $\mathcal{O}_i$ and each $x \in \mathcal{O}_i$, the Orbit-Stabilizer Theorem gives:
   $$
   |\mathcal{O}_i| = [G : G_x] = \frac{|G|}{|G_x|} \implies |G_x| = \frac{|G|}{|\mathcal{O}_i|}.
   $$
   Summing over all elements in the orbit $\mathcal{O}_i$:
   $$
   \sum_{x \in \mathcal{O}_i} |G_x| = \sum_{x \in \mathcal{O}_i} \frac{|G|}{|\mathcal{O}_i|} = |\mathcal{O}_i| \cdot \frac{|G|}{|\mathcal{O}_i|} = |G|.
   $$
   Summing across all $k$ orbits:
   $$
   \sum_{x \in X} |G_x| = \sum_{i=1}^k \left( \sum_{x \in \mathcal{O}_i} |G_x| \right) = \sum_{i=1}^k |G| = k \cdot |G| = |X/G| \cdot |G|.
   $$

4. **Conclusion:**
   Substituting back into the double counting equality:
   $$
   \sum_{g \in G} |X^g| = |X/G| \cdot |G|.
   $$
   Dividing both sides by $|G|$:
   $$
   |X/G| = \frac{1}{|G|} \sum_{g \in G} |X^g|.
   $$
:::
