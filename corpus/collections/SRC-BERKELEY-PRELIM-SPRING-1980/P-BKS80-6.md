---
schema: qual/card@1
id: P-BKS80-6
kind: problem
title: Coset action under a small-index factorial bound
classification: {areas: [prelim], topics: []}
relations: []
review: draft
audit:
- {event: source-checked, by: gpt-5.6-sol, date: 2026-09-13}
- event: solution-written
  by: chatgpt
  date: 2026-09-24
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-24
  note: >-
    The statement is false for G=C_2 and H={e}. Checked that this is the only
    exception: the coset action either has a nontrivial proper kernel or is an
    isomorphism onto S_k; in the latter case A_k gives the required normal
    subgroup for k>=3.
---

::: {.problem}
Let $G$ be a finite group of order $n$ and $H<G$ a proper subgroup of order $m$.
Assume
\[
(n/m)!<2n.
\]
Prove that $G$ has a proper nontrivial normal subgroup.
:::

::: {.solution}
The statement is false as printed. The exceptional case is
$$
G\cong C_2,
\qquad
H=\{e\}.
$$
Indeed, then $n=2$, $m=1$, and
$$
(n/m)!=2!<4=2n,
$$
but $C_2$ has no proper nontrivial subgroup.

The following argument shows that this is the only exception.

<1>1. Put
$$
k\coloneqq[G:H]=\frac nm.
$$
The action of $G$ on the $k$ left cosets of $H$ gives a homomorphism
$$
\varphi:G\longrightarrow S_k
$$
whose kernel $K$ is a proper normal subgroup of $G$.

::: {.proof}
The kernel of any homomorphism is normal. Since $H$ is proper, $k\ge2$,
and the coset action is transitive on at least two points. Hence the action
is not trivial, so $K\ne G$. Thus $K\lhd G$ and $K$ is proper.
:::

<1>2. If $K\ne\{e\}$, then $G$ has the required proper nontrivial normal
subgroup.

::: {.proof}
This is immediate from step <1>1.
:::

<1>3. Suppose $K=\{e\}$. Then
$$
G\cong S_k.
$$

::: {.proof}
If $K$ is trivial, then $\varphi$ is injective, so
$$
n=|G|=|\varphi(G)|
$$
divides $|S_k|=k!$. Therefore
$$
[S_k:\varphi(G)]
=
\frac{k!}{n}.
$$
The hypothesis $k!<2n$ gives
$$
1\le\frac{k!}{n}<2.
$$
The index is an integer, so it equals $1$. Hence
$\varphi(G)=S_k$ and $G\cong S_k$.
:::

<1>4. Under the hypothesis of step <1>3, if $k\ge3$, then $G$ has a
proper nontrivial normal subgroup.

::: {.proof}
For $k\ge3$, the alternating group
$$
A_k
$$
is a proper nontrivial normal subgroup of $S_k$. Transporting it through
the isomorphism in step <1>3 gives a proper nontrivial normal subgroup of
$G$.
:::

<1>5. Under the hypothesis of step <1>3, if $k=2$, then
$$
G\cong C_2
\qquad\text{and}\qquad
H=\{e\}.
$$

::: {.proof}
Step <1>3 gives $G\cong S_2\cong C_2$, so $n=2$. Since
$$
k=\frac nm=2,
$$
one has $m=1$, hence $H=\{e\}$.
:::

<1>6. Consequently the sharp conclusion under the printed hypotheses is:
$$
\boxed{
\text{either }(G,H)\cong(C_2,\{e\}),
\text{ or }G\text{ has a proper nontrivial normal subgroup}.}
$$

::: {.proof}
If the kernel $K$ from step <1>1 is nontrivial, apply step <1>2. If it is
trivial, step <1>3 identifies $G$ with $S_k$; step <1>4 settles $k\ge3$,
while step <1>5 identifies the unique remaining case $k=2$ with the
displayed exception.
:::

<1>7. Q.E.D.

::: {.proof}
The opening counterexample disproves the statement as printed, and step
<1>6 proves the corrected assertion with the unique exceptional case.
:::
:::
