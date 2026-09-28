---
schema: qual/card@1
id: P-BERK96S-08
kind: problem
title: Rightmost decimal digit of $17^{17^{17}}$
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-written
  by: chatgpt
  date: 2026-09-23
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-23
  note: >-
    Verified the exponent modulo 4 and the resulting final-digit congruence
    modulo 10.
---

::: {.problem}
Determine the rightmost decimal digit of
\[
17^{17^{17}}.
\]
:::

::: {.solution}
Set
$$
N\coloneqq 17^{17}.
$$

<1>1. One has
$$
N\equiv1\pmod4.
$$

::: {.proof}
Since
$$
17\equiv1\pmod4,
$$
raising both sides to the seventeenth power gives
$$
17^{17}\equiv1^{17}\equiv1\pmod4.
$$
:::

<1>2. One has
$$
17^N\equiv7\pmod{10}.
$$

::: {.proof}
Modulo $10$,
$$
17^N\equiv7^N.
$$
Also
$$
7^4=2401\equiv1\pmod{10}.
$$
By step <1>1, there is an integer $q$ such that $N=4q+1$. Therefore
$$
7^N
=
7(7^4)^q
\equiv
7\pmod{10}.
$$
:::

<1>3. The rightmost decimal digit of $17^{17^{17}}$ is
$$
\boxed{7}.
$$

::: {.proof}
The number in the problem is $17^N$, and step <1>2 says that it is congruent
to $7$ modulo $10$.
:::

<1>4. Q.E.D.

::: {.proof}
Step <1>3 gives the requested digit.
:::
:::
