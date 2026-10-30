---
schema: qual/card@1
id: P-GRECH2-41
kind: problem
title: Convergence of three infinite series
classification:
  areas: [prelim]
  topics:
  - Series
  - Convergence Tests
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Checked against Question 41 of the Chapter 2 review questions in assets/attachments/extracted/chapter-2.md (Mistral OCR), compared with the same page in the Cracking the GRE Mathematics Subject Test book extraction. The chapter extraction read n\sqrt[n]{n}; the book extraction and its Chapter 8 solution read n\sqrt[4]{n}.
---

::: {.problem}
Which of the following infinite series converge?

I. $\sum_{n=1}^{\infty} \frac{\cos^4(\arctan n)}{n\sqrt[4]{n}}$

II. $\sum_{n=2}^{\infty} \frac{1}{n \log n}$

III. $\sum_{n=0}^{\infty} \frac{(n+1)^3}{5(n+2)(n+3)(n+4)}$

(A) I only
(B) I and II only
(C) II only
(D) I and III only
(E) II and III only
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

Series I converges.


::: pf-proof

For every $n\ge1$,
$$
0\le
\frac{\cos^4(\arctan n)}{n\sqrt[4]{n}}
\le
\frac1{n^{5/4}},
$$
because $0\le\cos^4(\arctan n)\le1$ and
$n\sqrt[4]{n}=n^{5/4}$. The $p$-series
$\sum_{n=1}^\infty n^{-5/4}$ converges, so the comparison test proves convergence of series I.

:::

:::

::: {.pf-step #s1-2}

Series II diverges.


::: pf-proof

For $x\ge2$, the function
$$
f(x)=\frac1{x\log x}
$$
is positive, continuous, and decreasing. Moreover,
$$
\begin{aligned}
\int_2^b\frac{dx}{x\log x}
&=\left[\log(\log x)\right]_2^b\\
&=\log(\log b)-\log(\log2)
\longrightarrow\infty.
\end{aligned}
$$
The integral test therefore shows that
$\sum_{n=2}^\infty 1/(n\log n)$ diverges.

:::

:::

::: {.pf-step #s1-3}

Series III diverges.


::: pf-proof

Its terms do not tend to zero:
$$
\lim_{n\to\infty}
\frac{(n+1)^3}{5(n+2)(n+3)(n+4)}
=\frac15\ne0.
$$
Hence the term test implies divergence.

:::

:::

::: {.pf-step #s1-4}

Only series I converges, so the answer is
$$
\boxed{\text{(A) I only}}.
$$


::: pf-proof

This follows from steps [](#s1-1){.pf-ref} through [](#s1-3){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s1-4){.pf-ref} gives the requested choice.

:::

:::

:::
