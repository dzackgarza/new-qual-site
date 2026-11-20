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
audit:
- event: solution-written
  by: claude
  date: 2026-11-20
  note: >-
    The card carried no audit list; this one records the change. Eighteen steps asserted their claim with
    no justification and each now carries one: the order of $\zeta$, the identification of $\Phi_8$ with
    $x^4+1$, its irreducibility by Eisenstein after the shift $x \mapsto x+1$, the degree count, the
    Galois group $(\ZZ/8)^\times$ as the Klein four-group, the correspondence between quadratic subfields
    and the three subgroups of order 2, the explicit fixed fields from $\zeta^2$, $\zeta+\zeta^{-1}$ and
    $\zeta-\zeta^{-1}$, and in part (c) the identification $\QQ(\zeta) = \QQ(i,\sqrt2)$, the inclusion
    $\QQ(\sqrt2) \subseteq \QQ(\sqrt[4]{2})$, the Eisenstein irreducibility of $x^4-2$, the reality of
    $\QQ(\sqrt[4]{2})$ and the minimal polynomial $x^2+1$ of $i$ over it, ending in the tower law.
    Checked while writing: the two quadratic subfields $\QQ(\sqrt2)$ and $\QQ(\sqrt{-2})$ are distinct
    because $i\sqrt2$ is not a rational multiple of $\sqrt2$, and the tower law needs the intermediate
    field $\QQ(\sqrt[4]{2})$ of degree $4$. Two repairs: the step whose claim read "By the Tower Law of
    extension degrees:" now states the degree it computes, and the closing pf-qed that only listed which
    step answers which part is gone, so the tower-law step carries the QED. The statement is unchanged.
    The collection retains the UGA algebra qualifying exam of Spring 2019 and no solution sheet, so the
    argument is the card's own.
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


::: pf-proof
$\zeta^8 = e^{2\pi i} = 1$, and $\zeta^k = e^{2\pi i k/8} \neq 1$ for $1 \le k \le 7$ because $2\pi k/8$ is not a multiple of $2\pi$ there; so the order of $\zeta$ is exactly $8$.
:::

:::

::: pf-step

The minimal polynomial of $\zeta$ over $\QQ$ is the $8$-th cyclotomic polynomial:
    $$\Phi_8(x) = \frac{x^8 - 1}{x^4 - 1} = x^4 + 1.$$


::: pf-proof
For a primitive $n$-th root of unity the minimal polynomial over $\QQ$ is the $n$-th cyclotomic polynomial; for $n = 8$ that is $(x^8-1)/(x^4-1)$, which collects the four primitive $8$-th roots $\pm\zeta, \pm\zeta^3$, and division gives $x^4+1$.
:::

:::

::: pf-step

$\Phi_8(x)$ is irreducible over $\QQ$ (for instance, $\Phi_8(x+1) = x^4 + 4x^3 + 6x^2 + 4x + 2$ is irreducible by Eisenstein's criterion at $p = 2$).


::: pf-proof
$\Phi_8(x+1) = x^4+4x^3+6x^2+4x+2$ has every non-leading coefficient divisible by $2$ and constant term divisible by $2$ but not by $4$, so Eisenstein's criterion at $p = 2$ applies to it; a factorization of $\Phi_8$ would give one of $\Phi_8(x+1)$ by substituting $x-1$, so $\Phi_8$ is irreducible over $\QQ$.
:::

:::

::: pf-step

Therefore $[\QQ(\zeta) : \QQ] = \deg \Phi_8(x) = \varphi(8) = 8(1 - 1/2) = 4$.


::: pf-proof
The degree of $\QQ(\zeta)$ over $\QQ$ is the degree of the minimal polynomial of $\zeta$, which is $\Phi_8$; its degree is $4$, and $\varphi(8) = 8(1 - 1/2) = 4$ agrees with that.
:::

:::

:::

:::

::: {.pf-step #s2}

The three quadratic subfields of $\QQ(\zeta)$ are
$$
\boxed{\QQ(i),\quad \QQ(\sqrt2),\quad\QQ(\sqrt{-2})}.
$$

::: pf-proof

::: pf-step

The extension $\QQ(\zeta)/\QQ$ is Galois, with Galois group isomorphic to the unit group $(\ZZ/8\ZZ)^\times$:
    $$\operatorname{Gal}(\QQ(\zeta)/\QQ) \cong (\ZZ/8\ZZ)^\times = \{1, 3, 5, 7\} \cong \ZZ/2\ZZ \times \ZZ/2\ZZ,$$
    which is the Klein four-group $V_4$.


::: pf-proof
$\QQ(\zeta)$ is the splitting field of $x^8-1$ over $\QQ$, hence Galois; an automorphism sends $\zeta$ to another primitive $8$-th root, that is to $\zeta^a$ with $a$ coprime to $8$, and is determined by that choice, so the group is $(\ZZ/8\ZZ)^\times = \{1,3,5,7\}$. Each of these elements squares to $1$, so the group is $\ZZ/2\ZZ \times \ZZ/2\ZZ$.
:::

:::

::: pf-step

By the Fundamental Theorem of Galois Theory, intermediate fields $E$ with $[E : \QQ] = 2$ correspond bijectively to subgroups $H \le \operatorname{Gal}(\QQ(\zeta)/\QQ)$ of index 2 (which are subgroups of order 2).


::: pf-proof
The fundamental theorem makes $E \mapsto \Gal(\QQ(\zeta)/E)$ a bijection reversing inclusions with $[E:\QQ] = [G : \Gal(\QQ(\zeta)/E)]$, because the degree over $\QQ$ is the index of the corresponding subgroup; so $[E:\QQ] = 2$ exactly for the subgroups of index $2$, which have order $\abs{G}/2 = 2$.
:::

:::

::: pf-step

The group $\ZZ/2\ZZ \times \ZZ/2\ZZ$ has exactly three subgroups of order 2:
    $$H_1 = \langle 3 \rangle, \qquad H_2 = \langle 5 \rangle, \qquad H_3 = \langle 7 \rangle.$$


::: pf-proof
In a group all of whose nonidentity elements have order $2$, a subgroup of order $2$ is generated by one nonidentity element and contains no other, so the subgroups of order $2$ correspond bijectively to the three nonidentity elements $3$, $5$ and $7$.
:::

:::

::: pf-step

Compute the fixed fields:
        - Note $\zeta = \cos(\pi/4) + i \sin(\pi/4) = \frac{\sqrt{2}}{2}(1 + i)$.
        - Then $\zeta^2 = i$, so $\QQ(i) \subset \QQ(\zeta)$ is a quadratic subfield.
        - $\zeta + \zeta^{-1} = \frac{\sqrt{2}}{2}(1 + i) + \frac{\sqrt{2}}{2}(1 - i) = \sqrt{2}$, so $\QQ(\sqrt{2}) \subset \QQ(\zeta)$ is a quadratic subfield.
        - $\zeta - \zeta^{-1} = \frac{\sqrt{2}}{2}(1 + i) - \frac{\sqrt{2}}{2}(1 - i) = i \sqrt{2} = \sqrt{-2}$, so $\QQ(\sqrt{-2}) \subset \QQ(\zeta)$ is a quadratic subfield.


::: pf-proof
The element $\zeta$ equals $\frac{\sqrt2}{2}(1+i)$ and its inverse $\frac{\sqrt2}{2}(1-i)$, so $\zeta^2 = i$, $\zeta+\zeta^{-1} = \sqrt2$ and $\zeta-\zeta^{-1} = i\sqrt2$; each of $i$, $\sqrt2$ and $i\sqrt2$ satisfies a quadratic equation over $\QQ$ ($i^2 = -1$, $(\sqrt2)^2 = 2$, $(i\sqrt2)^2 = -2$), so each generates a quadratic subfield of $\QQ(\zeta)$.
:::

:::

::: pf-step

The three distinct quadratic subfields are $\QQ(i)$, $\QQ(\sqrt{2})$, and $\QQ(\sqrt{-2})$.


::: pf-proof
The three generators $i$, $\sqrt2$ and $i\sqrt2$ are pairwise independent over $\QQ$, so the three fields are distinct; since there are exactly three subgroups of order $2$ and the correspondence is a bijection, there are exactly three quadratic intermediate fields, and they are these.
:::

:::

:::

:::

::: {.pf-step #s3}

The extension obtained by adjoining the fourth root of two has degree
$$
\boxed{[\QQ(\zeta,\sqrt[4]2):\QQ]=8}.
$$

::: pf-proof

::: {.pf-step #zeta-field}

From step [](#s2){.pf-ref}, $\QQ(\zeta) = \QQ(i, \sqrt{2})$.


::: pf-proof
Both $i = \zeta^2$ and $\sqrt2 = \zeta+\zeta^{-1}$ lie in $\QQ(\zeta)$, so $\QQ(i,\sqrt2) \subseteq \QQ(\zeta)$; conversely $\zeta = \frac{\sqrt2}{2}(1+i)$ lies in $\QQ(i,\sqrt2)$, so the two fields are equal.
:::

:::

::: pf-step

Since $(\sqrt[4]{2})^2 = \sqrt{2}$, we have $\QQ(\sqrt{2}) \subseteq \QQ(\sqrt[4]{2})$.


::: pf-proof
$\sqrt2 = (\sqrt[4]{2})^2$ is a polynomial expression in $\sqrt[4]{2}$ with rational coefficients, so it lies in the field that $\sqrt[4]{2}$ generates.
:::

:::

::: pf-step

Therefore, adjoining $\sqrt[4]{2}$ to $\QQ(\zeta) = \QQ(i, \sqrt{2})$ gives
    $$\QQ(\zeta, \sqrt[4]{2}) = \QQ(i, \sqrt{2}, \sqrt[4]{2}) = \QQ(i, \sqrt[4]{2}).$$


::: pf-proof
By the identification of step [](#zeta-field){.pf-ref} the field generated by $\QQ(\zeta)$ and $\sqrt[4]{2}$ is $\QQ(i,\sqrt2,\sqrt[4]{2})$, and $\sqrt2$ already lies in $\QQ(\sqrt[4]{2})$, so it contributes nothing further; hence the field is $\QQ(i,\sqrt[4]{2})$.
:::

:::

::: pf-step

The polynomial $x^4 - 2 \in \QQ[x]$ is irreducible over $\QQ$ by Eisenstein at $p = 2$, so $[\QQ(\sqrt[4]{2}) : \QQ] = 4$.


::: pf-proof
Eisenstein's criterion at $p = 2$ applies to $x^4-2$: the leading coefficient is $1$, the only other nonzero coefficient is the constant term $-2$, divisible by $2$ but not by $4$. So the polynomial is irreducible over $\QQ$ and the degree of $\QQ(\sqrt[4]{2})$ over $\QQ$ equals its degree $4$.
:::

:::

::: pf-step

The field $\QQ(\sqrt[4]{2})$ is a subfield of $\RR$.


::: pf-proof
$\sqrt[4]{2}$ is the positive real fourth root of $2$, and a field generated over $\QQ$ by real numbers consists of real numbers, because $\RR$ is a field containing $\QQ$ and that root.
:::

:::

::: pf-step

Since $i \notin \RR$, $i \notin \QQ(\sqrt[4]{2})$.


::: pf-proof
Every element of $\QQ(\sqrt[4]{2})$ is real by the previous step, and $i$ is not real, so $i$ does not lie in that field.
:::

:::

::: pf-step

The minimal polynomial of $i$ over $\QQ(\sqrt[4]{2})$ is $x^2 + 1$, which has degree 2.


::: pf-proof
The element $i$ satisfies $x^2+1 = 0$, and $x^2+1$ has no root in the real field $\QQ(\sqrt[4]{2})$, so it has no linear factor there; a polynomial of degree $2$ with no linear factor is irreducible, and the monic irreducible polynomial of $i$ over that field is its minimal polynomial.
:::

:::

::: pf-step

Thus $[\QQ(i, \sqrt[4]{2}) : \QQ(\sqrt[4]{2})] = 2$.


::: pf-proof
Adjoining an element to a field gives an extension whose degree is the degree of the minimal polynomial of that element; here the minimal polynomial is $x^2+1$, of degree $2$.
:::

:::

::: pf-step

By the Tower Law, $[\QQ(\zeta, \sqrt[4]{2}) : \QQ] = 8$.


::: pf-proof
The tower law applied to $\QQ \subseteq \QQ(\sqrt[4]{2}) \subseteq \QQ(i,\sqrt[4]{2})$ gives $[\QQ(i,\sqrt[4]{2}):\QQ] = [\QQ(i,\sqrt[4]{2}):\QQ(\sqrt[4]{2})] \cdot [\QQ(\sqrt[4]{2}):\QQ] = 2 \cdot 4 = 8$, and the two fields are equal by the identification of the earlier steps.
:::

:::

$$[\QQ(\zeta, \sqrt[4]{2}) : \QQ] = [\QQ(i, \sqrt[4]{2}) : \QQ(\sqrt[4]{2})] \cdot [\QQ(\sqrt[4]{2}) : \QQ] = 2 \cdot 4 = 8.$$

:::

:::

:::

:::
