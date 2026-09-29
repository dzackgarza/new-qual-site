---
schema: qual/card@1
id: P-BKF14-9B
kind: problem
title: Number of roots of $x^{100000}-1$ in $\mathbb F_{65537}$
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-24
  note: >-
    Independently checked the retained Fall 2014 solution packet: the
    multiplicative group has order 2^16 and the exponent 100000 has 2-adic
    part 2^5.
- event: solution-written
  by: chatgpt
  date: 2026-09-24
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-24
  note: >-
    Checked the cyclic-group root count gcd(100000,65536)=32.
---

::: {.problem}
How many roots does the polynomial $x ^ { 1 0 0 0 0 0 } { - 1 }$ have in the finite field $\mathbb { F } _ { 6 5 5 3 7 } ?$ $( 6 5 5 3 7 = 2 ^ { 1 6 } + 1$ is a prime.)
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

Every root lies in the cyclic group
$$
\FF_{65537}^{\times},
$$
which has order
$$
65537-1=65536=2^{16}.
$$

::: pf-proof

If $x^{100000}=1$, then $x\ne0$, so every root belongs to the
multiplicative group of the field. The multiplicative group of a
finite field is cyclic, and here its order is the number of nonzero
field elements,
$$
65536=2^{16}.
$$

:::

:::

::: {.pf-step #s2}

In a cyclic group of order $N$, the equation
$$
x^m=1
$$
has exactly
$$
\gcd(m,N)
$$
solutions.

::: pf-proof

Let $\gamma$ generate the group. Every element has the form
$x=\gamma^k$ for a unique residue class $k$ modulo $N$. Then
$$
x^m=1
\iff
\gamma^{mk}=1
\iff
N\mid mk.
$$
Writing $d=\gcd(m,N)$, this is equivalent to
$$
\frac Nd\mid k.
$$
Modulo $N$, there are exactly $d$ such residue classes.

:::

:::

::: {.pf-step #s3}

One has
$$
\gcd(100000,65536)=32.
$$

::: pf-proof

Factor
$$
100000=10^5=2^5\,5^5
$$
and
$$
65536=2^{16}.
$$
Their greatest common divisor is therefore $2^5=32$.

:::

:::

::: {.pf-step #s4}

The polynomial has exactly
$$
\boxed{32}
$$
roots in $\FF_{65537}$.

::: pf-proof

Apply step [](#s2){.pf-ref} to the cyclic group in step [](#s1){.pf-ref} with
$$
m=100000,\qquad N=65536.
$$
Step [](#s3){.pf-ref} gives the number of solutions as $32$.

:::

:::

::: pf-qed

Step [](#s4){.pf-ref} is the requested root count.

:::

:::

:::
