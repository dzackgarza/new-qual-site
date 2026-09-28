---
schema: qual/card@1
id: P-W13SP
kind: problem
title: A subgroup of index equal to the smallest prime dividing $|G|$ is normal
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
  note: "Compared the smallest-prime hypothesis and conclusion with July 2013 Groups 3 in the retained source extraction."
- event: solution-written
  by: chatgpt
  date: 2026-09-10
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-10
  note: "Checked the coset kernel, the cancellation from p[H:K] dividing p!, and the prime-divisor obstruction, including p=2."
---

::: {.problem}
Let $p$ be the smallest prime dividing the order of the finite group $G$.
Show that any subgroup of $G$ of index $p$ is normal in $G$.
:::

::: {.solution}
Let $H\leq G$ have index $p$.

<1>1. There is a normal subgroup $K\lhd G$ with $K\leq H$
and $[G:K]\mid p!$.

::: {.proof}
Act on the set $X=G/H$ of left cosets by left multiplication.
The rule $\rho(g)(xH)=gxH$ is well-defined, since replacing
$x$ by $xh$, with $h\in H$, does not change $gxH$.
Its inverse is $\rho(g^{-1})$, and
$\rho(g_1g_2)=\rho(g_1)\rho(g_2)$, so it defines a
homomorphism $\rho:G\to\operatorname{Sym}(X)$.

Its kernel $K$ is normal. Every $k\in K$ fixes $H\in X$,
so $kH=H$ and $k\in H$. The first isomorphism theorem
identifies $G/K$ with $\rho(G)$ [@DF04]. Since $|X|=p$,
the group $\operatorname{Sym}(X)$ has order $p!$.
Lagrange's theorem therefore gives $[G:K]\mid p!$.
:::

<1>2. The subgroup $K$ equals $H$.

::: {.proof}
Put $m=[H:K]$. The index formula gives
$$
[G:K]=[G:H][H:K]=pm.
$$
Since $pm\mid p!=p(p-1)!$, cancellation of the positive
integer $p$ gives $m\mid(p-1)!$. Also $m$ divides
$|H|$, which divides $|G|$.

If $m>1$, it has a prime divisor $q$. Divisibility by
$(p-1)!$ implies $q\leq p-1$, whereas $q\mid|G|$
and the definition of $p$ imply $q\geq p$. This is a
contradiction. Hence $m=1$ and $H=K$. By step <1>1,
$H$ is normal in $G$.
:::
:::
