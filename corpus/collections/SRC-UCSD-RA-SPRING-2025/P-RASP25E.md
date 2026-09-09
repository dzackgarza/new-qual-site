---
schema: qual/card@1
id: P-RASP25E
kind: problem
title: "Poincare inequality and characterization of minimizers"
classification:
  areas:
  - real-analysis
  topics:
  - Real Analysis
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Problem 5 of the official UCSD Spring 2025 real-analysis qualifying exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: problem
Let $f \in C^1(\mathbb{R})$ such that $f(0) = f(1)$ and $\int_0^1 f(x)\,dx = 0$.

(1) Prove that $4\pi^2 \int_0^1 |f(x)|^2\,dx \leq \int_0^1 |f'(x)|^2\,dx$.

(2) Prove that if $4\pi^2 \int_0^1 |f(x)|^2\,dx = \int_0^1 |f'(x)|^2\,dx$, then there exist $a, b \in \mathbb{C}$ such that $f(x) = a\cos(2\pi x) + b\sin(2\pi x)$ for every $x \in [0,1]$.
:::

::: solution
For $n\in\mathbb Z$, write
\[
\widehat f(n):=\int_0^1 f(x)e^{-2\pi i n x}\,dx.
\]

<1>1. Relate the Fourier coefficients of $f'$ and $f$.
::: proof
Since $f\in C^1([0,1])$, integration by parts gives
\[
\begin{aligned}
\widehat{f'}(n)
&=\int_0^1 f'(x)e^{-2\pi i n x}\,dx\\
&=\left[f(x)e^{-2\pi i n x}\right]_0^1
+2\pi i n\int_0^1 f(x)e^{-2\pi i n x}\,dx.
\end{aligned}
\]
Because $e^{-2\pi i n}=1$ and $f(1)=f(0)$, the boundary term vanishes. Hence
\[
\boxed{\widehat{f'}(n)=2\pi i n\widehat f(n).}
\]
Also the zero-mean assumption says
\[
\widehat f(0)=0.
\]
:::

<1>2. Prove the Poincare inequality.
::: proof
By Parseval's identity,
\[
\int_0^1|f(x)|^2\,dx
=\sum_{n\in\mathbb Z}|\widehat f(n)|^2
=\sum_{n\ne0}|\widehat f(n)|^2.
\]
Using Step 1 and Parseval again,
\[
\int_0^1|f'(x)|^2\,dx
=4\pi^2\sum_{n\in\mathbb Z}n^2|\widehat f(n)|^2.
\]
Since $n^2\ge1$ for $n\ne0$,
\[
\int_0^1|f'(x)|^2\,dx
\ge4\pi^2\sum_{n\ne0}|\widehat f(n)|^2
=4\pi^2\int_0^1|f(x)|^2\,dx.
\]
Thus
\[
\boxed{4\pi^2\int_0^1|f|^2\le\int_0^1|f'|^2.}
\]
:::

<1>3. Characterize the equality case.
::: proof
Equality in Step 2 is equivalent to
\[
\sum_{n\ne0}(n^2-1)|\widehat f(n)|^2=0.
\]
Every summand is nonnegative, so
\[
\widehat f(n)=0
\qquad\text{for every }|n|\ge2.
\]
Together with $\widehat f(0)=0$, this yields
\[
f(x)=c_1e^{2\pi i x}+c_{-1}e^{-2\pi i x}
\]
in $L^2([0,1])$. Both sides are continuous, so the equality holds everywhere on $[0,1]$.

Using
\[
e^{2\pi i x}=\cos(2\pi x)+i\sin(2\pi x),
\qquad
e^{-2\pi i x}=\cos(2\pi x)-i\sin(2\pi x),
\]
we may write
\[
f(x)=a\cos(2\pi x)+b\sin(2\pi x)
\]
for suitable $a,b\in\mathbb C$. Therefore every equality case has exactly the stated form.
:::
:::
