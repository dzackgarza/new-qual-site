---
schema: qual/card@1
id: E-AMD-UEHZOJ3K
kind: exercise
title: Nilradical is the intersection of all prime ideals
classification:
  areas:
  - algebra
  topics:
  - Nilpotence
  - Prime Ideals
  - Ideals
relations: []
review: draft
---

::: exercise
Show that the nilradical of a commutative ring $R$ is equal to the intersection of all prime ideals of $R$.
:::

::: solution
**Goal:** Prove Krull's Theorem: for any commutative ring $R$, the nilradical $\operatorname{Nil}(R)$ is the intersection of all prime ideals of $R$,
$$
\operatorname{Nil}(R) = \bigcap_{\mathfrak{p} \in \operatorname{Spec}(R)} \mathfrak{p}.
$$

<1>1. Forward containment: $\operatorname{Nil}(R) \subseteq \bigcap_{\mathfrak{p} \in \operatorname{Spec}(R)} \mathfrak{p}$.
    *Proof:*
    <2>1. Let $x \in \operatorname{Nil}(R)$. By definition, there exists an integer $n \ge 1$ such that $x^n = 0$.
    <2>2. Let $\mathfrak{p} \in \operatorname{Spec}(R)$ be any prime ideal of $R$.
    <2>3. Since $\mathfrak{p}$ is an ideal, $0 \in \mathfrak{p}$, so $x^n \in \mathfrak{p}$.
    <2>4. We prove by induction on $k \ge 1$ that $x^k \in \mathfrak{p} \implies x \in \mathfrak{p}$.
    <2>5. Base case $k = 1$: $x^1 = x \in \mathfrak{p}$ is exactly the hypothesis, so the claim holds.
    <2>6. Induction step: if $x^k = x \cdot x^{k-1} \in \mathfrak{p}$, then since $\mathfrak{p}$ is prime, either $x \in \mathfrak{p}$ or $x^{k-1} \in \mathfrak{p}$. By the induction hypothesis, $x \in \mathfrak{p}$ in either case.
    <2>7. Thus $x \in \mathfrak{p}$ for every prime ideal $\mathfrak{p}$ of $R$.
    <2>8. Therefore $x \in \bigcap_{\mathfrak{p} \in \operatorname{Spec}(R)} \mathfrak{p}$.

<1>2. Reverse containment: $\bigcap_{\mathfrak{p} \in \operatorname{Spec}(R)} \mathfrak{p} \subseteq \operatorname{Nil}(R)$.
    *Proof:*
    <2>1. We prove the contrapositive: if $f \in R \setminus \operatorname{Nil}(R)$, then there exists a prime ideal $\mathfrak{p} \in \operatorname{Spec}(R)$ such that $f \notin \mathfrak{p}$.
    <2>2. Let $f \in R$ be non-nilpotent. Then the set of powers $S = \{f^n : n \ge 0\}$ (with $f^0 = 1$) is a multiplicative subset of $R$ with $0 \notin S$.
    <2>3. Define the family of ideals:
    $$\mathcal{F} = \{I \subseteq R : I \text{ is an ideal of } R \text{ and } I \cap S = \emptyset\}.$$
    <2>4. Since $0 \notin S$, the zero ideal $\{0\} \in \mathcal{F}$, so $\mathcal{F} \neq \emptyset$.
    <2>5. Order $\mathcal{F}$ by inclusion $\subseteq$. If $\mathcal{C} \subseteq \mathcal{F}$ is a non-empty totally ordered chain of ideals, the union $J = \bigcup_{I \in \mathcal{C}} I$ is an ideal of $R$.
    <2>6. Furthermore, $J \cap S = \bigcup_{I \in \mathcal{C}} (I \cap S) = \emptyset$, so $J \in \mathcal{F}$ is an upper bound for the chain $\mathcal{C}$.
    <2>7. By Zorn's Lemma, $\mathcal{F}$ contains a maximal element $\mathfrak{p}$.

<1>3. Primality of the maximal element $\mathfrak{p}$:
    *Proof:*
    <2>1. Since $\mathfrak{p} \in \mathcal{F}$, $\mathfrak{p} \cap S = \emptyset$. In particular, $1 = f^0 \notin \mathfrak{p}$, so $\mathfrak{p} \neq R$.
    <2>2. Suppose for contradiction that $\mathfrak{p}$ is not a prime ideal: there exist $a, b \in R$ such that $a b \in \mathfrak{p}$ with $a \notin \mathfrak{p}$ and $b \notin \mathfrak{p}$.
    <2>3. The ideals $\mathfrak{p} + \langle a \rangle$ and $\mathfrak{p} + \langle b \rangle$ strictly contain $\mathfrak{p}$.
    <2>4. By the maximality of $\mathfrak{p}$ in $\mathcal{F}$, neither strictly larger ideal belongs to $\mathcal{F}$.
    <2>5. Therefore both ideals must intersect the multiplicative set $S$: there exist integers $m, n \ge 0$ such that
    $$f^m \in \mathfrak{p} + \langle a \rangle \quad \text{and} \quad f^n \in \mathfrak{p} + \langle b \rangle.$$
    <2>6. Multiplying these elements gives
    $$f^{m+n} = f^m f^n \in (\mathfrak{p} + \langle a \rangle)(\mathfrak{p} + \langle b \rangle) \subseteq \mathfrak{p} + \langle a b \rangle.$$
    <2>7. Since $a b \in \mathfrak{p}$, we have $\mathfrak{p} + \langle a b \rangle = \mathfrak{p}$, which implies $f^{m+n} \in \mathfrak{p}$.
    <2>8. Thus $f^{m+n} \in \mathfrak{p} \cap S$, which contradicts $\mathfrak{p} \cap S = \emptyset$.
    <2>9. Hence $\mathfrak{p}$ is a prime ideal of $R$.

<1>4. Conclusion:
    *Proof:*
    Since $\mathfrak{p}$ is a prime ideal and $f = f^1 \in S$, we have $f \notin \mathfrak{p}$. Thus $f \notin \bigcap_{\mathfrak{q} \in \operatorname{Spec}(R)} \mathfrak{q}$. By contraposition, $\bigcap_{\mathfrak{p} \in \operatorname{Spec}(R)} \mathfrak{p} \subseteq \operatorname{Nil}(R)$, completing the equality $\operatorname{Nil}(R) = \bigcap_{\mathfrak{p} \in \operatorname{Spec}(R)} \mathfrak{p}$.
:::
