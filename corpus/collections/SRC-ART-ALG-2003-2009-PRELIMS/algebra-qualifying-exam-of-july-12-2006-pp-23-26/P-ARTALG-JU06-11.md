---
schema: qual/card@1
id: P-ARTALG-JU06-11
kind: problem
title: Non-free submodule of a free module
classification:
  areas:
  - algebra
  topics:
  - Modules
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

Give an example of an integral domain $R$, a free $R$-module $M$, and an $R$-submodule $N$ of $M$ such that $N$ is not a free $R$-module.

::: {.solution}
<1>1. Construction of the domain, free module, and submodule:
<2>1. Let $R = \mathbb{Z}[x]$, the polynomial ring with integer coefficients, which is an integral domain.
<2>2. Let $M = R = \mathbb{Z}[x]$, which is a free $R$-module of rank 1 with basis $\{1\}$.
<2>3. Let $N = \langle 2, x \rangle = \{ 2 p(x) + x q(x) \mid p, q \in \mathbb{Z}[x] \} \subset M$.
As an ideal of $R$, $N$ is an $R$-submodule of $M$.

<1>2. Proof that $N$ is not a free $R$-module:
<2>1. Suppose for contradiction that $N$ is a free $R$-module.
For any two non-zero elements $a, b \in N \subset R$, we have the non-trivial relation:
\[
b \cdot a - a \cdot b = 0.
\]
Because $R$ is an integral domain and $a, b \neq 0$, any two elements of $N$ are linearly dependent over $R$.
Thus the rank of $N$ as a free $R$-module can be at most 1.
<2>2. Since $N \neq \{0\}$, the rank must be exactly 1, so $N = R \cdot f(x) = \langle f(x) \rangle$ for some non-zero polynomial $f(x) \in \mathbb{Z}[x]$ (i.e. $N$ must be a principal ideal).
<2>3. Since $2 \in N = \langle f(x) \rangle$, $f(x)$ must divide $2$ in $\mathbb{Z}[x]$.
The only divisors of $2$ in $\mathbb{Z}[x]$ are $\pm 1$ and $\pm 2$.
<2>4. If $f(x) = \pm 1$, then $N = \mathbb{Z}[x]$, so $1 \in N$.
However, every element in $\langle 2, x \rangle$ has an even constant term $2 p(0) + 0 \cdot q(0) \in 2\mathbb{Z}$, while $1$ is odd, so $1 \notin N$, contradiction.
If $f(x) = \pm 2$, then $N = 2\mathbb{Z}[x]$.
However, $x \in N$, but $x \notin 2\mathbb{Z}[x]$ since $x$ has coefficient $1 \notin 2\mathbb{Z}$, contradiction.
<2>5. Therefore $N$ is not principal, so $N$ is not a free $R$-module.

<1>3. Conclusion:
$R = \mathbb{Z}[x]$, $M = \mathbb{Z}[x]$, and $N = \langle 2, x \rangle$ provide an example of a non-free submodule of a free module. Q.E.D.
:::
