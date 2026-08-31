---
schema: qual/card@1
id: P-QWEAV
kind: problem
title: Cayley's theorem, the sign of left translation, and nonsimplicity of groups
  of order $N\equiv 2\pmod{4}$
classification:
  areas:
  - algebra
  topics:
  - Permutations
  - Group Actions
  - Simple Groups
relations: []
review: draft
---

::: problem
Let $N$ be a positive integer, and let $G$ be a finite group of order $N$.

(a) Let $\operatorname{Sym}(G)$ denote the symmetric group of all bijections from $G$ to $G$ under composition. Prove that the Cayley map
$$
C: G \to \operatorname{Sym}(G), \quad C(g)(x) = g x,
$$
is an injective group homomorphism.

(b) Let $\Phi: \operatorname{Sym}(G) \to S_N$ be a group isomorphism. For $a \in G$, define $\varepsilon(a) = \operatorname{sgn}(\Phi(C(a))) \in \{\pm 1\}$ to be the sign of the permutation. If $a \in G$ has order $d$, prove that
$$
\varepsilon(a) = -1 \iff d \text{ is even and } N/d \text{ is odd}.
$$

(c) Suppose $N > 2$ and $N \equiv 2 \pmod 4$. Prove that $G$ is not simple.
:::

::: solution
**Goal:** Prove Cayley's embedding in (a), determine the parity of left translation permutations in (b), and construct an index-2 normal subgroup via the sign homomorphism to prove nonsimplicity in (c).

<1>1. Part (a): Cayley map is an injective group homomorphism.
    *Proof:*
    <2>1. Homomorphism property:
        - For any $g, h \in G$ and all $x \in G$:
        $$C(g h)(x) = (g h) x = g (h x) = C(g)(h x) = C(g)(C(h)(x)) = (C(g) \circ C(h))(x).$$
        - Thus $C(g h) = C(g) \circ C(h)$, so $C$ is a group homomorphism.
    <2>2. Injectivity:
        - Suppose $g \in \ker(C)$.
        - Then $C(g) = \operatorname{id}_G$, so $C(g)(x) = x$ for all $x \in G$.
        - Evaluating at $x = e$ gives $g e = e \implies g = e$.
        - Thus $\ker(C) = \{e\}$, so $C$ is injective.

<1>2. Part (b): $\varepsilon(a) = -1 \iff d$ is even and $N/d$ is odd.
    *Proof:*
    <2>1. Let $a \in G$ have order $d = \operatorname{ord}(a)$.
    <2>2. The cyclic group $\langle a \rangle \le G$ has order $d$.
    <2>3. The action of $\langle a \rangle$ on $G$ by left translation partitions $G$ into $m = [G : \langle a \rangle] = N/d$ orbits, each of which is a right coset $\langle a \rangle x = \{a^j x \mid 0 \le j < d\}$.
    <2>4. Since each orbit has cardinality $d$, the permutation $C(a)$ is a product of $m = N/d$ disjoint cycles of length $d$.
    <2>5. The sign of a single cycle of length $d$ is $(-1)^{d - 1}$.
    <2>6. Since the sign homomorphism $\operatorname{sgn}: S_N \to \{\pm 1\}$ is multiplicative on disjoint cycles and $\Phi$ is an isomorphism:
    $$\varepsilon(a) = \left( (-1)^{d - 1} \right)^{N/d} = (-1)^{\frac{N}{d}(d - 1)}.$$
    <2>7. Thus $\varepsilon(a) = -1$ if and only if the exponent $\frac{N}{d}(d - 1)$ is an odd integer.
    <2>8. The product $\frac{N}{d}(d - 1)$ is odd if and only if both factors are odd:
    $$\frac{N}{d} \text{ is odd} \quad \text{and} \quad d - 1 \text{ is odd} \iff \frac{N}{d} \text{ is odd} \quad \text{and} \quad d \text{ is even}.$$

<1>3. Part (c): $G$ is not simple when $N > 2$ and $N \equiv 2 \pmod 4$.
    *Proof:*
    <2>1. Since $N \equiv 2 \pmod 4$, $2 \mid N$ and $N/2$ is an odd integer.
    <2>2. By Cauchy's Theorem for finite groups, since $2 \mid |G| = N$, $G$ contains an element $g \in G$ of order $d = 2$.
    <2>3. For this element $g$, the order $d = 2$ is even and $N/d = N/2$ is odd.
    <2>4. By Part (b), $\varepsilon(g) = -1$.
    <2>5. The map $\varepsilon = \operatorname{sgn} \circ \Phi \circ C: G \to \{\pm 1\}$ is a group homomorphism since it is a composition of homomorphisms.
    <2>6. Since $\varepsilon(e) = 1$ and $\varepsilon(g) = -1$, the homomorphism $\varepsilon$ is surjective onto the group $\{\pm 1\} \cong \mathbb{Z}/2\mathbb{Z}$.
    <2>7. By the First Isomorphism Theorem, the kernel $H = \ker(\varepsilon)$ is a normal subgroup of $G$ of index:
    $$[G : H] = |\{\pm 1\}| = 2.$$
    <2>8. The order of $H$ is $|H| = |G|/2 = N/2$.
    <2>9. Since $N > 2$, $1 < |H| = N/2 < N$, so $H$ is a non-trivial, proper normal subgroup of $G$.
    <2>10. Therefore $G$ is not simple.

<1>4. Conclusion:
    *Proof:*
    $C$ is injective, $\varepsilon(a) = (-1)^{\frac{N}{d}(d-1)}$, and the kernel of $\varepsilon$ provides an index 2 normal subgroup when $N \equiv 2 \pmod 4$ and $N > 2$.
:::

