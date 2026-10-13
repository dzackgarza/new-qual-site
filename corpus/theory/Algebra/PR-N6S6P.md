---
schema: qual/card@1
id: PR-N6S6P
kind: proposition
title: Automorphism groups of finite cyclic groups
slogan: 'Automorphisms of $C_n$ are the units modulo $n$.'
classification:
  areas:
  - algebra
  topics:
  - Automorphisms
  - Cyclic Groups
relations: []
review: draft
---

::: {.proposition}
Let $\varphi$ be [[D-JX3YC|Euler's totient function]].

(a) For $n \geq 1$, a cyclic group $C_n$ has exactly $\varphi(n)$ generators, and for primes $p \neq q$ and $k, \ell \geq 1$,
$$
\begin{aligned}
\varphi(p) &= p-1, \\
\varphi(p^k) &= p^{k-1}(p - 1), \\
\varphi(p^k q^\ell) &= \varphi(p^k)\,\varphi(q^\ell).
\end{aligned}
$$

(b) $\Aut(C_n) \cong (\ZZ/n\ZZ)\units$, a group of order $\varphi(n)$.
It is cyclic if and only if $n = 1, 2, 4, p^k$, or $2p^k$ with $p$ an odd prime and $k \geq 1$.

(c) For $p$ an odd prime and $k \geq 1$, $\Aut(C_{p^k}) \cong C_{\varphi(p^k)}$; in particular $\Aut(C_p) \cong C_{p-1}$.

(d) $\Aut(C_2) = 1$, $\Aut(C_4) \cong C_2$, and for $k \geq 3$, $\Aut(C_{2^k}) \cong C_2 \times C_{2^{k-2}}$.

(e) If $G$ and $H$ are finite groups of coprime orders, then $\Aut(G \times H) \cong \Aut(G) \times \Aut(H)$.
Consequently, if $n = \prod_{k=1}^\ell p_k^{n_k}$ with distinct primes $p_k$, $p_1 = 2$, and $n_1 \geq 3$, then $C_n \cong \prod_{k=1}^{\ell} C_{p_k^{n_k}}$ and
$$
\begin{aligned}
\Aut(C_n)
&\cong \prod_{k=1}^\ell \Aut\qty{C_{p_k^{n_k}}} \\
&\cong \prod_{k=1}^\ell (\ZZ/p_k^{n_k}\ZZ)\units \\
&\cong \qty{C_2 \times C_{2^{n_1-2}} } \times \prod_{k=2}^\ell C_{m_k},
\qquad m_k \coloneqq \varphi(p_k^{n_k}) = p_k^{n_k-1}(p_k-1).
\end{aligned}
$$

:::

::: {.example}
$\Aut(C_8) \cong (\ZZ/8\ZZ)\units = \theset{1, 3, 5, 7}$ has every nonidentity element of order $2$, so $\Aut(C_8) \cong C_2 \times C_2 \not\cong C_4$.
:::
