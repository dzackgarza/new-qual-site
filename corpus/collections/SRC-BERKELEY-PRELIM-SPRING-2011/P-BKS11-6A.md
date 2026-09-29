---
schema: qual/card@1
id: P-BKS11-6A
kind: problem
title: Exponent of $(\mathbb Z/N\mathbb Z)^\times$ for $N=2^4\cdot 3^3\cdot 5^2\cdot 7$
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-25
  note: Compared the authored statement with page 2 of the retained Spring 2011 solution PDF and independently reviewed the Chinese-remainder exponent computation.
- event: solution-written
  by: chatgpt
  date: 2026-09-25
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-25
  note: Independently checked sufficiency and minimality of the exponents modulo 16, 27, 25, and 7 and their least common multiple.
---

::: {.problem}
If N is the integer $2 ^ { 4 } \cdot 3 ^ { 3 } \cdot 5 ^ { 2 } \cdot 7$ find the smallest positive integer m such that $x ^ { m } \equiv 1$ mod N for all integers x coprime to N .
:::

::: {.solution}
Set
$$
N=16\cdot27\cdot25\cdot7.
$$

::: pf

::: {.pf-step #exponent-16}
The exponent of $(\ZZ/16\ZZ)^\times$ is $4$.

::: pf-proof
Let $x$ be odd. Then
$$
x^2\equiv1\pmod8,
$$
so
$$
x^2=1+8q
$$
for some integer $q$. Squaring gives
$$
x^4
=
1+16q+64q^2
\equiv
1
\pmod{16}.
$$
Thus every unit modulo $16$ has fourth power $1$. The residue class of
$3$ has exact order $4$, since
$$
3^2=9\not\equiv1\pmod{16}
$$
while
$$
3^4=81\equiv1\pmod{16}.
$$
:::

:::

::: {.pf-step #exponent-27}
The exponent of $(\ZZ/27\ZZ)^\times$ is $18$.

::: pf-proof
Euler's theorem gives
$$
x^{18}\equiv1\pmod{27}
$$
for every unit $x$, since
$$
\varphi(27)=18.
$$
The class of $2$ has exact order $18$. Indeed,
$$
2^9=512\equiv-1\pmod{27},
$$
so its order does not divide $9$, while
$$
2^2=4\not\equiv1\pmod{27}
$$
and
$$
2^6=64\equiv10\not\equiv1\pmod{27}.
$$
Among the divisors of $18$, this rules out every proper divisor as the
order of $2$.
:::

:::

::: {.pf-step #exponent-25}
The exponent of $(\ZZ/25\ZZ)^\times$ is $20$.

::: pf-proof
Euler's theorem gives
$$
x^{20}\equiv1\pmod{25}
$$
for every unit $x$. The class of $2$ has exact order $20$: one has
$$
2^{10}=1024\equiv-1\pmod{25},
$$
so the order does not divide $10$, while
$$
2^4=16\not\equiv1\pmod{25}.
$$
The proper divisors of $20$ are $1,2,4,5,10$; the displayed congruences
exclude all of them.
:::

:::

::: {.pf-step #exponent-7}
The exponent of $(\ZZ/7\ZZ)^\times$ is $6$.

::: pf-proof
Fermat's theorem gives
$$
x^6\equiv1\pmod7
$$
for every unit $x$. The class of $3$ has exact order $6$, because
$$
3^3=27\equiv-1\pmod7
$$
and
$$
3^2=9\equiv2\not\equiv1\pmod7.
$$
:::

:::

::: {.pf-step #exponent-formula}
The exponent of $(\ZZ/N\ZZ)^\times$ is
$$
\operatorname{lcm}(4,18,20,6)=180.
$$

::: pf-proof
The four moduli $16,27,25,7$ are pairwise coprime, so the Chinese
remainder theorem gives
$$
(\ZZ/N\ZZ)^\times
\cong
(\ZZ/16\ZZ)^\times
\times
(\ZZ/27\ZZ)^\times
\times
(\ZZ/25\ZZ)^\times
\times
(\ZZ/7\ZZ)^\times.
$$
An integer power annihilates every element of a direct product exactly
when it is a common multiple of the exponents of all factors. Steps
[](#exponent-16){.pf-ref}, [](#exponent-27){.pf-ref}, [](#exponent-25){.pf-ref} and [](#exponent-7){.pf-ref} therefore give the exponent as their least common multiple.
Direct calculation yields
$$
\operatorname{lcm}(4,18,20,6)
=
2^2\cdot3^2\cdot5
=
180.
$$
:::

:::

::: {.pf-step #minimal-m}
The smallest positive integer with the required property is
$$
\boxed{180}.
$$

::: pf-proof
Step [](#exponent-formula){.pf-ref} shows both that every unit modulo $N$ has $180$th power $1$ and
that any exponent with this property must be divisible by each of
$4,18,20,6$, hence by $180$.
:::

:::

::: pf-qed
Step [](#minimal-m){.pf-ref} is the required minimal exponent.
:::

:::

:::
