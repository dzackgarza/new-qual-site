---
schema: qual/card@1
id: P-GRECH1-20
kind: problem
title: Formula for the inverse hyperbolic tangent
classification:
  areas:
  - algebra
  topics:
  - Hyperbolic Functions
  - Inverse Functions
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Re-transcribed from Chapter 1 review Question 20 in assets/attachments/extracted/Cracking_the_GRE_Mathematics_Subject.md (Mistral OCR), replacing the earlier chapter-1.pdf transcription. The book extraction dropped 'cosh x =' from the first display; the chapter-1.pdf extraction keeps it.
---

::: {.problem}
The hyperbolic cosine function, denoted $\cosh$, is defined by the equation:

$$
\cosh x = \frac{e^x + e^{-x}}{2}
$$

If the hyperbolic tangent function, $\tanh$, is defined by

$$
\tanh x = \frac{\sinh x}{\cosh x}
$$

find a formula for $\tanh^{-1} x$.

(A) $\frac{1}{2} \log \frac{x - 1}{x + 1}$
(B) $\log \frac{\frac{1}{2} x - 1}{\frac{1}{2} x + 1}$
(C) $\log \frac{1 + \frac{1}{2} x}{1 - \frac{1}{2} x}$
(D) $\frac{1}{2} \log \frac{x + 1}{x - 1}$
(E) $\frac{1}{2} \log \frac{1 + x}{1 - x}$
:::

::: {.solution}

Let $y=\tanh^{-1}x$, so that $x=\tanh y$.

::: pf

::: {.pf-step #s1-1}

The equation $x=\tanh y$ is equivalent to
$$
e^{2y}=\frac{1+x}{1-x}.
$$


::: pf-proof

Using the definitions of $\sinh$ and $\cosh$,
$$
x=\frac{e^y-e^{-y}}{e^y+e^{-y}}.
$$
Multiplying by $e^y(e^y+e^{-y})$ gives
$$
x(e^{2y}+1)=e^{2y}-1.
$$
Therefore
$$
(1-x)e^{2y}=1+x,
$$
which yields the displayed identity for $-1<x<1$, the range of $\tanh$.

:::

:::

::: {.pf-step #s1-2}

Hence
$$
\boxed{\tanh^{-1}x=\frac12\log\frac{1+x}{1-x}},
$$
so the answer is (E).


::: pf-proof

The quotient in step [](#s1-1){.pf-ref} is positive for $-1<x<1$. Taking logarithms gives
$$
2y=\log\frac{1+x}{1-x},
$$
and division by $2$ gives the claimed formula.

:::

:::

::: pf-qed

Step [](#s1-2){.pf-ref} gives the requested inverse formula on the full domain of $\tanh^{-1}$.

:::

:::

:::
