---
schema: qual/card@1
id: P-4DRTY
kind: problem
title: Is $\QQ(\sqrt[3]{21})$ normal?
classification:
  areas:
  - algebra
  topics:
  - Splitting Fields
  - Galois Theory
  - Field Extensions
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
---

::: problem
Is $\mathbb{Q}(\sqrt[3]{21})$ normal?
What is its splitting field?
What is its Galois group?
Describe the lattice of subfields.
:::

::: solution
**Goal:** Determine normality, the splitting field $K$, the Galois group $\operatorname{Gal}(K/\mathbb{Q})$, and the subfield lattice for the cubic field $\mathbb{Q}(\sqrt[3]{21})$.

<1>1. Normality of $\mathbb{Q}(\sqrt[3]{21})$:
    *Proof:*
    <2>1. The minimal polynomial of $\alpha = \sqrt[3]{21}$ over $\mathbb{Q}$ is $f(x) = x^3 - 21$.
    <2>2. $f(x)$ is irreducible over $\mathbb{Q}$ by Eisenstein's criterion at $p = 3$ (or $p = 7$).
    <2>3. The roots of $f(x)$ in $\mathbb{C}$ are:
        $$\alpha_1 = \sqrt[3]{21}, \qquad \alpha_2 = \sqrt[3]{21} \, \omega, \qquad \alpha_3 = \sqrt[3]{21} \, \omega^2,$$
        where $\omega = e^{2\pi i / 3} = \frac{-1 + i\sqrt{3}}{2}$.
    <2>4. The field $\mathbb{Q}(\sqrt[3]{21}) \subset \mathbb{R}$ is a real field, containing only the real root $\alpha_1$.
    <2>5. The non-real roots $\alpha_2, \alpha_3 \notin \mathbb{R}$, so $\alpha_2, \alpha_3 \notin \mathbb{Q}(\sqrt[3]{21})$.
    <2>6. Thus $\mathbb{Q}(\sqrt[3]{21})$ does not contain all roots of the irreducible polynomial $f(x)$, so it is **not normal** over $\mathbb{Q}$.

<1>2. The Splitting Field:
    *Proof:*
    <2>1. The splitting field of $x^3 - 21$ over $\mathbb{Q}$ is $K = \mathbb{Q}(\sqrt[3]{21}, \omega) = \mathbb{Q}(\sqrt[3]{21}, i\sqrt{3})$.
    <2>2. $[\mathbb{Q}(\sqrt[3]{21}) : \mathbb{Q}] = 3$ and $[\mathbb{Q}(\omega) : \mathbb{Q}] = 2$.
    <2>3. Since $\gcd(3, 2) = 1$, $[K : \mathbb{Q}] = 3 \cdot 2 = 6$.

<1>3. The Galois Group:
    *Proof:*
    <2>1. $K/\mathbb{Q}$ is the splitting field of an irreducible cubic polynomial with non-square discriminant:
        $$\Delta = -27(21)^2 = -11907 < 0 \implies \Delta \notin (\mathbb{Q}^\times)^2.$$
    <2>2. Therefore, the Galois group is the full symmetric group on 3 letters:
        $$\operatorname{Gal}(K/\mathbb{Q}) \cong S_3 = \langle \sigma, \tau \mid \sigma^3 = 1, \, \tau^2 = 1, \, \tau \sigma \tau = \sigma^{-1} \rangle,$$
        where $\sigma: \sqrt[3]{21} \mapsto \sqrt[3]{21}\omega, \ \omega \mapsto \omega$, and $\tau: \sqrt[3]{21} \mapsto \sqrt[3]{21}, \ \omega \mapsto \omega^2 = \overline{\omega}$.

<1>4. Lattice of Subfields:
    *Proof:*
    <2>1. By the Galois correspondence, intermediate subfields between $\mathbb{Q}$ and $K$ correspond bijectively (with inclusion reversing) to subgroups of $S_3$:
    <2>2. **Subgroups of $S_3$ and their fixed fields:**
        - $\{e\}$ of order 1 $\longleftrightarrow K = \mathbb{Q}(\sqrt[3]{21}, \omega)$ of degree 6 over $\mathbb{Q}$.
        - $\langle \tau \rangle = \{e, \tau\}$ of order 2 $\longleftrightarrow \mathbb{Q}(\sqrt[3]{21})$ of degree 3.
        - $\langle \sigma\tau \rangle$ of order 2 $\longleftrightarrow \mathbb{Q}(\sqrt[3]{21}\omega^2)$ of degree 3.
        - $\langle \sigma^2\tau \rangle$ of order 2 $\longleftrightarrow \mathbb{Q}(\sqrt[3]{21}\omega)$ of degree 3.
        - $A_3 = \langle \sigma \rangle = \{e, \sigma, \sigma^2\}$ of order 3 (normal subgroup) $\longleftrightarrow \mathbb{Q}(\omega) = \mathbb{Q}(i\sqrt{3})$ of degree 2 (the unique quadratic subfield, Galois over $\mathbb{Q}$).
        - $S_3$ of order 6 $\longleftrightarrow \mathbb{Q}$ of degree 1.
    <2>3. Structure: $\mathbb{Q}$ at the bottom has one quadratic extension $\mathbb{Q}(i\sqrt{3})$ and three cubic non-normal extensions $\mathbb{Q}(\sqrt[3]{21}\omega^j)$ ($j = 0, 1, 2$), all four of which join at the top field $K = \mathbb{Q}(\sqrt[3]{21}, i\sqrt{3})$.

<1>5. Conclusion:
    $\mathbb{Q}(\sqrt[3]{21})$ is not normal; the splitting field is $\mathbb{Q}(\sqrt[3]{21}, i\sqrt{3})$ of degree 6 with Galois group $S_3$; intermediate fields comprise three cubic conjugate fields and one quadratic normal field $\mathbb{Q}(i\sqrt{3})$. Q.E.D.
:::
