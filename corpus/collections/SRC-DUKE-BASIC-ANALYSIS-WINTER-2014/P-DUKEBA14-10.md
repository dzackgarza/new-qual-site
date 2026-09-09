---
schema: qual/card@1
id: P-DUKEBA14-10
kind: problem
title: Existence for a nonlinear Volterra integral equation by contraction
classification:
  areas: [real-analysis]
  topics: [Banach Fixed Point Theorem, Integral Equations]
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Part II, Problem 4 of the preserved Duke Winter 2014 Basic Analysis qualifying exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: problem
Prove that there exists $f\in C([0,1],\mathbb R)$ satisfying
\[
f(x)=\frac1{1066}\int_0^x e^{-s^2x^2}f(s)^2\,ds+\sin(2013x).
\]
:::

::: solution
<1>1. Define the fixed-point map on a closed ball.
::: proof
Let $X=C([0,1])$ with the sup norm and set
\[
B=\{f\in X:\|f\|_\infty\le2\}.
\]
The set $B$ is complete because it is closed in the Banach space $X$. Define
\[
(Tf)(x)=\frac1{1066}\int_0^x e^{-s^2x^2}f(s)^2\,ds+\sin(2013x).
\]
For $f\in B$, the integrand is continuous, so $Tf\in X$.
:::

<1>2. Show that $T$ maps $B$ into itself.
::: proof
If $f\in B$, then for $0\le x\le1$,
\[
|Tf(x)|
\le \frac1{1066}\int_0^x|f(s)|^2\,ds+1
\le \frac4{1066}+1<2.
\]
Thus $T(B)\subset B$.
:::

<1>3. Prove that $T$ is a contraction on $B$.
::: proof
For $f,g\in B$,
\[
|f(s)^2-g(s)^2|
\le(|f(s)|+|g(s)|)|f(s)-g(s)|
\le4\|f-g\|_\infty.
\]
Hence
\[
\begin{aligned}
|Tf(x)-Tg(x)|
&\le \frac1{1066}\int_0^x|f(s)^2-g(s)^2|\,ds\\
&\le \frac4{1066}\|f-g\|_\infty.
\end{aligned}
\]
Taking the supremum over $x$ gives
\[
\|Tf-Tg\|_\infty
\le \frac4{1066}\|f-g\|_\infty,
\]
and $4/1066<1$.
:::

<1>4. Apply Banach's fixed-point theorem.
::: proof
Since $T$ is a contraction of the complete metric space $B$ into itself, Banach's fixed-point theorem gives a unique $f\in B$ with $Tf=f$. This $f$ is continuous and satisfies the required integral equation.
:::
:::
