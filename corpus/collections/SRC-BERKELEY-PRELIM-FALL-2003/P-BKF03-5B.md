---
schema: qual/card@1
id: P-BKF03-5B
kind: problem
title: A noncyclic group of order $n$ when $\gcd(n,\phi(n))>1$
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against Problem 5B of the vendored Fall 2003 Berkeley prelim and independently reviewed the accompanying source solution.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Verified the totient divisibility dichotomy and both resulting noncyclic group constructions.
---

::: {.problem}
Let n be a positive integer.
Let $\phi ( n )$ be the Euler phi function, so $\phi ( n ) = \# ( \mathbb { Z } / n \mathbb { Z } ) ^ { * }$ Prove that if $\operatorname* { g c d } ( n , \phi ( n ) ) > 1$ , then there exists a noncyclic group of order n.
:::
\n\n::: {.solution}\nChoose a prime $p$ dividing $\gcd(n,\phi(n))$.
Then $p\mid n$ and $p\mid\phi(n)$.\n\n<1>1. Either $p^2\mid n$, or there is a prime $q\ne p$ with $q\mid n$ and $p\mid(q-1)$.\n::: {.proof}\nWrite\n\[\nn=\prod_{r\mid n} r^{a_r}.\n\]\nEuler's formula gives\n\[\n\phi(n)=\prod_{r\mid n} r^{a_r-1}(r-1).\n\]\nSince $p\mid n$, the prime $p$ occurs among the $r$.
If $a_p\ge2$, then $p^2\mid n$.
Otherwise $a_p=1$, so the factor $p^{a_p-1}$ contributes no factor of $p$ to $\phi(n)$.
Because $p\mid\phi(n)$ and $p\nmid(p-1)$, some distinct prime $q\mid n$ must satisfy $p\mid(q-1)$.\n:::\n\n<1>2. If $p^2\mid n$, then\n\[\nG=C_p\times C_p\times C_{n/p^2}\n\]\nis a noncyclic group of order $n$.\n::: {.proof}\nIts order is\n\[\n|G|=p\cdot p\cdot\frac{n}{p^2}=n.\n\]\nThe subgroup $C_p\times C_p\times\{1\}$ is not cyclic.
A subgroup of a cyclic group must be cyclic, so $G$ itself cannot be cyclic.\n:::\n\n<1>3. Suppose instead that $p^2\nmid n$.
Let $q\ne p$ be as in <1>1. There exists a nonabelian group $H$ of order $pq$.\n::: {.proof}\nSince $\mathbb F_q^\times$ is cyclic of order $q-1$ and $p\mid(q-1)$, it has a subgroup\n\[\n\mu_p=\{a\in\mathbb F_q^\times:a^p=1\}\n\]\nof order $p$.
Define\n\[\nH=\left\{\begin{pmatrix}a&b\\0&1\end{pmatrix}:a\in\mu_p,\ b\in\mathbb F_q\right\}.\n\]\nMatrix multiplication shows that $H$ is a subgroup of $\operatorname{GL}_2(\mathbb F_q)$, and there are $p$ choices for $a$ and $q$ choices for $b$, so $|H|=pq$.\n\nChoose $a\in\mu_p$ with $a\ne1$.
Then\n\[\n\begin{pmatrix}a&0\\0&1\end{pmatrix}\begin{pmatrix}1&1\\0&1\end{pmatrix}\n=\begin{pmatrix}a&a\\0&1\end{pmatrix},\n\]\nwhereas\n\[\n\begin{pmatrix}1&1\\0&1\end{pmatrix}\begin{pmatrix}a&0\\0&1\end{pmatrix}\n=\begin{pmatrix}a&1\\0&1\end{pmatrix}.\n\]\nThese differ because $a\ne1$, so $H$ is nonabelian.\n:::\n\n<1>4. In the second case,\n\[\nG=H\times C_{n/(pq)}\n\]\nis a noncyclic group of order $n$.\n::: {.proof}\nBecause $p$ and $q$ are distinct primes dividing $n$, $pq\mid n$.
Thus\n\[\n|G|=pq\cdot\frac{n}{pq}=n.\n\]\nThe direct factor $H$ is nonabelian by <1>3, so $G$ is nonabelian.
Every cyclic group is abelian; hence $G$ is not cyclic.\n:::\n\nIn either case there exists a noncyclic group of order $n$.\n:::\n
