---
schema: qual/card@1
id: P-RAF07C
kind: problem
title: "Smoothness and decay of an oscillatory integral"
classification:
  areas:
  - real-analysis
  topics:
  - Real Analysis
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-08
  note: Checked against Problem 3 of the official UCSD Fall 2007 real-analysis qualifying exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-08
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
---

::: problem
Let $f \in L^1(\mathbb{R})$ and put
$$
g(\xi) := \int_{\mathbb{R}} e^{i\xi \cos x} f(x)\,dx, \quad \xi \in \mathbb{R}.
$$

(a) Show that $g$ is continuous on $\mathbb{R}$.

(b) Show that $g$ is infinitely differentiable on $\mathbb{R}$ (i.e. $g \in C^\infty(\mathbb{R})$).

(c) Show that the sequence $\{g^{(n)}(\xi)\}$ converges uniformly to $0$ on $\mathbb{R}$, where $g^{(n)}(\xi)$ denotes the $n$th derivative of $g$.
:::


::: solution
<1>1. Prove continuity of $g$.
::: proof
Fix $\xi\in\mathbb R$ and let $\xi_k\to\xi$. For every $x$,
\[
e^{i\xi_k\cos x}f(x)\longrightarrow e^{i\xi\cos x}f(x),
\]
and
\[
|e^{i\xi_k\cos x}f(x)|=|f(x)|.
\]
Since $f\in L^1(\mathbb R)$, dominated convergence gives
\[
g(\xi_k)\to g(\xi).
\]
Hence $g$ is continuous.
:::

<1>2. Differentiate under the integral sign to all orders.
::: proof
For each integer $n\ge0$, define
\[
G_n(\xi,x):=(i\cos x)^n e^{i\xi\cos x}f(x).
\]
Then
\[
|G_n(\xi,x)|\le |f(x)|
\]
for every $\xi,x$. Also
\[
\frac{\partial}{\partial\xi}G_n(\xi,x)=G_{n+1}(\xi,x).
\]
Because $|G_{n+1}(\xi,x)|\le|f(x)|\in L^1$, dominated convergence applied to difference quotients justifies differentiation under the integral. Inductively,
\[
\boxed{
g^{(n)}(\xi)=\int_{\mathbb R}(i\cos x)^n e^{i\xi\cos x}f(x)\,dx.}
\]
The same dominated-convergence argument shows each $g^{(n)}$ is continuous. Thus
\[
g\in C^\infty(\mathbb R).
\]
:::

<1>3. Prove that $g^{(n)}\to0$ uniformly in $\xi$.
::: proof
For every $\xi\in\mathbb R$,
\[
|g^{(n)}(\xi)|
\le \int_{\mathbb R}|\cos x|^n|f(x)|\,dx.
\]
For almost every $x\in\mathbb R$,
\[
|\cos x|<1,
\]
because $|\cos x|=1$ only on the countable set $\pi\mathbb Z$. Hence
\[
|\cos x|^n|f(x)|\longrightarrow0
\]
for almost every $x$, while
\[
|\cos x|^n|f(x)|\le|f(x)|\in L^1.
\]
Dominated convergence therefore yields
\[
\int_{\mathbb R}|\cos x|^n|f(x)|\,dx\longrightarrow0.
\]
Since the bound is independent of $\xi$,
\[
\boxed{
\sup_{\xi\in\mathbb R}|g^{(n)}(\xi)|\longrightarrow0.}
\]
Thus $g^{(n)}\to0$ uniformly on $\mathbb R$.
:::
:::
