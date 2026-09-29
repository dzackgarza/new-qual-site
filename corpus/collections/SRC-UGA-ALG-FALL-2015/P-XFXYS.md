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

::: {.problem}
Let $R$ be a rng (a ring not assumed to have an identity $1$) with $R \ne \{0\}$, and suppose $R$ contains an element $u \in R$ such that for all $y \in R$, there exists an $x \in R$ with $x u = y$ (that is, $R u = R$).

Prove that $R$ contains a maximal left ideal.
:::

::: {.solution}
**Goal:** Prove the existence of a maximal left ideal in $R$ via Zorn's lemma by observing that any left ideal containing $u$ must equal $R$.

::: pf

::: {.pf-step #s1}
Key Lemma: Any left ideal containing $u$ is all of $R$.

::: pf-proof

::: pf-step
Let $I \subseteq R$ be a left ideal of $R$ such that $u \in I$.
:::

::: pf-step
Since $I$ is closed under left multiplication by elements of $R$, $R u \subseteq I$.
:::

::: pf-step
By hypothesis, the right-multiplication map by $u$ is surjective, so $R u = R$.
:::

::: pf-step
Therefore $R \subseteq I$, which forces $I = R$.
:::

::: pf-step
Contrapositively, if $I$ is a proper left ideal ($I \subsetneq R$), then $u \notin I$.
:::

:::

:::

::: pf-step
Definition of the poset $\mathcal{P}$:

::: pf-proof

::: pf-step
Define the collection of left ideals:
$$\mathcal{P} = \{I \subseteq R \mid I \text{ is a left ideal of } R \text{ and } u \notin I\},$$
partially ordered by subset inclusion $\subseteq$.
:::

::: pf-step
$\mathcal{P}$ is non-empty:

- The zero ideal $\{0\}$ is a left ideal of $R$.
- If $u \in \{0\}$, then $u = 0$, which would imply $R = R u = R \cdot 0 = \{0\}$, contradicting $R \ne \{0\}$.
- Thus $u \ne 0$, so $u \notin \{0\}$.
- Hence $\{0\} \in \mathcal{P}$.
:::

:::

:::

::: pf-step
Every non-empty chain in $\mathcal{P}$ has an upper bound in $\mathcal{P}$:

::: pf-proof

::: pf-step
Let $\mathcal{C} \subseteq \mathcal{P}$ be a non-empty totally ordered chain of left ideals in $\mathcal{P}$.
:::

::: pf-step
Define $J = \bigcup_{I \in \mathcal{C}} I$.
:::

::: pf-step
$J$ is a left ideal of $R$:

- For $a, b \in J$, there exist $I_1, I_2 \in \mathcal{C}$ with $a \in I_1$ and $b \in I_2$.
- Since $\mathcal{C}$ is a chain, either $I_1 \subseteq I_2$ or $I_2 \subseteq I_1$. WLOG, $I_1 \subseteq I_2$, so $a, b \in I_2$.
- Since $I_2$ is an ideal, $a - b \in I_2 \subseteq J$.
- For any $r \in R$ and $a \in J$, choose $I \in \mathcal{C}$ with $a \in I$. Since $I$ is a left ideal, $r a \in I \subseteq J$.
:::

::: pf-step
$u \notin J$:

- If $u \in J = \bigcup_{I \in \mathcal{C}} I$, then $u \in I$ for some $I \in \mathcal{C}$.
- But every $I \in \mathcal{C} \subseteq \mathcal{P}$ satisfies $u \notin I$, a contradiction.
:::

::: pf-step
Thus $J \in \mathcal{P}$, and $J$ is an upper bound for the chain $\mathcal{C}$.
:::

:::

:::

::: pf-step
Existence of a maximal element in $\mathcal{P}$ and proof that it is a maximal left ideal:

::: pf-proof

::: pf-step
By Zorn's Lemma, the poset $\mathcal{P}$ contains at least one maximal element, say $M \in \mathcal{P}$.
:::

::: pf-step
Since $M \in \mathcal{P}$, $M$ is a left ideal and $u \notin M$, so $M \subsetneq R$ is a proper left ideal.
:::

::: pf-step
Suppose $L$ is a left ideal of $R$ such that $M \subsetneq L \subseteq R$.
:::

::: pf-step
By maximality of $M$ in $\mathcal{P}$, $L$ cannot belong to $\mathcal{P}$.
:::

::: pf-step
Since $L$ is a left ideal, $L \notin \mathcal{P}$ implies $u \in L$.
:::

::: pf-step
By step [](#s1){.pf-ref}, $u \in L \implies L = R$.
:::

::: pf-step
Thus there are no left ideals strictly between $M$ and $R$, which proves that $M$ is a maximal left ideal of $R$.
:::

:::

:::

::: pf-step
Conclusion:

::: pf-proof
$R$ contains a maximal left ideal.
:::

:::

:::
:::
