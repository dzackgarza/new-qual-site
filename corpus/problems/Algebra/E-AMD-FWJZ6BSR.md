---
schema: qual/card@1
id: E-AMD-FWJZ6BSR
kind: exercise
title: Every ring has a proper maximal ideal
classification:
  areas:
  - algebra
  topics:
  - Maximal Ideals
  - Ideals
  - Zorn's Lemma
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
---

::: {.exercise}
Show that every non-zero ring with identity has a proper maximal ideal.
:::

::: solution
**Goal:** Prove Krull's Theorem: every non-zero ring $R$ with identity $1_R \neq 0$ contains at least one maximal ideal.

<1>1. Definition of the poset of proper ideals:
    *Proof:*
    <2>1. Let $\mathcal{P}$ be the set of all proper ideals of $R$:
        $$\mathcal{P} = \{ I \subseteq R \mid I \text{ is an ideal of } R \text{ and } I \neq R\}.$$
    <2>2. We partially order $\mathcal{P}$ by set inclusion $\subseteq$.
    <2>3. Because $1_R \neq 0$, the zero ideal $(0)$ is proper ($1_R \notin (0)$), so $(0) \in \mathcal{P}$.
    <2>4. Thus $\mathcal{P} \neq \varnothing$.

<1>2. Verification of Zorn's Lemma hypothesis for chains:
    *Proof:*
    <2>1. Let $\mathcal{C} = \{I_\alpha\}_{\alpha \in A}$ be an arbitrary non-empty chain (totally ordered subset) in $\mathcal{P}$.
    <2>2. Define $J = \bigcup_{\alpha \in A} I_\alpha$.
    <2>3. **$J$ is an additive subgroup:** For $x, y \in J$, there exist $\alpha, \beta \in A$ such that $x \in I_\alpha$ and $y \in I_\beta$.
        Since $\mathcal{C}$ is a chain, without loss of generality $I_\alpha \subseteq I_\beta$, so $x, y \in I_\beta$.
        Since $I_\beta$ is an ideal, $x - y \in I_\beta \subseteq J$.
    <2>4. **$J$ absorbs multiplication:** For $r \in R$ and $x \in J$, $x \in I_\alpha$ for some $\alpha$, so $rx, xr \in I_\alpha \subseteq J$.
    <2>5. **$J$ is proper ($J \neq R$):** An ideal in a ring with $1$ is proper if and only if it does not contain $1_R$.
        If $1_R \in J$, then $1_R \in I_\alpha$ for some $\alpha \in A$, contradicting the fact that $I_\alpha \in \mathcal{P}$ is proper.
        Hence $1_R \notin J$, so $J$ is a proper ideal ($J \in \mathcal{P}$).
    <2>6. By construction, $I_\alpha \subseteq J$ for all $\alpha \in A$, so $J$ is an upper bound for the chain $\mathcal{C}$ in $\mathcal{P}$.

<1>3. Existence of a maximal element:
    *Proof:*
    <2>1. Since every chain in $\mathcal{P}$ has an upper bound in $\mathcal{P}$, Zorn's Lemma implies that $\mathcal{P}$ has a maximal element $\mathfrak{m}$.
    <2>2. By definition of $\mathcal{P}$, $\mathfrak{m}$ is a proper ideal of $R$, and there exists no proper ideal of $R$ strictly containing $\mathfrak{m}$.
    <2>3. Therefore $\mathfrak{m}$ is a maximal ideal of $R$.

<1>4. Conclusion:
    Every non-zero ring with identity contains a proper maximal ideal. Q.E.D.
:::

::: {.solution}
<1>1. $H$ subgroup.
Proof: Sylow.

<1>2. Q.E.D.
Proof: <1>1.
:::
