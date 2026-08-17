---
schema: qual/card@1
id: P-RA-WORKSHOP-D7-11
kind: problem
title: 'Integrals of uniformly convergent continuous functions with a moving endpoint'
classification:
  areas:
  - real-analysis
  topics:
  - uniform-convergence
  - convergence-of-integrals
relations: []
review: draft
solved: true
---

::: {.problem title="?"}
(January 2005 #3b) Suppose $f_n:[0,1]\to\mathbb R$ are continuous functions converging uniformly to $f:[0,1]\to\mathbb R$.
Either prove that $$\lim_{n\to\infty}\int_{1/n}^1f_n(x)\,dx=\int_0^1f(x)\,dx$$ or give a counterexample.
:::

:::: {.solution}
> **AI-Generated Solution** **Goal:** Prove $\lim_{n\to\infty}\int_{1/n}^1 f_n(x)\,dx = \int_0^1 f(x)\,dx$ given $f_n \to f$ uniformly, all $f_n, f$ continuous on $[0,1]$.

<1>1. $\int_0^{1/n} f_n \to 0$ as $n \to \infty$.
Proof: $|\int_0^{1/n} f_n| \le \int_0^{1/n}|f_n| \le \frac1n \sup|f_n|$.
The $f_n$ are uniformly bounded: uniform convergence to the continuous (hence bounded) $f$ makes $\sup|f_n| \le \|f\|_\infty + 1$ eventually.
So $|\int_0^{1/n} f_n| \le \frac{1}{n}(\|f\|_\infty + 1) \to 0$.

<1>2. $\int_{1/n}^1 f_n \to \int_0^1 f$.
Proof: $\int_{1/n}^1 f_n = \int_0^1 f_n - \int_0^{1/n} f_n$.
By <1>1 the subtracted term vanishes, and $\int_0^1 f_n \to \int_0^1 f$ by uniform convergence (interchange of limit and integral): $|\int_0^1 (f_n - f)| \le \|f_n - f\|_\infty \to 0$.

<1>3. Q.E.D. Proof: <1>2 is the claim.
:::
