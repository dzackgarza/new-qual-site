---
schema: qual/card@1
id: P-PRACT20-W5-14
kind: problem
title: Which of $p$, $p+q$, $pq$, $p^q$, $q^p$ lie in a proper subgroup of $\ZZ$
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

::: {.solution}

::: pf

::: pf-step

Every proper nonzero subgroup of $(\ZZ,+)$ has the form
\[
d\ZZ
\]
for some integer $d\ge2$.


::: pf-proof

Every subgroup of the infinite cyclic group $\ZZ$ is cyclic, hence has
the form $d\ZZ$ for a unique $d\ge0$. The subgroup is proper and
contains some nonzero element of the displayed set, so $d\ge2$.

:::

:::

::: {.pf-step #s1-2}

If $J=d\ZZ$ contains three of the five displayed integers, then
those three integers have a common divisor $d>1$.


::: pf-proof

Membership in $d\ZZ$ means divisibility by $d$. Thus if three elements
belong to $J$, then $d$ divides all three.

:::

:::

::: {.pf-step #s1-3}

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

::: {.pf-step #s1-4}

The subgroup
\[
J=p\ZZ
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
Thus the other two numbers do not belong to $p\ZZ$.

:::

:::

::: pf-qed

Steps [](#s1-2){.pf-ref} and [](#s1-3){.pf-ref} force the three members to be those in step [](#s1-4){.pf-ref}, which
also shows that such a proper subgroup exists.

:::

:::

:::
