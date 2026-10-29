---
schema: qual/card@1
id: P-GREPT-51
kind: problem
title: "Mean of a shifted exponential distribution"
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: "Transcribed from Question 51 of the Practice Test (Chapter 9) in assets/attachments/extracted/Cracking_the_GRE_Mathematics_Subject.md (Mistral OCR)."
---

::: {.problem}
Let $X$ be a random variable whose probability density function is

$$f(t) = \begin{cases} \frac{1}{2} e^{-(t-1)/2} & \text{if } 1 < t < \infty \\ 0 & \text{otherwise} \end{cases}$$

What is the expectation (mean) of $X$?

(A) $1$
(B) $2$
(C) $3$
(D) $4$
(E) $6$
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

The expectation is
$$
\EE[X]
=\int_1^\infty t\,\frac12e^{-(t-1)/2}\,dt.
$$


::: pf-proof

For a continuous random variable with density $f$, the expectation is
$\int_{-\infty}^{\infty}tf(t)\,dt$. The given density vanishes outside
$(1,\infty)$, giving the displayed integral.

:::

:::

::: {.pf-step #s1-2}

With
$$
s=\frac{t-1}{2},
$$
the integral in step [](#s1-1){.pf-ref} becomes
$$
\int_0^\infty(2s+1)e^{-s}\,ds.
$$


::: pf-proof

The substitution gives $t=2s+1$ and $dt=2\,ds$, so
$$
t\frac12e^{-(t-1)/2}\,dt
=(2s+1)e^{-s}\,ds.
$$
The lower endpoint $t=1$ becomes $s=0$, and $t\to\infty$ becomes
$s\to\infty$.

:::

:::

::: {.pf-step #s1-3}

One has
$$
\int_0^\infty e^{-s}\,ds=1
\qquad\text{and}\qquad
\int_0^\infty se^{-s}\,ds=1.
$$


::: pf-proof

The first integral is
$[-e^{-s}]_0^\infty=1$. For the second, integration by parts gives
$$
\int_0^R se^{-s}\,ds
=\left[-se^{-s}\right]_0^R+\int_0^R e^{-s}\,ds.
$$
Letting $R\to\infty$ gives $1$, since $Re^{-R}\to0$.

:::

:::

::: {.pf-step #s1-4}

Therefore
$$
\EE[X]=\boxed{3},
$$
so the answer is (C).


::: pf-proof

By steps [](#s1-2){.pf-ref} through [](#s1-3){.pf-ref},
$$
\EE[X]
=2\int_0^\infty se^{-s}\,ds+\int_0^\infty e^{-s}\,ds
=2+1=3.
$$

:::

:::

::: pf-qed

Step [](#s1-4){.pf-ref} gives the requested mean.

:::

:::

:::
