---
schema: qual/card@1
id: P-BKF07-5A
kind: problem
title: Finite groups whose every subgroup is a retract
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
  note: Checked against the vendored UC Berkeley Fall 2007 preliminary-exam solution packet, which reproduces the problem statement with its solution.
- event: solution-written
  by: chatgpt
  date: 2026-09-24
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-24
  note: >-
    Independently checked the retained induction, including inheritance of
    the retract property by the kernel subgroup and injectivity of the product
    map to K x H.
---

::: {.problem}
Suppose \(G\) is a finite group such that for every subgroup \(H\le G\) there is a homomorphism
\[
\phi:G\to H
\]
with \(\phi(h)=h\) for every \(h\in H\). Show that \(G\) is a direct product of groups of prime order.
:::

::: {.solution}
<1>1. The claim holds when $G$ is trivial.

::: {.proof}
The trivial group is the empty direct product of groups of prime
order.
:::

<1>2. Assume $G$ is nontrivial and that the claim holds for all
smaller finite groups satisfying the same retract hypothesis. Choose
a subgroup $H\le G$ of prime order $p$.

::: {.proof}
By Cauchy's theorem, if a prime $p$ divides $\abs G$, then $G$ has an
element of order $p$. The subgroup it generates has order $p$.
:::

<1>3. Let
$$
\phi:G\longrightarrow H
$$
be a retraction supplied by the hypothesis, and set
$$
K=\ker\phi.
$$
Then
$$
\abs G=\abs K\,\abs H
$$
and $K$ is strictly smaller than $G$.

::: {.proof}
Since $\phi$ restricts to the identity on $H$, it is surjective.
The first isomorphism theorem therefore gives
$$
G/K\cong H,
$$
so
$$
[G:K]=\abs H=p.
$$
Thus $\abs G=\abs K\,\abs H$ and $\abs K<\abs G$.
:::

<1>4. The group $K$ satisfies the same retract hypothesis.

::: {.proof}
Let $L\le K$. By the hypothesis on $G$, there is a homomorphism
$$
\rho:G\longrightarrow L
$$
such that $\rho(\ell)=\ell$ for every $\ell\in L$. Restricting $\rho$
to $K$ gives a homomorphism
$$
\rho|_K:K\longrightarrow L
$$
which is still the identity on $L$. Hence every subgroup of $K$ is a
retract of $K$.
:::

<1>5. The group $K$ is a direct product of groups of prime order.

::: {.proof}
By steps <1>3--<1>4, $K$ is smaller than $G$ and satisfies the
induction hypothesis.
:::

<1>6. Let
$$
\sigma:G\longrightarrow K
$$
be a retraction onto $K$, and define
$$
\alpha:G\longrightarrow K\times H,
\qquad
\alpha(g)=(\sigma(g),\phi(g)).
$$
Then $\alpha$ is injective.

::: {.proof}
The subgroup $K\le G$ has a retraction $\sigma$ by the original
hypothesis. Both components of $\alpha$ are homomorphisms, so
$\alpha$ is a homomorphism.

If $g\in\ker\alpha$, then $\phi(g)=1$, so $g\in K$. But
$\sigma|_K=\operatorname{id}_K$, while $\sigma(g)=1$. Hence $g=1$.
Thus $\ker\alpha=\{1\}$ and $\alpha$ is injective.
:::

<1>7. The map $\alpha$ is an isomorphism
$$
G\cong K\times H.
$$

::: {.proof}
By step <1>3,
$$
\abs G=\abs K\,\abs H=\abs{K\times H}.
$$
The injective map $\alpha$ from step <1>6 is therefore a bijection
between finite groups of equal order, hence an isomorphism.
:::

<1>8. Therefore $G$ is a direct product of groups of prime order.

::: {.proof}
By step <1>5, write $K$ as a direct product of groups of prime order.
The group $H$ itself has prime order. Step <1>7 gives
$$
G\cong K\times H,
$$
so adjoining the factor $H$ gives the required decomposition.
:::

<1>9. Q.E.D.

::: {.proof}
Steps <1>1--<1>8 complete the induction on $\abs G$.
:::
:::
