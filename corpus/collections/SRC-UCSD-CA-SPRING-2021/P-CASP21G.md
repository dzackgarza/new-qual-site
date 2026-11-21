---
schema: qual/card@1
id: P-CASP21G
kind: problem
title: "Locally uniform limit of disc automorphisms is an automorphism"
classification:
  areas:
  - complex-analysis
  topics:
  - Automorphisms
  - Normal Families
  - Holomorphic Functions
relations: []
review: draft
audit:
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Lamport structure, with the forward reference removed and two gaps filled: the prose used "the family of holomorphic self-maps of the disc is normal" and then "the identity above shows g is nonconstant" before that identity was available, and it did not prove that f maps into the disk (which is what makes f(z) an interior point later). The card now proves |f| < 1 by the maximum modulus principle, orders the steps so that g o f = id precedes the use of it, proves g(D) ⊂ D the same way, and argues both composites with explicit compact discs and uniform convergence on them. No retained solution set covers the exercise; the card says the argument is its own.
---

::: {.problem}
Let $\{f_n\}$ be a sequence of automorphisms of the unit disc $\DD$, converging locally uniformly in $\DD$ to a nonconstant function $f$.
Show that $f$ is an automorphism of $\DD$.

Hint: Examine the family $\mathcal{F}$ consisting of the inverse automorphisms $f_n^{-1} : \DD \to \DD$.
:::

::: {.solution}
The collection's provenance is the examination paper alone, so no retained solution set covers this exercise; the argument is the card's own, following the hint.

Write $g_n=f_n^{-1}$, an automorphism of $\DD$ for each $n$.

::: pf

::: {.pf-step #finto}
$\abs{f(z)}<1$ for every $z\in\DD$, so $f$ maps $\DD$ into $\DD$.

::: pf-proof
$\abs{f_n}\le1$ on $\DD$ for every $n$, so the pointwise limit satisfies $\abs{f(z)}\le1$ on $\DD$. A nonconstant holomorphic function on the connected open set $\DD$ cannot attain the value $1$ in modulus at an interior point (maximum modulus principle), so $\abs{f(z)}<1$.
:::

:::

::: {.pf-step #injective}
$f$ is injective.

::: pf-proof
Each $f_n$ is an automorphism, hence injective and holomorphic. Hurwitz's theorem states that if a sequence of injective holomorphic functions on a region converges locally uniformly to a limit that is not constant, the limit is injective. By hypothesis $f_n\to f$ locally uniformly with $f$ nonconstant, so $f$ is injective.
:::

:::

::: {.pf-step #subsequence}
Some subsequence $g_{n_k}$ converges locally uniformly on $\DD$ to a holomorphic $g:\DD\to\overline\DD$, and $g$ is nonconstant.

::: pf-proof
The automorphisms of $\DD$ form a normal family (Montel: they are holomorphic and bounded by $1$ on $\DD$), so some subsequence converges locally uniformly to a holomorphic limit $g$ with $\abs{g}\le1$. Since $g\circ f=\operatorname{id}$ by step [](#composite){.pf-ref} and the identity is not constant, $g$ is not constant.
:::

:::

::: {.pf-step #composite}
$g\big(f(z)\big)=z$ for every $z\in\DD$.

::: pf-proof
Fix $z\in\DD$ and let $K$ be a compact disc in $\DD$ containing $f(z)$ in its interior, which exists because $f(z)\in\DD$ by step [](#finto){.pf-ref}. For $k$ large, $f_{n_k}(z)\in K$ by convergence; $g_{n_k}\to g$ uniformly on $K$; so
$$
g\big(f(z)\big)=\lim_k g_{n_k}\big(f_{n_k}(z)\big)=\lim_k z=z .
$$
:::

:::

::: {.pf-step #ginto}
$g$ maps $\DD$ into $\DD$.

::: pf-proof
$g$ is holomorphic and nonconstant on $\DD$ with $\abs g\le1$; the maximum modulus principle then gives $\abs{g(w)}<1$ for every $w\in\DD$.
:::

:::

::: {.pf-step #other}
$f\big(g(w)\big)=w$ for every $w\in\DD$.

::: pf-proof
Fix $w\in\DD$ and a compact disc $K\subseteq\DD$ containing $g(w)$ in its interior, possible by step [](#ginto){.pf-ref}. For large $k$, $g_{n_k}(w)\in K$; $f_{n_k}\to f$ uniformly on $K$; and $f_{n_k}\big(g_{n_k}(w)\big)=w$ because $g_{n_k}=f_{n_k}^{-1}$. Hence $f\big(g(w)\big)=\lim_k f_{n_k}\big(g_{n_k}(w)\big)=w$.
:::

:::

::: {.pf-step}
$f$ is an automorphism of $\DD$.

::: pf-proof
$f:\DD\to\DD$ is holomorphic and injective (steps [](#finto){.pf-ref}, [](#injective){.pf-ref}), $g:\DD\to\DD$ is holomorphic, and steps [](#composite){.pf-ref} and [](#other){.pf-ref} show $g\circ f=\operatorname{id}$ and $f\circ g=\operatorname{id}$. So $f$ is a biholomorphism of $\DD$ onto $\DD$, i.e. an automorphism.
:::

:::

:::
:::
