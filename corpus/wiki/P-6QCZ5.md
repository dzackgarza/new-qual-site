---
schema: qual/card@1
id: P-6QCZ5
kind: problem
title: Measurability of $f(x)$ and $f(x-y)g(y)$ on $\RR^n\times\RR^n$, and $\|f*g\|_p\le\|g\|_1\|f\|_p$
  for $p=1,2,\infty$ when $f\in L^1\cap L^\infty$ and $g\in L^1$
classification:
  areas:
  - real-analysis
  topics:
  - Convolution
  - L¹
  - Lp Spaces
relations: []
review: draft
solved: true
---

::: problem
a. Prove that if $f, g: \RR^n\to \CC$ is both measurable then $F(x, y) \definedas f(x)$ and $h(x, y)\definedas f(x-y) g(y)$ is measurable on $\RR^n\cross \RR^n$.

b. Show that if $f\in L^1(\RR^n) \intersect L^\infty(\RR^n)$ and $g\in L^1(\RR^n)$, then $f\ast g \in L^1(\RR^n) \intersect L^\infty(\RR^n)$ is well defined, and carefully show that it satisfies the following properties:
\[
\norm{f\ast g}_\infty &\leq \norm{g}_1 \norm{f}_\infty
\norm{f\ast g}_1      &\leq \norm{g}_1 \norm{f}_1
\norm{f\ast g}_2      &\leq \norm{g}_1 \norm{f}_2
.\]

> Hint: first show $\abs{f\ast g}^2 \leq \norm{g}_1 \qty{ \abs{f}^2 \ast \abs{g}}$.
:::

::: {.solution}
> **AI-Generated Solution**

<1>1. $F(x,y) = f(x)$ and $h(x,y) = f(x - y)g(y)$ are measurable on $\RR^n \cross \RR^n$.
    <2>1. $F$ is measurable.
        Proof: $F = f \circ \pi_1$ where $\pi_1(x,y) = x$ is continuous; composition of a measurable function with a continuous map is measurable.
    <2>2. $h$ is measurable.
        Proof: $(x,y) \mapsto (x - y, y)$ is continuous (hence Borel), and $(u,y) \mapsto f(u)g(y)$ is measurable (product of measurable functions of the coordinate projections, by <2>1 applied to $f$ and $g$); $h$ is their composition.

<1>2. If $f \in L^1 \intersect L^\infty$ and $g \in L^1$, then $f \ast g$ is well defined and lies in $L^1 \intersect L^\infty$.
    <2>1. $f \ast g \in L^1$ with $\|f \ast g\|_1 \le \|g\|_1\|f\|_1$.
        Proof: Tonelli: $\int|f\ast g(x)|\,dx \le \iint |f(x-y)||g(y)|\,dy\,dx = \|f\|_1\|g\|_1$.
    <2>2. $f \ast g$ is bounded with $\|f \ast g\|_\infty \le \|g\|_1\|f\|_\infty$.
        Proof: $|f\ast g(x)| \le \int |f(x-y)||g(y)|\,dy \le \|f\|_\infty\|g\|_1$ for every $x$.
    <2>3. Q.E.D.
        Proof: <2>1 and <2>2 show the convolution is finite a.e. and lies in both spaces.

<1>3. $\|f \ast g\|_2 \le \|g\|_1\|f\|_2$.
    <2>1. Cauchy–Schwarz: $|f \ast g(x)|^2 \le \|g\|_1 (|f|^2 \ast |g|)(x)$.
        Proof: write $f(x-y)g(y) = f(x-y)\sqrt{|g(y)|} \cdot \sqrt{|g(y)|}\,\mathrm{sgn}(g(y))$ and apply Cauchy–Schwarz in the $y$-integral: $|f\ast g(x)|^2 \le \left(\int|f(x-y)|^2|g(y)|\,dy\right)\left(\int|g(y)|\,dy\right) = \|g\|_1(|f|^2 \ast |g|)(x)$.
    <2>2. Integrate: $\|f \ast g\|_2^2 \le \|g\|_1 \|\,|f|^2 \ast |g|\,\|_1 \le \|g\|_1 \cdot \|\,|f|^2\|_1\|g\|_1 = \|g\|_1^2\|f\|_2^2$.
        Proof: <2>1 integrated; then the $L^1$ convolution bound (<1>2<2>1) applied to $|f|^2 \in L^1$ and $|g| \in L^1$; and $\|\,|f|^2\|_1 = \|f\|_2^2$.
    <2>3. Q.E.D.
        Proof: <2>2 gives $\|f\ast g\|_2 \le \|g\|_1\|f\|_2$.
:::
