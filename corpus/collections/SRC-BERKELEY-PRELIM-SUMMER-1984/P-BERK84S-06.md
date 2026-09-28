---
schema: qual/card@1
id: P-BERK84S-06
kind: problem
title: Zeros of truncated exponential reciprocals
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against Problem 6 of the vendored Berkeley Preliminary Exam, Summer 1984.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Verified the reciprocal-variable reduction and uniform Taylor-tail bound against the positive lower bound for |e^w| on the closed disk.
---

::: {.problem}
Let $\rho > 0$ . Show that for n large enough, all the zeros of

$$
f _ { n } ( z ) = 1 + { \frac { 1 } { z } } + { \frac { 1 } { 2 ! z ^ { 2 } } } + \cdots + { \frac { 1 } { n ! z ^ { n } } }
$$

lie in the circle $| z | < \rho .$
:::


::: {.solution}
Fix $\rho>0$ and put
\[
R=\frac1\rho.
\]
For $w\in\mathbb C$, let
\[
p_n(w)=\sum_{k=0}^n\frac{w^k}{k!}.
\]
Then for $z\ne0$,
\[
f_n(z)=p_n(1/z).
\]

<1>1. For all sufficiently large $n$, the polynomial $p_n$ has no zero in the closed disk $|w|\le R$.
::: {.proof}
On $|w|\le R$,
\[
|e^w|=e^{\operatorname{Re}w}\ge e^{-R}.
\]
Also
\[
|e^w-p_n(w)|
\le \sum_{k=n+1}^{\infty}\frac{|w|^k}{k!}
\le \sum_{k=n+1}^{\infty}\frac{R^k}{k!}.
\]
The last tail tends to $0$ as $n\to\infty$. Hence for all sufficiently large $n$,
\[
\sum_{k=n+1}^{\infty}\frac{R^k}{k!}<e^{-R}.
\]
For such $n$ and every $|w|\le R$,
\[
|p_n(w)|
\ge |e^w|-|e^w-p_n(w)|
>e^{-R}-e^{-R}=0.
\]
Thus $p_n$ has no zero in $|w|\le R$.
:::

<1>2. Every zero of $f_n$ then satisfies $|z|<\rho$.
::: {.proof}
Let $n$ be large enough for <1>1 and suppose $f_n(z)=0$. Since $f_n$ has a pole rather than a zero at $z=0$, we have $z\ne0$. Put $w=1/z$. Then
\[
p_n(w)=f_n(z)=0.
\]
By <1>1 this forces $|w|>R=1/\rho$. Therefore
\[
|z|=\frac1{|w|}<\rho.
\]
Hence, for all sufficiently large $n$, every zero of $f_n$ lies in the circle $|z|<\rho$.
:::
:::
