---
schema: qual/card@1
id: P-TM7YV
kind: problem
title: $\gal(E/B)$ and $\gal(E/C)$ for splitting fields of $f=gh$, $\gal(E/\QQ)\cong\gal(E/B)\times\gal(E/C)$
  when $B\cap C=\QQ$, and $\gal(\QQ[\sqrt{2}+\sqrt{3}]/\QQ)$
classification:
  areas:
  - algebra
  topics:
  - Galois Theory
  - Normal Subgroups
  - Direct Products
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
---

::: problem
Let $f(x) = g(x) h(x) \in \mathbb{Q}[x]$ and let $E, B, C / \mathbb{Q}$ be the splitting fields over $\mathbb{Q}$ of $f, g, h$ respectively (viewed inside a fixed algebraic closure $\overline{\mathbb{Q}}$).

(a) Prove that $\operatorname{Gal}(E/B)$ and $\operatorname{Gal}(E/C)$ are normal subgroups of $\operatorname{Gal}(E/\mathbb{Q})$.
(b) Prove that $\operatorname{Gal}(E/B) \cap \operatorname{Gal}(E/C) = \{1\}$.
(c) If $B \cap C = \mathbb{Q}$, show that $\operatorname{Gal}(E/B) \operatorname{Gal}(E/C) = \operatorname{Gal}(E/\mathbb{Q})$.
(d) Under the hypothesis of (c), show that $\operatorname{Gal}(E/\mathbb{Q}) \cong \operatorname{Gal}(E/B) \times \operatorname{Gal}(E/C) \cong \operatorname{Gal}(C/\mathbb{Q}) \times \operatorname{Gal}(B/\mathbb{Q})$.
(e) Use (d) to describe $\operatorname{Gal}(\mathbb{Q}[\alpha]/\mathbb{Q})$ where $\alpha = \sqrt{2} + \sqrt{3}$.
:::

::: solution
**Goal:** Prove the Galois group splitting for composita of linearly disjoint Galois extensions and compute the Galois group of $\mathbb{Q}(\sqrt{2} + \sqrt{3})$.

<1>1. Setting and Fixed Field Properties:
    *Proof:*
    <2>1. Since $B$ is the splitting field of $g(x) \in \mathbb{Q}[x]$ and $C$ is the splitting field of $h(x) \in \mathbb{Q}[x]$, both $B/\mathbb{Q}$ and $C/\mathbb{Q}$ are finite Galois extensions.
    <2>2. The splitting field $E$ of $f = gh$ is the compositum $E = BC$.
    <2>3. Since $E/\mathbb{Q}$ is finite Galois, the Fundamental Theorem of Galois Theory applies to intermediate fields.

<1>2. Part (a): Normality of $\operatorname{Gal}(E/B)$ and $\operatorname{Gal}(E/C)$:
    *Proof:*
    <2>1. By the **Fundamental Theorem of Galois Theory**, for any intermediate field $K$ with $\mathbb{Q} \subseteq K \subseteq E$, the subgroup $\operatorname{Gal}(E/K)$ is normal in $\operatorname{Gal}(E/\mathbb{Q})$ if and only if $K/\mathbb{Q}$ is a normal (Galois) extension.
    <2>2. Since $B/\mathbb{Q}$ and $C/\mathbb{Q}$ are splitting fields over $\mathbb{Q}$, both $B$ and $C$ are normal extensions of $\mathbb{Q}$.
    <2>3. Therefore, $\operatorname{Gal}(E/B) \trianglelefteq \operatorname{Gal}(E/\mathbb{Q})$ and $\operatorname{Gal}(E/C) \trianglelefteq \operatorname{Gal}(E/\mathbb{Q})$.

<1>3. Part (b): Intersection $\operatorname{Gal}(E/B) \cap \operatorname{Gal}(E/C) = \{1\}$:
    *Proof:*
    <2>1. Let $\sigma \in \operatorname{Gal}(E/B) \cap \operatorname{Gal}(E/C)$.
    <2>2. Since $\sigma \in \operatorname{Gal}(E/B)$, $\sigma$ fixes $B$ pointwise: $\sigma(b) = b$ for all $b \in B$.
    <2>3. Since $\sigma \in \operatorname{Gal}(E/C)$, $\sigma$ fixes $C$ pointwise: $\sigma(c) = c$ for all $c \in C$.
    <2>4. Since $E = BC$ is generated over $\mathbb{Q}$ by the roots of $g$ (which lie in $B$) and the roots of $h$ (which lie in $C$), $\sigma$ fixes all generators of $E$.
    <2>5. Thus $\sigma = \operatorname{id}_E = 1$, so $\operatorname{Gal}(E/B) \cap \operatorname{Gal}(E/C) = \{1\}$.

<1>4. Part (c): Product $\operatorname{Gal}(E/B) \operatorname{Gal}(E/C) = \operatorname{Gal}(E/\mathbb{Q})$ when $B \cap C = \mathbb{Q}$:
    *Proof:*
    <2>1. The fixed field of the subgroup $H \coloneqq \operatorname{Gal}(E/B) \operatorname{Gal}(E/C)$ is the intersection of the fixed fields of the two subgroups:
        $$\operatorname{Fix}(H) = \operatorname{Fix}(\operatorname{Gal}(E/B)) \cap \operatorname{Fix}(\operatorname{Gal}(E/C)) = B \cap C.$$
    <2>2. Under the hypothesis $B \cap C = \mathbb{Q}$, we have $\operatorname{Fix}(H) = \mathbb{Q}$.
    <2>3. By Galois correspondence, a subgroup whose fixed field is the base field $\mathbb{Q}$ must be the entire Galois group:
        $$H = \operatorname{Gal}(E/\mathbb{Q}) \implies \operatorname{Gal}(E/B) \operatorname{Gal}(E/C) = \operatorname{Gal}(E/\mathbb{Q}).$$

<1>5. Part (d): Direct Product Isomorphism:
    *Proof:*
    <2>1. $\operatorname{Gal}(E/B)$ and $\operatorname{Gal}(E/C)$ are normal subgroups of $\operatorname{Gal}(E/\mathbb{Q})$, their intersection is trivial $\{1\}$, and their product is $\operatorname{Gal}(E/\mathbb{Q})$.
    <2>2. By the **Internal Direct Product Theorem**:
        $$\operatorname{Gal}(E/\mathbb{Q}) \cong \operatorname{Gal}(E/B) \times \operatorname{Gal}(E/C).$$
    <2>3. Restriction map gives $\operatorname{Gal}(E/B) \cong \operatorname{Gal}(C/\mathbb{Q})$ and $\operatorname{Gal}(E/C) \cong \operatorname{Gal}(B/\mathbb{Q})$, so $\operatorname{Gal}(E/\mathbb{Q}) \cong \operatorname{Gal}(B/\mathbb{Q}) \times \operatorname{Gal}(C/\mathbb{Q})$.

<1>6. Part (e): Application to $\alpha = \sqrt{2} + \sqrt{3}$:
    *Proof:*
    <2>1. Let $g(x) = x^2 - 2$ and $h(x) = x^2 - 3$.
    <2>2. Then $B = \mathbb{Q}(\sqrt{2})$ and $C = \mathbb{Q}(\sqrt{3})$, both quadratic extensions over $\mathbb{Q}$.
    <2>3. $B \cap C = \mathbb{Q}(\sqrt{2}) \cap \mathbb{Q}(\sqrt{3}) = \mathbb{Q}$ since $\sqrt{3} \notin \mathbb{Q}(\sqrt{2})$.
    <2>4. The compositum is $E = BC = \mathbb{Q}(\sqrt{2}, \sqrt{3})$.
    <2>5. Since $\alpha = \sqrt{2} + \sqrt{3}$, $\alpha^2 = 5 + 2\sqrt{6} \implies \sqrt{6} = \frac{\alpha^2-5}{2} \in \mathbb{Q}(\alpha)$, and $\alpha(\sqrt{6}-1) = 2\sqrt{3} + 3\sqrt{2} - \sqrt{2} - \sqrt{3} = \sqrt{2} + 2\sqrt{3}$, from which both $\sqrt{2}, \sqrt{3} \in \mathbb{Q}(\alpha)$. Thus $\mathbb{Q}(\alpha) = E$.
    <2>6. Applying Part (d):
        $$\operatorname{Gal}(\mathbb{Q}[\alpha]/\mathbb{Q}) \cong \operatorname{Gal}(\mathbb{Q}(\sqrt{2})/\mathbb{Q}) \times \operatorname{Gal}(\mathbb{Q}(\sqrt{3})/\mathbb{Q}) \cong \mathbb{Z}/2\mathbb{Z} \times \mathbb{Z}/2\mathbb{Z} \cong V_4 \text{ (Klein four-group)}.$$
    <2>7. The four automorphisms are determined by the independent sign choices:
        $$\sigma_{\pm, \pm}(\sqrt{2}) = \pm \sqrt{2}, \qquad \sigma_{\pm, \pm}(\sqrt{3}) = \pm \sqrt{3}.$$

<1>7. Conclusion:
    $E/\mathbb{Q}$ has normal subgroups $\operatorname{Gal}(E/B), \operatorname{Gal}(E/C)$ intersecting trivially; when $B \cap C = \mathbb{Q}$, their direct product gives $\operatorname{Gal}(E/\mathbb{Q}) \cong \operatorname{Gal}(B/\mathbb{Q}) \times \operatorname{Gal}(C/\mathbb{Q})$, yielding $\mathbb{Z}_2 \times \mathbb{Z}_2$ for $\mathbb{Q}(\sqrt{2}+\sqrt{3})$. Q.E.D.
:::
