---
schema: qual/card@1
id: P-6KHMF
kind: problem
title: Maximal ideals, non-units, and prime annihilators of module elements
classification:
  areas:
  - algebra
  topics:
  - Maximal Ideals
  - Prime Ideals
  - Modules
relations: []
review: draft
---

::: {.problem}
Let $R$ be a commutative ring with identity $1 \ne 0$.

(a) Define a **maximal ideal** and prove that $R$ contains at least one maximal ideal.

(b) Show that an element $r \in R$ is not invertible if and only if $r$ is contained in some maximal ideal of $R$.

(c) Let $M$ be an $R$-module. For any $m \in M$, the **annihilator** of $m$ is the ideal
$$
\operatorname{Ann}(m) = \{r \in R : r m = 0\}.
$$
Suppose that $I = \operatorname{Ann}(\mu)$ for some non-zero element $\mu \in M \setminus \{0\}$ is maximal among all proper annihilator ideals $\{\operatorname{Ann}(m) : m \in M, \, m \ne 0\}$. Prove that $I$ is a prime ideal of $R$.
:::

::: {.solution}
**Goal:** Define maximal ideals and prove their existence via Zorn's Lemma in (a), characterize non-units via containment in maximal ideals in (b), and prove that maximal element-annihilators are prime ideals in (c).

::: pf

::: {.pf-step #s1}
Part (a): Definition of maximal ideal and existence via Zorn's Lemma.

::: pf-proof

::: pf-step
An ideal $\mathfrak{m} \subset R$ is a maximal ideal if $\mathfrak{m} \ne R$ (i.e. $\mathfrak{m}$ is a proper ideal) and the only ideals containing $\mathfrak{m}$ are $\mathfrak{m}$ and $R$.
:::

::: pf-step
Define the family of proper ideals:
$$\mathcal{S} = \{I \subseteq R : I \text{ is an ideal of } R \text{ and } I \ne R\}.$$
:::

::: pf-step
Since $R \ne 0$, the zero ideal $\{0\} \ne R$, so $\{0\} \in \mathcal{S}$ and $\mathcal{S} \ne \emptyset$.
:::

::: pf-step
Partially order $\mathcal{S}$ by set inclusion $\subseteq$. Let $\mathcal{C} \subseteq \mathcal{S}$ be a non-empty totally ordered chain of proper ideals.
:::

::: pf-step
The union $J = \bigcup_{I \in \mathcal{C}} I$ is an ideal of $R$: for any $x, y \in J$ and $r \in R$, there exist $I_1, I_2 \in \mathcal{C}$ with $x \in I_1$ and $y \in I_2$. Since $\mathcal{C}$ is a chain, assume without loss of generality that $I_1 \subseteq I_2$. Then $x, y \in I_2$, so $x - y \in I_2 \subseteq J$ and $r x \in I_2 \subseteq J$.
:::

::: pf-step
The ideal $J$ is proper: if $J = R$, then $1 \in J = \bigcup_{I \in \mathcal{C}} I$, so $1 \in I_0$ for some $I_0 \in \mathcal{C}$, which would mean $I_0 = R$, contradicting $I_0 \in \mathcal{S}$. Thus $1 \notin J$, so $J \in \mathcal{S}$.
:::

::: pf-step
Since $J$ contains every $I \in \mathcal{C}$, $J$ is an upper bound for $\mathcal{C}$ in $\mathcal{S}$.
:::

::: pf-step
By Zorn's Lemma, $\mathcal{S}$ contains a maximal element $\mathfrak{m}$, which is a maximal ideal of $R$.
:::

:::

:::

::: pf-step
Part (b): Characterization of non-units by maximal ideals.

::: pf-proof

::: pf-step
($\impliedby$): Let $\mathfrak{m}$ be a maximal ideal and suppose $r \in \mathfrak{m}$. If $r$ were invertible (a unit), then $1 = r^{-1} r \in \mathfrak{m}$, which implies $\mathfrak{m} = R$, contradicting the definition of a maximal ideal ($\mathfrak{m} \ne R$). Thus $r$ is not invertible.
:::

::: pf-step
($\implies$): Suppose $r \in R$ is not invertible.
:::

::: pf-step
The principal ideal $\langle r \rangle = R r$ is a proper ideal of $R$, because $1 \in \langle r \rangle \iff r$ is invertible.
:::

::: pf-step
Define the family of proper ideals containing $\langle r \rangle$:
$$\mathcal{S}_r = \{J \subseteq R : J \text{ is an ideal of } R, \, \langle r \rangle \subseteq J, \text{ and } J \ne R\}.$$
:::

::: pf-step
Since $\langle r \rangle \in \mathcal{S}_r$, $\mathcal{S}_r \ne \emptyset$.
:::

::: pf-step
Exactly as in step [](#s1){.pf-ref}, every non-empty chain in $\mathcal{S}_r$ has its union as an upper bound in $\mathcal{S}_r$.
:::

::: pf-step
By Zorn's Lemma, $\mathcal{S}_r$ contains a maximal element $\mathfrak{m}$.
:::

::: pf-step
The ideal $\mathfrak{m}$ is a maximal ideal of $R$ containing $r$.
:::

:::

:::

::: pf-step
Part (c): Proof that maximal element-annihilator $I$ is prime.

::: pf-proof

::: pf-step
$I$ is a proper ideal: since $\mu \ne 0$, $1 \cdot \mu = \mu \ne 0$, so $1 \notin \operatorname{Ann}(\mu) = I$, which means $I \ne R$.
:::

::: pf-step
Let $a, b \in R$ such that $a b \in I$. We show that $a \in I$ or $b \in I$.
:::

::: pf-step
Suppose $b \notin I$. By definition of $I = \operatorname{Ann}(\mu)$, this means $b \mu \ne 0$ in $M$.
:::

::: pf-step
Define the element $\nu = b \mu \in M \setminus \{0\}$, and consider its annihilator $J = \operatorname{Ann}(\nu) = \operatorname{Ann}(b \mu)$.
:::

::: pf-step
$J$ is a proper ideal: since $\nu \ne 0$, $1 \notin J$.
:::

::: pf-step
Containment $I \subseteq J$: for any $x \in I = \operatorname{Ann}(\mu)$, $x \mu = 0$, so
$$x \nu = x (b \mu) = b (x \mu) = b \cdot 0 = 0,$$
which proves $x \in \operatorname{Ann}(\nu) = J$. Thus $I \subseteq J$.
:::

::: pf-step
Maximality of $I$: by hypothesis, $I$ is maximal among the set of all proper annihilator ideals of non-zero module elements. Since $J = \operatorname{Ann}(b \mu)$ is a proper annihilator ideal containing $I$, we must have $I = J = \operatorname{Ann}(b \mu)$.
:::

::: pf-step
Deducing $a \in I$: since $a b \in I = \operatorname{Ann}(\mu)$, we have $(a b)\mu = 0$.
:::

::: pf-step
Rewriting: $a (b \mu) = (a b) \mu = 0$, so $a \in \operatorname{Ann}(b \mu) = J$.
:::

::: pf-step
Since $J = I$, we conclude $a \in I$.
:::

::: pf-step
Therefore, $a b \in I \implies a \in I \lor b \in I$, so $I$ is a prime ideal of $R$.
:::

:::

:::

::: pf-step
Conclusion:

::: pf-proof
Maximal ideals exist by Zorn's Lemma, non-units are precisely elements in maximal ideals, and maximal element-annihilator ideals are prime.
:::

:::

:::
:::
