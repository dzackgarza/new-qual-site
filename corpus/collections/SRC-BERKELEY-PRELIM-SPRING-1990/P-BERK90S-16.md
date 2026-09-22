---
schema: qual/card@1
id: P-BERK90S-16
kind: problem
title: Greatest common divisor of all integers $n^{13}-n$
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
- event: source-checked
  by: chatgpt
  date: 2026-09-22
  note: Compared the exponent 13, subtraction of n, and the range over all integers with Problem 16 in the retained MinerU Flash extraction of Spring90.pdf.
- event: solution-written
  by: chatgpt
  date: 2026-09-22
  note: Used Fermat's little theorem for the primes 2, 3, 5, 7, and 13 and an explicit integer combination of the values at 2 and 3 to determine the gcd.
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-22
  note: Checked the prime product, each exponent divisor, the two integer values and their displayed combination, and applicability to negative integers and zero.
---

::: {.problem}
Determine the greatest common divisor of the set
$$
\{n^{13}-n:n\in\ZZ\}.
$$
:::

::: {.hint}
For a prime $p$ with $p-1$ dividing $12$, apply Fermat's little
theorem to $n^{13}-n$. For an upper bound on the common
divisors, use the values at $n=2$ and $n=3$.
:::

::: {.solution}
For each $n\in\ZZ$, put $a_n\coloneqq n^{13}-n$.

<1>1. The integer $2730$ divides $a_n$ for every $n\in\ZZ$.

::: {.proof}
Let $p\in\{2,3,5,7,13\}$ and $n\in\ZZ$.
Each such $p$ is prime and $p-1$ divides $12$.
If $p\mid n$, then $p\mid a_n$.
If $p\nmid n$, [[FT-RVIGS|Fermat's little theorem]] gives
$$
n^{12}=\bigl(n^{p-1}\bigr)^{12/(p-1)}\equiv1\pmod p,
$$
so $a_n=n(n^{12}-1)$ is again divisible by $p$.
The listed primes are pairwise coprime, so their product
$$
2\cdot3\cdot5\cdot7\cdot13=2730
$$
divides every $a_n$.
:::

<1>2. The greatest common divisor is
$$
\gcd\{a_n:n\in\ZZ\}=\boxed{2730}.
$$

::: {.proof}
The values $a_2=8190$ and $a_3=1594320$ satisfy
$$
195a_2-a_3
=195\cdot8190-1594320
=2730.
$$
Every common divisor of all the $a_n$ divides this integer
combination, hence divides $2730$. Conversely, step <1>1
shows that $2730$ is itself a positive common divisor.
It is therefore the greatest common divisor.
:::

<1>3. Q.E.D.

::: {.proof}
Step <1>2 determines the gcd of the given set.
:::
:::
