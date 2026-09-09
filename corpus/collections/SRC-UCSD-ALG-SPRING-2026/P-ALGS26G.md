---
schema: qual/card@1
id: P-ALGS26G
kind: problem
title: "Galois extension with symmetric group has a degree n irreducible polynomial"
classification:
  areas:
  - algebra
  topics:
  - Algebra
relations: []
review: draft
audit:
- event: source-checked
  by: OpenAI
  date: 2026-09-09
- event: solution-written
  by: OpenAI
  date: 2026-09-09
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-09
---

::: problem
Suppose that $K/F$ is a Galois extension of fields with $\operatorname{Gal}(K/F) \cong S_n$ for some $n \geq 2$.
Show that there is an irreducible polynomial $f(x) \in F[x]$ with $\deg f(x) = n$ such that $K$ is the splitting field of $f(x)$ over $F$.
:::

::: {.solution}
<1>1. Fix an isomorphism
\[
\iota:\operatorname{Gal}(K/F)\xrightarrow{\sim}S_n,
\]
and let \(H\le \operatorname{Gal}(K/F)\) be the inverse image under \(\iota\) of the stabilizer of \(1\in\{1,\dots,n\}\). Then \([\operatorname{Gal}(K/F):H]=n\).
::: {.proof}
The stabilizer of one point in the natural action of \(S_n\) is isomorphic to \(S_{n-1}\) and has index \(n\).
:::

<1>2. Let \(L=K^H\). Then \([L:F]=n\), and \(L/F\) is finite separable.
::: {.proof}
By the fundamental theorem of Galois theory,
\[
[L:F]=[\operatorname{Gal}(K/F):H]=n.
\]
Because \(K/F\) is Galois, it is separable, and every intermediate extension \(L/F\) is separable.
:::

<1>3. There exists \(\alpha\in L\) such that \(L=F(\alpha)\).
::: {.proof}
The extension \(L/F\) is finite separable by <1>2, so the primitive element theorem applies.
:::

<1>4. Let \(f(x)\in F[x]\) be the minimal polynomial of \(\alpha\) over \(F\). Then \(f\) is irreducible and \(\deg f=n\).
::: {.proof}
Minimal polynomials are irreducible, and
\[
\deg f=[F(\alpha):F]=[L:F]=n
\]
by <1>2 and <1>3.
:::

<1>5. The stabilizer of \(\alpha\) in \(G:=\operatorname{Gal}(K/F)\) is exactly \(H\).
::: {.proof}
An element \(\sigma\in G\) fixes \(\alpha\) if and only if it fixes every element of \(F(\alpha)=L\). By the Galois correspondence,
\[
\operatorname{Gal}(K/L)=H.
\]
Thus \(G_\alpha=H\).
:::

<1>6. The roots of \(f\) in \(K\) are precisely the distinct elements \(\sigma(\alpha)\) as \(\sigma\) ranges over representatives for the left cosets of \(H\) in \(G\). In particular, \(f\) splits completely in \(K\).
::: {.proof}
Since \(K/F\) is normal, every \(F\)-embedding of \(F(\alpha)\) into an algebraic closure extends to an element of \(G\). Hence the conjugates of \(\alpha\) over \(F\) are exactly its \(G\)-orbit.
By <1>5, orbit-stabilizer gives
\[
|G\cdot\alpha|=[G:H]=n=\deg f,
\]
so these are all roots of \(f\), and they are distinct because \(L/F\) is separable.
:::

<1>7. Let \(K_0\subseteq K\) be the splitting field of \(f\) over \(F\). Then
\[
\operatorname{Gal}(K/K_0)=\bigcap_{\sigma\in G}\sigma H\sigma^{-1}.
\]
::: {.proof}
The field \(K_0\) is generated over \(F\) by all conjugates \(\sigma(\alpha)\). An element \(g\in G\) fixes every \(\sigma(\alpha)\) if and only if
\[
\sigma^{-1}g\sigma(\alpha)=\alpha
\]
for every \(\sigma\in G\). By <1>5, this is equivalent to \(\sigma^{-1}g\sigma\in H\) for every \(\sigma\), i.e.
\[
g\in\bigcap_{\sigma\in G}\sigma H\sigma^{-1}.
\]
:::

<1>8. The core
\[
\bigcap_{\sigma\in G}\sigma H\sigma^{-1}
\]
is trivial.
::: {.proof}
Under \(\iota:G\cong S_n\), the conjugates of \(H\) are the stabilizers of the individual points \(1,\dots,n\). Their intersection consists of the permutations fixing every point, hence only the identity permutation.
Therefore the corresponding intersection in \(G\) is trivial.
:::

<1>9. Consequently \(K_0=K\). Thus \(K\) is the splitting field over \(F\) of the irreducible polynomial \(f\) of degree \(n\).
::: {.proof}
By <1>7 and <1>8,
\[
\operatorname{Gal}(K/K_0)=1.
\]
The Galois correspondence therefore gives \(K_0=K\). Combined with <1>4, this is exactly the required conclusion.
:::
:::
