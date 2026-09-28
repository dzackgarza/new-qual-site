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
<1>1. If $m(X) < \infty$, then $L^\infty(X) \subseteq L^2(X) \subseteq L^1(X)$.

<2>1. $\|f\|_1 \le m(X)^{1/2}\|f\|_2$ for $f \in L^2(X)$.

::: {.proof}
By the Cauchy--Schwarz inequality, $\int|f| = \int |f|\cdot 1 \le \|f\|_2\|1\|_2 = \|f\|_2\, m(X)^{1/2}$.
:::

<2>2. $\|f\|_2 \le m(X)^{1/2}\|f\|_\infty$ for $f \in L^\infty(X)$.

::: {.proof}
$\int|f|^2 \le \|f\|_\infty^2\, m(X)$.
:::

<2>3. On $[0,1]$ with Lebesgue measure, $x^{-1/3} \in L^1 \setminus L^2$ and $\log x \in L^2 \setminus L^\infty$.

::: {.proof}
$\int_0^1 (\log x)^2\,dx = 2$ and $\log x$ is unbounded near $0$.
:::

<2>4. Q.E.D.

::: {.proof}
Steps <2>1 and <2>2 give the inclusions, and step <2>3 shows that they are strict.
:::

<1>2. For counting measure on $\ZZ$, $\ell^1(\ZZ) \subseteq \ell^2(\ZZ) \subseteq \ell^\infty(\ZZ)$, with strict inclusions.

<2>1. If $\sum_n |a_n| < \infty$ then $\sum_n |a_n|^2 < \infty$.

::: {.proof}
The terms of a convergent series tend to $0$, so $|a_n| \le 1$ for all but finitely many $n$, and for those $n$, $|a_n|^2 \le |a_n|$.
:::

<2>2. If $\sum_n |a_n|^2 < \infty$ then $|a_n| \le \|a\|_2$ for every $n$.

::: {.proof}
$|a_n|^2 \le \sum_k |a_k|^2$.
:::

<2>3. $a_n = 1/|n|$ ($n \neq 0$) is in $\ell^2 \setminus \ell^1$, and $a_n = 1/\sqrt{|n|}$ ($n \neq 0$) is in $\ell^\infty \setminus \ell^2$; set $a_0 = 0$ in both.

::: {.proof}
$\sum_{n \geq 1} 1/n$ diverges and $\sum_{n \geq 1} 1/n^2$ converges, and $\sup_n |n|^{-1/2} = 1$.
:::

<2>4. Q.E.D.

::: {.proof}
Steps <2>1--<2>3.
:::

<1>3. Q.E.D.

::: {.proof}
Step <1>1 proves the first line of the display. Step <1>2 proves the second line with $\ell^1$ and $\ell^2$ exchanged; by step <1>2 <2>3, the inclusion $\ell^2(\ZZ) \subset \ell^1(\ZZ)$ printed in the problem is false.
:::
:::

::: {.remark}
Erratum: the second line of the display should read $\ell^1(\ZZ) \subset \ell^2(\ZZ) \subset \ell^\infty(\ZZ)$. On a finite measure space the $L^p$ spaces decrease as $p$ increases, and for counting measure on $\ZZ$ the $\ell^p$ spaces increase as $p$ increases.
:::
