---
schema: qual/card@1
id: P-RA16M5
kind: problem
title: 'UGA analysis qualifying exam, May 2016, problem 5'
classification:
  areas:
  - real-analysis
  topics:
  - convergence-of-functions
  - uniform-convergence
relations: []
review: draft
solved: true
---

::: {.problem title="?"}
Let $$f_n(x)=n^\beta x(1-x^2)^n,\qquad x\in[0,1],\ n\in\mathbb N.$$

(a) Prove that $\{f_n\}_{n=1}^{\infty}$ converges point-wise on $[0,1]$ for every $\beta\in\mathbb R$.

(b) Show that the convergence in part (a) is uniform on $[0,1]$ for all $\beta<\frac12$, but not uniform for any $\beta\ge\frac12$.
:::

:::: {.solution}
> **AI-Generated Solution** **Goal:** For $f_n(x) = n^\beta x(1-x^2)^n$ on $[0,1]$: (a) pointwise convergence for every $\beta$; (b) uniform iff $\beta < \frac12$.

<1>1. (a) $f_n(x) \to 0$ pointwise for every $x \in [0,1]$ and every $\beta$.
<2>1. At $x = 0$: $f_n(0) = 0$ for all $n$.
<2>2. At $x = 1$: $f_n(1) = n^\beta \cdot 1 \cdot 0^n = 0$ for all $n$ (with $0^n = 0$ for $n \ge 1$). <2>3. For $x \in (0,1)$: $f_n(x) = n^\beta x (1-x^2)^n \to 0$.
Proof: $0 < 1 - x^2 < 1$, so $(1-x^2)^n$ decays exponentially while $n^\beta$ grows polynomially; exponential decay beats polynomial growth, so $n^\beta(1-x^2)^n \to 0$, and the factor $x$ is fixed.
<2>4. Q.E.D. Proof: <2>1–<2>3 cover all $x \in [0,1]$.

<1>2. (b) Uniform convergence on $[0,1]$ holds exactly when $\beta < \frac12$.
<2>1. Compute $\|f_n\|_\infty = n^\beta \max_{x \in [0,1]} x(1-x^2)^n$.
<2>2. The maximum of $x(1-x^2)^n$ on $[0,1]$ occurs at $x = \frac{1}{\sqrt{2n+1}}$ with value $\frac{1}{\sqrt{2n+1}}\left(1 - \frac{1}{2n+1}\right)^n$.
Proof: $g(x) = x(1-x^2)^n$, $g'(x) = (1-x^2)^n - 2nx^2(1-x^2)^{n-1} = (1-x^2)^{n-1}(1 - (2n+1)x^2)$; zero at $x^2 = 1/(2n+1)$.
<2>3. $\|f_n\|_\infty = n^\beta \cdot \frac{1}{\sqrt{2n+1}}\left(1 - \frac{1}{2n+1}\right)^n \sim n^{\beta - 1/2} \cdot \frac{1}{\sqrt2} e^{-1/2}$.
Proof: $(1 - 1/(2n+1))^n \to e^{-1/2}$ and $1/\sqrt{2n+1} \sim 1/\sqrt{2n}$.
<2>4. If $\beta < \frac12$: $\|f_n\|_\infty \sim Cn^{\beta - 1/2} \to 0$, so $f_n \to 0$ uniformly.
Proof: <2>3 with $\beta - 1/2 < 0$.
<2>5. If $\beta \ge \frac12$: $\|f_n\|_\infty \not\to 0$ ($n^{\beta-1/2} \ge 1$), so convergence is not uniform.
Proof: <2>3: the sup norm is bounded below by a positive constant (or diverges), so the uniform limit cannot be $0$; but the pointwise limit is $0$ by <1>1, and a uniform limit must equal the pointwise limit.
<2>6. Q.E.D. Proof: <2>4 and <2>5 give the exact threshold.
:::
