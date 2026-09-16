---
schema: qual/card@1
id: P-VGFA7
kind: problem
title: Homomorphisms from $S_n$ to a group of odd order
classification:
  areas:
  - algebra
  topics:
  - Permutations
  - Homomorphisms
  - Normal Subgroups
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
Let $n \ge 2$, and let $G$ be a finite group of odd order $|G| = m$.
Let $\phi: S_n \to G$ be a group homomorphism.
(1) Prove that if $\tau \in S_n$ is a transposition, then $\tau \in \ker\phi$.
(2) Prove that $\phi$ is the trivial homomorphism ($\ker\phi = S_n$).
(3) Does this result depend on whether $n$ is even or odd?
:::

::: {.solution}
Let $\tau\in S_n$ be a transposition. Since $\tau^2=1$,
\[
\phi(\tau)^2=1.
\]
Thus the order of $\phi(\tau)$ divides $2$. It also divides $|G|$, which is odd. Hence
\[
\operatorname{ord}(\phi(\tau))=1,
\]
so $\phi(\tau)=1$ and every transposition lies in $\ker\phi$.

Transpositions generate $S_n$. Therefore
\[
\ker\phi=S_n,
\]
and $\phi$ is trivial.

The parity of $n$ plays no role; the argument works for every $n\ge2$.
:::
