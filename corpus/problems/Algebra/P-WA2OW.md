---
schema: qual/card@1
id: P-WA2OW
kind: problem
title: The group algebra over $\CC$ versus other fields, and when the characteristic divides $\cardinality{G}$
classification:
  areas:
  - algebra
  topics:
  - Group Rings
  - Representation Theory
  - Characteristic
relations: []
review: draft
audit:
- event: solution-reviewed
  by: claude
  date: 2026-11-06
  note: >-
    Rewritten as a Lamport structured proof with Maschke's averaging argument
    broken into its three steps (a linear projection onto the submodule, the
    averaged equivariant projection, and the kernel as stable complement). What
    was checked: the statement (three questions — describe k[G], what is special
    about C, what changes when char k divides |G| — all answered, no repair
    needed), and the existing prose solution against a fresh re-derivation:
    Maschke, Artin-Wedderburn over an algebraically closed field, the central
    idempotent-style argument N^2 = |G|N = 0 in characteristic p, and the cyclic
    example (g-1)^p = g^p - 1, whose middle binomial coefficients vanish in
    characteristic p. All correct; the one point the prose left implicit is
    that the nonzero ideal k[G]N has square zero, which the structured proof now
    states. No source solution is retained for this card, so no source
    comparison was made. What was not checked: any printed source.
---

::: {.problem}
For a finite group $G$ and a field $k$, describe the group algebra $k[G]$. What is special about $k=\CC$, and what changes when $\operatorname{char}k$ divides $\cardinality{G}$?
:::

::: {.solution}
Throughout, $G$ is a finite group, $k$ is a field, $V$ is a finite-dimensional $k$-vector space, and $g\cdot v$ denotes the action of $g\in G$ on $v\in V$.

::: pf

::: {.pf-step #algebra}
$k[G]$ is the $k$-algebra with $k$-basis $G$ and product $\left(\sum_{g}a_gg\right)\left(\sum_{h}b_hh\right)=\sum_{g,h}a_gb_h\,gh$, and a $k$-linear representation of $G$ on $V$ is the same data as a left $k[G]$-module structure on $V$.

::: pf-proof
The product is $k$-bilinear by construction, so it extends the group law to the span of $G$ uniquely; associativity follows from associativity in $G$ coefficient by coefficient, and the identity element of $G$ is a two-sided identity for the span. A representation is a group homomorphism $\rho\colon G\to\GL(V)$, and $\left(\sum_g a_gg\right)\cdot v\coloneqq\sum_g a_g\rho(g)(v)$ is the unique left $k[G]$-module structure on $V$ extending it; conversely a left $k[G]$-module restricts to a homomorphism $G\to\GL(V)$.
:::

:::

::: {.pf-step #maschke}
If $\operatorname{char}k$ does not divide $\cardinality{G}$, then every $k[G]$-submodule $W\leq V$ has a $k[G]$-stable complement, and consequently $k[G]$ is semisimple.

::: pf-proof
Write $e=\cardinality{G}^{-1}\in k$, which exists because $\operatorname{char}k\nmid\cardinality{G}$.

::: {.pf-step #proj}
There is a $k$-linear map $\pi\colon V\to V$ with image $W$ and $\pi(w)=w$ for every $w\in W$.

::: pf-proof
Choose a $k$-basis $w_1,\ldots,w_m$ of $W$ and extend it to a $k$-basis $w_1,\ldots,w_m,u_1,\ldots,u_r$ of $V$. The assignment $\pi(w_i)=w_i$, $\pi(u_j)=0$, extended $k$-linearly, is a well-defined $k$-linear map, its image is spanned by $w_1,\ldots,w_m$ and hence is $W$, and it fixes each $w_i$, hence every element of $W$.
:::

:::

::: {.pf-step #average}
The map $\bar\pi(v)=e\sum_{g\in G}g\cdot\pi(g^{-1}\cdot v)$ is $k$-linear, has image in $W$, fixes every $w\in W$, and satisfies $\bar\pi(h\cdot v)=h\cdot\bar\pi(v)$ for every $h\in G$.

::: pf-proof
The sum is finite and its coefficients lie in $k$, so $\bar\pi$ is defined; each $v\mapsto g\cdot\pi(g^{-1}\cdot v)$ is $k$-linear as a composite of $k$-linear maps, so the sum is $k$-linear. Its values lie in $W$ because $\pi$ takes values in $W$ and $W$ is a $k[G]$-submodule. For $w\in W$ and $g\in G$ we have $g^{-1}\cdot w\in W$, so $\pi(g^{-1}\cdot w)=g^{-1}\cdot w$ by step [](#proj){.pf-ref}, hence $g\cdot\pi(g^{-1}\cdot w)=w$ and $\bar\pi(w)=e\cardinality{G}\,w=w$. For equivariance, fix $h\in G$; then
$$\bar\pi(h\cdot v)=e\sum_{g\in G}g\cdot\pi(g^{-1}h\cdot v)=e\sum_{k\in G}hk\cdot\pi(k^{-1}\cdot v)=h\cdot\bar\pi(v),$$
where the middle equality is the substitution $g=hk$, a permutation of the finite group $G$.
:::

:::

::: {.pf-step #complement}
$\ker\bar\pi$ is a $k[G]$-submodule of $V$ and $V=W\oplus\ker\bar\pi$.

::: pf-proof
The kernel of a $k$-linear map is a $k$-subspace, and it is stable under $G$ because $\bar\pi(h\cdot v)=h\cdot\bar\pi(v)$ by step [](#average){.pf-ref}, so $h\cdot v\in\ker\bar\pi$ whenever $v\in\ker\bar\pi$. If $v\in W\cap\ker\bar\pi$ then $v=\bar\pi(v)=0$, since $\bar\pi$ fixes $W$. Every $v\in V$ splits as $v=\bar\pi(v)+(v-\bar\pi(v))$, with $\bar\pi(v)\in W$ by step [](#average){.pf-ref} and $\bar\pi(v-\bar\pi(v))=\bar\pi(v)-\bar\pi(v)=0$; so $V=W+\ker\bar\pi$ and the sum is direct.
:::

:::

By steps [](#proj){.pf-ref}, [](#average){.pf-ref} and [](#complement){.pf-ref} every $k[G]$-submodule $W$ of every finite-dimensional $V$ has a $k[G]$-stable complement, which is complete reducibility of finite-dimensional $k[G]$-modules. A finite-dimensional algebra is semisimple exactly when all of its finite-dimensional modules are semisimple, and the splitting just constructed applies to a submodule of any finite-dimensional module, so $k[G]$ is semisimple.
:::

:::

::: {.pf-step #split-complex}
Over $k=\CC$ every irreducible representation of $G$ is absolutely irreducible, and $\CC[G]\cong\prod_{i}\Mat_{n_i}(\CC)$, the product running over the irreducible complex representations, of degrees $n_i$.

::: pf-proof
$\CC$ is algebraically closed, so the endomorphism algebra of an irreducible representation, a finite-dimensional division algebra over $\CC$, is $\CC$ itself; that is absolute irreducibility. By step [](#maschke){.pf-ref} the algebra $\CC[G]$ is semisimple, and by Artin--Wedderburn a finite-dimensional semisimple algebra over an algebraically closed field is a finite product of full matrix algebras over that field, one factor per irreducible representation, of size its degree.
:::

:::

::: {.pf-step #char-p}
If $\operatorname{char}k=p$ divides $\cardinality{G}$ and $N=\sum_{g\in G}g$, then $N\neq0$ and $N^2=0$, so $k[G]N$ is a two-sided ideal with square zero, and $k[G]$ is not semisimple.

::: pf-proof
$N\neq0$ because $G$ is a $k$-basis of $k[G]$ and every coefficient of $N$ is $1\in k$. For $h\in G$ we have $hN=\sum_g hg=N$ and $Nh=\sum_g gh=N$, so $N$ commutes with every basis element and hence is central, which makes $k[G]N$ a two-sided ideal. Then $N^2=N\cdot N=\sum_{h\in G}hN=\sum_{h\in G}N=\cardinality{G}\cdot N$, which is $0$ because $\cardinality{G}=0$ in $k$ when $p$ divides it. For $a,b\in k[G]$ therefore $(aN)(bN)=abN^2=0$, so the nonzero ideal $k[G]N$ has square zero. A semisimple ring has no nonzero nilpotent ideal, so $k[G]$ is not semisimple.
:::

:::

::: {.pf-step #cyclic}
For $G=C_p=\generators{g}$ in characteristic $p$, the element $g-1$ is nonzero and $(g-1)^p=0$.

::: pf-proof
In characteristic $p$ each binomial coefficient $\binom{p}{j}$ vanishes in $k$ for $0<j<p$, so $(g-1)^p=g^p-1$; and $g^p=1$ because $G$ has order $p$. The element $g-1$ is nonzero because $g$ and $1$ are distinct elements of the basis $G$.
:::

:::

::: {.pf-step}
$k[G]$ is semisimple if and only if $\operatorname{char}k$ does not divide $\cardinality{G}$; over $\CC$ it is the split semisimple algebra $\prod_i\Mat_{n_i}(\CC)$.

::: pf-proof
One direction is step [](#maschke){.pf-ref}, and the other is step [](#char-p){.pf-ref}, where the nonzero ideal $k[G]N$ with zero square rules out semisimplicity; the cyclic case of step [](#cyclic){.pf-ref} exhibits the same failure with the single nilpotent element $g-1$. The description over $\CC$ is step [](#split-complex){.pf-ref}. Nothing in the definition of $k[G]$ distinguishes $\CC$ from another field: what $\CC$ supplies is algebraic closure, so that every irreducible is absolutely irreducible and the product decomposition is by matrix algebras of the degrees, while semisimplicity depends only on whether $\operatorname{char}k$ divides $\cardinality{G}$.
:::

:::

:::
:::
