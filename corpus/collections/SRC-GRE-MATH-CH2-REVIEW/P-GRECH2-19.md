---
schema: qual/card@1
id: P-GRECH2-19
kind: problem
title: Conclusion of the mean value theorem for given endpoint values
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Checked against Question 19 of the Chapter 2 review questions in assets/attachments/extracted/chapter-2.md (Mistral OCR), compared with the same page in the Cracking the GRE Mathematics Subject Test book extraction.
---

::: {.problem}
Let $f(x)$ be continuous on a bounded interval, $[a, b]$, where $a \neq b$, such that $f(a) = 1$ and $f(b) = 3$, and $f'(x)$ exists for every $x$ in $(a, b)$.
What does the Mean-Value theorem say about $f$?

(A) There exists a number $c$ in the interval $(a, b)$ such that $f'(c) = 0$.
(B) There exists a number $c$ in the interval $(a, b)$ such that $f(c) = 0$.
(C) There exists a number $c$ in the interval $(a, b)$ such that $f'(c) = 2$.
(D) There exists a number $c$ in the interval $(a, b)$ such that $f'(c) = 2(b - a)$.
(E) There exists a number $c$ in the interval $(a, b)$ such that $(b - a)f'(c) = 2$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

There exists $c\in(a,b)$ such that
$$
f'(c)=\frac{2}{b-a}.
$$


::: pf-proof

The hypotheses state that $f$ is continuous on $[a,b]$ and differentiable on $(a,b)$, so the mean value theorem applies. Hence some $c\in(a,b)$ satisfies
$$
f'(c)=\frac{f(b)-f(a)}{b-a}
=\frac{3-1}{b-a}
=\frac2{b-a}.
$$

:::

:::

::: {.pf-step #s1-2}

Equivalently,
$$
\boxed{(b-a)f'(c)=2},
$$
so the answer is (E).


::: pf-proof

Since $a\ne b$, one has $b-a\ne0$. Multiplying the equality in step [](#s1-1){.pf-ref} by $b-a$ gives the displayed conclusion.

:::

:::

::: pf-qed

Step [](#s1-2){.pf-ref} is exactly the conclusion among the listed choices guaranteed by the mean value theorem.

:::

:::

:::
