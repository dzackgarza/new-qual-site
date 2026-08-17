---
schema: qual/card@1
id: E-UYQED
kind: exercise
title: "- Prove that uniform convergence implies pointwise convergence implies\u2026"
classification:
  areas:
  - real-analysis
  topics:
  - uniform-convergence
  - convergence-of-functions
  - series-of-functions
relations: []
review: draft
solved: true
---

::: exercise
- Prove that uniform convergence implies pointwise convergence implies a.e. convergence, but none of the implications may be reversed.

- Show that $\sum {x^n \over n!}$ converges uniformly on any compact subset of $\RR$.
:::

::: {.solution}
> **AI-Generated Solution**

<1>1. Uniform convergence implies pointwise convergence.
Proof: $\sup_x|f_n(x) - f(x)| \to 0$ forces $|f_n(x) - f(x)| \to 0$ for each fixed $x$.

<1>2. Pointwise convergence implies a.e. convergence.
Proof: if $f_n(x) \to f(x)$ for every $x$, then in particular for every $x$ outside any null set.

<1>3. Pointwise convergence need not be uniform.
<2>1. Take $f_n(x) = x^n$ on $[0,1]$.
Proof: standard example.
<2>2. $f_n \to f$ pointwise, where $f = 0$ on $[0,1)$ and $f(1) = 1$.
Proof: $x^n \to 0$ for $0 \le x < 1$, and $1^n = 1$.
<2>3. The convergence is not uniform.
Proof: each $f_n$ is continuous but $f$ is discontinuous, and a uniform limit of continuous functions is continuous (<1>2 of the companion card); directly, $\sup_{[0,1]}|f_n - f| \ge (1 - 1/n)^n \approx e^{-1} \not\to 0$.
<2>4. Q.E.D. Proof: <2>2 and <2>3.

<1>4. A.e. convergence need not be pointwise.
<2>1. Take $f_n = \chi_{[0, 1/n)}$ on $[0,1]$.
Proof: standard example.
<2>2. $f_n \to 0$ a.e. Proof: for every $x > 0$, $f_n(x) = 0$ once $1/n \le x$, so $f_n(x) \to 0$; only the null set $\{0\}$ is excluded.
<2>3. $f_n$ does not converge pointwise to $0$: $f_n(0) = 1$ for every $n$.
Proof: $0 \in [0, 1/n)$ for all $n$.
<2>4. Q.E.D. Proof: <2>2 and <2>3.

<1>5. $\sum_{n=0}^\infty \frac{x^n}{n!}$ converges uniformly on every compact subset of $\RR$.
<2>1. Let $K \subseteq [-M, M]$ be compact; then $\left|\frac{x^n}{n!}\right| \le \frac{M^n}{n!}$ on $K$.
Proof: $|x| \le M$ on $K$.
<2>2. $\sum_{n=0}^\infty \frac{M^n}{n!} = e^M < \infty$.
Proof: the exponential series converges, e.g. by the ratio test ($\frac{M^{n+1}/(n+1)!}{M^n/n!} = \frac{M}{n+1} \to 0 < 1$). <2>3. Q.E.D. Proof: Weierstrass M-test from <2>1 and <2>2.
:::
