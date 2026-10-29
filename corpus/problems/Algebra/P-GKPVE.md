---
schema: qual/card@1
id: P-GKPVE
kind: problem
title: $K(u)/K$ is not Galois and $\Aut(K(u)/K)$ is trivial for a single root of an
  irreducible of degree $n$
classification:
  areas:
  - algebra
  topics:
  - Galois Theory
  - Field Extensions
  - Automorphisms
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

Let $K\subseteq\RR$ be a field of characteristic $0$, and let $f(x) \in K[x]$ be an irreducible polynomial of degree $n \ge 3$ such that $f(x)$ has exactly one real root $u \in \RR$ and $n - 1$ non-real complex roots.

(a) Prove that the extension degree $[K(u) : K] = n$.

(b) Prove that $K(u)/K$ is not a Galois extension.

(c) Prove that the automorphism group $\Aut(K(u)/K)$ is trivial ($\Aut(K(u)/K) = \{\id\}$).

:::

::: {.solution}

::: pf

::: pf-step

(a) $[K(u):K]=n$.

::: pf-proof

Because $f$ is irreducible and $f(u)=0$, a scalar multiple of $f$ is the minimal polynomial of $u$ over $K$. Hence $[K(u):K]=\deg f=n$.

:::

:::

::: {.pf-step #only-root}

The only root of $f$ in $K(u)$ is $u$.

::: pf-proof

Since $K\subseteq\RR$ and $u\in\RR$, we have $K(u)\subseteq\RR$. All roots of $f$ other than $u$ are nonreal, so none lies in $K(u)$.

:::

:::

::: pf-step

(b) $K(u)/K$ is not Galois.

::: pf-proof

The polynomial $f$ is irreducible over $K$ and has the root $u$ in $K(u)$, but by step [](#only-root){.pf-ref} and $n\ge 3$ it does not split over $K(u)$. Hence $K(u)/K$ is not normal, and so not Galois.

:::

:::

::: pf-step

(c) $\Aut(K(u)/K)=\{\id\}$.

::: pf-proof

Let $\sigma\in\Aut(K(u)/K)$. Since $\sigma$ fixes the coefficients of $f$,
$$
0=\sigma(f(u))=f(\sigma(u)).
$$
Thus $\sigma(u)$ is a root of $f$ lying in $K(u)$, so $\sigma(u)=u$ by step [](#only-root){.pf-ref}. Since $K(u)$ is generated over $K$ by $u$, $\sigma=\id$.

:::

:::

:::

:::
