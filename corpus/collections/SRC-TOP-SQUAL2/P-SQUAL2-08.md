---
schema: qual/card@1
id: P-SQUAL2-08
kind: problem
title: Invariance of dimension for Euclidean spaces
classification: {areas: [topology], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
---

::: {.problem}
Prove that if $\RR^n$ is homeomorphic to $\RR^m$, then $n=m$.
:::

::: {.solution}

Suppose there is a homeomorphism
$$
h:\RR^n\to\RR^m.
$$

::: pf

::: pf-step

If $n=0$, then
$$
\RR^n
$$
is a one-point space.


::: pf-proof

By convention,
$$
\RR^0=\{*\}.
$$

:::

:::

::: {.pf-step #s1-2}

If $n=0$, then necessarily $m=0$.


::: pf-proof

A space homeomorphic to a one-point space has exactly one point. For every $m\ge1$, the space $\RR^m$ has infinitely many points. Thus $m=0$.

:::

:::

::: pf-step

Let
$$
p=0\in\RR^n
$$
and set
$$
q=h(p)\in\RR^m.
$$


::: pf-proof

This selects corresponding points under the homeomorphism.

:::

:::

::: {.pf-step #s1-4}

The homeomorphism $h$ restricts to a homeomorphism
$$
\boxed{
\RR^n\setminus\{p\}
\cong
\RR^m\setminus\{q\}}.
$$


::: pf-proof

Since $h$ is bijective and
$$
h(p)=q,
$$
it carries the complement of $\{p\}$ exactly onto the complement of $\{q\}$. The restricted map and its inverse are continuous.

:::

:::

::: {.pf-step #s1-5}

Translation gives
$$
\RR^m\setminus\{q\}
\cong
\RR^m\setminus\{0\}.
$$


::: pf-proof

The map
$$
x\longmapsto x-q
$$
is a homeomorphism of $\RR^m$ sending $q$ to $0$.

:::

:::

::: {.pf-step #s1-6}

For every $k\ge1$,
$$
\boxed{
\RR^k\setminus\{0\}
\simeq
S^{k-1}}.
$$


::: pf-proof

Define
$$
H(x,t)
=
\left(
(1-t)+\frac{t}{\|x\|}
\right)x
$$
for $x\ne0$. The scalar factor is positive, so the homotopy stays in
$$
\RR^k\setminus\{0\}.
$$
At $t=0$, it is the identity, and at $t=1$, it sends $x$ to
$$
x/\|x\|\in S^{k-1}.
$$
Points already on $S^{k-1}$ remain fixed. Thus this is a deformation retraction.

:::

:::

::: {.pf-step #s1-7}

Therefore
$$
\boxed{
\RR^n\setminus\{p\}
\simeq
S^{n-1}}
$$
and
$$
\boxed{
\RR^m\setminus\{q\}
\simeq
S^{m-1}}.
$$


::: pf-proof

For the $n$-dimensional space, $p=0$, so apply step [](#s1-6){.pf-ref} directly. For the $m$-dimensional space, combine step [](#s1-5){.pf-ref} with step [](#s1-6){.pf-ref}.

:::

:::

::: {.pf-step #s1-8}

By steps [](#s1-4){.pf-ref} and [](#s1-7){.pf-ref},
$$
\boxed{
S^{n-1}\simeq S^{m-1}}.
$$


::: pf-proof

Homeomorphic spaces are homotopy equivalent, and homotopy equivalence is transitive.

:::

:::

::: {.pf-step #s1-9}

For every $r\ge0$,
$$
\widetilde H_j(S^r;\ZZ)
\cong
\begin{cases}
\ZZ,&j=r,\\
0,&j\ne r.
\end{cases}
$$


::: pf-proof

This is the standard reduced homology computation for spheres.

:::

:::

::: {.pf-step #s1-10}

Since homotopy equivalent spaces have isomorphic homology groups,
$$
\widetilde H_j(S^{n-1})
\cong
\widetilde H_j(S^{m-1})
$$
for every $j$.


::: pf-proof

Apply homotopy invariance of reduced homology to step [](#s1-8){.pf-ref}.

:::

:::

::: pf-step

Taking
$$
j=n-1,
$$
one has
$$
\widetilde H_{n-1}(S^{n-1})
\cong
\ZZ.
$$


::: pf-proof

Apply step [](#s1-9){.pf-ref} with $r=n-1$.

:::

:::

::: {.pf-step #s1-12}

Hence
$$
\widetilde H_{n-1}(S^{m-1})
\cong
\ZZ.
$$


::: pf-proof

Use the isomorphism from step [](#s1-10){.pf-ref}.

:::

:::

::: {.pf-step #s1-13}

Therefore
$$
n-1=m-1.
$$


::: pf-proof

By step [](#s1-9){.pf-ref}, the only degree in which $S^{m-1}$ has nonzero reduced homology is degree $m-1$. Step [](#s1-12){.pf-ref} shows its reduced homology is nonzero in degree $n-1$. Hence these degrees are equal.

:::

:::

::: {.pf-step #s1-14}

Thus
$$
\boxed{n=m}.
$$


::: pf-proof

Add $1$ to the equality in step [](#s1-13){.pf-ref}. The zero-dimensional case was already handled in step [](#s1-2){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s1-14){.pf-ref} is the required invariance-of-dimension conclusion.

:::

:::

:::
