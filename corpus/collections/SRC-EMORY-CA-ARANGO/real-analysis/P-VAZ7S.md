---
schema: qual/card@1
id: P-VAZ7S
kind: problem
title: $\lim_{p\to\infty}\|f\|_p=\|f\|_\infty$ on a finite measure space
classification:
  areas:
  - real-analysis
  topics:
  - Lp Spaces
  - L∞
  - Limits
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-10
  note: The preserved Arango document is solutions-only at this point, so the problem statement is reconstructed from the solution. The prior proof omitted the finite-measure factor in the upper bound and used f rather than |f| in the essential-supremum lower bound.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-10
---

::: problem
[Reconstructed from solution — no problem statement page was present in this solutions-only document.] Let $(X,\mathcal M,\mu)$ be a finite measure space and let $f\in L^\infty(X,\mu)$.
Show that
\[
\lim_{p\to\infty}\|f\|_p=\|f\|_\infty.
\]
:::

::: solution
<1>1. Handle the degenerate cases.
::: proof
If $\mu(X)=0$, then every $L^p$ norm and the essential-supremum norm are zero. If $\|f\|_\infty=0$, then $f=0$ almost everywhere and the conclusion is again immediate. Hence assume
\[
0<\mu(X)<\infty,
\qquad
M:=\|f\|_\infty>0.
\]
:::

<1>2. Prove the upper bound.
::: proof
Since $|f|\le M$ almost everywhere,
\[
\|f\|_p^p=\int_X|f|^p\,d\mu\le M^p\mu(X).
\]
Therefore
\[
\|f\|_p\le M\mu(X)^{1/p}.
\]
As $p\to\infty$, $\mu(X)^{1/p}\to1$, so
\[
\limsup_{p\to\infty}\|f\|_p\le M.
\]
:::

<1>3. Prove the lower bound from the definition of essential supremum.
::: proof
Fix $0<\varepsilon<M$ and set
\[
A_\varepsilon=\{x\in X:|f(x)|>M-\varepsilon\}.
\]
By the definition of essential supremum,
\[
\mu(A_\varepsilon)>0.
\]
Hence
\[
\begin{aligned}
\|f\|_p^p
&=\int_X|f|^p\,d\mu\\
&\ge\int_{A_\varepsilon}|f|^p\,d\mu\\
&\ge (M-\varepsilon)^p\mu(A_\varepsilon).
\end{aligned}
\]
Thus
\[
\|f\|_p\ge (M-\varepsilon)\mu(A_\varepsilon)^{1/p}.
\]
Letting $p\to\infty$ gives
\[
\liminf_{p\to\infty}\|f\|_p\ge M-\varepsilon.
\]
Since $\varepsilon>0$ is arbitrary,
\[
\liminf_{p\to\infty}\|f\|_p\ge M.
\]
:::

<1>4. Conclude.
::: proof
Combining Steps 2 and 3,
\[
M\le\liminf_{p\to\infty}\|f\|_p
\le\limsup_{p\to\infty}\|f\|_p\le M.
\]
Therefore
\[
\boxed{\lim_{p\to\infty}\|f\|_p=\|f\|_\infty.}
\]
:::
:::
