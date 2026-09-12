---
schema: qual/card@1
id: P-RASP25C
kind: problem
title: "Weak convergence in C([0,1]) and non-reflexivity"
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
  note: Checked against Problem 3 of the official UCSD Spring 2025 real-analysis qualifying exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: problem
Let $E$ be the Banach space $C([0,1])$ endowed with the uniform norm.
Let $(f_h)_{h \in \mathbb{N}} \subset E$ be a sequence and $f \in E$.

(1) Prove that if $f_h$ converges weakly to $f$ then there is $M > 0$ such that $|f_h(x)| \leq M$ for every $x \in [0,1]$ and $h \in \mathbb{N}$.

(2) Prove that if $f_h$ converges weakly to $f$ then $f_h(x) \to f(x)$ for every $x \in [0,1]$.

(3) Show that $f_h(x) = x^h$ does not converge weakly in $E$.

(4) Show that $E$ is not reflexive.
:::

::: solution
<1>1. Weakly convergent sequences are uniformly bounded.
::: proof
Suppose $f_h\rightharpoonup f$ in $E=C([0,1])$. Every weakly convergent sequence in a Banach space is norm bounded. Indeed, for each $h$ define
\[
T_h:E^*\to\mathbb C,
\qquad
T_h(\varphi)=\varphi(f_h).
\]
For every fixed $\varphi\in E^*$, the scalar sequence $T_h(\varphi)$ converges, hence is bounded. By the Uniform Boundedness Principle,
\[
\sup_h\|T_h\|<\infty.
\]
Under the canonical embedding $E\hookrightarrow E^{**}$,
\[
\|T_h\|=\|f_h\|_\infty.
\]
Hence there is $M>0$ such that
\[
\|f_h\|_\infty\le M
\]
for every $h$. Therefore
\[
\boxed{|f_h(x)|\le M}
\]
for every $x\in[0,1]$ and every $h$.
:::

<1>2. Weak convergence implies pointwise convergence.
::: proof
Fix $x\in[0,1]$. The evaluation functional
\[
\delta_x:E\to\mathbb C,
\qquad
\delta_x(g)=g(x),
\]
is bounded because
\[
|\delta_x(g)|\le\|g\|_\infty.
\]
Thus $\delta_x\in E^*$. Weak convergence gives
\[
f_h(x)=\delta_x(f_h)\longrightarrow\delta_x(f)=f(x).
\]
Since $x$ was arbitrary,
\[
\boxed{f_h(x)\to f(x)\text{ for every }x\in[0,1].}
\]
:::

<1>3. Show that $f_h(x)=x^h$ does not converge weakly.
::: proof
For every $x\in[0,1)$,
\[
x^h\longrightarrow0,
\]
while
\[
1^h=1
\]
for every $h$. Thus the pointwise limit is
\[
g(x)=
\begin{cases}
0,&0\le x<1,\\
1,&x=1,
\end{cases}
\]
which is not continuous.

If $(x^h)$ converged weakly in $E$ to some $f\in E$, Step 2 would force pointwise convergence to the continuous function $f$. Hence $f=g$, impossible because $g\notin C([0,1])$. Therefore
\[
\boxed{x^h\text{ does not converge weakly in }C([0,1]).}
\]
:::

<1>4. Deduce that $C([0,1])$ is not reflexive.
::: proof
The sequence
\[
f_h(x)=x^h
\]
lies in the closed unit ball of $E$ because $\|f_h\|_\infty=1$.

Suppose $E$ were reflexive. Then its closed unit ball would be weakly compact. By the Eberlein--Smulian theorem, weak compactness in a Banach space implies weak sequential compactness. Therefore $(f_h)$ would have a weakly convergent subsequence.

But every subsequence $(x^{h_k})$ has the same pointwise limit $g$ from Step 3. By Step 2, any weak limit would have to equal $g$ pointwise, again impossible because $g$ is discontinuous. This contradiction proves
\[
\boxed{C([0,1])\text{ is not reflexive}.}
\]
:::
:::
