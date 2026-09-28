---
schema: qual/card@1
id: P-BKF77-5
kind: problem
title: Units in $\mathbb Z_n$
classification:
  areas:
  - prelim
  topics:
  - Abstract Algebra
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-11
- event: solution-written
  by: chatgpt
  date: 2026-09-11
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-11
  note: "Proved the unit-group property and the gcd criterion, corrected the missing distinct-primes hypothesis in part (c), and counted units by inclusion-exclusion."
---

::: {.problem}
(a) Show that the set of all units in a ring with unity forms a group under multiplication.

(b) In $\mathbb Z_n$, show that $k$ is a unit if and only if $k$ and $n$ are relatively prime.

(c) If $n=pq$ with $p,q$ distinct primes, prove that the number of units in $\mathbb Z_n$ is $(p-1)(q-1)$.
:::

::: {.remark}
The printed source says only that $p$ and $q$ are primes. Distinctness is
necessary: if $p=q=2$, then $n=4$ and $\mathbb Z_4$ has the two units
$[1]$ and $[3]$, whereas $(p-1)(q-1)=1$.
:::

::: {.solution}
<1>1. The units of a ring with unity form a group under multiplication.
::: {.proof}
Let $R$ be a ring with identity $1$, and let
$$
R^\times=\{u\in R:\text{$u$ has a two-sided multiplicative inverse}\}.
$$
Associativity is inherited from multiplication in $R$, and $1$ belongs to
$R^\times$.

If $u,v\in R^\times$, then
$$
(uv)(v^{-1}u^{-1})
=u(vv^{-1})u^{-1}
=1,
$$
and similarly
$$
(v^{-1}u^{-1})(uv)=1.
$$
Thus $uv$ is a unit, with
$$
(uv)^{-1}=v^{-1}u^{-1}.
$$
Finally, if $u$ is a unit, then its inverse $u^{-1}$ is again a unit, with
inverse $u$. Hence $R^\times$ satisfies all the group axioms.
:::

<1>2. Characterize the units of $\mathbb Z_n$.
::: {.proof}
The residue class $[k]\in\mathbb Z_n$ is a unit exactly when there exists
$[\ell]\in\mathbb Z_n$ such that
$$
[k][\ell]=[1].
$$
This is equivalent to
$$
k\ell\equiv1\pmod n,
$$
or equivalently to the existence of integers $\ell,m$ satisfying
$$
k\ell+nm=1.
$$
By Bézout's identity, such integers exist if and only if
$$
\gcd(k,n)=1.
$$
Therefore
$$
\boxed{[k]\in\mathbb Z_n^\times\iff \gcd(k,n)=1.}
$$
:::

<1>3. Count the units when $n=pq$ with $p\ne q$ prime.
::: {.proof}
By step <1>2, a residue class modulo $pq$ fails to be a unit exactly when
its representative is divisible by $p$ or by $q$.

Among the $pq$ residue classes, exactly $q$ are multiples of $p$, and exactly
$p$ are multiples of $q$. Since $p$ and $q$ are distinct primes, the only
class divisible by both is $[0]$. Inclusion-exclusion therefore gives
$$
q+p-1
$$
nonunits. Hence the number of units is
$$
pq-(p+q-1)
=pq-p-q+1
=(p-1)(q-1).
$$
Thus
$$
\boxed{|\mathbb Z_{pq}^\times|=(p-1)(q-1).}
$$
:::
:::
