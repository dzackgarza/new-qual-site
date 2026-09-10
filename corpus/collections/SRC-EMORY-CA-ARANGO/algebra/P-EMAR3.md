---
schema: qual/card@1
id: P-EMAR3
kind: problem
title: "Maximal ideals, PID prime ideals, and quotient fields"
classification:
  areas:
  - algebra
  topics:
  - Maximal Ideals
  - Principal Ideal Domains
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-10
  note: "Compared all three assertions with Rings 3 on the source's second page, retaining the identity and nonzero-prime hypotheses."
- event: solution-written
  by: chatgpt
  date: 2026-09-10
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-10
  note: "Checked the inverse in the quotient, both primality cases for an overideal in a PID, the nonzero cancellation, and the prime-element conclusion."
---

::: problem
$R$ is a commutative ring with 1. Prove that if $I$ is a maximal ideal in $R$, then $R/I$ is a field.
Prove that if $R$ is a PID, then every nonzero prime ideal in $R$ is maximal.
Conclude that if $R$ is a PID and $p \in R$ is prime, then $R/(p)$ is a field.
:::

::: solution
<1>1. A maximal ideal $I$ has a field as its quotient.

::: proof
The ideal is proper, so the commutative quotient
$R/I$ has $1+I\ne0+I$. Let $a+I$ be nonzero.
Then $a\notin I$, and $I+(a)$ strictly contains
$I$. Maximality implies $I+(a)=R$. In particular
$1=i+ba$ for some $i\in I$ and $b\in R$.
Passing to cosets gives $(b+I)(a+I)=1+I$.
Thus each nonzero element has an inverse, which
proves that $R/I$ is a field.
:::

<1>2. A nonzero prime ideal $P$ in a PID is maximal.

::: proof
Choose $a\ne0$ with $P=(a)$. Let $J$ be an
ideal containing $P$, and write $J=(b)$.
Since $a\in(b)$, there is $c\in R$ with $a=bc$.
Primality of $P$ gives $b\in P$ or $c\in P$.
If $b\in P$, then $J=(b)\subseteq P$, so $J=P$.
If $c\in P$, write $c=ad$. The equality $a=bad$
and cancellation of $a\ne0$ in the domain imply
$1=bd$. Hence $b$ is a unit and $J=R$.
These cases exhaust all overideals. Since $P$
is proper, this proves maximality.
:::

<1>3. For a prime element $p$ of a PID, $R/(p)$ is a field.

::: proof
A prime element is nonzero and not a unit, so
$(p)$ is a nonzero proper ideal. If $ab\in(p)$,
then $p\mid ab$; the defining prime-element
property gives $p\mid a$ or $p\mid b$, so
$a\in(p)$ or $b\in(p)$. Thus $(p)$ is prime.
Apply step <1>2 to make it maximal and then
step <1>1 to obtain the required field.
:::
:::
