---
schema: qual/card@1
id: P-RASP26F
kind: problem
title: "Compactness of uniformly tight L^2 sequences via Fourier concentration"
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
  note: Checked against Problem 6 of the official UCSD Spring 2026 real-analysis qualifying exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: problem
Let $f_k \in L^2(\mathbb{R}^n)$ and $\|f_k\|_2 \leq 1$ for each $k = 1, 2, \ldots$, and assume that
$$
\lim_{R \to \infty} \sup_{k \geq 1} \int_{\mathbb{R}^n \setminus B_R(0)} (|f_k(x)|^2 + |\hat{f}_k(x)|^2)\,dx = 0
$$
with $B_R(0)$ the ball of radius $R$ centered at the origin.
Show that $\{f_k\}_{k \geq 1}$ has a convergent subsequence in $L^2(\mathbb{R}^n)$.
:::

::: solution
Let $\mathcal F$ denote the unitary Fourier transform on $L^2(\mathbb R^n)$. For $R>0$, let
\[
P_Rh:=\mathbf1_{B_R}h
\]
and let
\[
Q_Rh:=\mathcal F^{-1}(\mathbf1_{B_R}\widehat h).
\]
Thus $P_R$ truncates in physical space and $Q_R$ truncates in frequency space.

<1>1. Approximate the sequence uniformly by doubly truncated functions.
::: proof
For every $h\in L^2$,
\[
\begin{aligned}
\|h-P_RQ_Rh\|_2
&\le \|h-P_Rh\|_2
+\|P_Rh-P_RQ_Rh\|_2\\
&\le \|(1-P_R)h\|_2+\|h-Q_Rh\|_2.
\end{aligned}
\]
By Plancherel,
\[
\|h-Q_Rh\|_2^2
=\int_{\mathbb R^n\setminus B_R}|\widehat h(\xi)|^2\,d\xi.
\]
Hence for the sequence $(f_k)$,
\[
\sup_k\|f_k-P_RQ_Rf_k\|_2
\le
\sup_k\left(
\int_{\mathbb R^n\setminus B_R}|f_k|^2
\right)^{1/2}
+
\sup_k\left(
\int_{\mathbb R^n\setminus B_R}|\widehat f_k|^2
\right)^{1/2}.
\]
The hypothesis therefore implies
\[
\boxed{
\sup_k\|f_k-P_RQ_Rf_k\|_2\longrightarrow0
\quad(R\to\infty).}
\]
:::

<1>2. Show that $P_RQ_R$ is compact.
::: proof
Write
\[
P_RQ_R
=P_R\mathcal F^{-1}P_R\mathcal F,
\]
where the middle $P_R$ acts on the frequency variable. The operator
\[
A_R:=P_R\mathcal F^{-1}P_R
\]
has integral kernel
\[
K_R(x,\xi)
=\mathbf1_{B_R}(x)\mathbf1_{B_R}(\xi)e^{2\pi i x\cdot\xi}
\]
up to the harmless normalization convention for the Fourier transform. Since
\[
\int_{\mathbb R^n}\int_{\mathbb R^n}|K_R(x,\xi)|^2\,dx\,d\xi
=m(B_R)^2<\infty,
\]
$A_R$ is Hilbert--Schmidt, hence compact.

The Fourier transform $\mathcal F$ is bounded and unitary, so
\[
P_RQ_R=A_R\mathcal F
\]
is compact as well.
:::

<1>3. Prove total boundedness of $\{f_k\}$.
::: proof
Fix $\varepsilon>0$. By Step 1, choose $R$ so large that
\[
\sup_k\|f_k-P_RQ_Rf_k\|_2<\frac\varepsilon2.
\]
Since $\|f_k\|_2\le1$ and $P_RQ_R$ is compact, the set
\[
\{P_RQ_Rf_k:k\ge1\}
\]
has compact closure and therefore admits a finite $\varepsilon/2$-net in $L^2$.

For each $k$, choose a point of that finite net within $\varepsilon/2$ of $P_RQ_Rf_k$. Then the same point is within
\[
\frac\varepsilon2+rac\varepsilon2=\varepsilon
\]
of $f_k$. Hence $\{f_k:k\ge1\}$ is totally bounded in $L^2(\mathbb R^n)$.
:::

<1>4. Extract a convergent subsequence.
::: proof
Every sequence in a totally bounded metric space has a Cauchy subsequence. Since $L^2(\mathbb R^n)$ is complete, that Cauchy subsequence converges in $L^2$.

Therefore
\[
\boxed{\{f_k\}_{k\ge1}\text{ has an }L^2\text{-convergent subsequence}.}
\]
:::
:::
