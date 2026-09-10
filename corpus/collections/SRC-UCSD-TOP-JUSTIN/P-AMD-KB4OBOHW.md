---
schema: qual/card@1
id: P-AMD-KB4OBOHW
kind: problem
title: $\operatorname{Ext}$ over $\ZZ[x,y]$ of $\ZZ[x,y]/(x-y)$ and $\ZZ[x,y]/(x,y)$
classification:
  areas:
  - topology
  topics:
  - Homological Algebra
  - Modules
relations: []
review: draft
---

::: {.problem}
Let $R = \ZZ[x,y]$, and $M = R/(x-y), N = R/(x,y)$.
Construct free resolutions of $M,N$ to compute:

- $\ext_R^*(M, M)$

- $\ext_R^*(M, N)$

- $\ext_R^*(N, M)$

- $\ext_R^*(N, N)$
:::

::: {.solution}
Let $R=\mathbb Z[x,y]$, $M=R/(x-y)$, and $N=R/(x,y)$.

<1>1. A free resolution of $M$ is
$$
0\to R\xrightarrow{x-y}R\to M\to0.
$$
::: {.proof}
The element $x-y$ is a non-zero-divisor in the domain $R$, and its cokernel is $M$.
:::

<1>2. A free resolution of $N$ is the Koszul resolution
$$
0\to R\xrightarrow{\binom{-y}{x}}R^2\xrightarrow{(x\;y)}R\to N\to0.
$$
::: {.proof}
The sequence $x,y$ is regular in $R$, so its Koszul complex is exact and resolves $R/(x,y)$.
:::

<1>3. We have
$$
\boxed{\operatorname{Ext}_R^0(M,M)\cong M,\quad
\operatorname{Ext}_R^1(M,M)\cong M,\quad
\operatorname{Ext}_R^i(M,M)=0\ (i\ge2).}
$$
::: {.proof}
Applying $\operatorname{Hom}_R(-,M)$ to <1>1 gives
$$
0\to M\xrightarrow{0}M\to0,
$$
because $x-y=0$ in $M$. Hence the degree-$0$ and degree-$1$ cohomology groups are both $M$, and there are no higher terms.
:::

<1>4. We have
$$
\boxed{\operatorname{Ext}_R^0(M,N)\cong N,\quad
\operatorname{Ext}_R^1(M,N)\cong N,\quad
\operatorname{Ext}_R^i(M,N)=0\ (i\ge2).}
$$
::: {.proof}
Apply $\operatorname{Hom}_R(-,N)$ to <1>1. Since $x=y=0$ in $N$, multiplication by $x-y$ is zero, so the cochain complex is $0\to N\xrightarrow0 N\to0$.
:::

<1>5. We have
$$
\boxed{\operatorname{Ext}_R^0(N,M)=0,\quad
\operatorname{Ext}_R^1(N,M)\cong\mathbb Z,\quad
\operatorname{Ext}_R^2(N,M)\cong\mathbb Z.}
$$
::: {.proof}
Identify $M\cong\mathbb Z[t]$ via $x=y=t$. Applying $\operatorname{Hom}_R(-,M)$ to the Koszul resolution gives
$$
0\to M\xrightarrow{m\mapsto(tm,tm)}M^2\xrightarrow{(a,b)\mapsto t(a-b)}M\to0.
$$
The first map is injective, so $H^0=0$. The kernel of the second map is the diagonal $\{(a,a)\}$, and modulo the image $tM\cdot(1,1)$ this gives $M/tM\cong\mathbb Z$, hence $H^1\cong\mathbb Z$. The second map has image $tM$, so its cokernel is also $M/tM\cong\mathbb Z$, giving $H^2\cong\mathbb Z$.
:::

<1>6. Finally,
$$
\boxed{\operatorname{Ext}_R^0(N,N)\cong N,\quad
\operatorname{Ext}_R^1(N,N)\cong N^2,\quad
\operatorname{Ext}_R^2(N,N)\cong N,}
$$
and higher Ext groups vanish.
::: {.proof}
After applying $\operatorname{Hom}_R(-,N)$ to the Koszul resolution, both differentials are zero because $x$ and $y$ act trivially on $N$. Hence the cohomology is simply $N$, $N^2$, $N$ in degrees $0,1,2$.
:::
:::
