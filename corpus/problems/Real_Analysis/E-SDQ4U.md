---
schema: qual/card@1
id: E-SDQ4U
kind: problem
title: $L^p$ inclusions on finite measure spaces and $\ell^p$ inclusions on $\mathbb{Z}$
classification:
  areas:
  - real-analysis
  topics:
  - Lp Spaces
  - L∞
  - L¹
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-17
---

::: {.exercise}
- Prove the following inclusions of $L^p$ spaces for $m(X) < \infty$:
\[
L^\infty(X) &\subset L^2(X) \subset L^1(X) \\
\ell^2(\ZZ) &\subset \ell^1(\ZZ) \subset \ell^\infty(\ZZ)
.\]
:::

::: {.solution}

::: pf

::: {.pf-step #s1}
If $m(X) < \infty$, then $L^\infty(X) \subseteq L^2(X) \subseteq L^1(X)$.

::: pf-proof

::: {.pf-step #s1-1}
$\|f\|_1 \le m(X)^{1/2}\|f\|_2$ for $f \in L^2(X)$.

::: pf-proof
By the Cauchy--Schwarz inequality, $\int|f| = \int |f|\cdot 1 \le \|f\|_2\|1\|_2 = \|f\|_2\, m(X)^{1/2}$.
:::

:::

::: {.pf-step #s1-2}
$\|f\|_2 \le m(X)^{1/2}\|f\|_\infty$ for $f \in L^\infty(X)$.

::: pf-proof
$\int|f|^2 \le \|f\|_\infty^2\, m(X)$.
:::

:::

::: {.pf-step #s1-3}
On $[0,1]$ with Lebesgue measure, $x^{-1/2} \in L^1 \setminus L^2$ and $\log x \in L^2 \setminus L^\infty$.

::: pf-proof
$\int_0^1 x^{-1/2}\,dx = 2$ and $\int_0^1 x^{-1}\,dx = \infty$. Also $\int_0^1 (\log x)^2\,dx = 2$ and $\log x$ is unbounded near $0$.
:::

:::

::: pf-qed
Steps [](#s1-1){.pf-ref} and [](#s1-2){.pf-ref} give the inclusions, and step [](#s1-3){.pf-ref} shows that they are strict.
:::

:::

:::

::: {.pf-step #s2}
For counting measure on $\ZZ$, $\ell^1(\ZZ) \subseteq \ell^2(\ZZ) \subseteq \ell^\infty(\ZZ)$, with strict inclusions.

::: pf-proof

::: {.pf-step #s2-1}
If $\sum_n |a_n| < \infty$ then $\sum_n |a_n|^2 < \infty$.

::: pf-proof
The terms of a convergent series tend to $0$, so $|a_n| \le 1$ for all but finitely many $n$, and for those $n$, $|a_n|^2 \le |a_n|$.
:::

:::

::: {.pf-step #s2-2}
If $\sum_n |a_n|^2 < \infty$ then $|a_n| \le \|a\|_2$ for every $n$.

::: pf-proof
$|a_n|^2 \le \sum_k |a_k|^2$.
:::

:::

::: {.pf-step #s2-3}
$a_n = 1/|n|$ ($n \neq 0$) is in $\ell^2 \setminus \ell^1$, and $a_n = 1/\sqrt{|n|}$ ($n \neq 0$) is in $\ell^\infty \setminus \ell^2$; set $a_0 = 0$ in both.

::: pf-proof
$\sum_{n \geq 1} 1/n$ diverges and $\sum_{n \geq 1} 1/n^2$ converges, and $\sup_n |n|^{-1/2} = 1$.
:::

:::

::: pf-qed
Steps [](#s2-1){.pf-ref} through [](#s2-3){.pf-ref}.
:::

:::

:::

::: pf-qed
Step [](#s1){.pf-ref} proves the first line of the display. Step [](#s2){.pf-ref} proves the second line with $\ell^1$ and $\ell^2$ exchanged; by step [](#s2-3){.pf-ref}, the inclusion $\ell^2(\ZZ) \subset \ell^1(\ZZ)$ printed in the problem is false.
:::

:::

:::

::: {.remark}
Erratum: the second line of the display should read $\ell^1(\ZZ) \subset \ell^2(\ZZ) \subset \ell^\infty(\ZZ)$. On a finite measure space the $L^p$ spaces decrease as $p$ increases, and for counting measure on $\ZZ$ the $\ell^p$ spaces increase as $p$ increases.
:::
