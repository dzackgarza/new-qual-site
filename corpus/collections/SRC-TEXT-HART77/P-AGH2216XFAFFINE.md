---
schema: qual/card@1
id: P-AGH2216XFAFFINE
kind: problem
title: Sections over the nonvanishing locus of a global function
classification:
  areas:
  - algebraic-geometry
  topics:
  - Schemes
  - Global Sections
  - Localization
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-17
  note: Checked against the collection's Hartshorne II.2.16 statement and source-order placement after II.2.15.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-17
---

::: {.problem}
Let $X$ be a scheme, let $f \in \Gamma(X, \OO_X)$, and define $X_f$ to be the subset of points $x \in X$ such that the stalk $f_x$ of $f$ at $x$ is not contained in the maximal ideal $\mfm_x$ of the local ring $\OO_x$.

a. If $U = \Spec B$ is an open affine subscheme of $X$ and $\bar{f} \in B = \Gamma\qty{U, \ro{\OO_X}{U}}$ is the restriction of $f$, show that $U \intersect X_f = D(\bar{f})$.
Conclude that $X_f$ is an open subset of $X$.

b. Assume that $X$ is quasi-compact.
Let $A = \Gamma(X, \OO_X)$ and let $a \in A$ be an element whose restriction to $X_f$ is $0$.
Show that $f^n a = 0$ for some $n > 0$.
Use an open affine cover of $X$.

c. Now assume that $X$ has a finite cover by open affines $U_i$ such that each intersection $U_i \intersect U_j$ is quasi-compact.
This hypothesis is satisfied, for example, if $\operatorname{sp}(X)$ is noetherian.
Let $b \in \Gamma(X_f, \OO_{X_f})$.
Show that for some $n > 0$ the section $f^n b$ is the restriction of an element of $A$.

d. With the hypothesis of (c), conclude that $\Gamma(X_f, \OO_{X_f}) \cong A_f$.
:::

::: {.solution}

::: pf

::: {.pf-step #x-x-f-criterion-pointwise}
Let
\[
U=\operatorname{Spec}B\subseteq X
\]
be affine, and let
\[
\bar f=f|_U\in B.
\]
For a point $x\in U$ corresponding to a prime $\mathfrak p\subseteq B$,
\[
x\in X_f
\iff
\bar f\notin\mathfrak p.
\]

::: pf-proof
The local ring at $x$ is
\[
\mathcal O_{X,x}=B_{\mathfrak p}
\]
with maximal ideal
\[
\mathfrak m_x=\mathfrak pB_{\mathfrak p}.
\]
The germ $f_x$ is the image
\[
\bar f/1\in B_{\mathfrak p}.
\]
Now
\[
\bar f/1\in\mathfrak pB_{\mathfrak p}
\iff
\bar f\in\mathfrak p,
\]
because contraction of the localized prime is
\[
\mathfrak pB_{\mathfrak p}\cap B=\mathfrak p.
\]
Thus $f_x$ is a unit, equivalently is not in the maximal ideal, exactly when $\bar f\notin\mathfrak p$.
:::

:::

::: {.pf-step #u-cap-xf-equals-dfbar}
Therefore
\[
\boxed{U\cap X_f=D(\bar f).}
\]
In particular $X_f$ is open in $X$.

::: pf-proof
The first equality is the pointwise criterion in step [](#x-x-f-criterion-pointwise){.pf-ref}.  Distinguished opens are open in $U$, and the affine opens $U$ cover $X$.  Hence $X_f$ has open intersection with every member of an open cover of $X$, so $X_f$ is open.
:::

:::

::: {.pf-step #local-annihilator-exponents-exist}
Assume $X$ is quasi-compact.  Choose a finite affine open cover
\[
X=U_1\cup\cdots\cup U_r,
\qquad
U_i=\operatorname{Spec}B_i.
\]
Let
\[
f_i=f|_{U_i},
\qquad
a_i=a|_{U_i}.
\]
If $a|_{X_f}=0$, then for every $i$ there is an integer $n_i\ge0$ such that
\[
f_i^{n_i}a_i=0
\]
in $B_i$.

::: pf-proof
By step [](#u-cap-xf-equals-dfbar){.pf-ref},
\[
U_i\cap X_f=D(f_i).
\]
The hypothesis says
\[
a_i|_{D(f_i)}=0.
\]
Since
\[
\Gamma(D(f_i),\mathcal O_X)
=(B_i)_{f_i},
\]
this means
\[
\frac{a_i}{1}=0
\]
in $(B_i)_{f_i}$.  By the definition of localization, this is equivalent to
\[
f_i^{n_i}a_i=0
\]
for some $n_i\ge0$.
:::

:::

::: {.pf-step #f-n-a-zero-global}
Under the hypotheses of step [](#local-annihilator-exponents-exist){.pf-ref}, there is one integer $n>0$ such that
\[
\boxed{f^na=0\text{ in }\Gamma(X,\mathcal O_X).}
\]

::: pf-proof
Take
\[
n>\max_i n_i.
\]
Then on every $U_i$,
\[
(f^na)|_{U_i}
=f_i^na_i
=0.
\]
The $U_i$ cover $X$, so the sheaf uniqueness axiom gives
\[
f^na=0
\]
globally.
:::

:::

::: {.pf-step #local-lift-fn-b}
Now assume the hypotheses of part (c):
\[
X=U_1\cup\cdots\cup U_r
\]
with each $U_i$ affine and each intersection
\[
U_{ij}=U_i\cap U_j
\]
quasi-compact.  Let
\[
b\in\Gamma(X_f,\mathcal O_{X_f}).
\]
For every $i$ there is an integer $n_i\ge0$ and a section
\[
c_i\in\Gamma(U_i,\mathcal O_X)
\]
such that on
\[
U_i\cap X_f
\]
one has
\[
c_i=f^{n_i}b.
\]

::: pf-proof
Write
\[
U_i=\operatorname{Spec}B_i,
\qquad
f_i=f|_{U_i}.
\]
By step [](#u-cap-xf-equals-dfbar){.pf-ref},
\[
U_i\cap X_f=D(f_i),
\]
and hence
\[
\Gamma(U_i\cap X_f,\mathcal O_X)
=(B_i)_{f_i}.
\]
The restriction of $b$ to this distinguished open is some fraction
\[
\frac{a_i}{f_i^{n_i}}
\]
with $a_i\in B_i$.  Let $c_i$ be the section corresponding to $a_i$.  Then
\[
f^{n_i}b=c_i
\]
on $U_i\cap X_f$.
:::

:::

::: {.pf-step #uniform-exponent-n0}
After increasing the exponents in step [](#local-lift-fn-b){.pf-ref}, there is a single integer $n_0\ge0$ such that for every $i$ there is
\[
c_i\in\Gamma(U_i,\mathcal O_X)
\]
with
\[
\boxed{c_i=f^{n_0}b\text{ on }U_i\cap X_f.}
\]

::: pf-proof
Take
\[
n_0=\max_i n_i.
\]
Replace the section from step [](#local-lift-fn-b){.pf-ref} by
\[
c_i':=f_i^{\,n_0-n_i}c_i.
\]
On $U_i\cap X_f$,
\[
c_i'
=f^{n_0-n_i}f^{n_i}b
=f^{n_0}b.
\]
Rename $c_i'$ as $c_i$.
:::

:::

::: {.pf-step #dij-vanishes-on-xf}
On every overlap $U_{ij}$, the difference
\[
d_{ij}=c_i|_{U_{ij}}-c_j|_{U_{ij}}
\]
restricts to zero on
\[
(U_{ij})_f=U_{ij}\cap X_f.
\]

::: pf-proof
By step [](#uniform-exponent-n0){.pf-ref}, both restrictions agree with
\[
f^{n_0}b
\]
on the common open subset
\[
U_i\cap U_j\cap X_f.
\]
Hence their difference vanishes there.
:::

:::

::: {.pf-step #f-mij-annihilates-dij}
For every pair $(i,j)$ there is an integer $m_{ij}\ge0$ such that
\[
f^{m_{ij}}d_{ij}=0
\]
on $U_{ij}$.

::: pf-proof
The scheme $U_{ij}$ is quasi-compact by hypothesis.  Apply part (b), proved in steps [](#local-annihilator-exponents-exist){.pf-ref} and [](#f-n-a-zero-global){.pf-ref}, to the quasi-compact scheme $U_{ij}$, the global function
\[
f|_{U_{ij}},
\]
and the section $d_{ij}$.  Step [](#dij-vanishes-on-xf){.pf-ref} is exactly the hypothesis that $d_{ij}$ vanishes on its nonvanishing locus.  Therefore some power of $f$ annihilates $d_{ij}$.
:::

:::

::: {.pf-step #fm-ci-agree-on-overlaps}
There is a single integer $m\ge0$ such that the sections
\[
f^mc_i\in\Gamma(U_i,\mathcal O_X)
\]
agree on every pairwise overlap.

::: pf-proof
There are only finitely many pairs $(i,j)$.  Take
\[
m=\max_{i,j}m_{ij}.
\]
Then on $U_{ij}$,
\[
f^m(c_i-c_j)
=f^md_{ij}
=0.
\]
Thus
\[
f^mc_i=f^mc_j
\]
on every overlap.
:::

:::

::: {.pf-step #glued-section-a}
The sections in step [](#fm-ci-agree-on-overlaps){.pf-ref} glue to a global section
\[
a\in A=\Gamma(X,\mathcal O_X)
\]
such that
\[
\boxed{a|_{X_f}=f^{n_0+m}b.}
\]

::: pf-proof
By step [](#fm-ci-agree-on-overlaps){.pf-ref}, the sections $f^mc_i$ form a compatible family on the finite open cover $\{U_i\}$.  The sheaf gluing axiom gives a unique
\[
a\in\Gamma(X,\mathcal O_X)
\]
whose restriction to $U_i$ is $f^mc_i$.

On $U_i\cap X_f$, step [](#uniform-exponent-n0){.pf-ref} gives
\[
a
=f^mc_i
=f^mf^{n_0}b
=f^{n_0+m}b.
\]
The opens $U_i\cap X_f$ cover $X_f$, so the equality holds globally on $X_f$.
:::

:::

::: {.pf-step #fn-b-extends-to-global}
Thus for every
\[
b\in\Gamma(X_f,\mathcal O_{X_f})
\]
there is an integer $N>0$ such that
\[
\boxed{f^Nb\text{ extends to a section of }\Gamma(X,\mathcal O_X).}
\]

::: pf-proof
Take
\[
N>n_0+m
\]
and multiply the global extension in step [](#glued-section-a){.pf-ref} by the additional power of $f$ if necessary.  Equivalently, step [](#glued-section-a){.pf-ref} already gives the statement with exponent $n_0+m$, except in the harmless case that this exponent is zero; increasing it to a positive integer preserves extendability.
:::

:::

::: {.pf-step #x-quasicompact-under-c}
Under the hypotheses of part (c), $X$ is quasi-compact.

::: pf-proof
It has the finite open cover
\[
X=U_1\cup\cdots\cup U_r
\]
by affine schemes.  Each affine $U_i$ is quasi-compact, and a finite union of quasi-compact open subsets is quasi-compact.
:::

:::

::: {.pf-step #theta-well-defined}
Restriction induces a natural ring homomorphism
\[
\theta:A_f
\longrightarrow
\Gamma(X_f,\mathcal O_{X_f}),
\qquad
\frac a{f^r}
\longmapsto
\frac{a|_{X_f}}{(f|_{X_f})^r}.
\]

::: pf-proof
On $X_f$, the section $f$ is a unit in every stalk and hence is a unit of the sheaf of rings locally.  In fact its pointwise inverse glues uniquely, so
\[
f|_{X_f}
\]
is an invertible global section.  Therefore the restriction map
\[
A\to\Gamma(X_f,\mathcal O_{X_f})
\]
sends $f$ to a unit and factors uniquely through the localization $A_f$.
:::

:::

::: {.pf-step #theta-injective}
The homomorphism $\theta$ is injective.

::: pf-proof
Suppose
\[
\theta\left(\frac a{f^r}\right)=0.
\]
Since $f|_{X_f}$ is invertible, this implies
\[
a|_{X_f}=0.
\]
By step [](#x-quasicompact-under-c){.pf-ref}, $X$ is quasi-compact, so part (b), namely step [](#f-n-a-zero-global){.pf-ref}, gives an integer $n>0$ with
\[
f^na=0
\]
in $A$.  This is exactly the condition that
\[
\frac a{f^r}=0
\]
in the localization $A_f$.
:::

:::

::: {.pf-step #theta-surjective}
The homomorphism $\theta$ is surjective.

::: pf-proof
Let
\[
b\in\Gamma(X_f,\mathcal O_{X_f}).
\]
By step [](#fn-b-extends-to-global){.pf-ref}, there is an integer $n>0$ and a global section
\[
a\in A
\]
such that
\[
a|_{X_f}=f^nb.
\]
Since $f$ is invertible on $X_f$,
\[
b
=\frac{a|_{X_f}}{f^n}
=\theta\left(\frac a{f^n}\right).
\]
Thus every section lies in the image.
:::

:::

::: {.pf-step #gamma-xf-iso-af}
Consequently
\[
\boxed{
\Gamma(X_f,\mathcal O_{X_f})
\cong
A_f.
}
\]

::: pf-proof
The natural map $\theta$ from step [](#theta-well-defined){.pf-ref} is injective by step [](#theta-injective){.pf-ref} and surjective by step [](#theta-surjective){.pf-ref}.
:::

:::

::: pf-qed
Steps [](#x-x-f-criterion-pointwise){.pf-ref} and [](#u-cap-xf-equals-dfbar){.pf-ref} prove (a), steps [](#local-annihilator-exponents-exist){.pf-ref} and [](#f-n-a-zero-global){.pf-ref} prove (b), steps [](#local-lift-fn-b){.pf-ref}, [](#uniform-exponent-n0){.pf-ref}, [](#dij-vanishes-on-xf){.pf-ref}, [](#f-mij-annihilates-dij){.pf-ref}, [](#fm-ci-agree-on-overlaps){.pf-ref}, [](#glued-section-a){.pf-ref} and [](#fn-b-extends-to-global){.pf-ref} prove (c), and steps [](#x-quasicompact-under-c){.pf-ref}, [](#theta-well-defined){.pf-ref}, [](#theta-injective){.pf-ref}, [](#theta-surjective){.pf-ref} and [](#gamma-xf-iso-af){.pf-ref} prove (d).
:::

:::

:::
