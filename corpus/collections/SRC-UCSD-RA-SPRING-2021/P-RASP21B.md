---
schema: qual/card@1
id: P-RASP21B
kind: problem
title: "Uniform integrability and convergence in measure"
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
  note: Checked against Problem 2 of the official UCSD Spring 2021 real-analysis qualifying exam. The card's definition had moved the quantifiers so that delta could depend on f and E; the source requires one delta working uniformly for all f in the family and all measurable E of sufficiently small measure.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: problem
$\mathcal F\subseteq L^1(\mu)$ is uniformly integrable if for every $\varepsilon>0$ there exists $\delta>0$ such that $|\int_E f\,d\mu|<\varepsilon$ whenever $f\in\mathcal F$ and $E\in\mathcal M$ satisfy $\mu(E)<\delta$.

(a) If $p \in (1, \infty]$ and $\mathcal{F}$ is bounded in $L^p(\mu)$, prove that $\mathcal{F}$ is uniformly integrable.

(b) Give an example where (a) fails for $p = 1$.

(c) Let $f_n, f \in L^1(\mu)$ and assume that $\mathcal{F} = \{f_1, f_2, \ldots\}$ is uniformly integrable.
If $f_n \to f$ in measure, prove that $f_n \to f$ in $L^1(\mu)$.
:::


::: solution
<1>1. Prove part (a).
::: proof
Assume first that $1<p<\infty$, and let $q=p/(p-1)$. If
\[
M:=\sup_{f\in\mathcal F}\|f\|_p<\infty,
\]
then Hölder's inequality gives, for every measurable $E$,
\[
\left|\int_E f\,d\mu\right|
\le \int_E|f|\,d\mu
\le \|f\|_p\,\mu(E)^{1/q}
\le M\mu(E)^{1/q}.
\]
Thus a single sufficiently small $\delta$ works for every $f\in\mathcal F$.

If $p=\infty$, then
\[
\left|\int_E f\,d\mu\right|
\le \|f\|_\infty\mu(E)
\le M\mu(E),
\]
so the same conclusion holds. Hence every bounded subset of $L^p$, $p>1$, is uniformly integrable in the stated sense.
:::

<1>2. Give the counterexample for $p=1$.
::: proof
Take $X=[0,1]$ with Lebesgue measure and
\[
f_n=n\mathbf1_{(0,1/n)}.
\]
Then
\[
\|f_n\|_1=1
\]
for every $n$, so the family is bounded in $L^1$. But for every $\delta>0$ choose $n>1/\delta$ and put $E=(0,1/n)$. Then
\[
m(E)<\delta,
\qquad
\left|\int_Ef_n\,dm\right|=1.
\]
Thus the family is not uniformly integrable.
:::

<1>3. Convert the source's signed-integral condition into absolute-integral control.
::: proof
For real-valued $h$, suppose that
\[
\left|\int_Ah\,d\mu\right|<\eta
\]
for every measurable $A$ with $\mu(A)<\delta$. If $E$ has $\mu(E)<\delta$, apply this to
\[
E_+=E\cap\{h\ge0\},
\qquad
E_-=E\cap\{h<0\}.
\]
Then
\[
\int_E|h|\,d\mu
=\int_{E_+}h\,d\mu-\int_{E_-}h\,d\mu
<2\eta.
\]
For complex-valued functions, apply the same argument to the real and imaginary parts; changing the constant by an inessential factor gives the usual uniform estimate
\[
\sup_{h\in\mathcal F}\int_E|h|\,d\mu\longrightarrow0
\quad\text{as }\mu(E)\to0.
\]
Thus the source's formulation implies the standard absolute-integral form of uniform integrability.
:::

<1>4. Show that the limit $f$ has the same small-set control.
::: proof
Since $f_n\to f$ in measure, every subsequence has a further subsequence converging to $f$ almost everywhere; in particular choose $f_{n_k}\to f$ a.e. If $\mu(E)<\delta$, Fatou's lemma gives
\[
\int_E|f|\,d\mu
\le \liminf_{k\to\infty}\int_E|f_{n_k}|\,d\mu.
\]
Hence the same small-set bound that holds uniformly for the $f_n$ also holds for $f$. Consequently the differences $f_n-f$ are uniformly integrable in the absolute-integral sense, since
\[
\int_E|f_n-f|\,d\mu
\le \int_E|f_n|\,d\mu+\int_E|f|\,d\mu.
\]
:::

<1>5. Use convergence in measure to conclude $L^1$ convergence.
::: proof
Let $\varepsilon>0$. Choose $\delta>0$ so that
\[
\mu(E)<\delta
\quad\Longrightarrow\quad
\sup_n\int_E|f_n-f|\,d\mu<\frac\varepsilon2.
\]
Because $\mu(X)<\infty$, choose $\eta>0$ with
\[
\eta\mu(X)<\frac\varepsilon2.
\]
Since $f_n\to f$ in measure,
\[
E_n:=\{|f_n-f|>\eta\}
\]
satisfies $\mu(E_n)<\delta$ for all sufficiently large $n$. Therefore
\[
\begin{aligned}
\|f_n-f\|_1
&=\int_{X\setminus E_n}|f_n-f|\,d\mu
 +\int_{E_n}|f_n-f|\,d\mu\\
&\le \eta\mu(X)+\frac\varepsilon2
<\varepsilon.
\end{aligned}
\]
Hence
\[
\boxed{f_n\to f\text{ in }L^1(\mu).}
\]
:::
:::
