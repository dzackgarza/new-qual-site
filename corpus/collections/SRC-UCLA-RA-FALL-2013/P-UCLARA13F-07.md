---
schema: qual/card@1
id: P-UCLARA13F-07
kind: problem
title: Density under a weighted mean-zero constraint
classification:
  areas:
  - real-analysis
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Transcribed from the UCLA Analysis Qualifying Exam Solutions compendium, Fall 2013 section.
---

::: {.problem}
Show that the set of functions $f\in L^2([0,1])$ such that $x\mapsto x^{-1/2}f(x)$ lies in $L^1([0,1])$ and
\[
\int_0^1 x^{-1/2}f(x)\,dx=0
\]
is dense in $L^2([0,1])$.
:::

::: {.solution}
Let $\mathcal D$ denote the set in the problem. It suffices to approximate functions supported away from $0$, while correcting their weighted integral by functions of arbitrarily small $L^2$ norm concentrated near $0$.

<1>1. The subspace
\[
\mathcal S=\{g\in L^2([0,1]):g=0\text{ a.e. on }[0,\varepsilon]\text{ for some }\varepsilon>0\}
\]
is dense in $L^2([0,1])$.

::: {.proof}
For $h\in L^2([0,1])$, set
\[
h_N=h\,\mathbf1_{[1/N,1]}.
\]
Then $h_N\in\mathcal S$ and
\[
\|h-h_N\|_2^2
=\int_0^{1/N}|h(x)|^2\,dx\to0
\]
by absolute continuity of the Lebesgue integral.
:::

<1>2. Every $g\in\mathcal S$ satisfies
\[
x^{-1/2}g(x)\in L^1([0,1]).
\]

::: {.proof}
Choose $\varepsilon>0$ such that $g=0$ on $[0,\varepsilon]$. On $[\varepsilon,1]$, one has $x^{-1/2}\leq\varepsilon^{-1/2}$. Since the interval has finite measure, $L^2\subset L^1$, so
\[
\int_0^1x^{-1/2}|g(x)|\,dx
\leq\varepsilon^{-1/2}\|g\|_1<\infty.
\]
:::

<1>3. For $N\geq2$, define
\[
\phi_N(x)=\frac{x^{-1/2}\mathbf1_{[1/N,1]}(x)}{\log N}.
\]
Then
\[
\int_0^1x^{-1/2}\phi_N(x)\,dx=1
\]
and
\[
\|\phi_N\|_2^2=\frac1{\log N}.
\]

::: {.proof}
Indeed,
\[
\int_0^1x^{-1/2}\phi_N(x)\,dx
=\frac1{\log N}\int_{1/N}^1\frac{dx}{x}=1.
\]
Similarly,
\[
\|\phi_N\|_2^2
=\frac1{(\log N)^2}\int_{1/N}^1\frac{dx}{x}
=\frac1{\log N}.
\]
Also $x^{-1/2}\phi_N\in L^1$ by the same computation.
:::

<1>4. Thus
\[
\|\phi_N\|_2\longrightarrow0
\]
while every $\phi_N$ has weighted integral $1$.

::: {.proof}
This is immediate from step <1>3 because $1/\log N\to0$.
:::

<1>5. Fix $g\in\mathcal S$ and set
\[
c=\int_0^1x^{-1/2}g(x)\,dx.
\]
Define
\[
g_N=g-c\phi_N.
\]
Then $g_N\in\mathcal D$.

::: {.proof}
By steps <1>2 and <1>3, both $x^{-1/2}g$ and $x^{-1/2}\phi_N$ are integrable, so the same is true for $g_N$. Moreover,
\[
\int_0^1x^{-1/2}g_N(x)\,dx
=c-c\cdot1=0.
\]
Thus $g_N$ satisfies both defining conditions of $\mathcal D$.
:::

<1>6. One has
\[
\|g_N-g\|_2=|c|\,\|\phi_N\|_2\longrightarrow0.
\]

::: {.proof}
By definition $g_N-g=-c\phi_N$, and step <1>4 gives the limit.
:::

<1>7. Therefore $\mathcal D$ is dense in $L^2([0,1])$.

::: {.proof}
Step <1>1 says $\mathcal S$ is dense in $L^2$. Steps <1>5--<1>6 show every $g\in\mathcal S$ lies in the $L^2$ closure of $\mathcal D$. Hence the closure of $\mathcal D$ contains the dense set $\mathcal S$, so it is all of $L^2([0,1])$.
:::

<1>8. Q.E.D.

::: {.proof}
Step <1>7 is the required density statement.
:::
:::
