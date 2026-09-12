---
schema: qual/card@1
id: E-MSDCC
kind: problem
title: On subgroups
classification:
  areas:
  - algebra
  topics:
  - Subgroups
  - Cyclic Groups
  - Sylow Theory
relations: []
review: draft
audit:
- event: solution-written
  by: OpenAI
  date: 2026-09-09
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-09
---

::: {.exercise}
\envlist

- Show that the intersection of two subgroups is again a subgroup.

  - Hint: one-step subgroup test.

- Show that if $H\cong C_m$ and $K\cong C_n$ are cyclic subgroups of $G$, then $|H\intersect K|$ divides $\gcd(m,n)$. If $H$ and $K$ lie in a common cyclic subgroup of $G$, show that $H\intersect K\cong C_d$ where $d=\gcd(m,n)$.

- Show that the intersection of two subgroups with coprime orders is trivial.

- Show that the union of two subgroups $H,K$ is a subgroup iff $H\subseteq K$ or $K\subseteq H$, and so is generally *not* a subgroup.

- Show that subgroups with the *same* prime order are either equal or intersect trivially.

- **Important for Sylow theory**: show (perhaps by example) that if $S_1, S_2$ are distinct subgroups of order $p^k$, then it's possible for their intersection to be trivial **or** for them to intersect in a subgroup of order $p^\ell$ for $1\leq \ell \leq k-1$.

- Give a counterexample where $H,K\leq G$ but $HK$ is not a subgroup of $G$.
:::

::: {.solution}
<1>1. The intersection of two subgroups is a subgroup.
::: {.proof}
Let $H,K\le G$. The identity lies in both subgroups, so $H\cap K$ is nonempty. If $x,y\in H\cap K$, then $x,y\in H$ and $x,y\in K$. Since both are subgroups,
\[
xy^{-1}\in H
\qquad\text{and}\qquad
xy^{-1}\in K.
\]
Hence $xy^{-1}\in H\cap K$. The one-step subgroup test gives $H\cap K\le G$.
:::

<1>2. If $H\cong C_m$ and $K\cong C_n$, then
\[
|H\cap K|\mid\gcd(m,n).
\]
If moreover $H$ and $K$ lie in a common cyclic subgroup, then
\[
H\cap K\cong C_{\gcd(m,n)}.
\]
::: {.proof}
By <1>1, $H\cap K$ is a subgroup of both $H$ and $K$. Lagrange's theorem therefore gives
\[
|H\cap K|\mid m,
\qquad
|H\cap K|\mid n,
\]
so $|H\cap K|\mid\gcd(m,n)$.

Now suppose $H,K\le C$ for a cyclic group $C$. Put $d=\gcd(m,n)$. A cyclic group has a unique subgroup of each order dividing its order. Let $D\le C$ be the unique subgroup of order $d$. Since $d\mid m$ and $d\mid n$, one has $D\le H$ and $D\le K$, hence $D\le H\cap K$. The first paragraph gives $|H\cap K|\le d$, while $|D|=d$, so $H\cap K=D\cong C_d$.
:::

<1>3. Subgroups of coprime finite orders intersect trivially.
::: {.proof}
If $|H|$ and $|K|$ are coprime, then by <1>2 the order of $H\cap K$ divides both $|H|$ and $|K|$. Hence
\[
|H\cap K|=1,
\]
so $H\cap K=\{e\}$.
:::

<1>4. The union $H\cup K$ is a subgroup if and only if $H\subseteq K$ or $K\subseteq H$.
::: {.proof}
If $H\subseteq K$, then $H\cup K=K$; similarly if $K\subseteq H$.

Conversely, suppose $H\cup K$ is a subgroup and neither subgroup contains the other. Choose
\[
h\in H\setminus K,
\qquad
k\in K\setminus H.
\]
Since $H\cup K$ is assumed to be a subgroup, $hk\in H\cup K$. If $hk\in H$, then
\[
k=h^{-1}(hk)\in H,
\]
a contradiction. If $hk\in K$, then
\[
h=(hk)k^{-1}\in K,
\]
again a contradiction. Thus one subgroup must contain the other.
:::

<1>5. Two subgroups of the same prime order are either equal or intersect trivially.
::: {.proof}
Let $|H|=|K|=p$ with $p$ prime. By Lagrange,
\[
|H\cap K|\mid p,
\]
so $|H\cap K|$ is either $1$ or $p$. In the first case the intersection is trivial. In the second case $H\cap K$ has the same order as both $H$ and $K$, hence
\[
H=H\cap K=K.
\]
:::

<1>6. Distinct subgroups of order $p^k$ can have trivial intersection or intersection of order $p^\ell$ for every $1\le\ell\le k-1$.
::: {.proof}
Work in elementary abelian $p$-groups, viewed as vector spaces over $\FF_p$.

For trivial intersection, take
\[
G=\FF_p^{2k},
\quad
S_1=\spanof\{e_1,\ldots,e_k\},
\quad
S_2=\spanof\{e_{k+1},\ldots,e_{2k}\}.
\]
Then $|S_1|=|S_2|=p^k$ and $S_1\cap S_2=0$.

For $1\le\ell\le k-1$, take
\[
G=\FF_p^{2k-\ell},
\]
and define
\[
S_1=\spanof\{e_1,\ldots,e_k\},
\]
\[
S_2=\spanof\{e_1,\ldots,e_\ell,e_{k+1},\ldots,e_{2k-\ell}\}.
\]
Both have dimension $k$, hence order $p^k$, while
\[
S_1\cap S_2=\spanof\{e_1,\ldots,e_\ell\}
\]
has dimension $\ell$ and order $p^\ell$.
:::

<1>7. A product $HK$ of subgroups need not be a subgroup.
::: {.proof}
Take $G=S_3$,
\[
H=\langle(12)\rangle,
\qquad
K=\langle(23)\rangle.
\]
Then
\[
HK=\{e,(12),(23),(123)\},
\]
so $|HK|=4$. If $HK$ were a subgroup of $S_3$, Lagrange's theorem would force $4\mid6$, which is false. Hence $HK$ is not a subgroup.
:::
:::
