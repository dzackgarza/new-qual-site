---
schema: qual/card@1
id: P-JHUSP08AND
kind: problem
title: "Boundedness of an operator on l2 from its matrix coefficients"
classification:
  areas:
  - real-analysis
  topics:
  - Hilbert Spaces
  - Bounded Operators
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-08
  note: Checked against Problem 4 of the JHU Analysis Qualifying Exam, Spring 2008. The source statement is too strong for an arbitrary everywhere-defined algebraic linear map, because matrix coefficients determine the map only on the finite-support subspace. The card is corrected to the intended matrix-defined operator formulation.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-08
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
---

::: {.problem}
Let $c_{00}\subset\ell^2$ be the finitely supported sequences, with standard basis $(e_m)$. Suppose a linear operator $T:c_{00}\to\ell^2$ has matrix coefficients
\[
a_{mn}=\langle Te_m,e_n\rangle.
\]

(a) Assume
\[
\sum_{m,n=1}^\infty |a_{mn}|^2<\infty.
\]
Show that $T$ is bounded on $c_{00}$ and therefore extends uniquely to a bounded operator on $\ell^2$.

(b) If instead only
\[
\sup_{m,n}|a_{mn}|<\infty,
\]
must $T$ extend boundedly to $\ell^2$? Explain.
:::

::: {.solution}
<1>1. Square-summable matrix coefficients give a bounded operator.
::: {.proof}
Let $x=\sum_m x_m e_m\in c_{00}$. For each $n$,
\[
(Tx)_n=\sum_m a_{mn}x_m.
\]
Hence, by Cauchy--Schwarz in the $m$-sum,
\[
|(Tx)_n|^2
\le
\left(\sum_m|a_{mn}|^2\right)
\left(\sum_m|x_m|^2\right).
\]
Summing over $n$ gives
\[
\begin{aligned}
\|Tx\|_2^2
&=\sum_n|(Tx)_n|^2\\
&\le
\left(\sum_{m,n}|a_{mn}|^2\right)\|x\|_2^2.
\end{aligned}
\]
Thus
\[
\|Tx\|_2\le
\left(\sum_{m,n}|a_{mn}|^2\right)^{1/2}\|x\|_2.
\]
Since $c_{00}$ is dense in $\ell^2$, $T$ extends uniquely by continuity to a bounded operator on $\ell^2$.
:::

<1>2. Uniformly bounded entries do not suffice.
::: {.proof}
Define $T:c_{00}\to\ell^2$ on the basis by
\[
Te_m=e_1+e_2+\cdots+e_m.
\]
Then
\[
a_{mn}=\langle Te_m,e_n\rangle
=
\begin{cases}
1,&n\le m,\\
0,&n>m,
\end{cases}
\]
so
\[
\sup_{m,n}|a_{mn}|=1.
\]
However,
\[
\|Te_m\|_2=\sqrt m,
\qquad
\|e_m\|_2=1.
\]
Therefore $T$ is unbounded on $c_{00}$ and cannot extend to a bounded operator on $\ell^2$.
:::

The source's literal formulation with an arbitrary algebraic map $T:\ell^2\to\ell^2$ cannot support part (a): an everywhere-defined discontinuous linear map can vanish on every $e_m$ and still be nonzero off the dense subspace $c_{00}$, so all its matrix coefficients can vanish while the map is unbounded. The corrected formulation above is the standard intended statement.
:::
