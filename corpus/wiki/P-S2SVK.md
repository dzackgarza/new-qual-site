---
schema: qual/card@1
id: P-S2SVK
kind: problem
title: $\bigl|\frac{d^n}{dx^n}\frac{\sin x}{x}\bigr|\le\frac1n$ for $x\neq 0$ and $n\ge 1$
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
Prove that
\[
\left| \frac{d^{n}}{d x^{n}} \frac{\sin x}{x}\right| \leq \frac{1}{n}
\]

for all $x \neq 0$ and positive integers $n$.

> Hint: Consider $\displaystyle\int_0^1 \cos(tx) dt$

:::{.solution}
:::{.concept}
- DCT
- Bounding in the right place. 
  Don't evaluate the actual integral!
:::

- By induction on the number of limits we can pass through the integral.
- For $n=1$ we first pass one derivative into the integral: let $x_n \to x$ be any sequence converging to $x$, then
\[
\dd{}{x} {\sin(x) \over x} 
&= \dd{}{x} \int_0^1 \cos(tx)\,dt  \\
&= \lim_{x_n\to x} {1\over x_n - x} \qty{ \int_0^1 \cos(t x_n)\,dt  - \int_0^1 \cos(tx) \,dt} \\
&= \lim_{x_n\to x} \qty{ \int_0^1 { \cos(tx_n)  - \cos(tx) \over x_n - x}   \,dt} \\
&= \lim_{x_n\to x} \qty{ \int_0^1 \qty{t\sin(tx)\mid_{x=\xi_n}}  \,dt} \qtext{where} \xi_n \in [x_n, x] \text{ by MVT}, \xi_n\to x \\
&= \lim_{\xi_n\to x} \qty{ \int_0^1 t \sin(t \xi_n)  \,dt}  \\
&=_{\text{DCT}}  \int_0^1 \lim_{\xi_n \to x} t \sin(t \xi_n)  \,dt \\
&= \int_0^1 t\sin(tx) \,dt \\
.\]

- Taking absolute values we obtain an upper bound 
\[
\abs{ \dd{}{x} {\sin(x) \over x} } 
&= \abs{ \int_0^1 t\sin(tx) \,dt } \\
&\leq \int_0^1 \abs{t\sin(tx)} \,dt \\
&\leq \int_0^1 1 \, dt = 1
,\]
  since $t\in [0, 1] \implies \abs{t} < 1$, and $\abs{\sin(xt)} \leq 1$ for any $x$ and $t$.

- Note that this bound also justifies the DCT, since the functions $f_n(t) = t\sin(t \xi_n )$ are uniformly dominated by $g(t) = 1$ on $L^1([0, 1])$.

> Note: integrating by parts here yields the actual formula:
\[
\int_0^1 t\sin(tx) \,dt 
&=_{\text{IBP}} \qty{-t\cos(tx) \over x}\mid_{t=0}^{t=1} - \int_0^1 {\cos(tx) \over x} \,dt \\
&= {-\cos(x) \over x} - {\sin(x) \over x^2} \\
&= {x\cos(x) - \sin(x) \over x^2}
.\]

- For the inductive step, we assume that we can pass $n-1$ limits through the integral and show we can pass the $n$th through as well.
\[
\dd{^n}{x^n} {\sin(x) \over x} 
&= \dd{^n}{x^n} \int_0^1 \cos(tx)\,dt  \\
&= \dd{}{x} \int_0^1 \dd{^{n-1}}{x^{n-1}} \cos(tx)\,dt  \\
&= \dd{}{x} \int_0^1 t^{n-1} f_{n-1}(x, t) \,dt 
\]
  - Note that $f_n(x, t) = \pm \sin(tx)$ when $n$ is odd and $f_n(x, t) = \pm \cos(tx)$ when $n$ is even, and a constant factor of $t$ is multiplied when each derivative is taken.

- We continue as in the base case:
\[
\dd{}{x} \int_0^1 t^{n-1} f_{n-1}(x, t) \,dt 
&= \lim_{x_k\to x} \int_0^1 t^{n-1} \qty{ f_{n-1}(x_n, t) - f_{n-1}(x, t) \over x_n - x} \,dt \\
&=_{\text{IVT}} \lim_{x_k\to x} \int_0^1 t^{n-1} \dd{f_{n-1}}{x}(\xi_k, t) \,dt \quad\text{where } \xi_k\in [x_k, x],\, \xi_k \to x \\
&=_{\text{DCT}} \int_0^1 \lim_{x_k\to x} t^{n-1} \dd{f_{n-1}}{x}(\xi_k, t) \,dt \\
&\definedas \int_0^1 \lim_{x_k\to x} t^{n} f_n(\xi_k, t) \,dt \\
&\definedas \int_0^1 t^{n} f_n(x, t) \,dt 
.\]
  - We've used the fact that $f_0(x) = \cos(tx)$ is smooth as a function of $x$, and in particular continuous 
  - The DCT is justified because the functions $h_{n, k}(x, t) = t^n f_n(\xi_k, t)$ are again uniformly (in $k$) bounded by 1 since $t\leq 1 \implies t^n \leq 1$ and each $f_n$ is a sin or cosine.

- Now take absolute values
\[
\abs {\dd{^n}{x^n} {\sin(x) \over x}  }
&= \abs{ \int_0^1 -t^n f_n(x, t) ~dt } \\ 
&\leq \int_0^1 \abs{t^n f_n(x, t)} ~dt \\
&\leq \int_0^1 \abs{t^n} \abs{f_n(x, t)} ~dt \\
&\leq \int_0^1 \abs{ t^n} \cdot 1 ~dt \\ 
&\leq \int_0^1 t^n ~dt \quad\text{since $t$ is positive} \\ 
&= \frac{1}{n+1} \\
&< \frac{1}{n}
.\]
  - We've again used the fact that $f_n(x, t)$ is of the form $\pm \cos(tx)$ or $\pm \sin(tx)$, both of which are bounded by 1.
:::

