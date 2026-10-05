---
schema: qual/card@1
id: P-UCLAB15S-03
kind: problem
title: A Lipschitz function with vanishing forward difference quotients
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
  note: Checked against the vendored UCLA Basic Examination, Spring 2015, `assets/attachments/basic-15S.pdf`.
---

::: {.problem}
Let $f:\mathbb R\to\mathbb R$ be Lipschitz.
Suppose that for every $x\in\mathbb R$,
\[
\lim_{n\to\infty}n\left[f\left(x+\frac1n\right)-f(x)\right]=0.
\]
Prove that $f$ is differentiable.
:::

::: {.solution}
Let
\[
L\ge0
\]
be a Lipschitz constant for $f$:
\[
|f(x)-f(y)|
\le
L|x-y|
\]
for all $x,y\in\mathbb R$.

<1>1. Define
\[
g_n(x)
=
n\left[
f\left(x+\frac1n\right)-f(x)
\right].
\]
Then
\[
|g_n(x)|\le L
\]
for every $x$ and $n$.

::: {.proof}
By the Lipschitz estimate,
\[
\left|
f\left(x+\frac1n\right)-f(x)
\right|
\le
\frac Ln.
\]
Multiplying by $n$ gives
\[
|g_n(x)|\le L.
\]
:::

<1>2. For every fixed $x\in\mathbb R$,
\[
g_n(x)\to0.
\]

::: {.proof}
This is exactly the hypothesis of the problem.
:::

<1>3. Fix real numbers
\[
a<b.
\]
Then
\[
\int_a^b g_n(x)\,dx
\longrightarrow0.
\]

::: {.proof}
By steps <1>1--<1>2,
\[
g_n(x)\to0
\]
pointwise on $[a,b]$ and
\[
|g_n(x)|\le L.
\]
The constant function $L$ is integrable on $[a,b]$.
Therefore the dominated convergence theorem gives
\[
\int_a^b g_n(x)\,dx
\to
\int_a^b0\,dx
=0.
\]
:::

<1>4. One has
\[
\int_a^b g_n(x)\,dx
=
n
\left[
\int_b^{b+1/n}f(u)\,du
-
\int_a^{a+1/n}f(u)\,du
\right].
\]

::: {.proof}
By definition,
\[
\begin{aligned}
\int_a^b g_n(x)\,dx
&=
n\int_a^b
\left[
f\left(x+\frac1n\right)-f(x)
\right]dx\\
&=
n
\left[
\int_a^b f\left(x+\frac1n\right)dx
-
\int_a^b f(x)\,dx
\right].
\end{aligned}
\]
In the first integral, set
\[
u=x+\frac1n.
\]
Then
\[
\int_a^b f\left(x+\frac1n\right)dx
=
\int_{a+1/n}^{b+1/n}f(u)\,du.
\]
Subtracting the integral over $[a,b]$ leaves exactly the two boundary pieces in the displayed formula.
:::

<1>5. One has
\[
n\int_b^{b+1/n}f(u)\,du
\longrightarrow
f(b).
\]

::: {.proof}
By continuity of $f$ at $b$,
\[
\sup_{u\in[b,b+1/n]}
|f(u)-f(b)|
\to0.
\]
Hence
\[
\begin{aligned}
\left|
n\int_b^{b+1/n}f(u)\,du-f(b)
\right|
&=
\left|
n\int_b^{b+1/n}
\bigl(f(u)-f(b)\bigr)\,du
\right|\\
&\le
\sup_{u\in[b,b+1/n]}
|f(u)-f(b)|
\to0.
\end{aligned}
\]
The function is continuous because every Lipschitz function is continuous.
:::

<1>6. Likewise,
\[
n\int_a^{a+1/n}f(u)\,du
\longrightarrow
f(a).
\]

::: {.proof}
Apply the same argument as in step <1>5 at the point $a$.
:::

<1>7. Therefore
\[
\int_a^b g_n(x)\,dx
\longrightarrow
f(b)-f(a).
\]

::: {.proof}
Use the identity in step <1>4 and the limits in steps <1>5--<1>6.
:::

<1>8. One has
\[
\boxed{f(a)=f(b)}.
\]

::: {.proof}
Step <1>3 says
\[
\int_a^b g_n(x)\,dx\to0,
\]
while step <1>7 says the same sequence of integrals converges to
\[
f(b)-f(a).
\]
Limits are unique, so
\[
f(b)-f(a)=0.
\]
:::

<1>9. The function $f$ is constant on $\mathbb R$.

::: {.proof}
The points
\[
a<b
\]
were arbitrary.
Step <1>8 therefore shows that every two real points have the same $f$-value.
:::

<1>10. Consequently $f$ is differentiable everywhere, with
\[
\boxed{f'(x)=0}
\]
for every $x\in\mathbb R$.

::: {.proof}
Every constant function is differentiable at every point, with derivative zero.
:::

<1>11. Q.E.D.

::: {.proof}
Step <1>10 is the required conclusion.
:::
:::
