---
title: Fixed point theorems
order: 242
topics:
- Fixed Points
- Lefschetz Fixed Point Theorem
- Borsuk-Ulam Theorem
- Hairy Ball Theorem
- Antipodal Map
---

# Fixed point theorems

Brouwer's theorem, the Lefschetz fixed point theorem, the Borsuk--Ulam theorem and the hairy ball theorem; the degree arguments that relate them sit on the cards, and the propositions below record the reductions between them.

[[T-S2OLJ]]

[[T-BX4LD]]

::: {.remark}
Brouwer's theorem is also the case $X = D^n$ of the Lefschetz fixed point theorem: $D^n$ is contractible, so $H_0(D^n;\QQ) = \QQ$, all higher homology vanishes, and every self-map $f$ has Lefschetz number $\tau(f) = \tr\qty{f_*\colon H_0(D^n;\QQ)\to H_0(D^n;\QQ)} = 1 \neq 0$.
The implication $\tau(f)\neq 0\Rightarrow$ $f$ has a fixed point has no converse in general: $\tau(f)=0$ does not imply that $f$ is homotopic to a map without fixed points.

:::

## Borsuk--Ulam

[[T-WNOWY]]

::: {.example title="The case $n=1$"}
For continuous $f\colon S^1\to\RR$, set $g(x)\coloneqq f(x)-f(-x)$.
Then $g(-x)=-g(x)$, so $g$ takes values of both signs or vanishes, and the intermediate value theorem on a path from $x$ to $-x$ gives $x$ with $g(x)=0$, that is, $f(x)=f(-x)$.

:::

::: {.proposition title="Ham sandwich theorem"}
For Lebesgue measurable sets $A_1,\ldots,A_n\subseteq\RR^n$ of finite measure, there is an affine hyperplane $P$ such that each $A_i$ meets the two open half-spaces of $\RR^n\sm P$ in sets of equal measure.
This is [[T-WNOWY]] applied to $f=(f_1,\ldots,f_n)\colon S^n\to\RR^n$, where $f_i(u)$ is the measure of $A_i\intersect\theset{x \st \inner{u'}{x} > u_0}$ for $u=(u_0,u')\in S^n\subseteq\RR\times\RR^n$; a point with $f(u)=f(-u)$ gives the hyperplane $\inner{u'}{x}=u_0$, unless $u'=0$, in which case any hyperplane bisects the sets.

:::

## Hairy ball theorem

[[T-VQTR6]]

::: {.example}
Every odd-dimensional sphere $S^{2n+1}\subseteq\CC^{n+1}$ admits the nonvanishing tangent vector field $v(z)=iz$.

:::
