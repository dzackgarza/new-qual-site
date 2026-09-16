---
schema: qual/card@1
id: T-BIRKGROTH
kind: theorem
title: Vector bundles on the projective line split
classification:
  areas:
  - algebraic-geometry
  topics:
  - Vector Bundles
  - Projective Line
  - Twisting Sheaves
relations:
- kind: uses
  target: T-MODVB
- kind: uses
  target: D-CB9XS
review: draft
prompts:
- What is the Birkhoff--Grothendieck theorem?
---

::: {.theorem title="Birkhoff--Grothendieck"}
Let $k$ be a field.
Every locally free sheaf of finite rank on $\PP^1_k$ is isomorphic to $\OO(a_1) \oplus \cdots \oplus \OO(a_r)$ for integers $a_1 \geq \cdots \geq a_r$, and these integers are uniquely determined.
:::

::: {.proof}
1. *Uniqueness:* $h^0(\OO(a_1) \oplus \cdots \oplus \OO(a_r) \otimes \OO(m)) = \sum_i \max(a_i + m + 1, 0)$ for all $m$, and this function of $m$ determines the multiset $\{a_i\}$.

2. *Existence, by induction on the rank $r$:* the case $r = 1$ is $\Pic(\PP^1) = \ZZ$.

3. For $\mathcal{E}$ of rank $r$, $h^0(\mathcal{E}(m)) = 0$ for $m \ll 0$ and $\neq 0$ for $m \gg 0$, so there is a largest $a$ with $H^0(\mathcal{E}(-a)) \neq 0$.
   A nonzero section $s$ of $\mathcal{E}(-a)$ vanishes nowhere, since otherwise it would be a section of $\mathcal{E}(-a-1)$ after dividing by a linear form vanishing at a zero; so $\OO(a) \to \mathcal{E}$ is a subbundle with locally free quotient $\mathcal{E}'$ of rank $r-1$.

4. By induction $\mathcal{E}' \cong \bigoplus_{i \geq 2} \OO(b_i)$.
   Maximality of $a$ gives $b_i \leq a$: twisting the sequence $0 \to \OO(a) \to \mathcal{E} \to \mathcal{E}' \to 0$ by $\OO(-a-1)$ gives $0 \to \OO(-1) \to \mathcal{E}(-a-1) \to \mathcal{E}'(-a-1) \to 0$; since $H^0(\mathcal{E}(-a-1)) = 0$ and $H^1(\OO(-1)) = 0$, also $H^0(\mathcal{E}'(-a-1)) = 0$, so every $b_i - a - 1 < 0$.

5. The extension class lies in $\operatorname{Ext}^1(\mathcal{E}', \OO(a)) = \bigoplus_i H^1(\OO(a - b_i))$, which vanishes because $a - b_i \geq 0 > -2$.
   So the sequence splits and $\mathcal{E} \cong \OO(a) \oplus \mathcal{E}'$.
:::

::: {.example}
The tangent bundle of $\PP^2$ restricted to a line $\ell$ is $\OO_\ell(2) \oplus \OO_\ell(1)$: the tangent bundle of the line is the first summand and the normal bundle $\OO_\ell(1)$ the second.
:::
