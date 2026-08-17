---
schema: qual/card@1
id: P-7QE3E
kind: problem
title: The integral $I(x)=\int\delta_F(y)/|x-y|^2\,dy$ for a closed set of finite complementary measure
classification:
  areas:
  - real-analysis
  topics:
  - measure-theory
  - integrals
  - fubini-tonelli
relations: []
review: draft
solved: true
---

::: problem
a.
Let $F \subset \mathbb{R}$ be closed, and define
\[
\delta_{F}(y):=\inf _{x \in F}|x-y| .
\]
For $y \notin F$, show that
\[
\int_{F}|x-y|^{-2} d x \leq \frac{2}{\delta_F(y)},
\]
b.
Let $F \subset \mathbb{R}$ be a closed set whose complement has finite measure, i.e. $m(R \sm F)< \infty$. 
Define the function
\[
I(x):=\int_{\mathbb{R}} \frac{\delta_{F}(y)}{|x-y|^{2}} d y
\]
Prove that $I(x)=\infty$ if $x \not\in F$, however $I(x)<\infty$ for almost every $x \in F$. 

  > Hint: investigate $\int_{F} I(x) d x$.
:::

::: {.solution}
> **AI-Generated Solution**

<1>1. For $y \notin F$: $\int_F \frac{dx}{|x - y|^2} \le \frac{2}{\delta_F(y)}$.
    <2>1. Every $x \in F$ with $x < y$ satisfies $y - x \ge \delta_F(y)$, and every $x \in F$ with $x > y$ satisfies $x - y \ge \delta_F(y)$.
        Proof: $\delta_F(y) = \inf_{x \in F}|x - y| \le |x - y|$ for every $x \in F$.
    <2>2. $\int_{F \cap (-\infty, y]}\frac{dx}{|x - y|^2} \le \int_{-\infty}^{y - \delta}\frac{dx}{(y - x)^2} = \int_\delta^\infty \frac{du}{u^2} = \frac{1}{\delta}$, where $\delta = \delta_F(y)$.
        Proof: by <2>1, $F \cap (-\infty, y] \subseteq (-\infty, y - \delta]$; substitute $u = y - x$.
    <2>3. Similarly $\int_{F \cap [y, \infty)}\frac{dx}{|x - y|^2} \le \frac{1}{\delta}$.
        Proof: $F \cap [y, \infty) \subseteq [y + \delta, \infty)$ by <2>1, and $\int_{y+\delta}^\infty (x-y)^{-2}dx = \int_\delta^\infty u^{-2}du = 1/\delta$.
    <2>4. Q.E.D.
        Proof: add <2>2 and <2>3.

<1>2. For $x \notin F$: $I(x) = \int_\RR \frac{\delta_F(y)}{|x - y|^2}\,dy = \infty$.
    <2>1. $\delta_F$ is $1$-Lipschitz, so $\delta_F(y) \ge \delta_F(x) - |y - x|$.
        Proof: $|\delta_F(y) - \delta_F(x)| \le |y - x|$ by the triangle inequality.
    <2>2. Since $F$ is closed and $x \notin F$, $\delta := \delta_F(x) > 0$; for $|y - x| < \delta/2$, $\delta_F(y) \ge \delta/2$.
        Proof: <2>1 and $\delta > 0$ (if $\delta_F(x) = 0$, then $x$ would be a limit point of $F$, and closedness gives $x \in F$).
    <2>3. $I(x) \ge \frac{\delta}{2}\int_{|y - x| < \delta/2}\frac{dy}{|x - y|^2} = \infty$.
        Proof: restrict the integrand to the ball of <2>2, where $\delta_F(y) \ge \delta/2$; the integral of $|x - y|^{-2}$ over any ball about $x$ diverges.
    <2>4. Q.E.D.
        Proof: <2>2 and <2>3.

<1>3. $\int_F I(x)\,dx < \infty$; consequently $I(x) < \infty$ for almost every $x \in F$.
    <2>1. By Tonelli, $\int_F I(x)\,dx = \int_\RR \delta_F(y)\left(\int_F \frac{dx}{|x - y|^2}\right)dy$.
        Proof: $I$ and the integrand are non-negative, so Tonelli applies.
    <2>2. For $y \in F$ the inner integral contributes $0$: $\delta_F(y) = 0$ there, so the integrand $\delta_F(y)|x - y|^{-2}$ is $0$ a.e. in $x$.
        Proof: $\delta_F(y) = 0$ exactly on $F$; the integrand vanishes for $x \ne y$, and $\{x = y\}$ is a null set.
    <2>3. For $y \notin F$: $\delta_F(y)\int_F |x - y|^{-2}dx \le \delta_F(y)\cdot\frac{2}{\delta_F(y)} = 2$.
        Proof: <1>1.
    <2>4. $\int_F I(x)\,dx \le \int_{\RR \setminus F} 2\,dy = 2m(\RR \setminus F) < \infty$.
        Proof: <2>1–<2>3, and $m(\RR \setminus F) < \infty$ by hypothesis.
    <2>5. Q.E.D.
        Proof: if $I = \infty$ on a set of positive measure inside $F$, then $\int_F I = \infty$, contradicting <2>4; hence $I < \infty$ a.e. on $F$.
:::
