---
schema: qual/card@1
id: P-XFXYS
kind: problem
title: A rng with a surjective right-multiplication map has a maximal left ideal
classification:
  areas:
  - algebra
  topics:
  - Maximal Ideals
  - Ideals
  - Zorn's Lemma
relations: []
review: draft
---

::: problem
Let $R$ be a rng (a ring not assumed to have an identity $1$) with $R \ne \{0\}$, and suppose $R$ contains an element $u \in R$ such that for all $y \in R$, there exists an $x \in R$ with $x u = y$ (that is, $R u = R$).

Prove that $R$ contains a maximal left ideal.
:::

::: solution
**Goal:** Prove the existence of a maximal left ideal in $R$ via Zorn's lemma by observing that any left ideal containing $u$ must equal $R$.

<1>1. Key Lemma: Any left ideal containing $u$ is all of $R$.
::: {.proof}
    <2>1. Let $I \subseteq R$ be a left ideal of $R$ such that $u \in I$.
    <2>2. Since $I$ is closed under left multiplication by elements of $R$, $R u \subseteq I$.
    <2>3. By hypothesis, the right-multiplication map by $u$ is surjective, so $R u = R$.
    <2>4. Therefore $R \subseteq I$, which forces $I = R$.
    <2>5. Contrapositively, if $I$ is a proper left ideal ($I \subsetneq R$), then $u \notin I$.

:::

<1>2. Definition of the poset $\mathcal{P}$:
::: {.proof}
    <2>1. Define the collection of left ideals:
    $$\mathcal{P} = \{I \subseteq R \mid I \text{ is a left ideal of } R \text{ and } u \notin I\},$$
    partially ordered by subset inclusion $\subseteq$.
    <2>2. $\mathcal{P}$ is non-empty:
        - The zero ideal $\{0\}$ is a left ideal of $R$.
        - If $u \in \{0\}$, then $u = 0$, which would imply $R = R u = R \cdot 0 = \{0\}$, contradicting $R \ne \{0\}$.
        - Thus $u \ne 0$, so $u \notin \{0\}$.
        - Hence $\{0\} \in \mathcal{P}$.

:::

<1>3. Every non-empty chain in $\mathcal{P}$ has an upper bound in $\mathcal{P}$:
::: {.proof}
    <2>1. Let $\mathcal{C} \subseteq \mathcal{P}$ be a non-empty totally ordered chain of left ideals in $\mathcal{P}$.
    <2>2. Define $J = \bigcup_{I \in \mathcal{C}} I$.
    <2>3. $J$ is a left ideal of $R$:
        - For $a, b \in J$, there exist $I_1, I_2 \in \mathcal{C}$ with $a \in I_1$ and $b \in I_2$.
        - Since $\mathcal{C}$ is a chain, either $I_1 \subseteq I_2$ or $I_2 \subseteq I_1$. WLOG, $I_1 \subseteq I_2$, so $a, b \in I_2$.
        - Since $I_2$ is an ideal, $a - b \in I_2 \subseteq J$.
        - For any $r \in R$ and $a \in J$, choose $I \in \mathcal{C}$ with $a \in I$. Since $I$ is a left ideal, $r a \in I \subseteq J$.
    <2>4. $u \notin J$:
        - If $u \in J = \bigcup_{I \in \mathcal{C}} I$, then $u \in I$ for some $I \in \mathcal{C}$.
        - But every $I \in \mathcal{C} \subseteq \mathcal{P}$ satisfies $u \notin I$, a contradiction.
    <2>5. Thus $J \in \mathcal{P}$, and $J$ is an upper bound for the chain $\mathcal{C}$.

:::

<1>4. Existence of a maximal element in $\mathcal{P}$ and proof that it is a maximal left ideal:
::: {.proof}
    <2>1. By Zorn's Lemma, the poset $\mathcal{P}$ contains at least one maximal element, say $M \in \mathcal{P}$.
    <2>2. Since $M \in \mathcal{P}$, $M$ is a left ideal and $u \notin M$, so $M \subsetneq R$ is a proper left ideal.
    <2>3. Suppose $L$ is a left ideal of $R$ such that $M \subsetneq L \subseteq R$.
    <2>4. By maximality of $M$ in $\mathcal{P}$, $L$ cannot belong to $\mathcal{P}$.
    <2>5. Since $L$ is a left ideal, $L \notin \mathcal{P}$ implies $u \in L$.
    <2>6. By <1>1, $u \in L \implies L = R$.
    <2>7. Thus there are no left ideals strictly between $M$ and $R$, which proves that $M$ is a maximal left ideal of $R$.

:::

<1>5. Conclusion:
::: {.proof}
    $R$ contains a maximal left ideal.
:::
:::
