---
schema: qual/card@1
id: P-GRECH2-05
kind: problem
title: Asymptotes of the curve $2x^2+3x-2xy-y=6$
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Checked against Question 5 of the Chapter 2 review questions in assets/attachments/extracted/chapter-2.md (Mistral OCR), compared with the same page in the Cracking the GRE Mathematics Subject Test book extraction.
---

::: {.problem}
The curve whose equation is

$$
2x^2 + 3x - 2xy - y = 6
$$

has two asymptotes. Identify these lines.

(A) $x = -1$ and $y = -2$
(B) $x = -2$ and $y = 1$
(C) $x = -\frac{1}{2}$ and $y = x$
(D) $x = -\frac{1}{2}$ and $y = x + 1$
(E) $x = \frac{1}{2}$ and $y = 1 - x$
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

Away from $x=-1/2$, the curve is the graph of
$$
y=x+1-\frac{7}{2x+1}.
$$


::: pf-proof

Rearranging the defining equation gives
$$
(2x+1)y=2x^2+3x-6.
$$
For $2x+1\ne0$,
$$
y=\frac{2x^2+3x-6}{2x+1}
=x+1-\frac7{2x+1},
$$
where the last equality is polynomial division.

:::

:::

::: {.pf-step #s1-2}

The vertical asymptote is $x=-1/2$.


::: pf-proof

In the expression from step [](#s1-1){.pf-ref}, the denominator $2x+1$ tends to $0$ as $x\to-1/2$, while the numerator of the fractional term is the nonzero constant $-7$. Hence the fractional term is unbounded, so $x=-1/2$ is a vertical asymptote.

:::

:::

::: {.pf-step #s1-3}

The oblique asymptote is $y=x+1$.


::: pf-proof

By step [](#s1-1){.pf-ref},
$$
y-(x+1)=-\frac7{2x+1}\longrightarrow0
$$
as $x\to\pm\infty$. Thus the graph approaches the line $y=x+1$ at infinity.

:::

:::

::: {.pf-step #s1-4}

The two asymptotes are
$$
\boxed{x=-\frac12\quad\text{and}\quad y=x+1},
$$
so the answer is (D).


::: pf-proof

Combine steps [](#s1-2){.pf-ref} and [](#s1-3){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s1-4){.pf-ref} identifies both requested lines and the corresponding choice.

:::

:::

:::
