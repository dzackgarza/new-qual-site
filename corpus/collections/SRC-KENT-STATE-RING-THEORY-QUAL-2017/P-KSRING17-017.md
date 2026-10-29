---
schema: qual/card@1
id: P-KSRING17-017
kind: problem
title: The reduction map $U_n\to U_m$ is surjective
classification:
  areas: [algebra]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against Problem 17 of the retained Kent State Algebra Qualifying Exam Problems — Ring Theory compilation, version August 29, 2017.
---

::: {.problem}
Let m, n be positive integers such that m divides n. Then the natural map $\varphi : \ZZ _ { n } \to \ZZ _ { m }$ given by $a + ( n ) \mapsto a + ( m )$ is a surjective ring homomorphism.
If $U _ { n } , U _ { m }$ are the units of $\ZZ _ { n }$ and $\ZZ _ { m }$ , respectively, show that $\varphi : U _ { n } \to U _ { m }$ is a surjective group homomorphism.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

The restriction
$$
\varphi:U_n\to U_m
$$
is a group homomorphism.


::: pf-proof

Since $\varphi$ is a ring homomorphism,
$$
\varphi(\overline a\,\overline b)
=
\varphi(\overline a)\varphi(\overline b).
$$
If $\overline a\in U_n$, choose $\overline c$ with
$$
\overline a\,\overline c=\overline1.
$$
Then
$$
\varphi(\overline a)\varphi(\overline c)
=
\varphi(\overline1)
=
\overline1,
$$
so $\varphi(\overline a)\in U_m$. Thus the restriction is well-defined and multiplicative.

:::

:::

::: {.pf-step #s1-2}

Let
$$
\overline a\in U_m.
$$
Then there exists an integer $b$ such that
$$
b\equiv a\pmod m
$$
and
$$
\gcd(b,n)=1.
$$


::: pf-proof

Since $\overline a$ is a unit modulo $m$,
$$
\gcd(a,m)=1.
$$
Let
$$
P
\coloneqq
\prod_{\substack{p\mid n\\p\nmid m}}p,
$$
the product of the prime divisors of $n$ that do not divide $m$. Then
$$
\gcd(P,m)=1.
$$
By the Chinese remainder theorem, choose $b$ satisfying
$$
b\equiv a\pmod m,
\qquad
b\equiv1\pmod P.
$$

Let $p\mid n$. If $p\mid m$, then
$$
b\equiv a\pmod p
$$
and $p\nmid a$, hence $p\nmid b$. If $p\nmid m$, then $p\mid P$ and
$$
b\equiv1\pmod p,
$$
so again $p\nmid b$. Thus no prime divisor of $n$ divides $b$, and therefore
$$
\gcd(b,n)=1.
$$

:::

:::

::: {.pf-step #s1-3}

The map
$$
\varphi:U_n\to U_m
$$
is surjective.


::: pf-proof

Let $\overline a\in U_m$. Choose $b$ as in step [](#s1-2){.pf-ref}. Then
$$
\overline b\in U_n
$$
because $\gcd(b,n)=1$, and
$$
\varphi(\overline b)
=
\overline a
$$
because $b\equiv a\pmod m$. Hence every unit modulo $m$ has a preimage in $U_n$.

:::

:::

::: {.pf-step #s1-4}

Therefore
$$
\boxed{
\varphi:U_n\to U_m
\text{ is a surjective group homomorphism.}
}
$$


::: pf-proof

Combine steps [](#s1-1){.pf-ref} and [](#s1-3){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s1-4){.pf-ref} is the required conclusion.

:::

:::

:::
