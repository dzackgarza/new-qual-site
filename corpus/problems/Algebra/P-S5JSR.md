---
schema: qual/card@1
id: P-S5JSR
kind: problem
title: 'Galois theory exercises: splitting fields, intermediate extensions, finite
  fields'
classification:
  areas:
  - algebra
  topics:
  - Galois Theory
  - Splitting Fields
  - Field Extensions
relations: []
review: draft
---

::: {.problem}
1. Let $n\ge3$. For the splitting field of $x^n-2$ over $\QQ$, prove the affine embedding
\[
\Gal\hookrightarrow (\ZZ/n\ZZ)\rtimes(\ZZ/n\ZZ)^\times
\]
and prove that the Galois group is dihedral of order $2n$ exactly for $n=3,4,6$.

2. Compute all intermediate fields of $\QQ(\sqrt2,\sqrt3)$, prove
\[
\QQ(\sqrt2,\sqrt3)=\QQ(\sqrt2+\sqrt3),
\]
and find the minimal polynomial of $\sqrt2+\sqrt3$.

3. Compute all intermediate fields of $\QQ(2^{1/4},\zeta_8)$.

4. Show that $\QQ(2^{1/3})$ and $\QQ(\zeta_3 2^{1/3})$ are isomorphic fields but are not identical as subfields of $\CC$.

5. Let $L/K$ be a finite separable extension. Show that $L/K$ is normal if and only if $L$ is the splitting field over $K$ of some polynomial in $K[x]$.

6. Is $\QQ(2^{1/3})/\QQ$ normal?

7. Show that $\GF(p^n)$ is the splitting field of $x^{p^n}-x$ over $\FF_p$.

8. Show that
\[
\GF(p^d)\subseteq\GF(p^n)
\iff d\mid n.
\]

9. Compute the Galois group of $x^n-1$ over $\QQ$.

10. For an odd prime $p$, identify all elements of the Galois group of $x^p-2$ over $\QQ$.

11. Compute the Galois group of $x^{15}+2$ over $\QQ$ and identify its Sylow $2$-complement structure.

12. Show that the Galois group of $x^3+4x+2$ over $\QQ$ is $S_3$.
:::

::: {.solution}
<1>1. The polynomial $x^n-2$.
Let $\alpha=2^{1/n}$ and let $\zeta_n$ be primitive. The roots are $\zeta_n^j\alpha$, so the splitting field is
\[
L=\QQ(\alpha,\zeta_n).
\]
Every automorphism has the form
\[
\sigma(\alpha)=\zeta_n^a\alpha,
\qquad
\sigma(\zeta_n)=\zeta_n^b,
\]
with $a\in\ZZ/n\ZZ$ and $b\in(\ZZ/n\ZZ)^\times$, giving an injection into the affine group with law
\[
(a,b)(c,d)=(a+bc,bd).
\]

For $n=3,4,6$, the cyclotomic field has degree $2$ and intersects the real pure field $\QQ(\alpha)$ trivially, so $[L:\QQ]=2n$. The translation $\alpha\mapsto\zeta_n\alpha$ has order $n$, complex conjugation has order $2$, and conjugation inverts the translation. Hence the group is $D_{2n}$.

Conversely, if the group were $D_{2n}$, then its cyclotomic quotient $(\ZZ/n\ZZ)^\times$ would be an abelian quotient of a dihedral group, hence would have order at most $4$ and exponent at most $2$. This reduces to $n=3,4,5,6,8,10,12$. The cases $5,10$ are excluded because the unit group is $C_4$. The case $8$ has order $16$ but generators satisfying $srs=r^3$ rather than $r^{-1}$, and the case $12$ would force $\sqrt2\in\QQ(\zeta_{12})$, impossible. Thus exactly $n=3,4,6$ are dihedral.

<1>2. The biquadratic field.
Let
\[
L=\QQ(\sqrt2,\sqrt3).
\]
Then
\[
\Gal(L/\QQ)\cong C_2\times C_2,
\]
so the proper nontrivial intermediate fields are
\[
\QQ(\sqrt2),\qquad \QQ(\sqrt3),\qquad \QQ(\sqrt6).
\]
If $\alpha=\sqrt2+\sqrt3$, then
\[
\alpha^{-1}=\sqrt3-\sqrt2,
\]
so both $\sqrt2$ and $\sqrt3$ lie in $\QQ(\alpha)$. Hence $L=\QQ(\alpha)$. Moreover
\[
(\alpha^2-5)^2=24,
\]
so the minimal polynomial is
\[
\boxed{x^4-10x^2+1}.
\]

<1>3. The field $\QQ(2^{1/4},\zeta_8)$.
Put $\alpha=2^{1/4}$. Since $\zeta_8=(1+i)/\sqrt2$,
\[
L=\QQ(\alpha,i)
\]
is the splitting field of $x^4-2$, with Galois group $D_8$.
The three quadratic intermediate fields are
\[
\QQ(i),\qquad \QQ(\sqrt2),\qquad \QQ(\sqrt{-2}).
\]
The five quartic intermediate fields are
\[
\QQ(\zeta_8),\quad
\QQ(\alpha),\quad
\QQ(i\alpha),\quad
\QQ((1+i)\alpha),\quad
\QQ((1-i)\alpha).
\]
Together with $\QQ$ and $L$, these exhaust the subgroup lattice of $D_8$.

<1>4. Two isomorphic but unequal cubic fields.
Let
\[
\alpha=2^{1/3},\qquad \beta=\zeta_3\alpha.
\]
Both have irreducible minimal polynomial $x^3-2$, so
\[
\QQ(\alpha)\cong\QQ[x]/(x^3-2)\cong\QQ(\beta).
\]
But $\QQ(\alpha)\subset\RR$ while $\beta$ is nonreal, so the two subfields of $\CC$ are not equal.

<1>5. Finite separable normal extensions are exactly finite splitting fields.
If $L/K$ is finite, separable, and normal, choose generators
\[
L=K(\alpha_1,\ldots,\alpha_r).
\]
Let $m_i$ be the minimal polynomial of $\alpha_i$ over $K$. Normality implies each $m_i$ splits in $L$, so $L$ is the splitting field of
\[
f=\prod_i m_i.
\]
Conversely, a splitting field is normal, and separability of $L/K$ ensures the relevant irreducible factors are separable. Hence the equivalence.

<1>6. The real cubic field is not normal.
The minimal polynomial of $2^{1/3}$ is $x^3-2$, whose other roots are
\[
\zeta_3 2^{1/3},\qquad \zeta_3^2 2^{1/3}.
\]
They are nonreal, while $\QQ(2^{1/3})\subset\RR$. Thus the polynomial does not split there, so the extension is not normal.

<1>7. Finite fields as splitting fields.
The roots of
\[
x^{p^n}-x
\]
in an algebraic closure are exactly the elements fixed by the $n$th iterate of Frobenius. They form the unique field with $p^n$ elements, namely $\GF(p^n)$. Since the derivative is $-1$, the polynomial is squarefree, so $\GF(p^n)$ is its splitting field.

<1>8. Subfields of finite fields.
The extension
\[
\GF(p^n)/\FF_p
\]
is cyclic Galois of degree $n$, generated by Frobenius. Its subgroups are in bijection with divisors of $n$. Therefore
\[
\GF(p^d)\subseteq\GF(p^n)
\iff d\mid n.
\]

<1>9. Cyclotomic Galois groups.
The splitting field of $x^n-1$ is $\QQ(\zeta_n)$, and
\[
\Gal(\QQ(\zeta_n)/\QQ)
\cong
(\ZZ/n\ZZ)^\times
\]
via
\[
a\longmapsto(\zeta_n\mapsto\zeta_n^a).
\]

<1>10. The Galois group of $x^p-2$ for odd prime $p$.
Let $\alpha=2^{1/p}$. Since
\[
[\QQ(\alpha):\QQ]=p,
\qquad
[\QQ(\zeta_p):\QQ]=p-1,
\]
their intersection is $\QQ$. Hence the splitting field has degree
\[
p(p-1).
\]
Every affine pair occurs, so
\[
\Gal(x^p-2/\QQ)
\cong
C_p\rtimes(\ZZ/p\ZZ)^\times
\cong
C_p\rtimes C_{p-1}.
\]
Its elements are precisely
\[
\sigma_{a,b}(\alpha)=\zeta_p^a\alpha,
\qquad
\sigma_{a,b}(\zeta_p)=\zeta_p^b,
\]
for $a\in\ZZ/p\ZZ$ and $b\in(\ZZ/p\ZZ)^\times$.

<1>11. The Galois group of $x^{15}+2$.
If $\alpha=2^{1/15}$, then $-\alpha$ is a root of $x^{15}+2$, so the splitting field is
\[
L=\QQ(\alpha,\zeta_{15}).
\]
The pure field has degree $15$ and the cyclotomic field has degree $\varphi(15)=8$; these degrees are coprime, so the intersection is $\QQ$. Hence
\[
[L:\QQ]=120
\]
and every affine pair occurs:
\[
\Gal(L/\QQ)
\cong
C_{15}\rtimes(\ZZ/15\ZZ)^\times.
\]
Since
\[
(\ZZ/15\ZZ)^\times\cong C_4\times C_2,
\]
this unit group is a Sylow $2$-subgroup $S_2$, and in the repository's semidirect-product convention
\[
\boxed{\Gal(L/\QQ)\cong C_{15}\rtimes S_2}.
\]

<1>12. The cubic $x^3+4x+2$.
The polynomial has no rational root, so it is irreducible over $\QQ$. Its discriminant is
\[
\Delta=-4(4)^3-27(2)^2=-364,
\]
which is not a square in $\QQ$. An irreducible cubic has transitive Galois group, hence either $A_3$ or $S_3$, and it lies in $A_3$ exactly when the discriminant is a square. Therefore
\[
\Gal(x^3+4x+2/\QQ)\cong S_3.
\]
:::
