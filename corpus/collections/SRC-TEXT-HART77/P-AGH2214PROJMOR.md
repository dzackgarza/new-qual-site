---
schema: qual/card@1
id: P-AGH2214PROJMOR
kind: problem
title: Graded ring homomorphisms induce morphisms of Proj
classification:
  areas:
  - algebraic-geometry
  topics:
  - Proj
  - Graded Rings
  - Projective Varieties
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-17
  note: Checked against the collection's Hartshorne II.2.14 statement and source-order placement after II.2.13.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-17
---

::: {.problem}
a. Let $S$ be a graded ring.
Show that $\Proj S = \varnothing$ if and only if every element of $S_{+}$ is nilpotent.

b. Let $\phi: S \to T$ be a graded homomorphism of graded rings, preserving degrees.
Let $U = \ts{\mfp \in \Proj T \st \mfp \not\supseteq \phi(S_+)}$.
Show that $U$ is an open subset of $\Proj T$, and show that $\phi$ determines a natural morphism $f: U \to \Proj S$.

c. The morphism $f$ can be an isomorphism even when $\phi$ is not.
For example, suppose that $\phi_d: S_d \to T_d$ is an isomorphism for all $d \geq d_0$, where $d_0$ is an integer.
Then show that $U = \Proj T$ and the morphism $f: \Proj T \to \Proj S$ is an isomorphism.

d. Let $V$ be a projective variety with homogeneous coordinate ring $S$.
Show that $t(V) \cong \Proj S$.
:::

::: {.solution}
Write
\[
S_+=\bigoplus_{d>0}S_d
\]
for the irrelevant ideal.

::: pf

::: {.pf-step #nilpotent-implies-proj-empty}
If every element of $S_+$ is nilpotent, then
\[
\Proj S=\varnothing.
\]

::: pf-proof
Every prime ideal contains every nilpotent element.
Hence every homogeneous prime ideal contains all of $S_+$.
But by definition
\[
\Proj S
=\{\mathfrak p:\mathfrak p\text{ homogeneous prime and }\mathfrak p\not\supseteq S_+\}.
\]
Thus no prime belongs to $\Proj S$.
:::

:::

::: {.pf-step #proj-empty-implies-homog-nilpotent}
Conversely, if
\[
\Proj S=\varnothing,
\]
then every homogeneous element of positive degree is nilpotent.

::: pf-proof
Let
\[
f\in S_d,
\qquad d>0,
\]
be homogeneous.
Suppose $f$ is not nilpotent.

Consider the set of homogeneous ideals $I\subseteq S$ such that
\[
I\cap\{1,f,f^2,\ldots\}=\varnothing.
\]
It is nonempty because $(0)$ belongs to it, and the union of any chain is again a homogeneous ideal disjoint from the powers of $f$.
By Zorn's lemma there is a maximal such homogeneous ideal $\mathfrak p$.

We claim $\mathfrak p$ is prime.
Let $a,b$ be homogeneous elements not in $\mathfrak p$.
By maximality, the homogeneous ideals
\[
\mathfrak p+(a)
\qquad\text{and}\qquad
\mathfrak p+(b)
\]
each meet the powers of $f$.
Thus for some $m,n$,
\[
f^m=p_1+ra,
\qquad
f^n=p_2+sb
\]
with $p_1,p_2\in\mathfrak p$.
Multiplying gives
\[
f^{m+n}
\in
\mathfrak p+(ab).
\]
If $ab\in\mathfrak p$, this would put $f^{m+n}$ in $\mathfrak p$, contradiction.
Hence
\[
ab\notin\mathfrak p.
\]
So the complement of $\mathfrak p$ is multiplicatively closed on homogeneous elements, which is the homogeneous-prime criterion.

Since
\[
f\notin\mathfrak p
\]
and $f\in S_+$, the prime $\mathfrak p$ does not contain $S_+$.
Hence
\[
\mathfrak p\in\Proj S,
\]
contradiction.
Therefore every homogeneous positive-degree element is nilpotent.
:::

:::

::: {.pf-step #homog-nilpotent-implies-nilpotent}
If every homogeneous element of $S_+$ is nilpotent, then every element of $S_+$ is nilpotent.

::: pf-proof
Every element
\[
s\in S_+
\]
is a finite sum of homogeneous positive-degree components:
\[
s=s_{d_1}+\cdots+s_{d_r}.
\]
Each $s_{d_i}$ is nilpotent by hypothesis.
The nilpotent elements of a commutative ring form the nilradical, which is an ideal, so their finite sum is nilpotent.
Hence $s$ is nilpotent.
:::

:::

::: {.pf-step #proj-empty-iff-splus-nilpotent}
Therefore
\[
\boxed{
\Proj S=\varnothing
\iff
\text{every element of }S_+\text{ is nilpotent}.
}
\]

::: pf-proof
The forward implication is steps [](#proj-empty-implies-homog-nilpotent){.pf-ref} and [](#homog-nilpotent-implies-nilpotent){.pf-ref} and the reverse implication is step [](#nilpotent-implies-proj-empty){.pf-ref}.
:::

:::

::: {.pf-step #u-is-open-union-of-dplus}
Let
\[
\phi:S\longrightarrow T
\]
be a degree-preserving graded homomorphism and put
\[
U
=
\{\mathfrak p\in\Proj T:\mathfrak p\not\supseteq\phi(S_+)\}.
\]
Then
\[
\boxed{
U
=
\bigcup_{\substack{s\in S_+\\s\text{ homogeneous}}}
D_+(\phi(s)),
}
\]
so $U$ is open in $\Proj T$.

::: pf-proof
A homogeneous prime $\mathfrak p\in\Proj T$ fails to contain the ideal $\phi(S_+)$ exactly when there is some homogeneous positive-degree element
\[
s\in S_+
\]
with
\[
\phi(s)\notin\mathfrak p.
\]
That is exactly the condition
\[
\mathfrak p\in D_+(\phi(s)).
\]
Taking the union over all such $s$ gives the formula.
:::

:::

::: {.pf-step #f-of-p-in-proj-s}
For $\mathfrak p\in U$, define
\[
f(\mathfrak p)=\phi^{-1}(\mathfrak p).
\]
Then
\[
f(\mathfrak p)\in\Proj S.
\]

::: pf-proof
The inverse image of a prime ideal under a ring homomorphism is prime, and because $\phi$ preserves degrees, the inverse image of a homogeneous ideal is homogeneous.
Thus
\[
\phi^{-1}(\mathfrak p)
\]
is a homogeneous prime ideal of $S$.

Since $\mathfrak p\in U$, some
\[
s\in S_+
\]
satisfies
\[
\phi(s)\notin\mathfrak p.
\]
Hence
\[
s\notin\phi^{-1}(\mathfrak p),
\]
so the inverse-image prime does not contain $S_+$.
Therefore it belongs to $\Proj S$.
:::

:::

::: {.pf-step #f-continuous-preimage-formula}
The map of points
\[
f:U\longrightarrow\Proj S
\]
is continuous, and for homogeneous $s\in S_+$,
\[
\boxed{
f^{-1}(D_+(s))
=D_+(\phi(s)).
}
\]

::: pf-proof
For $\mathfrak p\in U$,
\[
\begin{aligned}
f(\mathfrak p)\in D_+(s)
&\iff
s\notin\phi^{-1}(\mathfrak p)\\
&\iff
\phi(s)\notin\mathfrak p\\
&\iff
\mathfrak p\in D_+(\phi(s)).
\end{aligned}
\]
The distinguished opens form a basis of $\Proj S$, so this identity proves continuity.
:::

:::

::: {.pf-step #localization-map-s-to-t}
On the distinguished opens from step [](#f-continuous-preimage-formula){.pf-ref}, the homomorphism $\phi$ induces degree-zero localization maps
\[
\boxed{
S_{(s)}
\longrightarrow
T_{(\phi(s))}.
}
\]

::: pf-proof
Because $\phi$ is graded and
\[
\phi(s)
\]
is inverted in $T_{\phi(s)}$, the universal property of localization gives a graded homomorphism
\[
S_s\longrightarrow T_{\phi(s)}.
\]
It preserves degrees, so it restricts to the degree-zero parts
\[
(S_s)_0=S_{(s)}
\longrightarrow
(T_{\phi(s)})_0=T_{(\phi(s))}.
\]
:::

:::

::: {.pf-step #f-glues-to-morphism}
The affine morphisms
\[
D_+(\phi(s))
=\Spec T_{(\phi(s))}
\longrightarrow
\Spec S_{(s)}
=D_+(s)
\]
from step [](#localization-map-s-to-t){.pf-ref} agree on overlaps and glue to a morphism of schemes
\[
\boxed{
f:U\longrightarrow\Proj S.
}
\]

::: pf-proof
The affine morphism is the one induced by the ring map in step [](#localization-map-s-to-t){.pf-ref}. On points it is contraction of primes, hence agrees with the set map in step [](#f-of-p-in-proj-s){.pf-ref}.

If $s,t\in S_+$ are homogeneous, then on the overlap
\[
D_+(\phi(s))\cap D_+(\phi(t))
=D_+(\phi(st))
\]
both local morphisms are obtained from the same graded homomorphism $\phi$ after localizing further by $st$.
Hence they agree.
Since the opens $D_+(\phi(s))$ cover $U$ by step [](#u-is-open-union-of-dplus){.pf-ref}, they glue uniquely to the desired scheme morphism.
:::

:::

::: {.pf-step #u-equals-proj-t}
Suppose now that there is an integer $d_0$ such that
\[
\phi_d:S_d\xrightarrow{\sim}T_d
\]
for every $d\ge d_0$.
Then
\[
\boxed{U=\Proj T.}
\]

::: pf-proof
Suppose
\[
\mathfrak p\in\Proj T
\]
contained $\phi(S_+)$.
Then for every
\[
d\ge\max(d_0,1),
\]
the isomorphism
\[
\phi_d:S_d\to T_d
\]
would give
\[
T_d=\phi(S_d)\subseteq\mathfrak p.
\]

Let
\[
t\in T_n,
\qquad n>0,
\]
be homogeneous.
Choose $m$ large enough that
\[
mn\ge d_0.
\]
Then
\[
t^m\in T_{mn}\subseteq\mathfrak p.
\]
Since $\mathfrak p$ is prime,
\[
t\in\mathfrak p.
\]
Thus
\[
T_+\subseteq\mathfrak p,
\]
contradicting
\[
\mathfrak p\in\Proj T.
\]
Therefore no point of $\Proj T$ is excluded from $U$.
:::

:::

::: {.pf-step #localization-map-iso}
Let $s\in S$ be homogeneous of positive degree and assume
\[
\deg s\ge d_0.
\]
Then the map
\[
\boxed{
S_{(s)}
\xrightarrow{\sim}
T_{(\phi(s))}
}
\]
from step [](#localization-map-s-to-t){.pf-ref} is an isomorphism.

::: pf-proof
Put
\[
r=\deg s.
\]

For surjectivity, take a homogeneous degree-zero fraction
\[
\frac{t}{\phi(s)^n}
\in T_{(\phi(s))},
\qquad
t\in T_{nr}.
\]
Choose $N\ge0$ such that
\[
(n+N)r\ge d_0.
\]
Then
\[
t\phi(s)^N
\in T_{(n+N)r}.
\]
Since $\phi_{(n+N)r}$ is surjective, there exists
\[
a\in S_{(n+N)r}
\]
with
\[
\phi(a)=t\phi(s)^N.
\]
Hence
\[
\frac{t}{\phi(s)^n}
=
\frac{\phi(a)}{\phi(s)^{n+N}},
\]
the image of
\[
\frac a{s^{n+N}}\in S_{(s)}.
\]

For injectivity, suppose
\[
\frac a{s^n}\in S_{(s)}
\]
maps to zero.
Then for some $m\ge0$,
\[
\phi(s)^m\phi(a)=0
\]
in $T$.
Choose $N$ so large that
\[
\deg(s^{m+N}a)\ge d_0.
\]
Then
\[
\phi(s^{m+N}a)=0.
\]
Since $\phi$ is injective in that degree,
\[
s^{m+N}a=0.
\]
Thus
\[
\frac a{s^n}=0
\]
in the localization.
Hence the map is injective.
:::

:::

::: {.pf-step #dplus-s-cover-proj-s}
The opens
\[
D_+(s),
\qquad
s\in S_+\text{ homogeneous},
\quad
\deg s\ge d_0,
\]
cover $\Proj S$.

::: pf-proof
Let
\[
\mathfrak q\in\Proj S.
\]
Choose a homogeneous positive-degree element
\[
a\in S_+
\]
with
\[
a\notin\mathfrak q.
\]
Some power
\[
s=a^N
\]
has degree at least $d_0$.
Since $\mathfrak q$ is prime and $a\notin\mathfrak q$,
\[
s\notin\mathfrak q.
\]
Thus
\[
\mathfrak q\in D_+(s).
\]
:::

:::

::: {.pf-step #f-is-isomorphism}
Under the eventual degreewise-isomorphism hypothesis, the morphism
\[
f:\Proj T\longrightarrow\Proj S
\]
is an isomorphism.

::: pf-proof
By step [](#u-equals-proj-t){.pf-ref} the domain $U$ is all of $\Proj T$.

The opens in step [](#dplus-s-cover-proj-s){.pf-ref} cover $\Proj S$, and their inverse images are
\[
D_+(\phi(s))
\]
by step [](#f-continuous-preimage-formula){.pf-ref}. On every such pair, step [](#localization-map-iso){.pf-ref} shows that the defining ring map
\[
S_{(s)}\to T_{(\phi(s))}
\]
is an isomorphism.
Hence
\[
D_+(\phi(s))
\xrightarrow{\sim}
D_+(s)
\]
is an isomorphism of affine schemes.

Thus $f$ is an isomorphism on an open cover of the target and the corresponding inverse-image cover of the source.
The local inverses agree on overlaps, so they glue to a global inverse.
Therefore $f$ is an isomorphism.
:::

:::

::: {.pf-step #affine-coord-ring-of-vi}
Let $V\subseteq\mathbb P^n_k$ be a projective variety with homogeneous coordinate ring
\[
S=k[x_0,\ldots,x_n]/I(V).
\]
The standard open subsets
\[
V_i=V\cap\{x_i\ne0\}
\]
have affine coordinate rings
\[
\boxed{
\Gamma(V_i,\mathcal O_V)
\cong
S_{(x_i)}.
}
\]

::: pf-proof
Dehomogenizing with respect to $x_i$ identifies the affine variety $V_i$ with the zero set of the dehomogenized equations of $I(V)$ in the affine chart
\[
\{x_i\ne0\}\cong\mathbb A^n.
\]
Its coordinate ring is precisely the degree-zero part of the localization
\[
S_{x_i},
\]
namely $S_{(x_i)}$.
:::

:::

::: {.pf-step #dplus-xi-matches-vi}
The standard affine opens of $\Proj S$ are
\[
D_+(x_i)
\cong
\Spec S_{(x_i)}.
\]
Under the affine identification of step [](#affine-coord-ring-of-vi){.pf-ref}, they are exactly the schemes associated to the affine varieties $V_i$.

::: pf-proof
The standard theorem on $\Proj$ gives
\[
D_+(x_i)=\Spec S_{(x_i)}.
\]
Step [](#affine-coord-ring-of-vi){.pf-ref} gives the same affine coordinate ring for $V_i$.
Hence the scheme associated to $V_i$ is naturally isomorphic to this standard open of $\Proj S$.
:::

:::

::: {.pf-step #tv-iso-proj-s}
These local isomorphisms agree on overlaps, and therefore
\[
\boxed{t(V)\cong\Proj S.}
\]

::: pf-proof
On
\[
V_i\cap V_j,
\]
the transition from one affine chart to the other is obtained by further localizing the homogeneous coordinate ring by $x_ix_j$ and taking degree zero.
The same localization is the overlap
\[
D_+(x_i)\cap D_+(x_j)
=D_+(x_ix_j)
\]
inside $\Proj S$.

Thus the affine identifications from step [](#dplus-xi-matches-vi){.pf-ref} commute with the overlap identifications.
The associated scheme $t(V)$ is obtained by gluing the affine schemes of the $V_i$ by these transition maps, while $\Proj S$ is obtained by gluing the same affine schemes by the same maps.
The local isomorphisms therefore glue to the displayed global isomorphism.
:::

:::

::: pf-qed
Steps [](#nilpotent-implies-proj-empty){.pf-ref}, [](#proj-empty-implies-homog-nilpotent){.pf-ref}, [](#homog-nilpotent-implies-nilpotent){.pf-ref} and [](#proj-empty-iff-splus-nilpotent){.pf-ref} prove part (a), steps [](#u-is-open-union-of-dplus){.pf-ref}, [](#f-of-p-in-proj-s){.pf-ref}, [](#f-continuous-preimage-formula){.pf-ref}, [](#localization-map-s-to-t){.pf-ref} and [](#f-glues-to-morphism){.pf-ref} prove part (b), steps [](#u-equals-proj-t){.pf-ref}, [](#localization-map-iso){.pf-ref}, [](#dplus-s-cover-proj-s){.pf-ref} and [](#f-is-isomorphism){.pf-ref} prove part (c), and steps [](#affine-coord-ring-of-vi){.pf-ref}, [](#dplus-xi-matches-vi){.pf-ref} and [](#tv-iso-proj-s){.pf-ref} prove part (d).
:::

:::

:::
