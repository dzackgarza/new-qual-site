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
---

::: {.problem}
If $f(x) = \begin{cases} \frac{x}{2} + c & \text{for } 0 \le t \le 8 \\ 0 & \text{otherwise} \end{cases}$, for what value of $c$ is $f(x)$ the probability density function of a random variable $X$?

(A) $\frac{4}{3}$
(B) $\frac{2}{3}$
(C) $0$
(D) $-\frac{2}{3}$
(E) $-\frac{4}{3}$
:::

::: pf

::: {.pf-step #s1-1}

As printed, the piecewise condition uses the variable $t$ rather than the argument $x$, so it does not define a function of $x$ without an evident correction.


::: pf-proof

The displayed formula is written as $f(x)$ but its first branch is conditioned on $0\le t\le8$, where $t$ is otherwise undefined. The natural intended correction is to read the branch condition as $0\le x\le8$.

:::

:::

::: {.pf-step #s1-2}

Under that correction, normalization would force
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

::: {.pf-step #s1-4}

Consequently none of choices (A)--(E) is correct; in particular, the source's supplied answer $c=-4/3$ neither normalizes the function nor makes it nonnegative.


::: pf-proof

Step [](#s1-3){.pf-ref} proves that no real value of $c$ works. The listed choices are all real numbers, so none can be correct. For $c=-4/3$, one has $f(0)<0$ and
$$
\int_0^8 f(x)\,dx=16-\frac{32}{3}=\frac{16}{3}\ne1.
$$

:::

:::

::: pf-qed

Steps [](#s1-1){.pf-ref} through [](#s1-4){.pf-ref} identify both the malformed variable in the printed statement and the mathematical impossibility of the intended density problem.

:::

:::
