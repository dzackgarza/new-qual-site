---
schema: qual/card@1
id: P-AGH534MULTLOCRING
kind: problem
title: The Hilbert-Samuel polynomial and the multiplicity of a local ring
classification:
  areas:
  - algebraic-geometry
  topics:
  - Blowups
  - Surfaces
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-19
  note: >-
    Read Hartshorne V.3.4 and the retained Egbert companion discussion through
    parts (a)--(e), together with the corpus Hilbert-polynomial and blowup
    context. The companion's part (a) incorrectly treats gr_m(A) as a
    polynomial ring in general, and part (d) is only an example-driven sketch.
    The proof below instead uses the standard Hilbert--Serre theorem for the
    finitely generated standard graded ring gr_m(A), the equality
    dim gr_m(A)=dim A, the initial-form calculation for a plane hypersurface,
    and the homogeneous coordinate ring of a projective cone.
- event: solution-written
  by: chatgpt
  date: 2026-09-19
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-19
---

::: {.problem}
Let $A$ be a noetherian local ring with maximal ideal $\mfm$.
For any $l>0$, let $\psi(l)=\operatorname{length}\left(A / \mfm^l\right)$.
We call $\psi$ the **Hilbert-Samuel function of $A$**.

a. Show that there is a polynomial $P_A(z) \in \QQ[z]$ such that $P_A(l)=\psi(l)$ for all $l \gg 0$.
This is the Hilbert-Samuel polynomial of $A$.

Hint: Consider the graded ring $\mathrm{gr}_{\mfm} A=\bigoplus_{d \geqslant 0} \mfm^d / \mfm^{d+1}$, and apply $(\mathrm{I}, 7.5)$.

See Nagata $[7, \text{Ch} III, \S 23]$ or Zariski-Samuel $[1, \text{vol} 2 , \text{Ch} VIII, \S 10]$.

b. Show that $\operatorname{deg} P_A=\operatorname{dim} A$.

c. Let $n=\operatorname{dim} A$.
Then we define the multiplicity of $A$, denoted $\mu(A)$, to be $(n !)\cdot$ (leading coefficient of $P_A$). If $P$ is a point on a noetherian scheme $X$, we define the multiplicity of $P$ on $X$, $\mu_P(X)$, to be $\mu\left(\mathcal{O}_{P, X}\right)$.

d. Show that for a point $P$ on a curve $C$ on a surface $X$, this definition of $\mu_P(C)$ coincides with the one in the text just before (3.5.2).

e. If $Y$ is a variety of degree $d$ in $\PP^n$, show that the vertex of the cone over $Y$ is a point of multiplicity $d$.
:::

::: {.solution}
Let
$$
k=A/\mfm,
\qquad
G=\operatorname{gr}_{\mfm}A
=
\bigoplus_{q\ge0}\mfm^q/\mfm^{q+1}.
$$

<1>1. The graded $k$-algebra $G$ is finitely generated and generated in
degree one.

::: {.proof}
Since $A$ is noetherian, the maximal ideal is finitely generated, say
$$
\mfm=(x_1,\ldots,x_s).
$$
The initial forms of the $x_i$ generate
$$
\mfm^q/\mfm^{q+1}
$$
by degree-$q$ monomials for every $q$. Thus $G$ is a quotient of the standard
graded polynomial ring
$$
k[X_1,\ldots,X_s]
$$
with $X_i\mapsto x_i\bmod\mfm^2$.
:::

<1>2. For every $l>0$,
$$
\boxed{
\psi(l)
=
\sum_{q=0}^{l-1}
\dim_k G_q.}
$$

::: {.proof}
The quotient $A/\mfm^l$ has the finite filtration
$$
A/\mfm^l
\supset
\mfm/\mfm^l
\supset\cdots\supset
\mfm^{l-1}/\mfm^l
\supset0.
$$
Its successive quotients are
$$
\mfm^q/\mfm^{q+1}=G_q,
\qquad 0\le q<l.
$$
Each is a finite-dimensional vector space over the residue field $k$, hence
its $A$-module length equals its $k$-dimension. Additivity of length gives
the formula.
:::

<1>3. There is a polynomial
$$
P_A(z)\in\QQ[z]
$$
such that
$$
P_A(l)=\psi(l)
$$
for all sufficiently large $l$.

::: {.proof}
By step <1>1, $G$ is a finitely generated standard graded $k$-algebra.
Hilbert--Serre, equivalently Hartshorne I.7.5 as suggested in the exercise,
says that its Hilbert function
$$
h_G(q)=\dim_k G_q
$$
agrees for $q\gg0$ with a rational polynomial $Q(q)$.

By step <1>2, $\psi(l)$ is the partial sum of this Hilbert function. Finite
sums of the polynomial values $Q(q)$ are polynomial in the upper limit: for
each monomial $q^j$, the sum
$$
\sum_{q=0}^{l-1}q^j
$$
is a polynomial in $l$ of degree $j+1$. The finitely many initial values
where $h_G(q)\ne Q(q)$ change only the constant term. Hence a polynomial
$P_A(z)\in\QQ[z]$ satisfies
$$
P_A(l)=\psi(l)
$$
for all $l\gg0$. This proves part (a).
:::

<1>4. One has
$$
\boxed{\dim G=\dim A.}
$$

::: {.proof}
This is the standard dimension theorem for the associated graded ring of a
noetherian local ring. One way to see it is through the extended Rees ring
$$
\mathcal R'
=
A[t^{-1},\mfm t]
\subseteq
A[t,t^{-1}].
$$
The element $t^{-1}$ is a nonzerodivisor and
$$
\mathcal R'/(t^{-1})
\cong
\operatorname{gr}_{\mfm}A=G.
$$
The Rees dimension theorem gives
$$
\dim\mathcal R'=\dim A+1;
$$
quotienting by the homogeneous nonzerodivisor $t^{-1}$ lowers the dimension
by one. Therefore
$$
\dim G=\dim A.
$$
:::

<1>5. The Hilbert--Samuel polynomial has degree
$$
\boxed{\deg P_A=\dim A.}
$$

::: {.proof}
Put
$$
n=\dim A=\dim G
$$
by step <1>4.

If $n=0$, then $A$ is artinian, so $\mfm^N=0$ for some $N$ and
$$
\psi(l)=\operatorname{length}(A)
$$
for $l\ge N$. Thus $P_A$ is constant and has degree $0=n$.

Assume $n>0$. For a finitely generated standard graded $k$-algebra of
dimension $n$, the Hilbert polynomial of its graded pieces has degree
$n-1$. Hence the polynomial $Q$ in step <1>3 has degree $n-1$. Taking
partial sums raises the degree by one, so the polynomial $P_A$ has degree
$n$. This proves part (b).
:::

<1>6. With $n=\dim A$, the multiplicity is
$$
\boxed{
\mu(A)=n!\,[z^n]P_A(z).}
$$

::: {.proof}
This is the definition in part (c). For a point $P$ of a noetherian scheme
$X$, the local multiplicity is consequently
$$
\mu_P(X)=\mu(\OO_{X,P}).
$$
There is no further assertion to prove in part (c).
:::

<1>7. Let $P$ lie on a curve $C$ on a nonsingular surface $X$. Put
$$
R=\OO_{X,P},
\qquad
\mfm_R=\mfm,
$$
and let $f\in R$ be a local equation for $C$. If
$$
r=\max\{q:f\in\mfm^q\},
$$
then
$$
\operatorname{gr}_{\mfm_C}\OO_{C,P}
\cong
k[u,v]/(f_r),
$$
where $f_r$ is the nonzero degree-$r$ initial form of $f$.

::: {.proof}
Because $X$ is nonsingular of dimension two at $P$, $R$ is a regular local
ring of dimension two and
$$
\operatorname{gr}_{\mfm}R\cong k[u,v].
$$
The curve local ring is
$$
B=\OO_{C,P}=R/(f),
$$
with maximal ideal $\mfm_C=\mfm/(f)$.

The $\mfm$-adic order is additive in the regular local ring because its
associated graded ring $k[u,v]$ is a domain. Therefore the initial ideal of
the principal ideal $(f)$ is generated by the initial form $f_r$. Passing to
associated graded rings gives
$$
\operatorname{gr}_{\mfm_C}B
\cong
k[u,v]/(f_r).
$$
:::

<1>8. For all $l\ge r$,
$$
\operatorname{length}
\left(
\OO_{C,P}/\mfm_C^l
\right)
=
rl-\frac{r(r-1)}2.
$$

::: {.proof}
Since $f_r\ne0$ is homogeneous of degree $r$, multiplication by $f_r$ gives
an exact sequence of graded $k[u,v]$-modules
$$
0
\longrightarrow
k[u,v](-r)
\xrightarrow{\cdot f_r}
k[u,v]
\longrightarrow
k[u,v]/(f_r)
\longrightarrow0.
$$
Thus the degree-$q$ piece of the quotient has dimension
$$
h(q)
=
\begin{cases}
q+1,&q<r,\\
r,&q\ge r.
\end{cases}
$$
By step <1>2 applied to the one-dimensional local ring $B$,
$$
\operatorname{length}(B/\mfm_C^l)
=
\sum_{q=0}^{l-1}h(q).
$$
For $l\ge r$ this is
$$
\frac{r(r+1)}2+r(l-r)
=
rl-\frac{r(r-1)}2.
$$
:::

<1>9. The local-ring multiplicity of $C$ at $P$ equals the multiplicity used
before (3.5.2):
$$
\boxed{\mu_P(C)=r.}
$$

::: {.proof}
The local ring $\OO_{C,P}$ has dimension one. Step <1>8 shows that its
Hilbert--Samuel polynomial has leading term
$$
rz.
$$
By part (c), its multiplicity is therefore
$$
1!\cdot r=r.
$$
But $r$ is exactly the order of a local equation of $C$ in the maximal ideal
of the nonsingular surface,
$$
f\in\mfm^r\setminus\mfm^{r+1},
$$
which is the multiplicity definition used in the text before (3.5.2).
This proves part (d).
:::

<1>10. Let $Y\subseteq\PP^N$ be a projective variety of dimension $s$ and
degree $d$, with homogeneous coordinate ring
$$
S=k[x_0,\ldots,x_N]/I_Y.
$$
If $V$ is the vertex of the projective cone over $Y$, then
$$
\operatorname{gr}_{\mfm_V}\OO_{V,\operatorname{Cone}(Y)}
\cong S.
$$

::: {.proof}
Write the projective cone in $\PP^{N+1}$ with coordinates
$$
[x_0:\cdots:x_N:z]
$$
and the same homogeneous equations $I_Y$ in the $x_i$. Its vertex is
$$
V=[0:\cdots:0:1].
$$
On the affine chart $z\ne0$, the cone is the affine cone
$$
\Spec S,
$$
and $V$ corresponds to the homogeneous maximal ideal
$$
\mfm=(x_0,\ldots,x_N)S.
$$
Hence
$$
\OO_{V,\operatorname{Cone}(Y)}=S_{\mfm}.
$$

Because $S$ is standard graded,
$$
\mfm^q/\mfm^{q+1}\cong S_q.
$$
Localizing at $\mfm$ does not change these finite-dimensional residue-field
vector spaces, so the associated graded ring of the local ring is $S$.
:::

<1>11. The vertex of the cone over $Y$ has multiplicity
$$
\boxed{d}. 
$$

::: {.proof}
For $q\gg0$, the Hilbert function of the homogeneous coordinate ring is the
Hilbert polynomial of $Y$:
$$
\dim_k S_q
=
\frac{d}{s!}q^s+\text{lower-degree terms}
$$
[[D-L6ERW]]. By steps <1>2 and <1>10, the Hilbert--Samuel function at the
vertex is the partial sum
$$
\sum_{q=0}^{l-1}\dim_kS_q.
$$
Its leading term is therefore
$$
\frac{d}{(s+1)!}l^{s+1}.
$$
The local ring at the vertex has dimension $s+1$, so part (c) gives
$$
\mu_V(\operatorname{Cone}(Y))
=(s+1)!\frac{d}{(s+1)!}
=d.
$$
This proves part (e).
:::

<1>12. Q.E.D.

::: {.proof}
Steps <1>1--<1>3 prove part (a), steps <1>4--<1>5 prove part (b), step <1>6
records the definition in part (c), steps <1>7--<1>9 prove part (d), and
steps <1>10--<1>11 prove part (e).
:::
:::
