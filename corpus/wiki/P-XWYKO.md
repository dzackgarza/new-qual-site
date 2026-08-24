---
schema: qual/card@1
id: P-XWYKO
kind: problem
title: A single Jordan block of size $6$ for $T$ with $p_T(x)=\chi_T(x)=x^6$
classification:
  areas:
  - algebra
  topics:
  - Jordan Canonical Form
  - Nilpotence
  - Minimal and Characteristic Polynomials
relations: []
review: draft
---

::: problem
Note that we can't have $T^j = 0$ for any $j\leq 4$, since then $T^5 = T^{5-k}T^k = T^{5-k} 0 = 0$, contradicting $T^5 \neq 0$.

So in fact $p_T(x) = x^6$ is the minimal polynomial of $T$, and since $V$ is 6 dimensional, the degree of the characteristic polynomial $\chi_T(x)$ is 6. Since $p_T \divides \chi_T$, and both are monic polynomials of degree 6, we in fact have
$$
p_T(x) = \chi_T(x) = x^6.
$$

But this means $T$ has eigenvalue $\lambda = 0$ with multiplicity 6. This means

- The size of the largest Jordan block associated to $\lambda = 0$ is size 6, since $0$ has multiplicity 6 in $p_T$, and

- The sum of the sizes of all Jordan blocks associated to $\lambda = 0$ is 6, since $0$ has multiplicity 6 in $\chi_T$

which forces $JCF(T)$ to have a single Jordan block of size 6, i.e.
$$
JCF(T) = J_0^6 = 
\left[\begin{array}{cccccc}
0 & 1 & 0 & 0 & 0 & 0\\
0 & 0 & 1 & 0 & 0 & 0\\
0 & 0 & 0 & 1 & 0 & 0\\
0 & 0 & 0 & 0 & 1 & 0\\
0 & 0 & 0 & 0 & 0 & 1\\
0 & 0 & 0 & 0 & 0 & 0\\
\end{array}\right]
$$
:::
