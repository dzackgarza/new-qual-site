---
schema: qual/card@1
id: P-56PBT
kind: problem
title: The additive group of a finite field and cyclicity of its multiplicative group
classification:
  areas:
  - algebra
  topics:
  - Finite Fields
  - Structure Theorem
  - Cyclic Groups
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: problem
Let $\FF$ be a finite field.

a. Give (with proof) the decomposition of the additive group $(\FF, +)$ into a direct sum of cyclic groups.

b. The *exponent* of a finite group is the least common multiple of the orders of its elements.
Prove that a finite abelian group has an element of order equal to its exponent.

c. Prove that the multiplicative group $(\FF\units, \cdot)$ is cyclic.
:::

::: {.solution}
<1>1. Part (a): Additive structure of a finite field:
<2>1. Let $\operatorname{char}(\mathbb{F}) = p$. Since $\mathbb{F}$ is a field, $p$ is a prime number, and the prime subfield of $\mathbb{F}$ is $\mathbb{F}_p \cong \mathbb{Z}/p\mathbb{Z}$.
Proof: characteristic of an integral domain is prime.
<2>2. The field $\mathbb{F}$ is a finite-dimensional vector space over $\mathbb{F}_p$.
Let $n = [\mathbb{F} : \mathbb{F}_p] = \dim_{\mathbb{F}_p}(\mathbb{F})$.
Proof: finite field extension.
<2>3. Choosing an $\mathbb{F}_p$-basis $\{v_1, \dots, v_n\}$ for $\mathbb{F}$ gives an $\mathbb{F}_p$-linear isomorphism:
\[
(\mathbb{F}, +) \cong \mathbb{F}_p^n \cong \bigoplus_{i=1}^n \mathbb{Z}_p.
\]
Thus $(\mathbb{F}, +)$ is isomorphic to the direct sum of $n$ copies of the cyclic group $\mathbb{Z}_p$.
Proof: vector space isomorphism over $\mathbb{F}_p$.

<1>2. Part (b): Element of order equal to the exponent:
<2>1. By the Structure Theorem for Finite Abelian Groups, $G \cong \mathbb{Z}_{d_1} \oplus \mathbb{Z}_{d_2} \oplus \cdots \oplus \mathbb{Z}_{d_k}$, where the invariant factors satisfy $d_1 \mid d_2 \mid \cdots \mid d_k$.
Proof: Fundamental Theorem of Finite Abelian Groups.
<2>2. For every element $g = (g_1, \dots, g_k) \in G$, $|g_i| \mid d_i \mid d_k$, so $g^{d_k} = e$.
Thus the exponent $e = \exp(G) = \operatorname{lcm}_{g \in G} |g| = d_k$.
Proof: definition of group exponent.
<2>3. The element $x = (0, \dots, 0, 1) \in G$ has order exactly $d_k = e$.
Thus $G$ contains an element of order equal to $\exp(G)$.
Proof: order of generator in cyclic direct summand.

<1>3. Part (c): Cyclicity of the multiplicative group $(\mathbb{F}^\times, \cdot)$:
<2>1. The multiplicative group $\mathbb{F}^\times$ is a finite abelian group of order $N = |\mathbb{F}| - 1 = p^n - 1$.
Proof: non-zero elements of a finite field form an abelian group under multiplication.
<2>2. Let $e = \exp(\mathbb{F}^\times)$. By Part (b), there exists an element $g \in \mathbb{F}^\times$ of order $|g| = e$.
By Lagrange’s Theorem, $e \mid N$, so $e \le N$.
Proof: Part (b) and Lagrange's Theorem.
<2>3. By definition of the exponent, $x^e = 1$ for all $x \in \mathbb{F}^\times$.
Thus every element of $\mathbb{F}^\times$ is a root of the polynomial $P(T) = T^e - 1 \in \mathbb{F}[T]$.
Proof: $x^e = 1$ for all $x \in \mathbb{F}^\times$.
<2>4. Since $\mathbb{F}$ is a field, the non-zero polynomial $P(T)$ of degree $e$ has at most $e$ roots in $\mathbb{F}$.
Therefore:
\[
N = |\mathbb{F}^\times| \le e.
\]
Proof: a degree $e$ polynomial over a field has at most $e$ roots.
<2>5. Combining $e \le N$ (<2>2) and $N \le e$ (<2>4) gives $e = N = |\mathbb{F}^\times|$.
Since $g \in \mathbb{F}^\times$ has order $e = |\mathbb{F}^\times|$, $\mathbb{F}^\times = \langle g \rangle$ is cyclic.
Proof: a finite group containing an element of order equal to the group order is cyclic.

<1>4. Conclusion:
$(\mathbb{F}, +) \cong (\mathbb{Z}_p)^n$, any finite abelian group has an element of order $\exp(G)$, and $(\mathbb{F}^\times, \cdot)$ is cyclic. Q.E.D.
Proof: <1>1 through <1>3.
:::
