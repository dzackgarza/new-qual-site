---
schema: qual/card@1
id: D-IV2RAM
kind: definition
title: Ramification index, tame and wild ramification
classification:
  areas:
  - algebraic-geometry
  topics:
  - Ramification
  - Riemann-Hurwitz
  - Differentials
relations:
- kind: uses
  target: D-MORUNR
- kind: related-to
  target: T-LKT0U
review: draft
prompts:
- Define the ramification index of a morphism of curves at a point.
- What is the difference between tame and wild ramification?
- What is the length of $(\Omega_{X/Y})_p$, and how does it depend on that difference?
- Give a wildly ramified map and compute its ramification divisor.
- What is the ramification divisor of a morphism of smooth projective curves?
- What are the branch points and the branch locus?
---

::: {.definition title="Ramification index"}
Let $f : X \to Y$ be a finite morphism of curves, $p \in X$, $q = f(p)$, and $t$ a uniformizer of the discrete valuation ring $\OO_{Y,q}$.
The \dfn{ramification index} is
$$
e_p \definedas v_p(f^\sharp t) ,
$$
the valuation at $p$ of the pulled-back uniformizer.
$f$ is \dfn{ramified} at $p$ if $e_p > 1$ and \dfn{unramified} there if $e_p = 1$; the image $q$ of a ramification point is a \dfn{branch point}.
:::

::: {.definition title="Pullback of divisors"}
For $f : X \to Y$ a finite morphism of nonsingular curves, $f^* : \operatorname{Div} Y \to \operatorname{Div} X$ is the homomorphism with
$$
f^* q = \sum_{p \in f^{-1}(q)} e_p \, p .
$$
It preserves linear equivalence and satisfies $f^* \mcl(D) \cong \mcl(f^* D)$, so it induces $f^* : \Pic Y \to \Pic X$, and $\deg f^* D = \deg f \cdot \deg D$.
[@Har10a, §IV.2, Proposition II.6.9, Exercise II.6.8]
:::

::: {.definition title="Ramification divisor and branch locus"}
For $f \colon X \to Y$ a finite separable morphism of smooth projective curves, the \dfn{ramification divisor} is
$$
R = \sum_{p \in X} \length (\Omega_{X/Y})_p \cdot p ,
$$
which is $\sum_p (e_p - 1)\, p$ when all ramification is tame.
The \dfn{branch locus} is the finite set $f(\supp R)$ of branch points, and the \dfn{branch divisor} is the pushforward $f_* R = \sum_p \length(\Omega_{X/Y})_p \cdot f(p)$.
:::

::: {.definition title="Tame and wild"}
Let $\characteristic k = p_0$.
The ramification at $p$ is \dfn{tame} if $p_0 \nmid e_p$, and \dfn{wild} if $p_0 \mid e_p$.
In characteristic $0$ all ramification is tame.
:::

::: {.proposition title="The length formula"}
For $f$ finite separable, $\Omega_{X/Y}$ is a torsion sheaf supported exactly on the ramification locus, its stalks are principal $\OO_p$-modules, and
$$
\length (\Omega_{X/Y})_p
\begin{cases}
= e_p - 1 & \text{at a tamely ramified } p, \\
> e_p - 1 & \text{at a wildly ramified } p .
\end{cases}
$$
:::

::: {.remark title="Where the dichotomy comes from"}
The stalk length is computed by one derivative.
With $u$ a uniformizer at $p$ and $t$ one at $q$, write $f^\sharp t = c u^{e_p}(1 + \cdots)$; then
$$
f^* dt = \left( e_p \, c \, u^{e_p - 1} + \cdots \right) du ,
$$
and $\length(\Omega_{X/Y})_p$ is the valuation of that coefficient.
If $p_0 \nmid e_p$ the leading term survives and the valuation is $e_p - 1$.
If $p_0 \mid e_p$ the leading term is killed, the valuation is determined by whatever comes next, and it is strictly larger.
So the ramification at $p$ is tame if and only if $e_p$ is invertible in $k$.

The map $u \mapsto t=u^n$ with $p_0 \nmid n$ is tamely ramified at $u=0$, where $R$ has coefficient $n-1$.
For a wild example take $\characteristic k = p_0$ and $f : \PP^1 \to \PP^1$ with $t = u^{p_0} - u$, which is separable since $dt = -du$.
It is unramified on the affine line and totally ramified at infinity with $e = p_0$, which is wild, and the local computation there gives length $2p_0 - 2 > p_0 - 1$.
Riemann--Hurwitz confirms it: $-2 = p_0 \cdot (-2) + \deg R$ forces $\deg R = 2p_0 - 2$, carried by that one point.
:::

::: {.remark title="Ramification and Riemann--Hurwitz"}
Riemann--Hurwitz ([[T-LKT0U]]) holds with $\deg R = \sum_p \length (\Omega_{X/Y})_p$, which equals $\sum_p (e_p - 1)$ when all ramification is tame.
At a wildly ramified point the local length exceeds $e_p-1$, so $\deg R>\sum_p(e_p-1)$.
For the Artin--Schreier map $u\mapsto u^{p_0}-u$ of degree $p_0$, the tame formula would give $\deg R=p_0-1$ at its single ramification point, while Riemann--Hurwitz requires $\deg R=2p_0-2$.

The condition $e_p = 1$ at every $p$ is unramifiedness in the sense of [[D-MORUNR]]; a nonconstant morphism of smooth curves is flat, so it is étale if and only if $e_p=1$ at every $p$.
:::
