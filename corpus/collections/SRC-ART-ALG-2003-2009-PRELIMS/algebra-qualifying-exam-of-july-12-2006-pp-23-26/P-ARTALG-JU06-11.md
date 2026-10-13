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
::: {.problem}
Give an example of an integral domain $R$, a free $R$-module $M$, and an $R$-submodule $N$ of $M$ such that $N$ is not a free $R$-module.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

Let
$$
R=\ZZ[x],
\qquad
M=R,
\qquad
N=(2,x)\subseteq M.
$$
Then $R$ is an integral domain, $M$ is free of rank $1$, and $N$ is an $R$-submodule of $M$.

::: pf-proof

The polynomial ring $\ZZ[x]$ is an integral domain because the product of two nonzero polynomials has nonzero leading coefficient. As a module over itself, $M=R$ is free with basis $\{1\}$. The ideal
$$
N=(2,x)
=\{2p(x)+xq(x):p,q\in\ZZ[x]\}
$$
is closed under addition and multiplication by elements of $R$, so it is an $R$-submodule of $M$.

:::

:::

::: {.pf-step #s2}

If $N$ were free, then it would have rank $1$.

::: pf-proof

Suppose $N$ were free. Since $2\in N$, it is nonzero, so its rank is at least $1$.

On the other hand, any two nonzero elements $a,b\in N\subseteq R$ satisfy the nontrivial $R$-linear relation
$$
b\,a-a\,b=0.
$$
The coefficients $b$ and $-a$ are not both zero. Thus no two nonzero elements of $N$ are $R$-linearly independent, so a basis of the free module $N$ can contain at most one element. Hence the rank is exactly $1$.

:::

:::

::: {.pf-step #s3}

If $N$ were free, then the ideal $(2,x)$ would be principal.

::: pf-proof

By step [](#s2){.pf-ref}, a free $N$ would have a one-element basis $\{f\}$ for some nonzero $f\in N$. Then
$$
N=Rf=(f),
$$
so $N$ would be principal.

:::

:::

::: {.pf-step #s4}

The ideal $(2,x)$ is not principal.

::: pf-proof

Suppose
$$
(2,x)=(f).
$$
Since $2\in(f)$, one has
$$
2=fg
$$
for some $g\in\ZZ[x]$. Both factors are nonzero, so degrees add; since the right side has degree $0$, both $f$ and $g$ are constant integers. Thus $f$ divides $2$ in $\ZZ$, so
$$
f\in\{\pm1,\pm2\}.
$$

If $f=\pm1$, then $(f)=R$, but $(2,x)$ is proper because every element $2p+xq$ has even constant term, whereas $1$ does not.

If $f=\pm2$, then $(f)=(2)$, but $x\in(2,x)$ while $x\notin(2)$ because its coefficient of $x$ is odd. Both cases are impossible.

:::

:::

::: {.pf-step #s5}

Therefore
$$
\boxed{R=\ZZ[x],\quad M=R,\quad N=(2,x)}
$$
is an example in which $M$ is free and $N\le M$ is not free.

::: pf-proof

Step [](#s1){.pf-ref} gives the required domain, free module, and submodule. If $N$ were free, step [](#s3){.pf-ref} would make $(2,x)$ principal, contradicting step [](#s4){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s5){.pf-ref} is the required example.

:::

:::

:::
