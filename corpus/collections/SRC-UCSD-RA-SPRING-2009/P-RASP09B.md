---
schema: qual/card@1
id: P-RASP09B
kind: problem
title: "Bilinear maps on Banach spaces: separate boundedness implies joint continuity"
classification:
  areas:
  - real-analysis
  topics:
  - Banach Spaces
  - Bilinear Maps
  - Uniform Boundedness Principle
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-08
  note: Checked against Problem 2 of the official UCSD Spring 2009 real-analysis qualifying exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-08
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
---

::: problem
Assume that $X, Y, Z$ are Banach spaces.
Assume $\Phi : X \times Y \to Z$ is bilinear, namely for every $x \in X$, $\Phi(x, \cdot) : Y \to Z$ is linear and for every $y \in Y$, $\Phi(\cdot, y) : X \to Z$ is linear.
Show that if for every $z^* \in Z^*$, $z^*(\Phi(x, \cdot)) \in Y^*$ and $z^*(\Phi(\cdot, y)) \in X^*$, then:

(1) $\Phi_x(\cdot) = \Phi(x, \cdot) : Y \to Z$ and $\Phi_y(\cdot) = \Phi(\cdot, y) : X \to Z$ are bounded linear maps;

(2) there exists $M$ such that
$$
\|\Phi(x, y)\| \leq M \|x\| \|y\|.
$$
:::


::: solution
<1>1. Each partial map has closed graph.
::: proof
Fix $x\in X$ and consider
\[
\Phi_x:Y\to Z,
\qquad
\Phi_x(y)=\Phi(x,y).
\]
It is linear. Suppose
\[
y_n\to y\quad\text{in }Y,
\qquad
\Phi_x(y_n)\to z\quad\text{in }Z.
\]
For every $z^*\in Z^*$, the hypothesis says
\[
z^*\circ\Phi_x\in Y^*.
\]
Therefore
\[
\begin{aligned}
z^*(z)
&=\lim_{n\to\infty}z^*(\Phi_x(y_n))\\
&=z^*(\Phi_x(y)).
\end{aligned}
\]
Thus
\[
z^*(z-\Phi_x(y))=0
\]
for every $z^*\in Z^*$. Since the dual separates points of $Z$ by Hahn--Banach,
\[
z=\Phi_x(y).
\]
Hence the graph of $\Phi_x$ is closed. Since $Y$ and $Z$ are Banach spaces, the Closed Graph Theorem gives
\[
\Phi_x\in\mathcal B(Y,Z).
\]
The same argument, with the roles of $X$ and $Y$ reversed, shows that for every $y\in Y$,
\[
\Phi_y:X\to Z,
\qquad
\Phi_y(x)=\Phi(x,y),
\]
is bounded.
:::

<1>2. Apply Uniform Boundedness to obtain a joint estimate.
::: proof
Consider the family
\[
\mathcal F:=\{\Phi_x:\|x\|_X\le1\}\subset\mathcal B(Y,Z).
\]
Fix $y\in Y$. Since $\Phi_y:X\to Z$ is bounded,
\[
\sup_{\|x\|\le1}\|\Phi_x(y)\|_Z
=\sup_{\|x\|\le1}\|\Phi_y(x)\|_Z
\le\|\Phi_y\|<\infty.
\]
Thus the family $\mathcal F$ is pointwise bounded on the Banach space $Y$. By the Uniform Boundedness Principle,
\[
M:=\sup_{\|x\|\le1}\|\Phi_x\|_{Y\to Z}<\infty.
\]
Therefore, if $x\ne0$,
\[
\begin{aligned}
\|\Phi(x,y)\|_Z
&=\|x\|_X\left\|\Phi\!\left(\frac{x}{\|x\|_X},y\right)\right\|_Z\\
&\le M\|x\|_X\|y\|_Y.
\end{aligned}
\]
The same inequality is trivial when $x=0$. Hence
\[
\boxed{\|\Phi(x,y)\|_Z\le M\|x\|_X\|y\|_Y.}
\]
:::
:::
