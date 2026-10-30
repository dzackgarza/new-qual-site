---
schema: qual/card@1
id: P-GRECH2-38
kind: problem
title: Value of $\int_e^\infty dx/(x(\log x)^n)$ when it converges
classification:
  areas: [prelim]
  topics:
  - Improper Integrals
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Checked against Question 38 of the Chapter 2 review questions in assets/attachments/extracted/chapter-2.md (Mistral OCR), compared with the same page in the Cracking the GRE Mathematics Subject Test book extraction.
---

::: {.problem}
Let $n$ be a number for which the improper integral

$$
\int_{e}^{\infty} \frac{dx}{x(\log x)^n}
$$

converges. Determine the value of the integral.

(A) $\frac{1}{n+1}$
(B) $\frac{1}{n}$
(C) $\frac{1}{n-1}$
(D) $\frac{\log n}{n+1}$
(E) $\frac{\log n}{n-1}$
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

For every $b>e$, the substitution $u=\log x$ gives
$$
\int_e^b \frac{dx}{x(\log x)^n}
=\int_1^{\log b}u^{-n}\,du.
$$


::: pf-proof

Since $u=\log x$, one has $du=dx/x$. The lower endpoint $x=e$ becomes $u=1$, and the upper endpoint $x=b$ becomes $u=\log b$, which proves the displayed identity.

:::

:::

::: {.pf-step #s1-2}

The improper integral converges if and only if $n>1$.


::: pf-proof

By step [](#s1-1){.pf-ref}, if $n\ne1$, then
$$
\int_e^b \frac{dx}{x(\log x)^n}
=\frac{(\log b)^{1-n}-1}{1-n}.
$$
If $n<1$, then $1-n>0$ and $(\log b)^{1-n}\to\infty$, so the integral diverges. If $n=1$, then step [](#s1-1){.pf-ref} gives
$$
\int_1^{\log b}\frac{du}{u}
=\log(\log b),
$$
which also diverges as $b\to\infty$. If $n>1$, then $1-n<0$, so $(\log b)^{1-n}\to0$ and the limit is finite. Thus convergence is equivalent to $n>1$.

:::

:::

::: {.pf-step #s1-3}

For the admissible values of $n$,
$$
\boxed{\int_e^\infty \frac{dx}{x(\log x)^n}=\frac1{n-1}},
$$
so the answer is (C).


::: pf-proof

By step [](#s1-2){.pf-ref}, convergence implies $n>1$. Therefore the formula in step [](#s1-2){.pf-ref} yields
$$
\begin{aligned}
\int_e^\infty \frac{dx}{x(\log x)^n}
&=\lim_{b\to\infty}\frac{(\log b)^{1-n}-1}{1-n}\\
&=\frac{0-1}{1-n}\\
&=\frac1{n-1}.
\end{aligned}
$$

:::

:::

::: pf-qed

Step [](#s1-3){.pf-ref} gives the requested value and corresponding choice.

:::

:::

:::
