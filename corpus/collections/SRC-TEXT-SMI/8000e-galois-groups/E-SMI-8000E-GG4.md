---
schema: qual/card@1
id: E-SMI-8000E-GG4
kind: problem
title: Every finite abelian group is a Galois group over Q via cyclotomic extensions
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
  date: 2026-09-11
  note: "Checked the Smith packet pointer and the Dummit--Foote Corollary 28 argument; the required number-theoretic input is the existence of primes congruent to 1 modulo a prescribed integer."
- event: solution-written
  by: chatgpt
  date: 2026-09-11
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-11
  note: "Proved the needed prime-congruence input using cyclotomic polynomials, then used the structure theorem, CRT, cyclotomic Galois groups, and Galois correspondence to realize an arbitrary finite abelian group."
---

::: {.exercise}
Work problems 14, 15, 16, 17, page 557 of Dummit and Foote, then deduce Corollary 28, page 600: every finite abelian group occurs as the Galois group over $\QQ$ of some subextension of a cyclotomic extension.
:::

::: {.solution}

::: pf

::: {.pf-step #df14}

Every nonconstant monic polynomial in $\ZZ[x]$ has infinitely many prime divisors among its values at positive integers.

::: pf-proof

Let $F\in\ZZ[x]$ be monic of positive degree. Suppose that only the primes
$q_1,\ldots,q_k$ divide its nonzero values at positive integers. Choose
$N>0$ with $a=F(N)\ne0$ and put $Q=q_1\cdots q_k$. The polynomial
$$
B(t)=\frac{F(N+aQt)}{a}
$$
has integer coefficients: its constant term is $1$, and every other term
in its expansion about $N$ is divisible by $aQ$ before division by $a$.
Thus $B(t)\equiv1\pmod Q$ for every integer $t$.

Choose $t$ so that $N+aQt>0$ and $\abs{B(t)}>1$; both hold sufficiently
far along the direction in which $aQt$ is positive. A prime $q$ dividing
$B(t)$ divides $F(N+aQt)$ but does not divide $Q$. This contradicts the
list $q_1,\ldots,q_k$.

:::

:::

::: {.pf-step #df15}

If $p$ is an odd prime with $p\nmid m$ and $p\mid\Phi_m(a)$, then $a$ has order $m$ modulo $p$.

::: pf-proof

The factorization $x^m-1=\prod_{d\mid m}\Phi_d(x)$ gives
$a^m\equiv1\pmod p$, so $a$ is a unit modulo $p$ and its order $d$
divides $m$. If $d<m$, then $a$ is a root modulo $p$ of both
$x^d-1$ and $\Phi_m(x)$. Since both divide $x^m-1$ as distinct factors,
$a$ would be a multiple root of $x^m-1$ modulo $p$. But its derivative
is $mx^{m-1}$, which is nonzero at $a$ because $p\nmid m$ and $a$ is a
unit. Hence $d=m$.

:::

:::

::: {.pf-step #df16}

If an odd prime $p$ divides $\Phi_m(a)$, then either $p\mid m$ or $p\equiv1\pmod m$.

::: pf-proof

When $p\nmid m$, step [](#df15){.pf-ref} gives an element of order $m$
in $(\ZZ/p\ZZ)^\times$, whose order is $p-1$. Lagrange's theorem gives
$m\mid p-1$.

:::

:::

::: {.pf-step #s1}

For every positive integer $m$, there are infinitely many primes $p$ with $p\equiv1\pmod m$.

::: pf-proof

The cyclotomic polynomial $\Phi_m(x)$ is monic of positive degree. By
step [](#df14){.pf-ref}, infinitely many primes divide its values at
positive integers. Only finitely many of these primes divide $2m$.
Every other such prime is odd, does not divide $m$, and is congruent
to $1$ modulo $m$ by step [](#df16){.pf-ref}.

:::

:::

::: pf-step

Write the given finite abelian group as a product of cyclic groups.

::: pf-proof

Let $A$ be any finite abelian group. By the structure theorem for finite
abelian groups, there are positive integers $n_1,\ldots,n_r$ such that
$$
A\cong C_{n_1}\times\cdots\times C_{n_r}.
$$
We may discard any factor with $n_i=1$.

:::

:::

::: pf-step

Choose distinct primes whose unit groups have the required cyclic quotients.

::: pf-proof

By step [](#s1){.pf-ref}, choose distinct primes
$$
p_i\equiv1\pmod{n_i}
$$
for $1\le i\le r$. Since $p_i$ is prime,
$$
(\ZZ/p_i\ZZ)^\times
$$
is cyclic of order $p_i-1$. Because $n_i\mid p_i-1$, it has a unique subgroup
$H_i$ of order
$$
\frac{p_i-1}{n_i},
$$
and therefore
$$
(\ZZ/p_i\ZZ)^\times/H_i\cong C_{n_i}.
$$

:::

:::

::: pf-step

Assemble the cyclic quotients inside one cyclotomic Galois group.

::: pf-proof

Put
$$
N=p_1p_2\cdots p_r.
$$
The Chinese remainder theorem gives
$$
(\ZZ/N\ZZ)^\times
\cong
\prod_{i=1}^r(\ZZ/p_i\ZZ)^\times.
$$
Let
$$
H=H_1\times\cdots\times H_r
$$
under this identification. Then
$$
\begin{aligned}
(\ZZ/N\ZZ)^\times/H
&\cong
\prod_{i=1}^r
\bigl((\ZZ/p_i\ZZ)^\times/H_i\bigr)\\
&\cong C_{n_1}\times\cdots\times C_{n_r}\\
&\cong A.
\end{aligned}
$$

:::

:::

::: pf-step

Apply cyclotomic Galois theory and the fundamental theorem of Galois theory.

::: pf-proof

Let
$$
L=\QQ(\zeta_N).
$$
Cyclotomic Galois theory gives
$$
\operatorname{Gal}(L/\QQ)
\cong(\ZZ/N\ZZ)^\times
$$
via
$$
a\longmapsto(\zeta_N\mapsto\zeta_N^a)
$$
[@DF04]. Let the subgroup corresponding to $H$ under this isomorphism again
be denoted $H$, and set
$$
K=L^H.
$$

The ambient Galois group is abelian, so $H$ is normal. Hence
$K/\QQ$ is Galois, and the fundamental theorem of Galois theory yields
$$
\operatorname{Gal}(K/\QQ)
\cong\operatorname{Gal}(L/\QQ)/H
\cong A.
$$
Thus
$$
\boxed{\text{every finite abelian group occurs as }
\operatorname{Gal}(K/\QQ)
\text{ for a subfield }K\subseteq\QQ(\zeta_N).}
$$

:::

:::

:::

:::
