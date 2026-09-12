---
schema: qual/card@1
id: P-W13IN
kind: problem
title: A subgroup of index $n$ contains a normal subgroup $K$ with $[G:K]$ dividing
  $n!$
classification:
  areas:
  - algebra
  topics:
  - Normal Subgroups
  - Group Actions
  - Cosets and Lagrange
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-10
  note: "Visually compared the subgroup containment, normality, and factorial-divisibility request with July 2013 Groups 2 on PDF page 6."
- event: solution-written
  by: chatgpt
  date: 2026-09-10
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-10
  note: "Checked the coset-action well-definedness, exact intersection formula for its kernel, and divisibility rather than only an upper bound; included index one."
---

::: problem
Let $G$ be a finite group and $H$ be a subgroup of $G$ of index $n$.
Show that $H$ has a subgroup $K$ such that $K$ is normal in $G$ and $[G : K]$ divides $n!$.
:::

::: solution
Take the core of $H$ in $G$,
$$
K=\bigcap_{x\in G}xHx^{-1}.
$$

<1>1. Left multiplication defines an action of $G$ on the
set $X=\{xH:x\in G\}$ of its $n$ left cosets.

::: proof
For $g\in G$, set $\rho(g)(xH)=gxH$.
If $xH=yH$, then $x=yh$ for some $h\in H$, and
$gxH=gyhH=gyH$. Thus the map is independent of the chosen
representative. Its inverse is $\rho(g^{-1})$, and
$\rho(gh)(xH)=ghxH=\rho(g)\rho(h)(xH)$.
Consequently $\rho:G\to\operatorname{Sym}(X)$ is a group
homomorphism.
:::

<1>2. Its kernel is precisely $K$, which is normal in $G$
and contained in $H$.

::: proof
An element $g$ fixes the coset $xH$ exactly when
$gxH=xH$, or equivalently $x^{-1}gx\in H$.
It fixes every coset exactly when $g\in xHx^{-1}$ for every
$x\in G$. This proves $\ker\rho=K$.
A kernel is a normal subgroup, and the term $x=1$ in the
intersection shows $K\subseteq H$.
:::

<1>3. The index $[G:K]$ divides $n!$.

::: proof
The first isomorphism theorem gives
$G/K\cong\rho(G)\leq\operatorname{Sym}(X)$ [@DF04].
There are $n!$ permutations of a set of $n$ elements.
Lagrange's theorem therefore implies
$$
[G:K]=|\rho(G)|\mid|\operatorname{Sym}(X)|=n!.
$$
If $n=1$, the action is trivial and the construction gives
$K=H=G$, with index $1=1!$.
:::
:::
