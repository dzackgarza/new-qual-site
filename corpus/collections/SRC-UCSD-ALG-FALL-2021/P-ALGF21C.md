---
schema: qual/card@1
id: P-ALGF21C
kind: problem
title: $\sqrt[3]{2}$ not in a cyclotomic field $\mathbb{Q}(\zeta_n)$
classification:
  areas:
  - algebra
  topics:
  - Galois Theory
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
---

::: problem
Let $\zeta \in \mathbb{C}$ be a primitive $n$th root of unity for some integer $n \geq 2$.
Prove that $\sqrt[3]{2} \notin \mathbb{Q}(\zeta)$.
*(Use the Fundamental Theorem of Galois Theory).*
:::

::: solution
**Goal:** Prove that $\sqrt[3]{2} \notin \mathbb{Q}(\zeta_n)$ by showing that $\mathbb{Q}(\zeta_n)/\mathbb{Q}$ is an abelian Galois extension, whereas $\mathbb{Q}(\sqrt[3]{2})/\mathbb{Q}$ cannot embed into any abelian extension.

<1>1. Galois Group of the Cyclotomic Extension $\mathbb{Q}(\zeta_n)/\mathbb{Q}$:
    *Proof:*
    <2>1. The cyclotomic extension $\mathbb{Q}(\zeta_n)/\mathbb{Q}$ is the splitting field of the cyclotomic polynomial $\Phi_n(x)$ over $\mathbb{Q}$.
    <2>2. Thus $\mathbb{Q}(\zeta_n)/\mathbb{Q}$ is a **Galois extension**.
    <2>3. Its Galois group is isomorphic to the multiplicative group of units modulo $n$:
        $$\operatorname{Gal}(\mathbb{Q}(\zeta_n)/\mathbb{Q}) \cong (\mathbb{Z}/n\mathbb{Z})^\times.$$
    <2>4. Since $(\mathbb{Z}/n\mathbb{Z})^\times$ is a finite **abelian group**, $\mathbb{Q}(\zeta_n)/\mathbb{Q}$ is an **abelian Galois extension**.

<1>2. Galois Subfield Property (Fundamental Theorem of Galois Theory):
    *Proof:*
    <2>1. By the **Fundamental Theorem of Galois Theory**, every intermediate subfield $K$ with $\mathbb{Q} \subseteq K \subseteq \mathbb{Q}(\zeta_n)$ corresponds to a subgroup $H = \operatorname{Gal}(\mathbb{Q}(\zeta_n)/K) \le \operatorname{Gal}(\mathbb{Q}(\zeta_n)/\mathbb{Q})$.
    <2>2. Since the Galois group $\operatorname{Gal}(\mathbb{Q}(\zeta_n)/\mathbb{Q})$ is abelian, **every subgroup $H$ is normal** ($H \trianglelefteq \operatorname{Gal}(\mathbb{Q}(\zeta_n)/\mathbb{Q})$).
    <2>3. By Galois correspondence, $H \trianglelefteq \operatorname{Gal}(\mathbb{Q}(\zeta_n)/\mathbb{Q})$ if and only if the intermediate field $K$ is a **Galois extension of $\mathbb{Q}$**.
    <2>4. Therefore: **Every intermediate subfield $K \subseteq \mathbb{Q}(\zeta_n)$ must be Galois over $\mathbb{Q}$** (with abelian Galois group $\operatorname{Gal}(K/\mathbb{Q}) \cong \operatorname{Gal}(\mathbb{Q}(\zeta_n)/\mathbb{Q}) / H$).

<1>3. Non-Galois Property of the Cubic Field $\mathbb{Q}(\sqrt[3]{2})$:
    *Proof:*
    <2>1. Consider the field $L = \mathbb{Q}(\sqrt[3]{2})$.
    <2>2. The minimal polynomial of $\sqrt[3]{2}$ over $\mathbb{Q}$ is $m(x) = x^3 - 2$, which is irreducible over $\mathbb{Q}$ by Eisenstein's Criterion at $p = 2$.
    <2>3. The roots of $x^3 - 2$ in $\mathbb{C}$ are:
        $$r_1 = \sqrt[3]{2} \in \mathbb{R}, \qquad r_2 = \sqrt[3]{2} e^{2\pi i/3} \notin \mathbb{R}, \qquad r_3 = \sqrt[3]{2} e^{4\pi i/3} \notin \mathbb{R}.$$
    <2>4. Since $L = \mathbb{Q}(\sqrt[3]{2}) \subset \mathbb{R}$, $L$ contains the real root $r_1$, but does **not** contain the two non-real roots $r_2, r_3$.
    <2>5. Thus $L$ is not a splitting field of the irreducible polynomial $x^3 - 2$.
    <2>6. Therefore, $\mathbb{Q}(\sqrt[3]{2})/\mathbb{Q}$ is **not a Galois extension**.

<1>4. Obstruction / Conclusion:
    *Proof:*
    <2>1. If $\sqrt[3]{2} \in \mathbb{Q}(\zeta_n)$, then $\mathbb{Q}(\sqrt[3]{2})$ would be an intermediate subfield $\mathbb{Q} \subset \mathbb{Q}(\sqrt[3]{2}) \subseteq \mathbb{Q}(\zeta_n)$.
    <2>2. By Step 2, this would force $\mathbb{Q}(\sqrt[3]{2})/\mathbb{Q}$ to be a Galois extension.
    <2>3. But Step 3 proved that $\mathbb{Q}(\sqrt[3]{2})/\mathbb{Q}$ is not Galois.
    <2>4. This contradiction shows that $\sqrt[3]{2} \notin \mathbb{Q}(\zeta_n)$.

<1>5. Conclusion:
    $\sqrt[3]{2}$ does not lie in any cyclotomic field $\mathbb{Q}(\zeta_n)$. Q.E.D.
:::
