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

::: problem
a. Show that $f\in L^1(\RR^n) \implies \abs{f(x)} < \infty$ almost everywhere.

b. Show that if $\ts{f_k} \subseteq L^1(\RR^n)$ with $\sum \norm{f_k}_1 < \infty$ then $\sum f_k$ converges almost everywhere and in $L^1$.

c. Use the Dominated Convergence Theorem to evaluate
\[
\lim_{t\to 0} \int_0^1 {e^{tx^2} - 1 \over t} \dx
.\]
:::
::: {.solution}
<1>1. (a) $f \in L^1(\RR^n) \Rightarrow |f(x)| < \infty$ for a.e. $x$.
    ::: {.proof}
    $\{x : |f(x)| = \infty\} = \bigcap_{M} \{x : |f(x)| \ge M\}$ has measure $0$: else $m\{|f| \ge M\} \ge \delta > 0$ for all $M$, giving $\int |f| \ge M\delta \to \infty$, contradicting $f \in L^1$. More directly: $\int |f| < \infty$ forces $\{|f| = \infty\}$ null (Markov: $m\{|f| \ge M\} \le \|f\|_1/M \to 0$).
    :::

<1>2. (b) If $\ts{f_k} \subseteq L^1$ with $\sum \|f_k\|_1 < \infty$, then $\sum f_k$ converges a.e. and in $L^1$.
    <2>1. Let $g_N = \sum_{k=1}^N |f_k|$; then $g_N \uparrow g := \sum_k |f_k|$ with $\int g = \sum_k \|f_k\|_1 < \infty$ (monotone convergence).
        ::: {.proof}
        monotone convergence theorem applied to the nonnegative increasing $g_N$.
        :::
    <2>2. $g(x) < \infty$ for a.e. $x$, and $\sum_k f_k(x)$ converges absolutely, hence converges, for those $x$.
        ::: {.proof}
        <2>1 gives $g \in L^1$, so $g < \infty$ a.e. by (a); absolute convergence implies convergence.
        :::
    <2>3. $\sum_{k=1}^N f_k \to \sum_{k=1}^\infty f_k$ in $L^1$.
        ::: {.proof}
        $\left\|\sum_{k=N+1}^\infty f_k\right\|_1 \le \sum_{k=N+1}^\infty \|f_k\|_1 \to 0$ (tail of a convergent series), and the limit function is in $L^1$ with $\int \sum_k f_k = \sum_k \int f_k$ (dominated by $g$).
        :::

<1>3. (c) $\lim_{t \to 0}\int_0^1 \frac{e^{tx^2} - 1}{t}\,dx = \frac{1}{3}$: the integrand converges pointwise to $x^2$, and dominated convergence applies.
    <2>1. For $t \to 0$ (say $|t| \le 1$) and $x \in [0,1]$: $\left|\frac{e^{tx^2} - 1}{t}\right| \le e\,x^2 \le e$.
        ::: {.proof}
        for $|u| \le 1$, $|e^u - 1| \le e^{|u|}|u| \le e|u|$ (MVT: $e^u - 1 = e^\xi u$ with $|\xi| \le |u| \le 1$, so $|e^u - 1| \le e|u|$); with $u = tx^2$ this gives $\le e x^2 \le e$.
        :::
    <2>2. $\frac{e^{tx^2} - 1}{t} \to x^2$ pointwise as $t \to 0$.
        ::: {.proof}
        $e^{tx^2} = 1 + tx^2 + o(t)$.
        :::
    <2>3. Q.E.D.
        ::: {.proof}
        dominated convergence with the dominating function $e \in L^1[0,1]$: $\lim_{t\to0}\int_0^1 \frac{e^{tx^2}-1}{t}\,dx = \int_0^1 x^2\,dx = \frac13$.
        :::
:::
