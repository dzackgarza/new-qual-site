---
schema: qual/card@1
id: P-WESTOP14-4
kind: problem
title: Relative homology of a solid torus and its boundary
classification: {areas: [topology], topics: []}
relations: []
review: draft
audit:
- {event: source-checked, by: gpt-5.6-sol, date: 2026-09-14}
---

::: {.problem}
Let
$$
X=D^2\times S^1
$$
be a solid torus, and let
$$
A=S^1\times S^1
$$
be its boundary. Compute $H_n(X,A)$ for all $n$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

The absolute homology groups are
$$
H_k(X)\cong
\begin{cases}
\ZZ,&k=0,1,\\
0,&k\ge2,
\end{cases}
$$
and
$$
H_k(A)\cong
\begin{cases}
\ZZ,&k=0,2,\\
\ZZ^2,&k=1,\\
0,&k\ge3.
\end{cases}
$$


::: pf-proof

The solid torus $X=D^2\times S^1$ deformation retracts onto $\{0\}\times S^1$, so it has the homology of $S^1$. The boundary $A=S^1\times S^1$ is the torus, whose homology is the displayed one.

:::

:::

::: {.pf-step #s1-2}

Under the inclusion $i:A\hookrightarrow X$, the induced map
$$
i_*:H_1(A)\cong\ZZ^2\longrightarrow H_1(X)\cong\ZZ
$$
is surjective with kernel isomorphic to $\ZZ$.


::: pf-proof

Choose the standard generators of $H_1(A)$: the meridian $m=S^1\times\{1\}$ and the longitude $\ell=\{1\}\times S^1$. Inside $X$, the meridian bounds the disk $D^2\times\{1\}$, so $i_*[m]=0$. The longitude is homotopic in $X$ to the core circle $\{0\}\times S^1$, which generates $H_1(X)$. Thus $i_*$ sends one basis vector to $0$ and the other to a generator of $\ZZ$.

:::

:::

::: {.pf-step #s1-3}

One has
$$
H_3(X,A)\cong\ZZ.
$$


::: pf-proof

The long exact sequence of the pair contains
$$
H_3(X)\longrightarrow H_3(X,A)\longrightarrow H_2(A)\longrightarrow H_2(X).
$$
By step [](#s1-1){.pf-ref}, the outer groups are $0$ and $H_2(A)\cong\ZZ$. Exactness therefore gives $H_3(X,A)\cong\ZZ$.

:::

:::

::: {.pf-step #s1-4}

One has
$$
H_2(X,A)\cong\ZZ.
$$


::: pf-proof

The next part of the long exact sequence is
$$
0=H_2(X)\longrightarrow H_2(X,A)\longrightarrow H_1(A)\xrightarrow{i_*}H_1(X).
$$
Hence $H_2(X,A)\cong\ker i_*$. By step [](#s1-2){.pf-ref}, this kernel is isomorphic to $\ZZ$.

:::

:::

::: {.pf-step #s1-5}

One has
$$
H_1(X,A)=0.
$$


::: pf-proof

Continue the long exact sequence:
$$
H_1(A)\xrightarrow{i_*}H_1(X)\longrightarrow H_1(X,A)\longrightarrow H_0(A)\longrightarrow H_0(X).
$$
The map $i_*$ is surjective by step [](#s1-2){.pf-ref}, and $H_0(A)\to H_0(X)$ is an isomorphism because both spaces are connected. Exactness forces $H_1(X,A)=0$.

:::

:::

::: {.pf-step #s1-6}

One has
$$
H_0(X,A)=0
$$
and $H_n(X,A)=0$ for every $n\ge4$.


::: pf-proof

Since $A$ meets the unique path component of $X$, $H_0(X,A)=0$. For $n\ge4$, step [](#s1-1){.pf-ref} gives $H_n(X)=0$ and $H_{n-1}(A)=0$, so the long exact sequence gives $H_n(X,A)=0$.

:::

:::

::: {.pf-step #s1-7}

Therefore
$$
\boxed{
H_n(X,A)\cong
\begin{cases}
\ZZ,&n=2,3,\\
0,&\text{otherwise}.
\end{cases}}
$$


::: pf-proof

Combine steps [](#s1-3){.pf-ref} through [](#s1-6){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s1-7){.pf-ref} lists all relative homology groups.

:::

:::

:::
