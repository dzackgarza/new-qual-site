---
schema: qual/card@1
id: P-PRACT20-W5-14
kind: problem
title: Which of $p$, $p+q$, $pq$, $p^q$, $q^p$ lie in a proper subgroup of $\mathbb Z$
classification:
  areas:
  - algebra
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Rewrote the statement in clean LaTeX with spacing around inline math, checked against Week5_solns.pdf (Problem 14).
---

::: {.problem}
Let $p, q$ be distinct primes. If $J$ is a proper subgroup of $(\ZZ, +)$ containing exactly three of $\{p, p + q, pq, p^q, q^p\}$, which three elements does $J$ include?
:::

::: pf

::: pf-step

Every proper nonzero subgroup of $(\mathbb Z,+)$ has the form
\[
d\mathbb Z
\]
for some integer $d\ge2$.


::: pf-proof

Every subgroup of the infinite cyclic group $\mathbb Z$ is cyclic, hence has
the form $d\mathbb Z$ for a unique $d\ge0$. The subgroup is proper and
contains some nonzero element of the displayed set, so $d\ge2$.

:::

:::

::: pf-step

If $J=d\mathbb Z$ contains three of the five displayed integers, then
those three integers have a common divisor $d>1$.


::: pf-proof

Membership in $d\mathbb Z$ means divisibility by $d$. Thus if three elements
belong to $J$, then $d$ divides all three.

:::

:::

::: pf-step

The only three-element subset of
\[
\{p,p+q,pq,p^q,q^p\}
\]
having a common divisor greater than $1$ is
\[
\{p,pq,p^q\}.
\]


::: pf-proof

The three displayed numbers $p,pq,p^q$ are all divisible by $p$.

Any triple containing $p$ together with either $p+q$ or $q^p$ has greatest
common divisor $1$, because
\[
\gcd(p,p+q)=\gcd(p,q)=1
\]
and
\[
\gcd(p,q^p)=1.
\]

It remains to consider triples not containing $p$. Any triple containing both
$p+q$ and $pq$ has greatest common divisor $1$, since a common prime divisor
of $p+q$ and $pq$ would have to be $p$ or $q$, but neither prime divides
$p+q$. The only remaining triple is
\[
\{pq,p^q,q^p\},
\]
whose greatest common divisor is also $1$: the first two have common divisor
$p$, while $p\nmid q^p$.
Thus no other triple has a nontrivial common divisor.

:::

:::

::: pf-step

The subgroup
\[
J=p\mathbb Z
\]
contains exactly
\[
\boxed{p,\ pq,\ p^q}
\]
from the given set.


::: pf-proof

All three boxed numbers are divisible by $p$. Since $p$ and $q$ are distinct
primes,
\[
p\nmid p+q
\]
and
\[
p\nmid q^p.
\]
Thus the other two numbers do not belong to $p\mathbb Z$.

:::

:::

::: pf-qed

Steps <1>2 and <1>3 force the three members to be those in step <1>4, which
also shows that such a proper subgroup exists.

:::

:::
