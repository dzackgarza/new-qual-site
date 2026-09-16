---
schema: qual/card@1
id: PR-RJ3P7
kind: proposition
title: Going up and going down, read on spectra
classification:
  areas:
  - algebraic-geometry
  topics:
  - Going Up
  - Finite Morphisms
  - Flatness
relations:
- kind: uses
  target: D-VKR54
review: draft
prompts:
- What does the going up theorem mean in algebraic geometry?
- What does going down mean geometrically?
---

::: {.theorem title="Lying over and going up"}
Let $\phi: A \to B$ be a ring map with $B$ integral over $\phi(A)$, and $f: \Spec B \to \Spec A$ the induced map, $f(\mfq) = \phi^{-1}(\mfq)$.

- (Lying over) If $\phi$ is injective, then for every prime $\mfp \subseteq A$ there is a prime $\mfq \subseteq B$ with $\phi^{-1}(\mfq) = \mfp$; so $f$ is surjective.
- (Going up) If $\mfp_1 \subseteq \cdots \subseteq \mfp_n$ is a chain of primes of $A$ and $\mfq_1 \subseteq \cdots \subseteq \mfq_m$, $m < n$, is a chain of primes of $B$ with $\phi^{-1}(\mfq_i) = \mfp_i$, then it extends to a chain $\mfq_1 \subseteq \cdots \subseteq \mfq_n$ with $\phi^{-1}(\mfq_i) = \mfp_i$ for all $i$.

In particular $f$ is a closed map.
[@AM18]
:::

::: {.theorem title="Going down"}
Let $A \subseteq B$ be domains with $A$ integrally closed and $B$ integral over $A$.
If $\mfp_1 \supseteq \cdots \supseteq \mfp_n$ is a chain of primes of $A$ and $\mfq_1 \supseteq \cdots \supseteq \mfq_m$, $m < n$, is a chain of primes of $B$ with $\mfq_i \cap A = \mfp_i$, then it extends to a chain $\mfq_1 \supseteq \cdots \supseteq \mfq_n$ with $\mfq_i \cap A = \mfp_i$.
Going down also holds for every flat ring map $A \to B$.
[@AM18]
:::

::: {.remark}
The translation is the content of the answer: going up says that a chain of primes in $A$ ascending from one that is hit can be lifted, which is exactly the statement that the image of a closed set is closed.
So going up is the algebraic form of "a finite morphism is closed", hence of "a finite morphism is proper".

Going up together with incomparability makes $\dim B = \dim A$ for an integral extension, which is why a finite surjective morphism cannot drop dimension.
Going down is what makes heights match, $\operatorname{ht} \mfq = \operatorname{ht}(\mfq \cap A)$, under its hypotheses: geometrically, every generization of $f(\mfq)$ in $\Spec A$ lifts to a generization of $\mfq$.

The two are the reason finite morphisms behave like branched covers: closed, surjective, with finite fibres, and preserving dimension.
:::
