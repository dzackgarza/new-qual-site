---
schema: qual/card@1
id: P-YAOCN
kind: problem
title: The minimal polynomial over $L$ divides the minimal polynomial over $F$
classification:
  areas:
  - algebra
  topics:
  - Field Extensions
  - Polynomials
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
Let $L/F$ be a field extension, and let $\alpha$ be algebraic over $F$.
Let $m_F(x) = \irr(\alpha, F) \in F[x]$ and $m_L(x) = \irr(\alpha, L) \in L[x]$ be the minimal polynomials of $\alpha$ over $F$ and over $L$, respectively.
Prove that $m_L(x)$ divides $m_F(x)$ in the polynomial ring $L[x]$.
:::

::: {.solution}

::: pf

::: pf-step
$m_L(x)\mid m_F(x)$ in $L[x]$.

::: pf-proof
Since $F\subseteq L$, the polynomial $m_F$ lies in $L[x]$.
Divide in $L[x]$: $m_F=qm_L+r$ with $r=0$ or $\deg r<\deg m_L$.
Evaluating at $\alpha$ gives $0=q(\alpha)m_L(\alpha)+r(\alpha)=r(\alpha)$.
If $r\ne0$, it would be a nonzero polynomial in $L[x]$ of smaller degree than $m_L$ vanishing at $\alpha$, contradicting minimality of $m_L$.
So $r=0$.
:::

:::

:::

:::
