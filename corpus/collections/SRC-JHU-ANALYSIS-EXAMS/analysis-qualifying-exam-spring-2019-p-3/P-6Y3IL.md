---
schema: qual/card@1
id: P-6Y3IL
kind: problem
title: Weak convergence plus pointwise decay need not imply strong convergence in $L^2(\mathbb R^d)$
classification:
  areas:
  - real-analysis
  topics:
  - Lp Spaces
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Question 1.1 of the JHU Spring 2019 Analysis Qualifying Exam. The source claim is false as stated; the card is corrected to ask for a validity determination and counterexample.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

Question 1.1. Suppose that $f _ { j } \in L ^ { 2 } ( \mathbb { R } ^ { d } ) , j = 1 , 2 , . . . ,$ and $f \in L ^ { 2 } (  { \mathbb { R } } ^ { d } )$ satisfy

$$
\operatorname* { l i m } _ { j \to \infty } \int _ { \mathbb { R } ^ { d } } f _ { j } g = \int _ { \mathbb { R } ^ { d } } f g
$$

for all $g \in L ^ { 2 } (  { \mathbb { R } } ^ { d } )$ . That is, $f _ { j }$ converges to f weakly in $L ^ { 2 } .$ . Suppose that the sequence satisfies the uniform bound

$$
\operatorname* { s u p } _ { x \in \mathbb { R } ^ { d } } ( 1 + | x | ) ^ { d } | f _ { j } ( x ) | \leq M < \infty .\tag{A}
$$

Determine whether condition (A), together with weak convergence, implies
\[
\|f_j\|_2\to\|f\|_2
\qquad\text{and hence}\qquad
\|f_j-f\|_2\to0.
\]
If not, give a counterexample.

::: solution
<1>1. Construct a sequence satisfying the weighted pointwise bound.
::: proof
Let
\[
Q=[0,1]^d,
\qquad
f_j(x)=\mathbf1_Q(x)\sin(2\pi jx_1),
\qquad
f=0.
\]
Then $f_j\in L^2(\mathbb R^d)$ and, on $Q$,
\[
(1+|x|)^d|f_j(x)|\le (1+\sqrt d)^d.
\]
Outside $Q$, $f_j=0$. Hence condition (A) holds with
\[
M=(1+\sqrt d)^d.
\]
:::

<1>2. Prove weak convergence to zero.
::: proof
Fix $g\in L^2(\mathbb R^d)$. Since $Q$ has finite measure,
\[
g\mathbf1_Q\in L^1(Q)
\]
by Cauchy--Schwarz. Fubini gives an $L^1(0,1)$ function
\[
h(t):=\int_{[0,1]^{d-1}}g(t,x')\,dx'.
\]
Therefore
\[
\int_{\mathbb R^d}f_j(x)g(x)\,dx
=\int_0^1 h(t)\sin(2\pi jt)\,dt.
\]
By the Riemann--Lebesgue lemma, the right-hand side tends to $0$. Thus
\[
f_j\rightharpoonup0
\quad\text{in }L^2(\mathbb R^d).
\]
:::

<1>3. Show that strong convergence fails.
::: proof
For every positive integer $j$,
\[
\begin{aligned}
\|f_j\|_2^2
&=\int_Q\sin^2(2\pi jx_1)\,dx\\
&=\int_0^1\sin^2(2\pi jt)\,dt\\
&=\frac12.
\end{aligned}
\]
Hence
\[
\|f_j\|_2=2^{-1/2}
\]
for every $j$, while $\|f\|_2=0$. Consequently neither
\[
\|f_j\|_2\to\|f\|_2
\]
nor
\[
\|f_j-f\|_2\to0
\]
holds.

Thus the source assertion is false as stated: the weighted pointwise decay in (A) does not rule out high-frequency oscillation and is insufficient to upgrade weak convergence to strong convergence.
:::
:::
