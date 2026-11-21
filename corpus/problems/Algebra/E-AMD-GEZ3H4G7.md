---
schema: qual/card@1
id: E-AMD-GEZ3H4G7
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
  date: 2026-08-29
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Structured the card's prose proof into numbered steps and re-checked each: that m_{alpha,F}
    lies in L[x] and makes alpha algebraic over L, the division with remainder in L[x], the
    evaluation at alpha, and the appeal to minimality. Nothing was changed mathematically. Not
    checked against a printed source: no AmD solution set is retained in tmp/sources and the card
    records no page. The argument remains the card's own.
---

::: {.exercise}
Let $F\subseteq L\subseteq\Omega$ be fields and let $\alpha\in\Omega$ be algebraic over $F$. Show that the minimal polynomial of $\alpha$ over $L$ divides the minimal polynomial of $\alpha$ over $F$ in $L[x]$.
:::

::: {.solution}

The argument is the card's own: no solution set for this source is retained in `tmp/sources`, so nothing below is transcribed, and the card's existing solution is restructured into numbered steps. Here $F\subseteq L\subseteq\Omega$ are fields, $\alpha\in\Omega$ is algebraic over $F$, and $m_{\alpha,K}$ is the monic minimal polynomial of $\alpha$ over a field $K$; $L[x]$ is a principal ideal domain, so division with remainder is available.

::: pf

::: {.pf-step #alg}

$\alpha$ is algebraic over $L$.

::: pf-proof

$m_{\alpha,F}\in F[x]\subseteq L[x]$ is monic, nonzero and annihilates $\alpha$, so $\alpha$ is a root of a nonzero polynomial over $L$.

:::

:::

::: {.pf-step #div}

Divide: $m_{\alpha,F}=q\,m_{\alpha,L}+r$ in $L[x]$ with $\deg r<\deg m_{\alpha,L}$.

::: pf-proof

Division with remainder by the monic polynomial $m_{\alpha,L}$ in the polynomial ring over the field $L$.

:::

:::

::: {.pf-step #eval}

$r(\alpha)=0$.

::: pf-proof

$m_{\alpha,F}(\alpha)=0$ and $m_{\alpha,L}(\alpha)=0$, so $r(\alpha)=m_{\alpha,F}(\alpha)-q(\alpha)m_{\alpha,L}(\alpha)=0$.

:::

:::

::: {.pf-step #zero}

$r=0$.

::: pf-proof

By minimality of $m_{\alpha,L}$ over $L$ no nonzero polynomial over $L$ of degree below $\deg m_{\alpha,L}$ vanishes at $\alpha$; $r$ has smaller degree and vanishes at $\alpha$ by step [](#eval){.pf-ref}, so $r$ is the zero polynomial.

:::

:::

::: {.pf-step #done}

$m_{\alpha,L}$ divides $m_{\alpha,F}$ in $L[x]$.

::: pf-proof

Step [](#div){.pf-ref} with $r=0$ by step [](#zero){.pf-ref}.

:::

:::

:::

:::
