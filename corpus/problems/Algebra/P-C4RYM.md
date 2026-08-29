---
schema: qual/card@1
id: P-C4RYM
kind: problem
title: Burnside's lemma
classification:
  areas:
  - algebra
  topics:
  - Burnside's Lemma
  - Group Actions
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

::: problem
- Prove Burnside's theorem.
:::

::: {.solution}
**Goal.** Prove Burnside's lemma: the number of orbits of a finite group $G$ acting on a finite set $X$ is $\frac{1}{|G|}\sum_{g \in G} |X^g|$, where $X^g = \theset{x \in X : gx = x}$.

<1>1. Count the set $S = \theset{(g, x) \in G \times X : gx = x}$ in two ways.
<2>1. $\sum_{g \in G} |X^g| = |S|$.
Proof: for each $g$, the number of $x$ with $gx = x$ is $|X^g|$.
<2>2. $\sum_{x \in X} |G_x| = |S|$, where $G_x$ is the stabilizer of $x$.
Proof: for each $x$, the number of $g$ with $gx = x$ is $|G_x|$.
<2>3. Hence $\sum_{g \in G} |X^g| = \sum_{x \in X} |G_x|$.
Proof: both equal $|S|$.

<1>2. Relate $|G_x|$ to the orbit size.
<2>1. $|G| = |G_x| \cdot |\operatorname{Orb}(x)|$.
Proof: the orbit-stabilizer theorem.
<2>2. Hence $|G_x| = |G| / |\operatorname{Orb}(x)|$.
Proof: rearrange.

<1>3. Sum over orbits.
<2>1. $\sum_{x \in X} |G_x| = \sum_{x \in X} \frac{|G|}{|\operatorname{Orb}(x)|}$.
Proof: by <1>2.2. <2>2. Group the sum by orbits: for an orbit $O$, each $x \in O$ contributes $|G|/|O|$, and there are $|O|$ such $x$, so the orbit contributes $|G|$.
Proof: $\sum_{x \in O} |G|/|O| = |O| \cdot |G|/|O| = |G|$.
<2>3. Hence $\sum_{x \in X} |G_x| = |G| \cdot (\text{number of orbits})$.
Proof: each orbit contributes $|G|$.

<1>4. Combine.
<2>1. $\sum_{g \in G} |X^g| = |G| \cdot (\text{number of orbits})$.
Proof: <1>1.3 and <1>3.3. <2>2. Hence the number of orbits is $\frac{1}{|G|}\sum_{g \in G} |X^g|$.
Proof: divide by $|G|$.

<1>5. Q.E.D. Proof: <1>4.2 is Burnside's lemma.
:::
