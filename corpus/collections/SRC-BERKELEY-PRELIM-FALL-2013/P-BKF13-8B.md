---
schema: qual/card@1
id: P-BKF13-8B
kind: problem
title: $561$ is a Carmichael number
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
    Independently checked the retained Fall 2013 solution packet: Fermat's
    theorem modulo 3, 11, and 17 gives the required congruence modulo their
    squarefree product 561.
- event: solution-written
  by: chatgpt
  date: 2026-09-24
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-24
  note: >-
    Checked the factorization 561=3*11*17, the divisibilities
    2,10,16 | 560, and the final coprime-moduli argument.
---

::: {.problem}
Prove that if $n$ is coprime to $N=561$ then $n^{N-1}\equiv1\bmod N$.
:::

::: {.solution}
Let $N=561$.

::: pf

::: {.pf-step #s1}

One has
$$
N=3\cdot11\cdot17
\qquad\text{and}\qquad
N-1=560.
$$

::: pf-proof

Direct multiplication gives $3\cdot11\cdot17=561$, and subtracting $1$
gives $560$.

:::

:::

::: {.pf-step #s2}

If $\gcd(n,561)=1$, then
$$
n^{560}\equiv1\pmod3.
$$

::: pf-proof

The hypothesis implies $3\nmid n$. By Fermat's little theorem,
$n^2\equiv1\pmod3$. Since $560=280\cdot2$,
$$
n^{560}=(n^2)^{280}\equiv1\pmod3.
$$

:::

:::

::: {.pf-step #s3}

If $\gcd(n,561)=1$, then
$$
n^{560}\equiv1\pmod{11}.
$$

::: pf-proof

The hypothesis implies $11\nmid n$. By Fermat's little theorem,
$n^{10}\equiv1\pmod{11}$. Since $560=56\cdot10$,
$$
n^{560}=(n^{10})^{56}\equiv1\pmod{11}.
$$

:::

:::

::: {.pf-step #s4}

If $\gcd(n,561)=1$, then
$$
n^{560}\equiv1\pmod{17}.
$$

::: pf-proof

The hypothesis implies $17\nmid n$. By Fermat's little theorem,
$n^{16}\equiv1\pmod{17}$. Since $560=35\cdot16$,
$$
n^{560}=(n^{16})^{35}\equiv1\pmod{17}.
$$

:::

:::

::: {.pf-step #s5}

Therefore
$$
\boxed{n^{N-1}\equiv1\pmod N}.
$$

::: pf-proof

By steps [](#s2){.pf-ref}, [](#s3){.pf-ref} and [](#s4){.pf-ref}, each of the pairwise coprime integers $3$, $11$,
and $17$ divides $n^{560}-1$. Hence their product $561$ divides
$n^{560}-1$. Using step [](#s1){.pf-ref}, this is
$$
n^{N-1}\equiv1\pmod N.
$$

:::

:::

::: pf-qed

Step [](#s5){.pf-ref} is the required congruence.

:::

:::

:::
