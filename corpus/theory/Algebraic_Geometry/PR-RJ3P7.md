---
schema: qual/card@1
id: PR-RJ3P7
kind: proposition
title: Going up and going down, read on spectra
slogan: 'Integral extensions lift ascending prime chains; integrally closed-domain or flat hypotheses also lift descending chains.'
classification:
  areas:
  - algebraic-geometry
  - algebra
  topics:
  - Going Up
  - Finite Morphisms
  - Flatness
  - Integral Extensions
  - Prime Ideals
relations:
- kind: uses
  target: D-VKR54
review: draft
prompts:
- What is the going up theorem?
- What does the going up theorem mean in algebraic geometry?
- What does going down mean geometrically?
---

::: {.theorem title="Lying over and going up"}
Let $\phi: A \to B$ be a ring map with $B$ integral over $\phi(A)$, and $f: \Spec B \to \Spec A$ the induced map, $f(\mfq) = \phi^{-1}(\mfq)$.

- (Lying over) If $\phi$ is injective, then for every prime $\mfp \subseteq A$ there is a prime $\mfq \subseteq B$ with $\phi^{-1}(\mfq) = \mfp$; so $f$ is surjective.

- (Going up) If $\mfp_1 \subseteq \cdots \subseteq \mfp_n$ is a chain of primes of $A$ and $\mfq_1 \subseteq \cdots \subseteq \mfq_m$, $m < n$, is a chain of primes of $B$ with $\phi^{-1}(\mfq_i) = \mfp_i$, then it extends to a chain $\mfq_1 \subseteq \cdots \subseteq \mfq_n$ with $\phi^{-1}(\mfq_i) = \mfp_i$ for all $i$.

An integral morphism is affine and universally closed, so $f$ is closed (Stacks Project, Lemma 29.45.7, tag 01WM); it is finite when each such $B$ is a finite $\phi(A)$-module (Stacks Project, Definition 29.45.1, tag 01WH).
[@AM18, Theorems 5.10 and 5.11]
:::

::: {.theorem title="Going down"}
Let $A \subseteq B$ be domains with $A$ integrally closed and $B$ integral over $A$.
If $\mfp_1 \supseteq \cdots \supseteq \mfp_n$ is a chain of primes of $A$ and $\mfq_1 \supseteq \cdots \supseteq \mfq_m$, $m < n$, is a chain of primes of $B$ with $\mfq_i \cap A = \mfp_i$, then it extends to a chain $\mfq_1 \supseteq \cdots \supseteq \mfq_n$ with $\mfq_i \cap A = \mfp_i$ [@AM18, Theorem 5.16].
Going down also holds for every flat ring map $A \to B$ (Stacks Project, Lemma 10.39.19, tag 00HS).
:::

::: {.remark}
Going up says that a chain of primes of $A$ ascending from a prime in the image of $f$ lifts to $B$; this is what makes $f(V(\mfq)) = V(\phi^{-1}(\mfq))$, so the image of a closed set is closed, and going up is the algebraic form of the closedness of an integral morphism (Stacks Project, Lemma 29.45.7, tag 01WM).

Surjectivity is not part of that: it is lying over, and it needs $\phi$ injective. Without injectivity $f$ can miss points — the finite ring map $\ZZ\to\ZZ/2$ gives $\Spec\ZZ/2\to\Spec\ZZ$, which misses the generic point, although every finite morphism is closed and has finite fibres.

The dimension statement is separate again, and it is about an extension of rings rather than about an arbitrary finite map: going up together with incomparability makes $\dim B = \dim A$ for an integral extension $A\subseteq B$, so an integral morphism has the dimension of its image; a finite morphism need not preserve the dimension of its target, the same $\ZZ\to\ZZ/2$ having dimension $1$ below and $0$ above.

Going down is what makes heights match, $\operatorname{ht} \mfq = \operatorname{ht}(\mfq \cap A)$, under its hypotheses: geometrically, every generization of $f(\mfq)$ in $\Spec A$ lifts to a generization of $\mfq$.
:::
