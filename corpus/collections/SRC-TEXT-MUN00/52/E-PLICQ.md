---
schema: qual/card@1
id: E-PLICQ
kind: problem
title: Abelian fundamental groups and base-point independence
classification:
  areas:
  - topology
  topics:
  - Fundamental Group
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-10
---

::: {.exercise}

Let $x_0$ and $x_1$ be points of the path-connected space $X$.
Show that $\pi_1(X, x_0)$ is abelian if and only if for every pair $\alpha$ and $\beta$ of paths from $x_0$ to $x_1$, we have $\hat{\alpha} = \hat{\beta}$.
:::

::: {.solution}
For two paths \(\alpha,\beta:x_0\to x_1\), set
\[
\lambda=\alpha*\bar\beta,
\]
a loop at \(x_0\). For any loop \(f\) at \(x_0\), a direct path calculation gives
\[
\widehat\beta^{-1}\widehat\alpha([f])
=[\lambda^{-1}*f*\lambda],
\]
so \(\widehat\beta^{-1}\widehat\alpha\) is the inner automorphism determined by \([\lambda]\in\pi_1(X,x_0)\).

If \(\pi_1(X,x_0)\) is abelian, every inner automorphism is the identity. Hence
\[
\widehat\beta^{-1}\widehat\alpha=\operatorname{id},
\]
so \(\widehat\alpha=\widehat\beta\) for every \(\alpha,\beta\).

Conversely, suppose \(\widehat\alpha=\widehat\beta\) for every pair of paths from \(x_0\) to \(x_1\). Fix one path \(\beta:x_0\to x_1\). For an arbitrary loop \(\lambda\) at \(x_0\), put
\[
\alpha=\lambda*\beta.
\]
Then the displayed calculation shows that the inner automorphism induced by \([\lambda]\) is the identity. Since \([\lambda]\) was arbitrary, every element of \(\pi_1(X,x_0)\) is central. Thus \(\pi_1(X,x_0)\) is abelian.
:::
