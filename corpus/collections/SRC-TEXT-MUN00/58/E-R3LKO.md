---
schema: qual/card@1
id: E-R3LKO
kind: problem
title: When the inclusion induces an isomorphism on fundamental groups
classification:
  areas:
  - topology
  topics:
  - Fundamental Group
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-10
---

::: {.exercise}

Let $A$ be a subspace of $X$; let $j: A \to X$ be the inclusion map, and let $f: X \to A$ be a continuous map.
Suppose there is a homotopy $H: X \times I \to X$ between the map $j \circ f$ and the identity map of $X$.

(a) Show that if $f$ is a retraction, then $j_*$ is an isomorphism.

(b) Show that if $H$ maps $A \times I$ into $A$, then $j_*$ is an isomorphism.

(c) Give an example in which $j_*$ is not an isomorphism.
:::

::: {.solution}
Let \(a_0\in A\), and use it as basepoint; put \(x_0=j(a_0)\). The homotopy \(H\) need not preserve the basepoint, so homotopic maps induce homomorphisms differing by a change-of-basepoint isomorphism. In particular, since \(jf\simeq\operatorname{id}_X\), the composite
\[
j_*f_*:\pi_1(X,x_0)\to\pi_1(X,x_0)
\]
is an automorphism (up to the canonical basepoint-change isomorphism).

(a) If \(f\) is a retraction, then \(fj=\operatorname{id}_A\), so
\[
f_*j_*=\operatorname{id}_{\pi_1(A,a_0)}.
\]
Hence \(j_*\) is injective. Since \(j_*f_*\) is an automorphism, \(j_*\) is surjective. Thus \(j_*\) is an isomorphism.

(b) If \(H(A\times I)\subset A\), then restricting \(H\) to \(A\times I\) gives a homotopy in \(A\) from \(fj:A\to A\) to \(\operatorname{id}_A\). Hence \((fj)_*=f_*j_*\) is an automorphism (again with the harmless basepoint change determined by the restricted homotopy). Thus \(j_*\) has both a left inverse up to automorphism and, from \(jf\simeq\operatorname{id}_X\), a right inverse up to automorphism. Consequently \(j_*\) is bijective, hence an isomorphism.

(c) Let \(X=D^2\), \(A=S^1=\partial D^2\), and let \(f:D^2\to S^1\) be a constant map. Then \(jf\) is constant and is homotopic to \(\operatorname{id}_{D^2}\) because \(D^2\) is contractible. But
\[
j_*:\pi_1(S^1)\cong\mathbb Z\longrightarrow\pi_1(D^2)=0
\]
is not an isomorphism.
:::
