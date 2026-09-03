---
schema: qual/card@1
id: E-AMD-E3UUQEAP
kind: problem
title: Splitting field of $x^3-2$ is $\QQ(\sqrt[3]{2},\zeta_3)$
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
  date: 2026-08-29
---

::: {.exercise}
Show that the splitting field of $f(x) = x^3-2$ over $\mathbb{Q}$ is $\mathbb{Q}(\sqrt[3]{2}, \zeta_3)$.
:::

::: solution
**Goal:** Prove that the splitting field of $f(x) = x^3 - 2 \in \mathbb{Q}[x]$ is $K = \mathbb{Q}(\sqrt[3]{2}, \zeta_3)$, where $\zeta_3 = e^{2\pi i / 3} = \frac{-1 + i\sqrt{3}}{2}$.

<1>1. Roots of $f(x)$ in $\mathbb{C}$:
    *Proof:*
    <2>1. The polynomial $x^3 - 2$ has three distinct roots in $\mathbb{C}$:
        $$\alpha_1 = \sqrt[3]{2}, \quad \alpha_2 = \sqrt[3]{2}\zeta_3, \quad \alpha_3 = \sqrt[3]{2}\zeta_3^2.$$
    <2>2. By definition, the splitting field of $f(x)$ over $\mathbb{Q}$ is the minimal field extension containing all roots:
        $$K = \mathbb{Q}(\alpha_1, \alpha_2, \alpha_3) = \mathbb{Q}(\sqrt[3]{2}, \, \sqrt[3]{2}\zeta_3, \, \sqrt[3]{2}\zeta_3^2).$$

<1>2. Proof of equality $K = \mathbb{Q}(\sqrt[3]{2}, \zeta_3)$:
    *Proof:*
    <2>1. **Inclusion $K \subseteq \mathbb{Q}(\sqrt[3]{2}, \zeta_3)$:**
        Each root $\alpha_1 = \sqrt[3]{2}$, $\alpha_2 = \sqrt[3]{2}\zeta_3$, and $\alpha_3 = \sqrt[3]{2}\zeta_3^2$ is a product of elements in $\mathbb{Q}(\sqrt[3]{2}, \zeta_3)$.
        Thus $\mathbb{Q}(\alpha_1, \alpha_2, \alpha_3) \subseteq \mathbb{Q}(\sqrt[3]{2}, \zeta_3)$.
    <2>2. **Inclusion $\mathbb{Q}(\sqrt[3]{2}, \zeta_3) \subseteq K$:**
        Since $\sqrt[3]{2} = \alpha_1 \in K$ and $\sqrt[3]{2}\zeta_3 = \alpha_2 \in K$, their quotient is in $K$:
        $$\zeta_3 = \frac{\alpha_2}{\alpha_1} = \frac{\sqrt[3]{2}\zeta_3}{\sqrt[3]{2}} \in K.$$
        Since both generators $\sqrt[3]{2}$ and $\zeta_3$ lie in $K$, we have $\mathbb{Q}(\sqrt[3]{2}, \zeta_3) \subseteq K$.

<1>3. Degree of the extension:
    *Proof:*
    <2>1. $x^3 - 2$ is irreducible over $\mathbb{Q}$ by Eisenstein's criterion at $p = 2$, so $[\mathbb{Q}(\sqrt[3]{2}) : \mathbb{Q}] = 3$.
    <2>2. The minimal polynomial of $\zeta_3$ is the cyclotomic polynomial $\Phi_3(x) = x^2 + x + 1$.
    <2>3. Since $\mathbb{Q}(\sqrt[3]{2}) \subset \mathbb{R}$ and $\zeta_3 \notin \mathbb{R}$, $\Phi_3(x)$ remains irreducible over $\mathbb{Q}(\sqrt[3]{2})$, so $[\mathbb{Q}(\sqrt[3]{2}, \zeta_3) : \mathbb{Q}(\sqrt[3]{2})] = 2$.
    <2>4. By the Tower Law:
        $$[K : \mathbb{Q}] = [\mathbb{Q}(\sqrt[3]{2}, \zeta_3) : \mathbb{Q}(\sqrt[3]{2})] \cdot [\mathbb{Q}(\sqrt[3]{2}) : \mathbb{Q}] = 2 \cdot 3 = 6.$$

<1>4. Conclusion:
    The splitting field of $x^3 - 2$ over $\mathbb{Q}$ is $\mathbb{Q}(\sqrt[3]{2}, \zeta_3)$. Q.E.D.
:::
