---
schema: qual/card@1
id: P-TLYR4
kind: problem
title: Finite-dimensional division algebras over $\RR$
classification:
  areas:
  - algebra
  topics:
  - Algebras
  - Semisimplicity
  - Classification
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
---

::: {.problem}
Classify all finite-dimensional (associative) **division algebras** over the field of real numbers $\mathbb{R}$ (Frobenius' Theorem).
:::

::: {.solution}
**Frobenius' theorem.** Every finite-dimensional associative division algebra over $\mathbb R$ is isomorphic to exactly one of
\[
\mathbb R,\qquad \mathbb C,\qquad \mathbb H.
\]

One standard proof uses the Brauer group. Let $D$ be such a division algebra and let $Z=Z(D)$. The center is a finite field extension of $\mathbb R$, hence
\[
Z\cong\mathbb R\quad\text{or}\quad Z\cong\mathbb C.
\]
If $Z=\mathbb C$, then $D=\mathbb C$: for any $x\in D$, the finite-dimensional commutative subalgebra $\mathbb C[x]$ is a field, so the minimal polynomial of $x$ over the algebraically closed field $\mathbb C$ must be linear.

It remains to consider central division algebras over $\mathbb R$. The standard computation
\[
\operatorname{Br}(\mathbb R)\cong\mathbb Z/2\mathbb Z
\]
has two classes, represented by $\mathbb R$ and the Hamilton quaternion algebra $\mathbb H$. Every central simple algebra over $\mathbb R$ is therefore Morita-equivalent to one of these; its division-algebra representative is respectively $\mathbb R$ or $\mathbb H$. Hence a noncommutative finite-dimensional real division algebra is $\mathbb H$.

Thus the complete list is
\[
\boxed{\mathbb R,\ \mathbb C,\ \mathbb H}.
\]
:::
