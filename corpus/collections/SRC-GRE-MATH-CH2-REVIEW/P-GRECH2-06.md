---
schema: qual/card@1
id: P-GRECH2-06
kind: problem
title: Continuous extension of a rational function at a removable singularity
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Checked against Question 6 of the Chapter 2 review questions in assets/attachments/extracted/chapter-2.md (Mistral OCR), compared with the same page in the Cracking the GRE Mathematics Subject Test book extraction.
---

::: {.problem}
If the function

$$
f(x) = \begin{cases} \frac{x^2 - 6x + 8}{x^3 - 2x^2 + 2x - 4} & \text{if } x \neq 2 \\ k & \text{if } x = 2 \end{cases}
$$

is continuous everywhere, what is the value of $k$?

(A) $1$
(B) $\frac{1}{2}$
(C) $\frac{1}{8}$
(D) $-\frac{1}{3}$
(E) $-1$
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

For $x\ne2$,
$$
f(x)=\frac{x-4}{x^2+2}.
$$


::: pf-proof

Factor numerator and denominator:
$$
x^2-6x+8=(x-2)(x-4)
$$
and
$$
x^3-2x^2+2x-4
=x^2(x-2)+2(x-2)
=(x-2)(x^2+2).
$$
Cancelling the nonzero factor $x-2$ gives the displayed formula.

:::

:::

::: {.pf-step #s1-2}

Continuity at $x=2$ forces
$$
k=-\frac13.
$$


::: pf-proof

By step [](#s1-1){.pf-ref},
$$
\lim_{x\to2}f(x)
=\lim_{x\to2}\frac{x-4}{x^2+2}
=\frac{-2}{6}
=-\frac13.
$$
For continuity at $2$, the value $f(2)=k$ must equal this limit.

:::

:::

::: {.pf-step #s1-3}

Therefore
$$
\boxed{k=-\frac13},
$$
so the answer is (D).


::: pf-proof

This is exactly the value forced by step [](#s1-2){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s1-3){.pf-ref} gives the unique value making the function continuous everywhere.

:::

:::

:::
