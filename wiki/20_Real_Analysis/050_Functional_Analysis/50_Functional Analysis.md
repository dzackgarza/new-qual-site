---
title: Functional Analysis 
order: 50
---

title: Basics

# Functional Analysis

## $L^p$ Spaces

:::{.remark}
For any measure space $(X, M, \mu)$, one can define $L^2(\mu)$ with the inner product $\inner{f}{g} \da \int_X f\bar{g} d\mu$.

:::

[[PR-L35O7]]

[[PR-WS6NT]]

## General Facts

:::{.remark}
Working with inner products:
\[
\inner{tx + sy}{z} &= t\inner{x}{z} + s\inner{y}{z} \\
\inner{x}{y} &= \bar{\inner{y}{x}} \\
x\neq 0 \implies \inner{x}{x} > 0
.\]
We define $\norm{x} \da \sqrt{\inner{x}{x}}$.

:::

:::{.fact title="Cauchy-Schwarz"}
For $x, y\in H$,
\[
\abs{ \inner{x}{y}} \leq \norm{x} \norm{y}
,\]
with equality iff $x, y$ are linearly independent.

:::

:::{.fact title="Pythagoras"}
\[
\inner{v}{w} = 0 \implies \norm{v+w}^2 = \norm{v}^2 + \norm{w}^2
.\]
More generally, if $x_i \perp x_j$ for all $i\neq j$, then
\[
\norm{\sum_k x_k }_H^2 = \sum_k \norm{x_k}_H^2
.\]

:::

:::{.fact title="Polarization"}
For all $x, y\in H$,
\[
4 \inner{x}{y} = \norm{x+y}^2 - \norm{x-y}^2 +i\qty{\norm{x+iy}^2 - \norm{x-iy}^2}
.\]

:::

:::{.fact title="Parallelogram law"}
For all $x, y\in H$, 
\[
\norm{x+y}^2 + \norm{x-y}^2 = 2\qty{\norm{x}^2 + \norm{y}^2 }
.\]

:::

[[PR-KTZZ5]]

## Fourier Coefficients

[[T-4BDE3]]

[[T-4CDKK]]

:::{.proof title="of Bessel's inequality"}
\envlist

- Let $S_{N} = \sum_{n=1}^N \inner{x}{u_{n}} u_{n}$
\[
\norm{x - S_{N}}^2 
&= \inner{x - S_{n}}{x - S_{N}} \\
&= \norm{x}^2 + \norm{S_{N}}^2 - 2\Re\inner{x}{S_{N}} \\
&= \norm{x}^2 + \norm{S_{N}}^2 - 2\Re \inner{x}{\sum_{n=1}^N \inner{x}{u_{n}}u_{n}} \\
&= \norm{x}^2 + \norm{S_{N}}^2 - 2\Re \sum_{n=1}^N \inner{x}{ \inner{x}{u_{n}}u_{n}} \\
&= \norm{x}^2 + \norm{S_{N}}^2 - 2\Re \sum_{n=1}^N \overline{\inner{x}{u_{n}}}\inner{x}{u_{n}} \\
&= \norm{x}^2 + \left\|\sum_{n=1}^N \inner{x}{u_{n}} u_{n}\right\|^2 - 2 \sum_{n=1}^N \abs{\inner{x}{u_{n}}}^2 \\
&= \norm{x}^2 + \sum_{n=1}^N \abs{\inner{x}{u_{n}}}^2 - 2 \sum_{n=1}^N \abs{\inner{x}{u_{n}}}^2 \\
&= \norm{x}^2 - \sum_{n=1}^N \abs{\inner{x}{u_{n}}}^2
.\]

- By continuity of the norm and inner product, we have
\[
\lim_{N\to\infty} \norm{x - S_{N}}^2 
&= \lim_{N\to\infty} \norm{x}^2 - \sum_{n=1}^N \abs{\inner{x}{u_{n}}}^2 \\
\implies \norm{x - \lim_{N\to\infty} S_{N}}^2 &= \norm{x}^2 - \lim_{N\to\infty}\sum_{n=1}^N \abs{\inner{x}{u_{n}}}^2\\
\implies 
\norm{x - \sum_{n=1}^\infty \inner{x}{u_{n}} u_{n}}^2 &= \norm{x}^2 - 
\sum_{n=1}^\infty \abs{\inner{x}{u_{n}}}^2
.\]

- Then noting that $0 \leq \norm{x - S_{N}}^2$, 
\[
0 &\leq 
\norm{x}^2 - 
\sum_{n=1}^\infty \abs{\inner{x}{u_{n}}}^2 \\
\implies 
\sum_{n=1}^\infty \abs{\inner{x}{u_{n}}}^2 &\leq 
\norm{x}^2 \qed
.\]


:::

[[T-5AALA]]


[[T-LDCZB]]

:::{.proof title="?"}
\envlist

- Define $M \da \ker \Lambda$.
- Then $M$ is a closed subspace and so $H = M \oplus M^\perp$
- There is some $z\in M^\perp$ such that $\norm{z} = 1$.
- Set $u \da \Lambda(x) z - \Lambda(z) x$
- Check 

$$\Lambda(u) = \Lambda(\Lambda(x) z - \Lambda(z) x) = \Lambda(x) \Lambda(z) - \Lambda(z) \Lambda(x) = 0 \implies u\in M$$

- Compute

\[
0 &= \inner{u}{z} \\ 
&= \inner{\Lambda(x) z - \Lambda(z) x}{z} \\
&= \inner{\Lambda(x) z}{z} - \inner{\Lambda(z) x}{z} \\
&= \Lambda(x) \inner{z}{z} - \Lambda(z) \inner{x}{z} \\
&= \Lambda(x) \norm{z}^2 - \Lambda(z) \inner{x}{z} \\
&= \Lambda(x) - \Lambda(z) \inner{x}{z} \\
&= \Lambda(x) -  \inner{x}{\overline{\Lambda(z)} z}
,\]

- Choose $y \da \overline{\Lambda(z)} z$.
- Check uniqueness:

\[
\inner{x}{y} &= \inner{x}{y'} \quad\forall x \\
\implies  \inner{x}{y-y'} &= 0 \quad\forall x \\
\implies \inner{y-y'}{y-y'} &= 0 \\
\implies \norm{y-y'} &= 0 \\
\implies y-y' &= \vector 0 \implies y = y'
.\]


:::

[[T-J3AN3]]

:::{.proof title="?"}
\envlist

- Given $\theset{a_{n}}$, define $S_{N} = \sum^N a_{n} \vector u_{n}$.
- $S_{N}$ is Cauchy in $\mathcal{H}$ and so $S_{N} \to \vector x$ for some $\vector x \in \mathcal{H}$.
- $\inner{x}{u_{n}} = \inner{x - S_{N}}{u_{n}} + \inner{S_{N}}{u_{n}} \to a_{n}$
- By construction, $\norm{x-S_{N}}^2 = \norm{x}^2 - \sum^N \abs{a_{n}}^2 \to 0$, so $\norm{x}^2 = \sum^\infty \abs{a_{n}}^2$.

:::

## Operator Norms

[[T-5IWCG]]

:::{.proof title="?"}
$2 \implies 3$:
Choose $\delta < 1$ such that 
$$
\norm{x} \leq \delta \implies \abs{L(x)} < 1.
$$
Then
\[
\abs{L(x)} 
&= \abs{L\left( \frac{\norm x}{\delta} \frac{\delta }{\norm x} x \right)} \\
&= \frac{\norm x}{\delta} ~\abs{L\left( \delta \frac{x }{\norm x} \right)} \\
&\leq \frac{\norm x}{\delta} 1
,\]
so we can take $c = \frac 1 \delta$. $\qed$

$3 \implies 1$:

We have $\abs{L(x-y)} \leq c\norm{x-y}$, so given $\varepsilon \geq 0$ simply choose $\delta = \frac \varepsilon c$.

:::

[[T-QBTWN]]

:::{.proof title="?"}
The only nontrivial property is the triangle inequality, but
\[
\pnorm{L_{1} + L_{2}}{\op} = \sup \abs{L_{1}(x) + L_{2}(x)} \leq \sup \abs{L_{1}(x)} + \abs{\sup L_{2}(x)} = \pnorm{L_{1}}\op + \pnorm{L_{2}}\op
.\]

:::

[[T-W5SDY]]

:::{.proof title="?"}
\envlist

- Let $\theset{L_{n}}$ be Cauchy in $X\dual$.

- Then for all $x\in C$, $\theset{L_{n}(x)} \subset \CC$ is Cauchy and converges to something denoted $L(x)$.

- Need to show $L$ is continuous and $\norm{L_{n} - L} \to 0$.

- Since $\theset{L_{n}}$ is Cauchy in $X\dual$, choose $N$ large enough so that
\[
n, m \geq N \implies \norm{L_{n} - L_{m}} < \varepsilon \implies \abs{L_{m}(x) - L_{n}(x)} < \varepsilon \quad \forall x \suchthat \norm{x} = 1
.\]

- Take $n\to \infty$ to obtain
\[m \geq N 
&\implies \abs{L_{m}(x) - L(x)} < \varepsilon \quad \forall x \suchthat \norm{x} = 1\\
&\implies \norm{L_{m} - L} < \varepsilon \to 0
.\]

- Continuity:
\[
\abs{L(x)} &= \abs{L(x) - L_{n}(x) + L_{n}(x)} \\
&\leq  \abs{L(x) - L_{n}(x)} + \abs{L_{n}(x)} \\
&\leq \varepsilon \norm{x} + c\norm{x} \\
&= (\varepsilon + c)\norm{x} \qed
.\]

:::

## Misc

:::{.remark}
Big theorems for Banach spaces:

- Uniform boundedness principle
- Open mapping theorem
- Closed graph theorem

:::
