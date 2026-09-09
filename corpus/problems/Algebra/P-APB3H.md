---
schema: qual/card@1
id: P-APB3H
kind: problem
title: Frobenius of $\FF_{p^n}/\FF_p$ and its characteristic polynomial
classification:
  areas:
  - algebra
  topics:
  - Finite Fields
  - Minimal and Characteristic Polynomials
  - Galois Theory
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
---

::: problem
Let $K = \mathbb{F}_{p^n}$ be the finite field extension of degree $n$ over $F = \mathbb{F}_p$.
(1) What is the Frobenius endomorphism $\operatorname{Frob}_p: K \to K$, and how does it generate the Galois group $\operatorname{Gal}(K/F)$?
(2) Viewed as an $\mathbb{F}_p$-linear transformation $T: K \to K$ on the $n$-dimensional vector space $K \cong \mathbb{F}_p^n$, what are its minimal and characteristic polynomials?
:::

::: solution
The Frobenius map is
\[
F(x)=x^p.
\]
It is an \(\mathbb F_p\)-linear field automorphism of \(K=\mathbb F_{p^n}\), and
\[
F^k(x)=x^{p^k}.
\]
Its fixed field is \(\mathbb F_p\), and \(F\) has order \(n\); hence
\[
\operatorname{Gal}(\mathbb F_{p^n}/\mathbb F_p)=\langle F\rangle\cong C_n.
\]

Viewed as an \(\mathbb F_p\)-linear operator on the \(n\)-dimensional space \(K\), the normal basis theorem gives \(\alpha\in K\) such that
\[
\alpha,F\alpha,\dots,F^{n-1}\alpha
\]
is a basis. Relative to this basis, \(F\) is the cyclic shift, so \(\alpha\) is a cyclic vector and the minimal polynomial has degree \(n\). Since \(F^n=I\), its minimal polynomial divides \(x^n-1\); therefore
\[
\mu_F(x)=x^n-1.
\]
The characteristic polynomial has degree \(n\) and is divisible by the minimal polynomial, so
\[
\chi_F(x)=x^n-1.
\]
:::
