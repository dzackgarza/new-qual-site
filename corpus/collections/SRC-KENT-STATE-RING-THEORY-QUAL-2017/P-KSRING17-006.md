---
schema: qual/card@1
id: P-KSRING17-006
kind: problem
title: Integers $n$ with $(\mathbb Z/n\mathbb Z)^\times$ an elementary abelian 2-group
classification:
  areas: [algebra]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against Problem 6 of the retained Kent State Algebra Qualifying Exam Problems — Ring Theory compilation, version August 29, 2017.
---

::: {.problem}
[NEW] Find all positive integers n having the property that the group of units of $\mathbb { Z } / n \mathbb { Z }$ is an elementary abelian 2-group.
:::

::: {.solution}
<1>1. A finite abelian group is an elementary abelian $2$-group if and only if every element has square equal to the identity.

::: {.proof}
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

<1>2. If
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

::: {.proof}
The Chinese remainder theorem gives
$$
\ZZ/n\ZZ
\cong
\prod_i
\ZZ/p_i^{e_i}\ZZ.
$$
An element in a product ring is a unit exactly when each coordinate is a unit, so passing to unit groups gives the displayed isomorphism. Squaring is coordinatewise, proving the final assertion.
:::

<1>3. No odd prime $p\ge5$ can divide such an integer $n$.

::: {.proof}
If $p\mid n$, then by step <1>2 every nonzero class in
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

<1>4. If $3^e\mid n$, then
$$
e\le1.
$$

::: {.proof}
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
contradicting step <1>1. Therefore $e\le1$.
:::

<1>5. If $2^e\mid n$, then
$$
e\le3.
$$

::: {.proof}
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

<1>6. Consequently, every admissible $n$ divides $24$.

::: {.proof}
By step <1>3, the only possible odd prime divisor is $3$. Step <1>4 permits at most one factor of $3$, and step <1>5 permits at most three factors of $2$. Hence
$$
n
\mid
2^3\cdot3
=
24.
$$
:::

<1>7. Conversely, every positive divisor of $24$ has elementary abelian unit group.

::: {.proof}
It suffices by step <1>2 to check the prime powers
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
Every listed element has square $\overline1$. Any divisor of $24$ is a product of a divisor of $8$ and a divisor of $3$ with coprime factors, so the Chinese remainder theorem implies that every unit modulo such an $n$ has square $1$. Step <1>1 then gives an elementary abelian $2$-group.
:::

<1>8. Therefore the complete list is
$$
\boxed{
n\in
\{1,2,3,4,6,8,12,24\}.
}
$$

::: {.proof}
These are exactly the positive divisors of $24$, by steps <1>6 and <1>7. For $n=1$, the unit group is the trivial group, viewed as $(\ZZ/2\ZZ)^0$.
:::

<1>9. Q.E.D.

::: {.proof}
Step <1>8 gives all and only the required positive integers.
:::
:::
