---
schema: qual/card@1
id: P-RAF23F
kind: problem
title: "L^p characterization via distribution function and interpolation of weak-type bounds"
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
  note: Checked against Problem 6 of the official UCSD Fall 2023 real-analysis qualifying exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-08
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
---

::: problem
(i) Prove that for $p \geq 1$, $f \in L^p$ if and only if $\sum_{-\infty}^{+\infty} \beta^{kp} \lambda_f(\beta^k) < \infty$ for all $\beta > 1$.
Here $\lambda_f(\alpha) = \mu(\{x : |f|(x) > \alpha\})$.

(ii) Assume that $T$ is a linear operator from $L^p$ into $L^{q_1}$ and $L^{q_2}$ with $1 < q_1 < q_2$ such that $\lambda_{Tf}(2^k) \leq (C_1 \|f\|_p / 2^k)^{q_1}$ for integers $k \leq 0$; and $\lambda_{Tf}(2^\ell) \leq (C_2 \|f\|_p / 2^\ell)^{q_2}$ for integers $\ell \geq 0$.
Prove that for any $q_1 < q < q_2$, $\|Tf\|_q \leq C_q \|f\|_p$.
Here $C_q$ depends on $q, q_1, q_2$ and $C_1, C_2$.
:::

::: solution
<1>1. Prove the discrete characterization of $L^p$.
::: proof
Fix $\beta>1$ and define
\[
A_k:=\{x:\beta^k<|f(x)|\le \beta^{k+1}\}.
\]
Then the sets $A_k$ are pairwise disjoint and cover $\{|f|>0\}$ up to a null set. Hence
\[
\sum_k \beta^{kp}\mu(A_k)
\le \|f\|_p^p
\le \beta^p\sum_k\beta^{kp}\mu(A_k).
\]

Also
\[
\lambda_f(\beta^k)
=\sum_{j\ge k}\mu(A_j).
\]
Therefore, by Tonelli for nonnegative series,
\[
\begin{aligned}
\sum_{k\in\mathbb Z}\beta^{kp}\lambda_f(\beta^k)
&=\sum_j\mu(A_j)\sum_{k\le j}\beta^{kp}\\
&=\frac{\beta^p}{\beta^p-1}
\sum_j\beta^{jp}\mu(A_j).
\end{aligned}
\]
Thus
\[
\|f\|_p^p<\infty
\quad\Longleftrightarrow\quad
\sum_{k\in\mathbb Z}\beta^{kp}\lambda_f(\beta^k)<\infty.
\]
Since the argument holds for every $\beta>1$, this proves part (i).
:::

<1>2. Normalize the input for part (ii).
::: proof
If $f=0$, the conclusion is trivial. Otherwise set
\[
h:=\frac{f}{\|f\|_p}.
\]
Then $\|h\|_p=1$. By linearity,
\[
Tf=\|f\|_p\,Th.
\]
It is therefore enough to prove a bound
\[
\|Th\|_q\le C_q
\]
for all $h$ with $\|h\|_p=1$.
:::

<1>3. Sum the low-frequency distribution levels.
::: proof
For integers $k\le0$, the assumed weak-type estimate gives
\[
\lambda_{Th}(2^k)
\le C_1^{q_1}2^{-kq_1}.
\]
Hence
\[
\sum_{k\le0}2^{kq}\lambda_{Th}(2^k)
\le C_1^{q_1}
\sum_{k\le0}2^{k(q-q_1)}.
\]
Since $q>q_1$, this geometric series converges.
:::

<1>4. Sum the high-frequency distribution levels.
::: proof
For integers $k\ge0$,
\[
\lambda_{Th}(2^k)
\le C_2^{q_2}2^{-kq_2},
\]
so
\[
\sum_{k\ge0}2^{kq}\lambda_{Th}(2^k)
\le C_2^{q_2}
\sum_{k\ge0}2^{-k(q_2-q)}.
\]
Because $q<q_2$, this geometric series also converges.

Combining Steps 3 and 4 yields
\[
\sum_{k\in\mathbb Z}2^{kq}\lambda_{Th}(2^k)
\le C(q,q_1,q_2,C_1,C_2)<\infty.
\]
By part (i) with $\beta=2$, $Th\in L^q$. More quantitatively, the proof of part (i) gives
\[
\|Th\|_q^q
\le (2^q-1)
\sum_{k\in\mathbb Z}2^{kq}\lambda_{Th}(2^k),
\]
so
\[
\|Th\|_q\le C_q.
\]
Undoing the normalization,
\[
\boxed{\|Tf\|_q\le C_q\|f\|_p.}
\]
:::
:::
