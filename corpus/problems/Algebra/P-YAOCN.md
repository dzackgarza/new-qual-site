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
---

::: problem
Let $L/F$ be a field extension, and let $\alpha$ be algebraic over $F$.
Let $m_F(x) = \operatorname{irr}(\alpha, F) \in F[x]$ and $m_L(x) = \operatorname{irr}(\alpha, L) \in L[x]$ be the minimal polynomials of $\alpha$ over $F$ and over $L$, respectively.
Prove that $m_L(x)$ divides $m_F(x)$ in the polynomial ring $L[x]$.
:::

::: solution
**Goal:** Prove that $\operatorname{irr}(\alpha, L) \mid \operatorname{irr}(\alpha, F)$ in $L[x]$ when $F \subseteq L$.

<1>1. Polynomial Ring Containment:
    *Proof:*
    <2>1. Since $F$ is a subfield of $L$ ($F \subseteq L$), the polynomial ring $F[x]$ is naturally a subring of $L[x]$:
        $$F[x] \subseteq L[x].$$
    <2>2. The minimal polynomial $m_F(x) \in F[x]$ of $\alpha$ over $F$ is a monic polynomial in $F[x]$ satisfying $m_F(\alpha) = 0$.
    <2>3. Since $F[x] \subseteq L[x]$, we can view $m_F(x)$ as a polynomial with coefficients in $L$:
        $$m_F(x) \in L[x].$$

<1>2. Division Algorithm in $L[x]$:
    *Proof:*
    <2>1. By the Euclidean Division Algorithm in the Euclidean domain $L[x]$, divide $m_F(x)$ by the monic polynomial $m_L(x) \in L[x]$:
        $$m_F(x) = q(x) m_L(x) + r(x)$$
        where $q(x), r(x) \in L[x]$, and either $r(x) = 0$ or $\deg(r) < \deg(m_L)$.
    <2>2. Evaluate this polynomial identity at $x = \alpha$:
        $$m_F(\alpha) = q(\alpha) m_L(\alpha) + r(\alpha).$$
    <2>3. Since $m_F(\alpha) = 0$ and $m_L(\alpha) = 0$, we have:
        $$0 = q(\alpha) \cdot 0 + r(\alpha) \implies r(\alpha) = 0.$$

<1>3. Minimality of $\deg(m_L)$:
    *Proof:*
    <2>1. If $r(x) \ne 0$, then $r(x) \in L[x]$ is a non-zero polynomial having $\alpha$ as a root with $\deg(r) < \deg(m_L)$.
    <2>2. This strictly contradicts the definition of the minimal polynomial $m_L(x) = \operatorname{irr}(\alpha, L)$, which is the non-zero monic polynomial in $L[x]$ of **minimal degree** annihilating $\alpha$.
    <2>3. Therefore, $r(x)$ must be the zero polynomial:
        $$r(x) = 0.$$
    <2>4. Thus:
        $$m_F(x) = q(x) m_L(x) \in L[x].$$

<1>4. Conclusion:
    $m_L(x)$ divides $m_F(x)$ in $L[x]$ (and consequently $[L(\alpha) : L] \le [F(\alpha) : F]$). Q.E.D.
:::
