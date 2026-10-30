---
schema: qual/card@1
id: P-GRECH7-20
kind: problem
title: Principal logarithm of $-e^3$
classification:
  areas: [complex-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Checked against Question 20 of the Chapter 7 review questions in assets/attachments/extracted/Chapter-7.md (Mistral OCR), compared with the same page in the Cracking the GRE Mathematics Subject Test book extraction. The chapter extraction read -e^2; the book extraction and its Chapter 8 solution read -e^3.
---

::: {.problem}
What is $\operatorname{Log}(-e^3)$?

(A) $-3$
(B) $3$
(C) $3 + \pi i$
(D) $3 - \pi i$
(E) $3 + 2\pi i$
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

The modulus of $-e^3$ is $e^3$, and its principal argument is $\pi$.


::: pf-proof

The complex number $-e^3$ lies on the negative real axis at distance $e^3$ from the origin. Hence
$$
\abs{-e^3}=e^3.
$$
With the principal argument chosen in $(-\pi,\pi]$, the argument of a negative real number is $\pi$.

:::

:::

::: {.pf-step #s1-2}

Therefore
$$
\boxed{\operatorname{Log}(-e^3)=3+\pi i},
$$
so the answer is (C).


::: pf-proof

By definition of the principal logarithm,
$$
\operatorname{Log}z=\log\abs{z}+i\operatorname{Arg}z.
$$
Using step [](#s1-1){.pf-ref},
$$
\operatorname{Log}(-e^3)
=\log(e^3)+i\pi
=3+\pi i.
$$

:::

:::

::: pf-qed

Step [](#s1-2){.pf-ref} gives the requested principal logarithm.

:::

:::

:::
