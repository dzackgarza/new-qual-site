---
schema: qual/card@1
id: P-GJIZI
kind: problem
title: $L^1$ functions are finite a.e., absolutely summable series in $L^1$, and a
  dominated-convergence limit
classification:
  areas:
  - real-analysis
  topics:
  - L¹
  - Series of Functions
  - Convergence of Integrals
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-17
---

::: {.problem}
a. Show that $f\in L^1(\RR^n) \implies \abs{f(x)} < \infty$ almost everywhere.

b. Show that if $\ts{f_k} \subseteq L^1(\RR^n)$ with $\sum \norm{f_k}_1 < \infty$ then $\sum f_k$ converges almost everywhere and in $L^1$.

c. Use the Dominated Convergence Theorem to evaluate
\[
\lim_{t\to 0} \int_0^1 {e^{tx^2} - 1 \over t} \dx
.\]
:::
::: {.solution}
<1>1. If $f \in L^1(\RR^n)$, then $|f(x)| < \infty$ for a.e. $x$.

::: {.proof}
For every $M > 0$, $\theset{|f| = \infty} \subseteq \theset{|f| \ge M}$, and Markov's inequality gives $m\theset{|f| \ge M} \le \|f\|_1/M$. Letting $M \to \infty$ shows $m\theset{|f| = \infty} = 0$.
:::

<1>2. If $f_k \in L^1(\RR^n)$ and $\sum_k \|f_k\|_1 < \infty$, then $\sum_k f_k$ converges a.e. and in $L^1$.

<2>1. $g = \sum_k |f_k|$ is in $L^1$, and $g < \infty$ a.e.

::: {.proof}
By the monotone convergence theorem applied to the partial sums, $\int g = \sum_k \|f_k\|_1 < \infty$. Step <1>1 applied to $g$ gives $g < \infty$ a.e.
:::

<2>2. Q.E.D.

::: {.proof}
Where $g(x) < \infty$, the series $\sum_k f_k(x)$ converges absolutely; call its sum $F(x)$, and put $F = 0$ elsewhere. Then $|F| \le g$, so $F \in L^1$, and $\left\|F - \sum_{k=1}^N f_k\right\|_1 \le \int \sum_{k > N}|f_k| = \sum_{k>N}\|f_k\|_1 \to 0$.
:::

<1>3. $\lim_{t \to 0}\int_0^1 \frac{e^{tx^2} - 1}{t}\,dx = \boxed{\tfrac{1}{3}}$.

<2>1. For $0 < |t| \le 1$ and $x \in [0,1]$, $\left|\frac{e^{tx^2} - 1}{t}\right| \le e$.

::: {.proof}
By the mean value theorem, $e^u - 1 = e^\xi u$ for some $\xi$ between $0$ and $u$, so $|e^u - 1| \le e|u|$ for $|u| \le 1$. Take $u = tx^2$.
:::

<2>2. $\frac{e^{tx^2} - 1}{t} \to x^2$ as $t \to 0$ for each $x$.

::: {.proof}
This is the derivative of $t \mapsto e^{tx^2}$ at $t = 0$.
:::

<2>3. Q.E.D.

::: {.proof}
By steps <2>1 and <2>2, dominated convergence with dominating function $e$ on $[0,1]$ gives the limit $\int_0^1 x^2\,dx = \frac13$ along every sequence $t_k \to 0$.
:::
:::
