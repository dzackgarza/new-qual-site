---
schema: qual/card@1
id: P-RAF18H
kind: problem
title: "Precompactness from Fourier decay"
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
  note: Checked against Problem 8 of the official UCSD Fall 2018 real-analysis qualifying exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-08
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
---

::: problem
Let $-\infty < a < b < \infty$, $C([a,b], \mathbb{R})$ be the Banach space of continuous functions on $[a,b]$ equipped with the supremum norm,
$$
\mathcal{F} := \left\{f \in L^1(\mathbb{R}, m) \cap C(\mathbb{R}, \mathbb{R}) : \int_{\mathbb{R}} (1 + |k|)\,|\hat{f}(k)|\,dk \leq 1\right\},
$$
and
$$
\mathcal{F}_{[a,b]} := \{f|_{[a,b]} : f \in \mathcal{F}\}.
$$
Show $\mathcal{F}_{[a,b]}$ is a precompact subset of $C([a,b], \mathbb{R})$.
:::

::: solution
<1>1. Use Fourier inversion to obtain a uniform bound.
::: proof
For $f\in\mathcal F$,
\[
\int_{\mathbb R}|\widehat f(k)|\,dk\le1,
\]
so $\widehat f\in L^1(\mathbb R)$. Since also $f\in L^1(\mathbb R)\cap C(\mathbb R)$, the Fourier inversion theorem applies. Thus, with the fixed constant $C_{\mathcal F}>0$ determined by the Fourier-transform normalization,
\[
f(x)=C_{\mathcal F}\int_{\mathbb R}\widehat f(k)e^{ikx}\,dk.
\]
Consequently
\[
|f(x)|
\le C_{\mathcal F}\int_{\mathbb R}|\widehat f(k)|\,dk
\le C_{\mathcal F}
\]
for every $x\in\mathbb R$. Hence the restrictions in $\mathcal F_{[a,b]}$ are uniformly bounded.
:::

<1>2. Obtain a common modulus of continuity.
::: proof
For $x,y\in\mathbb R$,
\[
\begin{aligned}
|f(x)-f(y)|
&\le C_{\mathcal F}\int_{\mathbb R}|\widehat f(k)|\,|e^{ikx}-e^{iky}|\,dk\\
&\le C_{\mathcal F}|x-y|\int_{\mathbb R}|k|\,|\widehat f(k)|\,dk\\
&\le C_{\mathcal F}|x-y|,
\end{aligned}
\]
because $|e^{iu}-e^{iv}|\le|u-v|$. Thus every $f\in\mathcal F$ is Lipschitz with the same Lipschitz constant. In particular, $\mathcal F_{[a,b]}$ is equicontinuous.
:::

<1>3. Apply Arzelà--Ascoli.
::: proof
The interval $[a,b]$ is compact. By Steps 1 and 2, the family $\mathcal F_{[a,b]}\subset C([a,b])$ is uniformly bounded and equicontinuous. The Arzelà--Ascoli theorem therefore implies that its closure in the supremum norm is compact. Equivalently,
\[
\boxed{\mathcal F_{[a,b]}\text{ is precompact in }C([a,b]).}
\]
:::
:::
