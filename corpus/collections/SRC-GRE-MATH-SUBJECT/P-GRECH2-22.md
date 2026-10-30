---
schema: qual/card@1
id: P-GRECH2-22
kind: problem
title: Maximum of $x^ke^{-x}$ on $x>0$
classification:
  areas: [prelim]
  topics:
  - Optimization
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Checked against Question 22 of the Chapter 2 review questions in assets/attachments/extracted/chapter-2.md (Mistral OCR), compared with the same page in the Cracking the GRE Mathematics Subject Test book extraction.
---

::: {.problem}
Let $f(x) = x^k e^{-x}$, where $k$ is a positive constant. For $x > 0$, what is the maximum value attained by $f$?

(A) $\left(\frac{e}{k}\right)^k$
(B) $\sqrt[k]{\frac{e}{k^k}}$
(C) $\frac{(\log k)^k}{k}$
(D) $\left(\frac{e}{\log k}\right)^k$
(E) $\left(\frac{k}{e}\right)^k$
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

For $x>0$,
$$
f'(x)=x^{k-1}e^{-x}(k-x).
$$


::: pf-proof

Using the product rule,
$$
\begin{aligned}
f'(x)
&=kx^{k-1}e^{-x}-x^ke^{-x}\\
&=x^{k-1}e^{-x}(k-x).
\end{aligned}
$$

:::

:::

::: {.pf-step #s1-2}

$f$ is strictly increasing on $(0,k)$ and strictly decreasing on $(k,\infty)$.


::: pf-proof

For $x>0$, both $x^{k-1}$ and $e^{-x}$ are positive. Thus the sign of $f'(x)$ in step [](#s1-1){.pf-ref} is the sign of $k-x$: it is positive when $0<x<k$, zero at $x=k$, and negative when $x>k$.

:::

:::

::: {.pf-step #s1-3}

The maximum value is
$$
\boxed{f(k)=\left(\frac{k}{e}\right)^k},
$$
so the answer is (E).


::: pf-proof

By step [](#s1-2){.pf-ref}, the unique turning point $x=k$ is the global maximum on $x>0$. Evaluating there gives
$$
f(k)=k^ke^{-k}=\left(\frac{k}{e}\right)^k.
$$

:::

:::

::: pf-qed

Step [](#s1-3){.pf-ref} gives the requested maximum value and corresponding choice.

:::

:::

:::
