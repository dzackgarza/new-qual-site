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

::: pf

::: {.pf-step #s1-1}

The set $A-B$ consists of the prime numbers that are not odd.


::: pf-proof

By definition of relative complement,
$$
A-B=\{x:x\in A\text{ and }x\notin B\}.
$$
Here $A$ is the set of primes and $B$ is the set of odd integers, so the elements of $A-B$ are exactly the primes that are not odd.

:::

:::

::: {.pf-step #s1-2}

The only prime number that is not odd is $2$.


::: pf-proof

Every integer greater than $2$ that is even is divisible by $2$ and hence is composite. The integer $2$ itself is prime and even.

:::

:::

::: {.pf-step #s1-3}

Therefore
$$
\boxed{A-B=\{2\}},
$$
so the answer is (D).


::: pf-proof

Combine steps [](#s1-1){.pf-ref} and [](#s1-2){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s1-3){.pf-ref} gives the required relative complement.

:::

:::

:::
