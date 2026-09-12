---
schema: qual/card@1
id: P-ARTALG-SU05-5
kind: problem
title: 'Roots of $x^{80}-1$, $x^{81}-1$, and $x^{88}-1$ over $\mathbb F_{81}$'
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
  note: "Compared the field order and all three polynomial exponents with Summer 2005 problem 5 in the retained source extraction."
- event: solution-written
  by: chatgpt
  date: 2026-09-10
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-10
  note: "Checked characteristic 3, the distinction between root counts and multiplicities, and splitting of x^8-1 as a divisor of x^80-1."
---

::: problem
Let $F$ be a field of 81 elements.
For each of the following polynomials, determine the number of roots that lie in $F$: $x^{80}-1$, $x^{81}-1$, $x^{88}-1$.
:::

::: solution
The numbers of distinct roots in $F$ are, respectively,
$$
\boxed{80,\quad 1,\quad 8}.
$$

<1>1. The characteristic is $3$, and every nonzero $a\in F$
satisfies $a^{80}=1$.

::: proof
The additive order of $1$ divides $|F|=81$. It is a prime:
if it were $uv$ with $1<u,v<uv$, then the two nonzero field
elements $u\cdot1$ and $v\cdot1$ would have product zero.
Thus the characteristic is the only prime dividing $81$, namely
$3$. The multiplicative group $F^\times$ has order $80$, so
Lagrange's theorem gives $a^{80}=1$ for every $a\ne0$ [@DF04].
:::

<1>2. The polynomial $x^{80}-1$ has $80$ distinct roots in $F$.

::: proof
Every element of $F^\times$ is a root by step <1>1, and zero
is not a root. There are exactly $80$ such elements. In particular,
the monic degree-$80$ polynomial factors as
$$
x^{80}-1=\prod_{a\in F^\times}(x-a).
$$
:::

<1>3. The polynomial $x^{81}-1$ has exactly one root in $F$.

::: proof
In characteristic $3$ the binomial theorem gives
$(u-v)^3=u^3-v^3$. Iterating four times yields
$$
x^{81}-1=(x-1)^{81}.
$$
Hence the only root is $1$, with multiplicity $81$. Counting
multiplicity would not give the number of distinct elements of
$F$ requested here.
:::

<1>4. The polynomial $x^{88}-1$ has exactly $8$ roots in $F$.

::: proof
A root $a$ must be nonzero. Using $a^{80}=1$, the equation
$a^{88}=1$ is equivalent to $a^8=1$. Thus the roots in $F$
are precisely those of $x^8-1$.

The identity
$$
x^{80}-1=(x^8-1)(1+x^8+x^{16}+\cdots+x^{72})
$$
shows that $x^8-1$ divides the product of distinct linear factors
in step <1>2. Unique factorization in the polynomial ring over
a field implies that this monic divisor is itself a product of
distinct linear factors in $F[x]$ [@DF04]. Its degree is $8$,
so it has exactly $8$ distinct roots in $F$.
:::
:::
