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
---

::: {.exercise}
Show that if $L/F$ is a field extension and $\alpha$ is algebraic over $F$, then the minimal polynomial of $\alpha$ over $L$ divides the minimal polynomial of $\alpha$ over $F$ in $L[x]$.
:::

::: solution
**Goal:** Prove that for a field extension $L/F$ and an element $\alpha$ algebraic over $F$, the minimal polynomial $m_{\alpha, L}(x) \in L[x]$ divides $m_{\alpha, F}(x) \in F[x]$ in the polynomial ring $L[x]$.

<1>1. Polynomial ring inclusion and roots:
    *Proof:*
    <2>1. By definition, the minimal polynomial $m_{\alpha, F}(x)$ is a monic polynomial in $F[x]$ satisfying $m_{\alpha, F}(\alpha) = 0$.
    <2>2. Since $F \subseteq L$, there is a natural ring inclusion $F[x] \subseteq L[x]$, so $m_{\alpha, F}(x) \in L[x]$.
    <2>3. Thus $m_{\alpha, F}(x)$ is a polynomial in $L[x]$ that has $\alpha$ as a root.

<1>2. Division algorithm in $L[x]$:
    *Proof:*
    <2>1. In the Euclidean domain $L[x]$, divide $m_{\alpha, F}(x)$ by $m_{\alpha, L}(x)$:
        $$m_{\alpha, F}(x) = q(x) m_{\alpha, L}(x) + r(x),$$
        where $q(x), r(x) \in L[x]$ and either $r(x) = 0$ or $\deg(r) < \deg(m_{\alpha, L})$.
    <2>2. Evaluating both sides at $x = \alpha$:
        $$0 = m_{\alpha, F}(\alpha) = q(\alpha) m_{\alpha, L}(\alpha) + r(\alpha) = q(\alpha) \cdot 0 + r(\alpha) = r(\alpha).$$
    <2>3. Thus $r(\alpha) = 0$.

<1>3. Minimality contradiction forces $r(x) = 0$:
    *Proof:*
    <2>1. Suppose for contradiction that $r(x) \neq 0$.
    <2>2. Then $r(x) \in L[x]$ is a non-zero polynomial with $r(\alpha) = 0$ and $\deg(r) < \deg(m_{\alpha, L})$.
    <2>3. This contradicts the definition of $m_{\alpha, L}(x)$ as the non-zero polynomial in $L[x]$ of minimal degree having $\alpha$ as a root.
    <2>4. Therefore $r(x) = 0$.

<1>4. Conclusion:
    $m_{\alpha, F}(x) = q(x) m_{\alpha, L}(x)$, so $m_{\alpha, L}(x) \mid m_{\alpha, F}(x)$ in $L[x]$. Q.E.D.
:::
