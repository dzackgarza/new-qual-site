---
schema: qual/card@1
id: P-67WAD
kind: problem
title: The splitting field of $x^3-2$ is $\QQ(\sqrt[3]{2},\zeta_2)$
classification:
  areas:
  - algebra
  topics:
  - Splitting Fields
  - Roots of Unity
  - Field Extensions
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
---

::: problem
Show that the splitting field of $f(x) = x^3-2$ over $\mathbb{Q}$ is $\mathbb{Q}(\sqrt[3]{2}, \zeta_3)$ (where $\zeta_3 = e^{2\pi i/3}$).
:::

::: solution
**Goal:** Prove that the splitting field of $f(x) = x^3 - 2$ over $\mathbb{Q}$ is $K = \mathbb{Q}(\sqrt[3]{2}, \zeta_3)$.

<1>1. Finding the roots of $f(x)$ in $\mathbb{C}$:
    *Proof:*
    <2>1. The polynomial $f(x) = x^3 - 2$ has three distinct roots in $\mathbb{C}$:
        $$\alpha_1 = \sqrt[3]{2}, \qquad \alpha_2 = \sqrt[3]{2} \, \zeta_3, \qquad \alpha_3 = \sqrt[3]{2} \, \zeta_3^2,$$
        where $\sqrt[3]{2} \in \mathbb{R}$ is the real cube root and $\zeta_3 = e^{2\pi i/3} = \frac{-1 + i\sqrt{3}}{2}$ is a primitive third root of unity.

<1>2. The splitting field contains $\mathbb{Q}(\sqrt[3]{2}, \zeta_3)$:
    *Proof:*
    <2>1. By definition, the splitting field $L$ of $f$ over $\mathbb{Q}$ is the smallest field containing all roots: $L = \mathbb{Q}(\alpha_1, \alpha_2, \alpha_3) = \mathbb{Q}(\sqrt[3]{2}, \sqrt[3]{2}\zeta_3, \sqrt[3]{2}\zeta_3^2)$.
    <2>2. Since $\alpha_1 = \sqrt[3]{2} \in L$, we have $\sqrt[3]{2} \in L$.
    <2>3. Since $\alpha_2 = \sqrt[3]{2}\zeta_3 \in L$ and $\sqrt[3]{2} \in L^\times$, the ratio $\frac{\alpha_2}{\alpha_1} = \zeta_3$ must also belong to $L$.
    <2>4. Thus $\mathbb{Q}(\sqrt[3]{2}, \zeta_3) \subseteq L$.

<1>3. $\mathbb{Q}(\sqrt[3]{2}, \zeta_3)$ contains all roots:
    *Proof:*
    <2>1. In the field $K = \mathbb{Q}(\sqrt[3]{2}, \zeta_3)$:
        - $\alpha_1 = \sqrt[3]{2} \in K$.
        - $\alpha_2 = \sqrt[3]{2} \cdot \zeta_3 \in K$.
        - $\alpha_3 = \sqrt[3]{2} \cdot \zeta_3^2 \in K$.
    <2>2. Thus $f(x)$ completely factors into linear factors in $K[x]$:
        $$x^3 - 2 = (x - \sqrt[3]{2})(x - \sqrt[3]{2}\zeta_3)(x - \sqrt[3]{2}\zeta_3^2).$$
    <2>3. Therefore $L \subseteq K = \mathbb{Q}(\sqrt[3]{2}, \zeta_3)$.

<1>4. Degree of the extension:
    *Proof:*
    <2>1. $[\mathbb{Q}(\sqrt[3]{2}) : \mathbb{Q}] = 3$ since $x^3 - 2$ is irreducible by Eisenstein at $p = 2$.
    <2>2. $\zeta_3 = \frac{-1 + i\sqrt{3}}{2} \notin \mathbb{R} \supset \mathbb{Q}(\sqrt[3]{2})$, and its minimal polynomial over $\mathbb{Q}$ is $\Phi_3(x) = x^2 + x + 1$.
    <2>3. Thus $[K : \mathbb{Q}(\sqrt[3]{2})] = 2$, which gives $[K : \mathbb{Q}] = 3 \cdot 2 = 6$.

<1>5. Conclusion:
    The splitting field is precisely $L = \mathbb{Q}(\sqrt[3]{2}, \zeta_3) = \mathbb{Q}(\sqrt[3]{2}, i\sqrt{3})$ of degree 6 over $\mathbb{Q}$. Q.E.D.
:::
