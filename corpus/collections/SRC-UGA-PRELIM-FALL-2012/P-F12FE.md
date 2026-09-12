---
schema: qual/card@1
id: P-F12FE
kind: problem
title: $f(xy)=xf(y)+yf(x)$ implies $f(1)=0$ and $f(u^n)=n u^{n-1}f(u)$
classification:
  areas:
  - prelim
  topics:
  - Functions and Relations
  - Induction
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
---

::: problem
Suppose $f: \mathbb{R} \to \mathbb{R}$ satisfies $f(xy) = xf(y) + yf(x)$ for all $x, y \in \mathbb{R}$.
Prove that $f(1) = 0$ and that $f(u^n) = n u^{n-1} f(u)$ for all $n \in \mathbb{N}$ and $u \in \mathbb{R}$.
:::

::: solution
Putting $x=y=1$ gives
\[
f(1)=f(1)+f(1),
\]
so $f(1)=0$.

We prove by induction on $n\ge1$ that
\[
f(u^n)=nu^{n-1}f(u).
\]
For $n=1$ this is immediate. If it holds for $n$, then
\[
\begin{aligned}
f(u^{n+1})
&=f(u^n u)\\
&=u^n f(u)+u f(u^n)\\
&=u^n f(u)+u\bigl(nu^{n-1}f(u)\bigr)\\
&=(n+1)u^n f(u).
\end{aligned}
\]
Thus the formula holds for every positive integer $n$.
:::
