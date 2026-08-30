---
schema: qual/card@1
id: E-SS6.PR-1
kind: exercise
title: "This problem provides further estimates for  and  near"
classification:
  areas:
  - complex-analysis
  topics:
  - Riemann Zeta
relations: []
review: draft
audit:
- event: solution-written
  by: Codex 5.3 Spark Extra High
  date: 2026-08-30
---

::: exercise
1. This problem provides further estimates for $\zeta$ and $\zeta ^ { \prime }$ near $\operatorname { R e } ( s ) = 1$

(a) Use Proposition 2.5 and its corollary to prove

$$
\zeta (s) = \sum_ {1 \leq n <   N} n ^ {- s} - \frac {N ^ {s - 1}}{s - 1} + \sum_ {n \geq N} \delta_ {n} (s)
$$

for every integer $N \geq 2$ , whenever $\operatorname { R e } ( s ) > 0$

(b) Show that $| \zeta ( 1 + i t ) | = O ( \log | t | )$ , as $| t |  \infty$ by using the previous result with N =greatest integer in $| t | .$

(c) The second conclusion of Proposition 2.7 can be similarly refined.

(d) Show that if $t \neq 0$ and t is fixed, then the partial sums of the series $\textstyle \sum _ { n = 1 } ^ { \infty } 1 / n ^ { 1 + i t }$ are bounded, but the series does not converge.

2.∗ Prove that for $\operatorname { R e } ( s ) > 0$

$$
\zeta (s) = \frac {s}{s - 1} - s \int_ {1} ^ {\infty} \frac {\{x \}}{x ^ {s + 1}} d x
$$

where $\{ x \}$ is the fractional part of $x .$

3.∗ If $Q ( x ) = \{ x \} - 1 / 2$ , then we can write the expression in the previous problem as

$$
\zeta (s) = \frac {s}{s - 1} - \frac {1}{2} - s \int_ {1} ^ {\infty} \frac {Q (x)}{x ^ {s + 1}} d x.
$$

Let us construct $Q _ { k } ( x )$ recursively so that

$$
\int_ {0} ^ {1} Q _ {k} (x) d x = 0, \quad \frac {d Q _ {k + 1}}{d x} = Q _ {k} (x), \quad Q _ {0} (x) = Q (x) \quad \text { and } \quad Q _ {k} (x + 1) = Q _ {k} (x).
$$

Then we can write

$$
\zeta (s) = \frac {s}{s - 1} - \frac {1}{2} - s \int_ {1} ^ {\infty} \left(\frac {d ^ {k}}{d x ^ {k}} Q _ {k} (x)\right) x ^ {- s - 1} d x,
$$
:::

::: solution
**Goal:** Give the boundary formulas and growth bounds near $\Re(s)=1$.

<1>1. Part (a): Abel expansion.
    *Proof:*  
    For $\Re(s)>0$, fix $N\ge2$ and set
    $$\delta_n(s):=n^{-s}-\int_n^{n+1}x^{-s}\,dx.$$
    Then
    \begin{align*}
    \zeta(s)
    &=\sum_{n=1}^{N-1}n^{-s}+\sum_{n=N}^\infty n^{-s}\\
    &=\sum_{n=1}^{N-1}n^{-s}
      +\sum_{n=N}^\infty\int_n^{n+1}x^{-s}\,dx+\sum_{n=N}^\infty\delta_n(s)\\
    &=\sum_{n=1}^{N-1}n^{-s}+\int_N^\infty x^{-s}\,dx+\sum_{n=N}^\infty\delta_n(s)\\
    &=\sum_{n=1}^{N-1}n^{-s}-\frac{N^{s-1}}{s-1}+\sum_{n=N}^\infty\delta_n(s),
    \end{align*}
    since $\int_N^\infty x^{-s}\,dx=-N^{s-1}/(s-1)$.

<1>2. Part (b): bound for $\zeta(1+it)$.
    *Proof:*  
    Let $s=1+it$ and choose $N=\lfloor|t|\rfloor+1$.
    From (1),
    \[
    \zeta(1+it)=\sum_{n=1}^{N-1}n^{-1-it}-\frac{N^{it}}{it}+\sum_{n=N}^\infty\delta_n(1+it).
    \]
    We have
    \[
    \sum_{n< N}\frac1n=\log N+O(1).
    \]
    Also
    \[
    |\delta_n(1+it)|\le\int_n^{n+1}|n^{-1-it}-x^{-1-it}|\,dx\le \frac{C}{n^2},
    \]
    so the tail is absolutely convergent and bounded. Hence
    $|\zeta(1+it)|\ll\log N+1=O(\log|t|)$.

<1>3. Part (c): derivative refinement.
    *Proof:*  
    Differentiate the identity in (1) for $\Re(s)>1$:
    \[
    \zeta'(s)=-\frac1{(s-1)^2}-\sum_{n=1}^{N-1}n^{-s}\log n+\sum_{n=N}^\infty \delta_n'(s),
    \]
    with
    \[
    \delta_n'(s)=\frac{d}{ds}\!\left(n^{-s}-\int_n^{n+1}x^{-s}\,dx\right).
    \]
    At $s=1+it$ and $N\asymp|t|$, the first sum is $O((\log|t|)^2)$ and
    $\sum_{n=N}^\infty\delta_n'(1+it)=O(1)$, so $\zeta'(1+it)=O((\log|t|)^2)$.

<1>4. Part (d): bounded but nonconvergent partial sums.
    *Proof:*  
    Let $S_m(t)=\sum_{n=1}^m n^{-1-it}$. Apply (1) with $N=m+1$:
    \[
    \zeta(1+it)=S_m(t)-\frac{(m+1)^{it}}{it}+\sum_{n=m+1}^\infty\delta_n(1+it).
    \]
    Therefore
    $$S_m(t)=\zeta(1+it)+\frac{(m+1)^{it}}{it}+O(1).$$
    The tail is bounded uniformly in $m$, so $(S_m(t))$ is bounded.
    If $S_m(t)$ converged, then $(m+1)^{it}$ would converge as $m\to\infty$, impossible
    for fixed $t\ne0$.

<1>5. Part (2): first integral representation.
    *Proof:*  
    On $\Re(s)>0$,
    \[
    \zeta(s)=\sum_{n=1}^\infty n^{-s}
    =\sum_{n=1}^\infty\int_n^{n+1}\lfloor x\rfloor^{-s}\,dx
    =\int_1^\infty \lfloor x\rfloor^{-s}\,dx.
    \]
    Since $\lfloor x\rfloor=x-\{x\}$ and $\int_1^\infty x^{-s}dx=\frac1{s-1}$,
    \[
    \zeta(s)=\frac{s}{s-1}-s\int_1^\infty\frac{\{x\}}{x^{s+1}}\,dx.
    \]

<1>6. Part (3): recursive periodic refinement.
    *Proof:*  
    Write $\{x\}=Q(x)+\frac12$ to get
    \[
    \zeta(s)=\frac{s}{s-1}-\frac12-s\int_1^\infty Q(x)x^{-s-1}\,dx.
    \]
    With $\int_0^1Q_k=0$, $Q_{k+1}'=Q_k$, and $Q_k(x+1)=Q_k(x)$,
    integrate by parts repeatedly to obtain
    \[
    \zeta(s)=\frac{s}{s-1}-\frac12-s\int_1^\infty \frac{d^kQ_k}{dx^k}(x)\,x^{-s-1}\,dx.
    \]
:::
