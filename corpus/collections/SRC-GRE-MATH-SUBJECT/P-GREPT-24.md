---
schema: qual/card@1
id: P-GREPT-24
kind: problem
title: "Probability of a 5 then a 6 with a die weighted toward even faces"
classification:
  areas: [prelim]
  topics:
  - Probability
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: "Transcribed from Question 24 of the Practice Test (Chapter 9) in assets/attachments/extracted/Cracking_the_GRE_Mathematics_Subject.md (Mistral OCR)."
- event: source-checked
  by: claude-opus-5-5
  date: 2026-10-29
  note: The source said the die "is thrown twice" without stating independence, and its answer (A) assumes independent throws. The statement now says the die is thrown twice independently.
---

::: {.problem}
A six-sided die (whose faces are numbered $1$ through $6$, as usual) is known to be counterfeit: The probability of rolling any even number is twice the probability of rolling any odd number. What is the probability that if this die is thrown twice, independently, the first roll will be a $5$ and the second roll will be a $6$?

(A) $\frac{2}{81}$
(B) $\frac{1}{18}$
(C) $\frac{2}{27}$
(D) $\frac{1}{9}$
(E) Cannot be determined from the information given
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

If $p$ is the probability of each odd face, then the probability of
each even face is $2p$ and
$$
p=\frac19.
$$


::: pf-proof

There are three odd faces and three even faces, so the total probability is
$$
3p+3(2p)=9p.
$$
Since the six face probabilities sum to $1$, one has $9p=1$ and hence
$p=1/9$.

:::

:::

::: {.pf-step #s1-2}

Thus
$$
P(5)=\frac19
\qquad\text{and}\qquad
P(6)=\frac29.
$$


::: pf-proof

The face $5$ is odd, so its probability is $p$. The face $6$ is even, so its
probability is $2p$. Substitute the value of $p$ from step [](#s1-1){.pf-ref}.

:::

:::

::: {.pf-step #s1-3}

The requested probability is
$$
\boxed{\text{(A) }\frac{2}{81}}.
$$


::: pf-proof

The throws are independent, so step [](#s1-2){.pf-ref} gives
$$
P(5\text{ then }6)=P(5)\,P(6)=\frac19\cdot\frac29=\frac{2}{81}.
$$

:::

:::

::: pf-qed

Step [](#s1-3){.pf-ref} gives the answer.

:::

:::

:::
