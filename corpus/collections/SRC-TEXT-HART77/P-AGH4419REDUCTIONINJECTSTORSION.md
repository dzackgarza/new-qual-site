---
schema: qual/card@1
id: P-AGH4419REDUCTIONINJECTSTORSION
kind: problem
title: Reduction mod $p$ injects the prime-to-$p$ torsion of $X(\QQ)$
classification:
  areas:
  - algebraic-geometry
  topics:
  - Elliptic Curves
  - Jacobians
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-18
  note: >-
    Read Hartshorne IV.4.19 in source order and reviewed the good-reduction
    argument against Milne, Abelian Varieties, Proposition 20.7. In
    particular, checked flatness and finiteness of multiplication by n,
    flatness of its kernel, and the prime-to-p etale specialization argument.
- event: solution-written
  by: chatgpt
  date: 2026-09-18
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-18
  note: >-
    Rechecked the finite-flat and finite-etale arguments fibre by fibre,
    the specialization equalizer argument over Z_(p), and the point counts
    at p=3,5 used to rule out torsion in Exercises IV.4.17 and IV.4.18.
---

::: {.problem}
Let $X, P_0$ be an elliptic curve defined over $\QQ$, represented as a curve in $\PP^2$ defined by an equation with integer coefficients.
Then $X$ can be considered as the fibre over the generic point of a scheme $\bar{X}$ over $\Spec \ZZ$.
Let $T \subseteq \Spec \ZZ$ be the open subset consisting of all primes $p \neq 2$ such that the fibre $X_{(p)}$ of $\bar{X}$ over $p$ is nonsingular.

- For any $n$, show that $n_X: X \to X$ is defined over $T$, and is a flat morphism.

- Show that the kernel of $n_X$ is also flat over $T$.

- Conclude that for any $p \in T$, the natural map $X(\QQ) \to X_{(p)}(\FF_p)$ induced on the groups of rational points, maps the $n$-torsion points of $X(\QQ)$ injectively into the torsion subgroup of $X_{(p)}(\FF_p)$, for any $(n, p)=1$.

By this method one can show easily that the groups $X(\QQ)$ in (Ex.
4.17) and (Ex.
4.18) are torsion-free.
:::

::: {.solution}
Write
$$
\mathcal E=\bar X\times_{\Spec\ZZ}T
$$
and let
$$
e:T\longrightarrow\mathcal E
$$
be the section extending the chosen origin $P_0$.  For an integer $n\ge1$,
write $[n]$ for multiplication by $n$ and
$$
\mathcal E[n]=\ker[n].
$$

<1>1. The smooth model $\mathcal E/T$ is an elliptic scheme, and
$$
\boxed{[n]:\mathcal E\longrightarrow\mathcal E}
$$
extends $n_X:X\to X$.

::: {.proof}
Over $T$ every fibre of the projective plane cubic $\bar X$ is nonsingular.
Thus $\mathcal E\to T$ is a smooth proper family of genus-one curves.  The
rational point $P_0$ extends uniquely to a section over $T$: locally at a
prime of $T$ this is the valuative criterion of properness, and uniqueness
follows from separatedness.  A smooth proper genus-one curve with a section
is an elliptic scheme, so its group law, inverse, and zero section are all
defined over $T$.

Multiplication by $n$ is obtained from the group law by repeated addition.
Hence it is a morphism over $T$, and its generic fibre is the original
multiplication map $n_X$.
:::

<1>2. The morphism
$$
\boxed{[n]:\mathcal E\longrightarrow\mathcal E}
$$
is finite and flat over $T$.

::: {.proof}
For every point $s\in T$, the fibre $\mathcal E_s$ is an elliptic curve.
By [[P-AGH447DUALOFAMORPHISM|Exercise IV.4.7(e)]],
$$
\deg[n]_{\mathcal E_s}=n^2.
$$
Thus $[n]_{\mathcal E_s}$ is a nonconstant finite morphism of nonsingular
curves.  Such a morphism is flat: on local rings it gives a finite
torsion-free module over a discrete valuation ring, hence a free module.

The source $\mathcal E$ is flat over $T$.  The fibrewise flatness criterion
therefore shows that $[n]$ itself is flat.  It is also proper because
$\mathcal E$ is proper over $T$ and the target is separated over $T$.
Every fibre of $[n]$ is finite, so $[n]$ is quasi-finite.  A proper
quasi-finite morphism is finite.  Hence $[n]$ is finite and flat.
:::

<1>3. The kernel
$$
\boxed{\mathcal E[n]\longrightarrow T}
$$
is finite and flat.

::: {.proof}
By definition,
$$
\mathcal E[n]
=
T\times_{e,\mathcal E,[n]}\mathcal E.
$$
Thus $\mathcal E[n]\to T$ is the base change of the finite flat morphism
$[n]$ from step <1>2 along the zero section.  Finiteness and flatness are
preserved by base change.
:::

<1>4. Fix $p\in T$ with $(n,p)=1$.  After base change to
$$
S=\Spec\ZZ_{(p)},
$$
the group scheme $\mathcal E[n]_S$ is finite etale over $S$.

::: {.proof}
Since $p\nmid n$, the integer $n$ is a unit on $S$.  The differential of
$[n]$ on the relative tangent line at the identity is multiplication by
$n$, hence is an isomorphism.  Translation by a section identifies the
differential at any point with the differential at the identity, so $[n]$
is unramified over $S$.  Step <1>2 says that it is finite flat.  Therefore
$[n]$ is finite etale over $S$.

The kernel $\mathcal E[n]_S$ is its base change along the zero section, so
it is finite etale over $S$ as well.
:::

<1>5. For every $p\in T$ and every $n$ prime to $p$, reduction induces an
injection
$$
\boxed{
X(\QQ)[n]\hookrightarrow X_{(p)}(\FF_p)[n].
}
$$

::: {.proof}
Again put $S=\Spec\ZZ_{(p)}$.  A point
$$
P\in X(\QQ)[n]
$$
extends uniquely, by properness, to a section
$$
s_P:S\longrightarrow\mathcal E_S.
$$
The two sections $[n]\circ s_P$ and $e$ agree on the generic point of
$S$.  Since $\mathcal E_S$ is separated, they agree on all of $S$.
Hence $s_P$ factors through the finite etale group scheme
$\mathcal E[n]_S$ of step <1>4.

Suppose $P,Q\in X(\QQ)[n]$ have the same reduction modulo $p$.  Then the
corresponding sections
$$
s_P,s_Q:S\longrightarrow\mathcal E[n]_S
$$
agree at the closed point.  Because $\mathcal E[n]_S\to S$ is etale, its
diagonal is open; because it is separated, its diagonal is closed.  Thus the
equalizer of $s_P$ and $s_Q$ is both open and closed in the connected scheme
$S$.  It contains the closed point, so it is all of $S$.  Therefore
$s_P=s_Q$, and in particular $P=Q$ on the generic fibre.

Reduction is a homomorphism because it is induced by the group scheme
$\mathcal E_S$.  Hence it injects $X(\QQ)[n]$ into the $n$-torsion of
$X_{(p)}(\FF_p)$, proving the required assertion.
:::

<1>6. The groups of rational points in Exercises IV.4.17 and IV.4.18 are
torsion-free.

::: {.proof}
First consider
$$
E_{17}:y^2+y=x^3-x.
$$
By [[P-AGH4417MULTIPLESOFAPOINT|Exercise IV.4.17]], its discriminant is
$37$, so it has good reduction at $3$ and $5$.  Direct enumeration gives
$$
\#E_{17}(\FF_3)=7,
\qquad
\#E_{17}(\FF_5)=8.
$$
Indeed, for $x=0,1,2$ over $\FF_3$ the numbers of affine $y$-solutions are
$2,2,2$, while over $\FF_5$ for $x=0,1,2,3,4$ they are
$2,2,1,0,2$; in each case one then adds the point at infinity.

Now consider
$$
E_{18}:y^2=x^3-7x+10.
$$
Its discriminant is
$$
-16\bigl(4(-7)^3+27(10)^2\bigr)
=-2^8\cdot83,
$$
so again $3$ and $5$ are primes of good reduction.  Direct enumeration gives
$$
\#E_{18}(\FF_3)=7,
\qquad
\#E_{18}(\FF_5)=10.
$$
For $x=0,1,2$ over $\FF_3$ the numbers of affine $y$-solutions are
$2,2,2$, while over $\FF_5$ for $x=0,1,2,3,4$ they are
$1,2,2,2,2$.

Suppose either rational group had nonzero torsion.  Then it would contain a
point of some prime order $\ell$.  If $\ell\ne3,5$, step <1>5 at both
primes would force $\ell$ to divide both displayed group orders, impossible
because
$$
\gcd(7,8)=\gcd(7,10)=1.
$$
If $\ell=3$, reduction at $5$ would force $3$ to divide respectively $8$
or $10$, again impossible.  If $\ell=5$, reduction at $3$ would force
$5\mid7$, impossible.  Thus neither rational group contains a nonzero
torsion point.
:::

<1>7. Q.E.D.

::: {.proof}
Steps <1>1--<1>2 prove that multiplication by $n$ is defined and flat over
$T$, step <1>3 proves flatness of its kernel, step <1>5 proves the
prime-to-$p$ injectivity under reduction, and step <1>6 proves the stated
torsion-free applications.
:::
:::
