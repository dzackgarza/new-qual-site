---
schema: qual/card@1
id: E-S7K3V
kind: problem
title: Local compactness of balls versus completeness
classification:
  areas:
  - topology
  topics:
  - Metric Spaces
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: {.exercise}

Let $X$ be a metric space.

(a) Suppose that for some $\epsilon > 0$, every $\epsilon$-ball in $X$ has compact closure.
Show that $X$ is complete.

(b) Suppose that for each $x \in X$ there is an $\epsilon > 0$ such that the ball $B(x, \epsilon)$ has compact closure.
Show by means of an example that $X$ need not be complete.
:::

::: {.solution}
(a) Let \((x_n)\) be a Cauchy sequence. Choose \(N\) such that
\[
d(x_n,x_N)<\varepsilon/2\qquad(n\ge N).
\]
Then the tail of the sequence lies in \(B(x_N,\varepsilon)\), whose closure is compact by hypothesis. Hence the tail has a convergent subsequence \(x_{n_k}\to x\). Since the original sequence is Cauchy, a standard \(arepsilon/2\) argument shows the whole sequence converges to the same \(x\): given \(\eta>0\), choose \(N_1\) so \(d(x_m,x_n)<\eta/2\) for \(m,n\ge N_1\), then choose \(k\) with \(n_k\ge N_1\) and \(d(x_{n_k},x)<\eta/2\). For \(n\ge N_1\),
\[
d(x_n,x)<\eta.
\]
Thus every Cauchy sequence converges and \(X\) is complete.

(b) Take
\[
X=(0,1)
\]
with the usual metric. For each \(x\in(0,1)\), choose
\[
0<r<\min\{x,1-x\}.
\]
Then the closure in \(X\) of \(B(x,r)\) is the ordinary closed interval \([x-r,x+r]\), which is compact. Thus every point has a ball with compact closure.

Nevertheless \(X\) is not complete: the sequence \(x_n=1/n\) is Cauchy in \(X\) but has no limit in \(X\). Hence the local hypothesis in (b) does not imply completeness.
:::
