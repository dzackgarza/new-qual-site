---
schema: qual/card@1
id: P-ALGCOMP03-04
kind: problem
title: Intermediate fields and Frobenius roots in finite fields
classification:
  areas:
  - algebra
  topics: []
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Enumerated the full D4 subgroup lattice and checked each fixed-field generator; verified Frobenius bijectivity and the explicit p-th root formula.
---

::: {.problem}
(a) Let $\alpha$ be the positive real fourth root of $2$ and let $i=\sqrt{-1}$.
Find all intermediate fields in the extension $\mathbb Q(\alpha,i)/\mathbb Q$.

(b) Let $K$ be a finite field with $p^n$ elements.
Show that every element of $K$ has a unique $p$th root in $K$.
:::


::: {.solution}
<1>1. Determine all intermediate fields of \(L=\mathbb Q(\alpha,i)\) over \(\mathbb Q\).
::: {.proof}
The polynomial \(x^4-2\) is irreducible over \(\mathbb Q\) by Eisenstein at \(2\), so
\[
[\mathbb Q(\alpha):\mathbb Q]=4.
\]
Since \(\mathbb Q(\alpha)\subset\mathbb R\), it does not contain \(i\). Hence
\[
[L:\mathbb Q]=8.
\]
The field \(L\) is the splitting field of \(x^4-2\), whose roots are
\[
\alpha,\ i\alpha,\ -\alpha,\ -i\alpha.
\]
Thus \(L/\mathbb Q\) is Galois of degree \(8\).

Define automorphisms
\[
\sigma(\alpha)=i\alpha,
\qquad
\sigma(i)=i,
\]
and
\[
\tau(\alpha)=\alpha,
\qquad
\tau(i)=-i.
\]
Then
\[
\sigma^4=\tau^2=1,
\qquad
\tau\sigma\tau=\sigma^{-1},
\]
so
\[
\operatorname{Gal}(L/\mathbb Q)\cong D_4.
\]

The subgroups of \(D_4\) are exactly
\[
D_4,\quad
\langle\sigma\rangle,\quad
\langle\sigma^2,\tau\rangle,\quad
\langle\sigma^2,\sigma\tau\rangle,
\]
\[
\langle\sigma^2\rangle,\quad
\langle\tau\rangle,\quad
\langle\sigma\tau\rangle,\quad
\langle\sigma^2\tau\rangle,\quad
\langle\sigma^3\tau\rangle,\quad
\{1\}.
\]
By Galois correspondence, these give all intermediate fields.

The three index-two subgroups give the three quadratic fields:
\[
L^{\langle\sigma\rangle}=\mathbb Q(i),
\]
\[
L^{\langle\sigma^2,\tau\rangle}=\mathbb Q(\alpha^2)=\mathbb Q(\sqrt2),
\]
\[
L^{\langle\sigma^2,\sigma\tau\rangle}
=\mathbb Q(i\alpha^2)=\mathbb Q(\sqrt{-2}).
\]

The five order-two subgroups give the five quartic fields:
\[
L^{\langle\sigma^2\rangle}=\mathbb Q(\alpha^2,i)=\mathbb Q(\sqrt2,i),
\]
\[
L^{\langle\tau\rangle}=\mathbb Q(\alpha),
\]
\[
L^{\langle\sigma^2\tau\rangle}=\mathbb Q(i\alpha),
\]
\[
L^{\langle\sigma\tau\rangle}=\mathbb Q((1+i)\alpha),
\]
\[
L^{\langle\sigma^3\tau\rangle}=\mathbb Q((1-i)\alpha).
\]
For example,
\[
(\sigma\tau)((1+i)\alpha)
=(1-i)(i\alpha)
=(1+i)\alpha,
\]
so \((1+i)\alpha\) is fixed by \(\langle\sigma\tau\rangle\); a direct check of its orbit shows that its stabilizer is exactly that order-two subgroup, hence the generated field has degree \(4\). The other displayed generators are checked similarly.

Together with the fixed fields of the whole group and the trivial subgroup, the complete list is therefore
\[
\boxed{
\begin{gathered}
\mathbb Q,\\
\mathbb Q(i),\quad \mathbb Q(\sqrt2),\quad \mathbb Q(\sqrt{-2}),\\
\mathbb Q(\alpha),\quad \mathbb Q(i\alpha),\quad
\mathbb Q(\sqrt2,i),\quad
\mathbb Q((1+i)\alpha),\quad
\mathbb Q((1-i)\alpha),\\
\mathbb Q(\alpha,i).
\end{gathered}}
\]
:::

<1>2. Every element of a finite field \(K\) of order \(p^n\) has a unique \(p\)-th root in \(K\).
::: {.proof}
Consider the Frobenius map
\[
F:K\longrightarrow K,
\qquad
F(x)=x^p.
\]
Because \(K\) has characteristic \(p\),
\[
(x+y)^p=x^p+y^p,
\]
so \(F\) is a field homomorphism. Its kernel is \(0\), hence \(F\) is injective. Since \(K\) is finite, every injective self-map of \(K\) is surjective. Therefore \(F\) is an automorphism.

Thus for every \(a\in K\) there is a unique \(b\in K\) such that
\[
b^p=a.
\]
In fact the root is explicitly
\[
\boxed{b=a^{p^{n-1}}},
\]
because every \(a\in K\) satisfies \(a^{p^n}=a\), and hence
\[
\left(a^{p^{n-1}}\right)^p=a^{p^n}=a.
\]
Uniqueness follows from injectivity of Frobenius.
:::
:::
