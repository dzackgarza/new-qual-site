---
schema: qual/card@1
id: P-ZJFFS
kind: problem
title: Quadratic extensions in characteristic 0 are Galois; stacked quadratics need
  not be
classification:
  areas:
  - algebra
  topics:
  - Galois Theory
  - Field Extensions
  - Normal Subgroups
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
---

::: problem
Take a quadratic extension of a field of characteristic 0. Is it Galois?
Take a degree 2 extension on top of that.
Does it have to be Galois over the base field?
What statement in group theory can you think of that reflects this?
:::

::: solution
**Goal:** Address Galois property of degree 2 extensions and towers of quadratics, and relate this to the non-transitivity of normal subgroups.

<1>1. Quadratic extensions in characteristic 0 are Galois:
    *Proof:*
    <2>1. Let $K/F$ be an extension with $[K:F] = 2$ and $\operatorname{char}(F) = 0$.
    <2>2. Choose any $\alpha \in K \setminus F$. The minimal polynomial of $\alpha$ over $F$ is a quadratic $f(x) = x^2 + bx + c \in F[x]$.
    <2>3. The other root of $f(x)$ is $-b - \alpha \in K$.
    <2>4. Thus $K = F(\alpha)$ contains all roots of the irreducible polynomial $f(x)$, so $K/F$ is normal.
    <2>5. Since $\operatorname{char}(F) = 0$, $K/F$ is separable.
    <2>6. Hence $K/F$ is Galois with $\operatorname{Gal}(K/F) \cong \mathbb{Z}/2\mathbb{Z}$.

<1>2. Towers of quadratic extensions need not be Galois over the base field:
    *Proof:*
    <2>1. Consider the tower $\mathbb{Q} \subset \mathbb{Q}(\sqrt{2}) \subset \mathbb{Q}(\sqrt{1 + \sqrt{2}})$.
    <2>2. **Step 1:** $[\mathbb{Q}(\sqrt{2}) : \mathbb{Q}] = 2$ is Galois.
    <2>3. **Step 2:** Let $L = \mathbb{Q}(\sqrt{1 + \sqrt{2}})$. The element $\alpha = \sqrt{1 + \sqrt{2}}$ satisfies $\alpha^2 = 1 + \sqrt{2} \in \mathbb{Q}(\sqrt{2})$, and $\sqrt{1 + \sqrt{2}} \notin \mathbb{Q}(\sqrt{2})$ (since $1 + \sqrt{2}$ is not a square in $\mathbb{Q}(\sqrt{2})$). Thus $[L : \mathbb{Q}(\sqrt{2})] = 2$, which is Galois over $\mathbb{Q}(\sqrt{2})$.
    <2>4. **Failure over $\mathbb{Q}$:** The minimal polynomial of $\alpha$ over $\mathbb{Q}$ is $(x^2 - 1)^2 - 2 = x^4 - 2x^2 - 1$.
    <2>5. The four roots of $x^4 - 2x^2 - 1$ are $\pm \sqrt{1 + \sqrt{2}}$ (real) and $\pm \sqrt{1 - \sqrt{2}} = \pm i\sqrt{\sqrt{2} - 1}$ (non-real).
    <2>6. Since $L \subset \mathbb{R}$, $L$ contains the two real roots but none of the non-real roots.
    <2>7. Therefore, $L/\mathbb{Q}$ is not normal, hence not Galois over $\mathbb{Q}$.

<1>3. Group-theoretic analogue: Non-transitivity of normal subgroups:
    *Proof:*
    <2>1. By the Fundamental Theorem of Galois Theory, an intermediate extension $E/F$ inside a Galois extension $M/F$ is Galois over $F$ if and only if $\operatorname{Gal}(M/E) \trianglelefteq \operatorname{Gal}(M/F)$ is a normal subgroup.
    <2>2. In our tower $F \subset K \subset L$:
        - $K/F$ Galois corresponds to $\operatorname{Gal}(M/K) \trianglelefteq \operatorname{Gal}(M/F)$.
        - $L/K$ Galois corresponds to $\operatorname{Gal}(M/L) \trianglelefteq \operatorname{Gal}(M/K)$.
    <2>3. For $L/F$ to be Galois, we would need $\operatorname{Gal}(M/L) \trianglelefteq \operatorname{Gal}(M/F)$.
    <2>4. Thus, the failure of $L/F$ to be Galois reflects the fundamental group-theoretic fact that **normality of subgroups is not transitive**:
        $$H \trianglelefteq K \text{ and } K \trianglelefteq G \centernot\implies H \trianglelefteq G.$$
    <2>5. (Concrete group counterexample: $H = \langle (1\,2)(3\,4) \rangle \trianglelefteq V_4 \trianglelefteq A_4$, but $H \not\trianglelefteq A_4$).

<1>4. Conclusion:
    Single quadratics are always Galois, quadratic towers need not be (e.g. $\mathbb{Q}(\sqrt{1+\sqrt{2}})/\mathbb{Q}$), reflecting the non-transitivity of normal subgroups in group theory. Q.E.D.
:::
