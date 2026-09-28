---
schema: qual/card@1
id: P-AGH2611KCURVE
kind: problem
title: The Grothendieck group of a nonsingular curve
classification:
  areas:
  - algebraic-geometry
  topics:
  - Grothendieck Groups
  - Picard Groups
  - Determinant of a Sheaf
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-17
  note: Compared all four parts with the retained Hartshorne II.6.11 transcription. Proved the divisor-class formula for positive and negative divisors, constructed resolutions also for noncomplete curves, and proved determinant independence by fiber products and additivity by compatible kernel resolutions rather than assuming that vector bundles are globally projective objects.
- event: solution-written
  by: chatgpt
  date: 2026-09-17
---

::: {.problem}
Let $X$ be a nonsingular curve over an algebraically closed field $k$.
We show that $K(X) \cong \Pic X \oplus \ZZ$ in several steps.

(a) For any divisor $D = \sum n_i P_i$ on $X$, let $\psi(D) = \sum n_i \gamma(k(P_i)) \in K(X)$, where $k(P_i)$ is the skyscraper sheaf $k$ at $P_i$ and $0$ elsewhere.
    If $D$ is an effective divisor, let $\OO_D$ be the structure sheaf of the associated subscheme of codimension $1$, and show that $\psi(D) = \gamma(\OO_D)$.
    Then use (6.18) to show that for any $D$, $\psi(D)$ depends only on the linear equivalence class of $D$, so $\psi$ defines a homomorphism $\psi: \Cl X \to K(X)$.

(b) For any coherent sheaf $\mcf$ on $X$, show that there exist locally free sheaves $\mce_0$ and $\mce_1$ and an exact sequence $0 \to \mce_1 \to \mce_0 \to \mcf \to 0$.
   Let $r_0 = \rank \mce_0$, $r_1 = \rank \mce_1$, and define
$$
\det \mcf = \left(\bigwedge\nolimits^{r_0} \mce_0\right) \tensor \inverseof{\left(\bigwedge\nolimits^{r_1} \mce_1\right)} \in \Pic X
.
$$
   Here $\bigwedge$ denotes the exterior power (Ex. 5.16).
   Show that $\det \mcf$ is independent of the resolution chosen, and that it gives a homomorphism $\det: K(X) \to \Pic X$.
   Finally show that if $D$ is a divisor then $\det(\psi(D)) = \mcl(D)$.

(c) If $\mcf$ is any coherent sheaf of rank $r$, show that there is a divisor $D$ on $X$ and an exact sequence
$$
0 \to \mcl(D)^{\oplus r} \to \mcf \to \mct \to 0,
$$
   where $\mct$ is a torsion sheaf.
   Conclude that if $\mcf$ has rank $r$ then $\gamma(\mcf) - r\gamma(\OO_X) \in \im \psi$.

(d) Using the maps $\psi$, $\det$, $\rank$, and $1 \mapsto \gamma(\OO_X)$ from $\ZZ \to K(X)$, show that $K(X) \cong \Pic X \oplus \ZZ$.
:::

::: {.solution}
Write $\OO_X(D)=\mathcal L(D)$ and use the [[D-5PQ5W|isomorphism]] $\Cl(X)\cong\Pic(X)$, $[D]\mapsto[\OO_X(D)]$ [@Har10a, Corollary II.6.16].
The group $K(X)$ is the coherent-sheaf Grothendieck group of [[P-AGH2610KGROUP]], with rank defined at the generic point $\eta$.
For a finite-rank vector bundle $\mathcal E$, its [[D-MODCONORM|determinant]] is $\bigwedge^{\rank\mathcal E}\mathcal E$, including $\det(0)=\OO_X$.

<1>1. If $\mathcal T$ is a coherent torsion sheaf, then
$$
\gamma(\mathcal T)=\sum_{P\in X}\operatorname{length}_{\OO_{X,P}}(\mathcal T_P)\,\gamma(k(P)).
$$
In particular, $\psi(D)=\gamma(\OO_D)$ for an effective divisor $D$.

::: {.proof}
The support of $\mathcal T$ is closed and does not contain the generic point, so it is a finite set of closed points.
Its annihilator defines a zero-dimensional closed subscheme of the noetherian curve.
This subscheme is a finite disjoint union of spectra of artinian local rings, so $\mathcal T$ has a finite composition series whose simple quotients are the skyscraper sheaves $k(P)$.
Taking a stalk shows that $k(P)$ occurs exactly $\operatorname{length}(\mathcal T_P)$ times.
The defining short-exact-sequence relations give the displayed equality.

For $D=\sum_P n_P P$ effective, the local ring of $D$ at $P$ is
$$
\OO_{D,P}=\OO_{X,P}/(\pi_P^{n_P}),
$$
where $\pi_P$ is a uniformizer of the DVR $\OO_{X,P}$.
The filtration by powers of $\pi_P$ has $n_P$ successive residue-field quotients, so its length is $n_P$.
Applying the torsion formula proves the assertion for $\OO_D$.
:::

<1>2. For every divisor $D$, including divisors with negative coefficients,
$$
\psi(D)=\gamma(\OO_X(D))-\gamma(\OO_X).
$$
Consequently $\psi$ descends to a homomorphism $\Cl(X)\to K(X)$.

::: {.proof}
For any divisor $E$ and closed point $P$, tensor the sequence
$$
0\longrightarrow\OO_X(-P)\longrightarrow\OO_X\longrightarrow k(P)\longrightarrow0
$$
from [@Har10a, Proposition II.6.18] with the invertible sheaf $\OO_X(E)$.
It remains exact, and its last term is isomorphic to $k(P)$, giving
$$
\gamma(\OO_X(E))-\gamma(\OO_X(E-P))=\gamma(k(P)).
$$
Starting at the zero divisor, add or subtract points with the multiplicities in $D$.
This finite telescoping calculation proves the formula for every $D$.
Linearly equivalent divisors have isomorphic associated invertible sheaves, so the formula gives the same value on them.
Additivity on divisors follows from the definition of $\psi$, and hence passes to divisor classes.
:::

<1>3. Every coherent sheaf $\mathcal F$ has a resolution
$$
0\longrightarrow\mathcal E_1\longrightarrow\mathcal E_0\longrightarrow\mathcal F\longrightarrow0
$$
by vector bundles of finite rank, with $\mathcal E_0$ a finite direct sum of copies of one invertible sheaf.

::: {.proof}
A nonsingular curve is an open subcurve of a nonsingular projective curve $\overline X$ [@Har10a, Chapter I, §6].
Extend $\mathcal F$ to a coherent sheaf $\overline{\mathcal F}$ on $\overline X$ by [[P-AGH2515EXTCOH]], step <1>5. Choose a projective embedding of $\overline X$ and a hyperplane divisor $H$ for that embedding.
For sufficiently large $n\ge0$, the sheaf $\overline{\mathcal F}(nH)$ is generated by finitely many global sections [@Har10a, Theorem II.5.17].
Restricting the resulting surjection gives
$$
\mathcal E_0=\mathcal M^{\oplus N}\longrightarrow\mathcal F,
\qquad\mathcal M=\OO_{\overline X}(-nH)|_X.
$$
Let $\mathcal E_1$ be its kernel.
It is coherent and torsion-free as a subsheaf of $\mathcal E_0$.

A finite torsion-free module over a DVR is free, by the structure theorem for modules over a PID; the generic stalk is a vector space over a field.
Thus all stalks of $\mathcal E_1$ are free.
A basis at a stalk lifts to a morphism from a finite free sheaf on a neighborhood.
Its coherent kernel and cokernel vanish at that point, and therefore vanish after shrinking the neighborhood.
This proves local freeness of $\mathcal E_1$.
The same argument shows that every coherent torsion-free sheaf on $X$ is locally free.
:::

<1>4. The class $\det\mathcal F=[\det\mathcal E_0\otimes(\det\mathcal E_1)^{-1}]$ is independent of the resolution in step <1>3.

::: {.proof}
Suppose $0\to\mathcal E'_1\to\mathcal E'_0\to\mathcal F\to0$ is another vector-bundle resolution, and form the fiber product
$$
\mathcal G=\mathcal E_0\times_{\mathcal F}\mathcal E'_0.
$$
Its projections give short exact sequences
$$
0\to\mathcal E_1\to\mathcal G\to\mathcal E'_0\to0,
\qquad
0\to\mathcal E'_1\to\mathcal G\to\mathcal E_0\to0.
$$
They split locally because their quotient sheaves are locally free, so $\mathcal G$ is also a vector bundle.
The determinant identity for a short exact sequence of vector bundles, proved in [[P-AGH2516TENSOROPS]], step <1>4, gives
$$
\det\mathcal E_1\otimes\det\mathcal E'_0
\cong\det\mathcal G
\cong\det\mathcal E'_1\otimes\det\mathcal E_0.
$$
Rearranging in $\Pic(X)$ proves independence of the ratio defining $\det\mathcal F$.
For a vector bundle $\mathcal F$, the resolution with $\mathcal E_0=\mathcal F$ and $\mathcal E_1=0$ recovers its usual determinant.
:::

<1>5. Determinant is multiplicative in short exact sequences of coherent sheaves and induces a homomorphism $\det:K(X)\to\Pic(X)$.
For every divisor $D$, it satisfies $\det(\psi(D))=[\OO_X(D)]$.

::: {.proof}
Consider $0\to\mathcal F'\to\mathcal F\to\mathcal F''\to0$ and choose a resolution $0\to\mathcal E_1\to\mathcal E_0\to\mathcal F\to0$.
Let $\mathcal G$ be the inverse image of $\mathcal F'$ in $\mathcal E_0$.
It is a coherent torsion-free subsheaf of a vector bundle, so is locally free by step <1>3. The sequences
$$
0\to\mathcal E_1\to\mathcal G\to\mathcal F'\to0,
\qquad
0\to\mathcal G\to\mathcal E_0\to\mathcal F''\to0
$$
are vector-bundle resolutions.
Using step <1>4 to compute determinants with these particular resolutions yields
$$
\begin{aligned}
\det\mathcal F'\otimes\det\mathcal F''
&=[\det\mathcal G\otimes(\det\mathcal E_1)^{-1}
\otimes\det\mathcal E_0\otimes(\det\mathcal G)^{-1}]\\
&=[\det\mathcal E_0\otimes(\det\mathcal E_1)^{-1}]
=\det\mathcal F.
\end{aligned}
$$
Thus determinant respects the relations of $K(X)$.

The resolution $0\to\OO_X(-P)\to\OO_X\to k(P)\to0$ gives $\det k(P)=[\OO_X(P)]$.
Applying the homomorphism to $\psi(D)=\sum_P n_P\gamma(k(P))$ gives
$$
\det(\psi(D))=\left[\bigotimes_P\OO_X(P)^{\otimes n_P}\right]=[\OO_X(D)],
$$
also for negative coefficients.
:::

<1>6. Every coherent sheaf $\mathcal F$ of rank $r$ admits the exact sequence in part (c), and $\gamma(\mathcal F)-r\gamma(\OO_X)$ lies in $\im\psi$.

::: {.proof}
For $r=0$, take $D=0$ and $\mathcal T=\mathcal F$.
For $r>0$, use the surjection $\mathcal M^{\oplus N}\to\mathcal F$ from step <1>3. The images of its summands span the generic stalk of $\mathcal F$.
Choose $r$ summands whose images are a basis there.
The resulting morphism $\mathcal M^{\oplus r}\to\mathcal F$ is generically an isomorphism.
Its kernel is a coherent torsion subsheaf of a locally free sheaf, hence zero; its cokernel $\mathcal T$ has zero generic stalk, hence is torsion.
Writing $\mathcal M=\OO_X(D)$, with $D=-nH|_X$, gives
$$
0\to\OO_X(D)^{\oplus r}\to\mathcal F\to\mathcal T\to0.
$$
By steps <1>1 and <1>2,
$$
\gamma(\mathcal F)-r\gamma(\OO_X)
=r\psi(D)+\sum_P\operatorname{length}(\mathcal T_P)\,\psi(P),
$$
which belongs to $\im\psi$.
:::

<1>7. The required isomorphism and its inverse are
$$
\boxed{(\det,\rank):K(X)\xrightarrow{\cong}\Pic(X)\oplus\ZZ,}
\qquad
([\OO_X(D)],n)\longmapsto\psi(D)+n\gamma(\OO_X).
$$

::: {.proof}
Call the displayed inverse candidate $\Phi$.
It is well-defined and additive by step <1>2 and the identification $\Cl(X)\cong\Pic(X)$.
Step <1>5 gives $\det\psi(D)=[\OO_X(D)]$, and $\rank\psi(D)=0$ because skyscraper sheaves are torsion.
Also $\det\OO_X=[\OO_X]$ and $\rank\OO_X=1$.
Therefore $(\det,\rank)\circ\Phi$ is the identity.
Step <1>6 expresses every coherent-sheaf class as an element of $\im\Phi$, so $\Phi$ is surjective.
A surjective homomorphism with this left inverse is an isomorphism, and the displayed maps are mutual inverses.
:::

<1>8. Q.E.D.

::: {.proof}
Steps <1>1--<1>2 prove part (a), steps <1>3--<1>5 prove every assertion of part (b), step <1>6 proves part (c), and step <1>7 proves part (d).
:::
:::
