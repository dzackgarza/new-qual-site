---
schema: qual/card@1
id: P-GRECH7-32
kind: problem
title: Normalizing constant of a linear density on $[0,8]$
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Checked against Question 32 of the Chapter 7 review questions in assets/attachments/extracted/Chapter-7.md (Mistral OCR), compared with the same page in the Cracking the GRE Mathematics Subject Test book extraction.
- event: source-checked
  by: claude-opus-5-5
  date: 2026-10-29
  note: The source conditions the first branch on $0\le t\le8$, lists only choices (A)--(E), and its solution gives (E) $c=-4/3$ from the miscomputed $16+6c$; no real $c$ makes $f$ a density. The statement now reads $0\le x\le8$, asks for the value of $c$ if any, and adds choice (F) No value of $c$.
---

::: {.problem}
If $f(x) = \begin{cases} \frac{x}{2} + c & \text{for } 0 \le x \le 8 \\ 0 & \text{otherwise} \end{cases}$, for what value of $c$, if any, is $f(x)$ the probability density function of a random variable $X$?

(A) $\frac{4}{3}$
(B) $\frac{2}{3}$
(C) $0$
(D) $-\frac{2}{3}$
(E) $-\frac{4}{3}$
(F) No value of $c$
:::

::: {.solution}

::: pf

::: {.pf-step #s1-2}

Normalization forces
$$
c=-\frac{15}{8}.
$$


::: pf-proof

A probability density must satisfy
$$
\int_{-\infty}^{\infty} f(x)\,dx=1.
$$
Thus
$$
1=\int_0^8\left(\frac{x}{2}+c\right)dx
=\left[\frac{x^2}{4}+cx\right]_0^8
=16+8c.
$$
Hence $8c=-15$, so $c=-15/8$.

:::

:::

::: {.pf-step #s1-3}

The value in step [](#s1-2){.pf-ref} does not make $f$ a probability density, and in fact no value of $c$ does.


::: pf-proof

For the normalized value from step [](#s1-2){.pf-ref},
$$
f(0)=c=-\frac{15}{8}<0,
$$
violating the nonnegativity requirement for a density. Conversely, nonnegativity at $x=0$ requires $c\ge0$, but then
$$
\int_0^8\left(\frac{x}{2}+c\right)dx=16+8c\ge16>1,
$$
so normalization is impossible. Therefore no real $c$ satisfies both density conditions.

:::

:::

::: pf-step

The answer is $\boxed{\text{(F)}}$: no value of $c$ works.


::: pf-proof

Step [](#s1-3){.pf-ref} proves that no real value of $c$ works. For instance, for $c=-4/3$, one has $f(0)<0$ and
$$
\int_0^8 f(x)\,dx=16-\frac{32}{3}=\frac{16}{3}\ne1.
$$

:::

:::

:::

:::
