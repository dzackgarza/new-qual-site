---
order: 50
---

# Series: Reference

:::{.fact title="Convenient notation"}
Define $\rising{n}{k}$ to be the **rising factorial**
\[
\rising{n}{k} = n(n+1)(n+2) \cdots (n+(k-1)) = k! {n+k-1\choose k}
,\]
which has exactly $k$ terms.
Some useful identities:
\[
\rising{n}{k} &= {(n+k-1)! \over (k-1)!} = {\Gamma(n+k) \over \Gamma(n)} \\
{\rising{n}{k} \over k!} &= {n+k-1 \choose k}
.\]

Similarly define the **falling factorial**
\[
\falling{n}{k} = n(n-1)(n-2)\cdots(n-(k-1)) = k!{n\choose k}
,\]
which again has $k$ terms.
\[
\falling{n}{k} &= {n! \over (n-k)!} = {\Gamma(n+1) \over \Gamma(n - (k-1))}\\
{\falling{n}{k} \over k!} &= {n\choose k}
.\]

Where this comes up most often:
\[
\qty{\dd{}{z}}^k z^n = \falling{n}{k} \, z^{n-k}
.\]

:::

:::{.fact title="Generalized Binomial Theorem"}
Extend the binomial coefficients to negative numbers in the following way:
\[
{-n \choose k} &\da (-n)(-(n+1))\cdots (-(n + (k-1))) \cdot {1\over k!} = (-1)^k {n+k-1 \choose k}
.\]
Then
\[
(x+y)^n = \sum_{k\geq 0} {n\choose k} x^{k}y^{n-k}
.\]

:::

:::{.fact title="List of useful series"}
\[
\sum_{k=1}^{n} k 
  &=\frac{n(n+1)}{2} \\
\sum_{k=1}^{n} k^{2} 
  &=\frac{n(n+1)(2 n+1)}{6} \\
\sum_{k=1}^{n} k^{3} 
  &=\frac{n^{2}(n+1)^{2}}{4}  \\
\sum_{0\leq k \leq N} z^k 
  &= {1 - z^{N+1} \over 1-z} \\
{1\over 1-z} &= \sum_{k\geq 0} z^k \\
e^z &= \sum_{k\geq 0} {z^k \over k!} \\
\sin(z) 
  &= \sum_{\substack{ k \geq 1 \\ \text{odd} }} (-1)^{k+1 \over 2} {z^k \over k!} \\
  &= z - {1\over 3!}z^3 + {1\over 5!}z^5 + \cdots \\ \\
\cos(z) 
  &= \sum_{\substack{ k \geq 0 \\ \text{even}} } (-1)^{k\over 2} {z^k \over k!} \\
  &= 1 - {1\over 2!}z^2 + {1\over 4!}z^4 + \cdots \\ \\
\cosh(z) &= \sum_{k\geq 0} { z^{2k} \over (2k)! } \\
&= 1 + {1\over 2!}z^2 + {1\over 4!}z^4 + \cdots \\ \\
\sinh(z) &= \sum_{k\geq 0} { z^{2k+1} \over (2k+1)! } \\
&= z + {1\over 3!}z^3 + {1\over 5!}z^5 + \cdots \\ \\
\log(1-z) 
  &= -1\cdot \sum_{k \geq 1} {z^k\over k} \quad \abs{z} < 1 \\ \\
\qty{\dd{}{z}}^k \sum_{n=0}^\infty c_n z^n 
  &= \sum_{n=k}^\infty (n)_k \, c_n z^{n-k} \\
  &= \sum_{n=k}^\infty n(n-1)\cdots(n-k+1) c_n z^{n-k} \\
(1+z)^{1/2} 
  &= \sum_{k\geq 0} {1/2 \choose k}z^k,\qquad \abs{z} < 1 \\
  &= 1 + (1/2)z + {(1/2)(-1/2) \over 2!}z^2 + {(1/2)(-1/2)(-3/2) \over 3!}z^3 + \cdots \\
  &= 1 + {1\over 2}z - {1\over 8}z^2 + {1\over 16}z^3 - \cdots \\
(1+z)^{\alpha} 
  &= \sum_{k\geq 0} {\alpha \choose k}z^k,\qquad \abs{z} < 1 \\
{1\over 1+z^n} 
  &= \sum_{k\geq 0} {n+k-1 \choose k} (-z)^k, \qquad \abs{z} < 1
\]

Some other classes of series to remember:
\[
\sum_{k=1}^{n} k
&= \frac{n(n+1)}{2} \\
\sum_{k=1}^{n} k(k+1)
&= \frac{n(n+1)(n+2)}{3} \\
\sum_{k=1}^{n} k(k+1)(k+2)
&= \frac{n(n+1)(n+2)(n+3)}{4} \\
\vdots \quad & \vdots \\
\sum_{k=1}^{n} k^{(p)} 
&= \frac{n^{(p+1)}}{p+1} && k^{(p)}\da k(k+1)(k+2) \cdots (k+p-1)
.\]
How to remember: compare to the integral
\[
\int_{x=0}^{x=n} x^p \dx = { n^{p+1} \over p+1}
.\]

Remembering that $\sum_{1\leq k \leq n} k = n(n+1)/2$: realize as counting a triangle, flip to count an entire rectangle of size $n\times (n+1)$ and take half:

![](figures/2021-12-11_22-15-41.png)

Write $k^2 = k(k+1) - k$ to get
\[
\sum k^2 = \sum k(k+1) - \sum k = {n(n+1/2)(n+2/2) \over 3}
.\]
Similarly $\sum k^3 = (\sum k )^2$.

For summing the odds, $\sum_{k\geq 1} (2k-1)$:

![](figures/2021-12-11_22-09-24.png)

For denominators: 
\[
\sum_{k=1}^{n} \frac{1}{k(k+1)}=\frac{1}{1}-\frac{1}{n+1} \\
\sum_{k=1}^{n} \frac{2}{k(k+1)(k+2)}=\frac{1}{1 \cdot 2}-\frac{1}{(n+1)(n+2)} \\
\sum_{k=1}^{n} \frac{p}{k^{(p+1)}}=\frac{1}{1^{(p)}}-\frac{1}{(n+1)^{(p)}}
,\]
where $1^{(p)} \da p!$.
How to remember the last one:
\[
\int_{x=1}^{x=n+1}{p\over x^{p+1}}\dx = {1\over 1^p} - {1\over (n+1)^p}
.\]

:::

:::{.fact title="Expanding square roots"}
\[
\sqrt{z} 
&= \sqrt{z_0 + z - z_0} \\
&= \sqrt{z_0 \qty{ 1 + {z-z_0 \over z} }} \\
&= \sqrt{z_0} \sqrt{1+u},\quad u\da {z-z_0 \over z} \\
\implies 
\sqrt{z} 
&= \sqrt{z_0} \sum_{k\geq 0} {1/2 \choose k} \qty{z- z_0 \over z}^k
.\]

:::

:::{.fact title="Multiplying series: Cauchy product"}
The product of two sequences is given by the Cauchy product
\[
\sum a_kz^k \cdot \sum b_k z^k = \sum c_k z^k,\quad c_k \da \sum_{j\leq k} a_k b_{k-j}
.\]

:::

# Inverting Series

## Cauchy product formula for coefficients of $1/A(z)$

:::{.fact title="Multiplicatively inverting a series"}
Using the general ring theory fact that $A(z) \da \sum_{k\geq 0} a_k z^k \in R[[z]]$ is invertible iff $a_0$ is invertible in $R$, power series over fields can always be inverted.
There is a formula: writing $B(z) \da \sum_{k\geq 0 } b_k z^k \da 1/A(z) \in \CC[[z]]$, the coefficients can be inductively computed as
\[
b_0 &= a_0\inv \\
b_n &= -a_0\inv \sum_{1\leq i \leq n} a_i b_{n-i} \\
&= -a_0\inv \sum_{0\leq i \leq n-1} a_{n-i}b_i \\
&= -{1\over a_0}\qty{a_nb_0 + a_{n-1}b_1 + \cdots + a_1 b_{n-1} }
.\]

:::

:::{.proof title="Sketch"}
How to prove this:
\[
\qty{\sum a_k z^k}\qty{\sum b_k z^k} = 1
\implies 
a_0b_0 &=1 \\
a_0b_1 + a_1b_0 &= 1 \\
a_0b_2 + a_1b_1 + a_2b_0 &= 1 \\
\vdots \quad&\quad \vdots
\]

:::

[[P-VFAXW]]
[[P-IM6MH]]
[[P-OCOSY]]
[[P-VT4TV]]

## Geometric Series

:::{.fact title="Using geometric series to invert power series"}
Supposing $A(z) \da 1 + a_1 z + a_2z^2 + \cdots$, a direct expansion gives
\[
{1\over A(z)} 
&= {1\over 1 + \displaystyle\sum_{k\geq 1} a_k z^k }\\
&= 
1 - \qty{\sum_{k\geq 1} a_k z^k}
\  + \qty{\sum_{k\geq 1} a_k z^k}^2
\  - \qty{\sum_{k\geq 1} a_k z^k}^3
\  + \cdots \\
&= 1 - (A(z) - 1) + (A(z) - 1)^2 - (A(z) - 1)^3 + \cdots
,\]
where to compute the $z^m$ term you only need to consider the first $m+1$ summands in this expansion.

Purely formally, we have
\[
{1\over A(z)} = {1 \over 1- (1-A(z))} = \sum_{k\geq 0} (1-A(z))^k z^k
.\]

:::

:::{.warnings}
In order to invert $A$ using this method, you need to clear powers of $z$ so that a leading term is constant.

:::

[[P-VO5YR]]
[[P-NBSTW]]

## Polynomial Long Division

:::{.example title="Inverting by polynomial long division"}
With practice, it's much quicker to just do polynomial long division:
\[
{1\over \sin(z) } = z\inv\qty{z\over \sin(z)}
.\]

Now just run the grade school algorithm:
\[
  \begin{array}{rl}
    \underline{\hspace{8em} 1 + {1\over 3!}z^2 + \left({1\over 3!3!} - {1\over 5!} \right)z^4 + \cdots } &  \\[-5pt]
     z-{1\over 3!}z^3 + {1\over 5!}z^5 + \cdots\hspace{3em} |z\hspace{9em}  \\
      \underline{-(z-{1\over 3!}z^3 + {1\over 5!}z^5 + \cdots)} & \\
      {1\over 3!}z^3 - {1\over 5!}z^5 + {1\over 7!}z^7 - \cdots \hspace{0em}& \\
     \underline{-{1\over 3!}z^2(z-{1\over 3!}z^3 + {1\over 5!}z^5 + \cdots)} & \\
      \left( -{1\over 5!} + {1\over 3!3!}\right)z^5 + \left( {1\over 7!} - {1\over 3! 5!} \right)z + \cdots & \\
  \end{array}
.\]

Conclusion:
\[
{z\over \sin(z)} 
= 1 + {z^2\over 3!} + {7 z^4 \over 360 } + \bigo(z^6) \\
\implies {1 \over \sin(z)} 
= {1\over z}  + {z\over 3!} + {7 z^3 \over 360 } + \bigo(z^5)
.\]

:::

:::{.fact title="Dividing using polynomial long division"}
Polynomial long division basically works for formal power series, and with practice it's fast enough to just do in your head.
Recall the Euclidean algorithm, e.g. for ${z^3+1 \over z+1}$:
\[
z^3 + 1 &= (z+1)(z^2) + (-z^2 + 1) \\
\ -z^2 + 1 &= (z+1)(-z) + (z+1) \\
(z+1) &= (z+1)(1) + 0 \\
\implies
{z^3 + 1\over z+1} &= z^2 - z + 1
.\]
This goes by *increasing* powers, but one can also go by *decreasing* powers:
\[
1+z^3 &= (1+z)(1) + (-z+z^3) \\
\ -z+z^3 &= (1+z)(-z) + (z^2 + z^3) \\
z^2 +z^3 &= (1+z)(z^2) + 0 \\
\implies
{z^3 + 1\over z+1}&= 1 - z + z^2
,\]
which is useful for generating the first few low order terms of a series expansion.

:::

[[P-KUNLD]]

