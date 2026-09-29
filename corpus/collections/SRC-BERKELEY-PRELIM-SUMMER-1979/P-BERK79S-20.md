---
schema: qual/card@1
id: P-BERK79S-20
kind: problem
title: $x^2/(1+x^4)$ attains its maximum along a solution of $5x''+10x'+6x=0$
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-written
  by: chatgpt
  date: 2026-09-21
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-21
  note: >-
    Solved the ODE as
    x(t)=Re^{-t}cos(t/sqrt(5)-phi). The scalar function
    u^2/(1+u^4) is at most 1/2, with equality exactly at |u|=1. If x is
    nonzero, cosine maxima at times tending to -infinity have values
    Re^{-t} tending to infinity, while nearby cosine zeros give x=0; the
    intermediate value theorem therefore gives a time with |x|=1. The zero
    solution is handled separately.
---

::: {.problem}
Let $x:\mathbb R\to\mathbb R$ solve
\[
5x''+10x'+6x=0.
\]
Prove that the function
\[
f(t)=\frac{x(t)^2}{1+x(t)^4}
\]
attains a maximum value on $\mathbb R$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

The characteristic roots of the differential equation are
$$
-1\pm\frac{i}{\sqrt5}.
$$

::: pf-proof

The characteristic polynomial is
$$
5r^2+10r+6.
$$
The quadratic formula gives
$$
\begin{aligned}
r
&=
\frac{-10\pm\sqrt{100-120}}{10}\\
&=
-1\pm\frac{i}{\sqrt5}.
\end{aligned}
$$

:::

:::

::: {.pf-step #s2}

Every real solution has the form
$$
x(t)
=
e^{-t}
\left(
A\cos\frac{t}{\sqrt5}
+
B\sin\frac{t}{\sqrt5}
\right)
$$
for some $A,B\in\RR$.

::: pf-proof

Step [](#s1){.pf-ref} gives a conjugate pair of characteristic roots
$$
-1\pm i/\sqrt5.
$$
The standard real solution basis is therefore
$$
e^{-t}\cos\frac{t}{\sqrt5},
\qquad
e^{-t}\sin\frac{t}{\sqrt5}.
$$

:::

:::

::: {.pf-step #s3}

For every real number $u$,
$$
\frac{u^2}{1+u^4}\leq\frac12,
$$
with equality if and only if
$$
\abs{u}=1.
$$

::: pf-proof

The inequality
$$
(u^2-1)^2\geq0
$$
is equivalent to
$$
u^4+1\geq2u^2.
$$
Since $1+u^4>0$, division gives
$$
\frac{u^2}{1+u^4}\leq\frac12.
$$
Equality holds exactly when
$$
u^2=1,
$$
equivalently $\abs{u}=1$.

:::

:::

::: {.pf-step #s4}

If $x$ is the zero solution, then $f$ attains its maximum.

::: pf-proof

If $x\equiv0$, then
$$
f(t)=0
$$
for every $t$. Thus the maximum value is $0$, attained everywhere.

:::

:::

::: {.pf-step #s5}

Suppose $x$ is not the zero solution. Then there are
$$
R>0
\qquad\text{and}\qquad
\phi\in\RR
$$
such that
$$
x(t)
=
Re^{-t}
\cos\left(
\frac{t}{\sqrt5}-\phi
\right).
$$

::: pf-proof

In step [](#s2){.pf-ref}, the pair $(A,B)$ is not $(0,0)$. Set
$$
R=\sqrt{A^2+B^2}>0.
$$
Choose $\phi$ such that
$$
A=R\cos\phi,
\qquad
B=R\sin\phi.
$$
The angle-addition identity gives the displayed form.

:::

:::

::: {.pf-step #s6}

There is a sequence $(t_k)$ with
$$
t_k\longrightarrow-\infty
$$
and
$$
x(t_k)=Re^{-t_k}\longrightarrow\infty.
$$

::: pf-proof

Choose
$$
t_k
=
\sqrt5(\phi-2\pi k),
\qquad
k=1,2,\ldots.
$$
Then
$$
\frac{t_k}{\sqrt5}-\phi=-2\pi k,
$$
so the cosine in step [](#s5){.pf-ref} equals $1$. Hence
$$
x(t_k)=Re^{-t_k}.
$$
Since $t_k\to-\infty$, one has $e^{-t_k}\to\infty$.

:::

:::

::: {.pf-step #s7}

For every $k$, there is a point $s_k>t_k$ such that
$$
x(s_k)=0.
$$

::: pf-proof

Set
$$
s_k
=
t_k+\frac{\pi\sqrt5}{2}.
$$
Then
$$
\frac{s_k}{\sqrt5}-\phi
=
-2\pi k+\frac\pi2,
$$
whose cosine is $0$. Step [](#s5){.pf-ref} therefore gives $x(s_k)=0$.

:::

:::

::: {.pf-step #s8}

There is a point $c\in\RR$ such that
$$
x(c)=1.
$$

::: pf-proof

By step [](#s6){.pf-ref}, choose $k$ so large that
$$
x(t_k)>1.
$$
Step [](#s7){.pf-ref} gives
$$
x(s_k)=0.
$$
The function $x$ is continuous, so the intermediate value theorem on
$[t_k,s_k]$ gives a point $c$ with
$$
x(c)=1.
$$

:::

:::

::: {.pf-step #s9}

If $x$ is nonzero, then
$$
\boxed{
\max_{t\in\RR}f(t)=\frac12.
}
$$

::: pf-proof

By step [](#s3){.pf-ref},
$$
f(t)
=
\frac{x(t)^2}{1+x(t)^4}
\leq
\frac12
$$
for every $t$. Step [](#s8){.pf-ref} gives a point $c$ with $x(c)=1$, and therefore
$$
f(c)=\frac12.
$$
Thus the upper bound is attained.

:::

:::

::: {.pf-step #s10}

In every case, $f$ attains a maximum value on $\RR$.

::: pf-proof

The zero solution is handled by step [](#s4){.pf-ref}. Every nonzero solution is
handled by step [](#s9){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s10){.pf-ref} is the required conclusion.

:::

:::

:::
