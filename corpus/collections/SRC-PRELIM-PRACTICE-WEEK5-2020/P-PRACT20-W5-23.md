---
schema: qual/card@1
id: P-PRACT20-W5-23
kind: problem
title: Image of the imaginary axis under a real-valued entire function
classification:
  areas:
  - complex-analysis
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Rewrote the statement and replaced the OCR-garbled answer choices (a)-(c), checked against Week5_solns.pdf page 6 (Problem 23).
---

::: {.problem}
If $f$ is an entire function which maps the complex plane into the real axis, then which of the following are the possible images of the imaginary axis under $f$?

(a) the point $0$ (b) any arbitrary point in $\RR$ (c) a half line (i.e., a set $(a, \infty)$ or $(-\infty, a)$) (d) the whole real line
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

The function $f$ must be constant.


::: pf-proof

Suppose $f$ were nonconstant. By the open mapping theorem, the image
$$
f(\CC)
$$
would be an open subset of $\CC$. By hypothesis,
$$
f(\CC)\subseteq\RR.
$$
But the real axis contains no nonempty open subset of $\CC$. This is a
contradiction. Hence $f$ is constant.

:::

:::

::: {.pf-step #s1-2}

Therefore the image of the imaginary axis is a singleton
$$
\boxed{\{c\}\qquad\text{for some arbitrary }c\in\RR}.
$$


::: pf-proof

By step [](#s1-1){.pf-ref} there is $c\in\RR$ such that
$$
f(z)=c
\qquad(z\in\CC).
$$
Hence
$$
f(i\RR)=\{c\}.
$$
Conversely, every real constant function is entire and has this image.

:::

:::

::: {.pf-step #s1-3}

In the listed choices, (b) is the general answer, and (a) is its
special case $c=0$; neither (c) nor (d) is possible.


::: pf-proof

This follows immediately from the singleton classification in step [](#s1-2){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s1-3){.pf-ref} settles the alternatives.

:::

:::

:::
