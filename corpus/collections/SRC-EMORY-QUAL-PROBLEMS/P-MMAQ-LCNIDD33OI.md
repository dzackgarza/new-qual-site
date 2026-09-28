---
schema: qual/card@1
id: P-MMAQ-LCNIDD33OI
kind: problem
title: $R/I$ is a field for maximal $I$; nonzero primes in a PID are maximal; $R/(p)$
  is a field for prime $p$
classification:
  areas:
  - algebra
  topics:
  - Rings
  - Ideals
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-10
  note: "Visually compared all three assertions and the unital, domain, and nonzero-prime hypotheses with Rings 3 on PDF page 2."
- event: solution-written
  by: chatgpt
  date: 2026-09-10
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-10
  note: "Checked inversion modulo a maximal ideal, cancellation for the nonzero prime generator, and properness and primality of the prime-element ideal."
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: "Compared with Rings (3) of Arango-Piñeros, Some quals problems; merged the duplicate P-EMAR3, whose solution repeats this argument."
---

::: {.problem}
$R$ is a commutative ring with 1. Prove that if $I$ is a maximal ideal in $R$, then $R/I$ is a field.
Prove that if $R$ is a PID, then every nonzero prime ideal in $R$ is maximal.
Conclude that if $R$ is a PID and $p\in R$ is prime, then $R/(p)$ is a field.
:::

::: {.solution}
<1>1. If $I$ is maximal in a commutative unital ring $R$,
then $R/I$ is a field.

::: {.proof}
A maximal ideal is proper, so $1+I\ne0+I$.
For a nonzero coset $a+I$, one has $a\notin I$.
The ideal $I+(a)$ strictly contains $I$, and hence
equals $R$. Write $1=i+ba$ with $i\in I$ and
$b\in R$. Passing to the quotient gives
$(b+I)(a+I)=1+I$. Thus every nonzero element of
the nonzero commutative quotient is invertible.
:::

<1>2. Every nonzero prime ideal $P$ of a PID is maximal.

::: {.proof}
Write $P=(a)$ with $a\ne0$. Let $J$ be an ideal
containing $P$, and write $J=(b)$. The containment
gives $a=bc$ for some $c\in R$.
Since $bc\in P$ and $P$ is prime, either $b\in P$
or $c\in P$. In the first case $J=(b)\subseteq P$,
so $J=P$. In the second case write $c=ad$.
Then $a=bad$, and cancellation of the nonzero $a$
in the domain gives $1=bd$. Thus $b$ is a unit
and $J=R$. There is no ideal strictly between
the proper ideal $P$ and $R$, proving maximality.
:::

<1>3. If $p$ is a prime element of a PID, then $R/(p)$ is a field.

::: {.proof}
By definition a prime element is nonzero and not
a unit, and $p\mid ab$ implies $p\mid a$ or
$p\mid b$. These assertions say respectively that
$(p)$ is nonzero, proper, and a prime ideal.
Step <1>2 makes it maximal, and step <1>1 makes
its quotient a field.
:::
:::
