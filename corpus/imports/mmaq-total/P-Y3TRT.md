---
schema: qual/card@1
id: P-Y3TRT
kind: problem
title: 'Let g : $[0, 1] \times [0, 1] \to [0, 1]$ be a continuous function…'
classification:
  areas:
  - real-analysis
  topics:
  - sequences-of-functions
  - arzela-ascoli
relations: []
review: draft
---

::: problem
Let g : $[0, 1] \times [0, 1] \to [0, 1]$ be a continuous function and let $\{f_n\}$ be a sequence of functions such that

$$f_n(x)=\begin{cases}{0,   0\leq x\leq 1/n},\\{\int_0^{x-\frac1n} g(t,f_n(t))dt, 1/n\leq x \leq 1.}\end{cases}$$

With the help of the Arzela-Ascoli theorem or otherwise, show that there exists a continuous function $f : [0, 1] \to \mathbb{R}$ such that

$f(x) = \int_0^x g(t, f(t))dt$

for all $x \in [0, 1]$.

> Hint: first show that $|f_n(x_1) - f_n(x_2)| \leq |x_1 - x_2|$.
:::

::: {.solution}
> **AI-Generated Solution**

**Goal:** Using Arzelà–Ascoli, show there is a continuous $f : [0,1] \to \mathbb{R}$ with $f(x) = \int_0^x g(t, f(t)) \, dt$ for all $x \in [0,1]$, where $g : [0,1]^2 \to [0,1]$ is continuous and $f_n$ is the recursively defined sequence in the statement.

<1>1. The sequence $\{f_n\}$ is well defined, and $0 \leq f_n(x) \leq 1$ for all $n$ and all $x \in [0,1]$.
    <2>1. Each $f_n$ is well defined and continuous.
        Proof: on $[0, 1/n]$, $f_n \equiv 0$. On $[j/n, (j+1)/n]$ the integrand $g(t, f_n(t))$ is evaluated only at $t \leq x - 1/n \leq j/n$, i.e. at values of $f_n$ already defined on $[0, j/n]$, so the recursion is well founded and defines $f_n$ continuously piece by piece (integrals of continuous functions are continuous, and the pieces agree at the seams since the integrals start at $0$).
    <2>2. $0 \leq f_n(x) \leq x - \frac1n \leq 1$ for $x \geq \frac1n$; hence $0 \leq f_n \leq 1$ everywhere.
        Proof: $g \geq 0$ gives $f_n \geq 0$; $g \leq 1$ gives $f_n(x) = \int_0^{x - 1/n} g \leq \int_0^{x - 1/n} 1 = x - \frac1n \leq 1$.

<1>2. Each $f_n$ is $1$-Lipschitz: $|f_n(x_1) - f_n(x_2)| \leq |x_1 - x_2|$.
    <2>1. For $1/n \leq x_1 \leq x_2$: $|f_n(x_2) - f_n(x_1)| = \left|\int_{x_1 - 1/n}^{x_2 - 1/n} g(t, f_n(t)) \, dt\right| \leq x_2 - x_1$.
        Proof: $|g| \leq 1$, and the interval of integration has length $x_2 - x_1$.
    <2>2. For $x_1 < 1/n \leq x_2$: $|f_n(x_2) - f_n(x_1)| = |f_n(x_2)| \leq x_2 - \frac1n \leq x_2 - x_1$.
        Proof: $f_n(x_1) = 0$ by definition on $[0, 1/n]$, and $|f_n(x_2)| \leq x_2 - 1/n$ by <1>2<2>2.
    <2>3. For $x_2 < 1/n$, both values are $0$. Hence the Lipschitz bound holds in all cases (take $x_1 \leq x_2$).
        Proof: <2>1–<2>3 cover the three possible positions of $x_1, x_2$ relative to $1/n$.

<1>3. Arzelà–Ascoli gives a subsequence $f_{n_k} \to f$ uniformly on $[0,1]$, with $f$ continuous.
    Proof: $\{f_n\}$ is uniformly bounded by $1$ (<1>1) and equicontinuous (<1>2: a common Lipschitz constant), so Arzelà–Ascoli applies on the compact interval $[0,1]$.

<1>4. The limit $f$ satisfies $f(x) = \int_0^x g(t, f(t)) \, dt$ for every $x$.
    <2>1. $g(t, f_{n_k}(t)) \to g(t, f(t))$ uniformly in $t$.
        Proof: $g$ is uniformly continuous on the compact square $[0,1]^2$, and $f_{n_k} \to f$ uniformly (<1>3).
    <2>2. For each fixed $x \in (0,1]$: $\int_0^{x - 1/n_k} g(t, f_{n_k}(t)) \, dt \to \int_0^x g(t, f(t)) \, dt$.
        Proof: for $k$ large, $1/n_k \leq x$. Then $\left|\int_0^{x - 1/n_k} g(t, f_{n_k}(t))\,dt - \int_0^x g(t, f(t))\,dt\right| \leq \int_0^{x - 1/n_k} |g(t, f_{n_k}(t)) - g(t, f(t))|\,dt + \int_{x - 1/n_k}^x |g(t, f(t))|\,dt \leq \sup_t |g(t, f_{n_k}(t)) - g(t, f(t))| + \frac1{n_k}$, which tends to $0$ by <2>1 and the width $\frac1{n_k} \to 0$.
    <2>3. For $x = 0$: $f_{n_k}(0) = 0 = \int_0^0 g$, and $f(0) = \lim_k f_{n_k}(0) = 0$, so the equation holds at $0$ too.
        Proof: direct from the definition of $f_n$ and <1>3.
    <2>4. $f(x) = \int_0^x g(t, f(t)) \, dt$ for all $x \in [0,1]$.
        Proof: for $x > 0$, $f_{n_k}(x) = \int_0^{x - 1/n_k} g(t, f_{n_k}(t))\,dt$ (for $k$ large) converges to both $f(x)$ (uniform convergence) and $\int_0^x g(t, f(t))\,dt$ (<2>2); limits are unique. For $x = 0$, <2>3.
    <2>5. Q.E.D.
        Proof: <1>3 gives continuity of $f$ and <2>4 gives the integral equation, establishing existence.
:::
