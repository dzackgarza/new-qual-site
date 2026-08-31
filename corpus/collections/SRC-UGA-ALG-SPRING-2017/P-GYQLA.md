---
schema: qual/card@1
id: P-GYQLA
kind: problem
title: Left translation is an odd permutation iff its order is even and $|G|$ divided
  by the order is odd
classification:
  areas:
  - algebra
  topics:
  - Permutations
  - Group Actions
  - Cosets and Lagrange
relations: []
review: draft
---

::: problem
Let $G$ be a finite group and let $\pi: G \to \operatorname{Sym}(G)$ be the Cayley (left regular) representation, where $\pi(x)(g) = x g$ for all $g \in G$.

Prove that $\pi(x)$ is an odd permutation if and only if the order $\operatorname{ord}(\pi(x))$ is even and $|G| / \operatorname{ord}(\pi(x))$ is odd.
:::

::: solution
**Goal:** Prove that the sign of the left regular permutation $\pi(x)$ is $(-1)^{m(k-1)}$, where $k = \operatorname{ord}(\pi(x))$ and $m = |G|/k$, and characterize when it is odd.

<1>1. Disjoint cycle decomposition of $\pi(x)$:
    *Proof:*
    <2>1. Let $x \in G$, and let $k = \operatorname{ord}(x)$ be the order of $x$ in $G$.
    <2>2. Since the left regular action is faithful, $\operatorname{ord}(\pi(x)) = \operatorname{ord}(x) = k$.
    <2>3. The permutation $\pi(x)$ acts on the finite set $G$ by left multiplication $g \mapsto x g$.
    <2>4. The orbit of an element $g \in G$ under the action of $\langle x \rangle$ is the right coset:
    $$\mathcal{O}_g = \{x^j g \mid 0 \le j < k\} = \langle x \rangle g.$$
    <2>5. Since $|\langle x \rangle g| = |\langle x \rangle| = k$ for every $g \in G$, every orbit of $\pi(x)$ has size exactly $k$.
    <2>6. On each orbit $\mathcal{O}_g$, the cyclic action of $\pi(x)$ forms a cycle of length $k$:
    $$(g, \, x g, \, x^2 g, \, \dots, \, x^{k-1} g).$$
    <2>7. The number of disjoint orbits is the number of right cosets of $\langle x \rangle$ in $G$:
    $$m = [G : \langle x \rangle] = \frac{|G|}{k} = \frac{|G|}{\operatorname{ord}(\pi(x))}.$$
    <2>8. Thus $\pi(x)$ decomposes into the product of $m$ disjoint cycles of length $k$.

<1>2. Parity and sign of $\pi(x)$:
    *Proof:*
    <2>1. A cycle of length $k$ can be factored into a product of $k - 1$ transpositions:
    $$(c_1, c_2, \dots, c_k) = (c_1, c_k)(c_1, c_{k-1}) \cdots (c_1, c_2).$$
    <2>2. Thus the sign of a $k$-cycle is $\operatorname{sgn}(\text{cycle of length } k) = (-1)^{k - 1}$.
    <2>3. Because the sign homomorphism $\operatorname{sgn}: \operatorname{Sym}(G) \to \{\pm 1\}$ is multiplicative on products of disjoint cycles:
    $$\operatorname{sgn}(\pi(x)) = \left( (-1)^{k - 1} \right)^m = (-1)^{m(k - 1)}.$$

<1>3. Characterization of odd permutations:
    *Proof:*
    <2>1. By definition, $\pi(x)$ is an odd permutation if and only if $\operatorname{sgn}(\pi(x)) = -1$.
    <2>2. From <1>2, $(-1)^{m(k - 1)} = -1$ if and only if the exponent $m(k - 1)$ is an odd integer.
    <2>3. A product of two integers is odd if and only if both factors are odd:
    $$m(k - 1) \text{ is odd} \iff m \text{ is odd and } (k - 1) \text{ is odd}.$$
    <2>4. The integer $k - 1$ is odd if and only if $k$ is even.
    <2>5. Thus $\operatorname{sgn}(\pi(x)) = -1$ if and only if $k$ is even and $m$ is odd.
    <2>6. Substituting $k = \operatorname{ord}(\pi(x))$ and $m = |G|/\operatorname{ord}(\pi(x))$ completes the equivalence.

<1>4. Conclusion:
    *Proof:*
    $\pi(x)$ is an odd permutation if and only if $\operatorname{ord}(\pi(x))$ is even and $|G|/\operatorname{ord}(\pi(x))$ is odd.
:::
