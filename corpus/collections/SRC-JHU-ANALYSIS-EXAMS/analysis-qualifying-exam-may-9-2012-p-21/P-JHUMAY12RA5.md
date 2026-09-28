---
schema: qual/card@1
id: P-JHUMAY12RA5
kind: problem
title: 'Weak and strong convergence of squares in $L^2$'
classification:
  areas:
  - real-analysis
  topics:
  - Lp Spaces
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: {.problem}
Justify or give a counterexample to the following assertions:

(a) If $\{f_i\}$ is a sequence in $L^2([0,1])$ converging weakly to $f$ in $L^2([0,1])$ then $f_i^2$ converges weakly to $f^2$ in $L^1([0,1])$.

(b) If $\{f_i\}$ is a sequence in $L^2([0,1])$ converging strongly to $f$ in $L^2([0,1])$, then $f_i^2$ converges strongly to $f^2$ in $L^1([0,1])$.
:::

::: {.solution}
<1>1. Assertion (a) is false: the sequence
$$
f_n(x)=\sin(2\pi n x)
$$
converges weakly to $0$ in $L^2([0,1])$.

::: {.proof}
For $g\in L^2([0,1])$, finite measure gives $g\in L^1([0,1])$. Hence the [[PR-IGMH4|Riemann--Lebesgue lemma]] gives
$$
\int_0^1 f_n(x)g(x)\,dx
=\int_0^1 \sin(2\pi n x)g(x)\,dx
\longrightarrow0.
$$
Thus $f_n\rightharpoonup0$ in $L^2([0,1])$.
:::

<1>2. The squares in step <1>1 do not converge weakly to $0$ in $L^1([0,1])$.

::: {.proof}
The constant function $1$ belongs to $L^\infty([0,1])=(L^1([0,1]))^*$, and
$$
\int_0^1 f_n(x)^2\,dx
=\int_0^1\sin^2(2\pi n x)\,dx
=\frac12
$$
for every $n$. Since the weak limit asserted in part (a) would be $0^2=0$, testing against $1$ gives a contradiction.
:::

<1>3. Assertion (b) is true: if $f_i\to f$ strongly in $L^2([0,1])$, then
$$
\norm{f_i^2-f^2}_{L^1}\longrightarrow0.
$$

::: {.proof}
The sequence $(f_i)$ is bounded in $L^2$, so there is $M<\infty$ with $\norm{f_i}_{L^2}\le M$ for every $i$. By the [[FF-4XBYG|Cauchy--Schwarz inequality in $L^2$]],
$$
\begin{aligned}
\norm{f_i^2-f^2}_{L^1}
&=\int_0^1 \abs{f_i-f}\,\abs{f_i+f}\,dx\\
&\le \norm{f_i-f}_{L^2}\norm{f_i+f}_{L^2}\\
&\le \qty{M+\norm{f}_{L^2}}\norm{f_i-f}_{L^2}
\longrightarrow0.
\end{aligned}
$$
:::

<1>4. Q.E.D.

::: {.proof}
Steps <1>1 and <1>2 give the counterexample required for part (a), and step <1>3 proves part (b).
:::
:::
