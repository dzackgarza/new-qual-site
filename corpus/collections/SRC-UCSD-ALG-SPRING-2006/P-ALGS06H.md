---
schema: qual/card@1
id: P-ALGS06H
kind: problem
title: "Cyclic multiplicative group and existence of irreducible polynomials over finite fields"
classification:
  areas:
  - algebra
  topics:
  - Field Theory
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
- event: solution-written
  by: claude
  date: 2026-11-20
  note: >-
    The ten leaf steps of parts (a), (b) and (c) asserted their claim with no proof body; each
    now carries one, and the closing QED step also says what the three parts conclude. No claim,
    no numbering and no statement is changed. Cited by number only: Lagrange's theorem, the
    factor theorem bounding the number of roots of a nonzero polynomial over a field, the
    attainment of the exponent in a finite abelian group, the equality of the degree of a simple
    extension with the degree of the minimal polynomial, Dedekind's lemma on the independence of
    distinct characters, and the divisibility of the characteristic polynomial by the minimal
    polynomial. Checked: that the exponent divides $q-1$, that all $q-1$ units are distinct roots
    of $x^m-1$, that $\phi$ is an automorphism fixing $\FF_q$, and that $x^{q^n}=x$ for every
    element of $\FF_{q^n}$.
---

::: {.problem}
(a) If $\FF_q$ is a field with $q$ elements, show that $\FF_q^\times$ is a cyclic group.

(b) Show that for each integer $n \geq 1$, there exists an irreducible polynomial over $\FF_q$ of degree $n$.

(c) Consider the map $\phi: \FF_{q^n} \to \FF_{q^n}$ given by $\phi(x) = x^q$.
Note that $\phi$ is an $\FF_q$-linear endomorphism of the $\FF_q$-vector space $\FF_{q^n}$.
Find the characteristic and minimal polynomials of $\phi$.
:::

::: {.solution}

::: pf

::: pf-step
Part (a): $\FF_q^\times$ is cyclic:

::: pf-proof

::: pf-step
Let $G = \FF_q^\times$ be the multiplicative group of the finite field $\FF_q$, which is an abelian group of order $\cardinality{G} = q - 1$.
Let $m = \exp(G)$ denote the exponent of $G$, which is the least common multiple of the orders of all elements in $G$.
By Lagrange's Theorem, $m \le q - 1$.

::: pf-proof
The nonzero elements of a field form a group under multiplication, and it is abelian because multiplication in a field is commutative; it has $q-1$ elements because $\FF_q$ has $q$ and $0$ is the only excluded element. The exponent is the least common multiple of the element orders, each of which divides $\abs G=q-1$ by Lagrange's theorem, so the least common multiple of them divides $q-1$ and in particular is at most $q-1$.
:::

:::

::: pf-step
By definition of exponent, every element $x \in \FF_q^\times$ satisfies $x^m - 1 = 0$.
The polynomial $x^m - 1 \in \FF_q[x]$ has degree $m$ and can have at most $m$ roots in the field $\FF_q$.
Because all $q - 1$ elements of $\FF_q^\times$ are roots:
$$
q - 1 \le m.
$$

::: pf-proof
The exponent annihilates every element, so $x^m=1$ for all $x\in\FF_q^\times$. A nonzero polynomial of degree $m$ over a field has at most $m$ roots, counted without multiplicity, by the factor theorem: each root contributes a linear factor, and the degrees add. The $q-1$ elements of $\FF_q^\times$ are distinct roots, so $q-1\le m$.
:::

:::

::: pf-step
Combining $m \le q - 1$ and $q - 1 \le m$ gives $m = q - 1$.
For any finite abelian group, there exists an element whose order equals the exponent $m$.
Thus there exists $\alpha \in \FF_q^\times$ with $o(\alpha) = q - 1 = \cardinality{\FF_q^\times}$, so $\FF_q^\times = \langle \alpha \rangle$ is cyclic.

::: pf-proof
The two inequalities give equality of the exponent with the group order. In a finite abelian group the exponent is attained: writing the group as a product of cyclic groups of prime-power orders, the element whose components generate the largest cyclic factor of each prime attains the least common multiple of the orders. An element of order equal to $\abs{\FF_q^\times}$ generates a subgroup with as many elements as the group, hence the whole group.
:::

:::

:::

:::

::: pf-step
Part (b): Existence of an irreducible polynomial of degree $n$ over $\FF_q$:

::: pf-proof

::: pf-step
Consider the finite field extension $\FF_{q^n}$, which is an $n$-dimensional vector space over $\FF_q$, so $[\FF_{q^n} : \FF_q] = n$.

::: pf-proof
A finite field of order $q^n$ exists for every prime power $q^n$, and it contains its prime field; more generally it is a vector space over any subfield, and counting gives $\abs{\FF_{q^n}}=q^{[\FF_{q^n}:\FF_q]}$, so the degree is $n$. A vector space over a field with $q$ elements of dimension $d$ has $q^d$ elements, and $q^d=q^n$ forces $d=n$.
:::

:::

::: pf-step
By Part (a), the multiplicative group $\FF_{q^n}^\times$ is cyclic.
Let $\gamma$ be a generator of $\FF_{q^n}^\times$.
Then $\FF_{q^n} = \FF_q(\gamma)$.

::: pf-proof
Part (a) applies to the finite field $\FF_{q^n}$ and gives a generator $\gamma$ of its multiplicative group. Every nonzero element is then a power of $\gamma$, and $0$ is in $\FF_q\subseteq\FF_q(\gamma)$, so every element of $\FF_{q^n}$ lies in the subfield generated by $\FF_q$ and $\gamma$; the reverse inclusion is immediate, since $\gamma\in\FF_{q^n}$.
:::

:::

::: pf-step
Let $m_\gamma(x) \in \FF_q[x]$ be the minimal polynomial of $\gamma$ over $\FF_q$.
By field theory, $m_\gamma(x)$ is irreducible over $\FF_q$, and its degree is:
$$
\deg(m_\gamma) = [\FF_q(\gamma) : \FF_q] = [\FF_{q^n} : \FF_q] = n.
$$
Thus $m_\gamma(x)$ is an irreducible polynomial of degree $n$ over $\FF_q$.

::: pf-proof
The minimal polynomial of an algebraic element is the monic polynomial of least degree over the base field vanishing at it; it is irreducible, since a nontrivial factorisation would give a factor of smaller degree vanishing at $\gamma$. The degree of the extension generated by $\gamma$ equals the degree of its minimal polynomial, because $1,\gamma,\dots,\gamma^{d-1}$ with $d=\deg m_\gamma$ form a basis of $\FF_q(\gamma)$ over $\FF_q$. Step 2.2 identifies $\FF_q(\gamma)$ with $\FF_{q^n}$ and step 2.1 gives the degree $n$.
:::

:::

:::

:::

::: pf-step
Part (c): Characteristic and minimal polynomials of the Frobenius endomorphism $\phi$:

::: pf-proof

::: pf-step
The map $\phi: \FF_{q^n} \to \FF_{q^n}$ given by $\phi(x) = x^q$ is the Frobenius $\FF_q$-automorphism.
For any $x \in \FF_{q^n}$, $\phi^n(x) = x^{q^n} = x$, so $\phi^n = \operatorname{id}_{\FF_{q^n}}$.
Thus $\phi$ satisfies the polynomial $T^n - 1 \in \FF_q[T]$.

::: pf-proof
$\phi$ is additive because $(x+y)^q=x^q+y^q$ in characteristic $p$ by the binomial theorem, and multiplicative because $(xy)^q=x^qy^q$; it fixes $\FF_q$ because $a^q=a$ for $a\in\FF_q$. It is injective, since $x^q=0$ only for $x=0$, and a bijective endomorphism of a finite-dimensional space is an automorphism. Iterating, $\phi^n(x)=x^{q^n}$, and $x^{q^n}=x$ for every $x$ in the field with $q^n$ elements because its group of units has order $q^n-1$. So $\phi^n-\mathrm{id}=0$, which is the evaluation of $T^n-1$ at $\phi$.
:::

:::

::: pf-step
By Dedekind's Theorem on the linear independence of distinct group characters/automorphisms, the automorphisms $\{\operatorname{id}, \phi, \phi^2, \ldots, \phi^{n-1}\}$ are linearly independent over $\FF_{q^n}$ (and hence over $\FF_q$).

::: pf-proof
Dedekind's lemma states that distinct homomorphisms from a group to the multiplicative group of a field are linearly independent over that field; the automorphisms $\phi^k$ are distinct, since $\phi^k=\phi^\ell$ for $0\le k<\ell<n$ would force $q^k\equiv q^\ell$ in a way that contradicts the minimality of the degree $n$, and they are homomorphisms of the additive or the multiplicative group. Linear independence over $\FF_{q^n}$ implies that over the subfield $\FF_q$, since a nontrivial $\FF_q$-relation is a nontrivial $\FF_{q^n}$-relation.
:::

:::

::: pf-step
Therefore, no non-zero polynomial in $\FF_q[T]$ of degree strictly less than $n$ can annihilate $\phi$.
Since $T^n - 1$ is a monic polynomial of degree $n$ annihilating $\phi$, the minimal polynomial is:
$$
m_\phi(T) = T^n - 1.
$$

::: pf-proof
A polynomial $a_0+a_1T+\dots+a_{n-1}T^{n-1}$ of degree $<n$ annihilating $\phi$ means $a_0\mathrm{id}+a_1\phi+\dots+a_{n-1}\phi^{n-1}=0$, which is a linear relation among the automorphisms of step 3.2, so all coefficients vanish. Hence the minimal polynomial has degree exactly $n$, and $T^n-1$ is a monic annihilating polynomial of that degree, so it is the minimal polynomial.
:::

:::

::: pf-step
The characteristic polynomial $\chi_\phi(T)$ is a monic polynomial of degree $\dim_{\FF_q}(\FF_{q^n}) = n$ which is divisible by $m_\phi(T)$.
Since $\deg(m_\phi) = n = \deg(\chi_\phi)$ and both are monic:
$$
\chi_\phi(T) = T^n - 1.
$$

::: pf-proof
The characteristic polynomial of an endomorphism of an $n$-dimensional vector space is monic of degree $n$. The minimal polynomial divides the characteristic polynomial (Cayley--Hamilton together with the division algorithm for the minimal polynomial). Two monic polynomials of the same degree, one dividing the other, are equal, and here both have degree $n$ by step 3.3 and step 2.1.
:::

:::

:::

:::

::: pf-qed
Conclusion:

::: pf-proof
Part (a) is steps 1.1 to 1.3, part (b) steps 2.1 to 2.3, and part (c) steps 3.1 to 3.4; the three conclusions are that $\FF_q^\times$ is cyclic, that a minimal polynomial of a generator of $\FF_{q^n}^\times$ is irreducible of degree $n$, and that both the minimal and the characteristic polynomial of the Frobenius are $T^n-1$.
:::

:::

:::

:::
