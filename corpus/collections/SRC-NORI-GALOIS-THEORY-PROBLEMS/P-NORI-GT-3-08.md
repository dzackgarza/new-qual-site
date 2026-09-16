---
schema: qual/card@1
id: P-NORI-GT-3-08
kind: problem
title: $\Phi_{n'p^k}=\Phi_{n'}^{\varphi(p^k)}$ in $\mathbb F_p[X]$
classification:
  areas: [algebra]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against problem 3.8 of the retained Nori Galois Theory Problems PDF.
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Stated the setup and claim of Problem 3.7, on which this problem depends, from p. 2 of the Nori Galois Theory Problems PDF.
---

::: {.problem}
The cylotomic polynomials $\Phi_n(X) \in \mathbb{Z}[X]$ defined for all natural numbers $n$ have the property
$$
X^n - 1 = \prod_{d \mid n} \Phi_d(X).
$$
Let $n = n'p^k$ with $p$ not dividing $n'$, and let $\varphi$ be Euler's phi function.
Problem 3.7 reads: let $F$ be a field of characteristic $p$ such that $\mu_{n'}(F)$ has order $n'$. Show that the roots of $\Phi_n(X)$ in $F$ are the primitive $n'$-th roots of unity, each of them occuring with multiplicity $\varphi(p^k)$.

Deduce the equality $\Phi_n(X) = \Phi_{n'}(X)^{\varphi(p^k)}$ in $\mathbb{F}_p[X]$ from the previous problem.
:::

::: {.remark}
Here $\mu_{n'}(F) = \{x \in F : x^{n'} = 1\}$, as in the notation paragraph of the source.
:::
