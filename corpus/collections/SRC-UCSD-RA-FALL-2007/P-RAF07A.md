---
schema: qual/card@1
id: P-RAF07A
kind: problem
title: "True/false on convergence, operators, and compactness"
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
  note: Checked against Problem 1 of the official UCSD Fall 2007 real-analysis qualifying exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-08
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
---

::: problem
True or false.
For each part, determine if it is always true or sometimes false.
If true give a brief proof.
If false give a counterexample or disprove it.
No credit if reason is missing or incorrect.

(a) If $f : \mathbb{R} \to \mathbb{R}$ is continuous with $f \in L^1(\mathbb{R}, m)$, then $\lim_{x \to \infty} f(x) = 0$.

(b) If $f : \mathbb{R} \to \mathbb{R}$ is a continuously differentiable function with $f, f' \in L^1(\mathbb{R}, m)$, then $\lim_{x \to \infty} f(x) = 0$.

(c) If $\{f_n\}$ is a sequence of Lebesgue integrable functions on $[0,1]$ such that $f_n$ converges to $0$ in $L^1([0,1], m)$, then there exists a Lebesgue measurable set $E \subset [0,1]$ with $m(E) > 0$ such that $\lim_{n \to \infty} f_n(x) = 0$ for all $x \in E$.

(d) If $X$ and $Y$ are Banach spaces and $T : X \to Y$ is a linear mapping for which $f \circ T \in X^*$ for all $f \in Y^*$, then $T$ is bounded.

(e) If $\alpha > 0$ and $\{f_n\}$ a sequence of functions on $[0,1]$ for which
$$
|f_n(x) - f_n(y)| \leq |x - y|^\alpha \quad \text{and} \quad f_n(0) = 0 \;\forall n,\; \forall x, y \in [0,1],
$$
then there exists a subsequence $\{f_{n_j}\}$ that converges uniformly on $[0,1]$.
:::

::: solution
<1>1. Part (a) is false.
::: proof
For each integer $n\ge1$, let $\phi_n$ be the triangular function supported on
\[
[n-2^{-n-2},\,n+2^{-n-2}]
\]
with $\phi_n(n)=1$ and linear on each side of $n$. The supports are disjoint. Define
\[
f:=\sum_{n=1}^\infty \phi_n.
\]
Then $f$ is continuous and
\[
\int_{\mathbb R}|f(x)|\,dx
=\sum_{n=1}^\infty \int\phi_n
=\sum_{n=1}^\infty 2^{-n-2}<\infty.
\]
Thus $f\in L^1(\mathbb R)$, but
\[
f(n)=1
\]
for every $n$, so $f(x)$ does not tend to $0$ as $x\to\infty$.
:::

<1>2. Part (b) is true.
::: proof
For $y>x$,
\[
|f(y)-f(x)|
\le \int_x^y |f'(t)|\,dt.
\]
Since $f'\in L^1(\mathbb R)$, the right-hand side is uniformly small when $x,y$ are sufficiently large. Hence $f(x)$ has a finite limit $L$ as $x\to\infty$.

If $L\ne0$, then for sufficiently large $x$,
\[
|f(x)|\ge \frac{|L|}{2},
\]
which would force
\[
\int_{\mathbb R}|f|=\infty.
\]
Since $f\in L^1$, necessarily
\[
\boxed{\lim_{x\to\infty}f(x)=0.}
\]
:::

<1>3. Part (c) is false.
::: proof
Enumerate the dyadic intervals level by level. For each $k\ge1$ and $0\le j<2^k$, let
\[
I_{k,j}=[j2^{-k},(j+1)2^{-k})
\]
except that the last interval at each level includes $1$. Let $(I_n)$ be the resulting sequence and set
\[
f_n:=\mathbf1_{I_n}.
\]
At level $k$, every such interval has length $2^{-k}$, so
\[
\|f_n\|_1\longrightarrow0.
\]
Thus $f_n\to0$ in $L^1([0,1])$.

However, every $x\in[0,1]$ belongs to exactly one dyadic interval at each level. Hence $f_n(x)=1$ for infinitely many $n$. It is also $0$ for infinitely many $n$, because each level has more than one interval. Therefore $f_n(x)$ fails to converge to $0$ for every $x\in[0,1]$. In particular there is no positive-measure set on which the full sequence converges pointwise to $0$.
:::

<1>4. Part (d) is true.
::: proof
We show that the graph of $T$ is closed. Suppose
\[
x_n\to x\quad\text{in }X,
\qquad
Tx_n\to y\quad\text{in }Y.
\]
For every $f\in Y^*$, the assumption gives $f\circ T\in X^*$. Hence
\[
f(Tx_n)=(f\circ T)(x_n)\longrightarrow(f\circ T)(x)=f(Tx).
\]
But also continuity of $f$ on $Y$ gives
\[
f(Tx_n)\longrightarrow f(y).
\]
Thus
\[
f(y)=f(Tx)
\]
for every $f\in Y^*$. By Hahn--Banach, continuous linear functionals separate points of $Y$, so $y=Tx$. Therefore the graph of $T$ is closed.

Since $X$ and $Y$ are Banach spaces, the Closed Graph Theorem implies that $T$ is bounded.
:::

<1>5. Part (e) is true.
::: proof
Taking $y=0$ gives
\[
|f_n(x)|=|f_n(x)-f_n(0)|\le |x|^\alpha\le1,
\]
so the family is uniformly bounded. The common Hölder estimate
\[
|f_n(x)-f_n(y)|\le |x-y|^\alpha
\]
makes it equicontinuous on the compact interval $[0,1]$.

By the Arzelà--Ascoli theorem, $(f_n)$ has a uniformly convergent subsequence.
:::
:::
