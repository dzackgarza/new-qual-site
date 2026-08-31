---
schema: qual/card@1
id: P-NNNLA
kind: problem
title: Degree of $\QQ(\zeta_8)$, its quadratic subfields, and $[\QQ(\zeta_8,\sqrt[4]{2}):\QQ]$
classification:
  areas:
  - algebra
  topics:
  - Roots of Unity
  - Field Extensions
  - Galois Theory
relations: []
review: draft
---

::: problem
Let $\zeta = e^{2\pi i / 8}$ be a primitive $8$-th root of unity in $\mathbb{C}$.

(a) What is the degree $[\mathbb{Q}(\zeta) : \mathbb{Q}]$?

(b) How many quadratic subfields of $\mathbb{Q}(\zeta)$ are there? List them with justification.

(c) What is the degree $[\mathbb{Q}(\zeta, \sqrt[4]{2}) : \mathbb{Q}]$?
:::

::: solution
**Goal:** Compute the cyclotomic extension degree in (a), classify its quadratic subfields via Galois correspondence in (b), and compute the field degree of $\mathbb{Q}(\zeta, \sqrt[4]{2})/\mathbb{Q}$ in (c).

<1>1. Part (a): Degree $[\mathbb{Q}(\zeta) : \mathbb{Q}] = 4$.
    *Proof:*
    <2>1. The element $\zeta = e^{2\pi i / 8}$ is a primitive $8$-th root of unity.
    <2>2. The minimal polynomial of $\zeta$ over $\mathbb{Q}$ is the $8$-th cyclotomic polynomial:
    $$\Phi_8(x) = \frac{x^8 - 1}{x^4 - 1} = x^4 + 1.$$
    <2>3. $\Phi_8(x)$ is irreducible over $\mathbb{Q}$ (for instance, $\Phi_8(x+1) = x^4 + 4x^3 + 6x^2 + 4x + 2$ is irreducible by Eisenstein's criterion at $p = 2$).
    <2>4. Therefore $[\mathbb{Q}(\zeta) : \mathbb{Q}] = \deg \Phi_8(x) = \varphi(8) = 8(1 - 1/2) = 4$.

<1>2. Part (b): There are exactly 3 quadratic subfields of $\mathbb{Q}(\zeta)$.
    *Proof:*
    <2>1. The extension $\mathbb{Q}(\zeta)/\mathbb{Q}$ is Galois, with Galois group isomorphic to the unit group $(\mathbb{Z}/8\mathbb{Z})^\times$:
    $$\operatorname{Gal}(\mathbb{Q}(\zeta)/\mathbb{Q}) \cong (\mathbb{Z}/8\mathbb{Z})^\times = \{1, 3, 5, 7\} \cong \mathbb{Z}/2\mathbb{Z} \times \mathbb{Z}/2\mathbb{Z},$$
    which is the Klein four-group $V_4$.
    <2>2. By the Fundamental Theorem of Galois Theory, intermediate fields $E$ with $[E : \mathbb{Q}] = 2$ correspond bijectively to subgroups $H \le \operatorname{Gal}(\mathbb{Q}(\zeta)/\mathbb{Q})$ of index 2 (which are subgroups of order 2).
    <2>3. The group $\mathbb{Z}/2\mathbb{Z} \times \mathbb{Z}/2\mathbb{Z}$ has exactly three subgroups of order 2:
    $$H_1 = \langle 3 \rangle, \qquad H_2 = \langle 5 \rangle, \qquad H_3 = \langle 7 \rangle.$$
    <2>4. Compute the fixed fields:
        - Note $\zeta = \cos(\pi/4) + i \sin(\pi/4) = \frac{\sqrt{2}}{2}(1 + i)$.
        - Then $\zeta^2 = i$, so $\mathbb{Q}(i) \subset \mathbb{Q}(\zeta)$ is a quadratic subfield.
        - $\zeta + \zeta^{-1} = \frac{\sqrt{2}}{2}(1 + i) + \frac{\sqrt{2}}{2}(1 - i) = \sqrt{2}$, so $\mathbb{Q}(\sqrt{2}) \subset \mathbb{Q}(\zeta)$ is a quadratic subfield.
        - $\zeta - \zeta^{-1} = \frac{\sqrt{2}}{2}(1 + i) - \frac{\sqrt{2}}{2}(1 - i) = i \sqrt{2} = \sqrt{-2}$, so $\mathbb{Q}(\sqrt{-2}) \subset \mathbb{Q}(\zeta)$ is a quadratic subfield.
    <2>5. The three distinct quadratic subfields are $\mathbb{Q}(i)$, $\mathbb{Q}(\sqrt{2})$, and $\mathbb{Q}(\sqrt{-2})$.

<1>3. Part (c): $[\mathbb{Q}(\zeta, \sqrt[4]{2}) : \mathbb{Q}] = 8$.
    *Proof:*
    <2>1. From <1>2, $\mathbb{Q}(\zeta) = \mathbb{Q}(i, \sqrt{2})$.
    <2>2. Since $(\sqrt[4]{2})^2 = \sqrt{2}$, we have $\mathbb{Q}(\sqrt{2}) \subseteq \mathbb{Q}(\sqrt[4]{2})$.
    <2>3. Therefore, adjoining $\sqrt[4]{2}$ to $\mathbb{Q}(\zeta) = \mathbb{Q}(i, \sqrt{2})$ gives
    $$\mathbb{Q}(\zeta, \sqrt[4]{2}) = \mathbb{Q}(i, \sqrt{2}, \sqrt[4]{2}) = \mathbb{Q}(i, \sqrt[4]{2}).$$
    <2>4. The polynomial $x^4 - 2 \in \mathbb{Q}[x]$ is irreducible over $\mathbb{Q}$ by Eisenstein at $p = 2$, so $[\mathbb{Q}(\sqrt[4]{2}) : \mathbb{Q}] = 4$.
    <2>5. The field $\mathbb{Q}(\sqrt[4]{2})$ is a subfield of $\mathbb{R}$.
    <2>6. Since $i \notin \mathbb{R}$, $i \notin \mathbb{Q}(\sqrt[4]{2})$.
    <2>7. The minimal polynomial of $i$ over $\mathbb{Q}(\sqrt[4]{2})$ is $x^2 + 1$, which has degree 2.
    <2>8. Thus $[\mathbb{Q}(i, \sqrt[4]{2}) : \mathbb{Q}(\sqrt[4]{2})] = 2$.
    <2>9. By the Tower Law of extension degrees:
    $$[\mathbb{Q}(\zeta, \sqrt[4]{2}) : \mathbb{Q}] = [\mathbb{Q}(i, \sqrt[4]{2}) : \mathbb{Q}(\sqrt[4]{2})] \cdot [\mathbb{Q}(\sqrt[4]{2}) : \mathbb{Q}] = 2 \cdot 4 = 8.$$

<1>4. Conclusion:
    *Proof:*
    $[\mathbb{Q}(\zeta) : \mathbb{Q}] = 4$, there are 3 quadratic subfields, and $[\mathbb{Q}(\zeta, \sqrt[4]{2}) : \mathbb{Q}] = 8$.
:::


