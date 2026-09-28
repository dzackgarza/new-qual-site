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
<1>1. Every root lies in the cyclic group
$$
\FF_{65537}^{\times},
$$
which has order
$$
65537-1=65536=2^{16}.
$$

::: {.proof}
If $x^{100000}=1$, then $x\ne0$, so every root belongs to the
multiplicative group of the field. The multiplicative group of a
finite field is cyclic, and here its order is the number of nonzero
field elements,
$$
65536=2^{16}.
$$
:::

<1>2. In a cyclic group of order $N$, the equation
$$
x^m=1
$$
has exactly
$$
\gcd(m,N)
$$
solutions.

::: {.proof}
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

<1>3. One has
$$
\gcd(100000,65536)=32.
$$

::: {.proof}
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

<1>4. The polynomial has exactly
$$
\boxed{32}
$$
roots in $\FF_{65537}$.

::: {.proof}
Apply step <1>2 to the cyclic group in step <1>1 with
$$
m=100000,\qquad N=65536.
$$
Step <1>3 gives the number of solutions as $32$.
:::

<1>5. Q.E.D.

::: {.proof}
Step <1>4 is the requested root count.
:::
:::
