---
schema: qual/card@1
id: P-APAS20B
kind: problem
title: Singular values and Frobenius perturbation bound $\dim\ker(\phi+\psi)$
classification:
  areas:
  - applied-algebra
  topics:
  - Singular Values
  - Linear Algebra
relations: []
review: draft
---

::: problem
Suppose $\mathbb{C}^{10}$ has its usual inner product and $\phi,\psi\colon\mathbb{C}^{10}\to\mathbb{C}^{10}$ are two linear maps.
Suppose that the singular values of $\phi$ are given by $\sigma_i(\phi)=11-i$ for $1\le i\le 10$; i.e.,
\[
\sigma_1(\phi)=10,\ \sigma_2(\phi)=9,\ \sigma_3(\phi)=8,\ \ldots,\ \sigma_{10}(\phi)=1;
\]
and that the Frobenius norm $\|\psi\|_{\mathrm{Frob}}$ is exactly $1$.

(a) Show that $\dim\ker(\phi+\psi)\le 1$.

(b) Show that if $\dim\ker(\phi+\psi)=1$ then $\psi$ has rank $1$.
:::

::: solution
Let \(K=\ker(\phi+\psi)\). If \(x\in K\), then
\[
\phi x=-\psi x.
\]

For any \(k\)-dimensional subspace \(S\subset\mathbb C^{10}\) with orthonormal basis \(u_1,\ldots,u_k\), the min--max principle for singular values gives
\[
\sum_{j=1}^k\|\phi u_j\|^2\ge
\sigma_{11-k}(\phi)^2+\cdots+\sigma_{10}(\phi)^2.
\]
If \(\dim K\ge2\), choose orthonormal \(u_1,u_2\in K\). Then
\[
\|\psi\|_{\mathrm{Frob}}^2
\ge \|\psi u_1\|^2+\|\psi u_2\|^2
=\|\phi u_1\|^2+\|\phi u_2\|^2
\ge 2^2+1^2=5,
\]
contradicting \(\|\psi\|_{\mathrm{Frob}}=1\). Therefore
\[
\dim\ker(\phi+\psi)\le1.
\]

Now suppose \(\dim K=1\), and let \(u\) be a unit vector spanning \(K\). Then
\[
1=\|\psi\|_{\mathrm{Frob}}^2
\ge \|\psi u\|^2
=\|\phi u\|^2
\ge \sigma_{10}(\phi)^2=1.
\]
Hence equality holds throughout. Extend \(u\) to an orthonormal basis \(u,u_2,\ldots,u_{10}\). Since
\[
\|\psi\|_{\mathrm{Frob}}^2
=\|\psi u\|^2+\sum_{j=2}^{10}\|\psi u_j\|^2
=1,
\]
and \(\|\psi u\|^2=1\), we must have \(\psi u_j=0\) for every \(j\ge2\). Thus \(\psi\) vanishes on \(u^\perp\), so \(\operatorname{rank}\psi\le1\). Also \(\psi u=-\phi u\ne0\), because all singular values of \(\phi\) are positive. Therefore
\[
\operatorname{rank}\psi=1.
\]
:::
