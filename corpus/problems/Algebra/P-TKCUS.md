---
schema: qual/card@1
id: P-TKCUS
kind: problem
title: $x^{p^d}-x$ divides $x^{p^n}-x$ iff $d$ divides $n$
classification:
  areas:
  - algebra
  topics:
  - Finite Fields
  - Polynomials
  - Factorization
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-16
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
- event: statement-corrected
  by: claude-opus-5.5
  date: 2026-10-29
  note: 'The source reads "Show that $x^{p^d} - x \divides x^{p^n} - x \iff d \divides n$" and declares none of $p$, $d$, $n$ or the coefficient ring; the statement takes $p$ prime, $d,n$ positive integers, and polynomials in $\FF_p[x]$.'
---

::: {.problem}
Let $p$ be a prime and $d,n$ positive integers. Show that $x^{p^d} - x \divides x^{p^n} - x$ in $\FF_p[x]$ $\iff d \divides n$.
:::

::: {.solution}

::: pf

::: {.pf-step #power-divisibility}
For an integer $a>1$ and positive integers $A,B$, $a^A-1\divides a^B-1$ if and only if $A\divides B$; likewise $x^A-1\divides x^B-1$ in $F[x]$ for any field $F$ if and only if $A\divides B$.

::: pf-proof
Write $B=qA+r$ with $0\le r<A$. Then
$$
x^B-1=x^r\bigl(x^{qA}-1\bigr)+\bigl(x^r-1\bigr),
$$
and $x^A-1$ divides $x^{qA}-1$, so the remainder of $x^B-1$ on division by $x^A-1$ is $x^r-1$, which has degree less than $A$ and is zero exactly when $r=0$.
Substituting $x=a$ gives $a^B-1\equiv a^r-1\pmod{a^A-1}$ with $0\le a^r-1<a^A-1$, so the same conclusion holds for integers.
:::

:::

::: {.pf-step #cancel}
$x^{p^d}-x\divides x^{p^n}-x$ if and only if $x^{p^d-1}-1\divides x^{p^n-1}-1$.

::: pf-proof
$x^{p^m}-x=x\bigl(x^{p^m-1}-1\bigr)$, and the common factor $x$ cancels in the domain $\FF_p[x]$.
:::

:::

::: pf-step
$\boxed{x^{p^d}-x\divides x^{p^n}-x\iff d\divides n}$.

::: pf-proof
By step [](#cancel){.pf-ref} and the polynomial case of step [](#power-divisibility){.pf-ref}, the divisibility holds if and only if $p^d-1\divides p^n-1$, and by the integer case with $a=p$ this holds if and only if $d\divides n$.
:::

:::

:::

:::
