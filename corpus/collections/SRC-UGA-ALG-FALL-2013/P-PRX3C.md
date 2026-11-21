---
schema: qual/card@1
id: P-PRX3C
kind: problem
title: Prime and maximal ideals, with examples in $\ZZ$
classification:
  areas:
  - algebra
  topics:
  - Prime Ideals
  - Maximal Ideals
  - Ideals
relations: []
review: draft
audit:
  - event: source-checked
    by: claude
    date: 2026-11-19
    note: >-
      Read against the UGA algebra qualifying exam retained for this collection as
      SRC-UGA-ALG-FALL-2013; the card's two parts are that exam's question, asking for the
      definitions of prime and maximal ideal with an example in Z of each kind and proofs.
  - event: solution-written
    by: claude
    date: 2026-11-19
    note: >-
      Rewritten into numbered steps from the card's own prose; no retained solution set for
      this exam covers it. The prose justified maximality of pZ by two general theorems that
      it did not state (that primes are maximal in a PID, and "to contain is to divide" for
      Dedekind domains, which is more theory than the example needs). The steps replace
      both by the elementary argument in Z: every ideal of Z is mZ, and mZ containing pZ
      means m divides p, so m is +-1 or +-p. The non-primality of 8Z is kept, with the
      coprimality of the factors stated.
---

::: {.problem}
a. Define *prime ideal*, give an example of a nontrivial ideal in the ring $\ZZ$ that is not prime, and prove that it is not prime.

b. Define *maximal ideal*, give an example of a nontrivial maximal ideal in $\ZZ$ and prove that it is maximal.
:::

::: {.solution}

The question is the one recorded for the UGA Fall 2013 algebra qualifying exam. No retained
solution set covers it; the argument below is the card's own, restructured as numbered steps.

Throughout, $\ZZ$ is the ring of integers, and an ideal of $\ZZ$ is a subgroup under addition
closed under multiplication by every integer.

::: pf

::: {.pf-step #prime-def}

A proper ideal $\mathfrak{p}$ of a commutative ring $R$ is prime when $ab\in\mathfrak{p}$
implies $a\in\mathfrak{p}$ or $b\in\mathfrak{p}$, for all $a,b\in R$.

::: pf-proof

This is the definition; equivalently $R/\mathfrak{p}$ is an integral domain, which is not
needed below. Properness is part of the definition, since a ring with a unity is not an
integral domain when the ideal is all of $R$.

:::

:::

::: {.pf-step #eight-not-prime}

$8\ZZ$ is a nontrivial ideal of $\ZZ$ that is not prime.

::: pf-proof

$8\ZZ=\theset{8k : k\in\ZZ}$ is a subgroup of $(\ZZ,+)$ and is closed under multiplication by
integers, so it is an ideal; it is neither $\theset{0}$ nor $\ZZ$, hence nontrivial. Now
$2\cdot4=8\in8\ZZ$, while $2\notin8\ZZ$ and $4\notin8\ZZ$ because $8$ divides neither $2$ nor
$4$. So the prime condition fails with $a=2$, $b=4$.

:::

:::

::: {.pf-step #maximal-def}

A proper ideal $\mathfrak{m}$ of a ring $R$ is maximal when the only ideals $I$ of $R$ with
$\mathfrak{m}\subseteq I\subseteq R$ are $I=\mathfrak{m}$ and $I=R$.

::: pf-proof

This is the definition of a maximal element of the set of proper ideals under inclusion.

:::

:::

::: {.pf-step #ideals-are-principal}

Every ideal of $\ZZ$ is $m\ZZ=\theset{mk : k\in\ZZ}$ for some integer $m\ge0$.

::: pf-proof

Let $I$ be an ideal of $\ZZ$. If $I=\theset{0}$ take $m=0$. Otherwise $I$ contains a nonzero
element, hence a positive one (negate a negative element, using closure under subtraction),
and we may take $m$ to be the least positive element of $I$. Then $m\ZZ\subseteq I$ since $I$
is closed under multiplication by integers. Conversely, for $n\in I$ write
$n=qm+r$ with $0\le r<m$; then $r=n-qm\in I$, and $0\le r<m$ with $m$ least positive forces
$r=0$, so $n=qm\in m\ZZ$ and $I=m\ZZ$.

:::

:::

::: {.pf-step #pz-maximal}

For a prime $p$, $p\ZZ$ is a nontrivial maximal ideal of $\ZZ$.

::: pf-proof

$p\ZZ$ is an ideal by the same check as in step [](#eight-not-prime){.pf-ref}, and it is
neither $\theset{0}$ nor $\ZZ$. Let $I$ be an ideal with $p\ZZ\subseteq I\subseteq\ZZ$. By
step [](#ideals-are-principal){.pf-ref} $I=m\ZZ$ and $p\ZZ\subseteq m\ZZ$ for some $m\ge0$,
which means $m$ divides $p$. As $p$ is prime, $m\in\theset{1,p}$: $m=1$ gives $I=\ZZ$ and
$m=p$ gives $I=p\ZZ$. These are the two alternatives required by step
[](#maximal-def){.pf-ref}, so $p\ZZ$ is maximal.

:::

:::

:::

:::
