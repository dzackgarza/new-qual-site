---
schema: qual/card@1
id: P-5QNZJ
kind: problem
title: Translation is continuous in $L^1$; $L^1*L^\infty$ convolutions are bounded
  and uniformly continuous
classification:
  areas:
  - real-analysis
  topics:
  - Convolution
  - Uniform Continuity
  - L¹
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-25
---

::: problem
1. Let $f \in C_c^0(\RR^n)$, and show
\[
\lim _{t \to 0} \int_{\RR^n} |f(x+t) - f(x)| \, dx = 0
.\]

2. Extend the above result to $f\in L^1(\RR^n)$ and show that
\[
f\in L^1(\RR^n), \quad g\in L^\infty(\RR^n) \quad
\implies f \ast g \text{ is bounded and uniformly continuous. }
\]
:::

::: {.solution}
<1>1. For $f \in C_c^0(\RR^n)$: $\lim_{t\to 0}\int_{\RR^n}|f(x + t) - f(x)|\,dx = 0$.
    <2>1. $f$ is uniformly continuous.
        Proof: $f$ is continuous with compact support.
    <2>2. $\int_{\RR^n}|f(x+t) - f(x)|\,dx \le \mu(\supp f + B(0,1))\cdot \omega_f(|t|)$ for $|t| \le 1$, where $\omega_f$ is the modulus of continuity.
        Proof: the integrand vanishes outside $\supp f + B(0,1)$, a bounded set; on it, $|f(x+t) - f(x)| \le \omega_f(|t|)$ by <2>1.
    <2>3. Q.E.D.
        Proof: $\omega_f(|t|) \to 0$ as $t \to 0$ by <2>1.

<1>2. The result extends to $f \in L^1(\RR^n)$.
    <2>1. Given $\eps > 0$, choose $g \in C_c^0$ with $\|f - g\|_1 < \eps/3$.
        Proof: continuous compactly supported functions are dense in $L^1$.
    <2>2. For small $t$: $\|\tau_t f - f\|_1 \le \|\tau_t f - \tau_t g\|_1 + \|\tau_t g - g\|_1 + \|g - f\|_1 < \eps$.
        Proof: $\|\tau_t f - \tau_t g\|_1 = \|f - g\|_1$ (translation invariance), $\|\tau_t g - g\|_1 < \eps/3$ for small $t$ by <1>1, and $\|g - f\|_1 < \eps/3$ by <2>1.

<1>3. For $f \in L^1$, $g \in L^\infty$: $f \ast g$ is bounded and uniformly continuous.
    <2>1. $|f \ast g(x)| \le \|g\|_\infty\|f\|_1$ for all $x$.
        Proof: $|f\ast g(x)| \le \int|f(x-y)||g(y)|\,dy \le \|g\|_\infty\|f\|_1$.
    <2>2. $|f \ast g(x + t) - f \ast g(x)| \le \|g\|_\infty\int|f(u + t) - f(u)|\,du \to 0$ as $t \to 0$, uniformly in $x$.
        Proof: substitute $u = x - y$ and use <1>2.
    <2>3. Q.E.D.
        Proof: <2>1 and <2>2.
:::
