---
schema: qual/card@1
id: E-AMD-KDSJ3FW4
kind: problem
title: Every proper ideal is contained in a maximal ideal
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
Show that every proper ideal in a commutative ring with identity is contained in a maximal ideal.
:::

::: solution
**Goal:** Prove that every proper ideal $I \subsetneq R$ in a commutative ring with identity is contained in a maximal ideal.

<1>1. Setup for Zorn's Lemma:
    *Proof:*
    <2>1. Let $\mathcal{F} = \{J \subseteq R \mid J \text{ is a proper ideal of } R \text{ and } I \subseteq J\}$.
    <2>2. $\mathcal{F} \neq \varnothing$ because $I \in \mathcal{F}$.
    <2>3. Partially order $\mathcal{F}$ by inclusion.

<1>2. Verification of the chain condition:
    *Proof:*
    <2>1. Let $\{J_\alpha\}_{\alpha \in \Lambda}$ be a totally ordered chain in $\mathcal{F}$.
    <2>2. Define $J = \bigcup_{\alpha \in \Lambda} J_\alpha$.
    <2>3. **$J$ is an ideal:** For any $a, b \in J$, there exist $\alpha, \beta$ with $a \in J_\alpha, b \in J_\beta$. Since the chain is totally ordered, $J_\alpha \subseteq J_\beta$ or $J_\beta \subseteq J_\alpha$; in either case $a, b$ lie in a common $J_\gamma$, so $a - b \in J_\gamma \subseteq J$. For $r \in R$, $ra \in J_\alpha \subseteq J$.
    <2>4. **$J$ is proper:** If $1_R \in J$, then $1_R \in J_\alpha$ for some $\alpha$, which would make $J_\alpha = R$, contradicting $J_\alpha \in \mathcal{F}$. Thus $1_R \notin J$, so $J \neq R$.
    <2>5. **$I \subseteq J$:** $I \subseteq J_\alpha \subseteq J$ for every $\alpha$.
    <2>6. Thus $J \in \mathcal{F}$ is an upper bound for the chain.

<1>3. Application of Zorn's Lemma:
    *Proof:*
    <2>1. By Zorn's Lemma, $\mathcal{F}$ has a maximal element $\mathfrak{m}$.
    <2>2. By maximality in $\mathcal{F}$: $\mathfrak{m}$ is a proper ideal containing $I$, and there is no proper ideal strictly between $\mathfrak{m}$ and $R$.
    <2>3. This is exactly the definition of a maximal ideal.

<1>4. Conclusion:
    $I \subseteq \mathfrak{m}$ and $\mathfrak{m}$ is a maximal ideal of $R$. Q.E.D.
:::
