---
schema: qual/card@1
id: P-UWYTU
kind: problem
title: Cyclic extensions of prime order $p$
classification:
  areas:
  - algebra
  topics:
  - Galois Theory
  - Cyclic Groups
  - Field Extensions
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
---

::: problem
What are the cyclic extensions of prime degree $p$?
:::

::: solution
**Goal:** Classify all cyclic Galois extensions $K/F$ of prime degree $p = [K:F]$ using Kummer theory and Artin-Schreier theory.

<1>1. Case 1: Characteristic not equal to $p$, containing primitive $p$-th roots of unity (Kummer Theory):
    *Proof:*
    <2>1. Assume $\operatorname{char}(F) \ne p$ and $\mu_p \subseteq F$ (where $\mu_p$ is the group of $p$-th roots of unity).
    <2>2. **Theorem (Kummer):** Every cyclic extension $K/F$ of degree $p$ is of the form:
        $$K = F(\sqrt[p]{a}) = F(\alpha) \quad \text{where } \alpha^p = a \in F^\times,$$
        and $a \notin (F^\times)^p$ (i.e. $a$ is not a $p$-th power in $F$).
    <2>3. Two elements $a, b \in F^\times$ generate the same extension $F(\sqrt[p]{a}) = F(\sqrt[p]{b})$ if and only if $a$ and $b$ generate the same subgroup of $F^\times / (F^\times)^p$.
    <2>4. The isomorphism $\operatorname{Gal}(K/F) \cong \mathbb{Z}/p\mathbb{Z}$ is given by $\sigma(\alpha) = \zeta_p \alpha$ for a primitive root $\zeta_p \in F$.

<1>2. Case 2: Characteristic not equal to $p$, not containing primitive $p$-th roots of unity:
    *Proof:*
    <2>1. If $\mu_p \not\subseteq F$, one passes to the cyclotomic extension $F(\zeta_p)$.
    <2>2. Any cyclic degree $p$ extension $K/F$ gives a Kummer extension $K(\zeta_p) / F(\zeta_p)$ of degree $p$, where $K(\zeta_p) = F(\zeta_p)(\sqrt[p]{a})$ for some $a \in F(\zeta_p)^\times$, subject to the condition that the Galois action of $\operatorname{Gal}(F(\zeta_p)/F)$ on $\langle a \pmod{(F(\zeta_p)^\times)^p} \rangle$ matches the cyclotomic character.

<1>3. Case 3: Characteristic equal to $p$ (Artin–Schreier Theory):
    *Proof:*
    <2>1. Assume $\operatorname{char}(F) = p > 0$.
    <2>2. **Theorem (Artin–Schreier):** Every cyclic extension $K/F$ of degree $p$ is of the form:
        $$K = F(\alpha) \quad \text{where } \alpha^p - \alpha = a \in F,$$
        and $a \notin \wp(F)$, where $\wp: F \to F$ is the Artin-Schreier operator $\wp(x) = x^p - x$.
    <2>3. The roots of $x^p - x - a$ are $\alpha, \alpha + 1, \dots, \alpha + (p - 1)$.
    <2>4. The generator $\sigma \in \operatorname{Gal}(K/F) \cong \mathbb{Z}/p\mathbb{Z}$ acts by $\sigma(\alpha) = \alpha + 1$.
    <2>5. Two elements $a, b \in F$ generate the same extension $F(\wp^{-1}(a)) = F(\wp^{-1}(b))$ if and only if $a \equiv kb \pmod{\wp(F)}$ for some $k \in (\mathbb{F}_p)^\times$.

<1>4. Conclusion:
    - If $\operatorname{char}(F) \ne p$ and $\mu_p \subseteq F$: $K = F(\sqrt[p]{a})$ for $a \in F^\times \setminus (F^\times)^p$ (Kummer extensions).
    - If $\operatorname{char}(F) = p$: $K = F(\alpha)$ with $\alpha^p - \alpha = a \in F \setminus \wp(F)$ (Artin-Schreier extensions).
    Q.E.D.
:::
