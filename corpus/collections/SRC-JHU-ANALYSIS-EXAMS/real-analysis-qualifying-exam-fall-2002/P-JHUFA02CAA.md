---
schema: qual/card@1
id: P-JHUFA02CAA
kind: problem
title: "A continuous nowhere differentiable function built from the triangle wave"
classification:
  areas:
  - real-analysis
  topics:
  - Uniform Convergence
  - Continuous Functions
  - Nowhere Differentiable Functions
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Problem 1 of the preserved JHU Fall 2002 Real Analysis qualifying exam packet.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

1. Let $\psi ( x ) = x$ on $[ 0 , \frac { 1 } { 2 } ] \ , \ \psi ( x ) = 1 - x$ on $[ \textstyle { \frac { 1 } { 2 } } , 1 ]$ and extended periodically of period 1. Define $\begin{array} { r } { f ( x ) = \sum _ { n = 0 } ^ { \infty } 2 ^ { - n } \psi ( 8 ^ { n } x ) } \end{array}$

i. Show that $f ( x )$ is continuous everywhere.

ii.
Show that $f ( x )$ is differentiable nowhere.

Hint: Consider the difference quotients

$$
\Delta _ { h } f ( x ) \equiv { \frac { f ( x + h ) - f ( x ) } { h } }
$$

where $h = \pm 8 ^ { - k }$ and the sign is chosen so that x and $x + h$ lie on the same linear segment of the graph of $\psi ( 8 ^ { k - 1 } x )$ . Then

a. $\begin{array} { r } { \Delta _ { h } f ( x ) = \sum _ { n = 0 } ^ { k - 1 } 2 ^ { - n } \Delta _ { h } \psi ( 8 ^ { n } x ) } \end{array}$

b. $\begin{array} { r } { | \Delta _ { h } f ( x ) | \geq 4 ^ { k - 1 } - \sum _ { n = 0 } ^ { k - 2 } 4 ^ { n } } \end{array}$

::: {.solution}
<1>1. The series converges uniformly, hence defines a continuous function.
::: {.proof}
The periodic triangle wave satisfies
\[
0\le \psi(x)\le \frac12
\]
for every $x$. Hence
\[
\left|2^{-n}\psi(8^n x)\right|\le 2^{-n-1}
\]
uniformly in $x$. Since
\[
\sum_{n=0}^\infty 2^{-n-1}<\infty,
\]
the Weierstrass $M$-test gives uniform convergence of
\[
f(x)=\sum_{n=0}^\infty 2^{-n}\psi(8^n x).
\]
Each summand is continuous, so $f$ is continuous on $\mathbb R$.
:::

<1>2. Construct small increments with a large difference quotient.
::: {.proof}
Fix $x\in\mathbb R$ and $k\ge1$. Choose
\[
h_k\in\{8^{-k},-8^{-k}\}
\]
so that $8^{k-1}x$ and $8^{k-1}(x+h_k)$ lie in one linear piece of the periodic triangle wave $\psi$. This is always possible because the displacement in the argument is only $1/8$, whereas every linear piece has length $1/2$.

For $n\ge k$,
\[
8^n h_k=\pm 8^{n-k}\in\mathbb Z,
\]
so periodicity gives
\[
\psi(8^n(x+h_k))=\psi(8^n x).
\]
Thus
\[
\Delta_{h_k}f(x)
=\sum_{n=0}^{k-1}2^{-n}\Delta_{h_k}\bigl(\psi(8^n x)\bigr).
\]

Because $\psi$ is $1$-Lipschitz,
\[
\left|\Delta_{h_k}\bigl(\psi(8^n x)\bigr)\right|
\le 8^n
\]
for $n<k-1$. On the other hand, by the choice of sign, the $n=k-1$ term lies entirely in one linear piece of slope $\pm1$, so
\[
\left|2^{-(k-1)}\Delta_{h_k}\bigl(\psi(8^{k-1}x)\bigr)\right|
=2^{-(k-1)}8^{k-1}=4^{k-1}.
\]
Therefore
\[
\begin{aligned}
|\Delta_{h_k}f(x)|
&\ge 4^{k-1}-\sum_{n=0}^{k-2}2^{-n}8^n\\
&=4^{k-1}-\sum_{n=0}^{k-2}4^n\\
&=4^{k-1}-\frac{4^{k-1}-1}{3}\\
&=\frac{2\cdot4^{k-1}+1}{3}.
\end{aligned}
\]
The right-hand side tends to $\infty$ as $k\to\infty$.
:::

<1>3. Conclude nowhere differentiability.
::: {.proof}
Since $|h_k|=8^{-k}\to0$ while
\[
|\Delta_{h_k}f(x)|\to\infty,
\]
the difference quotients at $x$ cannot converge to a finite limit. Thus $f$ is not differentiable at $x$.

The point $x$ was arbitrary, so $f$ is nowhere differentiable.
:::
:::
