---
schema: qual/card@1
id: P-UCLAB17F-10
kind: problem
title: A continuous function with all polynomial moments zero
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against the vendored UCLA Basic Examination, Fall 2017, `assets/attachments/basic-17F.pdf`.
---

::: {.problem}
Let $f:[a,b]\to\mathbb R$ be continuous and suppose
\[
\int_a^b f(x)x^n\,dx=0
\]
for every integer $n\ge0$. Prove that $f=0$.
:::

::: {.solution}
<1>1. For every polynomial
\[
p(x)=\sum_{k=0}^N c_kx^k,
\]
one has
\[
\int_a^b f(x)p(x)\,dx=0.
\]

::: {.proof}
By linearity of the integral,
\[
\begin{aligned}
\int_a^b f(x)p(x)\,dx
&=
\sum_{k=0}^N c_k
\int_a^b f(x)x^k\,dx.
\end{aligned}
\]
Every moment on the right is zero by hypothesis.
:::

<1>2. There exists a sequence of polynomials $(p_m)$ such that
\[
\|p_m-f\|_\infty\to0
\]
on $[a,b]$.

::: {.proof}
The function $f$ is continuous on the compact interval $[a,b]$.
By the Weierstrass approximation theorem, polynomials are uniformly dense in
\[
C([a,b]).
\]
Thus such a sequence exists.
:::

<1>3. For every $m$,
\[
\int_a^b f(x)p_m(x)\,dx=0.
\]

::: {.proof}
Each $p_m$ is a polynomial, so step <1>1 applies.
:::

<1>4. One has
\[
\int_a^b f(x)^2\,dx=0.
\]

::: {.proof}
Since $f$ is continuous on $[a,b]$, it is bounded.
Hence
\[
\begin{aligned}
\left|
\int_a^b f(x)^2\,dx
-
\int_a^b f(x)p_m(x)\,dx
\right|
&=
\left|
\int_a^b f(x)(f(x)-p_m(x))\,dx
\right|\\
&\le
(b-a)\|f\|_\infty\|f-p_m\|_\infty.
\end{aligned}
\]
The right side tends to $0$ by step <1>2.
Using step <1>3 and taking $m\to\infty$ gives
\[
\int_a^b f(x)^2\,dx=0.
\]
:::

<1>5. The function $f$ is identically zero.

::: {.proof}
The continuous function
\[
f^2
\]
is nonnegative on $[a,b]$ and has integral zero by step <1>4.
If there were
\[
x_0\in[a,b]
\]
with
\[
f(x_0)\ne0,
\]
continuity would give an interval on which
\[
f(x)^2\ge\varepsilon
\]
for some $\varepsilon>0$.
Its integral would then be strictly positive, contradicting step <1>4.
Therefore
\[
\boxed{f\equiv0}.
\]
:::

<1>6. Q.E.D.

::: {.proof}
Step <1>5 is the required conclusion.
:::
:::
