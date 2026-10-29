---
schema: qual/card@1
id: P-GREPT-34
kind: problem
title: "Sign and size of $f^{(4)}(0)$ for a power series"
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: "Transcribed from Question 34 of the Practice Test (Chapter 9) in assets/attachments/extracted/Cracking_the_GRE_Mathematics_Subject.md (Mistral OCR)."
---

::: {.problem}
If $f(x) = \sum_{n=0}^{\infty} \frac{(n+1)^{n/2}}{(n!)^2} x^n$, what is true of the value of $f^{(4)}(0)$?

(A) It is negative.
(B) It is positive and less than $1$.
(C) It is equal to $1$.
(D) It is greater than $1$.
(E) It does not exist.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

The coefficient of $x^4$ in the power series for $f$ is
$$
a_4=\frac{5^2}{(4!)^2}.
$$


::: pf-proof

Substituting $n=4$ into
$$
a_n=\frac{(n+1)^{n/2}}{(n!)^2}
$$
gives
$$
a_4=\frac{(4+1)^{4/2}}{(4!)^2}
=\frac{25}{(4!)^2}.
$$

:::

:::

::: {.pf-step #s1-2}

One has
$$
f^{(4)}(0)=4!a_4=\frac{25}{24}.
$$


::: pf-proof

For a power series $f(x)=\sum_{n\ge0}a_nx^n$, the Taylor coefficient
identity gives
$$
a_4=\frac{f^{(4)}(0)}{4!}.
$$
Using step [](#s1-1){.pf-ref} therefore yields
$$
f^{(4)}(0)=4!\frac{25}{(4!)^2}
=\frac{25}{4!}
=\frac{25}{24}.
$$

:::

:::

::: {.pf-step #s1-3}

Therefore
$$
\boxed{f^{(4)}(0)>1},
$$
so the answer is (D).


::: pf-proof

Step [](#s1-2){.pf-ref} gives $f^{(4)}(0)=25/24$, and $25/24>1$.

:::

:::

::: pf-qed

Step [](#s1-3){.pf-ref} gives the required comparison.

:::

:::

:::
