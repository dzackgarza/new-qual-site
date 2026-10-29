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
::: {.problem}
Let $\zeta = e^{2\pi i / 8}$ be a primitive $8$-th root of unity in $\CC$.

(a) What is the degree $[\QQ(\zeta) : \QQ]$?

(b) How many quadratic subfields of $\QQ(\zeta)$ are there? List them with justification.

(c) What is the degree $[\QQ(\zeta, \sqrt[4]{2}) : \QQ]$?
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

The degree of the cyclotomic extension is $[\QQ(\zeta):\QQ]=4$.

::: pf-proof

::: pf-step

The element $\zeta = e^{2\pi i / 8}$ is a primitive $8$-th root of unity.

:::

::: pf-step

The minimal polynomial of $\zeta$ over $\QQ$ is the $8$-th cyclotomic polynomial:
    $$\Phi_8(x) = \frac{x^8 - 1}{x^4 - 1} = x^4 + 1.$$

:::

::: pf-step

$\Phi_8(x)$ is irreducible over $\QQ$ (for instance, $\Phi_8(x+1) = x^4 + 4x^3 + 6x^2 + 4x + 2$ is irreducible by Eisenstein's criterion at $p = 2$).

:::

::: pf-step

Therefore $[\QQ(\zeta) : \QQ] = \deg \Phi_8(x) = \varphi(8) = 8(1 - 1/2) = 4$.

:::

:::

:::

::: {.pf-step #s2}

The three quadratic subfields of $\QQ(\zeta)$ are
\[
\boxed{\QQ(i),\quad \QQ(\sqrt2),\quad\QQ(\sqrt{-2})}.
\]

::: pf-proof

::: pf-step

The extension $\QQ(\zeta)/\QQ$ is Galois, with Galois group isomorphic to the unit group $(\ZZ/8\ZZ)^\times$:
    $$\operatorname{Gal}(\QQ(\zeta)/\QQ) \cong (\ZZ/8\ZZ)^\times = \{1, 3, 5, 7\} \cong \ZZ/2\ZZ \times \ZZ/2\ZZ,$$
    which is the Klein four-group $V_4$.

:::

::: pf-step

By the Fundamental Theorem of Galois Theory, intermediate fields $E$ with $[E : \QQ] = 2$ correspond bijectively to subgroups $H \le \operatorname{Gal}(\QQ(\zeta)/\QQ)$ of index 2 (which are subgroups of order 2).

:::

::: pf-step

The group $\ZZ/2\ZZ \times \ZZ/2\ZZ$ has exactly three subgroups of order 2:
    $$H_1 = \langle 3 \rangle, \qquad H_2 = \langle 5 \rangle, \qquad H_3 = \langle 7 \rangle.$$

:::

::: pf-step

Compute the fixed fields:
        - Note $\zeta = \cos(\pi/4) + i \sin(\pi/4) = \frac{\sqrt{2}}{2}(1 + i)$.
        - Then $\zeta^2 = i$, so $\QQ(i) \subset \QQ(\zeta)$ is a quadratic subfield.
        - $\zeta + \zeta^{-1} = \frac{\sqrt{2}}{2}(1 + i) + \frac{\sqrt{2}}{2}(1 - i) = \sqrt{2}$, so $\QQ(\sqrt{2}) \subset \QQ(\zeta)$ is a quadratic subfield.
        - $\zeta - \zeta^{-1} = \frac{\sqrt{2}}{2}(1 + i) - \frac{\sqrt{2}}{2}(1 - i) = i \sqrt{2} = \sqrt{-2}$, so $\QQ(\sqrt{-2}) \subset \QQ(\zeta)$ is a quadratic subfield.

:::

::: pf-step

The three distinct quadratic subfields are $\QQ(i)$, $\QQ(\sqrt{2})$, and $\QQ(\sqrt{-2})$.

:::

:::

:::

::: {.pf-step #s3}

The extension obtained by adjoining the fourth root of two has degree
\[
\boxed{[\QQ(\zeta,\sqrt[4]2):\QQ]=8}.
\]

::: pf-proof

::: pf-step

From step [](#s2){.pf-ref}, $\QQ(\zeta) = \QQ(i, \sqrt{2})$.

:::

::: pf-step

Since $(\sqrt[4]{2})^2 = \sqrt{2}$, we have $\QQ(\sqrt{2}) \subseteq \QQ(\sqrt[4]{2})$.

:::

::: pf-step

Therefore, adjoining $\sqrt[4]{2}$ to $\QQ(\zeta) = \QQ(i, \sqrt{2})$ gives
    $$\QQ(\zeta, \sqrt[4]{2}) = \QQ(i, \sqrt{2}, \sqrt[4]{2}) = \QQ(i, \sqrt[4]{2}).$$

:::

::: pf-step

The polynomial $x^4 - 2 \in \QQ[x]$ is irreducible over $\QQ$ by Eisenstein at $p = 2$, so $[\QQ(\sqrt[4]{2}) : \QQ] = 4$.

:::

::: pf-step

The field $\QQ(\sqrt[4]{2})$ is a subfield of $\RR$.

:::

::: pf-step

Since $i \notin \RR$, $i \notin \QQ(\sqrt[4]{2})$.

:::

::: pf-step

The minimal polynomial of $i$ over $\QQ(\sqrt[4]{2})$ is $x^2 + 1$, which has degree 2.

:::

::: pf-step

Thus $[\QQ(i, \sqrt[4]{2}) : \QQ(\sqrt[4]{2})] = 2$.

:::

::: pf-step

By the Tower Law of extension degrees:

:::

$$[\QQ(\zeta, \sqrt[4]{2}) : \QQ] = [\QQ(i, \sqrt[4]{2}) : \QQ(\sqrt[4]{2})] \cdot [\QQ(\sqrt[4]{2}) : \QQ] = 2 \cdot 4 = 8.$$

:::

:::

::: pf-qed

Steps [](#s1){.pf-ref}, [](#s2){.pf-ref} and [](#s3){.pf-ref} prove parts (a), (b), and (c), respectively.

:::

:::

:::
