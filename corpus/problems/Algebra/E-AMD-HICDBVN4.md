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
- event: source-checked
  by: claude
  date: 2026-11-06
  note: >-
    Read against the printed exercise, Hungerford, Algebra (1974), section V.1,
    exercise 4(d), book page 241: "(d) If each u_i is algebraic over K, then
    K(u_1, ..., u_n) = K[u_1, ..., u_n]." The card states exactly this part,
    which is the part the collection lists. The proof was checked: for α
    algebraic over a field L with minimal polynomial m_α, evaluation gives
    L[x]/(m_α) ≅ L[α], and since m_α is irreducible the ideal is maximal, so
    L[α] is a field and equals L(α); adjoining the α_i one at a time, each
    remains algebraic over the larger field because its minimal polynomial over
    K is still available there; and K[u_1, ..., u_n] is the iterated simple
    extension ring. Complete; no defect. The card claims only part (d); parts
    (a), (b), (c) of the same exercise are not claimed.
---

---

::: {.exercise}
Let $F/K$ be a field extension, and let $\alpha_1,\dots,\alpha_n\in F$ be algebraic over $K$.
Show that
$$
K[\alpha_1,\dots,\alpha_n]=K(\alpha_1,\dots,\alpha_n).
$$
:::

::: {.solution}
It is enough to prove that adjoining one algebraic element to a field already gives a field.

Let $L$ be a field and let $\alpha$ be algebraic over $L$, with minimal polynomial $m_\alpha(x)\in L[x]$. Evaluation induces an isomorphism
$$
L[x]/(m_\alpha)\cong L[\alpha].
$$
Since $m_\alpha$ is irreducible, $(m_\alpha)$ is maximal, so $L[\alpha]$ is a field. Hence
$$
L[\alpha]=L(\alpha).
$$

Apply this inductively. Starting with $K_0=K$, define
$$
K_i=K_{i-1}[\alpha_i].
$$
Each $\alpha_i$ is algebraic over $K$, hence also algebraic over the larger field $K_{i-1}$. Therefore every $K_i$ is a field, and
$$
K_i=K_{i-1}(\alpha_i).
$$
After $n$ steps,
$$
K[\alpha_1,\ldots,\alpha_n]
=K_n
=K(\alpha_1,\ldots,\alpha_n).
$$
:::
