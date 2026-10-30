---
schema: qual/card@1
id: P-GRECH2-17
kind: problem
title: Derivative of $f(x^3)/(xf(x^2))$ at $x=1$
classification:
  areas: [prelim]
  topics:
  - Differentiation
  - Chain Rule
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Checked against Question 17 of the Chapter 2 review questions in assets/attachments/extracted/chapter-2.md (Mistral OCR), compared with the same page in the Cracking the GRE Mathematics Subject Test book extraction.
---

::: {.problem}
If $f(1) = 1$ and $f'(1) = -1$, then the value of $\frac{d}{dx} \left[ \frac{f(x^3)}{xf(x^2)} \right]$ at $x = 1$ is equal to

(A) $1$
(B) $0$
(C) $-1$
(D) $-2$
(E) $-3$
:::

::: {.solution}

Set
$$
N(x)=f(x^3),
\qquad
D(x)=x f(x^2).
$$

::: pf

::: {.pf-step #s1-1}

At $x=1$,
$$
N(1)=1,
\qquad
N'(1)=-3.
$$


::: pf-proof

The hypothesis gives $N(1)=f(1)=1$. By the chain rule,
$$
N'(x)=3x^2 f'(x^3),
$$
so
$$
N'(1)=3f'(1)=3(-1)=-3.
$$

:::

:::

::: {.pf-step #s1-2}

At $x=1$,
$$
D(1)=1,
\qquad
D'(1)=-1.
$$


::: pf-proof

First,
$$
D(1)=1\cdot f(1)=1.
$$
By the product and chain rules,
$$
D'(x)=f(x^2)+2x^2f'(x^2).
$$
Therefore
$$
D'(1)=f(1)+2f'(1)=1-2=-1.
$$

:::

:::

::: {.pf-step #s1-3}

The requested derivative is
$$
\boxed{-2},
$$
so the answer is (D).


::: pf-proof

The quotient rule and steps [](#s1-1){.pf-ref} through [](#s1-2){.pf-ref} give
$$
\left(\frac ND\right)'(1)
=\frac{N'(1)D(1)-N(1)D'(1)}{D(1)^2}
=\frac{(-3)(1)-(1)(-1)}{1}
=-2.
$$

:::

:::

::: pf-qed

Step [](#s1-3){.pf-ref} gives the requested derivative value and corresponding choice.

:::

:::

:::
