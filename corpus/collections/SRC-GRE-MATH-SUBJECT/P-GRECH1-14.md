---
schema: qual/card@1
id: P-GRECH1-14
kind: problem
title: Polynomial forced constant by five equal values
classification:
  areas:
  - algebra
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Re-transcribed from Chapter 1 review Question 14 in assets/attachments/extracted/Cracking_the_GRE_Mathematics_Subject.md (Mistral OCR), replacing the earlier chapter-1.pdf transcription.
---

::: {.problem}
Given that $p(x)$ is a real polynomial of degree $\le 4$ such that one can find five distinct solutions to the equation $p(x) = 5$, what is the value of $p(5)$?

(A) $0$
(B) $1$
(C) $4$
(D) $5$
(E) Cannot be determined from the information given
:::

::: {.solution}

Define $q(x)=p(x)-5$.

::: pf

::: {.pf-step #s1-1}

$q$ is the zero polynomial.


::: pf-proof

The polynomial $q$ has degree at most $4$ unless it is identically zero. Every solution of $p(x)=5$ is a root of $q$, so by hypothesis $q$ has five distinct real roots. A nonzero polynomial of degree at most $4$ has at most four distinct roots. Therefore $q$ must be identically zero.

:::

:::

::: {.pf-step #s1-2}

$p$ is identically equal to $5$.


::: pf-proof

By step [](#s1-1){.pf-ref},
$$
p(x)-5=q(x)=0
$$
for every $x$, so $p(x)=5$ identically.

:::

:::

::: {.pf-step #s1-3}

The requested value is
$$
\boxed{p(5)=5},
$$
so the answer is (D).


::: pf-proof

Evaluate the identity from step [](#s1-2){.pf-ref} at $x=5$.

:::

:::

::: pf-qed

Step [](#s1-3){.pf-ref} gives the requested value and choice.

:::

:::

:::
