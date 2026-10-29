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

::: {.problem}
Let $K = \FF_{p^n}$ be the finite field extension of degree $n$ over $F = \FF_p$.

(a) What is the Frobenius endomorphism $\operatorname{Frob}_p: K \to K$, and how does it generate the Galois group $\Gal(K/F)$?

(b) Viewed as an $\FF_p$-linear transformation $T: K \to K$ on the $n$-dimensional vector space $K \cong \FF_p^n$, what are its minimal and characteristic polynomials?
:::

::: {.solution}
Write $\varphi=\operatorname{Frob}_p$.

::: pf

::: pf-step

(a) $\boxed{\varphi(x)=x^p}$, and $\Gal(K/F)=\langle\varphi\rangle\cong C_n$.

::: pf-proof

In characteristic $p$, $(x+y)^p=x^p+y^p$ and $(xy)^p=x^py^p$, so $\varphi$ is a ring endomorphism of $K$. It is injective because $K$ is a field, hence bijective because $K$ is finite. It fixes $\FF_p$ by Fermat's little theorem, so $\varphi\in\Gal(K/F)$.

For $k\ge1$, $\varphi^k(x)=x^{p^k}$. The fixed points of $\varphi^k$ are the roots of $x^{p^k}-x$, of which there are at most $p^k$. For $1\le k<n$ this is fewer than $\abs{K}=p^n$, so $\varphi^k\ne\id$. Since $x^{p^n}=x$ for every $x\in K$, $\varphi^n=\id$. Thus $\varphi$ has order $n$. Because $K/F$ is Galois of degree $n$, $\abs{\Gal(K/F)}=n$, so $\Gal(K/F)=\langle\varphi\rangle\cong C_n$.

:::

:::

::: pf-step

(b) The minimal and characteristic polynomials of $T=\varphi$ are both $\boxed{x^n-1}$.

::: pf-proof

Since $\varphi^n=\id$, the minimal polynomial $\mu_T$ divides $x^n-1$. If $\mu_T$ had degree $d<n$, then $\id,\varphi,\ldots,\varphi^{d}$ would be linearly dependent over $\FF_p\subseteq K$, contradicting Dedekind's lemma on the linear independence of the distinct automorphisms $\id,\varphi,\ldots,\varphi^{n-1}$ of $K$. Hence $\deg\mu_T=n$ and $\mu_T(x)=x^n-1$. The characteristic polynomial $\chi_T$ is monic of degree $n=\dim_{\FF_p}K$ and divisible by $\mu_T$, so $\chi_T(x)=x^n-1$.

:::

:::

:::

:::
