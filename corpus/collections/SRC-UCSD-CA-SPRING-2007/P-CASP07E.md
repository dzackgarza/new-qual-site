---
schema: qual/card@1
id: P-CASP07E
kind: problem
title: "Infinite product convergence and zeros for products of (1 - α_n z^n)"
classification:
  areas:
  - complex-analysis
  topics:
  - Complex Analysis
relations: []
review: draft
---

::: problem
Let $\{\alpha_n\}_{n=1}^{\infty}$ be positive numbers such that $\lim_{n \to \infty} \alpha_n^{1/n} = \lambda$.
Define $q_n(z) := 1 - \alpha_n z^n$ and $r = 1/\lambda$.
Show that the infinite product $\prod_{n=1}^{\infty} q_n(z)$ converges in $\mathcal{O}(B(0, r))$ to an analytic function whose zeros (counting multiplicities) inside $B(0, r)$ are precisely those of the $q_n(z)$.
:::

::: solution
Let $0<\rho<r=1/\lambda$. Choose $q$ with
\[
\lambda\rho<q<1.
\]
Since $\alpha_n^{1/n}\to\lambda$, for all sufficiently large $n$,
\[
\alpha_n^{1/n}\rho\le q.
\]
Hence for $|z|\le\rho$,
\[
|\alpha_n z^n|
\le (\alpha_n^{1/n}\rho)^n
\le q^n.
\]
Therefore
\[
\sum_{n=1}^\infty \sup_{|z|\le\rho}|\alpha_n z^n|<\infty.
\]
The standard theorem on normally convergent infinite products now shows that
\[
\prod_{n=1}^\infty(1-\alpha_nz^n)
\]
converges uniformly on $|z|\le\rho$. Since every compact subset of $B(0,r)$
lies in such a disk, the product converges in $\mathcal O(B(0,r))$ to a
holomorphic function $Q$.

Moreover, on any compact set avoiding the zeros of all factors, the tail
product converges to a nonzero holomorphic function because
$\sum|\alpha_nz^n|$ converges uniformly there. Thus $Q$ has no zeros except
those already supplied by the factors $q_n$. At a zero $z_0$ of finitely many
factors, the remaining nonvanishing product is holomorphic and nonzero near
$z_0$, so the multiplicity of $Q$ is exactly the sum of the multiplicities
contributed by those factors. Hence the zeros of $Q$ in $B(0,r)$, counted with
multiplicity, are precisely the zeros of the $q_n$.
:::
