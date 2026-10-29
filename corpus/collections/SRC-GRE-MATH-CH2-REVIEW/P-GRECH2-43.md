---
schema: qual/card@1
id: P-GRECH2-43
kind: problem
title: Riemann-sum limit of $\sum_{k=1}^n (k/n^2-k^2/n^3)$
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Checked against Question 43 of the Chapter 2 review questions in assets/attachments/extracted/chapter-2.md (Mistral OCR), compared with the same page in the Cracking the GRE Mathematics Subject Test book extraction.
---

::: {.problem}
Evaluate the following limit:

$$
\lim_{n \to \infty} \sum_{k=1}^{n} \left[ \frac{k}{n^2} - \frac{k^2}{n^3} \right]
$$

(A) $\frac{2}{3}$
(B) $\frac{1}{2}$
(C) $\frac{1}{3}$
(D) $\frac{1}{6}$
(E) $\frac{1}{12}$
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

For every positive integer $n$,
$$
\sum_{k=1}^n\left(\frac{k}{n^2}-\frac{k^2}{n^3}\right)
=\frac1n\sum_{k=1}^n
\left[\frac{k}{n}-\left(\frac{k}{n}\right)^2\right].
$$


::: pf-proof

Factor $1/n$ from each summand:
$$
\frac{k}{n^2}-\frac{k^2}{n^3}
=\frac1n\left[\frac{k}{n}-\left(\frac{k}{n}\right)^2\right].
$$
Summing from $k=1$ to $n$ gives the identity.

:::

:::

::: {.pf-step #s1-2}

The required limit equals
$$
\int_0^1(x-x^2)\,dx.
$$


::: pf-proof

Let $f(x)=x-x^2$. The expression in step [](#s1-1){.pf-ref} is the right-endpoint Riemann sum for $f$ on $[0,1]$ with $n$ equal subintervals. Since $f$ is continuous on $[0,1]$, these Riemann sums converge to $\int_0^1f(x)\,dx$.

:::

:::

::: {.pf-step #s1-3}

The limit is
$$
\boxed{\frac16},
$$
so the answer is (D).


::: pf-proof

By step [](#s1-2){.pf-ref},
$$
\begin{aligned}
\int_0^1(x-x^2)\,dx
&=\left[\frac{x^2}{2}-\frac{x^3}{3}\right]_0^1\\
&=\frac12-\frac13\\
&=\frac16.
\end{aligned}
$$

:::

:::

::: pf-qed

Step [](#s1-3){.pf-ref} gives the requested limit and corresponding choice.

:::

:::

:::
