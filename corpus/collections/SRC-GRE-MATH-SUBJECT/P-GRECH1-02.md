---
schema: qual/card@1
id: P-GRECH1-02
kind: problem
title: Positive solutions of a rational inequality
classification:
  areas:
  - algebra
  topics:
  - Inequalities
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Re-transcribed from Chapter 1 review Question 2 in assets/attachments/extracted/Cracking_the_GRE_Mathematics_Subject.md (Mistral OCR), replacing the earlier chapter-1.pdf transcription.
---

::: {.problem}
Determine the set of positive values of $x$ that satisfy the following inequality:

$$
\frac{1}{x} - \frac{1}{x-1} > \frac{1}{x-2}
$$

(A) $(0, 1) \cup (\sqrt{2}, 2)$
(B) $(0, \frac{1}{2}) \cup (1, 2)$
(C) $(\frac{1}{2}, 1) \cup (\sqrt{2}, 2\sqrt{2})$
(D) $(0, \sqrt{2}) \cup (\frac{3}{2}, 2)$
(E) $(1, \sqrt{2}) \cup (2, 2\sqrt{2})$
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

For $x\notin\{0,1,2\}$, the inequality is equivalent to
$$
\frac{2-x^2}{x(x-1)(x-2)}>0.
$$


::: pf-proof

Move the right-hand term to the left and combine fractions:
$$
\frac1x-\frac1{x-1}-\frac1{x-2}
=
\frac{(x-1)(x-2)-x(x-2)-x(x-1)}{x(x-1)(x-2)}
=
\frac{2-x^2}{x(x-1)(x-2)}.
$$

:::

:::

::: {.pf-step #s1-2}

On the positive axis, the expression in step [](#s1-1){.pf-ref} is positive exactly
on
$$
(0,1)\cup(\sqrt2,2).
$$


::: pf-proof

The positive critical points are $1$, $\sqrt2$, and $2$. On the four resulting
intervals the signs of the numerator and denominator are:
$$
\begin{array}{c|c|c|c}
\text{interval}&2-x^2&x(x-1)(x-2)&\text{quotient}\\ \hline
(0,1)&+&+&+\\
(1,\sqrt2)&+&-&-\\
(\sqrt2,2)&-&-&+\\
(2,\infty)&-&+&-
\end{array}
$$
The points $1$ and $2$ are outside the domain, and $\sqrt2$ makes the
numerator zero; the inequality is strict, so none is included.

:::

:::

::: {.pf-step #s1-3}

The solution set is
$$
\boxed{(0,1)\cup(\sqrt2,2)},
$$
so the answer is (A).


::: pf-proof

This is exactly the positive set obtained in step [](#s1-2){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s1-3){.pf-ref} gives the requested set and choice.

:::

:::

:::
