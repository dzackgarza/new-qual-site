---
schema: qual/card@1
id: P-RAF11D
kind: problem
title: "Convolution with L^1 kernel preserves weak L^2 convergence"
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
  note: Checked against Problem 4 of the official UCSD Fall 2011 real-analysis qualifying exam.
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-30
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
---

::: problem
Let $K \in L^1(\mathbb{R}^d)$ with Lebesgue measure.
Suppose that $\psi_n \in L^2(\mathbb{R}^d)$ is a sequence of functions such that $\psi_n \to \psi$ (weak $L^2$ convergence), and also with the property that $\psi_n \equiv 0$ for $|x| > 1$.
Show that
$$
f_n(x) = \int_{\mathbb{R}^d} K(x-y)\,\psi_n(y)\,dy
$$
converges to
$$
f(x) = \int_{\mathbb{R}^d} K(x-y)\,\psi(y)\,dy
$$
strongly in $L^2(\mathbb{R}^d)$.
:::

::: solution
<1>1. The weak limit is also supported in the unit ball.
::: proof
Let
\[
B:=\{x\in\mathbb R^d:|x|\le1\}.
\]
If $h\in L^2(\mathbb R^d)$ is supported in $B^c$, then
\[
\langle \psi_n,h\rangle=0
\]
for every $n$. Passing to the weak limit gives
\[
\langle \psi,h\rangle=0.
\]
Taking $h=\psi\mathbf1_{B^c}$ shows
\[
\psi=0
\]
almost everywhere on $B^c$. Thus both $\psi_n$ and $\psi$ may be regarded as elements of $L^2(B)$, extended by zero outside $B$.
:::

<1>2. Define the restricted convolution operator and prove it is bounded.
::: proof
For $u\in L^2(B)$, extend $u$ by zero to $\mathbb R^d$ and set
\[
T_Ku:=K*u.
\]
Young's convolution inequality gives
\[
\|T_Ku\|_{L^2(\mathbb R^d)}
\le \|K\|_1\|u\|_2.
\]
Hence
\[
T_K:L^2(B)\to L^2(\mathbb R^d)
\]
is bounded.
:::

<1>3. Approximate $T_K$ in operator norm by Hilbert--Schmidt operators.
::: proof
Choose $K_m\in C_c(\mathbb R^d)$ such that
\[
\|K_m-K\|_1\longrightarrow0.
\]
For $u\in L^2(B)$, Young's inequality gives
\[
\|(T_{K_m}-T_K)u\|_2
\le \|K_m-K\|_1\|u\|_2.
\]
Therefore
\[
\|T_{K_m}-T_K\|_{L^2(B)\to L^2(\mathbb R^d)}
\le \|K_m-K\|_1\longrightarrow0.
\]

For each $m$, the operator $T_{K_m}$ has integral kernel
\[
k_m(x,y)=K_m(x-y),
\qquad
x\in\mathbb R^d,\ y\in B.
\]
Since $K_m\in L^2(\mathbb R^d)$,
\[
\begin{aligned}
\int_B\int_{\mathbb R^d}|k_m(x,y)|^2\,dx\,dy
&=\int_B\int_{\mathbb R^d}|K_m(x-y)|^2\,dx\,dy\\
&=|B|\,\|K_m\|_2^2<\infty.
\end{aligned}
\]
Thus $T_{K_m}$ is Hilbert--Schmidt, hence compact. Since compact operators are closed in the operator norm, $T_K$ is compact.
:::

<1>4. Compact operators send weakly convergent sequences to norm-convergent sequences.
::: proof
We have
\[
\psi_n\rightharpoonup\psi
\]
in $L^2(B)$. Suppose, contrary to the desired conclusion, that
\[
\|T_K\psi_n-T_K\psi\|_2\not\to0.
\]
Then some subsequence satisfies
\[
\|T_K\psi_{n_j}-T_K\psi\|_2\ge\varepsilon>0.
\]
Compactness of $T_K$ gives a further subsequence for which $T_K\psi_{n_{j_\ell}}$ converges strongly to some $v$. On the other hand, bounded linear maps are weak-to-weak continuous, so
\[
T_K\psi_{n_{j_\ell}}\rightharpoonup T_K\psi.
\]
Strong convergence also implies weak convergence to $v$, hence uniqueness of weak limits gives
\[
v=T_K\psi,
\]
contradicting the lower bound by $\varepsilon$. Therefore
\[
\|T_K\psi_n-T_K\psi\|_2\to0.
\]
Since $f_n=T_K\psi_n$ and $f=T_K\psi$, this is exactly
\[
\boxed{f_n\to f\text{ strongly in }L^2(\mathbb R^d).}
\]
:::
:::
