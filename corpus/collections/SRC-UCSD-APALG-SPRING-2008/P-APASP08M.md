---
schema: qual/card@1
id: P-APASP08M
kind: problem
title: "Construction of a matrix group via Young representation, invariant ring, and Hilbert series"
classification:
  areas:
  - applied-algebra
  topics:
  - Commutative Algebra
  - Representation Theory
  - Gröbner Bases
relations: []
review: draft
audit:
- event: solution-written
  by: OpenAI
  date: 2026-09-10
---

::: problem
Construct the group $G$ of $3 \times 3$ matrices by applying the Young natural representation indexed by $[2,1,1]$ to the permutations of $S_4$.

(1) Compute the Hilbert series $F_{\mathbb{R}[x_1,x_2,x_3]^G}(q)$ of the ring of $G$-invariants.

(2) Rewrite it in the form $$F_{\mathbb{R}[x]}(q) = \frac{1 + q^d}{(1 - q^{d_1})(1 - q^{d_2})(1 - q^{d_3})}.$$

(3) Calculate the first 10 terms of this series.

(4) Construct three homogeneous $G$-invariants of degrees $d_1, d_2, d_3$.

(5) Compute the Gröbner basis of the ideal $(I_1, I_2, I_3)$.

(6) Verify that $I_1, I_2, I_3$ are a system of parameters by checking that the quotient $\mathbb{Q}[x_1, x_2, x_3]/(I_1, I_2, I_3)$ has finite dimension.
If not, go back to step (4).

(7) Construct a $G$-invariant $\eta$ of degree $d$.

(9) Verify that it is not a polynomial in $I_1, I_2, I_3$ by computing the polynomial $Q$ such that $Q(\eta, I_1, I_2, I_3) = 0$.

(10) Based on your previous results, show that step (9) is not needed.

(11) Compute the Jacobian of $I_1, I_2, I_3$ and construct its linear factors.

(12) Assuming that there is a reflection group $G'$ that also leaves $I_1, I_2, I_3$ invariant, you could have predicted the number of these linear factors.
Why?
:::

::: solution
The irreducible $S_4$-representation indexed by $(2,1,1)$ is the sign twist of the standard representation indexed by $(3,1)$. A convenient equivalent matrix model is the orientation-preserving signed permutation group
\[
G=
\left\{
DP_\sigma:
D=\operatorname{diag}(\varepsilon_1,\varepsilon_2,\varepsilon_3),\quad
\varepsilon_i\in\{\pm1\},\quad
\sigma\in S_3,\quad
\det(DP_\sigma)=1
\right\}.
\]
There are $3!\cdot 2^2=24$ such matrices. This group acts faithfully on the four body-diagonal lines of a cube, hence is isomorphic to $S_4$. Its natural three-dimensional representation is irreducible: the diagonal Klein four subgroup has the three coordinate axes as its distinct simultaneous eigenspaces, while a $3$-cycle permutation matrix permutes those axes transitively. Since every matrix in $G$ has determinant $1$, this is the $(2,1,1)$ representation rather than the standard $(3,1)$ representation, whose determinant is the sign character.

Let $G'$ be the full signed permutation group in three variables. Then $G$ is the index-two subgroup
\[
G=\ker(\det:G'\to\{\pm1\}).
\]
The $G'$-invariant ring is
\[
\mathbb R[x_1,x_2,x_3]^{G'}
=
\mathbb R[I_1,I_2,I_3],
\]
where
\[
I_1=x_1^2+x_2^2+x_3^2,
\]
\[
I_2=x_1^2x_2^2+x_1^2x_3^2+x_2^2x_3^2,
\]
and
\[
I_3=x_1^2x_2^2x_3^2.
\]
Their degrees are
\[
d_1=2,
\qquad d_2=4,
\qquad d_3=6.
\]

Define the $G'$-anti-invariant
\[
\eta
=
x_1x_2x_3
(x_1^2-x_2^2)(x_1^2-x_3^2)(x_2^2-x_3^2).
\]
It has degree
\[
d=3+2+2+2=9.
\]
Every reflection in $G'$ changes the sign of $\eta$, so every element of $G$ fixes it.

Conversely, if $f$ is $G$-invariant, choose any reflection $r\in G'\setminus G$ and write
\[
f=f_++f_-,
\qquad
f_\pm=\frac12(f\pm r\cdot f).
\]
Then $f_+$ is $G'$-invariant and $f_-$ transforms by the determinant character of $G'$. Such an anti-invariant polynomial vanishes on every reflecting hyperplane. Hence it is divisible by
\[
x_1x_2x_3
(x_1-x_2)(x_1+x_2)
(x_1-x_3)(x_1+x_3)
(x_2-x_3)(x_2+x_3)=\eta.
\]
After division by $\eta$, the quotient is $G'$-invariant. Therefore
\[
\mathbb R[x_1,x_2,x_3]^G
=
\mathbb R[I_1,I_2,I_3]
\oplus
\eta\,\mathbb R[I_1,I_2,I_3].
\]
This simultaneously gives parts (1), (2), (4), and (7). The Hilbert series is
\[
\boxed{
F_{\mathbb R[x_1,x_2,x_3]^G}(q)
=
\frac{1+q^9}{(1-q^2)(1-q^4)(1-q^6)}.
}
\]
Thus
\[
\boxed{(d_1,d_2,d_3;d)=(2,4,6;9)}.
\]

Expanding gives
\[
\begin{aligned}
F(q)
={}&1+q^2+2q^4+3q^6+4q^8+q^9+5q^{10}+q^{11}\\
&+7q^{12}+2q^{13}+8q^{14}+3q^{15}+\cdots.
\end{aligned}
\]
Hence the first ten nonzero terms are
\[
\boxed{
1+q^2+2q^4+3q^6+4q^8+q^9+5q^{10}+q^{11}+7q^{12}+2q^{13}.
}
\]
Equivalently, the coefficients in degrees $0$ through $9$ are
\[
1,0,1,0,2,0,3,0,4,1.
\]

For parts (5) and (6), use lexicographic order $x_1>x_2>x_3$. A Gröbner basis of
\[
(I_1,I_2,I_3)
\]
is
\[
\boxed{
\begin{aligned}
g_1&=x_1^2+x_2^2+x_3^2,\\
g_2&=x_2^4+x_2^2x_3^2+x_3^4,\\
g_3&=x_3^6.
\end{aligned}}
\]
Indeed, reducing $I_2$ by $g_1$ gives $-g_2$. After substituting $x_1^2=-x_2^2-x_3^2$ in $I_3$, one obtains
\[
-x_2^4x_3^2-x_2^2x_3^4,
\]
and reducing this by $g_2$ gives $x_3^6$. Conversely these reductions express the same ideal. The leading monomials
\[
x_1^2,
\qquad x_2^4,
\qquad x_3^6
\]
are pairwise relatively prime, so Buchberger's product criterion proves that the displayed set is a Gröbner basis.

The standard monomials are therefore
\[
x_1^a x_2^b x_3^c,
\qquad
0\le a<2,\quad0\le b<4,\quad0\le c<6.
\]
Hence
\[
\dim_\mathbb Q
\mathbb Q[x_1,x_2,x_3]/(I_1,I_2,I_3)
=2\cdot4\cdot6=48<\infty.
\]
Thus $I_1,I_2,I_3$ form a homogeneous system of parameters.

For part (9), put
\[
a=x_1^2,
\qquad b=x_2^2,
\qquad c=x_3^2.
\]
Then $I_1,I_2,I_3$ are the elementary symmetric functions
\[
a+b+c,
\qquad ab+ac+bc,
\qquad abc.
\]
Moreover
\[
\eta^2
=abc(a-b)^2(a-c)^2(b-c)^2.
\]
The discriminant of
\[
t^3-I_1t^2+I_2t-I_3
\]
is
\[
I_1^2I_2^2-4I_2^3-4I_1^3I_3-27I_3^2+18I_1I_2I_3.
\]
Therefore
\[
\boxed{
\eta^2
=I_3\left(
I_1^2I_2^2-4I_2^3-4I_1^3I_3-27I_3^2+18I_1I_2I_3
\right).
}
\]
Thus one may take
\[
\boxed{
Q(T,U,V,W)
=T^2-W(U^2V^2-4V^3-4U^3W-27W^2+18UVW).
}
\]

Part (9) is not needed to prove that $\eta$ is not a polynomial in $I_1,I_2,I_3$. Every polynomial in $I_1,I_2,I_3$ is a sum of terms of even degree because the three generators have even degrees $2,4,6$, whereas $\eta$ is a nonzero homogeneous invariant of odd degree $9$. Hence
\[
\eta\notin\mathbb R[I_1,I_2,I_3].
\]
The Hilbert-series numerator $1+q^9$ gives the same conclusion and shows that $1,\eta$ are exactly the two secondary generators over the polynomial subring of primary invariants.

For part (11), the Jacobian is
\[
J
=
det\left(
\frac{\partial(I_1,I_2,I_3)}{\partial(x_1,x_2,x_3)}
\right).
\]
Direct expansion gives
\[
\boxed{J=8\eta}.
\]
Thus, up to the nonzero scalar $8$, its linear factorization is
\[
\boxed{
J
=8x_1x_2x_3
(x_1-x_2)(x_1+x_2)
(x_1-x_3)(x_1+x_3)
(x_2-x_3)(x_2+x_3).
}
\]
There are nine linear factors, corresponding to the nine reflecting hyperplanes of the full reflection group $G'$ of type $B_3$.

Finally, for a finite real reflection group whose invariant ring has homogeneous basic invariants of degrees $d_1,d_2,d_3$, the Jacobian of those basic invariants is, up to a nonzero scalar, the product of the defining linear forms of the reflecting hyperplanes; its degree is
\[
\sum_{i=1}^3(d_i-1).
\]
Here this equals
\[
(2-1)+(4-1)+(6-1)=9.
\]
Thus, under the hypothesis in part (12), the degrees alone predict exactly nine linear factors, agreeing with the explicit Jacobian above.
:::
