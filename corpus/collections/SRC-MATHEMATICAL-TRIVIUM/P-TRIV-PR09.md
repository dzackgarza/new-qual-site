---
schema: qual/card@1
id: P-TRIV-PR09
kind: problem
title: Meeting problem with a ten-minute wait
classification:
  areas: [prelim]
  topics:
  - Geometric Probability
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Probability, Problem 9, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md.
---

::: {.problem}
Two persons agreed to meet at some place between 2 and 3 o’clock.
Whoever arrives first, he waits 10 minutes, then leaves.
What is the probability to fail the meeting?
Assume that anyone can arrive at any time within the given interval.
:::

::: {.solution}

Measure arrival times $X,Y$ in minutes after 2:00, and assume they are independent and uniform on $[0,60]$.

::: pf

::: {.pf-step #s1-1}

The two people meet exactly when
$$
\abs{X-Y}\leq10.
$$


::: pf-proof

The earlier arrival waits for ten minutes. Thus a meeting occurs precisely when the later arrival is no more than ten minutes after the earlier one.

:::

:::

::: {.pf-step #s1-2}

The sample space is the square
$$
[0,60]^2
$$
of area $3600$.


::: pf-proof

Independence and uniformity make $(X,Y)$ uniformly distributed on this square, so probabilities are ratios of planar areas.

:::

:::

::: {.pf-step #s1-3}

Failure occurs in the two triangles
$$
Y>X+10
\qquad\text{or}\qquad
X>Y+10.
$$
Each triangle has legs of length $50$ and area $1250$.


::: pf-proof

By step [](#s1-1){.pf-ref}, failure is $\abs{X-Y}>10$. The two components lie above $Y=X+10$ and below $Y=X-10$. Each is a right triangle with vertices separated by $60-10=50$ along the two coordinate directions, hence has area $50^2/2=1250$.

:::

:::

::: {.pf-step #s1-4}

Therefore
$$
\boxed{P(\text{fail})=\frac{2\cdot1250}{3600}=\frac{25}{36}}.
$$


::: pf-proof

Divide the total failure area $2500$ from step [](#s1-3){.pf-ref} by the sample-space area $3600$ from step [](#s1-2){.pf-ref} and reduce the fraction.

:::

:::

::: pf-qed

Step [](#s1-4){.pf-ref} gives the requested probability of failing to meet.

:::

:::

:::
