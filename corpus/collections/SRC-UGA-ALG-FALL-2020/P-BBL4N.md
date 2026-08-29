---
schema: qual/card@1
id: P-BBL4N
kind: problem
title: Elementary divisors, invariant factors, and minimal and characteristic polynomials
  of a given $\RR[x]$-module
classification:
  areas:
  - algebra
  topics:
  - Structure Theorem
  - Minimal and Characteristic Polynomials
  - Modules
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

::: problem
Let $A \in \Mat(n\times n, \RR)$ be arbitrary.
Make $\RR^n$ into an $\RR[x]\dash$module by letting $f(x).\vector{v} \da f(A)(\vector{v})$ for $f(\vector{v})\in \RR[x]$ and $\vector{v} \in \RR^n$.
Suppose that this induces the following direct sum decomposition:
\[
\RR^n \cong
{ \RR[x] \over \gens{ (x-1)^3 } }
\oplus
{ \RR[x] \over \gens{ (x^2+1)^2 } }
\oplus
{ \RR[x] \over \gens{ (x-1)(x^2-1)(x^2+1)^4 } }
\oplus
{ \RR[x] \over \gens{ (x+2)(x^2+1)^2 } }
.\]
a. Determine the elementary divisors and invariant factors of $A$.

b. Determine the minimal polynomial of $A$.

c. Determine the characteristic polynomial of $A$.
:::

::: {.solution}
<1>1. Factor the third summand: $(x-1)(x^2-1)(x^2+1)^4 = (x-1)^2(x+1)(x^2+1)^4$.
Proof: $x^2 - 1 = (x-1)(x+1)$.

<1>2. The elementary divisors (primary factors) are
$$(x-1)^3,\ (x-1)^2,\ (x+1),\ (x+2),\ (x^2+1)^2,\ (x^2+1)^2,\ (x^2+1)^4.$$
Proof: decompose each summand into primary components over $\RR$: $(x-1)^3$; $(x^2+1)^2$; $(x-1)^2$, $(x+1)$, $(x^2+1)^4$; $(x+2)$, $(x^2+1)^2$.

<1>3. The invariant factors are
$$d_1 = (x^2+1)^2,\quad d_2 = (x-1)^2(x^2+1)^2,\quad d_3 = (x-1)^3(x+1)(x+2)(x^2+1)^4.$$
Proof: group the elementary divisors by prime and multiply the highest power of each prime for the last invariant factor, the next-highest for the second, and so on; this gives $d_1 \mid d_2 \mid d_3$.

<1>4. The minimal polynomial is $d_3 = (x-1)^3(x+1)(x+2)(x^2+1)^4$.
Proof: the minimal polynomial is the largest invariant factor.

<1>5. The characteristic polynomial is $d_1 d_2 d_3 = (x-1)^5(x+1)(x+2)(x^2+1)^8$.
Proof: the characteristic polynomial is the product of all invariant factors; the $(x-1)$-powers contribute $2 + 3 = 5$, and the $(x^2+1)$-powers contribute $2 + 2 + 4 = 8$.

<1>6. Dimension check: $\deg d_1 + \deg d_2 + \deg d_3 = 4 + 6 + 13 = 23 = n$.
Proof: $\deg d_1 = 4$, $\deg d_2 = 2 + 4 = 6$, $\deg d_3 = 3 + 1 + 1 + 8 = 13$.

<1>7. Q.E.D.
Proof: <1>2 (a), <1>3 (a), <1>4 (b), and <1>5 (c).
:::
