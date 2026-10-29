---
schema: qual/card@1
id: P-F2YIN
kind: problem
title: Factorisation in $R[x_1,\ldots,x_n]$
classification:
  areas:
  - algebra
  topics:
  - Factorization
  - Polynomials
  - Irreducibility Criteria
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
- event: solution-written
  by: Claude Opus 5.5
  date: 2026-10-29
  note: Converted the prose solution to a STYLE-08 structured proof.
---

::: {.problem}
Talk about factorisation and primes in a polynomial ring.
What is irreducibility?
For what rings $R$ is it true that $R[x_1, \ldots , x_n]$ is a unique factorisation domain?
What is wrong with unique factorisation if we don't have a domain?
Now, PIDs are Noetherian, but are there UFDs which are not?
:::

::: {.solution}
Let $R$ be an integral domain.

::: pf

::: pf-step
Recall that a nonzero nonunit $a\in R$ is [[D-TO3IY|irreducible]] if $a=bc$ implies $b\in R^\times$ or $c\in R^\times$, and [[D-AWSKI|prime]] if $a\mid bc$ implies $a\mid b$ or $a\mid c$.
Every prime element is irreducible, and in a UFD every irreducible element is prime.

::: pf-proof
If $a$ is prime and $a=bc$, then $a\mid b$ or $a\mid c$; say $b=ad$, so $a=adc$ and $dc=1$ since $R$ is a domain, so $c$ is a unit.
In a UFD, if an irreducible $a$ divides $bc$, then by uniqueness of factorization $a$ is associate to an irreducible factor of $b$ or of $c$.
:::

:::

::: pf-step
$R[x_1,\ldots,x_n]$ is a UFD if and only if $R$ is a UFD.

::: pf-proof
If $R$ is a UFD, then $R[x]$ is a UFD by Gauss's theorem, and induction on $n$ gives the claim for $R[x_1,\ldots,x_n]$.
Conversely, suppose $R[x_1,\ldots,x_n]$ is a UFD and let $a\in R$ be a nonzero nonunit.
The units of the polynomial ring are the units of $R$, and degrees add in a product over a domain, so every factorization of the constant $a$ has only constant factors.
Hence the unique factorization of $a$ in the polynomial ring is a unique factorization in $R$.
:::

:::

::: pf-step
Without a domain, factorizations into nonunits need not have bounded length.

::: pf-proof
A UFD is by definition a domain.
In $\ZZ/6\ZZ$ the idempotent nonunit $3$ satisfies $3=3\cdot3=3^n$ for every $n\ge1$.
:::

:::

::: pf-step
$k[x_1,x_2,x_3,\ldots]$ is a UFD that is not Noetherian.

::: pf-proof

::: {.pf-step #ufd}
$k[x_1,x_2,\ldots]$ is a UFD.

::: pf-proof
Every nonzero nonunit $f$ lies in some $A_m=k[x_1,\ldots,x_m]$, which is a UFD, and factors there into irreducibles.
Each such irreducible $p\in A_m$ is prime in $A_m$, and $k[x_1,x_2,\ldots]/(p)\cong(A_m/(p))[x_{m+1},x_{m+2},\ldots]$ is a domain, so $p$ is prime in the full ring.
A factorization into primes is unique up to order and units.
:::

:::

::: pf-qed
By step [](#ufd){.pf-ref} the ring is a UFD, and the chain $(x_1)\subsetneq(x_1,x_2)\subsetneq(x_1,x_2,x_3)\subsetneq\cdots$ does not stabilize, since $x_{n+1}\notin(x_1,\ldots,x_n)$.
:::

:::

:::

:::

:::
