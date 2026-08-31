---
schema: qual/card@1
id: P-FPWV6
kind: problem
title: Examples - a false converse, continuous not differentiable, separate continuity, non-Cauchy bounded sequence, and a series converging exactly on $[0,2]$
classification:
  areas:
  - prelim
  topics:
  - Counterexamples
  - Differentiation
  - Continuity
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: {.problem}
Provide examples of the following.
[No justification is required.]

a) a true implication whose converse is false,

b) a function $f: \mathbb{R} \to \mathbb{R}$ which is continuous at $7$, but not differentiable there,

c) a function $f: \mathbb{R}^2 \to \mathbb{R}$ which is continuous in each variable separately, but is not continuous at $(0,0)$,

d) a bounded sequence which is not Cauchy,

e) a (real) power series whose domain of convergence is the closed interval $[0,2]$.
:::

::: {.solution}
<1>1. Part (a): A true implication whose converse is false:
<2>1. Consider the statement for an integer $n \in \mathbb{Z}$:
\[
P(n) \implies Q(n), \quad \text{where } P(n) \text{ is } ``4 \mid n" \text{ and } Q(n) \text{ is } ``2 \mid n".
\]
If $4 \mid n$, then $n = 4k = 2(2k)$, so $2 \mid n$, which is a true implication.
<2>2. The converse $Q(n) \implies P(n)$ is false, as witnessed by the counterexample $n = 2$: $2 \mid 2$ is true, but $4 \mid 2$ is false.

<1>2. Part (b): Continuous at $7$ but not differentiable at $7$:
<2>1. Define $f: \mathbb{R} \to \mathbb{R}$ by:
\[
f(x) = |x - 7|.
\]
$f$ is continuous on $\mathbb{R}$ as the composition of continuous functions.
<2>2. Compute the one-sided derivative difference quotients at $x = 7$:
\[
\lim_{h \to 0^+} \frac{f(7+h) - f(7)}{h} = \lim_{h \to 0^+} \frac{|h|}{h} = 1, \qquad \lim_{h \to 0^-} \frac{f(7+h) - f(7)}{h} = \lim_{h \to 0^-} \frac{-h}{h} = -1.
\]
Because the left and right limits do not agree, $f'(7)$ does not exist.

<1>3. Part (c): Separately continuous on $\mathbb{R}^2$ but not continuous at $(0, 0)$:
<2>1. Define $f: \mathbb{R}^2 \to \mathbb{R}$ by:
\[
f(x, y) = \begin{cases} \dfrac{xy}{x^2 + y^2} & (x, y) \neq (0, 0), \\ 0 & (x, y) = (0, 0). \end{cases}
\]
<2>2. For any fixed $y_0$, $x \mapsto f(x, y_0)$ is continuous on $\mathbb{R}$ (at $x = 0$, $f(x, 0) = 0$ for all $x$, so $\lim_{x\to 0} f(x, 0) = 0 = f(0, 0)$).
Symmetrically, for any fixed $x_0$, $y \mapsto f(x_0, y)$ is continuous on $\mathbb{R}$.
Thus $f$ is separately continuous in each variable.
<2>3. Along the line $y = x$, for $x \neq 0$:
\[
f(x, x) = \frac{x^2}{x^2 + x^2} = \frac{1}{2}.
\]
Thus $\lim_{x \to 0} f(x, x) = \frac{1}{2} \neq 0 = f(0, 0)$, so $f$ is not continuous at $(0, 0)$.

<1>4. Part (d): A bounded sequence that is not Cauchy:
<2>1. Consider the sequence $(a_n)_{n=1}^\infty$ defined by $a_n = (-1)^n$.
Then $|a_n| = 1 \le 1$ for all $n$, so the sequence is bounded.
<2>2. For any $n \in \mathbb{N}$, $|a_{n+1} - a_n| = |(-1)^{n+1} - (-1)^n| = 2$.
Taking $\varepsilon = 1$, there is no $N$ such that $|a_n - a_m| < 1$ for all $n, m \ge N$.
Thus $(a_n)$ is not Cauchy.

<1>5. Part (e): A real power series whose domain of convergence is $[0, 2]$:
<2>1. Define the power series centered at $c = 1$:
\[
S(x) = \sum_{n=1}^\infty \frac{(x - 1)^n}{n^2}.
\]
<2>2. The radius of convergence $R$ satisfies:
\[
\frac{1}{R} = \lim_{n \to \infty} \left| \frac{1}{n^2} \right|^{1/n} = 1 \implies R = 1.
\]
Thus the series converges absolutely for $|x - 1| < 1$ (i.e. $x \in (0, 2)$) and diverges for $|x - 1| > 1$.
<2>3. At the endpoints:
- For $x = 2$: $\sum_{n=1}^\infty \frac{1^n}{n^2} = \sum_{n=1}^\infty \frac{1}{n^2}$, which converges (a $p$-series with $p = 2 > 1$).
- For $x = 0$: $\sum_{n=1}^\infty \frac{(-1)^n}{n^2}$, which converges absolutely by comparison to $\sum \frac{1}{n^2}$.
Therefore the exact interval of convergence is the closed interval $[0, 2]$.

<1>6. Conclusion:
All five requested examples are defined and verified. Q.E.D.
:::
