---
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

For $n\geq 1$ and a continuous map $f\colon S^n\to S^n$, the [[D-XC53X|degree]] $\deg f\in\ZZ$ is defined by
$$
f_*[S^n]=\deg(f)\,[S^n]\in H_n(S^n;\ZZ).
$$

## The degree

::: {.fact title="Properties of the degree"}
Let $n\geq 1$ and $f,g\colon S^n\to S^n$.

- A constant map has degree $0$.
- $\deg\id_{S^n} = 1$.
- $\deg (f\circ g) = \deg f \cdot \deg g$.
- If $f\homotopic g$, then $f_* = g_*$, so $\deg f = \deg g$. Conversely, by Hopf's theorem, maps of equal degree are homotopic.
- If $f$ is a homotopy equivalence with homotopy inverse $h$, then $\deg f\cdot\deg h = \deg\id = 1$, so $\deg f = \pm 1$.
- For $1\leq i\leq n+1$, the reflection $R_i\colon S^n\to S^n$, $(x_1, \ldots, x_i, \ldots, x_{n+1}) \mapsto (x_1, \ldots, - x_i, \ldots, x_{n+1})$, has degree $-1$.
- The antipodal map $x\mapsto -x$ on $S^n\subseteq \RR^{n+1}$ is the composite $R_1\circ\cdots\circ R_{n+1}$, so it has degree $(-1)^{n+1}$.
  In particular, a map of even degree is not homotopic to the antipodal map.

:::

## Exercises

[[E-EYILL]]

[[E-ZXKDY]]

## Brouwer and Lefschetz

[[T-S2OLJ]]

::: {.proof title="Brouwer's theorem via retractions"}
Let $n\geq 1$ and suppose $f\colon D^n \to D^n$ has no fixed point.
For $x\in D^n$, let $g(x)$ be the point where the ray from $f(x)$ through $x$ meets $\del D^n = S^{n-1}$.
Then $g\colon D^n\to S^{n-1}$ is continuous, and $g(x)=x$ for $x\in S^{n-1}$, so with $\iota\colon S^{n-1}\injects D^n$ the inclusion, $g\circ\iota = \id_{S^{n-1}}$.
On reduced homology in degree $n-1$ this gives $\id = g_*\circ\iota_*$, which factors through $\tilde H_{n-1}(D^n) = 0$.
This contradicts $\tilde H_{n-1}(S^{n-1})\cong\ZZ$.

:::

[[T-BX4LD]]

::: {.remark}
Brouwer's theorem is also the case $X = D^n$ of the Lefschetz fixed point theorem: $D^n$ is contractible, so $H_0(D^n;\QQ) = \QQ$, all higher homology vanishes, and every self-map $f$ has Lefschetz number $\Lambda_f = \operatorname{Tr}(f_* \mid H_0) = 1 \neq 0$.
The implication $\Lambda_f\neq 0\Rightarrow$ $f$ has a fixed point has no converse in general: $\Lambda_f=0$ does not imply that $f$ is homotopic to a map without fixed points.

:::

## Borsuk--Ulam

[[T-WNOWY]]

::: {.example title="The case $n=1$"}
For continuous $f\colon S^1\to\RR$, set $g(x)\coloneqq f(x)-f(-x)$.
Then $g(-x)=-g(x)$, so $g$ takes values of both signs or vanishes, and the intermediate value theorem on a path from $x$ to $-x$ gives $x$ with $g(x)=0$, that is, $f(x)=f(-x)$.

:::

::: {.proposition title="Ham sandwich theorem"}
For Lebesgue measurable sets $A_1,\ldots,A_n\subseteq\RR^n$ of finite measure, there is an affine hyperplane $P$ such that each $A_i$ meets the two open half-spaces of $\RR^n\sm P$ in sets of equal measure.

:::

::: {.proof}
For $u=(u_0,u')\in S^n\subseteq\RR\times\RR^n$, let $f_i(u)$ be the measure of $A_i\cap\ts{x \st \inner{u'}{x} > u_0}$, which is continuous in $u$.
By the Borsuk--Ulam theorem applied to $f=(f_1,\ldots,f_n)\colon S^n\to\RR^n$, there is $u$ with $f(u)=f(-u)$.
If $u'=0$, then one of the two sets is empty and the other is $\RR^n$, so $f(u)=f(-u)$ forces every $A_i$ to have measure $0$ and any hyperplane works.
Otherwise $P\coloneqq\ts{\inner{u'}{x}=u_0}$ is a hyperplane of measure zero, and $f(u)=f(-u)$ says that $P$ bisects each $A_i$.

:::

## Hairy ball theorem

[[T-VQTR6]]

::: {.proof}
Suppose $S^k\subseteq\RR^{k+1}$ admits a nonvanishing continuous tangent vector field $v$, so $x \cdot v(x) = 0$ for all $x\in S^k$.
Define $H\colon S^k \times [0, 1] \to \RR^{k+1}$ by
$$
H(x, t) \coloneqq x \cos(\pi t) + \frac{v(x)}{\norm{v(x)}} \sin(\pi t).
$$
Since $x \perp v(x)$, $\norm{H(x, t)}^2 = \cos^2(\pi t) + \sin^2(\pi t) = 1$, so $H$ is a homotopy in $S^k$ from $H(\wait,0)=\id_{S^k}$ to $H(\wait,1)=-\id_{S^k}$.
By homotopy invariance, $1=\deg(\id_{S^k}) = \deg(-\id_{S^k}) = (-1)^{k+1}$, so $k$ is odd.

:::

::: {.example}
Every odd-dimensional sphere $S^{2n+1}\subseteq\CC^{n+1}$ admits the nonvanishing tangent vector field $v(z)=iz$.
The spheres $S^0$, $S^1$, $S^3$, and $S^7$ are parallelizable.

:::
