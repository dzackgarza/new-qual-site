---
schema: qual/card@1
id: P-USHDW
kind: problem
title: The nilradical is contained in every prime, primes avoiding powers of a non-nilpotent,
  and rings with a unique prime consist of nilpotents and units
classification:
  areas:
  - algebra
  topics:
  - Nilpotence
  - Prime Ideals
  - Zorn's Lemma
relations: []
review: draft
---

::: problem
Let $R$ be a commutative ring with identity $1 \ne 0$. Assume Zorn's Lemma.

(a) Show that the nilradical
$$
N = \{r \in R \mid r^n = 0 \text{ for some } n > 0\}
$$
is an ideal that is contained in every prime ideal of $R$.

(b) Let $r \in R \setminus N$. Let $\mathcal{S}$ be the collection of all ideals of $R$ that do not contain any positive power of $r$. Use Zorn's Lemma to prove that there is a prime ideal in $\mathcal{S}$.

(c) Suppose that $R$ has exactly one prime ideal $P$. Prove that every element $r \in R$ is either nilpotent or a unit.
:::

::: solution
**Goal:** Prove that the nilradical is an ideal contained in all prime ideals in (a), use Zorn's Lemma to construct a prime ideal avoiding powers of a non-nilpotent element in (b), and prove that every element in a ring with a unique prime ideal is nilpotent or a unit in (c).

<1>1. Part (a): $N$ is an ideal contained in every prime ideal.
    *Proof:*
    <2>1. $N$ is an ideal:
        - $0 \in N$ since $0^1 = 0$.
        - If $x, y \in N$, there exist $m, n \ge 1$ such that $x^m = 0$ and $y^n = 0$. By the Binomial Theorem (since $R$ is commutative):
        $$(x - y)^{m+n-1} = \sum_{j=0}^{m+n-1} \binom{m+n-1}{j} x^j (-y)^{m+n-1-j}.$$
        In each term, either $j \ge m$ (so $x^j = 0$) or $(m+n-1-j) \ge n$ (so $y^{m+n-1-j} = 0$). Thus $(x - y)^{m+n-1} = 0$, so $x - y \in N$.
        - For any $s \in R$ and $x \in N$ with $x^m = 0$: $(s x)^m = s^m x^m = s^m \cdot 0 = 0$, so $s x \in N$.
        - Thus $N$ is an ideal of $R$.
    <2>2. $N \subseteq \mathfrak{p}$ for every prime ideal $\mathfrak{p}$:
        - Let $\mathfrak{p} \subset R$ be a prime ideal and let $x \in N$.
        - There exists $n \ge 1$ such that $x^n = 0 \in \mathfrak{p}$.
        - By definition of a prime ideal, $a b \in \mathfrak{p} \implies a \in \mathfrak{p}$ or $b \in \mathfrak{p}$.
        - By induction on $n$, $x^n \in \mathfrak{p} \implies x \in \mathfrak{p}$.
        - Thus $N \subseteq \mathfrak{p}$.

<1>2. Part (b): Existence of a prime ideal avoiding powers of $r$.
    *Proof:*
    <2>1. Define the multiplicative set $\Sigma = \{r^k \mid k \in \mathbb{N}_{\ge 1}\}$.
    <2>2. Define the family of ideals:
    $$\mathcal{S} = \{I \trianglelefteq R \mid I \cap \Sigma = \emptyset\}.$$
    <2>3. $\mathcal{S}$ is non-empty: Since $r \notin N$, $r^k \ne 0$ for all $k \ge 1$, which means $\{0\} \cap \Sigma = \emptyset$. Thus the zero ideal $\{0\} \in \mathcal{S}$.
    <2>4. Partially order $\mathcal{S}$ by inclusion $\subseteq$.
    <2>5. Upper bounds for chains: Let $\mathcal{C} \subseteq \mathcal{S}$ be a totally ordered chain of ideals. The union $I_0 = \bigcup_{I \in \mathcal{C}} I$ is an ideal of $R$. If $I_0 \cap \Sigma \ne \emptyset$, then $r^k \in I_0$ for some $k$, so $r^k \in I'$ for some $I' \in \mathcal{C}$, contradicting $I' \in \mathcal{S}$. Thus $I_0 \in \mathcal{S}$, and $I_0$ is an upper bound for $\mathcal{C}$.
    <2>6. By Zorn's Lemma, $\mathcal{S}$ has a maximal element, denoted $P \in \mathcal{S}$.
    <2>7. $P$ is a proper ideal: Since $1 = r^0$ or $r^1 \in \Sigma$, $1 \notin P$ because $P \cap \Sigma = \emptyset$.
    <2>8. $P$ is prime:
        - Let $a, b \in R$ such that $a b \in P$. Suppose for contradiction that $a \notin P$ and $b \notin P$.
        - The ideals $P + \langle a \rangle$ and $P + \langle b \rangle$ strictly contain $P$.
        - By the maximality of $P$ in $\mathcal{S}$, neither ideal belongs to $\mathcal{S}$.
        - Thus there exist powers $r^m \in P + \langle a \rangle$ and $r^n \in P + \langle b \rangle$ for some $m, n \ge 1$.
        - Write $r^m = p_1 + u a$ and $r^n = p_2 + v b$ for some $p_1, p_2 \in P$ and $u, v \in R$.
        - Multiply the two expressions:
        $$r^{m+n} = (p_1 + u a)(p_2 + v b) = p_1 p_2 + p_1 v b + p_2 u a + u v (a b).$$
        - Since $p_1, p_2, a b \in P$, all terms on the right-hand side belong to $P$, so $r^{m+n} \in P$.
        - This contradicts $P \cap \Sigma = \emptyset$.
        - Thus $a \in P$ or $b \in P$, proving that $P$ is a prime ideal in $\mathcal{S}$.

<1>3. Part (c): Rings with a unique prime ideal consist of nilpotents and units.
    *Proof:*
    <2>1. Let $P$ be the unique prime ideal of $R$.
    <2>2. Since every maximal ideal of $R$ is prime, and maximal ideals exist in every non-trivial commutative ring by Krull's Theorem, $P$ must also be the unique maximal ideal of $R$.
    <2>3. Let $r \in R$. Suppose $r$ is not a unit.
    <2>4. The principal ideal $\langle r \rangle$ is proper.
    <2>5. By Krull's Theorem, $\langle r \rangle$ is contained in a maximal ideal, so $\langle r \rangle \subseteq P$, which means $r \in P$.
    <2>6. Suppose for contradiction that $r \notin N$.
    <2>7. By Part (b), there exists a prime ideal $Q \subset R$ avoiding all positive powers of $r$.
    <2>8. In particular, $r \notin Q$.
    <2>9. Since $P$ is the only prime ideal of $R$, we must have $Q = P$.
    <2>10. But then $r \notin P$, contradicting <2>5 where $r \in P$.
    <2>11. Thus $r \in N$, so $r$ is nilpotent.
    <2>12. Therefore every element of $R$ is either a unit or nilpotent.

<1>4. Conclusion:
    *Proof:*
    $N$ is an ideal contained in every prime, Zorn's Lemma yields a prime ideal avoiding powers of non-nilpotents, and every element in a ring with a unique prime is a unit or nilpotent.
:::
