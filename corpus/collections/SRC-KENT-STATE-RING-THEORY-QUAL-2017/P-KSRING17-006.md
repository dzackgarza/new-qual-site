---
schema: qual/card@1
id: P-KSRING17-006
kind: problem
title: Integers $n$ with $(\ZZ/n\ZZ)^\times$ an elementary abelian 2-group
classification:
  areas: [algebra]
  topics:
  - Units
  - Integers Modulo n
  - Elementary Abelian Groups
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against Problem 6 of the retained Kent State Algebra Qualifying Exam Problems — Ring Theory compilation, version August 29, 2017.
---

::: {.problem}
Find all positive integers n having the property that the group of units of $\ZZ / n \ZZ$ is an elementary abelian 2-group.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

A finite abelian group is an elementary abelian $2$-group if and only if every element has square equal to the identity.


::: pf-proof

An elementary abelian $2$-group is a finite direct product of copies of
$$
\ZZ/2\ZZ,
$$
so every element has order dividing $2$.

Conversely, if a finite abelian group $G$ satisfies
$$
g^2=1
$$
for every $g\in G$, then every nonidentity element has order $2$. Hence $G$ is a vector space over $\FF_2$, with its group law as addition, and is therefore isomorphic to
$$
(\ZZ/2\ZZ)^r
$$
for some $r\ge0$.

:::

:::

::: {.pf-step #s1-2}

If
$$
n=\prod_i p_i^{e_i},
$$
then
$$
(\ZZ/n\ZZ)^\times
\cong
\prod_i
(\ZZ/p_i^{e_i}\ZZ)^\times.
$$
Thus every unit modulo $n$ has square $1$ if and only if the same is true modulo every prime-power divisor $p_i^{e_i}$.


::: pf-proof

The Chinese remainder theorem gives
$$
\ZZ/n\ZZ
\cong
\prod_i
\ZZ/p_i^{e_i}\ZZ.
$$
An element in a product ring is a unit exactly when each coordinate is a unit, so passing to unit groups gives the displayed isomorphism. Squaring is coordinatewise, proving the final assertion.

:::

:::

::: {.pf-step #s1-3}

No odd prime $p\ge5$ can divide such an integer $n$.


::: pf-proof

If $p\mid n$, then by step [](#s1-2){.pf-ref} every nonzero class in
$$
\FF_p
$$
would satisfy
$$
x^2=1.
$$
But the polynomial
$$
X^2-1
$$
has at most two roots over the field $\FF_p$, whereas $\FF_p^\times$ has
$$
p-1\ge4
$$
elements. This is impossible.

:::

:::

::: {.pf-step #s1-4}

If $3^e\mid n$, then
$$
e\le1.
$$


::: pf-proof

Suppose $e\ge2$. The class
$$
u
\coloneqq
1+3^{e-1}
$$
is a unit modulo $3^e$, since it is congruent to $1$ modulo $3$. But
$$
\begin{aligned}
u^2-1
&=
2\cdot3^{e-1}
+
3^{2e-2}.
\end{aligned}
$$
The second term is divisible by $3^e$, while the first is not. Hence
$$
u^2\not\equiv1\pmod{3^e},
$$
contradicting step [](#s1-1){.pf-ref}. Therefore $e\le1$.

:::

:::

::: {.pf-step #s1-5}

If $2^e\mid n$, then
$$
e\le3.
$$


::: pf-proof

If $e\ge4$, the class of $3$ is a unit modulo $2^e$, but
$$
3^2=9
\not\equiv
1
\pmod{16}.
$$
Hence
$$
3^2\not\equiv1\pmod{2^e}
$$
for every $e\ge4$. This contradicts the exponent-$2$ condition. Thus $e\le3$.

:::

:::

::: {.pf-step #s1-6}

Consequently, every admissible $n$ divides $24$.


::: pf-proof

By step [](#s1-3){.pf-ref}, the only possible odd prime divisor is $3$. Step [](#s1-4){.pf-ref} permits at most one factor of $3$, and step [](#s1-5){.pf-ref} permits at most three factors of $2$. Hence
$$
n
\mid
2^3\cdot3
=
24.
$$

:::

:::

::: {.pf-step #s1-7}

Conversely, every positive divisor of $24$ has elementary abelian unit group.


::: pf-proof

It suffices by step [](#s1-2){.pf-ref} to check the prime powers
$$
2,\quad4,\quad8,\quad3.
$$
Their unit groups are
$$
\begin{aligned}
(\ZZ/2\ZZ)^\times
&=
\{\overline1\},\\
(\ZZ/4\ZZ)^\times
&=
\{\overline1,\overline3\},\\
(\ZZ/8\ZZ)^\times
&=
\{\overline1,\overline3,\overline5,\overline7\},\\
(\ZZ/3\ZZ)^\times
&=
\{\overline1,\overline2\}.
\end{aligned}
$$
Every listed element has square $\overline1$. Any divisor of $24$ is a product of a divisor of $8$ and a divisor of $3$ with coprime factors, so the Chinese remainder theorem implies that every unit modulo such an $n$ has square $1$. Step [](#s1-1){.pf-ref} then gives an elementary abelian $2$-group.

:::

:::

::: {.pf-step #s1-8}

Therefore the complete list is
$$
\boxed{
n\in
\{1,2,3,4,6,8,12,24\}.
}
$$


::: pf-proof

These are exactly the positive divisors of $24$, by steps [](#s1-6){.pf-ref} and [](#s1-7){.pf-ref}. For $n=1$, the unit group is the trivial group, viewed as $(\ZZ/2\ZZ)^0$.

:::

:::

::: pf-qed

Step [](#s1-8){.pf-ref} gives all and only the required positive integers.

:::

:::

:::
