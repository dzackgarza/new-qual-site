---
schema: qual/card@1
id: P-MNR6F
kind: problem
title: $f^{-1}(f(S))=S$ for all $S$ iff $f$ is injective
classification:
  areas:
  - prelim
  topics:
  - Functions and Relations
relations: []
review: draft
---

::: problem
Let $f:X\to Y$ be a map of sets.
Give, with proof, necessary and sufficient conditions for
\[
f^{-1}(f(S))=S
\]
for every subset $S\subseteq X$.
:::

::: solution
The condition is that $f$ is injective.

For every map and every $S\subseteq X$, one has $S\subseteq f^{-1}(f(S))$.
If $f$ is injective and $x\in f^{-1}(f(S))$, then $f(x)=f(s)$ for some $s\in S$.
Injectivity gives $x=s$, so $x\in S$.
Thus equality holds.

Conversely, suppose the equality holds for every $S\subseteq X$.
If $f(a)=f(b)$, then
\[
b\in f^{-1}(f(\{a\}))=\{a\},
\]
so $b=a$.
Hence $f$ is injective.
:::
