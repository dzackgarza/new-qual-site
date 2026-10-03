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
<1>1. Every integer solution satisfies
$$
n\equiv3\pmod7.
$$

::: {.proof}
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

<1>2. All integer solutions are
$$
n=3+7k,
\qquad
m=-2-12k,
\qquad k\in\ZZ.
$$

::: {.proof}
By step <1>1, write $n=3+7k$. Substitution gives
$$
7m+12(3+7k)=22,
$$
hence $7m=-14-84k$ and $m=-2-12k$. Conversely, these formulas satisfy the
original equation for every integer $k$.
:::

<1>3. Consequently,
$$
B=\{1-5k:k\in\ZZ\}.
$$

::: {.proof}
For the solutions in step <1>2,
$$
m+n=(-2-12k)+(3+7k)=1-5k.
$$
Every integer solution occurs there, so these are exactly the elements of
$B$.
:::

<1>4. The greatest negative element of $B$ is
$$
\boxed{-4},
$$
so the answer is (B).

::: {.proof}
The value $1-5k$ is negative exactly when $k\ge1$. Among those integers it is
largest when $k=1$, yielding $1-5=-4$.
:::

<1>5. Q.E.D.

::: {.proof}
Step <1>4 gives the requested greatest negative value.
:::
:::
