---
schema: qual/card@1
id: E-XIT36
kind: problem
title: Application of summation by parts
classification:
  areas:
  - complex-analysis
  topics:
  - Convergence Tests
  - Series of Numbers
  - Trigonometry
relations: []
review: draft
---

::: {.exercise}
Use summation by parts to show that $\sin(n)/n$ converges.
:::

::: solution
As written, $\sin(n)/n$ is a sequence rather than a series, and its
convergence is immediate:
\[
\left|{\sin n\over n}\right|\le {1\over n}\longrightarrow0.
\]
Thus the displayed sequence converges to $0$; summation by parts is not needed
for this assertion.

The standard summation-by-parts exercise suggested by the wording is the
convergence of
\[
\sum_{n=1}^\infty {\sin n\over n}.
\]
For that corrected statement, put
\[
B_N=\sum_{n=1}^N\sin n.
\]
Using a geometric sum,
\[
\sum_{n=1}^N e^{in}
=e^i{1-e^{iN}\over1-e^i},
\]
so $(B_N)$ is bounded. Summation by parts gives, for $N>M$,
\[
\sum_{n=M}^N {\sin n\over n}
={B_N\over N}-{B_{M-1}\over M}
+\sum_{n=M}^{N-1}B_n\left({1\over n}-{1\over n+1}\right).
\]
If $|B_n|\le C$, the absolute value of the right-hand side is at most
\[
{C\over N}+{C\over M}
+C\sum_{n=M}^{N-1}\left({1\over n}-{1\over n+1}\right)
\le {3C\over M},
\]
which tends to $0$ as $M\to\infty$. Hence the corrected series is Cauchy and
therefore convergent.
:::
