---
schema: qual/card@1
id: P-APASP07K
kind: problem
title: "Equivalent representations yield the same Hilbert series of invariant rings"
classification:
  areas:
  - applied-algebra
  topics:
  - Commutative Algebra
  - Representation Theory
relations: []
review: draft
audit:
- event: solution-written
  by: OpenAI
  date: 2026-09-10
- event: solution-reviewed
  by: claude
  date: 2026-11-18
  note: >-
    Restructured into Lamport steps; checked that equivalence gives a single intertwining P,
    that f -> f o P is a graded algebra automorphism, the intertwining computation (P*f)(B_g
    v) = f(A_g (Pv)) giving the bijection of invariant rings, and the degree-wise
    isomorphism yielding the same Hilbert series. For (b): invariants of diag(-1,1) are
    C[x^2,y] with series 1/((1-t^2)(1-t)), invariants of -I are the even-degree polynomials
    with series sum (2m+1)t^{2m} = (1+t^2)/(1-t^2)^2, and the two differ, shown by the
    orders of the pole at t = 1 rather than asserted. The argument is the card's own; no
    retained set is cited.
---

::: {.problem}
(a) Show the following: Let $G$ be a finite group, and let $g \mapsto A_g \in \operatorname{GL}(\CC^n)$ and $g \mapsto B_g \in \operatorname{GL}(\CC^n)$ be two equivalent representations of $G$.
Show that the rings of invariants $\CC[x_1, x_2, \ldots, x_n]^G$ defined by these two actions have the same Hilbert series.

(b) Give two examples of an action of a group $G$ on a two-dimensional vector space which lead to two different Hilbert series of the corresponding rings $\CC[x,y]^G$.
:::

::: {.solution}
The argument is the card's own; no retained solution set is cited on it. Write $V=\CC^{n}$ and $\CC[V]=\CC[x_{1},\dots,x_{n}]$, graded by total degree, and for a representation $\rho$ let $\CC[V]^{G,\rho}=\{f: f(\rho(g)v)=f(v)\ \text{for all } g\in G,\ v\in V\}$.

::: pf

::: {.pf-step #setup}
(a) Equivalence means $B_{g}=PA_{g}P^{-1}$ for one $P\in GL_{n}(\CC)$ and all $g$; the map $P^{*}f=f\circ P$ is a graded algebra automorphism of $\CC[V]$.

::: pf-proof
By hypothesis there is a single $P$ with $B_{g}=PA_{g}P^{-1}$ for every $g$, equivalently $A_{g}=P^{-1}B_{g}P$. The map $f\mapsto f\circ P$ is an algebra homomorphism because composition with a linear map is, it is invertible with inverse $f\mapsto f\circ P^{-1}$, and it preserves total degree because $P$ is linear.
:::

:::

::: {.pf-step #intertwining}
(a) $f\in\CC[V]^{G,A}$ if and only if $P^{*}f\in\CC[V]^{G,B}$.

::: pf-proof
For $g\in G$ and $v\in V$,
$$
(P^{*}f)(B_{g}v)=f(PB_{g}v)=f\big(PB_{g}P^{-1}(Pv)\big)=f(A_{g}(Pv)),
$$
so $(P^{*}f)(B_{g}v)=(P^{*}f)(v)$ for all $g,v$ exactly when $f(A_{g}w)=f(w)$ for all $g$ and all $w=Pv$; since $P$ is onto, that is exactly the invariance of $f$ for $A$. The correspondence is bijective because $P^{*}$ is an automorphism, so it also carries invariants for $B$ back to invariants for $A$.
:::

:::

::: {.pf-step #part-a}
(a) $\CC[V]^{G,A}$ and $\CC[V]^{G,B}$ have the same Hilbert series.

::: pf-proof
By step [](#intertwining){.pf-ref} the automorphism $P^{*}$ restricts to a bijection between the two invariant rings, and by step [](#setup){.pf-ref} it preserves degrees, so it restricts to an isomorphism of each homogeneous piece $\CC[V]^{G,A}_{d}\to\CC[V]^{G,B}_{d}$; the dimensions of these pieces are the coefficients of the Hilbert series, so the two series coincide.
:::

:::

::: {.pf-step #example-one}
(b) For $G=C_{2}=\{1,s\}$ acting by $s\mapsto\operatorname{diag}(-1,1)$ one has $\CC[x,y]^{G}=\CC[x^{2},y]$ and $H_{1}(t)=\dfrac{1}{(1-t^{2})(1-t)}$.

::: pf-proof
$s$ sends $x^{a}y^{b}$ to $(-1)^{a}x^{a}y^{b}$, so the invariant monomials are those with $a$ even, and they are exactly the monomials of $\CC[x^{2},y]$. A basis of the invariant ring is $\{(x^{2})^{i}y^{j}\}$ with degrees $2i+j$, so the Hilbert series is $\sum_{i,j\ge0}t^{2i+j}=\big(\sum_i t^{2i}\big)\big(\sum_j t^{j}\big)=\frac{1}{(1-t^{2})(1-t)}$.
:::

:::

::: {.pf-step #example-two}
(b) For $G=C_{2}$ acting by $s\mapsto-I_{2}$ one has $H_{2}(t)=\dfrac{1+t^{2}}{(1-t^{2})^{2}}$.

::: pf-proof
$s$ sends $x^{a}y^{b}$ to $(-1)^{a+b}x^{a}y^{b}$, so the invariant monomials are those of even total degree. The degree-$2m$ homogeneous piece of $\CC[x,y]$ has dimension $2m+1$ (the monomials $x^{2m},x^{2m-1}y,\dots,y^{2m}$) and consists entirely of invariants, while the degree-$2m+1$ piece contains no invariant monomial. Hence $H_{2}(t)=\sum_{m\ge0}(2m+1)t^{2m}$, and with $u=t^{2}$ the identity $\sum_{m\ge0}(2m+1)u^{m}=\frac{1+u}{(1-u)^{2}}$ — from $\sum(m+1)u^{m}=1/(1-u)^{2}$ and $\sum m u^{m}=u/(1-u)^{2}$ — gives $H_{2}(t)=\frac{1+t^{2}}{(1-t^{2})^{2}}$.
:::

:::

::: {.pf-step #different}
(b) Both groups are $C_{2}$ acting on a two-dimensional space, and $H_{1}\ne H_{2}$.

::: pf-proof
If $t\to1$ then $H_{1}(t)\sim\frac{1}{2(1-t)}$, a simple pole, while $H_{2}(t)=\frac{1+t^{2}}{(1-t^{2})^{2}}\sim\frac{2}{4(1-t)^{2}}=\frac{1}{2(1-t)^{2}}$, a double pole; a rational function has a pole of a definite order at $t=1$, so $H_{1}\ne H_{2}$.
:::

:::

::: {.pf-step}
Both parts hold.

::: pf-proof
Step [](#part-a){.pf-ref} is (a); steps [](#example-one){.pf-ref}, [](#example-two){.pf-ref} and [](#different){.pf-ref} are the two examples and their disagreement, which is (b).
:::

:::

:::
:::
