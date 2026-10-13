---
schema: qual/card@1
id: P-PRACT20-W5-07
kind: problem
title: A group is not a union of two proper subgroups but can be a union of three
classification:
  areas:
  - algebra
  topics: []
relations: []
review: draft
---

::: {.problem}
Show that a group is never the union of two of its proper subgroups. Show by example that a group can be the union of three of its proper subgroups.
:::

::: {.solution}
<1>1. Let $H,K<G$ be proper subgroups. If one is contained in the other,
then
\[
H\cup K\ne G.
\]

::: {.proof}
If, for example, $H\subseteq K$, then
\[
H\cup K=K.
\]
Since $K$ is proper, $K\ne G$.
:::

<1>2. Suppose neither $H$ nor $K$ contains the other. Choose
\[
h\in H\setminus K,
\qquad
k\in K\setminus H.
\]
Then
\[
hk\notin H\cup K.
\]

::: {.proof}
If $hk\in H$, then since $h^{-1}\in H$,
\[
k=h^{-1}(hk)\in H,
\]
contradicting $k\notin H$.

If $hk\in K$, then since $k^{-1}\in K$,
\[
h=(hk)k^{-1}\in K,
\]
contradicting $h\notin K$.
Thus $hk$ lies in neither subgroup.
:::

<1>3. Hence a group cannot be the union of two proper subgroups:
\[
\boxed{G\ne H\cup K\qquad(H,K<G)}.
\]

::: {.proof}
Step <1>1 handles the containment case, while step <1>2 handles the remaining
case.
:::

<1>4. The Klein four group is the union of three proper subgroups.

::: {.proof}
Write
\[
V_4=\{e,a,b,c\},
\]
with
\[
a^2=b^2=c^2=e.
\]
Then
\[
H_a=\{e,a\},
\qquad
H_b=\{e,b\},
\qquad
H_c=\{e,c\}
\]
are proper subgroups and
\[
\boxed{V_4=H_a\cup H_b\cup H_c}.
\]
:::

<1>5. Q.E.D.

::: {.proof}
Step <1>3 proves the impossibility for two proper subgroups, and step <1>4
gives the requested three-subgroup example.
:::
:::
