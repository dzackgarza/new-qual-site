---
schema: qual/card@1
id: P-RA-WORKSHOP-D7-13
kind: problem
title: A trigonometric integral limit
classification:
  areas:
  - real-analysis
  topics:
  - Convergence of Integrals
  - Integrals
relations: []
review: draft
---

::: {.problem}
(June 2007 #4b part i) Evaluate $$\lim_{n\to\infty}\int_{\pi/2}^{\pi}\frac{n\sin(x/n)}{x}\,dx$$ and justify your reasoning.
:::

:::: {.solution}
> **AI-Generated Solution** **Goal:** Evaluate $\lim_{n\to\infty}\int_{\pi/2}^{\pi}\frac{n\sin(x/n)}{x}\,dx$.

<1>1. The answer is $\pi/2$.
<2>1. Pointwise limit: for each fixed $x \in [\pi/2, \pi]$, $\frac{n\sin(x/n)}{x} \to 1$.
Proof: $\frac{n\sin(x/n)}{x} = \frac{\sin(x/n)}{x/n} \to \frac{\sin 0}{0}\text{-form} = 1$ since $\lim_{t \to 0} \sin t / t = 1$ and $x/n \to 0$.
<2>2. Domination: $\left|\frac{n\sin(x/n)}{x}\right| \le 1$ on $[\pi/2, \pi]$ for all $n \ge 1$.
Proof: $\frac{n\sin(x/n)}{x} = \frac{\sin(x/n)}{x/n}$ with $0 \le x/n \le \pi$ (as $x \le \pi$, $n \ge 1$). For $0 \le t \le \pi$, $\sin t / t \le 1$ (standard: $\sin t \le t$ on $[0,\infty)$), and $\sin(x/n) \ge 0$ since $x/n \in [0, \pi]$.
So $0 \le \frac{\sin(x/n)}{x/n} \le 1$.
<2>3. Q.E.D. Proof: Dominated Convergence: by <2>1 and <2>2, $\lim_n \int_{\pi/2}^\pi \frac{n\sin(x/n)}{x}\,dx = \int_{\pi/2}^\pi 1\,dx = \pi - \pi/2 = \pi/2$.
:::
