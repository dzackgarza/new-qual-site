---
schema: qual/card@1
id: P-RASP24C
kind: problem
title: "Hölder space is a Banach space with compact unit ball"
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
  note: Checked against Problem 3 of the official UCSD Spring 2024 real-analysis qualifying exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: problem
Let $0 < \alpha \leq 1$ and let $\Lambda_\alpha([0,1])$ denote the space of Hölder continuous functions of exponent $\alpha$ on $[0,1]$.
Specifically, $\Lambda_\alpha([0,1]) = \{f \in C([0,1]) : \|f\|_{\Lambda_\alpha} < \infty\}$ where
$$
\|f\|_{\Lambda_\alpha} = |f(0)| + \sup_{x \neq y \in [0,1]} \frac{|f(x) - f(y)|}{|x - y|^\alpha}.
$$

(a) Show that $\|\cdot\|_{\Lambda_\alpha}$ is a norm on $\Lambda_\alpha([0,1])$ and that with this norm $\Lambda_\alpha([0,1])$ is a Banach space.

(b) Let $B = \{f \in \Lambda_\alpha([0,1]) : \|f\|_{\Lambda_\alpha} \leq 1\}$ be the closed unit ball.
Show that $B$ is compact with respect to the uniform norm.
:::

::: solution
Write
\[
[f]_\alpha:=\sup_{x\ne y}
\frac{|f(x)-f(y)|}{|x-y|^\alpha},
\qquad
\|f\|_{\Lambda_\alpha}=|f(0)|+[f]_\alpha.
\]

<1>1. Verify that $\|\cdot\|_{\Lambda_\alpha}$ is a norm.
::: proof
Nonnegativity and absolute homogeneity are immediate. If
\[
\|f\|_{\Lambda_\alpha}=0,
\]
then $f(0)=0$ and $[f]_\alpha=0$, so $f(x)=f(y)$ for all $x,y$. Thus $f\equiv0$.

For the triangle inequality,
\[
|f(0)+g(0)|\le |f(0)|+|g(0)|
\]
and
\[
[f+g]_\alpha\le [f]_\alpha+[g]_\alpha.
\]
Hence
\[
\|f+g\|_{\Lambda_\alpha}
\le \|f\|_{\Lambda_\alpha}+\|g\|_{\Lambda_\alpha}.
\]
:::

<1>2. Prove completeness.
::: proof
Let $(f_n)$ be Cauchy in $\|\cdot\|_{\Lambda_\alpha}$. For every $h\in\Lambda_\alpha([0,1])$ and $x\in[0,1]$,
\[
|h(x)|\le |h(0)|+[h]_\alpha |x|^\alpha
\le \|h\|_{\Lambda_\alpha}.
\]
Therefore
\[
\|h\|_\infty\le \|h\|_{\Lambda_\alpha},
\]
so $(f_n)$ is uniformly Cauchy. Since $C([0,1])$ is complete in the uniform norm, there is $f\in C([0,1])$ such that
\[
f_n\to f
\]
uniformly.

Fix $\varepsilon>0$. Choose $N$ such that for $m,n\ge N$,
\[
\|f_n-f_m\|_{\Lambda_\alpha}<\varepsilon.
\]
Fix $n\ge N$ and let $m\to\infty$. Uniform convergence gives
\[
|f_n(0)-f(0)|\le\varepsilon.
\]
Also, for every $x\ne y$,
\[
\frac{|(f_n-f)(x)-(f_n-f)(y)|}{|x-y|^\alpha}
=\lim_{m\to\infty}
\frac{|(f_n-f_m)(x)-(f_n-f_m)(y)|}{|x-y|^\alpha}
\le\varepsilon.
\]
Taking the supremum over $x\ne y$ gives
\[
[f_n-f]_\alpha\le\varepsilon.
\]
Thus
\[
\|f_n-f\|_{\Lambda_\alpha}\le2\varepsilon
\]
for all $n\ge N$. In particular $f\in\Lambda_\alpha([0,1])$ and $f_n\to f$ in the Hölder norm. Hence $\Lambda_\alpha([0,1])$ is Banach.
:::

<1>3. Establish the Arzelà--Ascoli hypotheses for the unit ball.
::: proof
If $f\in B$, then
\[
|f(0)|\le1,
\qquad
[f]_\alpha\le1.
\]
Hence for every $x\in[0,1]$,
\[
|f(x)|\le |f(0)|+[f]_\alpha |x|^\alpha\le2.
\]
Thus $B$ is uniformly bounded. Moreover, for every $x,y\in[0,1]$,
\[
|f(x)-f(y)|\le |x-y|^\alpha
\]
uniformly for $f\in B$, so $B$ is equicontinuous.

By the Arzelà--Ascoli theorem, $B$ is relatively compact in the uniform norm.
:::

<1>4. Show that $B$ is uniformly closed.
::: proof
Suppose $f_n\in B$ and $f_n\to f$ uniformly. For each fixed $x\ne y$,
\[
|f_n(0)|+
\frac{|f_n(x)-f_n(y)|}{|x-y|^\alpha}
\le1.
\]
Passing to the limit gives
\[
|f(0)|+
\frac{|f(x)-f(y)|}{|x-y|^\alpha}
\le1.
\]
Taking the supremum over $x\ne y$ yields
\[
|f(0)|+[f]_\alpha\le1.
\]
Therefore $f\in B$. Thus $B$ is closed in the uniform norm.

Since $B$ is both relatively compact and closed in $C([0,1])$, it is compact in the uniform norm.
:::
:::
