---
title: Fixed points and degree theory
order: 240
topics:
- Degree
- Fixed Points
- Fixed Point Theorems
- Fixed Point Theory
- Borsuk-Ulam Theorem
- Antipodal Map
- Lefschetz Fixed Point Theorem
- Invariance of Domain
---

# Fixed points and degree theory

[[D-XC53X]]

## The degree

::: {.proposition title="Properties of the degree"}
Let $n\geq 1$ and $f,g\colon S^n\to S^n$.

- A constant map has degree $0$.
- $\deg\id_{S^n} = 1$.
- $\deg (f\circ g) = \deg f \cdot \deg g$.
- If $f\homotopic g$, then $f_* = g_*$, so $\deg f = \deg g$. Conversely, by Hopf's theorem, maps of equal degree are homotopic.
- If $f$ is a homotopy equivalence with homotopy inverse $h$, then $\deg f\cdot\deg h = \deg\id = 1$, so $\deg f = \pm 1$.
- For $1\leq i\leq n+1$, the reflection $R_i\colon S^n\to S^n$, $(x_1, \ldots, x_i, \ldots, x_{n+1}) \mapsto (x_1, \ldots, - x_i, \ldots, x_{n+1})$, has degree $-1$.
- The antipodal map $x\mapsto -x$ on $S^n\subseteq \RR^{n+1}$ is the composite $R_1\circ\cdots\circ R_{n+1}$, so it has degree $(-1)^{n+1}$.
[@Hat02, §2.2, "Degree"]

:::

## Exercises

[[E-EYILL]]

[[E-ZXKDY]]

## Brouwer and Lefschetz

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
