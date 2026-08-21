---
schema: qual/card@1
id: PR-N6S6P
kind: proposition
title: How to count sizes of automorphism groups
classification:
  areas:
  - algebra
  topics:
  - Automorphisms
  - Cyclic Groups
  - Semidirect Products
relations: []
review: draft
---

:::{.proposition title="How to count sizes of automorphism groups"}
Homs among various cyclic groups $C_m$ and any of their automorphism groups $\Aut(C_m)$ are **completely** classified, so for example $\Hom(C_m, C_n), \Hom(C_m, \Aut(C_n)), \Hom(\Aut(C_m), C_n)$, etc.
There's a good reference here: 

<https://www.whitman.edu/documents/Academics/Mathematics/SeniorProject_BrianSloan.pdf>


Let $\varphi$ be the totient function, and note that a cyclic group $C_n$ has precisely $\phi(n)$ choices of generators.
One can compute
\[
\phi(p) &= p-1 \\
\phi(p^k) &= p^{k-1}(p - 1) \\
\phi(p^kq^\ell) &= \phi(p^k)\phi(q^\ell) \quad\text{when } \gcd(q, p) = 1
.\]

- Automorphisms of cyclic groups are completely known:
\[
\Aut(C_n) \cong C_n\units 
,\]
which has size $\phi(n)$ but is not generally isomorphic to $C_{\phi(n)}$

:::{.warnings}
Warning: $C_n\units$ is not always cyclic!! 
For example, $C_8\units \cong C_2^2 \neq C_{4}$.
In fact, $C_n\units$ cyclic iff $n=2,4,p^k, 2p^k$ for $p$ an odd prime.
:::


- For $p$ an odd prime, $\Aut(C_p) \cong C_p\units \cong C_{p-1}$ is cyclic. 

- For $p^k$ an odd prime power, $\Aut(C_{p^k}) \cong C_{\varphi(p^k)}$ is cyclic.


- For $2^k$ with $k\geq 3$, $C_{2^k}\units \cong C_{2}\times C_{2^{k-2}}$.
  The two small cases are separate: $C_2\units = 1$ and $C_4\units \cong C_2$.

- If $G, H$ have coprime order then $\Aut(G \cross H) \cong \Aut(G) \cross  \Aut(H)$.
  One can then compute a general order by factoring $n = \prod_{k=1}^\ell p_k^{n_k}$ to get a decomposition 
\[
C_n= C_{\prod_{k=1}^\ell p_k^{n_k}}= \prod_{k=1}^{\ell} C_{p_k^{n_k}} 
,\]
  and thus
  \[
  \Aut(C_n) 
  &\cong \Aut\qty{\prod_{k=1}^{\ell} C_{p_k^{n_k}} }\\
  &\cong \prod_{k=1}^\ell \Aut\qty{C_{p_k^{n_k}}} \\
  &\cong \prod_{k=1}^\ell C_{p_k^{n_k}}\units \\
  &\cong C_{2^{n_1}}\units \cross \prod_{\substack{k=1 \\ p_k\neq 2} }^\ell C_{p_k^{n_k}}\units \\
  &\cong \qty{C_2 \cross C_{2^{n_1-2}} } \cross \prod_{\substack{k=1 \\ p_k\neq 2} }^\ell C_{m_k} && m_k \da \varphi(p_k^{n_k}) \\
  &\cong \qty{C_2 \cross C_{2^{n_1-2}} } \cross \prod_{\substack{k=1 \\ p_k\neq 2} }^\ell C_{m_k} &&  m_k \da p_k^{n_k-1}(p_k-1)  
  .\]

  Here $p_1 = 2$ with exponent $n_1$, and the $2\dash$part is written this way only when $n_1 \geq 3$; the exponent of the $2\dash$factor is $n_1$, not the number of distinct primes $\ell$.



- $\Aut(C_p^n) \cong \GL_n(\FF_p)$ which has size 
\[
\size \GL_n(\FF_p) = \prod_{k=0}^{n-1}(p^n-p^k) = (p^n-1)(p^n-p)(p^n-p^2)\cdots(p^n-p^{n-1})
.\]

- $\Aut(C_m^n)$ for $m$ not prime: no clue!
  For $n=2$, this seems to be a wreath product $\Aut(C_m) \wr C_2$.


- Counting homs: $\size \Hom_\Grp(C_n, C_m) = \gcd(n ,m)$.


-  If $\sigma \in \Aut(H)$ and $\tau \in \Aut(N)$, then \(N \semidirect_\psi H \cong N \semidirect_{\tau \circ \psi \circ \sigma} H\).
  - So if $\GL_n$ shows up in a semidirect product, it suffices to consider similarity classes of matrices (i.e. just use canonical forms).

- $\Inn(G) \cong G/Z(G)$.

:::
