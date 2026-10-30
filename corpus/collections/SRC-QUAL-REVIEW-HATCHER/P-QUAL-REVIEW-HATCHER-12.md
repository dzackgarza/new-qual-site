---
schema: qual/card@1
id: P-QUAL-REVIEW-HATCHER-12
kind: problem
title: The dimension of a manifold is intrinsic
classification:
  areas: [topology]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against practice problem 12 in assets/attachments/Qual_Review_Selection_of_Hatcher_Problems_-_Unknown_extracted.md.
---

::: {.problem}
Let $M$ be an $n$-manifold.
Prove that $M$ is not a $k$-manifold for any $k\ne n$.
:::

::: {.solution}

Fix
$$
x\in M.
$$

::: pf

::: {.pf-step #s1-1}

Since $M$ is an $n$-manifold, there is an open neighborhood
$$
U\ni x
$$
and a homeomorphism
$$
\phi:U\to V
$$
onto an open set
$$
V\subseteq\RR^n
$$
with
$$
\phi(x)=0.
$$


::: pf-proof

This is the definition of an $n$-manifold, after translating the Euclidean chart so that the image of $x$ is the origin.

:::

:::

::: {.pf-step #s1-2}

Excision gives
$$
\boxed{
H_i(M,M\setminus\{x\})
\cong
H_i(U,U\setminus\{x\})}.
$$


::: pf-proof

The complement
$$
M-U
$$
has closure contained in
$$
M\setminus\{x\},
$$
so excising $M-U$ from the pair
$$
(M,M\setminus\{x\})
$$
gives the displayed isomorphism.

:::

:::

::: {.pf-step #s1-3}

Via the chart,
$$
\boxed{
H_i(U,U\setminus\{x\})
\cong
H_i(V,V\setminus\{0\})}.
$$


::: pf-proof

A homeomorphism of pairs induces isomorphisms on relative homology.

:::

:::

::: {.pf-step #s1-4}

Shrinking $V$ if necessary, excision identifies
$$
H_i(V,V\setminus\{0\})
$$
with
$$
H_i(\RR^n,\RR^n\setminus\{0\}).
$$


::: pf-proof

Choose an open ball $B$ centered at $0$ with
$$
\overline B\subseteq V.
$$
Excision gives
$$
H_i(V,V\setminus\{0\})
\cong
H_i(B,B\setminus\{0\}),
$$
and the same argument gives
$$
H_i(\RR^n,\RR^n\setminus\{0\})
\cong
H_i(B,B\setminus\{0\}).
$$

:::

:::

::: {.pf-step #s1-5}

The space
$$
\RR^n\setminus\{0\}
$$
deformation retracts onto
$$
S^{n-1}.
$$


::: pf-proof

Use radial projection
$$
v\longmapsto\frac{v}{\norm{v}}.
$$

:::

:::

::: {.pf-step #s1-6}

Since $\RR^n$ is contractible, the long exact sequence of the pair gives
$$
\boxed{
H_i(\RR^n,\RR^n\setminus\{0\})
\cong
\widetilde H_{i-1}(\RR^n\setminus\{0\})}.
$$


::: pf-proof

For $i>0$, the absolute homology groups of $\RR^n$ vanish, so the connecting maps in the long exact sequence are isomorphisms. The reduced formulation also handles the degree-zero edge cleanly.

:::

:::

::: {.pf-step #s1-7}

Therefore
$$
H_i(\RR^n,\RR^n\setminus\{0\})
\cong
\widetilde H_{i-1}(S^{n-1}).
$$


::: pf-proof

Apply step [](#s1-5){.pf-ref} to step [](#s1-6){.pf-ref}.

:::

:::

::: {.pf-step #s1-8}

Hence
$$
\boxed{
H_i(M,M\setminus\{x\};\ZZ)
\cong
\begin{cases}
\ZZ,&i=n,\\
0,&i\ne n.
\end{cases}}
$$


::: pf-proof

By steps [](#s1-2){.pf-ref} through [](#s1-7){.pf-ref}, the local relative homology is the reduced homology of $S^{n-1}$, shifted by one degree. The sphere has reduced homology $\ZZ$ only in degree $n-1$.

:::

:::

::: {.pf-step #s1-9}

Applying the same local-homology calculation using a $k$-dimensional chart gives
$$
\boxed{
H_i(M,M\setminus\{x\};\ZZ)
\cong
\begin{cases}
\ZZ,&i=k,\\
0,&i\ne k.
\end{cases}}
$$


::: pf-proof

Repeat steps [](#s1-1){.pf-ref} through [](#s1-8){.pf-ref} with $\RR^k$ in place of $\RR^n$.

:::

:::

::: pf-step

The local homology group in step [](#s1-8){.pf-ref} is nonzero exactly in degree $n$, while the same group in step [](#s1-9){.pf-ref} is nonzero exactly in degree $k$.


::: pf-proof

Both statements concern the same pair
$$
(M,M\setminus\{x\}),
$$
so both degree descriptions must agree.

:::

:::

::: {.pf-step #s1-11}

Therefore
$$
\boxed{n=k}.
$$


::: pf-proof

If $n\ne k$, then at degree $i=n$, step [](#s1-8){.pf-ref} gives $\ZZ$ while step [](#s1-9){.pf-ref} gives $0$, contradiction.

:::

:::

::: {.pf-step #s1-12}

Hence an $n$-manifold cannot also be a $k$-manifold for any
$$
\boxed{k\ne n}.
$$


::: pf-proof

Step [](#s1-11){.pf-ref} shows equality of dimensions is necessary.

:::

:::

::: pf-qed

Step [](#s1-12){.pf-ref} is the required conclusion.

:::

:::

:::
