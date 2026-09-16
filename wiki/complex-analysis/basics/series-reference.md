---
order: 50
title: Series reference
---

# Series reference

## Factorial notation

::: {.definition title="Rising and falling factorials"}
For $n\in\CC$ and $k\in\ZZ_{\geq 0}$, the \dfn{rising factorial} is
$$
\rising{n}{k} \coloneqq n(n+1)(n+2) \cdots (n+k-1),
$$
and the \dfn{falling factorial} is
$$
\falling{n}{k} \coloneqq n(n-1)(n-2)\cdots(n-k+1);
$$
each is a product of $k$ factors, and the empty product for $k=0$ is $1$.

:::

::: {.fact}
For $n\in\ZZ_{>0}$,
$$
\rising{n}{k} = {(n+k-1)! \over (n-1)!} = {\Gamma(n+k) \over \Gamma(n)} = k!{n+k-1 \choose k}.
$$
For $n\in\ZZ_{\geq 0}$ and $0\leq k\leq n$,
$$
\falling{n}{k} = {n! \over (n-k)!} = {\Gamma(n+1) \over \Gamma(n-k+1)} = k!{n\choose k}.
$$
For $n\in\ZZ_{\geq 0}$, $\qty{\frac{d}{dz}}^k z^n = \falling{n}{k} \, z^{n-k}$.

:::

## Standard series

::: {.fact title="Generalized binomial theorem"}
For $\alpha\in\CC$ and $k\geq 0$, set
$$
{\alpha\choose k} \coloneqq {\alpha(\alpha-1)\cdots(\alpha-k+1)\over k!} = \frac{\falling{\alpha}{k}}{k!}.
$$
Then, for $\abs z<1$ and the holomorphic branch of $(1+z)^\alpha$ with value $1$ at $z=0$,
$$
(1+z)^\alpha = \sum_{k\geq 0}{\alpha\choose k}z^k.
$$
When $\alpha\in\ZZ_{\geq 0}$ the series terminates and is the binomial theorem.

:::

::: {.fact title="Power series"}
For $z\in\CC$ unless a radius is stated,
$$
\begin{aligned}
\sum_{k=0}^{N} z^k &= {1 - z^{N+1} \over 1-z} \quad (z\neq 1), \\
{1\over 1-z} &= \sum_{k\geq 0} z^k, \qquad \abs z<1, \\
{1\over 1+z^n} &= \sum_{k\geq 0} (-1)^kz^{nk}, \qquad \abs{z} < 1,\ n\geq 1, \\
e^z &= \sum_{k\geq 0} {z^k \over k!}, \\
\sin(z) &= \sum_{k \geq 0} (-1)^{k} {z^{2k+1} \over (2k+1)!} = z - {1\over 3!}z^3 + {1\over 5!}z^5 - \cdots, \\
\cos(z) &= \sum_{k \geq 0} (-1)^{k} {z^{2k} \over (2k)!} = 1 - {1\over 2!}z^2 + {1\over 4!}z^4 - \cdots, \\
\cosh(z) &= \sum_{k\geq 0} { z^{2k} \over (2k)! } = 1 + {1\over 2!}z^2 + {1\over 4!}z^4 + \cdots, \\
\sinh(z) &= \sum_{k\geq 0} { z^{2k+1} \over (2k+1)! } = z + {1\over 3!}z^3 + {1\over 5!}z^5 + \cdots, \\
\log(1-z) &= - \sum_{k \geq 1} {z^k\over k}, \qquad \abs{z} < 1, \\
(1+z)^{1/2} &= \sum_{k\geq 0} {1/2 \choose k}z^k = 1 + {1\over 2}z - {1\over 8}z^2 + {1\over 16}z^3 - \cdots, \qquad \abs{z} < 1.
\end{aligned}
$$
Within the disc of convergence,
$$
\qty{\frac{d}{dz}}^k \sum_{n\geq 0} c_n z^n = \sum_{n\geq k} \falling{n}{k} \, c_n z^{n-k}.
$$

:::

[[FF-LF5ND]] [[FF-XKATS]]

[[FF-ENSFJ]] [[FF-5GLOZ]]

::: {.fact title="Expanding square roots"}
Fix $z_0\neq 0$ and a branch $\sqrt{\phantom z}$ on the disc $\abs{z-z_0}<\abs{z_0}$, and let $\sqrt{z_0}$ denote its value at $z_0$.
On that disc, with $u\coloneqq (z-z_0)/z_0$,
$$
\sqrt{z} = \sqrt{z_0} \sqrt{1+u} = \sqrt{z_0} \sum_{k\geq 0} {1/2 \choose k} \qty{z- z_0 \over z_0}^k,
$$
where $\sqrt{1+u}$ is the branch with value $1$ at $u=0$.

:::

## Finite sums

::: {.fact title="Sums of powers"}
$$
\begin{aligned}
\sum_{k=1}^{n} k &=\frac{n(n+1)}{2}, \\
\sum_{k=1}^{n} k^{2} &=\frac{n(n+1)(2 n+1)}{6}, \\
\sum_{k=1}^{n} k^{3} &=\frac{n^{2}(n+1)^{2}}{4} = \qty{\sum_{k=1}^n k}^2, \\
\sum_{k=1}^{n}(2k-1) &= n^2.
\end{aligned}
$$

![](figures/2021-12-11_22-09-24.png)

:::

::: {.fact title="Sums of rising factorials"}
For $p\geq 1$, with $k^{(p)}\coloneqq k(k+1) \cdots (k+p-1)$,
$$
\begin{aligned}
\sum_{k=1}^{n} k^{(p)} &= \frac{n^{(p+1)}}{p+1}, \\
\sum_{k=1}^{n} \frac{p}{k^{(p+1)}} &= \frac{1}{1^{(p)}}-\frac{1}{(n+1)^{(p)}}, \qquad 1^{(p)} = p!.
\end{aligned}
$$
For $p=1,2$ these read $\sum_{k=1}^{n} k(k+1) = \frac{n(n+1)(n+2)}{3}$, $\sum_{k=1}^{n} k(k+1)(k+2) = \frac{n(n+1)(n+2)(n+3)}{4}$, $\sum_{k=1}^{n} \frac{1}{k(k+1)}=1-\frac{1}{n+1}$, and $\sum_{k=1}^{n} \frac{2}{k(k+1)(k+2)}=\frac{1}{2}-\frac{1}{(n+1)(n+2)}$.

:::

::: {.remark}
The two identities are discrete analogues of $\int_0^n x^p \dx = { n^{p+1} \over p+1}$ and $\int_1^{n+1}{p\over x^{p+1}}\dx = 1 - {1\over (n+1)^p}$.
Writing $k^2 = k(k+1) - k$ gives $\sum_{k=1}^n k^2 = \frac{n(n+1)(n+2)}{3} - \frac{n(n+1)}{2} = {n(n+1)(2n+1) \over 6}$.
The identity $\sum_{k=1}^n k = n(n+1)/2$ counts a staircase of $n$ columns as half of an $n\times(n+1)$ rectangle:

![](figures/2021-12-11_22-15-41.png)

:::

## Inverting power series

::: {.fact title="Cauchy product"}
Where both series converge absolutely,
$$
\sum_{k\geq 0} a_kz^k \cdot \sum_{k\geq 0} b_k z^k = \sum_{k\geq 0} c_k z^k,\qquad c_k \coloneqq \sum_{j=0}^k a_j b_{k-j}.
$$

:::

::: {.proposition title="Coefficients of $1/A(z)$"}
For a commutative ring $R$, $A(z) \coloneqq \sum_{k\geq 0} a_k z^k \in R[[z]]$ is invertible if and only if $a_0$ is a unit in $R$; over a field, if and only if $a_0\neq 0$.
In that case the coefficients of $B(z) \coloneqq \sum_{k\geq 0 } b_k z^k \coloneqq 1/A(z)$ are determined recursively by
$$
\begin{aligned}
b_0 &= a_0\inv, \\
b_n &= -a_0\inv \sum_{1\leq i \leq n} a_i b_{n-i} = -{1\over a_0}\qty{a_nb_0 + a_{n-1}b_1 + \cdots + a_1 b_{n-1} }, \qquad n\geq 1.
\end{aligned}
$$

:::

::: {.proof}
Comparing coefficients of $z^n$ in $A(z)B(z) = 1$ gives
$$
a_0b_0 =1, \qquad \sum_{i=0}^n a_ib_{n-i} = 0 \quad (n\geq 1),
$$
and solving the $n$th equation for $b_n$ gives the recursion.
Conversely, if $a_0$ is a unit, the recursion defines $B$ with $AB = 1$; if $AB=1$, then $a_0b_0 = 1$.

:::

[[FF-JKLWM]]

[[P-VFAXW]]
[[P-IM6MH]]
[[P-OCOSY]]
[[P-VT4TV]]

::: {.fact title="Inverting with the geometric series"}
For $A(z) \coloneqq 1 + a_1 z + a_2z^2 + \cdots$,
$$
{1\over A(z)} = {1 \over 1- (1-A(z))} = \sum_{k\geq 0} (1-A(z))^k = 1 - (A(z) - 1) + (A(z) - 1)^2 - (A(z) - 1)^3 + \cdots
$$
as formal power series.
Since $(A(z)-1)^k$ has no terms of degree below $k$, the coefficient of $z^m$ in $1/A(z)$ is determined by the summands with $k\leq m$.

:::

::: {.remark}
If $A(z) = z^m \tilde A(z)$ with $\tilde A(0) \neq 0$, then $1/A(z) = z^{-m}/\tilde A(z)$, and $1/\tilde A(z)$ is computed by either method after dividing by $\tilde A(0)$.

:::

[[FF-UQZNR]]

[[P-VO5YR]]
[[P-NBSTW]]

## Long division of power series

::: {.fact title="Long division"}
Polynomial long division applies to formal power series.
Dividing by leading terms of highest degree gives the quotient of polynomials, as for $\frac{z^3+1}{z+1}$:
$$
\begin{aligned}
z^3 + 1 &= (z+1)(z^2) + (-z^2 + 1), \\
-z^2 + 1 &= (z+1)(-z) + (z+1), \\
z+1 &= (z+1)(1) + 0,
\end{aligned}
$$
so $\frac{z^3 + 1}{z+1} = z^2 - z + 1$.
Dividing by terms of lowest degree produces the quotient in increasing powers of $z$, which gives the low-order terms of a power series quotient:
$$
\begin{aligned}
1+z^3 &= (1+z)(1) + (-z+z^3), \\
-z+z^3 &= (1+z)(-z) + (z^2 + z^3), \\
z^2 +z^3 &= (1+z)(z^2) + 0,
\end{aligned}
$$
so $\frac{1+z^3}{1+z} = 1 - z + z^2$.

:::

::: {.example title="The Laurent series of $1/\sin(z)$"}
Write $\frac{1}{\sin(z)} = z\inv\qty{\frac{z}{\sin(z)}}$ and divide $z$ by $\sin(z) = z-\frac{1}{3!}z^3 + \frac{1}{5!}z^5 - \cdots$ in increasing powers:
$$
  \begin{array}{rl}
    \underline{\hspace{8em} 1 + {1\over 3!}z^2 + \left({1\over 3!3!} - {1\over 5!} \right)z^4 + \cdots } &  \\[-5pt]
     z-{1\over 3!}z^3 + {1\over 5!}z^5 + \cdots\hspace{3em} |z\hspace{9em}  \\
      \underline{-(z-{1\over 3!}z^3 + {1\over 5!}z^5 + \cdots)} & \\
      {1\over 3!}z^3 - {1\over 5!}z^5 + {1\over 7!}z^7 - \cdots \hspace{0em}& \\
     \underline{-{1\over 3!}z^2(z-{1\over 3!}z^3 + {1\over 5!}z^5 + \cdots)} & \\
      \left( -{1\over 5!} + {1\over 3!3!}\right)z^5 + \left( {1\over 7!} - {1\over 3! 5!} \right)z^7 + \cdots & \\
  \end{array}
$$
So
$$
\begin{aligned}
{z\over \sin(z)} &= 1 + {z^2\over 3!} + {7 z^4 \over 360 } + \bigo(z^6), \\
{1 \over \sin(z)} &= {1\over z}  + {z\over 3!} + {7 z^3 \over 360 } + \bigo(z^5).
\end{aligned}
$$

:::

[[P-KUNLD]]
