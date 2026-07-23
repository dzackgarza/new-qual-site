---
schema: qual/card@1
id: P-WASE4
kind: problem
title: "Use Rouche's theorem to prove the Fundamental Theorem of Algebra."
classification:
  areas:
  - complex-analysis
  topics: []
relations: []
review: draft
---
:::{.problem title="?"}
Use Rouche's theorem to prove the Fundamental Theorem of Algebra.
:::

:::{.solution}
Write $f(z) = \sum_{k\leq n} c_k z^k$.
Big: $M(z) = c_nz^n$.
Small: $m(z) = f(z) - M(z) = \sum_{k\leq n-1} c_k z^k$.

Now use that
\[
\abs{m(z) \over M(z)} 
&\da \abs{c_n\inv \sum_{k\leq n-1} c_k z^{k-n}} \\
&= \abs{c_n\inv\qty{ {c_1\over z^n} + {c_2\over z^{n-1} } + \cdots + {c_{n-1}\over z}  }} \\
&\convergesto{\abs{z}\to\infty}0
,\]
so choose $R$ large enough such that for $\abs{z} \geq R$, $\abs{M(z)\over m(z)} < 1$.
Then on $\abs{z} = R$,
\[
\abs{m(z) \over M(z)} < 1 \implies \abs{m(z)} < \abs{M(z)}
\implies \size n = \size Z_{M} = \size Z_{M+m} = \size Z_{f}
,\]
since $c_n z^n$ has $z=0$ as a root with multiplicity $n$.
:::

:::{.solution title="Explicit bound"}
An estimate: write $f(z) = \sum_{k\leq n} c_k z^k$ with $c_n = 1$, then for $R> 1$, on $\abs{z} = R$ we have
\[
\abs{f(z) - z^n} 
&\leq \sum_{k\leq n-1} \abs{ c_k z^k} \\
&\leq \sum_{k\leq n-1} \abs{ c_k} R^k \\
&\leq \sum_{k\leq n-1} \abs{ c_k} R^{n-1} \\
&= R^{n-1} \sum_{k\leq n-1} \abs{ c_k}  \\
&\da R^{n-1} C \\
&\leq R^n \\
&= \abs{z^n}
,\]
provided we can choose $C<R$, but this is possible since $\sum_{k\leq n-1}\abs{c_k}$ is a constant.
So $n = \size Z_{z^n} = \size Z_f$.
:::

