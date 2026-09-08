---
schema: qual/card@1
id: P-RASP08D
kind: problem
title: "Banach limit extension of Cesaro mean functional"
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
  note: Checked against Problem 4 of the official UCSD Spring 2008 real-analysis qualifying exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-08
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
---

::: problem
Let $\ell^\infty$ denote the Banach space of all bounded real-valued functions on $\mathbb{N}$, and $f_n$ the bounded linear functional
$$
f_n(x) := \frac{x(1) + \ldots + x(n)}{n}.
$$
Let $M \subset \ell^\infty$ be the subspace of all $x$ such that $\lim_{n \to \infty} f_n(x)$ exists, and $f$ the linear functional $M \to \mathbb{R}$ given by $f(x) := \lim_{n \to \infty} f_n(x)$.

(a) Let $\tau : \ell^\infty \to \ell^\infty$ denote the shift operator given by $(\tau x)(n) = x(n+1)$ for $n = 1, 2, \ldots$.
Show that $\tau$ sends $M$ to $M$ and $f(\tau x) = f(x)$ for all $x \in M$.

(b) Show that there is a linear functional $F : \ell^\infty \to \mathbb{R}$ such that $F|_M = f$ and
$$
\liminf_{n \to \infty} x(n) \leq F(x) \leq \limsup_{n \to \infty} x(n).
$$
:::


::: solution
<1>1. Prove shift invariance of the Cesaro-limit subspace.
::: proof
For $x\in\ell^\infty$,
\[
\begin{aligned}
f_n(\tau x)-f_n(x)
&=\frac{x(2)+\cdots+x(n+1)}n-rac{x(1)+\cdots+x(n)}n\\
&=\frac{x(n+1)-x(1)}n.
\end{aligned}
\]
Since $x$ is bounded, the right-hand side tends to $0$. Therefore, whenever $f_n(x)$ converges, $f_n(\tau x)$ converges to the same limit. Thus
\[
\tau(M)\subseteq M
\]
and
\[
\boxed{f(\tau x)=f(x)\qquad(x\in M).}
\]
:::

<1>2. Define the sublinear dominating functional.
::: proof
For $x\in\ell^\infty$, set
\[
p(x):=\limsup_{n\to\infty}x(n).
\]
Then for $x,y\in\ell^\infty$ and $\lambda\ge0$,
\[
p(x+y)\le p(x)+p(y),
\qquad
p(\lambda x)=\lambda p(x),
\]
so $p$ is sublinear.

If $x\in M$ and
\[
f(x)=\lim_{n\to\infty}\frac1n\sum_{k=1}^n x(k)=L,
\]
then
\[
\liminf_{n\to\infty}x(n)\le L\le\limsup_{n\to\infty}x(n).
\]
Indeed, for every $\varepsilon>0$, all sufficiently late terms satisfy
\[
x(n)\le p(x)+\varepsilon,
\]
and the finitely many earlier terms contribute $o(1)$ to the Cesaro averages; hence $L\le p(x)$. Applying this to $-x$ gives the lower bound. In particular,
\[
f(x)\le p(x)
\qquad(x\in M).
\]
:::

<1>3. Apply the Hahn--Banach theorem.
::: proof
By the real Hahn--Banach theorem in dominated form, there exists a linear functional
\[
F:\ell^\infty\to\mathbb R
\]
such that
\[
F|_M=f
\qquad\text{and}\qquad
F(x)\le p(x)=\limsup_{n\to\infty}x(n)
\]
for every $x\in\ell^\infty$.

Applying this upper bound to $-x$ gives
\[
-F(x)=F(-x)
\le \limsup_{n\to\infty}(-x(n))
=-\liminf_{n\to\infty}x(n).
\]
Therefore
\[
\liminf_{n\to\infty}x(n)\le F(x)\le\limsup_{n\to\infty}x(n).
\]
Hence
\[
\boxed{
F|_M=f,
\qquad
\liminf x(n)\le F(x)\le\limsup x(n)
}
\]
for every bounded real sequence $x$.
:::
:::
