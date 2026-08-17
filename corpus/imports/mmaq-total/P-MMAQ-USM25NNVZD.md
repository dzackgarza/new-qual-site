---
schema: qual/card@1
id: P-MMAQ-USM25NNVZD
kind: problem
title: $\bigl|\frac{d^n}{dx^n}\frac{\sin x}{x}\bigr|\leq\frac1n$ for $x\neq 0$
classification:
  areas:
  - real-analysis
  topics:
  - integrals
  - differentiation
relations: []
review: draft
solved: true
---

::: problem
Prove that
$$
\left|\frac{d^{n}}{d x^{n}} \frac{\sin x}{x}\right| \leq \frac{1}{n}
$$

for all $x \neq 0$ and positive integers $n$.

> Hint: Consider $\displaystyle\int_0^1 \cos(tx) dt$
:::

::: {.solution}
> **AI-Generated Solution**

**Goal:** Prove $\abs{\frac{d^n}{dx^n} \frac{\sin x}{x}} \leq \frac{1}{n}$ for all $x \neq 0$ and all positive integers $n$.

<1>1. Represent $\frac{\sin x}{x}$ as an integral.
<2>1. For $x \neq 0$, $\frac{\sin x}{x} = \int_0^1 \cos(tx) ~dt$.
Proof: $\int_0^1 \cos(tx) ~dt = \left[\frac{\sin(tx)}{x}\right]_0^1 = \frac{\sin x}{x}$.
<2>2. Q.E.D. Proof: This is the identity suggested by the hint.

<1>2. Differentiate under the integral sign.
<2>1. For each $n \geq 0$ and $x \neq 0$, $$\frac{d^n}{dx^n}\frac{\sin x}{x} = \int_0^1 \frac{\partial^n}{\partial x^n} \cos(tx) ~dt = \int_0^1 t^n \cos^{(n)}(tx) ~dt,$$ where $\cos^{(n)}$ denotes the $n$-th derivative of $\cos$.
Proof: Differentiating under the integral is legitimate by induction on $n$: the integrand and its $x$-derivatives $\frac{\partial^k}{\partial x^k}\cos(tx) = t^k \cos^{(k)}(tx)$ are continuous in $(t,x)$ and bounded in absolute value by $t^k \leq 1$ on $[0,1]$, uniformly for $x$ in any compact interval avoiding $0$; the dominated convergence theorem justifies passing the derivative inside (standard differentiation-under-the-integral theorem).
<2>2. Q.E.D. Proof: The formula of <2>1 holds for every $n \geq 1$.

<1>3. Bound the derivative.
<2>1. $\abs{\cos^{(n)}(tx)} \leq 1$ for all $t, x$.
Proof: The derivatives of $\cos$ are $\pm \cos$ or $\pm \sin$, all bounded in absolute value by $1$.
<2>2. Hence $$\abs{\frac{d^n}{dx^n}\frac{\sin x}{x}} = \abs{\int_0^1 t^n \cos^{(n)}(tx) ~dt} \leq \int_0^1 t^n \cdot 1 ~dt = \frac{1}{n+1}.$$ Proof: Triangle inequality inside the integral, then <2>1 and the elementary integral $\int_0^1 t^n ~dt = 1/(n+1)$.
<2>3. $\frac{1}{n+1} \leq \frac{1}{n}$ for $n \geq 1$.
Proof: $n + 1 > n$.
<2>4. Q.E.D. Proof: By <2>2 and <2>3, $\abs{\frac{d^n}{dx^n}\frac{\sin x}{x}} \leq \frac{1}{n}$ (in fact the sharper bound $1/(n+1)$ holds).
:::
