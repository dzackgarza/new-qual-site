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
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
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

::: {.solution}
**(a).**

<1>1. Uniform integrability plus $f_n\to f$ a.e. on finite measure gives $f\in L^1$ and $\int|f_n-f|\to0$ (Vitali).
Proof: Vitali convergence theorem: truncate and use Egorov; uniform integrability controls small sets and tails (finite measure controls large sets).

<1>2. Hence $f_n\to f$ in $L^1$.
Proof: <1>1.

**(b).**

<1>1. Take $X=\R$ with Lebesgue, $f_n=\chi_{[n,n+1]}$.
Proof: example.

<1>2. For any $\epsilon>0$, choose $\delta=\epsilon$; then $|E|<\delta\Rightarrow\sup_n\int_E|f_n|=\sup_n|E\cap[n,n+1]|<\epsilon$.
Proof: uniform integrability holds.

<1>3. $f_n\to0$ a.e., but $\int|f_n|=1\not\to0$, so $f_n\not\to f$ in $L^1$.
Proof: <1>2.

<1>4. Hence finite measure is necessary.
Proof: <1>3.

<1>5. Q.E.D.
Proof: <1>2 and <1>4.
:::
