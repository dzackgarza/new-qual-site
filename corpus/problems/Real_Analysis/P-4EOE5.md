---
schema: qual/card@1
id: P-4EOE5
kind: problem
title: Lebesgue regularity, invariance of the integral, convolution, and $L^p$ norms
classification:
  areas:
  - real-analysis
  topics:
  - Measure Theory
  - Integrals
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-17
---

::: {.problem}
- $\star$: Show that for $E\subseteq \RR^n$, TFAE: 
  1. $E$ is measurable
  2. $E = H\union Z$ here $H$ is $F_\sigma$ and $Z$ is null
  3. $E = V\setminus Z'$ where $V\in G_\delta$ and $Z'$ is null.
- $\star$: Show that if $E\subseteq \RR^n$ is measurable then $m(E) = \sup \theset{ m(K) \suchthat K\subset E\text{ compact}}$ iff for all $\eps> 0$ there exists a compact $K\subseteq E$ such that $m(K) \geq m(E) - \eps$.
- $\star$: Show that cylinder functions are measurable, i.e. if $f$ is measurable on $\RR^s$, then $F(x, y) \definedas f(x)$ is measurable on $\RR^s\cross \RR^t$ for any $t$.
- $\star$: Prove that the Lebesgue integral is translation invariant, i.e. if $\tau_h(x) = x+h$ then $\int \tau_h f = \int f$.
- $\star$: Prove that the Lebesgue integral is dilation invariant, i.e. if $f_\delta(x) = {f({x\over \delta}) \over \delta^n}$ then $\int f_\delta = \int f$.
- $\star$: Prove continuity in $L^1$, i.e.
  \[
  f \in L^{1} \Longrightarrow \lim _{h \rightarrow 0} \int|f(x+h)-f(x)|=0
  .\]
- $\star$: Show that $$f,g \in L^1 \implies f\ast g \in L^1 \qtext{and} \norm{f\ast g}_1 \leq \norm{f}_1 \norm{g}_1.$$

- $\star$: Show that if $X\subseteq \RR$ with $\mu(X) < \infty$ then
\[  
\norm{f}_p \converges{p\to\infty}\to \norm{f}_\infty
.\]
:::

::: {.solution}
Let $m$ be Lebesgue measure.

<1>1. $E \subseteq \RR^n$ is measurable if and only if $E = H \cup Z$ with $H$ an $F_\sigma$ set and $Z$ null, if and only if $E = V \setminus Z'$ with $V$ a $G_\delta$ set and $Z'$ null.

::: {.proof}
If $E$ is measurable, outer regularity gives open $G_k \supseteq E$ and, applied to $E^c$, closed $F_k \subseteq E$ with $m(G_k \setminus E) < 1/k$ and $m(E \setminus F_k) < 1/k$. Then $H = \bigcup_k F_k$ and $V = \bigcap_k G_k$ satisfy $m(E \setminus H) = 0$ and $m(V \setminus E) = 0$. Conversely $F_\sigma$ and $G_\delta$ sets are Borel and null sets are measurable. See [[E-D75O4]].
:::

<1>2. $m(E) = \sup\theset{m(K) : K \subseteq E \text{ compact}}$ if and only if for every $\eps > 0$ there is a compact $K \subseteq E$ with $m(K) \ge m(E) - \eps$.

::: {.proof}
$m(E)$ is an upper bound of $\theset{m(K) : K \subseteq E \text{ compact}}$ by monotonicity. It is the least upper bound exactly when no $m(E) - \eps$ with $\eps > 0$ is an upper bound, which is the stated condition. See [[E-3OAGD]].
:::

<1>3. If $f$ is Lebesgue measurable on $\RR^s$, then $F(x,y) = f(x)$ is Lebesgue measurable on $\RR^s \times \RR^t$.

::: {.proof}
For an open $W \subseteq \RR$, $F^{-1}(W) = f^{-1}(W) \times \RR^t$ with $f^{-1}(W)$ Lebesgue measurable. Write $f^{-1}(W) = V \setminus Z$ with $V$ a $G_\delta$ set and $Z$ null by step <1>1. Then $V \times \RR^t$ is Borel and $Z \times \RR^t$ is null, so $F^{-1}(W)$ is measurable. See [[E-JJ746]].
:::

<1>4. $\int f(x+h)\,dx = \int f$ and $\int \delta^{-n}f(x/\delta)\,dx = \int f$ for $f \geq 0$ measurable or $f \in L^1$.

::: {.proof}
For $f = \chi_E$ these are $m(E - h) = m(E)$ and $\delta^{-n}m(\delta E) = m(E)$. Linearity extends them to simple functions, the monotone convergence theorem to measurable $f \geq 0$, and the decomposition $f = f^+ - f^-$ to $L^1$. See [[E-QFOPP]] and [[E-KVDIA]].
:::

<1>5. For $f \in L^1(\RR^n)$, $\lim_{h\to 0}\int|f(x+h) - f(x)|\,dx = 0$.

::: {.proof}
For the indicator of a bounded box $I$, the integral is $m(I \triangle (I - h))$, which tends to $0$. Finite linear combinations of such indicators are dense in $L^1$, and by step <1>4 translation preserves $L^1$ distances, so for such a combination $s$ with $\|f - s\|_1 < \eps$, $\int|f(x+h) - f(x)|\,dx < 2\eps + \int|s(x+h) - s(x)|\,dx$. See [[E-F6IXU]].
:::

<1>6. If $f, g \in L^1$, then $f \ast g \in L^1$ and $\|f \ast g\|_1 \le \|f\|_1\|g\|_1$.

::: {.proof}
By Tonelli's theorem and step <1>4, $\iint |f(x-y)||g(y)|\,dy\,dx = \|f\|_1\|g\|_1 < \infty$. So $f\ast g(x)$ is defined for a.e. $x$ by Fubini's theorem, and $\int|f\ast g| \le \iint |f(x-y)||g(y)|\,dy\,dx$. See [[E-DUWXR]].
:::

<1>7. If $\mu(X) < \infty$, then $\|f\|_p \to \|f\|_\infty$ as $p \to \infty$.

::: {.proof}
If $\mu(X) = 0$ both sides vanish. Otherwise $\|f\|_p \le \|f\|_\infty\,\mu(X)^{1/p} \to \|f\|_\infty$, and for $0 < M < \|f\|_\infty$ the set $\theset{|f| > M}$ has positive finite measure, so $\|f\|_p \ge M\mu\theset{|f|>M}^{1/p} \to M$. See [[E-TVBUC]].
:::

<1>8. Q.E.D.

::: {.proof}
Steps <1>1--<1>7 treat the parts in order.
:::
:::
