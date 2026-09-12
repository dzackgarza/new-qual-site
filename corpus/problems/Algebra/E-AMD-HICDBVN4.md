---
schema: qual/card@1
id: E-AMD-HICDBVN4
kind: problem
title: $K[\alpha_1,\ldots,\alpha_n]=K(\alpha_1,\ldots,\alpha_n)$ for algebraic $\alpha_i$
classification:
  areas:
  - algebra
  topics:
  - Field Extensions
  - Rings
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09

---

::: {.exercise}
Let $F/K$ be a field extension, and let $\alpha_1,\dots,\alpha_n\in F$ be algebraic over $K$.
Show that
\[
K[\alpha_1,\dots,\alpha_n]=K(\alpha_1,\dots,\alpha_n).
\]
:::

::: solution
It is enough to prove that adjoining one algebraic element to a field already gives a field.

Let $L$ be a field and let $\alpha$ be algebraic over $L$, with minimal polynomial $m_\alpha(x)\in L[x]$. Evaluation induces an isomorphism
\[
L[x]/(m_\alpha)\cong L[\alpha].
\]
Since $m_\alpha$ is irreducible, $(m_\alpha)$ is maximal, so $L[\alpha]$ is a field. Hence
\[
L[\alpha]=L(\alpha).
\]

Apply this inductively. Starting with $K_0=K$, define
\[
K_i=K_{i-1}[\alpha_i].
\]
Each $\alpha_i$ is algebraic over $K$, hence also algebraic over the larger field $K_{i-1}$. Therefore every $K_i$ is a field, and
\[
K_i=K_{i-1}(\alpha_i).
\]
After $n$ steps,
\[
K[\alpha_1,\ldots,\alpha_n]
=K_n
=K(\alpha_1,\ldots,\alpha_n).
\]
:::
