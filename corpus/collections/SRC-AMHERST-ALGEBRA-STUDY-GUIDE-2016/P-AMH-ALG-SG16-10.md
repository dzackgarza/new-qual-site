---
schema: qual/card@1
id: P-AMH-ALG-SG16-10
kind: problem
title: Cosets of the preimage of a subgroup under a homomorphism
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
(March 2015) Let $G_1,G_2$ be groups, let $H_2\subseteq G_2$ be a subgroup, and let $\varphi:G_1\to G_2$ be a homomorphism.
Define
\[
H_1=\{x\in G_1\mid \varphi(x)\in H_2\}.
\]
It is a fact, which you may assume, that $H_1$ is a subgroup of $G_1$.
Prove that for any $x,y\in G_1$, $H_1x=H_1y$ if and only if $H_2\varphi(x)=H_2\varphi(y)$.
:::

::: {.solution}
Proof.
(=⇒) Given x,y ∈G1 such that H1x =H1y, we have xy−1∈H1 [by the right coset relation for H1]. So φ(x)φ(y)−1 =φ ( xy−1) ∈H2, by deﬁnition of H1. Thus, [by the right coset relation for H2], we have H2φ(x) =H2φ(y). (⇐=) Given x,y ∈ G1 such that H2φ(x) = H2φ(y), we have φ(x)φ(y)−1∈ H2 [by the right coset relation for H2]. Thus, φ ( xy−1) =φ(x)φ(y)−1∈H2, and therefore xy−1∈ H1, by deﬁnition of H1. Thus, [by the right coset relation for H1], we have H1x =H1y. QED
:::
