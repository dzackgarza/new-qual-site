---
schema: qual/card@1
id: P-GRECH7-14
kind: problem
title: Laurent series of $1/(z-3)$ on $|z-4|>1$
classification:
  areas: [complex-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Checked against Question 14 of the Chapter 7 review questions in assets/attachments/extracted/Chapter-7.md (Mistral OCR), compared with the same page in the Cracking the GRE Mathematics Subject Test book extraction.
---

::: {.problem}
Find the Laurent series expansions of the function $f(z) = \frac{1}{z - 3}$ that is valid in the annulus $|z - 4| > 1$.

(A) $\sum_{n=1}^{\infty} (4 - z)^{-n-1}$
(B) $\sum_{n=0}^{\infty} (-1)^n (z - 4)^{-n}$
(C) $\sum_{n=1}^{\infty} (-1)^n (z - 4)^{-n-1}$
(D) $\sum_{n=0}^{\infty} (-1)^n (z - 4)^{-n-1}$
(E) $\sum_{n=1}^{\infty} (z - 4)^{-n-1}$
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

For $|z-4|>1$,
$$
\frac1{z-3}
=\frac1{z-4}\frac1{1+\frac1{z-4}}.
$$


::: pf-proof

Since $z-3=(z-4)+1$, factoring $z-4$ from the denominator gives
$$
z-3=(z-4)\left(1+\frac1{z-4}\right),
$$
which yields the displayed identity.

:::

:::

::: {.pf-step #s1-2}

The geometric-series expansion is
$$
\frac1{z-3}
=\sum_{n=0}^{\infty}(-1)^n(z-4)^{-n-1}.
$$


::: pf-proof

The hypothesis $|z-4|>1$ gives
$$
\left|\frac{-1}{z-4}\right|<1.
$$
Hence, using $1/(1-w)=\sum_{n=0}^{\infty}w^n$ with $w=-1/(z-4)$ in step [](#s1-1){.pf-ref},
$$
\begin{aligned}
\frac1{z-3}
&=\frac1{z-4}\sum_{n=0}^{\infty}\left(\frac{-1}{z-4}\right)^n\\
&=\sum_{n=0}^{\infty}(-1)^n(z-4)^{-n-1}.
\end{aligned}
$$
The convergence condition is exactly $|z-4|>1$.

:::

:::

::: {.pf-step #s1-3}

Therefore the required Laurent series is
$$
\boxed{\sum_{n=0}^{\infty}(-1)^n(z-4)^{-n-1}},
$$
so the answer is (D).


::: pf-proof

Step [](#s1-2){.pf-ref} derives the expansion on the stated annulus. In particular, the $n=0$ term $(z-4)^{-1}$ is present, so the otherwise similar choice (C), whose sum starts at $n=1$, omits the leading term and cannot equal $f$.

:::

:::

::: pf-qed

Step [](#s1-3){.pf-ref} gives the required expansion.

:::

:::

:::
