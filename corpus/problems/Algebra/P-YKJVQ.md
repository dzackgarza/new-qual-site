---
schema: qual/card@1
id: P-YKJVQ
kind: problem
title: $\langle 2,x\rangle$ is not principal in $\ZZ[x]$
classification:
  areas:
  - algebra
  topics:
  - Ideals
  - Principal Ideal Domains
  - Polynomials
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-16
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
---

::: {.problem}
- Show that \( \gens{ 2, x }\normal \ZZ[x]  \) is not a principal ideal.
:::

::: {.solution}
Let
\[
I=(2,x)\subset\mathbb Z[x].
\]
Suppose $I=(f)$ were principal. Since $2\in(f)$, the polynomial $f$ divides the constant polynomial $2$. Because $\mathbb Z[x]$ is a domain,
\[
\deg f=0,
\]
so $f$ is an integer divisor of $2$. Up to a unit,
\[
f=1\quad\text{or}\quad f=2.
\]

If $f=2$, then $(f)=(2)$ does not contain $x$. If $f=1$, then $(f)=\mathbb Z[x]$, but $I$ is proper: reduction modulo $2$ followed by evaluation at $x=0$ gives a homomorphism
\[
\mathbb Z[x]\to\mathbb F_2
\]
whose kernel contains $(2,x)$ but not $1$.

Both possibilities are impossible. Therefore
\[
\boxed{(2,x)\text{ is not principal in }\mathbb Z[x]}.
\]
:::
