---
schema: qual/card@1
id: E-K4SU4
kind: exercise
title: $R_p$ is a local ring for $p\in\operatorname{Spec} R$
classification:
  areas:
  - algebra
  topics:
  - Localization
  - Local Rings
  - Prime Ideals
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
---

::: {.exercise}
Show that if $\mathfrak{p} \in \operatorname{Spec}(R)$, then the localization $R_\mathfrak{p}$ is a local ring with unique maximal ideal $\mathfrak{p} R_\mathfrak{p}$.
:::

::: solution
**Goal:** Prove that the localization of a commutative ring $R$ at a prime ideal $\mathfrak{p} \in \operatorname{Spec}(R)$ is a local ring with unique maximal ideal $\mathfrak{m} = \mathfrak{p} R_\mathfrak{p}$.

<1>1. Setting up the localization:
    *Proof:*
    <2>1. Let $R$ be a commutative ring with $1$, and $\mathfrak{p} \subset R$ a prime ideal.
    <2>2. The set $S = R \setminus \mathfrak{p}$ is multiplicatively closed: $1 \in S$ (since $\mathfrak{p} \ne R$), and for any $s_1, s_2 \in S$, $s_1 s_2 \notin \mathfrak{p}$ (by definition of a prime ideal), so $s_1 s_2 \in S$.
    <2>3. The localization is $R_\mathfrak{p} = S^{-1}R = \{r/s \mid r \in R, s \in S\} / \sim$.

<1>2. The ideal $\mathfrak{p} R_\mathfrak{p}$:
    *Proof:*
    <2>1. Define $\mathfrak{m} = \mathfrak{p} R_\mathfrak{p} = \{a/s \mid a \in \mathfrak{p}, s \in S\}$.
    <2>2. **$\mathfrak{m}$ is an ideal:** For $a_1/s_1, a_2/s_2 \in \mathfrak{m}$ and $r/s \in R_\mathfrak{p}$:
        $$\frac{a_1}{s_1} + \frac{a_2}{s_2} = \frac{a_1 s_2 + a_2 s_1}{s_1 s_2} \in \mathfrak{m} \quad (\text{since } a_1 s_2 + a_2 s_1 \in \mathfrak{p}),$$
        $$\frac{r}{s} \cdot \frac{a_1}{s_1} = \frac{r a_1}{s s_1} \in \mathfrak{m} \quad (\text{since } r a_1 \in \mathfrak{p}).$$
    <2>3. **$\mathfrak{m}$ is proper:** $1/1 \in \mathfrak{m} \iff 1 \cdot u \in \mathfrak{p}$ for some $u \in S$, which means $u \in \mathfrak{p} \cap S = \varnothing$, a contradiction. Thus $1 \notin \mathfrak{m}$, so $\mathfrak{m} \subsetneq R_\mathfrak{p}$.

<1>3. Every element in $R_\mathfrak{p} \setminus \mathfrak{m}$ is a unit:
    *Proof:*
    <2>1. Let $x = r/s \in R_\mathfrak{p} \setminus \mathfrak{m}$.
    <2>2. By definition of $\mathfrak{m}$, $r \notin \mathfrak{p}$, which means $r \in S = R \setminus \mathfrak{p}$.
    <2>3. Since $r \in S$, the fraction $s/r$ is a valid element of $R_\mathfrak{p} = S^{-1}R$.
    <2>4. Then:
        $$\frac{r}{s} \cdot \frac{s}{r} = \frac{rs}{sr} = \frac{1}{1}.$$
    <2>5. Thus $x = r/s$ is invertible in $R_\mathfrak{p}$, with inverse $x^{-1} = s/r$.

<1>4. Uniqueness of the maximal ideal:
    *Proof:*
    <2>1. Let $I \subsetneq R_\mathfrak{p}$ be any proper ideal of $R_\mathfrak{p}$.
    <2>2. If $I$ contained any element $x \in R_\mathfrak{p} \setminus \mathfrak{m}$, then $x$ would be a unit, forcing $I = R_\mathfrak{p}$, contradicting properness.
    <2>3. Therefore, every element of $I$ must lie in $\mathfrak{m}$, which proves $I \subseteq \mathfrak{m}$.
    <2>4. Thus $\mathfrak{m}$ is the unique maximal ideal of $R_\mathfrak{p}$.

<1>5. Conclusion:
    $R_\mathfrak{p}$ is a local ring with unique maximal ideal $\mathfrak{p} R_\mathfrak{p}$. Q.E.D.
:::
