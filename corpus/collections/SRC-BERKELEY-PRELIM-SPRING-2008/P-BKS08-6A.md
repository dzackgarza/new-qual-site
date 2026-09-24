---
schema: qual/card@1
id: P-BKS08-6A
kind: problem
title: A finite group with one automorphism has order at most two
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against the vendored UC Berkeley Spring 2008 preliminary-exam solution packet, which reproduces the problem statement with its solution.
- event: solution-written
  by: chatgpt
  date: 2026-09-24
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-24
  note: >-
    Independently checked the reduction from trivial inner automorphisms to an
    elementary abelian 2-group and the nontrivial coordinate-swap automorphism
    in dimension at least two.
---

::: {.problem}
Suppose \(G\) is a finite group with only one automorphism.
Show that
\[
|G|\le2.
\]
:::

::: {.solution}
<1>1. The group $G$ is abelian.

::: {.proof}
For every $g\in G$, conjugation
$$
c_g(h)=ghg^{-1}
$$
is an automorphism of $G$. Since $G$ has only one automorphism and the
identity map is an automorphism, every $c_g$ must be the identity.
Thus every $g$ commutes with every $h$, so $G$ is abelian.
:::

<1>2. Every element of $G$ has order dividing $2$.

::: {.proof}
By step <1>1, inversion
$$
\iota(g)=g^{-1}
$$
is an automorphism of $G$. It must therefore be the identity
automorphism. Hence $g=g^{-1}$ for every $g\in G$, so $g^2=e$.
:::

<1>3. The group $G$ is isomorphic to $(\ZZ/2\ZZ)^r$ for some
integer $r\ge0$.

::: {.proof}
Step <1>1 makes $G$ abelian, and step <1>2 says every element is
annihilated by $2$. Therefore $G$ is a finite-dimensional vector space
over $\FF_2$, hence has the displayed form.
:::

<1>4. One has $r\le1$.

::: {.proof}
If $r\ge2$, choose a basis $e_1,\ldots,e_r$ of the
$\FF_2$-vector space $G$. The linear map exchanging $e_1$ and $e_2$
and fixing all other basis vectors is a nonidentity automorphism of
$G$, contradicting the hypothesis. Thus $r\le1$.
:::

<1>5. Therefore
$$
\boxed{\abs{G}\le2}.
$$

::: {.proof}
By steps <1>3--<1>4,
$$
\abs{G}=2^r
$$
with $r\le1$, so $\abs{G}\le2$.
:::

<1>6. Q.E.D.

::: {.proof}
Step <1>5 is the required conclusion.
:::
:::
