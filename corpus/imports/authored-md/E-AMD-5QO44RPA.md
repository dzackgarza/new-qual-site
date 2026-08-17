---
schema: qual/card@1
id: E-AMD-5QO44RPA
kind: exercise
title: Show that no group of order $p^2 q^2$ is simple for $p<q$ primes.
classification:
  areas:
  - algebra
  topics:
  - sylow-theory
  - simple-groups
  - classification
relations: []
review: draft
solved: true
---

::: {.exercise}
Show that no group of order $p^2 q^2$ is simple for $p<q$ primes.
:::

::: {.solution}
> **AI-Generated Solution** (Gemini 3.7 Flash)

**Goal:** Let $p$ and $q$ be prime numbers with $p < q$, and let $G$ be a group of order $|G| = p^2 q^2$.
Prove that $G$ is not simple.

<1>1. Let $n_q$ denote the number of Sylow $q$-subgroups of $G$, and let $n_p$ denote the number of Sylow $p$-subgroups of $G$.
Proof: The existence and count of Sylow subgroups are guaranteed by Sylow's Theorems for the finite group $G$ with $|G| = p^2 q^2$.

<1>2. By Sylow's Third Theorem, $n_q$ divides $p^2$ and $n_q \equiv 1 \pmod q$.
Proof: The order of $G$ is $p^2 q^2$.
Sylow's Third Theorem states that the number of Sylow $q$-subgroups divides the index $[G : Q] = p^2$ (for any $Q \in \operatorname{Syl}_q(G)$) and satisfies $n_q \equiv 1 \pmod q$.

<1>3. The divisors of $p^2$ are $1$, $p$, and $p^2$.
Thus, $n_q \in \{1, p, p^2\}$.
Proof: Since $p$ is prime, the only positive integer divisors of $p^2$ are $1, p, p^2$.

<1>4. $n_q \neq p$.
<2>1. If $n_q = p$, then $p \equiv 1 \pmod q$.
Proof: By <1>2, $n_q \equiv 1 \pmod q$.
<2>2. $p \equiv 1 \pmod q$ implies $p \ge q + 1 > q$.
Proof: Since $p$ is a positive integer, $p \equiv 1 \pmod q$ means $p = 1 + k q$ for some integer $k \ge 1$, which gives $p > q$.
<2>3. Contradiction: $p < q$ by hypothesis.
Proof: The problem assumes $p < q$, contradicting $p > q$ from <2>2. <2>4. Q.E.D. Proof: By <2>1, <2>2, and <2>3, the case $n_q = p$ is impossible.

<1>5. If $n_q = 1$, then $G$ contains a unique Sylow $q$-subgroup $Q$, which is normal in $G$, hence $G$ is not simple.
<2>1. A Sylow subgroup is normal if and only if it is the unique Sylow subgroup for that prime.
Proof: All Sylow $q$-subgroups are conjugate by Sylow's Second Theorem.
Conjugation preserves $Q$ if and only if $g Q g^{-1} = Q$ for all $g \in G$, meaning $n_q = 1$.
<2>2. The order of $Q$ is $|Q| = q^2$.
Proof: By definition of Sylow $q$-subgroups of a group of order $p^2 q^2$.
<2>3. Since $p < q$ and $p, q \ge 2$, $1 < q^2 < p^2 q^2$, so $Q$ is a proper, non-trivial normal subgroup.
Proof: $q \ge 3$ (since $p \ge 2$ and $p < q$), so $|Q| = q^2 \ge 9 > 1$, and $|Q| < p^2 q^2$ as $p \ge 2$.
<2>4. Q.E.D. Proof: The existence of a proper non-trivial normal subgroup $Q \trianglelefteq G$ proves $G$ is not simple.

<1>6. If $n_q = p^2$, then $n_p = 1$, and hence $G$ contains a unique Sylow $p$-subgroup $P \trianglelefteq G$, so $G$ is not simple.
<2>1. Assume $n_q = p^2$.
Then $p^2 \equiv 1 \pmod q$, so $q \mid (p^2 - 1) = (p-1)(p+1)$.
Proof: By <1>2, $n_q \equiv 1 \pmod q$.
Thus $q \mid (p^2 - 1)$.
<2>2. Since $q$ is prime and $p < q$, $q \nmid (p-1)$ because $0 < p-1 < q$.
Proof: $p < q$ implies $p - 1 < q$, and $p \ge 2$ implies $p - 1 \ge 1$.
A prime $q$ cannot divide a positive integer strictly smaller than $q$.
<2>3. Therefore, $q \mid (p+1)$, which forces $q = p+1$.
Proof: Since $q \mid (p-1)(p+1)$ and $\gcd(q, p-1) = 1$, Euclid's Lemma implies $q \mid (p+1)$.
Since $p < q$, we have $p+1 \le q$.
Thus $q \mid (p+1)$ and $p+1 \le q$ imply $q = p+1$.
<2>4. The only primes satisfying $q = p+1$ are $p = 2$ and $q = 3$.
Proof: One of any two consecutive integers is even.
The only even prime is $2$, so $p = 2$, which gives $q = 3$.
<2>5. For $p = 2, q = 3$, $|G| = 2^2 \cdot 3^2 = 36$.
Proof: Direct evaluation $|G| = p^2 q^2 = 4 \cdot 9 = 36$.
<2>6. For $|G| = 36$, if $n_3 = 2^2 = 4$, then $G$ has a non-trivial proper normal subgroup.
<3>1. Let $G$ act on the set $X = \operatorname{Syl}_3(G)$ of 4 Sylow 3-subgroups by conjugation.
Proof: Group action by conjugation is well-defined, and $|X| = n_3 = 4$.
<3>2. This action induces a group homomorphism $\phi: G \to S_4$.
Proof: The permutation representation associated to a group action on a 4-element set gives a homomorphism into $S_4$.
<3>3. $\ker(\phi)$ is a normal subgroup of $G$.
Proof: The kernel of any group homomorphism is a normal subgroup of the domain.
<3>4. $\ker(\phi) \neq \{e\}$.
Proof: If $\ker(\phi) = \{e\}$, then $\phi$ is injective, which implies $|G| \le |S_4|$.
But $|G| = 36$ and $|S_4| = 4! = 24$, so $|G| > |S_4|$, a contradiction.
<3>5. $\ker(\phi) \neq G$.
Proof: The action of $G$ on $\operatorname{Syl}_3(G)$ is transitive by Sylow's Second Theorem.
Since $|X| = 4 > 1$, the action is non-trivial, so $\ker(\phi) \neq G$.
<3>6. Q.E.D. Proof: $\ker(\phi)$ is a proper non-trivial normal subgroup of $G$, so $G$ is not simple.
<2>7. Q.E.D. Proof: In all cases with $n_q = p^2$, $G$ contains a proper non-trivial normal subgroup.

<1>7. Conclusion: In all possible cases for $n_q \in \{1, p, p^2\}$, $G$ is not simple.
Proof: By <1>3, $n_q \in \{1, p, p^2\}$.
<1>4 rules out $n_q = p$.
<1>5 shows $G$ is not simple when $n_q = 1$.
<1>6 shows $G$ is not simple when $n_q = p^2$.
Thus $G$ is never simple.
:::
