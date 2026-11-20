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
- event: solution-written
  by: claude
  date: 2026-11-20
  note: >-
    Part (c) repaired. Dedekind's lemma was applied to the Frobenius powers with
    their distinctness asserted only vaguely, as something that "would force
    q^k congruent to q^l in a way" contradicting the degree. A new step proves
    that id, phi, ..., phi^{n-1} are pairwise distinct by evaluating at a
    generator gamma of the multiplicative group: equality would give
    gamma^{q^l - q^k} = 1, hence q^n - 1 divides q^l - q^k, which is impossible
    because that difference lies strictly between 0 and q^n - 1. The Dedekind
    step now applies the lemma to the restrictions of the powers to the
    multiplicative group and derives linear independence of the endomorphisms
    over FF_{q^n} and over FF_q, and the later steps cite the new step by
    reference instead of by number. No statement, claim or part is changed.
    Cited by number only: Dedekind's lemma, Cayley-Hamilton.
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

::: {.pf-step #part-a}
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

::: {.pf-step #part-b}
Part (b): Existence of an irreducible polynomial of degree $n$ over $\FF_q$:

::: pf-proof

::: {.pf-step #degree}
Consider the finite field extension $\FF_{q^n}$, which is an $n$-dimensional vector space over $\FF_q$, so $[\FF_{q^n} : \FF_q] = n$.

::: pf-proof
A finite field of order $q^n$ exists for every prime power $q^n$, and it contains its prime field; more generally it is a vector space over any subfield, and counting gives $\abs{\FF_{q^n}}=q^{[\FF_{q^n}:\FF_q]}$, so the degree is $n$. A vector space over a field with $q$ elements of dimension $d$ has $q^d$ elements, and $q^d=q^n$ forces $d=n$.
:::

:::

::: {.pf-step #generator}
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

::: {.pf-step #part-c}
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

::: {.pf-step #distinct}
The automorphisms $\operatorname{id}, \phi, \phi^2, \ldots, \phi^{n-1}$ are pairwise distinct.

::: pf-proof
By step [](#generator){.pf-ref} there is a generator $\gamma$ of the multiplicative group $\FF_{q^n}^\times$, an element of order $q^n - 1$.
Suppose that $\phi^k = \phi^\ell$ with $0 \le k < \ell \le n-1$.
Evaluating both sides at $\gamma$ gives $\gamma^{q^k} = \gamma^{q^\ell}$, hence $\gamma^{q^\ell - q^k} = 1$.
Since $\gamma$ has order $q^n - 1$, this forces $q^n - 1 \mid q^\ell - q^k$.
But
$$
0 < q^\ell - q^k \le q^{n-1} - 1 < q^n - 1:
$$
the lower bound holds because $\ell > k$ and $q \ge 2$, and the upper bound because $\ell \le n-1$ and $k \ge 0$.
No positive multiple of $q^n - 1$ is smaller than $q^n - 1$, so no such pair $k < \ell$ exists.
:::

:::

::: {.pf-step #dedekind}
The automorphisms $\operatorname{id}, \phi, \phi^2, \ldots, \phi^{n-1}$ are linearly independent over $\FF_{q^n}$, hence also over $\FF_q$.

::: pf-proof
Dedekind's lemma states that distinct homomorphisms from a group to the multiplicative group of a field are linearly independent over that field.
The restrictions of $\operatorname{id}, \phi, \ldots, \phi^{n-1}$ to the multiplicative group $\FF_{q^n}^\times$ are homomorphisms into $\FF_{q^n}^\times$, and they are distinct by step [](#distinct){.pf-ref}; so they are linearly independent over $\FF_{q^n}$.
A linear relation among the endomorphisms themselves restricts to one among these characters, so the endomorphisms are linearly independent over $\FF_{q^n}$ as well.
A nontrivial relation with coefficients in $\FF_q$ is in particular a nontrivial relation with coefficients in $\FF_{q^n}$, so independence over $\FF_{q^n}$ implies independence over $\FF_q$.
:::

:::

::: {.pf-step #minimal}
Therefore, no non-zero polynomial in $\FF_q[T]$ of degree strictly less than $n$ can annihilate $\phi$.
Since $T^n - 1$ is a monic polynomial of degree $n$ annihilating $\phi$, the minimal polynomial is:
$$
m_\phi(T) = T^n - 1.
$$

::: pf-proof
A polynomial $a_0+a_1T+\dots+a_{n-1}T^{n-1}$ of degree $<n$ annihilating $\phi$ means $a_0\mathrm{id}+a_1\phi+\dots+a_{n-1}\phi^{n-1}=0$, which is a linear relation among the automorphisms of step [](#dedekind){.pf-ref}, so all coefficients vanish. Hence no nonzero polynomial over $\FF_q$ of degree less than $n$ annihilates $\phi$. The minimal polynomial divides the annihilating polynomial $T^n-1$, so its degree is at most $n$, and no annihilator of smaller degree exists, so its degree is exactly $n$. Both it and $T^n-1$ are monic of degree $n$, and the minimal polynomial divides $T^n-1$, so the two are equal.
:::

:::

::: pf-step
The characteristic polynomial $\chi_\phi(T)$ is a monic polynomial of degree $\dim_{\FF_q}(\FF_{q^n}) = n$ which is divisible by $m_\phi(T)$.
Since $\deg(m_\phi) = n = \deg(\chi_\phi)$ and both are monic:
$$
\chi_\phi(T) = T^n - 1.
$$

::: pf-proof
The characteristic polynomial of an endomorphism of an $n$-dimensional vector space is monic of degree $n$. The minimal polynomial divides the characteristic polynomial (Cayley--Hamilton together with the division algorithm for the minimal polynomial). Two monic polynomials of the same degree, one dividing the other, are equal, and here both have degree $n$ by step [](#minimal){.pf-ref} and step [](#degree){.pf-ref}.
:::

:::

:::

:::

::: pf-qed
Conclusion:

::: pf-proof
Step [](#part-a){.pf-ref} proves that $\FF_q^\times$ is cyclic, step [](#part-b){.pf-ref} that a minimal polynomial of a generator of $\FF_{q^n}^\times$ is irreducible of degree $n$, and step [](#part-c){.pf-ref} that both the minimal and the characteristic polynomial of the Frobenius are $T^n-1$.
:::

:::

:::

:::
