---
schema: qual/card@1
id: P-GRECH2-01
kind: problem
title: Limit of $(\cos n\pi)(\sin^2 n)/\sqrt[e]{n}$
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Checked against Question 1 of the Chapter 2 review questions in assets/attachments/extracted/chapter-2.md (Mistral OCR), compared with the same page in the Cracking the GRE Mathematics Subject Test book extraction. Both extractions garbled the root index; the book's Chapter 8 solution bounds the term by 1/n^(1/e), fixing the e-th root.
---

::: {.problem}
Consider the sequence $(x_n)$ whose terms are given by the formula

$$
x_n = \frac{(\cos n\pi)(\sin^2 n)}{\sqrt[e]{n}}
$$

for each integer $n \ge 1$. Given that this sequence converges, what is its limit?

(A) $0$
(B) $1$
(C) $\log 2$
(D) $\sqrt[4]{2}$
(E) $\sqrt[4]{e}$
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

For every $n\geq1$,
$$
\abs{x_n}\leq \frac{1}{n^{1/e}}.
$$


::: pf-proof

Since $\abs{\cos(n\pi)}\leq1$ and $0\leq\sin^2 n\leq1$,
$$
\abs{x_n}
=\frac{\abs{\cos(n\pi)}\sin^2 n}{\sqrt[e]{n}}
\leq\frac1{\sqrt[e]{n}}
=\frac1{n^{1/e}}.
$$

:::

:::

::: {.pf-step #s1-2}

$\lim_{n\to\infty}x_n=0$.


::: pf-proof

Because $1/e>0$,
$$
\lim_{n\to\infty}\frac1{n^{1/e}}=0.
$$
Together with step [](#s1-1){.pf-ref}, this gives
$$
-\frac1{n^{1/e}}\leq x_n\leq\frac1{n^{1/e}},
$$
so the squeeze theorem yields $x_n\to0$.

:::

:::

::: {.pf-step #s1-3}

The limit is
$$
\boxed{0},
$$
so the answer is (A).


::: pf-proof

This is exactly the limit established in step [](#s1-2){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s1-3){.pf-ref} gives the requested limit and corresponding choice.

:::

:::

:::
