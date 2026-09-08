---
schema: qual/card@1
id: P-JHUMAY11ANL
kind: problem
title: 'The translation operator on $L^2$ of the line'
classification:
  areas:
  - real-analysis
  topics:
  - Operator Theory
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-08
  note: Checked against Problem 4 of the JHU Analysis Qualifying Exam, May 2011, in the preserved exam collection.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-08
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
---

::: {.problem}
Define $U:L^2(\mathbb R)\to L^2(\mathbb R)$ by
\[
Uf(x)=f(x-1).
\]
Show that if $Uf=\lambda f$ for some real $\lambda$, then $f=0$ almost everywhere.
:::

::: {.solution}
The translation operator is unitary:
\[
\|Uf\|_2=\|f\|_2.
\]
If $Uf=\lambda f$ and $f\ne0$, then
\[
\|f\|_2=\|Uf\|_2=|\lambda|\,\|f\|_2,
\]
so $|\lambda|=1$. Since $\lambda$ is real, $\lambda=\pm1$. Therefore
\[
|f(x-1)|=|f(x)|
\]
for almost every $x$, so $|f|^2$ is 1-periodic almost everywhere.

Let
\[
c=\int_0^1|f(x)|^2\,dx.
\]
By periodicity, for every integer $k$,
\[
\int_k^{k+1}|f(x)|^2\,dx=c.
\]
Hence
\[
\|f\|_2^2=\sum_{k\in\mathbb Z}c.
\]
Since $f\in L^2(\mathbb R)$, this sum is finite, forcing $c=0$. Thus $f=0$ almost everywhere on $[0,1]$, and periodicity then gives $f=0$ almost everywhere on all of $\mathbb R$.

Therefore the translation operator has no nonzero real eigenvectors.
:::
