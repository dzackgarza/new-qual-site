---
schema: qual/card@1
id: P-HCAX10
kind: problem
title: A compact-uniform limit of univalent functions can be constant
classification:
  areas:
  - complex-analysis
  topics:
  - Univalent Functions
relations: []
review: draft
---

::: problem
Give a sequence of holomorphic injective functions which converges uniformly on compact sets to a non-injective function.
Show that this example describes the only possible failure of injectivity in such a limit.
:::

::: solution
On any domain $\Omega\subseteq\mathbb C$, the functions
\[
f_n(z)=\frac{z}{n}
\]
are holomorphic and injective, while $f_n\to 0$ uniformly on compact subsets. Thus a constant function can occur as a non-injective limit.

We show that this is the only possibility. Suppose $f_n:\Omega\to\mathbb C$ are holomorphic and injective, $f_n\to f$ uniformly on compact subsets, and $f$ is not constant. If $f$ were not injective, there would be distinct points $a,b\in\Omega$ with $f(a)=f(b)$.

Set
\[
g_n(z)=f_n(z)-f_n(b),\qquad g(z)=f(z)-f(b).
\]
Then $g_n\to g$ uniformly on compact subsets. The function $g$ is not identically zero because $f$ is nonconstant, and $g(a)=0$. Choose a closed disk $\overline{D(a,r)}\subset\Omega$ that does not contain $b$ and whose boundary contains no zero of $g$. By Hurwitz's theorem, for all sufficiently large $n$, the function $g_n$ has a zero $a_n$ in $D(a,r)$. Hence
\[
f_n(a_n)=f_n(b).
\]
Since $a_n\ne b$, this contradicts injectivity of $f_n$.

Therefore every nonconstant compact-uniform limit of holomorphic injective functions is injective. The only possible loss of injectivity is that the limit becomes constant.
:::
