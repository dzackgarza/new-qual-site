---
schema: qual/card@1
id: P-WESTOP12-6
kind: problem
title: Relative homology of $S^2$ modulo a finite discrete subset
classification: {areas: [topology], topics: []}
relations: []
review: draft
audit:
- {event: source-checked, by: gpt-5.6-sol, date: 2026-09-14}
---

::: {.problem}
Let $A$ be a discrete set of $r>1$ points in $S^2$. Determine the relative homology groups
$$
H_n(S^2,A)
$$
for all $n\ge0$.
:::

::: {.solution}

All homology groups have integer coefficients.

::: pf

::: {.pf-step #s1-1}

Since $A$ consists of $r$ discrete points,
$$
H_n(A)
\cong
\begin{cases}
\ZZ^r,&n=0,\\
0,&n>0.
\end{cases}
$$


::: pf-proof

Each point contributes one path component, so
$$
H_0(A)\cong\ZZ^r.
$$
Every higher homology group of a discrete space vanishes.

:::

:::

::: {.pf-step #s1-2}

The homology of the sphere is
$$
H_n(S^2)
\cong
\begin{cases}
\ZZ,&n=0,2,\\
0,&\text{otherwise}.
\end{cases}
$$


::: pf-proof

This is the standard homology computation for $S^2$.

:::

:::

::: {.pf-step #s1-3}

For
$$
n\ge3,
$$
one has
$$
H_n(S^2,A)=0.
$$


::: pf-proof

The long exact sequence of the pair contains
$$
H_n(A)
\longrightarrow
H_n(S^2)
\longrightarrow
H_n(S^2,A)
\longrightarrow
H_{n-1}(A).
$$
For
$$
n\ge3,
$$
all three absolute groups surrounding the relative group vanish by
steps [](#s1-1){.pf-ref} through [](#s1-2){.pf-ref}.
Hence exactness forces
$$
H_n(S^2,A)=0.
$$

:::

:::

::: {.pf-step #s1-4}

In degree $2$,
$$
\boxed{
H_2(S^2,A)
\cong
\ZZ.
}
$$


::: pf-proof

The relevant part of the long exact sequence is
$$
H_2(A)
\longrightarrow
H_2(S^2)
\longrightarrow
H_2(S^2,A)
\longrightarrow
H_1(A).
$$
By step [](#s1-1){.pf-ref},
$$
H_2(A)=0
$$
and
$$
H_1(A)=0.
$$
Thus
$$
0
\longrightarrow
\ZZ
\longrightarrow
H_2(S^2,A)
\longrightarrow
0
$$
is exact, giving
$$
H_2(S^2,A)
\cong
\ZZ.
$$

:::

:::

::: {.pf-step #s1-5}

The degree-$1$ and degree-$0$ part of the long exact sequence is
$$
0
\longrightarrow
H_1(S^2,A)
\xrightarrow{\partial}
\ZZ^r
\xrightarrow{i_*}
\ZZ
\longrightarrow
H_0(S^2,A)
\longrightarrow
0.
$$


::: pf-proof

Insert
$$
H_1(S^2)=0,
\qquad
H_0(A)=\ZZ^r,
\qquad
H_0(S^2)=\ZZ
$$
into the long exact sequence of the pair.

:::

:::

::: pf-step

The map
$$
i_*:
H_0(A)
\to
H_0(S^2)
$$
is
$$
\boxed{
(n_1,\dots,n_r)
\longmapsto
n_1+\cdots+n_r.
}
$$


::: pf-proof

Each generator of
$$
H_0(A)
\cong
\ZZ^r
$$
comes from one point of $A$.
Under inclusion into the connected space $S^2$, every such point represents
the same generator of
$$
H_0(S^2)\cong\ZZ.
$$
Therefore each standard basis vector maps to $1$, giving the augmentation
map.

:::

:::

::: {.pf-step #s1-7}

The map $i_*$ is surjective and
$$
\ker i_*
\cong
\ZZ^{r-1}.
$$


::: pf-proof

Surjectivity is immediate because
$$
(1,0,\dots,0)
\longmapsto
1.
$$

Its kernel is
$$
\left\{
(n_1,\dots,n_r)
\in
\ZZ^r:
n_1+\cdots+n_r=0
\right\}.
$$
This is free of rank
$$
r-1.
$$
For example, a basis is
$$
e_1-e_r,
\dots,
e_{r-1}-e_r.
$$

:::

:::

::: {.pf-step #s1-8}

Therefore
$$
\boxed{
H_1(S^2,A)
\cong
\ZZ^{r-1}.
}
$$


::: pf-proof

By exactness of the sequence in step [](#s1-5){.pf-ref},
$$
\operatorname{im}\partial
=
\ker i_*.
$$
The map
$$
\partial
$$
is injective because the preceding group is zero.
Thus
$$
H_1(S^2,A)
\cong
\ker i_*
\cong
\ZZ^{r-1}
$$
by step [](#s1-7){.pf-ref}.

:::

:::

::: {.pf-step #s1-9}

One has
$$
\boxed{
H_0(S^2,A)=0.
}
$$


::: pf-proof

In step [](#s1-5){.pf-ref}, the map
$$
i_*:\ZZ^r\to\ZZ
$$
is surjective by step [](#s1-7){.pf-ref}.
Hence its cokernel is zero.
Exactness gives
$$
H_0(S^2,A)=0.
$$

:::

:::

::: {.pf-step #s1-10}

The complete answer is
$$
\boxed{
H_n(S^2,A)
\cong
\begin{cases}
\ZZ,
&n=2,\\
\ZZ^{r-1},
&n=1,\\
0,
&n=0\text{ or }n\ge3.
\end{cases}
}
$$


::: pf-proof

Collect steps [](#s1-3){.pf-ref} through [](#s1-4){.pf-ref} and [](#s1-8){.pf-ref} through [](#s1-9){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s1-10){.pf-ref} gives all relative homology groups.

:::

:::

:::
