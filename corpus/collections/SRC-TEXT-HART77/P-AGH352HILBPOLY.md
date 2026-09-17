---
schema: qual/card@1
id: P-AGH352HILBPOLY
kind: problem
title: Existence of the Hilbert polynomial of a coherent sheaf
classification:
  areas:
  - algebraic-geometry
  topics:
  - Hilbert Polynomial
  - Euler Characteristic
  - Coherent Sheaves
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-17
  note: Compared both parts and the dimension-induction hint with the retained Hartshorne Chapter III section 5 transcription. The proof handles finite fields by an explicit flat Cech base-extension comparison, proves the polynomial identity for all integer twists, and proves finite generation of a high truncation rather than assuming the full all-degree section module is finite.
- event: solution-written
  by: chatgpt
  date: 2026-09-17
---

::: {.problem}
(a) Let $X$ be a projective scheme over a field $k$, let $\mco_X(1)$ be a very ample invertible sheaf on $X$ over $k$, and let $\mcf$ be a coherent sheaf on $X$.
Show that there is a polynomial $P(z) \in \QQ[z]$, such that $\chi(\mcf(n))=P(n)$ for all $n \in \ZZ$.
We call $P$ the **Hilbert polynomial** of $\mcf$ with respect to the sheaf $\mco_X(1)$.

(b) Now let $X=\PP_k^r$, and let $M=\Gamma_*(\mcf)$, considered as a graded $S=k[x_0, \ldots, x_r]$-module.
Use (5.2) to show that the Hilbert polynomial of $\mcf$ just defined is the same as the Hilbert polynomial of $M$ defined in (I, §7).
Here the polynomial of the all-degree section module means its eventual Hilbert-function polynomial; justify the finite-module comparison by taking a sufficiently high truncation of $M$.
:::

::: {.hint}
For (a), use induction on $\dim\operatorname{Supp}\mcf$, general properties of numerical polynomials (I, 7.3), and exact sequences of the form
$$
0\to\mcr\to\mcf(-1)\to\mcf\to\mcl\to0.
$$
:::

::: {.solution}
Write $L=\OO_X(1)$ and $\mcf(n)=\mcf\otimes L^{\otimes n}$ for every $n\in\ZZ$, using dual tensor powers for negative $n$.
The Euler characteristic is defined and additive by [[P-AGH351EULERCHAR]].
All Euler characteristics and cohomology dimensions are taken over the field of definition of the scheme in question.

<1>1. Euler characteristics of these twists are unchanged by extension of the ground field.

::: {.proof}
Let $K/k$ be a field extension, set $X_K=X\times_k\Spec K$, and write $\mcf_K$ and $L_K$ for the pullbacks.
Choose a finite affine open cover of the noetherian separated scheme $X$.
Its finite intersections are affine, and the base-changed cover has the same property on $X_K$.
On an intersection $\Spec A$, if a quasi-coherent sheaf corresponds to an $A$-module $N$, its pullback corresponds to $N\otimes_k K$ over $A\otimes_k K$.
Thus the Čech complex of each $\mcf_K(n)$ is the tensor product over $k$ of the Čech complex of $\mcf(n)$ with $K$.
The finite products in a term of this finite-cover complex commute with tensor product.
Since $K$ is flat over $k$, taking cohomology commutes with that tensor product.
The affine-cover comparison [@Har10a, Theorem III.4.5] gives
$$
H^i(X_K,\mcf_K(n))\cong H^i(X,\mcf(n))\otimes_k K.
$$
These groups are finite-dimensional [@Har10a, Theorem III.5.2], and tensoring a finite-dimensional $k$-space with $K$ preserves its dimension over the respective field.
Taking the alternating sum proves $\chi(X_K,\mcf_K(n))=\chi(X,\mcf(n))$ for every integer $n$.
:::

<1>2. If $\mcf=0$, its Euler-characteristic polynomial is zero.
If $\mcf$ has zero-dimensional support, then $\chi(\mcf(n))=\chi(\mcf)$ for every $n$.

::: {.proof}
The zero sheaf assertion is immediate.
Otherwise a zero-dimensional closed subset of a noetherian scheme consists of finitely many closed points.
For each point of the support, choose an open neighborhood on which $L$ is trivial and which contains no other point of the support.
These neighborhoods, together with the complement of the support, cover $X$.
On each such neighborhood a chosen frame of $L$ identifies $\mcf(n)$ with $\mcf$ for every integer $n$.
On an intersection of two different neighborhoods the sheaf is zero, since that intersection contains no support point.
It is also zero on the complement of its support.
Hence the local isomorphisms glue to $\mcf(n)\cong\mcf$.
Their Euler characteristics are equal, giving the constant polynomial required in the zero-dimensional induction case.
:::

<1>3. Over an infinite field, $\chi(\mcf(n))$ is a polynomial in $n$ with rational coefficients for all $n\in\ZZ$.

::: {.proof}
Induct on the dimension $d$ of the support, using step <1>2 for dimension zero and the zero sheaf.
Suppose $d>0$.
Use the projective embedding for $L$ to choose a hyperplane not containing any irreducible component of $\operatorname{Supp}\mcf$.
Such a hyperplane exists over an infinite field: the linear forms vanishing on a fixed component constitute a proper linear subspace, and a finite-dimensional vector space over an infinite field is not a finite union of proper linear subspaces.
For the latter assertion, choose a nonzero linear functional vanishing on each proper subspace; their product is a nonzero polynomial, and a nonzero polynomial over an infinite field does not vanish at every vector, by induction on the number of variables.

Let $h$ be the resulting section of $L$ and use multiplication by $h$ to form
$$
0\longrightarrow\mathcal R\longrightarrow\mcf(-1)
\xrightarrow{h}\mcf\longrightarrow\mathcal Q\longrightarrow0.
$$
The sheaves $\mathcal R$ and $\mathcal Q$ are coherent.
Their supports are contained in $V(h)\cap\operatorname{Supp}\mcf$, since the map is an isomorphism where $h$ is invertible.
This intersection has dimension at most $d-1$, since the hyperplane contains no component of the support.
The induction hypothesis therefore gives polynomials $P_{\mathcal R},P_{\mathcal Q}$ for all twists of these two sheaves.

Twisting the displayed exact sequence by $L^n$ is exact, and additivity of Euler characteristic gives
$$
\chi(\mcf(n))-\chi(\mcf(n-1))=P_{\mathcal Q}(n)-P_{\mathcal R}(n)
\qquad(n\in\ZZ).
$$
Every polynomial $D(z)\in\QQ[z]$ has a polynomial antiderivative for this finite-difference operator.
Indeed, express $D$ as a rational linear combination of the basis polynomials $\binom{z-1}{j}$, and replace each by $\binom{z}{j+1}$, whose difference at $z,z-1$ is $\binom{z-1}{j}$ [@Har10a, Proposition I.7.3].
Choose $Q$ with $Q(z)-Q(z-1)=P_{\mathcal Q}(z)-P_{\mathcal R}(z)$ and set
$$
P(z)=Q(z)+\chi(\mcf)-Q(0).
$$
The functions $P(n)$ and $\chi(\mcf(n))$ have the same difference for every integer $n$ and agree at $n=0$.
Induction both upwards and downwards from zero gives equality for every $n\in\ZZ$.
This completes the induction, including possible kernels of multiplication by the hyperplane section.
:::

<1>4. Part (a) holds over every field, and its polynomial is unique.

::: {.proof}
For an arbitrary $k$, pass to the infinite field $K=k(t)$.
Apply step <1>3 to the projective scheme $X_K$, its very ample sheaf $L_K$, and $\mcf_K$.
Step <1>1 identifies its Euler-characteristic function at every integer with the original function.
The same polynomial $P\in\QQ[z]$ therefore satisfies
$$
\boxed{P(n)=\chi(X,\mcf\otimes L^{\otimes n})\qquad(n\in\ZZ).}
$$
Two rational polynomials satisfying this identity agree at infinitely many integers, so their difference is zero.
This proves uniqueness as well as existence, without an infinite-field hypothesis on the original data.
:::

<1>5. In (b), a sufficiently high truncation of $M=\Gamma_*(\mcf)$ is a finite graded $S$-module.

::: {.proof}
Choose $a\ge0$ so that $\mcf(a)$ is generated by finitely many global sections, using ampleness of $\OO(1)$ and quasi-compactness.
This gives an exact sequence
$$
0\longrightarrow\mathcal K\longrightarrow\OO_X(-a)^{\oplus s}
\longrightarrow\mcf\longrightarrow0
$$
with coherent kernel.
Serre vanishing makes $H^1(X,\mathcal K(n))=0$ for every sufficiently large $n$ [@Har10a, Theorem III.5.2].
Choose $n_0\ge a$ beyond this bound.
For every $n\ge n_0$, taking sections gives a surjection
$$
S_{n-a}^{\oplus s}\longrightarrow H^0(X,\mcf(n))=M_n.
$$
Here $H^0(\PP_k^r,\OO(n-a))=S_{n-a}$ because $n-a\ge0$, including $r=0$ as checked in [[P-AGH2510SATIDEAL]].
The maps arise from the same generating sections and commute with multiplication by homogeneous polynomials.
Thus they combine to a graded surjection
$$
\bigl(S(-a)^{\oplus s}\bigr)_{\ge n_0}\twoheadrightarrow M_{\ge n_0}.
$$
The source is a submodule of a finite module over the noetherian ring $S$ and is finite.
Its quotient $M_{\ge n_0}$ is consequently finite as claimed.
:::

<1>6. The Hilbert polynomial of this finite graded truncation, and hence the eventual Hilbert polynomial of $M$, is the polynomial in (a).

::: {.proof}
For $n\ge n_0$, the truncation from step <1>5 has graded piece $M_n$.
Its Hilbert polynomial from [@Har10a, Chapter I, §7] agrees with $\dim_k M_n$ for all sufficiently large $n$.
Serre vanishing also gives
$$
\dim_k M_n=h^0(X,\mcf(n))=\chi(X,\mcf(n))=P(n)
$$
for all sufficiently large $n$.
The two polynomials therefore agree at infinitely many integers and are equal.
Further truncation leaves the eventual Hilbert function unchanged, so this comparison does not depend on $n_0$.
This proves (b).
:::

<1>7. Q.E.D.

::: {.proof}
Steps <1>1--<1>4 prove (a) at all integer twists over every field, and steps <1>5--<1>6 prove the graded-module comparison in (b).
:::
:::

::: {.remark title="The full graded section module need not be finite"}
For the structure sheaf of a $k$-rational point in $\PP_k^1$, every twist has a one-dimensional space of global sections.
Thus $\Gamma_*(\mcf)$ has nonzero graded pieces in arbitrarily negative degrees.
A finitely generated graded module over $k[x_0,x_1]$ is bounded below, since finitely many homogeneous generators have a least degree and ring multiplication cannot decrease degrees.
The full section module in this example is therefore not finite.
Step <1>5 provides the finite truncation needed for applying the finite-module Hilbert-polynomial theorem without changing the eventual function in (b).
:::
