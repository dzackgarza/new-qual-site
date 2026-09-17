---
schema: qual/card@1
id: P-AGH265QUADRIC
kind: problem
title: Class groups of quadric hypersurfaces and Klein's theorem
classification:
  areas:
  - algebraic-geometry
  topics:
  - Divisor Class Groups
  - Quadric Hypersurfaces
  - Complete Intersections
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-17
  note: Read all four parts of Exercise II.6.5 and its hint in the Hartshorne transcription. Made the algebraically closed base-field convention and the bounds 2 <= r <= n explicit. The proof computes every relation from units on the hyperplane complement and constructs the irreducible ambient hypersurface in Klein's theorem.
- event: solution-written
  by: chatgpt
  date: 2026-09-17
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-17
---

::: {.problem}
Let $k$ be an algebraically closed field of characteristic different from two, let $2\le r\le n$, and put
$$
S=k[x_0,\ldots,x_n]/(x_0^2+\cdots+x_r^2),\qquad X=\Spec S.
$$

(a) Show that $X$ is normal, using Exercise II.6.4.

(b) By a linear change of coordinates, write the equation as $x_0x_1=x_2^2+\cdots+x_r^2$.
Compute the class group and show that
$$
\Cl(X)\cong
\begin{cases}
\ZZ/2\ZZ,&r=2,\\
\ZZ,&r=3,\\
0,&r\ge4.
\end{cases}
$$

(c) Let $Q=\Proj S\subseteq\PP_k^n$ be the projective quadric defined by the same equation, and let $h$ be its hyperplane-section class.
Show that $\Cl(Q)\cong\ZZ$ with $h$ twice a generator when $r=2$, that $\Cl(Q)\cong\ZZ\oplus\ZZ$ when $r=3$, and that $\Cl(Q)\cong\ZZ$ with generator $h$ when $r\ge4$.

(d) Prove Klein's theorem: for $r\ge4$, every irreducible codimension-one subvariety $Y\subseteq Q$ is the intersection of $Q$ with an irreducible hypersurface $V\subseteq\PP_k^n$, with multiplicity one.
Thus $Y$ is a complete intersection.
:::

::: {.hint}
For part (d), first show that the homogeneous coordinate ring $S(Q)$ is a unique factorization domain.
:::

::: {.solution}
All class groups are [[D-5PQ5W|Weil-divisor class groups]].
The extra coordinates $x_{r+1},\ldots,x_n$ are retained throughout the calculation.

<1>1. The ring $S$ is an integrally closed domain, and $Q$ is normal.

::: {.proof}
In $R=k[x_1,\ldots,x_n]$, the polynomial $f=-(x_1^2+\cdots+x_r^2)$ is square-free.
Indeed, a repeated irreducible factor would divide every partial derivative of $f$, and in particular both $-2x_1$ and $-2x_2$.
This is impossible, since $x_1,x_2$ are relatively prime and $2$ is a unit.
The [[P-AGH264DOUBLECOVER|square-free double-cover calculation]] therefore makes $S=R[x_0]/(x_0^2-f)$ an integrally closed domain, proving part (a).

For a nonzero degree-one coordinate $s\in S$, put $B=(S_s)_0$.
The standard grading gives $S_s=B[s,s^{-1}]$.
If $\alpha\in\operatorname{Frac}(B)$ is integral over $B$, it is integral over the normal ring $S_s$ and therefore lies in $S_s$.
The equality $\operatorname{Frac}(B)\cap B[s,s^{-1}]=B$, inside $\operatorname{Frac}(B)(s)$, then gives $\alpha\in B$.
Hence every standard affine chart of $Q$ is normal, so $Q$ is normal.
:::

<1>2. There are coordinates in which $S=k[u,v,w_2,\ldots,w_n]/(uv-g)$, where $g=w_2^2+\cdots+w_r^2$.

::: {.proof}
Choose $\iota\in k$ with $\iota^2=-1$ and set
$$
u=x_0+\iota x_1,\qquad v=-x_0+\iota x_1,\qquad w_j=x_j\quad(j\ge2).
$$
This transformation is invertible, with $x_0=(u-v)/2$ and $x_1=(u+v)/(2\iota)$.
Since $uv=-(x_0^2+x_1^2)$, it transforms the equation into $uv=g$.

Factor $g$ in $B=k[w_2,\ldots,w_n]$ as $g=\prod_{j=1}^s p_j^{e_j}$, with distinct irreducible factors.
The factors and multiplicities are
$$
\begin{array}{c|c|c}
r& (p_1,\ldots,p_s)&(e_1,\ldots,e_s)\\\hline
2&(w_2)&(2)\\
3&(w_2+\iota w_3,\ w_2-\iota w_3)&(1,1)\\
r\ge4&(g)&(1).
\end{array}
$$
For the last row, a factorization of the homogeneous quadratic $g$ would be a product of two linear forms.
The symmetric matrix of such a product has rank at most two, whereas the matrix of $g$ has rank $r-1\ge3$.
Thus $g$ is irreducible in that case.
The linear factors in the middle row are distinct because $\operatorname{char}k\ne2$.
:::

<1>3. The complement of $D(u)\subseteq X$ has prime-divisor components $D_j=V(u,p_j)$, and
$$
\operatorname{div}_X(u)=\sum_{j=1}^s e_jD_j.
$$

::: {.proof}
Setting $u=0$ gives $S/(u)=B[v]/(g)$, whose minimal primes are precisely $(p_j)$.
Thus its irreducible components are the $D_j$.
The element $v$ is nonzero at their generic points, and
$$
S_v=B[v,v^{-1}],\qquad u=g/v.
$$
At the generic point of $D_j$, this is the localization at the height-one prime $(p_j)$.
It is a DVR with uniformizer $p_j$.
The other factors of $g$ and $v$ are units there, so $v_{D_j}(u)=e_j$.
Since $u$ is regular and invertible away from its zero set, it has no other zeros or poles.
:::

<1>4. The affine class group has the presentation
$$
\Cl(X)\cong\left(\bigoplus_{j=1}^s\ZZ d_j\right)\Big/\ZZ\left(\sum_{j=1}^s e_jd_j\right),\qquad d_j\longmapsto[D_j],
$$
where the $d_j$ are formal free generators.

::: {.proof}
Localizing at $u$ eliminates $v$, giving
$$
S_u=B[u,u^{-1}].
$$
This is a [[D-INULL|unique factorization domain]], so $\Cl(D(u))=0$ [@Har10a, Proposition II.6.2].
The divisor restriction sequence shows that the classes $[D_j]$ generate $\Cl(X)$ [@Har10a, Proposition II.6.5].

Suppose $\sum_j a_jD_j=\operatorname{div}_X(F)$ for $F\in K(X)^\times$.
On $D(u)$, the divisor of $F$ is zero.
Writing $F$ as a quotient of relatively prime elements in the UFD $S_u$, zero valuation at every irreducible forces both numerator and denominator to be units.
Hence $F\in S_u^\times=k^\times u^{\ZZ}$.
For $F=cu^m$, step <1>3 gives $a_j=me_j$ for every $j$.
Conversely, each such vector is the divisor of $u^m$.
This proves that the displayed relation generates all relations, not just one relation among the generators.

Substituting the multiplicities in step <1>2 yields
$$
\boxed{\Cl(X)\cong
\begin{cases}
\ZZ d_1/\ZZ(2d_1)\cong\ZZ/2\ZZ,&r=2,\\
(\ZZ d_1\oplus\ZZ d_2)/\ZZ(d_1+d_2)\cong\ZZ,&r=3,\\
0,&r\ge4.
\end{cases}}
$$
For $r=3$, the class $[D_1]$ is a generator and $[D_2]=-[D_1]$.
This proves part (b).
:::

<1>5. The projective class group is freely generated by $E_j=V_+(u,p_j)\subseteq Q$, and $h=\sum_j e_j[E_j]$.

::: {.proof}
On the standard chart $D_+(u)$, divide all coordinates by $u$ and eliminate $v/u$ using the equation.
This gives
$$
D_+(u)\cong\Spec k[w_2/u,\ldots,w_n/u]\cong\AA_k^{n-1}.
$$
Its class group is zero, and its only invertible regular functions are $k^\times$.
The complement has exactly the prime-divisor components $E_j$, so their classes generate $\Cl(Q)$ by Proposition II.6.5.

If $\sum_j a_jE_j=\operatorname{div}_Q(F)$, then $F$ has zero divisor on this affine-space chart.
The same relatively prime numerator-and-denominator argument as in step <1>4 makes its restriction a unit of the polynomial ring, hence an element of $k^\times$.
Since this chart is dense, $F$ is that constant in $K(Q)$ and its divisor is zero everywhere.
Therefore every $a_j=0$, proving that the generators are independent.

At the generic point of $E_j$, the coordinate $v$ is nonzero.
On $D_+(v)$, the hyperplane section $u=0$ has local equation
$$
u/v=g(w_2/v,\ldots,w_r/v)=\prod_{j=1}^s p_j(w_2/v,\ldots,w_n/v)^{e_j}.
$$
This chart is also affine space, and its local ring at $E_j$ is the DVR whose uniformizer is the corresponding irreducible factor $p_j(w/v)$.
Thus the hyperplane divisor is $\sum_j e_jE_j$.
Any other hyperplane not containing $Q$ has the same class, since the ratio of the two linear equations is a rational function on $Q$ [@Har10a, Exercise II.6.2].
Consequently
$$
\boxed{(\Cl(Q),h)\cong
\begin{cases}
(\ZZ,2),&r=2,\\
(\ZZ^2,(1,1)),&r=3,\\
(\ZZ,1),&r\ge4.
\end{cases}}
$$
These identifications prove all assertions in part (c).
:::

<1>6. For $r\ge4$, every prime divisor $Y\subseteq Q$ is the reduced scheme-theoretic intersection of $Q$ with an irreducible hypersurface of $\PP_k^n$.

::: {.proof}
Steps <1>1 and <1>4 make $S$ a normal noetherian domain with zero divisor class group.
It is therefore a UFD by Proposition II.6.2.
The homogeneous prime ideal $\mathfrak p=I(Y)/I(Q)$ has height one in $S$: the affine cone over $Y$ has dimension $\dim Y+1$, one less than the dimension $\dim Q+1$ of $\Spec S$ [@Har10a, Exercise I.2.10].
Hence $\mathfrak p=(f)$ for an irreducible element $f\in S$.

The generator can be chosen homogeneous.
Indeed, a nonzero homogeneous component $f_d$ of $f$ belongs to the homogeneous ideal $\mathfrak p$, so $f_d=fb$ for some nonzero $b\in S$.
In a nonnegatively graded domain, the least and greatest nonzero degrees of a product are the sums of the respective least and greatest degrees of its factors.
Since $fb$ is homogeneous, both factors have only one nonzero degree.
Thus $f$ is homogeneous, of degree $d>0$ because $S_0=k$ and a nonzero constant cannot generate a proper ideal.

Choose a homogeneous lift $F\in k[x_0,\ldots,x_n]$ of $f$ of the same degree.
This lift is irreducible.
To see this, a nontrivial factorization $F=GH$ would have homogeneous positive-degree factors by the same least-and-greatest-degree argument.
Their images in $S$ would be nonzero, since their product is $f\ne0$.
Neither image could be a unit: the same grading argument shows that the only units of $S$ are $k^\times$.
Their product would therefore contradict irreducibility of $f$ in $S$.

Let $V=V_+(F)\subseteq\PP_k^n$.
It is an irreducible hypersurface, and
$$
V\cap Q=\Proj(S/(f))=\Proj(S/\mathfrak p)=Y
$$
as closed subschemes.
The quotient $S/\mathfrak p$ is a domain, so this intersection is reduced.
In particular, at the generic point of $Y$, its local equation generates the maximal ideal of the DVR $\OO_{Q,\eta_Y}$ and has valuation one.
This gives the required multiplicity.
Finally, the quadratic equation of $Q$ and $F$ form a regular sequence in the ambient polynomial ring: the first is nonzero in a domain, and the image $f$ of the second is nonzero in the domain $S$.
Thus $Y$ is a complete intersection, proving part (d).
:::

<1>7. Q.E.D.

::: {.proof}
Step <1>1 proves normality, steps <1>2--<1>4 give the coordinate change and affine class groups, step <1>5 gives the projective class groups with their hyperplane classes, and step <1>6 proves Klein's theorem.
:::
:::

::: {.remark title="The base field"}
The algebraically closed-field hypothesis makes the coordinate change and the factorization used in part (b) available.
Characteristic different from two alone does not suffice for that change over an arbitrary field.
For example, over $\mathbb R$ the form $x_0^2+x_1^2+x_2^2$ has no nonzero zero, whereas $uv-w^2$ vanishes at $(1,0,0)$; an invertible real linear transformation preserves the existence of a nonzero zero.
Part (a), unlike the splitting argument, holds over every field of characteristic different from two by step <1>1.
:::
