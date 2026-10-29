---
schema: qual/card@1
id: P-GREPT-55
kind: problem
title: "Greatest negative $m+n$ with $7m+12n=22$"
classification:
  areas: [algebra]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: "Transcribed from Question 55 of the Practice Test (Chapter 9) in assets/attachments/extracted/Cracking_the_GRE_Mathematics_Subject.md (Mistral OCR)."
---

::: {.problem}
Let $A$ be the set of all ordered pairs of integers $(m, n)$ such that $7m + 12n = 22$. What is the greatest negative number in the set $B = \{m + n : (m, n) \in A\}$?

(A) $-5$
(B) $-4$
(C) $-3$
(D) $-2$
(E) $-1$
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

Every integer solution satisfies
$$
n\equiv3\pmod7.
$$


::: pf-proof

Reducing
$$
7m+12n=22
$$
modulo $7$ gives
$$
5n\equiv1\pmod7.
$$
Since $5^{-1}\equiv3\pmod7$, multiplication by $3$ gives
$n\equiv3\pmod7$.

:::

:::

::: {.pf-step #s1-2}

All integer solutions are
$$
n=3+7k,
\qquad
m=-2-12k,
\qquad k\in\ZZ.
$$


::: pf-proof

By step [](#s1-1){.pf-ref}, write $n=3+7k$. Substitution gives
$$
7m+12(3+7k)=22,
$$
hence $7m=-14-84k$ and $m=-2-12k$. Conversely, these formulas satisfy the
original equation for every integer $k$.

:::

:::

::: pf-step

Consequently,
$$
B=\{1-5k:k\in\ZZ\}.
$$


::: pf-proof

For the solutions in step [](#s1-2){.pf-ref},
$$
m+n=(-2-12k)+(3+7k)=1-5k.
$$
Every integer solution occurs there, so these are exactly the elements of
$B$.

:::

:::

::: {.pf-step #s1-4}

The greatest negative element of $B$ is
$$
\boxed{-4},
$$
so the answer is (B).


::: pf-proof

The value $1-5k$ is negative exactly when $k\ge1$. Among those integers it is
largest when $k=1$, yielding $1-5=-4$.

:::

:::

::: pf-qed

Step [](#s1-4){.pf-ref} gives the requested greatest negative value.

:::

:::

:::
