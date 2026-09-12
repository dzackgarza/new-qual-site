---
schema: qual/card@1
id: P-CASP09F
kind: problem
title: "Statement and proof of the Weierstrass Product Theorem"
classification:
  areas:
  - complex-analysis
  topics:
  - Complex Analysis
relations: []
review: draft
---

::: problem
State and prove the Weierstrass Product Theorem.
You may use any general convergence criteria without proof, but you should state what these criteria are.
:::

::: solution
For $p\ge0$ define the primary factor
\[
E_p(w)=(1-w)\exp\left(w+\frac{w^2}{2}+\cdots+\frac{w^p}{p}\right),
\]
with $E_0(w)=1-w$.

**Weierstrass product theorem.** Let $(a_n)$ be a sequence of nonzero complex
numbers with no finite accumulation point. Then there are integers $p_n\ge0$
such that
\[
P(z)=\prod_{n=1}^\infty E_{p_n}(z/a_n)
\]
converges uniformly on compact subsets of $\mathbb C$ to an entire function
whose zeros, with multiplicity, are exactly the $a_n$. If $0$ is also to be a
zero of multiplicity $m$, multiply by $z^m$.

Moreover, every nonzero entire function $f$ with zeros $0$ of multiplicity
$m$ and nonzero zeros $(a_n)$, repeated according to multiplicity, has a
representation
\[
\boxed{
f(z)=z^m e^{g(z)}
\prod_{n=1}^\infty E_{p_n}(z/a_n)}
\]
for some entire function $g$ and suitable $p_n$.

To prove convergence, note that for $|w|\le1/2$,
\[
\log E_p(w)
=-\sum_{k=p+1}^\infty\frac{w^k}{k},
\]
so
\[
|\log E_p(w)|\le C|w|^{p+1}
\]
with an absolute constant $C$. Since $|a_n|\to\infty$, choose $p_n$ so large
that for every integer $R\ge1$ the tail satisfies
\[
\sum_{|a_n|>2R}\left(\frac{R}{|a_n|}\right)^{p_n+1}<\infty.
\]
Then on $|z|\le R$ the corresponding series of logarithms converges uniformly,
hence the product converges uniformly there. As $R$ is arbitrary, the product
converges locally uniformly on $\mathbb C$ and is entire.

On a compact set avoiding all $a_n$, the tail product is nonzero because the
series of logarithms converges. Hence the only zeros are the prescribed zeros,
with the multiplicities contributed by their factors.

Finally let $f$ be an arbitrary entire function with those zeros and let $P$
be the product just constructed. Then
\[
h(z)=\frac{f(z)}{z^mP(z)}
\]
is entire and nowhere zero. Since $\mathbb C$ is simply connected, $h$ has an
entire logarithm: there is entire $g$ with $h=e^g$. This gives the displayed
factorization and completes the proof.
:::
