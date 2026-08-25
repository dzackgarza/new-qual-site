---
schema: qual/card@1
id: P-KNIPC
kind: problem
title: $P_n(z)=\sum_{k=1}^n kz^{k-1}$ has no zeros in $|z|<r<1$ for large $n$
classification:
  areas:
  - complex-analysis
  topics:
  - Rouché
  - Zeros
  - Polynomials
  - Uniform Convergence
relations: []
review: draft
---

:::{.problem title="?"}
Let $0<r<1$. Show that polynomials
$P_n(z)  = 1 + 2z + 3 z^2 + \cdots + n z^{n-1}$ have no zeros in $|z|<r$
for all sufficiently large $n$'s.
:::

:::{.solution}
Key observation:
\[
P_n(z) = \sum_{1\leq k\leq n-1} kz^{k-1} = \dd{}{z}Q_n(z) 
\qquad Q(z) \da \sum_{0\leq k \leq n} z^k
.\]
Note that $Q(z) \to \sum_{k\geq 0} z^k = {1\over 1-z}$ uniformly on $\abs{z} \leq R < 1$ since this power series has radius of convergence 1.
Similarly $P_n(z)$ converges uniformly to $\dd{}{z}{1\over 1-z} = {1\over (1-z)^2}$, so let $P(z) \da {1\over (1-z)^2}$.
Note that $P$ is nonvanishing in $\DD$.

Strategy:

- Small: $m(z) = P(z) - P_n(z)$, look for an upper bound $\abs{m(z)} < U$
- Big: $P(z)$, look for a lower bound $L$ with $\abs{P(z)} > L > U$.

Just by considering the geometry of circles of radius $R < 1$ and $1$ and measuring distances to the point $1$, we can estimate
\[
0 < 1-R \leq \abs{1-z} < 1+R < 2 \implies \abs{P(z)} = {1\over \abs{1-z}^2} \geq {1\over 2^2} = {1\over 4}
.\]

Now fix $\eps < {1\over 4}$ and use uniform convergence of $P_n\to P$ to produce an $N$ such that $n\geq N$ implies $\norm{P-P_n}_\infty < \eps$ in $\abs{z} \leq R$.
Then on $\abs{z} = R$, for $n\geq N$,
\[
\abs{m(z)} \da \abs{P(z) - P_n(z)} \leq \norm{P - P_n}_\infty < \eps < {1\over 4} \leq \abs{P(z)} = \abs{M(z)}
,\]
so $0 = Z_P = Z_{P_n}$ by Rouché.
:::

