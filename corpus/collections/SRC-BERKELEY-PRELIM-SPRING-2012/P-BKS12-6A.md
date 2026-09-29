---
schema: qual/card@1
id: P-BKS12-6A
kind: problem
title: Mersenne numbers $2^p-1$ are base-2 pseudoprimes
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-25
  note: Compared the authored statement with page 2 of the retained Spring 2012 solution PDF and independently reviewed the Fermat-congruence argument.
- event: solution-written
  by: chatgpt
  date: 2026-09-25
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-25
  note: Independently checked divisibility of 2^p-2 by p and the resulting exponent congruence modulo 2^p-1.
---

::: {.problem}
A positive integer m is called a pseudoprime to the base 2 if m divides $2 ^ { m - 1 } - 1$ . Show $2 ^ { p } - 1$ is a pseudoprime to the base 2 if $p$ is prime.
:::

::: {.solution}
Let
$$
M\coloneqq2^p-1.
$$

::: pf

::: {.pf-step #p-divides-m-minus-one}
The integer $p$ divides $M-1$.

::: pf-proof
Since $p$ is prime, Fermat's little theorem gives
$$
2^p\equiv2\pmod p.
$$
Hence
$$
p\mid(2^p-2).
$$
But
$$
M-1
=
2^p-2.
$$
:::

:::

::: {.pf-step #k-exists}
There is an integer $k\geq1$ such that
$$
M-1=pk.
$$

::: pf-proof
This is exactly the divisibility statement in step [](#p-divides-m-minus-one){.pf-ref}.
:::

:::

::: {.pf-step #two-p-mod-m}
One has
$$
2^p\equiv1\pmod M.
$$

::: pf-proof
By definition,
$$
M=2^p-1,
$$
so
$$
2^p-1\equiv0\pmod M.
$$
:::

:::

::: {.pf-step #fermat-condition}
One has
$$
2^{M-1}\equiv1\pmod M.
$$

::: pf-proof
By step [](#k-exists){.pf-ref},
$$
2^{M-1}
=
2^{pk}
=
(2^p)^k.
$$
Applying step [](#two-p-mod-m){.pf-ref} gives
$$
(2^p)^k
\equiv
1^k
=
1
\pmod M.
$$
:::

:::

::: {.pf-step #pseudoprime-conclusion}
Therefore
$$
\boxed{2^p-1}
$$
is a pseudoprime to base $2$ in the sense of the stated definition.

::: pf-proof
Step [](#fermat-condition){.pf-ref} says exactly that
$$
M\mid 2^{M-1}-1.
$$
:::

:::

::: pf-qed
Step [](#pseudoprime-conclusion){.pf-ref} is the required conclusion.
:::

:::

:::
