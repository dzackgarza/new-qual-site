---
schema: qual/card@1
id: E-SS5.PR-1
kind: problem
title: Zeros of a bounded holomorphic function satisfy the Blaschke condition
classification:
  areas:
  - complex-analysis
  topics:
  - Zeros
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-11
---

::: {.exercise}
Prove that if $f$ is holomorphic in the unit disc, bounded, and not identically zero, and $z_1,z_2,\ldots$ are its zeros, with $\abs{z_k}<1$, then

$$
\sum_n(1-\abs{z_n})<\infty.
$$

*Hint.* Use Jensen's formula.
:::

::: {.solution}
If $0$ is a zero of $f$, factor $f(z)=z^m g(z)$ with $g(0)\ne0$; this removes only finitely many zeros, so it suffices to treat the case $f(0)\ne0$.

Let $M=\sup_{\DD}\abs{f}$. For $0<r<1$ such that no zero lies on $\abs{z}=r$, Jensen's formula gives
$$
\log \abs{f(0)}+\sum_{\abs{z_n}<r}\log\frac r{\abs{z_n}}
=\frac1{2\pi}\int_0^{2\pi}\log\abs{f(re^{i\theta})}\,d\theta
\le \log M.
$$
Hence
$$
\sum_{\abs{z_n}<r}\log\frac r{\abs{z_n}}\le \log\frac M{\abs{f(0)}}.
\tag{1}
$$
Fix $0<R<1$ and let $r\uparrow1$ through radii larger than $R$. From (1),
$$
\sum_{\abs{z_n}<R}\log\frac1{\abs{z_n}}\le \log\frac M{\abs{f(0)}}.
$$
Letting $R\uparrow1$ and using monotone convergence for the nonnegative terms yields
$$
\sum_n\log\frac1{\abs{z_n}}<\infty.
$$
Finally, for $0<t<1$, $-\log t\ge1-t$. Therefore
$$
\sum_n(1-\abs{z_n})\le \sum_n\log\frac1{\abs{z_n}}<\infty.
$$
:::
