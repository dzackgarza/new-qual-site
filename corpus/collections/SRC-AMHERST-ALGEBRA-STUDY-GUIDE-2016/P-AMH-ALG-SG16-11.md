---
schema: qual/card@1
id: P-AMH-ALG-SG16-11
kind: problem
title: Amherst algebra study guide problem 11
classification:
  areas:
  - algebra
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against the vendored Amherst College Study Guide for Algebra (September 2016).
---

::: {.problem}
(February 2013) Let $G_1$ and $G_2$ be groups, let $\varphi:G_1\to G_2$ be a homomorphism, and let $H_1\subseteq G_1$ be a subgroup.
Recall that the set
\[
H_2=\{\varphi(x)\mid x\in H_1\}
\]
is a subgroup of $G_2$, called the image of $H_1$ under $\varphi$, sometimes notated $\varphi(H_1)$.
If $G_1$ is finite, prove that $|H_2|\mid |G_1|$.
That is, prove that the order of $H_2$ divides the order of $G_1$.
:::

::: {.solution}
Proof.
Let K = Ker(φ) denote the kernel of φ. Then: • φ(G1)∼=G1/K by the fundamental theorem of group homomorphisms, so |φ(G1)| =|G1/K|. • We also know that|G1/K| =|G1|/|K|. Together, these two facts yield (1) |φ(G1)|·| K| =|G1|, and hence|φ(G1)| ⏐⏐⏐|G1| We also observe the following about H1 and H2: • Since H1⊆G1, we have H2 =φ(H1)⊆φ(G1). • By Lagrange’s Theorem, it follows that |H2| divides|φ(G1)|. Since|H2| divides|φ(G1)| by the last bullet, and |φ(G1)| divides|G1| by (1), it follows that |H2| divides|G1|. QED
:::
