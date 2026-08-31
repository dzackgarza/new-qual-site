---
schema: qual/card@1
id: P-UKZE6
kind: problem
title: Every proper ideal lies in a maximal ideal; $x\in J(R)$ iff $1+rx$ is a unit;
  $J(R)$ consists of the nilpotents when $R$ is finite
classification:
  areas:
  - algebra
  topics:
  - Jacobson Radical
  - Maximal Ideals
  - Nilpotence
relations: []
review: draft
---

::: problem
Let $R$ be a commutative ring with identity $1 \ne 0$.

(a) Show that every proper ideal of $R$ is contained in at least one maximal ideal.

(b) Let $J(R) = \bigcap_{\mathfrak{m} \in \operatorname{MaxSpec}(R)} \mathfrak{m}$ denote the Jacobson radical of $R$. Show that $x \in J(R)$ if and only if $1 + r x$ is a unit in $R$ for all $r \in R$.

(c) Suppose that $R$ is a finite ring. Show that $J(R) = \operatorname{Nil}(R)$, the set of all nilpotent elements of $R$.
:::

::: solution
**Goal:** Prove Krull's existence theorem for maximal ideals containing a given proper ideal in (a), characterize the Jacobson radical via units in (b), and prove $J(R) = \operatorname{Nil}(R)$ for finite commutative rings in (c).

<1>1. Part (a): Every proper ideal is contained in a maximal ideal.
    *Proof:*
    <2>1. Let $I \subsetneq R$ be a proper ideal of $R$.
    <2>2. Define the family of proper ideals of $R$ containing $I$:
    $$\mathcal{S} = \{J \subseteq R : J \text{ is an ideal of } R, \, I \subseteq J, \text{ and } J \ne R\}.$$
    <2>3. Since $I \in \mathcal{S}$, $\mathcal{S}$ is non-empty. Partially order $\mathcal{S}$ by inclusion $\subseteq$.
    <2>4. Let $\mathcal{C} \subseteq \mathcal{S}$ be a non-empty totally ordered chain of ideals.
    <2>5. The union $J_0 = \bigcup_{J \in \mathcal{C}} J$ is an ideal containing $I$: for any $x, y \in J_0$ and $r \in R$, choose $J_1, J_2 \in \mathcal{C}$ with $x \in J_1, y \in J_2$. Assuming without loss of generality $J_1 \subseteq J_2$, $x, y \in J_2$, so $x - y \in J_2 \subseteq J_0$ and $r x \in J_2 \subseteq J_0$.
    <2>6. $J_0$ is proper: if $1 \in J_0$, then $1 \in J'$ for some $J' \in \mathcal{C}$, which would mean $J' = R$, contradicting $J' \in \mathcal{S}$. Thus $1 \notin J_0$, so $J_0 \ne R$ and $J_0 \in \mathcal{S}$.
    <2>7. Thus $J_0$ is an upper bound for $\mathcal{C}$ in $\mathcal{S}$.
    <2>8. By Zorn's Lemma, $\mathcal{S}$ contains a maximal element $\mathfrak{m}$, which is a maximal ideal of $R$ containing $I$.

<1>2. Part (b): $x \in J(R) \iff 1 + r x \in R^\times$ for all $r \in R$.
    *Proof:*
    <2>1. ($\implies$): Assume $x \in J(R)$, so $x \in \mathfrak{m}$ for every maximal ideal $\mathfrak{m}$.
        *Proof:* Let $r \in R$. Suppose for contradiction that $1 + r x$ is not a unit. Then the principal ideal $\langle 1 + r x \rangle$ is proper. By Part (a), $\langle 1 + r x \rangle \subseteq \mathfrak{m}_0$ for some maximal ideal $\mathfrak{m}_0$. Since $x \in J(R)$, $x \in \mathfrak{m}_0$, and hence $r x \in \mathfrak{m}_0$. Since $1 + r x \in \mathfrak{m}_0$ and $r x \in \mathfrak{m}_0$, we have $1 = (1 + r x) - r x \in \mathfrak{m}_0$, which implies $\mathfrak{m}_0 = R$, contradicting that $\mathfrak{m}_0$ is proper. Thus $1 + r x$ must be a unit.
    <2>2. ($\impliedby$): Assume $1 + r x \in R^\times$ for all $r \in R$.
        *Proof:* Suppose for contradiction that $x \notin J(R)$. Then there exists a maximal ideal $\mathfrak{m}$ such that $x \notin \mathfrak{m}$. Since $\mathfrak{m}$ is maximal and $x \notin \mathfrak{m}$, the ideal $\mathfrak{m} + \langle x \rangle = R$. Thus $1 \in \mathfrak{m} + \langle x \rangle$, so there exist $m \in \mathfrak{m}$ and $s \in R$ such that $1 = m - s x$. Rearranging gives $m = 1 + s x$. By hypothesis, choosing $r = s \in R$, $1 + s x$ is a unit, so $m \in \mathfrak{m}$ is a unit. This implies $\mathfrak{m} = R$, contradicting that $\mathfrak{m}$ is a proper ideal. Thus $x \in \mathfrak{m}$ for all maximal ideals, so $x \in J(R)$.

<1>3. Part (c): $J(R) = \operatorname{Nil}(R)$ when $R$ is finite.
    *Proof:*
    <2>1. Finite integral domains are fields: Let $D$ be a finite integral domain. For any non-zero element $a \in D \setminus \{0\}$, the multiplication map $\mu_a: D \to D, y \mapsto a y$ is injective (since $a y_1 = a y_2 \implies a (y_1 - y_2) = 0 \implies y_1 = y_2$). Since $D$ is finite, every injective map on $D$ is surjective. Thus $1 \in \operatorname{im}(\mu_a)$, so there exists $b \in D$ such that $a b = 1$. Thus $D$ is a field.
    <2>2. Every prime ideal of a finite commutative ring is maximal: Let $\mathfrak{p} \subset R$ be a prime ideal. The quotient ring $R/\mathfrak{p}$ is a finite integral domain. By <2>1, $R/\mathfrak{p}$ is a field, which implies $\mathfrak{p}$ is a maximal ideal.
    <2>3. Equality of prime and maximal spectra: Thus $\operatorname{Spec}(R) = \operatorname{MaxSpec}(R)$ for any finite commutative ring $R$.
    <2>4. Nilradical and Jacobson radical: By Krull's Theorem, the nilradical $\operatorname{Nil}(R) = \bigcap_{\mathfrak{p} \in \operatorname{Spec}(R)} \mathfrak{p}$.
    <2>5. Since $\operatorname{Spec}(R) = \operatorname{MaxSpec}(R)$, we have
    $$J(R) = \bigcap_{\mathfrak{m} \in \operatorname{MaxSpec}(R)} \mathfrak{m} = \bigcap_{\mathfrak{p} \in \operatorname{Spec}(R)} \mathfrak{p} = \operatorname{Nil}(R).$$

<1>4. Conclusion:
    *Proof:*
    All proper ideals lie in maximal ideals, $x \in J(R) \iff 1 + rx \in R^\times$ for all $r$, and $J(R) = \operatorname{Nil}(R)$ when $R$ is finite.
:::
