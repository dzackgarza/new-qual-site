---
schema: qual/card@1
id: P-CALCPT3-40
kind: problem
title: "Probability that $x\\ge yz$ for independent uniform $x,y,z$ on $[0,1]$"
classification:
  areas: [prelim]
  topics: [Probability, Integrals]
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-10-30
  note: "Transcribed from Question 40 of assets/attachments/calculus_practice_test3.pdf and checked against its MinerU Flash extraction; they agree."
- event: solution-reviewed
  by: claude
  date: 2026-11-19
  note: >-
    Read against the Lamport standard and checked by direct computation. With x, y, z independent
    uniform on [0,1] the triple is uniform on the cube, so the probability is a volume. Step #fixed:
    for fixed y, z in [0,1] the set of x with x < yz has measure yz, the interval [0, yz) lying
    inside [0,1]. Step #complement: Fubini gives int_0^1 int_0^1 yz dy dz = (1/2)(1/2) = 1/4. Last
    step: the complement has probability 3/4, so the answer is choice (A). The value was also
    checked by simulation of 200000 triples, seed 7, which gave 0.7493, consistent with 3/4. Not claimed: independence of any
    other function of the three variables, which the argument does not need.
---

::: {.problem}
If $x$, $y$, and $z$ are selected independently and at random from the interval $[0,1]$, then the probability that $x\ge yz$ is

(A) $\frac34$
(B) $\frac23$
(C) $\frac12$
(D) $\frac13$
(E) $\frac14$
:::

::: {.solution}
Let $x,y,z$ be independent and uniform on $[0,1]$, so $(x,y,z)$ is uniform on the unit cube and probabilities are volumes.

::: pf

::: {.pf-step #fixed}
For fixed $y,z\in[0,1]$, the probability over $x$ that $x<yz$ is $yz$.

::: pf-proof
$yz\in[0,1]$, and $x$ is uniform on $[0,1]$.
:::

:::

::: {.pf-step #complement}
The probability that $x<yz$ is $\frac14$.

::: pf-proof
By step [](#fixed){.pf-ref} and Fubini's theorem, it equals $\int_0^1\int_0^1yz\,dy\,dz=\frac12\cdot\frac12=\frac14$.
:::

:::

::: pf-step
The probability that $x\ge yz$ is $\boxed{\frac34}$, choice (A).

::: pf-proof
It is the complement of the event in step [](#complement){.pf-ref}, so it is $1-\frac14=\frac34$; this value differs from each of (B) through (E).
:::

:::

:::

:::
