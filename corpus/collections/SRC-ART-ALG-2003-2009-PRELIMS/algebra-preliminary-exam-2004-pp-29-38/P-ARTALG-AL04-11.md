---
schema: qual/card@1
id: P-ARTALG-AL04-11
kind: problem
title: 'Subfields of a field of order $5^{20}$'
classification:
  areas:
  - algebra
  topics:
  - Galois Theory
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-10
  note: "Recovered the omitted 2004 Fields 4 from PDF page 38 (printed page 10), visually checking the exponent 20, both parts, and the requested order 25."
- event: solution-written
  by: chatgpt
  date: 2026-09-10
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-10
  note: "Checked the characteristic and tower-degree restriction, existence via divisibility of Frobenius polynomials, field closure of each root set, and uniqueness as an actual subfield rather than merely up to isomorphism."
---

::: problem
(a) Let $F$ be a field of order $5^{20}$. List the orders of all the subfields of $F$.

(b) Does $F$ have more than one subfield of order $25$? Explain.
:::

::: solution
The subfield orders are
$$
5,\quad 5^2,\quad 5^4,\quad 5^5,\quad 5^{10},\quad 5^{20}.
$$
There is exactly one subfield of each listed order. In particular,
there is exactly one subfield of order $25$.

<1>1. Every subfield has order $5^d$ with $d$ a positive divisor of $20$.

::: proof
The characteristic of a finite field is a prime dividing its order:
the additive order of $1$ divides the additive group order, and a
composite characteristic would give nonzero zero divisors.
Here that prime must be $5$. Thus $F$ contains its prime field
$\mathbb F_5$. If $[F:\mathbb F_5]=n$, a basis counts its
elements as $5^n$, so $n=20$.

Every subfield $K$ contains $\mathbb F_5$. Writing
$d=[K:\mathbb F_5]$, the tower law gives
$$
20=[F:\mathbb F_5]=[F:K]d.
$$
Consequently $d\mid20$ and $|K|=5^d$. The positive divisors
of $20=2^2\cdot5$ are exactly $1,2,4,5,10,20$.
:::

<1>2. For each $d\mid20$, the set
$F_d=\{a\in F:a^{5^d}=a\}$ is a subfield with exactly $5^d$ elements.

::: proof
Put $h_d(T)=T^{5^d}-T$. First, $h_d$ divides $h_{20}$ in
$\mathbb F_5[T]$. Indeed, in the quotient ring by $(h_d)$ the
class $t$ of $T$ satisfies $t^{5^d}=t$. Repeatedly taking the
$5^d$th power gives $t^{5^{kd}}=t$ for every positive integer
$k$. Taking $k=20/d$ shows that $h_{20}$ has zero class in
this quotient, which is exactly the asserted divisibility.

Every nonzero element of $F$ satisfies $a^{5^{20}-1}=1$ by
Lagrange's theorem in its multiplicative group [@DF04]. Zero
also satisfies $h_{20}(0)=0$. Thus
$$
h_{20}(T)=\prod_{a\in F}(T-a),
$$
a product of distinct linear factors. A monic divisor of this
polynomial is itself a product of distinct linear factors in
$F[T]$, by unique factorization in a polynomial ring over a field
[@DF04]. Hence $h_d$ has exactly its degree, $5^d$, distinct
roots in $F$.

It remains to check that those roots form a field. The map
$a\mapsto a^{5^d}$ is a field homomorphism, as follows by
iterating the characteristic-five identity
$(a+b)^5=a^5+b^5$ and using multiplicativity.
Its fixed elements contain $0,1$ and are closed under addition,
subtraction, and multiplication. For a nonzero fixed element $a$,
$$
(a^{-1})^{5^d}=(a^{5^d})^{-1}=a^{-1},
$$
so they are also closed under inversion. This proves that $F_d$
is a subfield, with the cardinality already established.
:::

<1>3. A subfield of a given listed order is unique.

::: proof
If $K\subseteq F$ has order $5^d$, every nonzero $a\in K$
satisfies $a^{5^d-1}=1$ by Lagrange's theorem in $K^\times$.
Including zero, every element of $K$ satisfies $a^{5^d}=a$.
Thus $K\subseteq F_d$. Since both fields have $5^d$ elements,
they are equal. Together with steps <1>1 and <1>2, this proves
that the displayed list is exhaustive and each order is realized
by exactly one embedded subfield. For $d=2$ this says
$$
\{a\in F:a^{25}=a\}
$$
is the unique subfield of order $25$, answering part (b).
:::
:::
