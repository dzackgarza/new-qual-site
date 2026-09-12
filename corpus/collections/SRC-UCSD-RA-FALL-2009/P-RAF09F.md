---
schema: qual/card@1
id: P-RAF09F
kind: problem
title: "Maximal function bound for approximate identity supremum"
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
  date: 2026-09-08
  note: Checked against Problem 6 of the official UCSD Fall 2009 real-analysis qualifying exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-08
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
---

::: problem
Suppose that on $\mathbb{R}^n$, $|\phi(x)| \leq C(1 + |x|)^{-n-\epsilon}$ for some positive $C$ and $\epsilon > 0$.
Also assume that $\phi(x)$ is measurable.
If $f \in L^p(\mathbb{R}^n)$ with $1 \leq p \leq \infty$, define
$$
M_\phi(f)(x) := \sup_{t > 0} |f * \phi_t(x)|
$$
where $f * \phi_t(x) = \int f(x-y)\phi_t(y)\,dy$, $\phi_t(y) = \frac{1}{t^n}\phi\!\left(\frac{y}{t}\right)$.

Show that there exists $C'$, independent of $f$, such that $M_\phi(f) \leq C' H(f)$, where $H(f)$ is the Hardy-Littlewood maximal function defined as
$$
H(f)(x) := \sup_{r > 0} \frac{1}{m(B(x,r))} \int_{B(x,r)} |f(y)|\,dy.
$$
:::

::: solution
<1>1. Decompose the convolution into dyadic annuli.
::: proof
Fix $x\in\mathbb R^n$ and $t>0$. From the assumed decay,
\[
|\phi_t(y)|
\le C t^{-n}\left(1+\frac{|y|}{t}\right)^{-n-\varepsilon}.
\]
Therefore
\[
|f*\phi_t(x)|
\le \int_{\mathbb R^n}|f(x-y)|\,|\phi_t(y)|\,dy.
\]
Split $\mathbb R^n$ into
\[
A_0:=\{|y|<t\},
\qquad
A_k:=\{2^{k-1}t\le |y|<2^kt\},\quad k\ge1.
\]
:::

<1>2. Estimate the inner ball.
::: proof
On $A_0$,
\[
|\phi_t(y)|\le Ct^{-n}.
\]
Hence, writing $v_n=m(B(0,1))$,
\[
\begin{aligned}
\int_{A_0}|f(x-y)|\,|\phi_t(y)|\,dy
&\le Ct^{-n}\int_{|y|<t}|f(x-y)|\,dy\\
&=Ct^{-n}\int_{B(x,t)}|f(z)|\,dz\\
&\le Cv_n H(f)(x).
\end{aligned}
\]
:::

<1>3. Estimate each outer annulus.
::: proof
If $y\in A_k$ with $k\ge1$, then
\[
1+\frac{|y|}{t}\ge 2^{k-1},
\]
so
\[
|\phi_t(y)|
\le Ct^{-n}2^{-(k-1)(n+\varepsilon)}.
\]
Also $A_k\subset B(0,2^kt)$. Therefore
\[
\begin{aligned}
\int_{A_k}|f(x-y)|\,|\phi_t(y)|\,dy
&\le Ct^{-n}2^{-(k-1)(n+\varepsilon)}
\int_{|y|<2^kt}|f(x-y)|\,dy\\
&\le Ct^{-n}2^{-(k-1)(n+\varepsilon)}
v_n(2^kt)^n H(f)(x)\\
&=Cv_n2^{n+\varepsilon}2^{-k\varepsilon}H(f)(x).
\end{aligned}
\]
:::

<1>4. Sum the geometric series and take the supremum in $t$.
::: proof
Combining the preceding estimates gives
\[
|f*\phi_t(x)|
\le Cv_n\left(
1+2^{n+\varepsilon}\sum_{k=1}^\infty2^{-k\varepsilon}
\right)H(f)(x).
\]
The series converges because $\varepsilon>0$. Thus there is a finite constant
\[
C'=Cv_n\left(
1+2^{n+\varepsilon}\frac{2^{-\varepsilon}}{1-2^{-\varepsilon}}
\right),
\]
depending only on $C,n,\varepsilon$, such that
\[
|f*\phi_t(x)|\le C'H(f)(x)
\]
for every $t>0$. Taking the supremum over $t$ yields
\[
\boxed{M_\phi(f)(x)\le C'H(f)(x).}
\]
The constant is independent of $f$.
:::
:::
