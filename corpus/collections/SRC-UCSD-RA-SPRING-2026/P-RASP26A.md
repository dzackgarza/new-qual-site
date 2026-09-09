---
schema: qual/card@1
id: P-RASP26A
kind: problem
title: "Equi-integrability and strong L^1 convergence"
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
  note: Checked against Problem 1 of the official UCSD Spring 2026 real-analysis qualifying exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: problem
Let $(\Omega, \mathcal{M}, \mu)$ be a measure space.
A sequence $(f_n)_n \subset L^1(\Omega, \mu)$ is equi-integrable if:

(a) for every $\epsilon > 0$ there is a $\delta > 0$ such that $\sup_n \int_E |f_n|\,d\mu < \epsilon$ for all $E \in \mathcal{M}$ with $\mu(E) < \delta$;

(b) for every $\epsilon > 0$ there is $A_\epsilon \in \mathcal{M}$ with $\mu(A_\epsilon) < +\infty$ and $\sup_n \int_{\Omega \setminus A_\epsilon} |f_n|\,d\mu < \epsilon$.

(1) Show that if $(f_n)_n$ is equi-integrable and $f_n \to f$ $\mu$-a.e., then $f \in L^1(\Omega, \mu)$ and $f_n \to f$ strongly in $L^1$.

(2) Show that if $(f_n)_n$ converges strongly in $L^1$ then condition (a) holds.
:::

::: solution
<1>1. Transfer the equi-integrability bounds to the a.e. limit.
::: proof
Assume $(f_n)$ is equi-integrable and $f_n\to f$ almost everywhere.

Fix $\varepsilon>0$. By condition (a), choose $\delta>0$ such that
\[
\mu(E)<\delta
\quad\Longrightarrow\quad
\sup_n\int_E|f_n|\,d\mu<\varepsilon.
\]
For such an $E$, Fatou's lemma gives
\[
\int_E|f|\,d\mu
\le\liminf_{n\to\infty}\int_E|f_n|\,d\mu
\le\varepsilon.
\]

Likewise, by condition (b), choose $A\in\mathcal M$ with
\[
\mu(A)<\infty
\qquad\text{and}\qquad
\sup_n\int_{\Omega\setminus A}|f_n|\,d\mu<\varepsilon.
\]
Fatou again gives
\[
\int_{\Omega\setminus A}|f|\,d\mu\le\varepsilon.
\]
Thus the same small-set and tail estimates hold for $f$.
:::

<1>2. Show that $f\in L^1$.
::: proof
Keep the finite-measure set $A$ from Step 1. By Egorov's theorem, there is a measurable set $E\subset A$ with
\[
\mu(E)<\delta
\]
such that $f_n\to f$ uniformly on $A\setminus E$.

Choose one index $N$. Uniform convergence implies that $f-f_N$ is bounded on $A\setminus E$, so
\[
\int_{A\setminus E}|f|\,d\mu
\le
\int_{A\setminus E}|f_N|\,d\mu
+\mu(A)\|f-f_N\|_{L^\infty(A\setminus E)}
<\infty.
\]
Also Step 1 gives
\[
\int_E|f|\,d\mu\le\varepsilon,
\qquad
\int_{\Omega\setminus A}|f|\,d\mu\le\varepsilon.
\]
Hence $f\in L^1(\Omega,\mu)$.
:::

<1>3. Prove strong $L^1$ convergence.
::: proof
Fix $\varepsilon>0$. Apply conditions (a) and (b) with bounds small enough that each occurrence below is at most $\varepsilon$; choose $A$ of finite measure and then, by Egorov, choose $E\subset A$ with $\mu(E)<\delta$ such that $f_n\to f$ uniformly on $A\setminus E$.

By Step 1,
\[
\int_E|f_n-f|\,d\mu
\le\int_E|f_n|\,d\mu+\int_E|f|\,d\mu
\le2\varepsilon.
\]
Similarly,
\[
\int_{\Omega\setminus A}|f_n-f|\,d\mu
\le2\varepsilon.
\]
On $A\setminus E$, uniform convergence gives
\[
\int_{A\setminus E}|f_n-f|\,d\mu
\le\mu(A)\|f_n-f\|_{L^\infty(A\setminus E)}
\longrightarrow0.
\]
Therefore
\[
\limsup_{n\to\infty}\|f_n-f\|_1\le4\varepsilon.
\]
Since $\varepsilon$ is arbitrary,
\[
\boxed{\|f_n-f\|_1\to0.}
\]
:::

<1>4. Strong $L^1$ convergence implies condition (a).
::: proof
Suppose $f_n\to f$ in $L^1$. Fix $\varepsilon>0$. Choose $N$ such that
\[
\|f_n-f\|_1<\frac\varepsilon2
\qquad(n\ge N).
\]
Since $f,f_1,\ldots,f_{N-1}\in L^1$, absolute continuity of the Lebesgue integral gives $\delta>0$ such that whenever $\mu(E)<\delta$,
\[
\int_E|f|\,d\mu<\frac\varepsilon2
\]
and
\[
\int_E|f_j|\,d\mu<\varepsilon
\qquad(1\le j<N).
\]
For $n\ge N$,
\[
\int_E|f_n|\,d\mu
\le\|f_n-f\|_1+\int_E|f|\,d\mu
<\varepsilon.
\]
Thus for every measurable $E$ with $\mu(E)<\delta$,
\[
\sup_n\int_E|f_n|\,d\mu<\varepsilon.
\]
This is condition (a).
:::
:::
