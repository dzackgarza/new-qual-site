---
schema: qual/card@1
id: P-RAF11C
kind: problem
title: "Uniform integrability and convergence in L^1"
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
  note: Checked against Problem 3 of the official UCSD Fall 2011 real-analysis qualifying exam.
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
---

::: problem
(a) Let $(X, \mathcal{M}, \mu)$ be a finite measure space.
Suppose that $f_n \in L^1(d\mu)$ is a sequence of functions with the property that for every $\epsilon > 0$ there exists a $\delta > 0$ such that for all $E \in \mathcal{M}$:
$$
|E| < \delta \implies \sup_n \int_E |f_n|\,d\mu < \epsilon.
$$
Suppose in addition that there exists $f$ with $f_n \to f$ $\mu$-a.e. Show that $f_n \to f$ in $L^1(d\mu)$.

(b) Give a simple example to show that if one drops the finite measure assumption but keeps all the other hypotheses above, the conclusion can fail.
:::

::: solution
<1>1. The limit inherits the small-set integral bound.
::: proof
Fix $\varepsilon>0$. By hypothesis there is $\delta>0$ such that
\[
\mu(E)<\delta
\quad\Longrightarrow\quad
\sup_n\int_E|f_n|\,d\mu<\varepsilon.
\]
For such an $E$, Fatou's lemma and $f_n\to f$ almost everywhere give
\[
\int_E|f|\,d\mu
\le \liminf_{n\to\infty}\int_E|f_n|\,d\mu
\le\varepsilon.
\]
Consequently
\[
\int_E|f_n-f|\,d\mu
\le\int_E|f_n|\,d\mu+\int_E|f|\,d\mu
<2\varepsilon
\]
for every $n$.
:::

<1>2. Use Egorov's theorem away from a small exceptional set.
::: proof
Let $\eta>0$. Apply Step 1 with $\varepsilon=\eta/4$ and obtain the corresponding $\delta>0$. Since $\mu(X)<\infty$ and $f_n\to f$ almost everywhere, Egorov's theorem gives a measurable set $E\subseteq X$ such that
\[
\mu(E)<\delta
\]
and $f_n\to f$ uniformly on $X\setminus E$.

For all sufficiently large $n$,
\[
\sup_{X\setminus E}|f_n-f|<\frac{\eta}{2\mu(X)}
\]
when $\mu(X)>0$; the case $\mu(X)=0$ is trivial. Hence
\[
\int_{X\setminus E}|f_n-f|\,d\mu<\frac\eta2.
\]
By Step 1,
\[
\int_E|f_n-f|\,d\mu<\frac\eta2.
\]
Therefore
\[
\|f_n-f\|_1<\eta
\]
for all sufficiently large $n$. Thus
\[
\boxed{f_n\to f\text{ in }L^1(d\mu).}
\]
In particular, $f\in L^1(d\mu)$.
:::

<1>3. Give a counterexample on an infinite-measure space.
::: proof
Take $X=\mathbb R$ with Lebesgue measure and
\[
f_n=\mathbf1_{[n,n+1]}.
\]
For every $\varepsilon>0$, choose $\delta=\varepsilon$. If $m(E)<\delta$, then
\[
\sup_n\int_E|f_n|\,dm
=\sup_n m(E\cap[n,n+1])
\le m(E)<\varepsilon.
\]
Thus the stated uniform small-set condition holds. Also $f_n(x)\to0$ for every $x\in\mathbb R$. Nevertheless
\[
\|f_n\|_1=1
\]
for every $n$, so $f_n$ does not converge to $0$ in $L^1$. Hence finiteness of $\mu(X)$ cannot be dropped.
:::
:::
