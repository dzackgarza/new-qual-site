---
schema: qual/card@1
id: P-KSRING17-007
kind: problem
title: Surjectivity of $U(\mathbb Z_n)\to U(\mathbb Z_m)$ and its failure for general ring surjections
classification:
  areas: [algebra]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against Problem 7 of the retained Kent State Algebra Qualifying Exam Problems — Ring Theory compilation, version August 29, 2017.
---

::: {.problem}
Let $U ( R )$ denote the group of units of a ring R. Prove that if m divides n, then the natural ring homomorphism $\mathbb { Z } _ { n } \to \mathbb { Z } _ { m }$ maps $U ( \mathbb { Z } _ { n } )$ onto $U ( \mathbb { Z } _ { m } )$

Give an example that shows that $U ( R )$ does not have to map onto $U ( S )$ under a surjective ring homomorphism $R \to S$ .
:::

::: {.solution}
<1>1. Let
$$
m\mid n
$$
and let
$$
\pi:\ZZ/n\ZZ\longrightarrow\ZZ/m\ZZ
$$
be the natural quotient homomorphism.
Fix a unit
$$
\overline a\in(\ZZ/m\ZZ)^\times.
$$

::: {.proof}
Since $\overline a$ is a unit modulo $m$,
$$
\gcd(a,m)=1.
$$
We must find an integer $b$ such that
$$
b\equiv a\pmod m
$$
and
$$
\gcd(b,n)=1.
$$
Then $\overline b$ will be a unit modulo $n$ mapping to $\overline a$.
:::

<1>2. Let
$$
P
\coloneqq
\prod_{\substack{p\mid n\\p\nmid m}}p,
$$
the product of the prime divisors of $n$ that do not divide $m$.
Then
$$
\gcd(P,m)=1.
$$

::: {.proof}
By construction, every prime factor of $P$ fails to divide $m$. Therefore no prime divides both $P$ and $m$, so they are relatively prime.
:::

<1>3. There exists an integer $b$ satisfying
$$
b\equiv a\pmod m,
\qquad
b\equiv1\pmod P.
$$

::: {.proof}
Step <1>2 gives
$$
\gcd(m,P)=1.
$$
The Chinese remainder theorem therefore gives a simultaneous solution to the two congruences.
:::

<1>4. The integer $b$ from step <1>3 satisfies
$$
\gcd(b,n)=1.
$$

::: {.proof}
Let $p$ be any prime divisor of $n$.

If
$$
p\mid m,
$$
then
$$
b\equiv a\pmod p.
$$
Since $\gcd(a,m)=1$, one has $p\nmid a$, hence $p\nmid b$.

If
$$
p\nmid m,
$$
then $p\mid P$, so
$$
b\equiv1\pmod p,
$$
and again $p\nmid b$.

Thus no prime divisor of $n$ divides $b$, which is exactly
$$
\gcd(b,n)=1.
$$
:::

<1>5. The natural map on unit groups
$$
\boxed{
(\ZZ/n\ZZ)^\times
\longrightarrow
(\ZZ/m\ZZ)^\times
}
$$
is surjective.

::: {.proof}
For the arbitrary unit $\overline a$ chosen in step <1>1, steps <1>3--<1>4 construct a unit
$$
\overline b\in(\ZZ/n\ZZ)^\times
$$
such that
$$
\pi(\overline b)=\overline a.
$$
Hence every unit modulo $m$ has a unit lift modulo $n$.
:::

<1>6. Surjectivity on units fails for general surjective ring homomorphisms.

::: {.proof}
Consider the quotient map
$$
q:\ZZ\longrightarrow\ZZ/8\ZZ.
$$
It is a surjective ring homomorphism. The units of $\ZZ$ are
$$
U(\ZZ)=\{1,-1\},
$$
so their images are
$$
q(U(\ZZ))
=
\{\overline1,\overline7\}.
$$
But
$$
U(\ZZ/8\ZZ)
=
\{
\overline1,
\overline3,
\overline5,
\overline7
\}.
$$
In particular,
$$
\overline3
$$
and
$$
\overline5
$$
are units in the quotient with no unit preimage in $\ZZ$. Therefore
$$
U(\ZZ)\to U(\ZZ/8\ZZ)
$$
is not surjective.
:::

<1>7. Q.E.D.

::: {.proof}
Step <1>5 proves the first assertion, and step <1>6 gives the requested counterexample.
:::
:::
