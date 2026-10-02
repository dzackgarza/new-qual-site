---
schema: qual/card@1
id: P-GRECH7-06
kind: problem
title: Relative complement of the odd integers in the primes
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Checked against Question 6 of the Chapter 7 review questions in assets/attachments/extracted/Chapter-7.md (Mistral OCR), compared with the same page in the Cracking the GRE Mathematics Subject Test book extraction.
---

::: {.problem}
Suppose $A$ is the set of all prime numbers, and $B$ is the set of all odd integers. Then the relative complement $A-B$ is equivalent to the set of

(A) $\{x\mid x\text{ is even}\}$
(B) $\{x\mid x\text{ is positive and odd}\}$
(C) $\{x\mid x\text{ is a composite integer}\}$
(D) $\{2\}$
(E) $\{0\}$
:::

::: {.solution}
<1>1. The set $A-B$ consists of the prime numbers that are not odd.

::: {.proof}
By definition of relative complement,
$$
A-B=\{x:x\in A\text{ and }x\notin B\}.
$$
Here $A$ is the set of primes and $B$ is the set of odd integers, so the elements of $A-B$ are exactly the primes that are not odd.
:::

<1>2. The only prime number that is not odd is $2$.

::: {.proof}
Every integer greater than $2$ that is even is divisible by $2$ and hence is composite. The integer $2$ itself is prime and even.
:::

<1>3. Therefore
$$
\boxed{A-B=\{2\}},
$$
so the answer is (D).

::: {.proof}
Combine steps <1>1 and <1>2.
:::

<1>4. Q.E.D.

::: {.proof}
Step <1>3 gives the required relative complement.
:::
:::
