---
schema: qual/card@1
id: P-7ALW6
kind: problem
title: $\mathrm{Gal}(\QQ(\sqrt{2},\sqrt{3})/\QQ)$
classification:
  areas:
  - algebra
  topics:
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
What is the Galois group of $\mathbb{Q}(\sqrt{2}, \sqrt{3}) / \mathbb{Q}$?
:::

::: solution
**Goal:** Compute the Galois group $\operatorname{Gal}(K/\mathbb{Q})$ for $K = \mathbb{Q}(\sqrt{2}, \sqrt{3})$.

<1>1. Degree of the extension $[K : \mathbb{Q}]$:
    *Proof:*
    <2>1. Clearly $[\mathbb{Q}(\sqrt{2}) : \mathbb{Q}] = 2$ because $x^2 - 2$ is irreducible over $\mathbb{Q}$ by Eisenstein at $p = 2$.
    <2>2. We show $\sqrt{3} \notin \mathbb{Q}(\sqrt{2})$.
        - Suppose $\sqrt{3} = a + b\sqrt{2}$ for some $a, b \in \mathbb{Q}$.
        - Squaring both sides: $3 = (a^2 + 2b^2) + 2ab\sqrt{2}$.
        - Since $\sqrt{2} \notin \mathbb{Q}$, we must have $2ab = 0$.
        - If $b = 0$, then $3 = a^2$, impossible for $a \in \mathbb{Q}$.
        - If $a = 0$, then $3 = 2b^2 \implies b^2 = 3/2$, impossible for $b \in \mathbb{Q}$.
        - Thus $\sqrt{3} \notin \mathbb{Q}(\sqrt{2})$.
    <2>3. Hence the minimal polynomial of $\sqrt{3}$ over $\mathbb{Q}(\sqrt{2})$ is $x^2 - 3$, so $[K : \mathbb{Q}(\sqrt{2})] = 2$.
    <2>4. By the tower law, $[K : \mathbb{Q}] = [K : \mathbb{Q}(\sqrt{2})] \cdot [\mathbb{Q}(\sqrt{2}) : \mathbb{Q}] = 2 \cdot 2 = 4$.

<1>2. $K/\mathbb{Q}$ is a Galois extension:
    *Proof:*
    <2>1. $K = \mathbb{Q}(\sqrt{2}, \sqrt{3})$ is the splitting field of $(x^2 - 2)(x^2 - 3)$ over $\mathbb{Q}$.
    <2>2. In characteristic 0, splitting fields are Galois extensions.
    <2>3. Thus $|\operatorname{Gal}(K/\mathbb{Q})| = [K : \mathbb{Q}] = 4$.

<1>3. Generators and isomorphism type:
    *Proof:*
    <2>1. Any $\mathbb{Q}$-automorphism $\sigma \in \operatorname{Gal}(K/\mathbb{Q})$ must send $\sqrt{2} \mapsto \pm\sqrt{2}$ and $\sqrt{3} \mapsto \pm\sqrt{3}$.
    <2>2. The four possible sign choices define four distinct automorphisms:
        - $\operatorname{id}: \sqrt{2} \mapsto \sqrt{2}, \ \sqrt{3} \mapsto \sqrt{3}$.
        - $\sigma: \sqrt{2} \mapsto -\sqrt{2}, \ \sqrt{3} \mapsto \sqrt{3}$.
        - $\tau: \sqrt{2} \mapsto \sqrt{2}, \ \sqrt{3} \mapsto -\sqrt{3}$.
        - $\sigma\tau: \sqrt{2} \mapsto -\sqrt{2}, \ \sqrt{3} \mapsto -\sqrt{3}$.
    <2>3. Each non-identity element has order 2: $\sigma^2 = \tau^2 = (\sigma\tau)^2 = \operatorname{id}$.
    <2>4. Thus $\operatorname{Gal}(K/\mathbb{Q})$ is abelian with every non-identity element of order 2, which is the Klein four-group:
        $$\operatorname{Gal}(\mathbb{Q}(\sqrt{2}, \sqrt{3}) / \mathbb{Q}) \cong \mathbb{Z}/2\mathbb{Z} \times \mathbb{Z}/2\mathbb{Z} \cong V_4.$$

<1>4. Conclusion:
    The Galois group is $\mathbb{Z}/2\mathbb{Z} \times \mathbb{Z}/2\mathbb{Z} \cong V_4$. Q.E.D.
:::
