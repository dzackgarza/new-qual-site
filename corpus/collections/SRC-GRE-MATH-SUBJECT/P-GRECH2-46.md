---
schema: qual/card@1
id: P-GRECH2-46
kind: problem
title: First integer outside the convergence set of $\sum n!(2n)!x^n/(3n)!$
classification:
  areas: [prelim]
  topics:
  - Power Series
  - Radius of Convergence
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Checked against Question 46 of the Chapter 2 review questions in assets/attachments/extracted/chapter-2.md (Mistral OCR), compared with the same page in the Cracking the GRE Mathematics Subject Test book extraction.
---

::: {.problem}
The smallest positive integer $x$ for which the power series $\sum_{n=1}^{\infty} \frac{n!(2n)!}{(3n)!} x^n$ does not converge is

(A) $4$
(B) $6$
(C) $7$
(D) $8$
(E) $9$
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

If
$$
c_n(x)=\frac{n!(2n)!}{(3n)!}x^n,
$$
then for $x\ne0$,
$$
\lim_{n\to\infty}\abs{\frac{c_{n+1}(x)}{c_n(x)}}
=\frac{4\abs{x}}{27}.
$$


::: pf-proof

Cancelling factorials gives
$$
\abs{\frac{c_{n+1}(x)}{c_n(x)}}
=\abs{x}\,
\frac{(n+1)(2n+1)(2n+2)}
{(3n+1)(3n+2)(3n+3)}.
$$
Dividing numerator and denominator by $n^3$ and taking the limit yields
$4\abs{x}/27$.

:::

:::

::: {.pf-step #s1-2}

The series converges absolutely for $\abs{x}<27/4$ and diverges for $\abs{x}>27/4$.


::: pf-proof

This is the ratio test applied to the limit in step [](#s1-1){.pf-ref}. At $x=0$ the series is identically zero, so it also converges.

:::

:::

::: {.pf-step #s1-3}

The smallest positive integer for which the series does not converge is
$$
\boxed{x=7},
$$
so the answer is (C).


::: pf-proof

The positive integers $1,\ldots,6$ all satisfy $x<27/4$, so step [](#s1-2){.pf-ref} gives convergence. Since
$$
7>\frac{27}{4},
$$
step [](#s1-2){.pf-ref} gives divergence at $x=7$. Thus $7$ is the first positive integer outside the convergence interval.

:::

:::

::: pf-qed

Step [](#s1-3){.pf-ref} gives the requested integer and corresponding choice.

:::

:::

:::
