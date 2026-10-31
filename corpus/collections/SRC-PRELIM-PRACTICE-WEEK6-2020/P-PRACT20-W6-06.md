---
schema: qual/card@1
id: P-PRACT20-W6-06
kind: problem
title: Separating continuity, uniform continuity, Lipschitz continuity and differentiability on $(-1,1)$
classification:
  areas:
  - prelim
  topics:
  - Uniform Continuity
  - Lipschitz Continuity
  - Differentiability
relations: []
review: draft
---

::: {.problem}
Find examples of a function $f : ( - 1 , 1 ) \to \RR$ which is

(A) continuous but not uniformly continuous,

(B) uniformly continuous but not Lipschitz continuous,

(C) Lipschitz continuous but not differentiable,

(D) differentiable but not continuously differentiable.
:::

::: {.solution}
(A) Let $f(x)=\frac{1}{1-x}$. Then $f$ is continuous on $(-1,1)$. It is not uniformly continuous: $x_n=1-1/n\to1$ is a Cauchy sequence, but $f(x_n)=n$ is not Cauchy, while a uniformly continuous function maps Cauchy sequences to Cauchy sequences.

(B) Let $f(x)=\sqrt{1-x}$. Then $f$ extends continuously to the compact set $[-1,1]$, so it is uniformly continuous there and hence on $(-1,1)$. It is not Lipschitz continuous. Indeed, $f$ is differentiable on $(-1,1)$ with

$$
\abs{f'(x)}=\frac{1}{2\sqrt{1-x}}\to\infty\quad\text{as }x\to1.
$$

So for any $K>0$ there is $\delta>0$ with $\abs{f'(x)}>K$ for $x\in(1-\delta,1)$. For $x\neq y$ in $(1-\delta,1)$, the mean value theorem gives $c$ between $x$ and $y$ with

$$
\abs{f(x)-f(y)}=\abs{f'(c)}\abs{x-y}>K\abs{x-y},
$$

so $K$ is not a Lipschitz constant for $f$. Since $K>0$ was arbitrary, $f$ is not Lipschitz continuous.

(C) Let $f(x)=\abs{x}$. It is Lipschitz continuous with constant $1$ by the reverse triangle inequality, but it is not differentiable at $x=0$.

(D) Let

$$
f(x)=\begin{cases}x^2\sin\left(\frac1x\right),&x\in(-1,0)\cup(0,1),\\0,&x=0.\end{cases}
$$

For $x\neq0$, $f$ is a product of smooth functions, with

$$
f'(x)=2x\sin\left(\frac1x\right)-\cos\left(\frac1x\right),\qquad x\in(-1,0)\cup(0,1).
$$

At $x=0$,

$$
\lim_{x\to0}\frac{f(x)-f(0)}{x-0}=\lim_{x\to0}x\sin\left(\frac1x\right)=0,
$$

so $f'(0)=0$ and $f$ is differentiable on $(-1,1)$. The derivative is discontinuous at $0$: along $x_n=\frac{1}{(2n+1)\pi}\to0$, we have $\sin(1/x_n)=0$ and $\cos(1/x_n)=-1$, so $f'(x_n)=1\not\to0=f'(0)$.
:::
