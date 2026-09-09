---
schema: qual/card@1
id: P-RASP04F
kind: problem
title: "Multiplication operators on L^2 and bounded convergence"
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
  note: Checked against Problem 6 of the official UCSD Spring 2004 real-analysis qualifying exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-08
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
---

::: problem
Suppose $f : X \to [-1,1]$ is a measurable function and $\varphi : [-1,1] \to \mathbb{R}$ is a bounded Borel measurable function.
Show:

(a) $\|M_{\varphi \circ f}\|_{B(L^2(\mu))} \leq \|\varphi\|_u := \sup_{|x| \leq 1} |\varphi(x)|$.

(b) Suppose $\varphi_n : [-1,1] \to \mathbb{R}$ are bounded Borel measurable functions converging boundedly to $\varphi$.
Then for all $h \in L^2(\mu)$,
$$
L^2(\mu)\text{-}\lim_{n \to \infty} M_{\varphi_n \circ f}\,h = M_{\varphi \circ f}\,h.
$$

(c) Show by example that it is possible that $\lim_{n \to \infty} \|M_{\varphi_n \circ f}\|_{B(L^2(\mu))} \neq 0$ even though $\varphi_n \to 0$ boundedly.
:::

::: solution
<1>1. Bound the multiplication operator.
::: proof
For $h\in L^2(\mu)$,
\[
\begin{aligned}
\|M_{\varphi\circ f}h\|_2^2
&=\int_X |\varphi(f(x))|^2|h(x)|^2\,d\mu(x)\\
&\le \|\varphi\|_u^2\|h\|_2^2.
\end{aligned}
\]
Therefore
\[
\boxed{\|M_{\varphi\circ f}\|\le \|\varphi\|_u.}
\]
:::

<1>2. Prove strong convergence under bounded pointwise convergence.
::: proof
Assume $\varphi_n(t)\to\varphi(t)$ for every $t\in[-1,1]$ and that
\[
\sup_n\|\varphi_n\|_u\le C<\infty.
\]
Then $|\varphi|\le C$ as well. For fixed $h\in L^2(\mu)$,
\[
\begin{aligned}
\|M_{\varphi_n\circ f}h-M_{\varphi\circ f}h\|_2^2
&=\int_X |\varphi_n(f(x))-\varphi(f(x))|^2|h(x)|^2\,d\mu(x).
\end{aligned}
\]
The integrand converges pointwise to $0$ and is bounded by
\[
4C^2|h(x)|^2,
\]
which is integrable. By the Dominated Convergence Theorem,
\[
\boxed{M_{\varphi_n\circ f}h\to M_{\varphi\circ f}h\text{ in }L^2.}
\]
:::

<1>3. Strong convergence need not imply convergence in operator norm.
::: proof
Take
\[
X=[0,1],\qquad \mu=m,\qquad f(x)=x,
\]
and define
\[
\varphi_n(t)=\mathbf1_{(0,1/n)}(t),
\qquad -1\le t\le1.
\]
Then $|\varphi_n|\le1$ and $\varphi_n(t)\to0$ for every $t$, so $\varphi_n\to0$ boundedly.

However,
\[
M_{\varphi_n\circ f}=M_{\mathbf1_{(0,1/n)}}.
\]
Its operator norm is $1$: Step 1 gives the upper bound, while for
\[
h_n=\frac{\mathbf1_{(0,1/n)}}{\sqrt{m((0,1/n))}}
\]
we have $\|h_n\|_2=1$ and
\[
M_{\varphi_n\circ f}h_n=h_n.
\]
Thus
\[
\boxed{\|M_{\varphi_n\circ f}\|=1\quad\text{for every }n,}
\]
even though $\varphi_n\to0$ boundedly.
:::
:::
