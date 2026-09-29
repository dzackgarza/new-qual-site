---
schema: qual/card@1
id: P-BERK97S-15
kind: problem
title: Two idempotents with invertible $I-(P+Q)$ have equal rank
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
---

::: {.problem}
Let $P,Q$ be $n\times n$ matrices satisfying
\[
P^2=P,
\qquad
Q^2=Q,
\]
and suppose
\[
I-(P+Q)
\]
is invertible. Prove that $P$ and $Q$ have the same rank.
:::

::: {.solution}
Put
$$
A\coloneqq I-(P+Q).
$$

::: pf

::: {.pf-step #s1}

The matrices $A,P,Q$ satisfy
$$
AP=QA.
$$

::: pf-proof

Using $P^2=P$ gives
$$
AP
=(I-P-Q)P
=P-P^2-QP
=-QP.
$$
Using $Q^2=Q$ gives
$$
QA
=Q(I-P-Q)
=Q-QP-Q^2
=-QP.
$$
Hence $AP=QA$.

:::

:::

::: {.pf-step #s2}

The matrices $P$ and $Q$ are similar:
$$
Q=APA^{-1}.
$$

::: pf-proof

By hypothesis, $A$ is invertible. Multiplying the identity in step [](#s1){.pf-ref}
on the right by $A^{-1}$ gives the displayed equality.

:::

:::

::: {.pf-step #s3}

Therefore
$$
\boxed{\operatorname{rank}P=\operatorname{rank}Q}.
$$

::: pf-proof

By step [](#s2){.pf-ref},
$$
Q=APA^{-1}.
$$
Left and right multiplication by invertible matrices preserve rank, so
$P$ and $Q$ have the same rank.

:::

:::

::: pf-qed

Step [](#s3){.pf-ref} is the required conclusion.

:::

:::

:::
