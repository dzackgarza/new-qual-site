---
schema: qual/card@1
id: E-KWLRQ
kind: exercise
title: "Suppose $f$ is entire and there exist $A, R >0$ and natural number $N$\u2026"
classification:
  areas:
  - complex-analysis
  topics:
  - entire-functions
  - polynomials
  - liouville-s-theorem
  - cauchy-estimates
relations: []
review: draft
solved: true
---
:::{.problem title="?"}
Suppose $f$ is entire and there exist $A, R >0$ and natural number $N$ such that 
\[
|f(z)| \geq A |z|^N\ \text{for}\ |z| \geq R
.\]

Show that 

- $f$ is a polynomial and 
- the degree of $f$ is at least $N$.
:::

:::{.solution}
The easier version of this question: when $\abs{f} \leq A\abs{z}^N$, $f$ is a polynomial of degree *at most* $N$ by Cauchy's integral formula:
\[
\abs{f^{(n)}(z)} 
&= \abs{ {1\over 2\pi i} \oint_\gamma {f(\xi) \over (\xi - z)^{n+1}} \dxi } \\
&\leq  {1\over 2\pi i} \oint_\gamma { \abs{ f(\xi) } \over \abs{\xi - z}^{n+1}} \dxi \\
&\leq {1\over 2\pi i } \oint_\gamma {AR^N \over R^{n+1} } \dxi \\
&= {A\over 2\pi i} R^{N-(n+1)} \cdot 2\pi R \\
&= AR^{N-n} \\
&\convergesto{R\to\infty} 0 \qquad \iff N-n<0 \iff n>N
.\]

Now rearrange the given equality 
\[
\abs{f(z) \over z^N} \geq A \qquad \abs{z} \implies \abs{z^N\over f(z)} \leq A\inv
.\]
A priori, $f$ is equal to its power series at $z=0$, so $f(z) = \sum_{k\geq 0} c_k z^k$.
Since $\DD_R$ is compact, $f$ has finitely many zeros in this region, say $\ts{z_k}_{k\leq m}$.
This set must be finite, since an infinite subset of a compact set has a limit point, and being zero on a set with a limit point implies being identically zero by the identity principle.

Define 
\[
p(z) \da \prod_{1\leq k\leq m} (z-z_k) = z^m + \bigo(z^{m-1})
,\]
the product of these roots.
Increase $R$ if necessary to ensure that
\[
\abs{p(z)\over z^m} < 1 \implies
\abs{p(z)} < \abs{z}^m
.\]
Now define
\[
G(z) \da {p(z) z^N \over f(z)} \implies \abs{G(z)} = \abs{p(z) z^N\over f(z)} 
= \abs{z^N\over f(z)}\cdot \abs{p(z)} \leq A\inv \abs{z}^m 
.\]

> Issue: this might not be entire? There could be poles at the zeros of $f$ outside of $\DD_R$...

By the previous result, $G$ is a polynomial of degree at most $m$.
Now consider leading terms: on one hand,
\[
f(z) G(z) = p(z) z^N \sim \qty{z^m + \cdots }\cdot z^N = z^{N+m} + \cdots
.\]
On the other hand,
\[
f(z) G(z) 
&= f(z) \qty{z^m + \cdots} \\
&\sim \sum_{k\geq 0} c_k z^{k+m} + z^{m-1}f(z) + \cdots \\
&= (z^m + \cdots + c_{N}z^{N+m} + \cdots) + z^{m-1}f(z) + \cdots
,\]
and by the previous expression, this must be a polynomial of degree at most $N+m$.
This forces $c_k = 0$ for all $k> N$, otherwise these would contribute higher order terms.

> Note: maybe not quite right! 

Alternatively, note that the inequality can be rewritten as
\[
\abs{G(z)} \leq A\inv \abs{z}^m \implies \abs{p(z)\over f(z)} \leq A\inv \abs{z}^{m-N}
.\]

- If $m-N = 0$, then $p/f$ is an entire bounded function and thus constant, making $p(z) = \lambda f(z)$ and $f$ is a polynomial of degree exactly $N$.
-If $m-N>0$, then $p/f$ is a polynomial of degree at most $m-N$ by the previous result.
  But $p/f$ is a polynomial with no zeros, since $Z_p = Z_f$, and the only nonvanishing polynomial is a constant, so again $p = \lambda f$.
- If $m-N<0$, then use the inequality
\[
\abs{z^{N-m}p(z) \over f(z)} \leq A\inv
,\]
so the LHS is an entire bounded function and thus constant, so $z^{N-m}p(z) = \lambda f(z)$.
But the LHS is evidently a polynomial of degree $(N-m)+m = m$.
:::

:::{.solution title="Older"}
Note that the analogue of this problem where $\abs{f(z)} \leq A \abs{z}^N$ implies $f$ is a polynomial of degree at *most* $N$ is easy by the Cauchy estimate:
\[
\abs{f(z)} =\abs{\sum_{k\geq 0} c_k z^k } \implies 
\abs{c_n} = \abs{f^{(n)}(0)} 
&= \abs{{n!\over 2\pi i }\int_\gamma {f(\xi) \over (\xi-a)^{n+1} } \dxi } \quad \text{ at } a=0\\
&\leq {n!\over 2\pi }\int_\gamma {\abs{f(\xi)} \over \abs{\xi}^{n+1} } \dxi \\
&\leq {n!\over 2\pi }\int_\gamma {A {\abs{\xi}^N } \over \abs{\xi}^{n+1} } \dxi \\
&= {A n!\over 2\pi }\int_\gamma {{R ^N } \over R^{n+1} } \dxi \\
&= {An!\over 2\pi} \cdot {2\pi R \over R^{n+1-N}} \\
&= {An! \over R^{n-N}} \\
&\convergesto{R\to\infty} 0 \quad \iff n-N>0 \quad\iff n>N
,\]
so $f(z) = \sum_{0\leq k\leq N} c_k z^k$.

For the case at hand, a solution I liked from MSE:

- Write $g(z) \da f(1/z)$, so $g$ has a singularity at $z=0$.
  The claim is that this is a pole.

- It can't be removable: 
\[
\abs{g(z)} \geq A \abs{1\over z}^n \to\infty
\quad \text{ for }
\abs{1/z} \geq R \,\, (\iff \abs{z} < 1/R)
,\]
so $g$ is unbounded near $z=0$.
- It can't be essential: if so, take the neighborhood of $z=0$ given by $U\da D_{1\over R}(0)\smz = \ts{z\st 0< \abs{z} < {1\over R} }$.
Then $g(U) \subseteq \CC$ would be dense by Casorati-Weierstrass, but note that $g(z) = w\in g(U) \implies \abs{w} \da \abs{g(z)} \geq A\abs{1/z}^n$ since $\abs{z}<1/R$, so $g(U) \subseteq (\CC\sm D_{A\over R^n}(0))$ and in particular does not intersect the interior of $D_{A\over R^n}(0)$.

- Since $z=0$ is a pole, it has some finite order $m$, so write
\[
g(z) = \qty{c_{-m}z^{-m} + \cdots + c_{-1}z\inv} + \qty{c_0 + c_1 z + \cdots} \da p(1/z) + h(z)
,\]
where $p$ is polynomial of degree exactly $m$ (since $c_{-m} \neq 0$) and $h$ is entire.
In particular, $z=0$ is not a singularity of $h$.

- Now
\[
g(z) = p(1/z) + h(z) \implies f(z) = p(z) + h(1/z)
.\]

- Then
\[
f(z) - p(z) = h(1/z) \convergesto{\abs z\to \infty} c_0 \da h(0)
,\]
since holomorphic functions are continuous.

- Then $h$ is an entire function with a finite limit $L$ at $\infty$.
$h$ is bounded by $c_0$ in a neighborhood $U_\infty$ of $\infty$ and takes on a maximum on $U_\infty^c$ by compactness and the maximum modulus principle.
So $h$ is bounded on all of $\CC$, and thus constant by Liouville, and thus $h(1/z) = L$ for all $z$.

- So 
\[
f(z) &= p(z) + h(1/z) = p(z) + c_0 \\
\implies f(z) &= (c_{-1}z + \cdots + c_{-m}z^m) + c_0
,\]
which is a polynomial of degree exactly $m\da \deg p$.
- Why $m \geq N$: if not, $m<N$ so $N-m > 0$.
Then for large $z$,
\[
A \leq \abs{f(z) \over z^N} 
&= \abs{c_0 + c_{-1}z + \cdots + c_{-m}z^m \over z^N}\\
&= \abs{ {c_0 \over z^N} + {c_{-1} \over z^{N-1}} + \cdots + {c_{-m} \over z^{N-m}} } \\
&\convergesto{\abs{z}\to\infty} 0
,\]
since every term has a factor of $z$ in the denominator.
This contradicts $A>0$. $\contradiction$
:::
