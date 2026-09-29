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

::: {.problem}
Let $\FF$ be a finite field.

a. Give (with proof) the decomposition of the additive group $(\FF, +)$ into a direct sum of cyclic groups.

b. The *exponent* of a finite group is the least common multiple of the orders of its elements.
   Prove that a finite abelian group has an element of order equal to its exponent.

c. Prove that the multiplicative group $(\unitsof{\FF}, \cdot)$ is cyclic.
:::

::: {.solution}

::: pf

::: {.pf-step #part-a-additive-structure}
Part (a): Additive structure of a finite field:

::: pf-proof

::: pf-step
Let $\operatorname{char}(\mathbb{F}) = p$.
Since $\mathbb{F}$ is a field, $p$ is a prime number, and the prime subfield of $\mathbb{F}$ is $\mathbb{F}_p \cong \mathbb{Z}/p\mathbb{Z}$.

::: pf-proof
characteristic of an integral domain is prime.
:::

:::

::: pf-step
The field $\mathbb{F}$ is a finite-dimensional vector space over $\mathbb{F}_p$.
Let $n = [\mathbb{F} : \mathbb{F}_p] = \dim_{\mathbb{F}_p}(\mathbb{F})$.

::: pf-proof
finite field extension.
:::

:::

::: pf-step
Choosing an $\mathbb{F}_p$-basis $\{v_1, \dots, v_n\}$ for $\mathbb{F}$ gives an $\mathbb{F}_p$-linear isomorphism:
\[
(\mathbb{F}, +) \cong \mathbb{F}_p^n \cong \bigoplus_{i=1}^n \mathbb{Z}_p.
\]
Thus $(\mathbb{F}, +)$ is isomorphic to the direct sum of $n$ copies of the cyclic group $\mathbb{Z}_p$.

::: pf-proof
vector space isomorphism over $\mathbb{F}_p$.
:::

:::

:::

:::

::: {.pf-step #part-b-element-of-exponent-order}
Part (b): Element of order equal to the exponent:

::: pf-proof

::: pf-step
By the Structure Theorem for Finite Abelian Groups, $G \cong \mathbb{Z}_{d_1} \oplus \mathbb{Z}_{d_2} \oplus \cdots \oplus \mathbb{Z}_{d_k}$, where the invariant factors satisfy $d_1 \mid d_2 \mid \cdots \mid d_k$.

::: pf-proof
Fundamental Theorem of Finite Abelian Groups.
:::

:::

::: pf-step
For every element $g = (g_1, \dots, g_k) \in G$, $|g_i| \mid d_i \mid d_k$, so $g^{d_k} = e$.
Thus the exponent $e = \exp(G) = \operatorname{lcm}_{g \in G} |g| = d_k$.

::: pf-proof
definition of group exponent.
:::

:::

::: pf-step
The element $x = (0, \dots, 0, 1) \in G$ has order exactly $d_k = e$.
Thus $G$ contains an element of order equal to $\exp(G)$.

::: pf-proof
order of generator in cyclic direct summand.
:::

:::

:::

:::

::: {.pf-step #part-c-cyclicity}
Part (c): Cyclicity of the multiplicative group $(\mathbb{F}^\times, \cdot)$:

::: pf-proof

::: pf-step
The multiplicative group $\mathbb{F}^\times$ is a finite abelian group of order $N = |\mathbb{F}| - 1 = p^n - 1$.

::: pf-proof
non-zero elements of a finite field form an abelian group under multiplication.
:::

:::

::: {.pf-step #e-leq-n}
Let $e = \exp(\mathbb{F}^\times)$. By Part (b), there exists an element $g \in \mathbb{F}^\times$ of order $|g| = e$.
By Lagrange’s Theorem, $e \mid N$, so $e \le N$.

::: pf-proof
Part (b) and Lagrange's Theorem.
:::

:::

::: pf-step
By definition of the exponent, $x^e = 1$ for all $x \in \mathbb{F}^\times$.
Thus every element of $\mathbb{F}^\times$ is a root of the polynomial $P(T) = T^e - 1 \in \mathbb{F}[T]$.

::: pf-proof
$x^e = 1$ for all $x \in \mathbb{F}^\times$.
:::

:::

::: {.pf-step #n-leq-e}
Since $\mathbb{F}$ is a field, the non-zero polynomial $P(T)$ of degree $e$ has at most $e$ roots in $\mathbb{F}$.
Therefore:
\[
N = |\mathbb{F}^\times| \le e.
\]

::: pf-proof
a degree $e$ polynomial over a field has at most $e$ roots.
:::

:::

::: pf-step
Combining $e \le N$ (step [](#e-leq-n){.pf-ref}) and $N \le e$ (step [](#n-leq-e){.pf-ref}) gives $e = N = |\mathbb{F}^\times|$.
Since $g \in \mathbb{F}^\times$ has order $e = |\mathbb{F}^\times|$, $\mathbb{F}^\times = \langle g \rangle$ is cyclic.

::: pf-proof
a finite group containing an element of order equal to the group order is cyclic.
:::

:::

:::

:::

::: pf-step
Conclusion:
$(\mathbb{F}, +) \cong (\mathbb{Z}_p)^n$, any finite abelian group has an element of order $\exp(G)$, and $(\mathbb{F}^\times, \cdot)$ is cyclic. Q.E.D.

::: pf-proof
Step [](#part-a-additive-structure){.pf-ref} through step [](#part-c-cyclicity){.pf-ref}.
:::

:::

:::

:::
