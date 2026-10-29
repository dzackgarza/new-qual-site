---
schema: qual/card@1
id: PR-MK2W6
kind: example
title: An irreducible inseparable polynomial over an imperfect field
classification:
  areas:
  - algebra
  topics:
  - Separability
  - Splitting Fields
  - Irreducibility Criteria
relations: []
review: draft
---

::: {.example}
Let $k=\FF_p(t)$.
The polynomial
$$
f(x)=x^p-t\in k[x]
$$
is irreducible and inseparable, and
$$
k(t^{1/p})/k
$$
is an inseparable extension of degree $p$.
:::

::: {.proof}
Let $\alpha=t^{1/p}$ in an algebraic closure of $k$.
Then
$$
x^p-t=(x-\alpha)^p.
$$
If $f$ had a monic factor in $k[x]$ of degree $j$ with $0<j<p$, then over the algebraic closure that factor would be $(x-\alpha)^j$.
Its coefficient of $x^{j-1}$ is $-j\alpha$.
Since $j\neq0$ in $\FF_p$, this would imply $\alpha\in k$, hence $t=\alpha^p\in k^p$.
But $t$ is not a $p$th power in $\FF_p(t)$, since the $t$-adic valuation of a $p$th power is divisible by $p$ while $v_t(t)=1$.
Thus $f$ is irreducible.
Its derivative is zero, so [[PR-TLBPS]] shows that $f$ is inseparable.
Therefore the minimal polynomial of $\alpha$ over $k$ is inseparable of degree $p$.
:::
