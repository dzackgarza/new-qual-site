---
schema: qual/card@1
id: P-AGH317NORMAL
kind: problem
title: Normal varieties and the normalization of an affine variety
classification:
  areas:
  - algebraic-geometry
  topics:
  - Normal Varieties
  - Integral Closure
  - Cuspidal Cubic
relations:
- kind: uses
  target: P-AGH31CONICS
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-17
  note: 'Compared all five parts with Hartshorne I.3.17 and restored the source cross-reference to II.6.4 for Q_2. The normalization construction uses Theorem I.3.9A exactly as indicated.'
- event: solution-written
  by: chatgpt
  date: 2026-09-17
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-17
  note: 'Reviewed each normality argument and the universal property against published discussions. A common Q_2 proof divides by 2 and fails in characteristic 2; the attached proof instead uses the characteristic-free normality of k[s^2,st,t^2] via parity of total degree.'
---

::: {.problem}
A variety $Y$ is **normal at a point** $P \in Y$ if $\mco_P$ is an integrally closed ring, and $Y$ is **normal** if it is normal at every point.

(a) Show that every conic in $\PP^2$ is normal.

(b) Show that the quadric surfaces $Q_1 : xy = zw$ and $Q_2 : xy = z^2$ in $\PP^3$ are normal. For the latter, compare (II, Ex. 6.4).

(c) Show that the cuspidal cubic $y^2 = x^3$ in $\AA^2$ is not normal.

(d) If $Y$ is affine, show that $Y$ is normal if and only if $A(Y)$ is integrally closed.

(e) Let $Y$ be an affine variety.
Show that there is a normal affine variety $\tilde{Y}$ and a morphism $\pi: \tilde{Y} \to Y$ with the following property: whenever $Z$ is a normal variety and $\phi: Z \to Y$ is a **dominant** morphism, meaning $\phi(Z)$ is dense in $Y$, there is a unique morphism $\theta: Z \to \tilde{Y}$ with $\phi = \pi \circ \theta$.
The variety $\tilde{Y}$ is called the **normalization** of $Y$.
:::

::: {.solution}
We first record the affine criterion needed repeatedly below.

<1>1. If $A$ is an integrally closed domain, every localization $S^{-1}A$ is integrally closed.

::: {.proof}
Let $\xi\in\operatorname{Frac}A$ be integral over $S^{-1}A$.
Choose a monic relation
$$
\xi^n+\frac{a_{n-1}}{s_{n-1}}\xi^{n-1}+\cdots+\frac{a_0}{s_0}=0,
$$
with $a_i\in A$ and $s_i\in S$, and put $s=s_0\cdots s_{n-1}$.
Multiplying by $s^n$ rewrites the equation as a monic equation for $s\xi$ with coefficients in $A$.
Thus $s\xi$ is integral over $A$, hence lies in $A$.
Therefore $\xi=(s\xi)/s\in S^{-1}A$.
:::

<1>2. For an affine variety $Y$ with $A=A(Y)$,
$$
Y\text{ is normal}\quad\Longleftrightarrow\quad A\text{ is integrally closed}.
$$
This proves (d).

::: {.proof}
If $A$ is integrally closed, then for every point $P\in Y$,
$$
\mco_{P,Y}\cong A_{\mathfrak m_P}
$$
is integrally closed by step <1>1, so $Y$ is normal.

Conversely, suppose every local ring $A_{\mathfrak m}$ at a maximal ideal is integrally closed.
Let $\xi\in\operatorname{Frac}A$ be integral over $A$.
Then $\xi$ is integral over every $A_{\mathfrak m}$ and hence belongs to every such localization.
We claim
$$
A=\bigcap_{\mathfrak m\text{ maximal}}A_{\mathfrak m}
\subseteq\operatorname{Frac}A.
$$
Indeed, if $\xi\notin A$, the ideal
$$
I=\{a\in A:a\xi\in A\}
$$
is proper and lies in some maximal ideal $\mathfrak m$.
But $\xi\in A_{\mathfrak m}$ would give $s\notin\mathfrak m$ with $s\xi\in A$, so $s\in I\subseteq\mathfrak m$, a contradiction.
Hence $\xi\in A$, proving that $A$ is integrally closed.
:::

<1>3. Every conic in $\PP^2$ is normal, proving (a).

::: {.proof}
By [[P-AGH31CONICS]], every projective conic is isomorphic to $\PP^1$.
The standard affine charts of $\PP^1$ are copies of $\AA^1$, whose coordinate ring $k[t]$ is a UFD and hence integrally closed.
By step <1>2 each chart is normal, and the local ring of $\PP^1$ at a point is the same as the local ring in any open chart containing that point.
Thus $\PP^1$ is normal.
Normality is preserved by isomorphism, so every conic is normal.
:::

<1>4. The quadric surface
$$
Q_1=Z(xy-zw)\subseteq\PP^3
$$
is normal.

::: {.proof}
Its four standard affine charts are all affine planes.
For example, on $w\ne0$ set $w=1$; the equation becomes $z=xy$, so this chart has coordinate ring
$$
k[x,y,z]/(z-xy)\cong k[x,y].
$$
The same elimination works on the charts $x\ne0$, $y\ne0$, and $z\ne0$ by solving for the coordinate paired with the chosen nonzero coordinate in $xy=zw$.
Thus every point has an affine neighborhood isomorphic to $\AA^2$, which is normal by step <1>2.
Hence $Q_1$ is normal.
:::

<1>5. The affine domain
$$
R=k[x,y,z]/(xy-z^2)
$$
is integrally closed in every characteristic.

::: {.proof}
Define
$$
R\longrightarrow k[s,t],
\qquad
x\longmapsto s^2,
\quad
y\longmapsto t^2,
\quad
z\longmapsto st.
$$
Every class in $R$ has a representative of the form
$$
f(x,y)+z g(x,y),
$$
because powers $z^r$ reduce using $z^2=xy$.
Its image is
$$
f(s^2,t^2)+st\,g(s^2,t^2).
$$
The first summand contains only monomials whose two exponents are even, and the second only monomials whose two exponents are odd.
Their supports are disjoint, and $s^2,t^2$ are algebraically independent, so the displayed map is injective.
This also proves that the displayed representatives are unique.
Its image is
$$
k[s^2,st,t^2],
$$
which is exactly the subring of $k[s,t]$ spanned by monomials of even total degree.

Write $K=\operatorname{Frac}R\subseteq k(s,t)$.
We first show
$$
k[s,t]\cap K=R.
$$
Let $h\in k[s,t]\cap K$ and write $h=a/b$ with nonzero $a,b\in R$.
Decompose $h=h_{\mathrm{ev}}+h_{\mathrm{odd}}$ according to parity of total monomial degree.
Since every monomial of $b$ has even total degree, multiplication by $b$ preserves this parity decomposition.
The equation $hb=a$, whose right side has only even total degree, forces
$$
h_{\mathrm{odd}}b=0.
$$
Because $k[s,t]$ is a domain, $h_{\mathrm{odd}}=0$.
Thus $h$ has only even-total-degree monomials and hence belongs to $R$.

Now let $\alpha\in K$ be integral over $R$.
The same monic equation shows that $\alpha$ is integral over $k[s,t]$.
Since the UFD $k[s,t]$ is integrally closed,
$$
\alpha\in k[s,t].
$$
The intersection equality then gives $\alpha\in R$.
Therefore $R$ is integrally closed.
:::

<1>6. The quadric surface
$$
Q_2=Z(xy-z^2)\subseteq\PP^3
$$
is normal, completing (b).

::: {.proof}
The only point of $Q_2$ at which $x=y=z=0$ is the vertex
$$
V=[0:0:0:1].
$$
Every other point lies in $D_+(x)$ or $D_+(y)$: if $z\ne0$, the equation $xy=z^2$ forces both $x$ and $y$ to be nonzero.
On $D_+(x)$, setting $x=1$ gives $y=z^2$, so the chart is $\AA^2$ with coordinates $z,w$; similarly for $D_+(y)$.

The vertex lies in the chart $w\ne0$.
Setting $w=1$ identifies this chart with the affine surface
$$
xy=z^2
$$
whose coordinate ring is the integrally closed domain $R$ of step <1>5.
By step <1>2 this affine chart is normal.
Thus every point of $Q_2$ has a normal affine neighborhood, and $Q_2$ is normal.
:::

<1>7. The cuspidal cubic
$$
C=Z(y^2-x^3)\subseteq\AA^2
$$
is not normal, proving (c).

::: {.proof}
Its coordinate ring is
$$
A(C)=k[x,y]/(y^2-x^3)\cong k[t^2,t^3],
$$
under $x\mapsto t^2$ and $y\mapsto t^3$.
The element $t$ belongs to the fraction field, since
$$
t=\frac{t^3}{t^2},
$$
and it is integral over $A(C)$ because it satisfies
$$
T^2-t^2=0.
$$
But $t\notin k[t^2,t^3]$: every positive exponent occurring in that subring belongs to the semigroup generated by $2$ and $3$, which does not contain $1$.
Thus $A(C)$ is not integrally closed, and step <1>2 implies that $C$ is not normal.
:::

<1>8. Let $A=A(Y)$, let $K=\operatorname{Frac}A$, and let $B$ be the integral closure of $A$ in $K$.
Then $B$ is the coordinate ring of a normal affine variety $\widetilde Y$, and the inclusion $A\hookrightarrow B$ induces a morphism
$$
\pi:\widetilde Y\to Y.
$$

::: {.proof}
Hartshorne's finiteness of integral closure theorem [@Har10a, Theorem I.3.9A], applied to the degree-one field extension $K/K$, says that $B$ is a finitely generated $A$-module and in particular a finitely generated $k$-algebra.
It is a domain and is integrally closed by definition.
Hence $B=A(\widetilde Y)$ for an affine variety $\widetilde Y$, which is normal by step <1>2.
The inclusion of coordinate rings $A\hookrightarrow B$ gives the morphism $\pi$.
:::

<1>9. Every dominant morphism $\phi:Z\to Y$ from a normal variety factors uniquely through $\pi$.

::: {.proof}
Dominance makes the pullback
$$
\phi^*:A\longrightarrow\mco(Z)
$$
injective.
Indeed, if $0\ne a\in A$ had $a\circ\phi=0$, the dense set $\phi(Z)$ would lie in the proper closed zero set $Z_Y(a)$, impossible.
Thus $\phi^*$ extends to an embedding
$$
K=\operatorname{Frac}A\hookrightarrow K(Z).
$$

Take $b\in B$ and regard its image as an element of $K(Z)$.
Because $b$ is integral over $A$, at every point $z\in Z$ its image satisfies a monic equation with coefficients in the local ring $\mco_{z,Z}$.
Normality of $Z$ makes that local ring integrally closed in $K(Z)$, so the image of $b$ belongs to $\mco_{z,Z}$ for every $z$.
Hence it is a global regular function on $Z$: the local representatives supplied by these germs agree on overlaps because they represent the same rational function.
We obtain a $k$-algebra homomorphism
$$
B\longrightarrow\mco(Z)
$$
extending $\phi^*:A\to\mco(Z)$.
Choosing affine coordinates for $\widetilde Y$ from generators of $B$, these global regular functions define a morphism
$$
\theta:Z\to\widetilde Y
$$
[@Har10a, Lemma I.3.6].
The equality of pullbacks on $A$ gives
$$
\phi=\pi\circ\theta.
$$

For uniqueness, let $\theta'$ be another such factorization.
Its pullback $B\to\mco(Z)$ agrees with $\phi^*$ on $A$.
For any $b\in B\subseteq K=\operatorname{Frac}A$, write $b=a/c$ with $a,c\in A$ and $c\ne0$.
Then in the domain $K(Z)$ every extension of $\phi^*$ must satisfy
$$
\theta'^*(b)=\frac{\phi^*(a)}{\phi^*(c)}=\theta^*(b),
$$
since injectivity gives $\phi^*(c)\ne0$.
Thus the two pullbacks on $B$ coincide, so the two morphisms to the affine variety $\widetilde Y$ coincide.
This is the required universal property.
:::

<1>10. Q.E.D.

::: {.proof}
Steps <1>3, <1>4--<1>6, <1>7, <1>2, and <1>8--<1>9 prove parts (a)--(e), respectively.
:::
:::
