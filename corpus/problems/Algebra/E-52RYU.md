---
schema: qual/card@1
id: E-52RYU
kind: problem
title: Irreducible with a root in a splitting field splits completely
classification:
  areas:
  - algebra
  topics:
  - Splitting Fields
  - Field Extensions
  - Irreducibility Criteria
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
---

::: problem
Let $F$ be the splitting field of $f \in K[x]$ over $K$.
Prove that if $g \in K[x]$ is irreducible and has a root in $F$, then $g$ splits into linear factors over $F$.
:::

::: solution
**Goal:** Prove that if $F/K$ is a normal extension (e.g. the splitting field of a polynomial $f \in K[x]$) and $g \in K[x]$ is irreducible with a root $\alpha \in F$, then all roots of $g$ lie in $F$.

<1>1. Splitting fields are normal extensions:
    *Proof:*
    <2>1. By definition, $F$ is generated over $K$ by all the roots of $f(x) \in K[x]$.
    <2>2. **Theorem (Normality of splitting fields):** Any splitting field of a polynomial over $K$ is a **normal extension** of $K$.
    <2>3. That is, for every algebraic extension $F/K$, $F/K$ is normal if and only if every irreducible polynomial $g \in K[x]$ that has at least one root in $F$ splits completely into linear factors in $F[x]$.

<1>2. Direct field-theoretic proof:
    *Proof:*
    <2>1. Let $\alpha \in F$ be a root of the irreducible polynomial $g(x) \in K[x]$.
    <2>2. Let $\beta \in \overline{K}$ be any other root of $g(x)$ in an algebraic closure $\overline{K}$ of $F$.
    <2>3. Because $g(x)$ is irreducible over $K$, there exists a $K$-isomorphism of fields:
        $$\sigma: K(\alpha) \xrightarrow{\sim} K(\beta) \quad \text{such that } \sigma(\alpha) = \beta \text{ and } \sigma|_K = \operatorname{id}_K.$$
    <2>4. Note that $F = K(\alpha_1, \dots, \alpha_n)$ where $\alpha_1, \dots, \alpha_n$ are the roots of $f(x)$.
    <2>5. The field $F(\alpha) = F$ is the splitting field of $f(x)$ over $K(\alpha)$.
    <2>6. The field $F(\beta)$ is the splitting field of $\sigma(f)(x) = f(x)$ over $K(\beta)$.
    <2>7. By the Isomorphism Extension Theorem for splitting fields, the isomorphism $\sigma: K(\alpha) \to K(\beta)$ extends to an isomorphism of splitting fields:
        $$\widetilde{\sigma}: F(\alpha) \xrightarrow{\sim} F(\beta) \quad \text{such that } \widetilde{\sigma}|_{K(\alpha)} = \sigma.$$
    <2>8. Since $\alpha \in F$, $F(\alpha) = F$.
    <2>9. Therefore $[F(\beta) : K] = [F(\alpha) : K] = [F : K]$.
    <2>10. Since $F \subseteq F(\beta)$ and they have the same finite degree over $K$, we must have $F(\beta) = F$.
    <2>11. In particular, $\beta \in F$.

<1>3. Conclusion:
    Since every root $\beta$ of $g(x)$ in $\overline{K}$ lies in $F$, $g(x)$ splits completely into linear factors over $F$. Q.E.D.
:::
