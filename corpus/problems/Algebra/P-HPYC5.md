---
schema: qual/card@1
id: P-HPYC5
kind: problem
title: $A_n$ is simple for $n \geq 5$
classification:
  areas:
  - algebra
  topics:
  - Simple Groups
  - Permutations
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

::: problem
- Argue that $A_n$ is simple for $n \geq 5$.
:::


::: {.solution}
Let $n\ge5$, and let $N\trianglelefteq A_n$ be nontrivial. We prove $N=A_n$.
For a permutation $\sigma$, write $\operatorname{supp}(\sigma)$ for the set of points moved by $\sigma$.

<1>1. Choose $1\ne\sigma\in N$ with $|\operatorname{supp}(\sigma)|$ minimal. Then $|\operatorname{supp}(\sigma)|\le5$.
::: {.proof}
Suppose instead that $\sigma$ moves at least six points. Choose a moved point $a$ and put $b=\sigma(a)$.

If $\sigma(b)\notin\{a,b\}$, choose
\[
c\notin\{a,b,\sigma(b)\}.
\]
If $\sigma(b)=a$, so that $(a\ b)$ is a $2$-cycle of $\sigma$, choose a moved point $c$ outside $\{a,b\}$; then $\sigma(c)\notin\{a,b,c\}$ after choosing $c$ in another cycle and, if necessary, replacing $c$ by its predecessor in that cycle.

Set
\[
\tau=(a\ b\ c)\in A_n
\]
and consider
\[
\rho=\tau\sigma\tau^{-1}\sigma^{-1}\in N.
\]
The inclusion $\rho\in N$ follows from normality. Moreover,
\[
\operatorname{supp}(\rho)
\subseteq \operatorname{supp}(\tau)\cup \sigma(\operatorname{supp}(\tau))
=\{a,b,c\}\cup\{b,\sigma(b),\sigma(c)\},
\]
so $\rho$ moves at most five points.

By our choice of $c$, the set $\{a,b,c\}$ is not preserved by $\sigma$. Hence $\sigma\tau\sigma^{-1}\ne\tau$, so $\rho\ne1$. Thus $N$ contains a nonidentity element moving at most five points, contradicting the minimality of $\sigma$. Therefore $|\operatorname{supp}(\sigma)|\le5$.
:::

<1>2. The subgroup $N$ contains a $3$-cycle.
::: {.proof}
A nonidentity even permutation cannot move exactly two points. If the minimal-support element $\sigma$ moves three points, then it is a $3$-cycle and we are done.

If $\sigma$ moves four points, then, being even and having no fixed point on its support, it is a product of two disjoint transpositions. After relabeling,
\[
\sigma=(1\ 2)(3\ 4).
\]
Since $n\ge5$, let $\tau=(1\ 2\ 5)$. Direct calculation gives
\[
\tau\sigma\tau^{-1}\sigma^{-1}=(1\ 5\ 2),
\]
a $3$-cycle in $N$.

If $\sigma$ moves five points, the only fixed-point-free even cycle type on five points is a $5$-cycle. After relabeling,
\[
\sigma=(1\ 2\ 3\ 4\ 5).
\]
Taking $\tau=(1\ 2\ 3)$ gives
\[
\tau\sigma\tau^{-1}\sigma^{-1}=(1\ 2\ 4),
\]
Again this is a $3$-cycle in $N$.

Thus in every case $N$ contains a $3$-cycle.
:::

<1>3. All $3$-cycles are conjugate in $A_n$ for $n\ge5$.
::: {.proof}
Any two $3$-cycles are conjugate in $S_n$. Let $\alpha$ and $\beta$ be $3$-cycles and choose $g\in S_n$ with $g\alpha g^{-1}=\beta$. If $g$ is even, there is nothing to prove. If $g$ is odd, choose two points outside the support of $\alpha$; this is possible because $n\ge5$. Let $t$ be the transposition of those two points. Then $t$ commutes with $\alpha$, and $gt$ is even. Hence
\[
(gt)\alpha(gt)^{-1}=g\alpha g^{-1}=\beta.
\]
So the conjugating element may be chosen in $A_n$.
:::

<1>4. The $3$-cycles generate $A_n$.
::: {.proof}
Every element of $A_n$ is a product of an even number of transpositions. Pair the transpositions. If two transpositions share a point, their product is a $3$-cycle (or the identity). If they are disjoint, then
\[
(a\ b)(c\ d)=(a\ c\ b)(a\ c\ d),
\]
a product of two $3$-cycles. Hence every even permutation is a product of $3$-cycles.
:::

<1>5. Therefore $N=A_n$, so $A_n$ is simple.
::: {.proof}
By <1>2, $N$ contains one $3$-cycle. Since $N$ is normal, <1>3 implies that it contains every $3$-cycle. By <1>4, those elements generate $A_n$. Hence $N=A_n$.

Thus the only normal subgroups of $A_n$ are $1$ and $A_n$ for every $n\ge5$.
:::
:::
