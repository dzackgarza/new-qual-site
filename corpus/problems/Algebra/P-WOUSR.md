---
schema: qual/card@1
id: P-WOUSR
kind: problem
title: $\Out(A_4)$ is nontrivial
classification:
  areas:
  - algebra
  topics:
  - Automorphisms
  - Permutations
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

::: problem
- Show that $\Out(A_4)$ is nontrivial.
:::

::: {.solution}
Because $A_4\trianglelefteq S_4$, conjugation by the odd permutation $(12)$ restricts to an automorphism
\[
\varphi:A_4\to A_4.
\]
We show that $\varphi$ is not inner.

Suppose there were $g\in A_4$ such that
\[
(12)x(12)^{-1}=gxg^{-1}
\qquad\text{for every }x\in A_4.
\]
Then $g^{-1}(12)$ would centralize $A_4$. But
\[
C_{S_4}(A_4)\subseteq C_{S_4}((123))\cap C_{S_4}((124)).
\]
The two centralizers on the right are respectively
\[
\langle(123)\rangle
\quad\text{and}\quad
\langle(124)\rangle,
\]
whose intersection is trivial. Hence
\[
C_{S_4}(A_4)=1.
\]
Thus $g^{-1}(12)=1$, forcing $g=(12)$, impossible because $g\in A_4$.

Therefore $\varphi$ is an outer automorphism, so
\[
\boxed{\operatorname{Out}(A_4)\ne1}.
\]
:::
