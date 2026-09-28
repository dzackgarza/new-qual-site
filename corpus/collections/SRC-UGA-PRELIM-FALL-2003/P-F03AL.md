---
schema: qual/card@1
id: P-F03AL
kind: problem
title: Convergence of series, and the alternating series test
classification:
  areas:
  - prelim
  topics:
  - Series
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
---

::: {.problem}
a) Define what is meant for an infinite series $\sum_{n=1}^\infty b_n$ of real numbers $b_n$ to converge.

b) Let $a_1, a_2, \dots$ be a sequence of positive real numbers such that $a_1 > a_2 > \cdots > a_n > a_{n+1} > \cdots$ and $\lim_{n \to \infty} a_n = 0$.
Prove that the infinite series $\sum_{n=1}^\infty (-1)^n a_n$ converges.
:::

::: {.solution}
The series $\sum_{n=1}^\infty b_n$ converges if its sequence of partial sums
\[
s_N=\sum_{n=1}^N b_n
\]
converges to a finite real number.

It is enough to prove convergence of
\[
t_N=\sum_{n=1}^N(-1)^{n+1}a_n,
\]
because the series in the question has partial sums $-t_N$.
For even indices,
\[
t_{2m}=(a_1-a_2)+(a_3-a_4)+\cdots +(a_{2m-1}-a_{2m}),
\]
so $(t_{2m})$ is increasing. Also $t_{2m}<a_1$, since
\[
t_{2m}=a_1-(a_2-a_3)-\cdots-(a_{2m-2}-a_{2m-1})-a_{2m}<a_1.
\]
Hence $t_{2m}\to L$ for some $L$.

Moreover
\[
t_{2m+1}-t_{2m}=a_{2m+1}\to0,
\]
so $t_{2m+1}\to L$ as well. Therefore the full sequence $(t_N)$ converges to $L$, and consequently
\[
\sum_{n=1}^\infty(-1)^n a_n
\]
converges to $-L$.
:::
