---
schema: qual/card@1
id: P-AGH2711BLOWUPIDEAL
kind: problem
title: Ideal sheaves giving isomorphic blowings-up
classification:
  areas:
  - algebraic-geometry
  topics:
  - Blowing Up
  - Ideal Sheaves
  - Regular Schemes
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-17
  note: Compared all three parts with the retained Hartshorne II.7.11 transcription. Checked the blowup universal property and invertibility of the transformed ideal against Stacks Project Tags 0806 and 01OF. The proof removes the invertible common-divisor ideal using the double dual and identifies the resulting center with the entire non-isomorphism locus.
- event: solution-written
  by: chatgpt
  date: 2026-09-17
---

::: {.problem}
On a noetherian scheme $X$, different sheaves of ideals can give rise to isomorphic blown up schemes.

(a) If $\mci$ is any coherent sheaf of ideals on $X$, show that blowing up $\mci^d$ for any $d \geq 1$ gives a scheme isomorphic to the blowing up of $\mci$ (cf. Ex. 5.13).

(b) If $\mci$ is any coherent sheaf of ideals, and if $\mcj$ is an invertible sheaf of ideals, then $\mci$ and $\mci \cdot \mcj$ give isomorphic blowings-up.

(c) In the setting of Theorem II.7.17, assume that $X$ is regular.
Write the morphism there as $f:X'\to X$, with a blowup presentation $X'\cong\operatorname{Bl}_{\mci_0}X$ for a nonzero coherent ideal $\mci_0$ on the integral scheme $X$.
Let $U\subseteq X$ be the largest open set over which $f$ is an isomorphism.
Show that the ideal in a blowup presentation can be chosen so that its closed subscheme $Y$ has support exactly $X\setminus U$.
:::

::: {.solution}
For a coherent ideal $\mathcal I$, write
$$
\mathcal R(\mathcal I)=\bigoplus_{q\ge0}\mathcal I^q,
\qquad B(\mathcal I)=\operatorname{Proj}_X\mathcal R(\mathcal I).
$$
The degree-zero summand is $\OO_X$, and the grading distinguishes the different copies of powers of the ideal.
These are the [[D-SCHBLOWUP|Rees algebra and blowup]].
All isomorphisms of blowups below are over $X$.

<1>1. There is a canonical isomorphism $B(\mathcal I^d)\cong B(\mathcal I)$ for every $d\ge1$.

::: {.proof}
The Rees algebra of $\mathcal I^d$ is the $d$th Veronese algebra
$$
\mathcal R(\mathcal I^d)=\bigoplus_{q\ge0}\mathcal I^{dq}
=\mathcal R(\mathcal I)^{(d)},
$$
with the degrees divided by $d$.
Relative Proj is unchanged by this operation [@Har10a, Exercise II.5.13].

The local isomorphisms can be checked without assumptions on zero divisors.
On an affine open, let $R$ be the Rees algebra and let $f$ be a degree-one generator.
The natural map identifies the degree-zero rings
$$
(R^{(d)}[1/f^d])_0=(R[1/f])_0.
$$
Indeed, a degree-zero fraction $b/f^q$ on the right can be multiplied in numerator and denominator by a power of $f$ until the denominator exponent is divisible by $d$.
Its numerator then also has degree divisible by $d$, so it is a fraction on the left.
The equality criterion for fractions is the same on both sides, since a power of $f$ annihilates an element exactly when some power of $f^d$ does.
These charts cover the two Proj schemes and their identifications agree after further localization.
They also commute with restriction on $X$, so they glue to the required isomorphism.
If the positive-degree algebra is nilpotent, both Proj schemes are empty and the same assertion holds.
:::

<1>2. Multiplying by an invertible ideal $\mathcal J$ does not change the blowup.

::: {.proof}
Work on an open set where $\mathcal J$ has a generator $a$.
Because $\mathcal J\subseteq\OO_X$ is an invertible module, multiplication by $a$ identifies $\OO_X$ with this ideal; thus $a$ is a non-zero-divisor.
For every $q$, multiplication by $a^q$ is an isomorphism
$$
\mathcal I^q\longrightarrow(\mathcal I\mathcal J)^q.
$$
Together these maps form a graded algebra isomorphism, since the degree-$q$ and degree-$r$ factors multiply with coefficient $a^{q+r}$.
It induces a local isomorphism of the two blowups.

If $a$ is replaced by $ua$ for a unit $u$, the graded isomorphism is changed by multiplication by $u^q$ in degree $q$.
This change acts identically on Proj: in a degree-zero fraction, numerator and denominator have the same degree, and the powers of $u$ cancel.
Thus the local isomorphisms agree on overlaps and glue to $B(\mathcal I\mathcal J)\cong B(\mathcal I)$.
This proves (b) for the original noetherian scheme, without requiring it to be integral.
:::

<1>3. On the regular integral scheme in (c), the double dual $\mathcal J=\mathcal I_0^{\vee\vee}$ is an invertible ideal containing $\mathcal I_0$.

::: {.proof}
Duals are taken with respect to $\OO_X$.
The sheaves in question are coherent, and taking their duals commutes with localization because their modules are finitely presented on noetherian affine opens.
Fix a point $x$, put $R=\OO_{X,x}$ and $K=\operatorname{Frac}R$, and write $I=(\mathcal I_0)_x$.
The ring $R$ is a UFD because it is regular [@Har10a, Remark II.6.11.1A].
The ideal $I$ is nonzero, and its finite generating list has a greatest common divisor $g\ne0$, defined up to a unit.

Every $R$-linear map $I\to R$ is multiplication by an element of $K$.
For if $0\ne a\in I$ and $\lambda:I\to R$ is linear, then
$$
a\lambda(b)=\lambda(ab)=b\lambda(a)\qquad(b\in I),
$$
so $\lambda(b)=(\lambda(a)/a)b$.
Writing a multiplier as a relatively prime fraction in the UFD shows that its denominator must divide every generator of $I$, and hence must divide $g$.
Conversely, every multiplier in $g^{-1}R$ carries $I$ into $R$.
Therefore
$$
\Hom_R(I,R)=g^{-1}R,
\qquad I^{\vee\vee}=gR\subseteq R.
$$
Under these identifications the natural double-dual map is the inclusion $I\subseteq gR$.

The double dual of the inclusion $\mathcal I_0\hookrightarrow\OO_X$ consequently embeds $\mathcal J$ into $\OO_X$ at every stalk.
Every stalk of $\mathcal J$ is free of rank one.
For a coherent sheaf, a stalk basis extends to a basis on a neighborhood: extend the generator, and shrink until the coherent kernel and cokernel of the resulting map from $\OO_X$ vanish.
Thus $\mathcal J$ is an invertible ideal with the stated inclusion.
:::

<1>4. Define the coherent ideal
$$
\boxed{\mathcal K\coloneqq\mathcal I_0\otimes\mathcal J^{-1}\subseteq\OO_X,
\qquad\mathcal J=\mathcal I_0^{\vee\vee}.}
$$
Then $B(\mathcal K)\cong X'$, and $\mathcal K_x=\OO_{X,x}$ exactly when $(\mathcal I_0)_x$ is principal.

::: {.proof}
Tensor the inclusion $\mathcal I_0\subseteq\mathcal J$ with the invertible sheaf $\mathcal J^{-1}$.
This gives the displayed ideal inclusion.
At the point considered in step <1>3, its stalk is $g^{-1}I\subseteq R$, and multiplication gives $\mathcal K\mathcal J=\mathcal I_0$ globally.
Part (b), proved in step <1>2, therefore identifies $B(\mathcal K)$ with $B(\mathcal I_0)=X'$.

If $I$ is principal, its generator is a greatest common divisor of its generators, so $I=gR$ and $g^{-1}I=R$.
Conversely, $g^{-1}I=R$ implies $I=gR$, which is principal.
Since $R$ is a domain and $I\ne0$, being principal here is equivalent to being an invertible ideal at the stalk.
:::

<1>5. The non-isomorphism locus of $f$ is exactly $V(\mathcal K)$.

::: {.proof}
Where $\mathcal I_0$ is invertible, its blowup is the identity: locally its Rees algebra is $R[T]$, with the generator of the ideal corresponding to $T$ in degree one, and $\operatorname{Proj}R[T]=\Spec R$.
Thus its invertibility locus is contained in $U$.

Conversely, the extended ideal $\mathcal I_0\OO_{X'}$ on its blowup is invertible.
On an affine blowup chart $R[I/a]\subseteq\operatorname{Frac}R$, with $0\ne a\in I$, the extended ideal is $IR[I/a]=aR[I/a]$.
The generator $a$ is nonzero in this domain, so it identifies the ideal with a free module of rank one.
These charts cover the blowup, proving the assertion.
Over an open set where $f$ is an isomorphism, this identifies $\mathcal I_0$ itself with an invertible ideal.
Consequently $U$ is precisely the invertibility locus of $\mathcal I_0$.
Invertibility at a stalk extends to a neighborhood by coherence, so this also proves the equality pointwise.

Step <1>4 now gives
$$
x\in U\quad\Longleftrightarrow\quad\mathcal K_x=\OO_{X,x}
\quad\Longleftrightarrow\quad x\notin\operatorname{Supp}(\OO_X/\mathcal K).
$$
The closed subscheme $Y$ defined by $\mathcal K$ therefore has support exactly $X\setminus U$, while its blowup is $X'$.
This is the required strengthening of the blowup presentation in (c).
:::

<1>6. Q.E.D.

::: {.proof}
Step <1>1 proves (a), step <1>2 proves (b), and steps <1>3--<1>5 construct the ideal and prove the exact support assertion in (c).
:::
:::
