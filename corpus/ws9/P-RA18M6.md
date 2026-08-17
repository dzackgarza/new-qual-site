---
schema: qual/card@1
id: P-RA18M6
kind: problem
title: 'UGA analysis qualifying exam, May 2018, problem 6'
classification:
  areas:
  - real-analysis
  topics:
  - uniform-convergence
  - continuity
  - counterexamples
relations: []
review: draft
solved: true
---

::: {.problem title="?"}
Let $f:\mathbb R\to\mathbb R$ be a continuous function, and for all $n\ge 1$ put $f_n(x)=f\left(x+\frac1n\right)$.

(a) Show that $f_n$ converges uniformly, as $n\to\infty$, over any closed interval $[a,b]$.

(b) Give an example of a continuous function $f$ for which the convergence is not uniform on $\mathbb R$.
:::

:::: {.solution}
> **AI-Generated Solution** **Goal:** (a) $f_n(x) = f(x + 1/n)$ converges uniformly to $f$ on any closed interval $[a,b]$; (b) give a continuous $f$ for which convergence is not uniform on $\mathbb R$.

<1>1. (a) $f_n \to f$ uniformly on $[a,b]$.
<2>1. $f$ is uniformly continuous on the enlarged interval $[a-1, b+1]$.
Proof: $f$ is continuous on the compact set $[a-1, b+1]$, hence uniformly continuous there.
For $x \in [a,b]$ and $n \ge 1$, both $x$ and $x + 1/n$ lie in $[a-1, b+1]$.
<2>2. Given $\varepsilon > 0$, uniform continuity gives $\delta > 0$ with $|u - v| < \delta \Rightarrow |f(u) - f(v)| < \varepsilon$ on $[a-1, b+1]$.
<2>3. Choose $N$ with $1/N < \delta$.
For $n \ge N$ and all $x \in [a,b]$: $|f_n(x) - f(x)| = |f(x + 1/n) - f(x)| < \varepsilon$, since $|(x+1/n) - x| = 1/n \le 1/N < \delta$.
Proof: <2>2 with $u = x + 1/n$, $v = x$.
<2>4. Q.E.D. Proof: <2>3 shows $\sup_{[a,b]}|f_n - f| \le \varepsilon$ for $n \ge N$: uniform convergence on $[a,b]$.

<1>2. (b) Example: $f(x) = \sin(x^2)$; the convergence is not uniform on $\mathbb R$.
<2>1. $f$ is continuous on $\mathbb R$.
<2>2. For each fixed $n$, $\sup_{x \in \mathbb R}|f(x + 1/n) - f(x)| \ge 1$.
Proof: set $x_k = \sqrt{2\pi k + \pi/2}$ so that $f(x_k) = \sin(2\pi k + \pi/2) = 1$.
Then with $y_k := x_k - 1/n$ (large $k$ so $y_k > 0$), $f_n(y_k) = f(y_k + 1/n) = f(x_k) = 1$, while $f(y_k) = f(x_k - 1/n) = \sin\left(\left(x_k - \frac1n\right)^2\right) = \sin\left(2\pi k + \frac{\pi}{2} - \frac{2x_k}{n} + \frac{1}{n^2}\right)$.
The sequence $\theta_k := \frac{2x_k}{n} - \frac{1}{n^2}$ is dense modulo $2\pi$ (its increments $\theta_{k+1} - \theta_k = \frac{2}{n}(\sqrt{2\pi(k+1)+\pi/2} - \sqrt{2\pi k + \pi/2}) \to 0$ while $\theta_k \to \infty$), so there are $k$ with $\theta_k \equiv \frac{\pi}{2} \pmod{2\pi}$ up to an arbitrarily small error; at such $k$, $f(y_k) \approx \sin(2\pi k + \pi/2 - \pi/2) = \sin(2\pi k) = 0$, giving $|f_n(y_k) - f(y_k)| \approx 1$.
Hence $\sup_x|f_n(x) - f(x)| \ge 1 - o(1) > 0$: the sup norms do not tend to $0$.
<2>3. Q.E.D. Proof: <2>2 shows $\|f_n - f\|_\infty \not\to 0$ on $\mathbb R$, so convergence is not uniform there, while part (a) guarantees uniform convergence on every compact interval.
(The mechanism: $f$ is not uniformly continuous on $\mathbb R$ — its derivative $2x\cos(x^2)$ is unbounded — so the fixed shift $1/n$ produces $O(1)$-sized differences far out.)
:::
