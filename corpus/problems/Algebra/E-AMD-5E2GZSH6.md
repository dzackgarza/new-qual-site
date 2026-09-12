---
schema: qual/card@1
id: E-AMD-5E2GZSH6
kind: problem
title: Burnside's theorem
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
  date: 2026-08-16
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
---

::: {.exercise}
Prove Burnside's Orbit-Counting Lemma: If a finite group $G$ acts on a finite set $X$, then the number of orbits $|X/G|$ is given by:
$$
|X/G| = \frac{1}{|G|} \sum_{g \in G} |X^g|,
$$
where $X^g = \{x \in X \mid g \cdot x = x\}$ is the fixed point set of $g$.
:::

::: {.solution}
Let
\[
S=\{(g,x)\in G\times X:g\cdot x=x\}.
\]
We count \(|S|\) in two ways.

For fixed \(g\in G\), the admissible \(x\) are exactly \(X^g\), so
\[
|S|=\sum_{g\in G}|X^g|.
\]
For fixed \(x\in X\), the admissible \(g\) are exactly the stabilizer \(G_x\), so
\[
|S|=\sum_{x\in X}|G_x|.
\]

Now sum the second expression orbit by orbit. If \(\mathcal O\) is an orbit and \(x\in\mathcal O\), then orbit-stabilizer gives
\[
|G_x|=\frac{|G|}{|\mathcal O|}.
\]
Hence
\[
\sum_{x\in\mathcal O}|G_x|
=|\mathcal O|\frac{|G|}{|\mathcal O|}
=|G|.
\]
There are \(|X/G|\) orbits, so
\[
\sum_{x\in X}|G_x|=|G|\,|X/G|.
\]
Combining the two counts yields
\[
\boxed{|X/G|=\frac1{|G|}\sum_{g\in G}|X^g|}.
\]
:::
