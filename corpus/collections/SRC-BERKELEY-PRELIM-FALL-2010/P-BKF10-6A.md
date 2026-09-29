---
schema: qual/card@1
id: P-BKF10-6A
kind: problem
title: Distributivity of $\gcd$ over $\operatorname{lcm}$
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-12
  note: Checked against Problem 6A of the retained Berkeley Fall 2010 preliminary-exam solution packet f10solutions.pdf.
- event: solution-written
  by: chatgpt
  date: 2026-09-24
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-24
  note: >-
    Checked the prime-valuation formulas for gcd and lcm and the lattice
    identity min(A,max(B,C))=max(min(A,B),min(A,C)).
---

::: {.problem}
For nonzero integers $a,b,c$, show that
$$
\gcd\{a,\operatorname{lcm}\{b,c\}\}
=
\operatorname{lcm}\{\gcd\{a,b\},\gcd\{a,c\}\}.
$$
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

Fix a prime $p$ and put
$$
A=v_p(\abs{a}),
\qquad
B=v_p(\abs{b}),
\qquad
C=v_p(\abs{c}).
$$
Then
$$
v_p(\gcd(a,b))=\min(A,B)
$$
and
$$
v_p(\operatorname{lcm}(a,b))=\max(A,B).
$$

::: pf-proof

In the prime factorizations of positive integers, the greatest common
divisor takes the smaller exponent of each prime, while the least common
multiple takes the larger exponent. Replacing a nonzero integer by its
absolute value does not change either exponent.

:::

:::

::: {.pf-step #s2}

For all nonnegative integers $A,B,C$,
$$
\min(A,\max(B,C))
=\max(\min(A,B),\min(A,C)).
$$

::: pf-proof

If $A\le\max(B,C)$, then the left side is $A$. At least one of $B,C$ is
at least $A$, so one of $\min(A,B),\min(A,C)$ equals $A$, while the other
is at most $A$. Hence the right side is also $A$.

If $A>\max(B,C)$, then $A>B$ and $A>C$. The left side is
$\max(B,C)$, while the right side is
$$
\max(B,C)
=\max(\min(A,B),\min(A,C)).
$$
Thus the identity holds in both cases.

:::

:::

::: {.pf-step #s3}

For every prime $p$, the two integers in the required identity
have the same $p$-adic valuation.

::: pf-proof

Using step [](#s1){.pf-ref}, the valuation of the left-hand side is
$$
\min(A,\max(B,C)).
$$
The valuation of the right-hand side is
$$
\max(\min(A,B),\min(A,C)).
$$
These are equal by step [](#s2){.pf-ref}.

:::

:::

::: {.pf-step #s4}

Therefore
$$
\boxed{
\gcd\{a,\operatorname{lcm}\{b,c\}\}
=
\operatorname{lcm}\{\gcd\{a,b\},\gcd\{a,c\}\}
}.
$$

::: pf-proof

Both sides are positive integers. Step [](#s3){.pf-ref} shows that their prime
factorizations have the same exponent at every prime, so the fundamental
theorem of arithmetic implies that they are equal.

:::

:::

::: pf-qed

Step [](#s4){.pf-ref} is exactly the desired identity.

:::

:::

:::
