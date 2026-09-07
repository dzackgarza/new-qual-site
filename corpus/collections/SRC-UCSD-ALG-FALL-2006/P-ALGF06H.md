---
schema: qual/card@1
id: P-ALGF06H
kind: problem
title: "Splitting fields and Galois groups of polynomials over Q"
classification:
  areas:
  - algebra
  topics:
  - Galois Theory
  - Field Theory
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-07
  note: Checked against Question 4.1 of the official UCSD Algebra Qualifying Examination, Fall 2006; all four polynomials agree with the source.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-07
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-07
  note: Verified all splitting fields, intersection degrees, discriminants, extension degrees, and Galois-group structures, including the order-120 semidirect product for x^15-2.
---

::: {.problem}
Find the splitting fields and Galois groups of the following polynomials over $\mathbb{Q}$.
You should state clearly results that you use.

(a) $(x^2 + 3)(x^3 - 5)$

(b) $(x^2 - 3)(x^3 - 7)$

(c) $x^{15} - 2$

(d) $x^3 + 2x^2 + 1$
:::

::: {.solution}
We use the following standard facts.
A cubic over $\mathbb Q$ is reducible if and only if it has a rational root.
For an irreducible cubic, the Galois group of its splitting field is the transitive subgroup $A_3$ of $S_3$ when its discriminant is a square in $\mathbb Q$, and is $S_3$ otherwise.
Indeed, the square root of the discriminant is, up to sign, the product of the three pairwise differences of the roots, so it is fixed precisely by the even permutations.

<1>1. For
\[
f_a(x)=(x^2+3)(x^3-5),
\]
the splitting field is
\[
L_a=\mathbb Q(\sqrt[3]{5},\zeta_3)
=\mathbb Q(\sqrt[3]{5},\sqrt{-3}),
\]
and
\[
\operatorname{Gal}(L_a/\mathbb Q)\cong S_3.
\]
::: {.proof}
Let
\[
\alpha=\sqrt[3]{5}
\]
and let $\zeta_3$ be a primitive cube root of unity.
The roots of $x^3-5$ are
\[
\alpha,
\qquad
\zeta_3\alpha,
\qquad
\zeta_3^2\alpha,
\]
so its splitting field is $\mathbb Q(\alpha,\zeta_3)$.
Since
\[
\zeta_3=\frac{-1+\sqrt{-3}}2,
\]
this field already contains the two roots $\pm\sqrt{-3}$ of $x^2+3$.
Thus it is the splitting field of the product.

The polynomial $x^3-5$ is Eisenstein at $5$, hence
\[
[\mathbb Q(\alpha):\mathbb Q]=3.
\]
The field $\mathbb Q(\alpha)$ is contained in $\mathbb R$, whereas $\zeta_3\notin\mathbb R$, so $\zeta_3\notin\mathbb Q(\alpha)$.
Therefore
\[
[L_a:\mathbb Q]=6.
\]
The automorphisms
\[
\sigma:\alpha\mapsto\zeta_3\alpha,\quad \zeta_3\mapsto\zeta_3,
\]
and
\[
\tau:\alpha\mapsto\alpha,\quad \zeta_3\mapsto\zeta_3^{-1}
\]
satisfy
\[
\sigma^3=\tau^2=1,
\qquad
\tau\sigma\tau=\sigma^{-1}.
\]
They generate all six automorphisms, giving the standard presentation of $S_3$.
:::

<1>2. For
\[
f_b(x)=(x^2-3)(x^3-7),
\]
the splitting field is
\[
L_b=\mathbb Q(\sqrt[3]{7},\zeta_3,\sqrt3),
\]
and
\[
\operatorname{Gal}(L_b/\mathbb Q)\cong S_3\times C_2.
\]
::: {.proof}
Put
\[
\beta=\sqrt[3]{7},
\qquad
K=\mathbb Q(\beta,\zeta_3).
\]
Exactly as in <1>1, $K$ is the splitting field of $x^3-7$ and
\[
[K:\mathbb Q]=6,
\qquad
\operatorname{Gal}(K/\mathbb Q)\cong S_3.
\]
Its quadratic subfield is uniquely determined.
Indeed, quadratic subfields correspond to subgroups of index $2$ in $S_3$, and the unique index-$2$ subgroup is $A_3$.
Since
\[
\mathbb Q(\zeta_3)=\mathbb Q(\sqrt{-3})
\]
is already a quadratic subfield of $K$, it is the unique one.

Hence
\[
\sqrt3\notin K,
\]
because $\mathbb Q(\sqrt3)$ is a real quadratic field distinct from $\mathbb Q(\sqrt{-3})$.
Consequently
\[
K\cap\mathbb Q(\sqrt3)=\mathbb Q
\]
and
\[
[L_b:\mathbb Q]=[K:\mathbb Q]\,[\mathbb Q(\sqrt3):\mathbb Q]=12.
\]
Both $K/\mathbb Q$ and $\mathbb Q(\sqrt3)/\mathbb Q$ are Galois, and their intersection is $\mathbb Q$.
Restriction therefore gives an isomorphism
\[
\operatorname{Gal}(L_b/\mathbb Q)
\cong
\operatorname{Gal}(K/\mathbb Q)
\times
\operatorname{Gal}(\mathbb Q(\sqrt3)/\mathbb Q)
\cong S_3\times C_2.
\]
:::

<1>3. For
\[
f_c(x)=x^{15}-2,
\]
the splitting field is
\[
L_c=\mathbb Q(2^{1/15},\zeta_{15}),
\]
and
\[
\operatorname{Gal}(L_c/\mathbb Q)
\cong
C_{15}\rtimes (\mathbb Z/15\mathbb Z)^\times,
\]
where $(\mathbb Z/15\mathbb Z)^\times$ acts on $C_{15}$ by multiplication.
In particular,
\[
|\operatorname{Gal}(L_c/\mathbb Q)|=120.
\]
::: {.proof}
Let
\[
\alpha=2^{1/15}
\]
and let $\zeta=\zeta_{15}$ be a primitive fifteenth root of unity.
The fifteen roots are
\[
\zeta^a\alpha,
\qquad
a\in\mathbb Z/15\mathbb Z,
\]
so the splitting field is $L_c=\mathbb Q(\alpha,\zeta)$.

The polynomial $x^{15}-2$ is Eisenstein at $2$, hence
\[
[\mathbb Q(\alpha):\mathbb Q]=15.
\]
Also
\[
[\mathbb Q(\zeta):\mathbb Q]=\varphi(15)=8.
\]
If
\[
E=\mathbb Q(\alpha)\cap\mathbb Q(\zeta),
\]
then $[E:\mathbb Q]$ divides both $15$ and $8$, so
\[
[E:\mathbb Q]=1.
\]
Thus the two fields have trivial intersection and
\[
[L_c:\mathbb Q]=15\cdot8=120.
\]
Since $L_c$ is a splitting field in characteristic zero, it is Galois, so its Galois group also has order $120$.

Every automorphism is determined by
\[
\alpha\longmapsto\zeta^a\alpha,
\qquad
\zeta\longmapsto\zeta^b,
\]
where
\[
a\in\mathbb Z/15\mathbb Z,
\qquad
b\in(\mathbb Z/15\mathbb Z)^\times.
\]
There are exactly $15\cdot8=120$ such pairs, equal to the number of automorphisms, so every pair occurs.
Let $\sigma$ correspond to $(a,b)=(1,1)$, and for a unit $b$ let $\tau_b$ correspond to $(0,b)$.
Then
\[
\sigma^{15}=1,
\qquad
\tau_b\sigma\tau_b^{-1}=\sigma^b.
\]
Hence
\[
\operatorname{Gal}(L_c/\mathbb Q)
\cong
C_{15}\rtimes(\mathbb Z/15\mathbb Z)^\times.
\]
By the Chinese remainder theorem,
\[
(\mathbb Z/15\mathbb Z)^\times
\cong
(\mathbb Z/3\mathbb Z)^\times\times(\mathbb Z/5\mathbb Z)^\times
\cong C_2\times C_4.
\]
:::

<1>4. For
\[
f_d(x)=x^3+2x^2+1,
\]
if $\theta$ is any root, the splitting field is
\[
L_d=\mathbb Q(\theta,\sqrt{-59}),
\]
and
\[
\operatorname{Gal}(L_d/\mathbb Q)\cong S_3.
\]
::: {.proof}
The only possible rational roots are $\pm1$, and
\[
f_d(1)=4,
\qquad
f_d(-1)=2.
\]
Thus $f_d$ has no rational root and, being cubic, is irreducible over $\mathbb Q$.

For a monic cubic
\[
x^3+bx^2+cx+d,
\]
the discriminant is
\[
\Delta=b^2c^2-4c^3-4b^3d-27d^2+18bcd.
\]
Here $b=2$, $c=0$, and $d=1$, so
\[
\Delta=-4(2^3)-27=-32-27=-59.
\]
This is not a square in $\mathbb Q$.
Therefore the Galois group of the splitting field is the transitive subgroup $S_3$, rather than $A_3$, and the splitting field has degree $6$.

If the three roots are $r_1,r_2,r_3$, then
\[
\sqrt\Delta
=(r_1-r_2)(r_1-r_3)(r_2-r_3)
\]
up to sign, so $\sqrt{-59}$ belongs to the splitting field.
Since $\mathbb Q(\theta)$ has degree $3$, it cannot contain the quadratic field $\mathbb Q(\sqrt{-59})$.
Hence
\[
[\mathbb Q(\theta,\sqrt{-59}):\mathbb Q]=6.
\]
This degree-$6$ field lies inside the degree-$6$ splitting field, so they are equal.
:::
:::
