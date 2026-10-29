---
schema: qual/card@1
id: T-OTR5M
kind: theorem
title: Borel--Cantelli lemma
slogan: 'If $\sum_k \mu(E_k)<\infty$, then almost every point lies in only finitely many of the sets $E_k$.'
prompts:
- What is the Borel-Cantelli lemma?
classification:
  areas:
  - real-analysis
  topics:
  - Borel-Cantelli
  - Measure Theory
relations: []
review: draft
---

::: {.theorem}
Let $(X,\mcm,\mu)$ be a [[D-QYLPH|measure]] space and let $(E_k)_{k\geq1}$ be a sequence in $\mcm$ with
$$
\sum_{k=1}^\infty \mu(E_k) < \infty .
$$
Then the [[D-PAEDW|limit superior]] $\limsup_k E_k$ lies in $\mcm$ and $\mu\qty{\limsup_{k\to\infty} E_k} = 0$; equivalently, almost every $x\in X$ lies in only finitely many of the sets $E_k$.
:::

::: {.proof}
We have $\limsup_k E_k = \bigcap_{n\geq 1}\bigcup_{k\geq n} E_k$, a countable intersection of countable unions of sets in $\mcm$, so it lies in $\mcm$; it is the set of points lying in infinitely many $E_k$.
For every $n\geq 1$, $\limsup_k E_k\subseteq\bigcup_{k\geq n}E_k$, so by countable subadditivity
$$
\mu\qty{\limsup_k E_k}\leq\sum_{k\geq n}\mu(E_k).
$$
The right side is the tail of a convergent series, so it tends to $0$ as $n\to\infty$.
:::

::: {.remark}
For Lebesgue measure $m$ on $\RR^n$ and [[D-MDJII|Lebesgue measurable]] sets $E_k$ with $\sum_k m(E_k)<\infty$, almost every $x\in\RR^n$ lies in only finitely many $E_k$.
For a probability measure $P$ and events $E_k$ with $\sum_k P(E_k)<\infty$, with probability $0$ infinitely many of the events $E_k$ occur.
:::

::: {.remark title="Second Borel--Cantelli lemma"}
On a probability space $(\Omega,\mcf,P)$, if the events $E_n$ are independent and $\sum_{n\geq 1} P(E_n) = \infty$, then $P(\limsup_n E_n) = 1$.

The complement of $\limsup_n E_n$ is $\bigcup_{N\geq 1}\bigcap_{n\geq N}E_n^c$.
For $M\geq N$, independence and $1-t\leq e^{-t}$ give
$$
P\qty{\bigcap_{n=N}^{M}E_n^c} = \prod_{n=N}^{M}(1-P(E_n))\leq\exp\qty{-\sum_{n=N}^{M}P(E_n)}\convergesto{M\to\infty} 0 ,
$$
so $P\qty{\bigcap_{n\geq N}E_n^c} = 0$ for every $N$, and the countable union of these null events is null.
:::
