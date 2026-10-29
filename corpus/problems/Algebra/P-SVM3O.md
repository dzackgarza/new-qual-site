---
schema: qual/card@1
id: P-SVM3O
kind: problem
title: The order of an element divides the order of the group
classification:
  areas:
  - algebra
  topics:
  - Cosets and Lagrange
  - Cyclic Groups
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
Let $G$ be a finite group and let $g \in G$. Prove that the order of $g$, denoted $\operatorname{ord}(g)$, divides the order of the group $|G|$.
:::

::: {.solution}

::: pf

::: {.pf-step #cyclic}

$\abs{\langle g\rangle}=\operatorname{ord}(g)$.

::: pf-proof

Let $n=\operatorname{ord}(g)$, which is finite because $G$ is finite. The elements $e,g,\ldots,g^{n-1}$ are distinct, since $g^i=g^j$ with $0\le i<j<n$ would give $g^{j-i}=e$ with $0<j-i<n$. Every power $g^k$ equals $g^r$ where $r$ is the remainder of $k$ modulo $n$. So $\langle g\rangle=\{e,g,\ldots,g^{n-1}\}$ has $n$ elements.

:::

:::

::: pf-qed

By Lagrange's theorem, $\abs{G}=[G:\langle g\rangle]\,\abs{\langle g\rangle}$, so step [](#cyclic){.pf-ref} gives $\operatorname{ord}(g)\mid\abs{G}$. In particular $g^{\abs{G}}=e$.

:::

:::

:::
