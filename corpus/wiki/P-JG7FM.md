---
schema: qual/card@1
id: P-JG7FM
kind: problem
title: $[\QQ(\zeta_n+\zeta_n^{-1}):\QQ]=\phi(n)/2$
classification:
  areas:
  - algebra
  topics:
  - Roots of Unity
  - Field Extensions
  - Galois Theory
relations: []
review: draft
---

Let $n\geq 3$ and $\zeta_n$ be a primitive $n$th root of unity. Show that $[\QQ(\zeta_n + \zeta_n\inv): \QQ] = \phi(n)/2$ for $\phi$ the totient function.

:::{.solution}
\envlist

- Some notation: let $\alpha_k \da \zeta_n^k + \zeta_n^{-k}$.
- Let $m(x)$ be the minimal polynomial of $\alpha_1 \da \zeta_n + \zeta_n\inv$.
  Note that $\alpha_1 \in \QQ(\zeta_n)$. 
- Use that $\Gal(\QQ(\zeta_n)/\QQ) \cong C_n\units$, consisting of maps $\sigma_k: \zeta \mapsto \zeta^k$ for $\gcd(k, n) = 1$, of which there are $\phi(n)$ many.
- Galois transitively permutes the roots of irreducible polynomials, so the roots of $m$ are precisely the Galois conjugates of $\alpha$, i.e. the Galois orbit of $\alpha$, so we can just compute it.
  For illustrative purposes, suppose $n$ is prime, then
  \[
  \sigma_1(\zeta_n + \zeta_n\inv) &= \zeta_n + \zeta_n\inv =\alpha_1 \\
  \sigma_2(\zeta_n + \zeta_n\inv) &= \zeta_n^2 + \zeta_n^{-2} = \alpha_2 \\
  \sigma_3(\zeta_n + \zeta_n\inv) &= \zeta_n^3 + \zeta_n^{-3} = \alpha_3 \\
  \vdots&\\
  \sigma_{n-1}(\zeta_n + \zeta_n\inv) &= \zeta_n^{n-1} + \zeta_n^{-(n-1)} = \zeta_n^{-1} + \zeta_n^{1} = \alpha_1 \\
  \sigma_{n-2}(\zeta_n + \zeta_n\inv) &= \zeta_n^{n-2} + \zeta_n^{-(n-2)} = \zeta_n^{-2} + \zeta_n^{2} = \alpha_2 \\
  \sigma_{n-3}(\zeta_n + \zeta_n\inv) &= \zeta_n^{n-3} + \zeta_n^{-(n-3)} = \zeta_n^{-3} + \zeta_n^{3} = \alpha_3
  ,\]
  where we've used that $\zeta^{k} = \zeta^{k\mod n}$.
  From this, we see that $\sigma_{k}(\alpha_1)=\sigma_{n-k}(\alpha_1)$ and we pick up $(n-1)/2$ distinct conjugates.

- For $n$ not prime, the exact same argument runs through the $\phi(n)$ values of $k$ coprime to $n$, and again yields $\sigma_{k}(\alpha_1) = \sigma_{n - k}(\alpha_1)$, since $\zeta_n^{n-k} = \zeta_n^{-k}$.
  The pairing $k \leftrightarrow n-k$ is fixed-point free on those $k$ for $n\geq 3$, so it partitions them into $\phi(n)/2$ pairs, giving $\phi(n)/2$ distinct roots.
:::


