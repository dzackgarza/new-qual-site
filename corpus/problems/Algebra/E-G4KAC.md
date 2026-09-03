---
schema: qual/card@1
id: E-G4KAC
kind: problem
title: $x\in J(R)\iff 1-xR\subseteq R^\times$
classification:
  areas:
  - algebra
  topics:
  - Jacobson Radical
  - Rings
  - Ideals
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
---

::: {.exercise}
Let $R$ be a ring with identity. Prove that an element $x \in R$ belongs to the Jacobson radical $J(R)$ if and only if $1 - x r \in R^\times$ for all $r \in R$ (i.e. $1 - x R \subseteq R^\times$).
:::

::: solution
**Goal:** Prove the characterization $x \in J(R) \iff 1 - xr \in R^\times$ for all $r \in R$, where $J(R) = \bigcap_{\mathfrak{m} \text{ maximal left ideal}} \mathfrak{m}$.

<1>1. Direction $(\implies)$: $x \in J(R) \implies 1 - xr \in R^\times$ for all $r \in R$:
    *Proof:*
    <2>1. Let $x \in J(R)$ and let $r \in R$ be arbitrary.
    <2>2. We first show that $1 - xr$ has a left inverse:
        - Consider the left ideal $L = R(1 - xr)$.
        - If $L \ne R$, then by Zorn's Lemma, $L$ is contained in some maximal left ideal $\mathfrak{m} \subset R$.
        - Thus $1 - xr \in \mathfrak{m}$.
        - Since $x \in J(R) \subseteq \mathfrak{m}$, the left ideal property gives $xr \in \mathfrak{m}$.
        - Therefore, $1 = (1 - xr) + xr \in \mathfrak{m}$, which implies $\mathfrak{m} = R$, contradicting the properness of $\mathfrak{m}$.
        - Thus $L = R$, meaning $1 \in R(1 - xr)$, so there exists $u \in R$ such that $u(1 - xr) = 1$.
    <2>3. We now show that $u$ is a two-sided unit:
        - From $u(1 - xr) = 1$, we have $u - uxr = 1 \implies 1 - u = -uxr$.
        - Since $x \in J(R)$ and $J(R)$ is a two-sided ideal, $uxr \in J(R)$, so $1 - u \in J(R)$.
        - By the same argument applied to $y = 1 - u \in J(R)$, $1 - y = u$ must have a left inverse $v \in R$ such that $vu = 1$.
        - Since $vu = 1$ and $u(1 - xr) = 1$, we have $1 - xr = (vu)(1 - xr) = v(u(1 - xr)) = v(1) = v$.
        - Thus $(1 - xr)u = 1$, proving $u = (1 - xr)^{-1}$ is a two-sided inverse.
    <2>4. Hence $1 - xr \in R^\times$.

<1>2. Direction $(\impliedby)$: $1 - xR \subseteq R^\times \implies x \in J(R)$:
    *Proof:*
    <2>1. Suppose $1 - xr \in R^\times$ for all $r \in R$.
    <2>2. We must show that $x \in \mathfrak{m}$ for every maximal left ideal $\mathfrak{m}$ of $R$.
    <2>3. Suppose, for contradiction, that $x \notin \mathfrak{m}$ for some maximal left ideal $\mathfrak{m}$.
    <2>4. Because $\mathfrak{m}$ is maximal and $x \notin \mathfrak{m}$, the left ideal $\mathfrak{m} + Rx$ strictly contains $\mathfrak{m}$, so:
        $$\mathfrak{m} + Rx = R.$$
    <2>5. In particular, $1 \in \mathfrak{m} + Rx$, so there exist $m \in \mathfrak{m}$ and $r \in R$ such that:
        $$m + rx = 1 \implies m = 1 - rx.$$
    <2>6. By hypothesis, $1 - rx \in R^\times$ is a unit.
    <2>7. Thus $m \in \mathfrak{m}$ is a unit, which forces $\mathfrak{m} = R$, contradicting that $\mathfrak{m}$ is a proper (maximal) left ideal!
    <2>8. Therefore, $x \in \mathfrak{m}$ for every maximal left ideal $\mathfrak{m}$.
    <2>9. Thus $x \in \bigcap \mathfrak{m} = J(R)$.

<1>3. Conclusion:
    $x \in J(R) \iff 1 - xR \subseteq R^\times$. Q.E.D.
:::
