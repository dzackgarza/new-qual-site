---
schema: qual/card@1
id: P-AGH358ONEDIMPROJ
kind: problem
title: Every one-dimensional proper scheme is projective
classification:
  areas:
  - algebraic-geometry
  topics:
  - Proper Schemes
  - Projectivity
  - Curves
  - Picard Group
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-17
  note: Compared all four cases with the retained Hartshorne Chapter III section 5 transcription. The proof writes O(D) for the divisor-associated sheaf, descends a hyperplane divisor supported over the nonsingular locus, and proves both Picard surjectivity assertions using unit sheaves, including nonreduced intersections and nilpotent thickenings.
- event: solution-written
  by: chatgpt
  date: 2026-09-17
---

::: {.problem}
Prove that every one-dimensional proper scheme $X$ over an algebraically closed field $k$ is projective.

(a) If $X$ is irreducible and nonsingular, then $X$ is projective by (II, 6.7).

(b) If $X$ is integral, let $\tilde X$ be its normalization (II, Ex. 3.8).
Show that $\tilde X$ is complete and nonsingular, hence projective by (a).

Let $f:\tilde X\to X$ be the projection and let $\mcl$ be a very ample invertible sheaf on $\tilde X$.
Show that there is an effective divisor $D=\sum P_i$ on $\tilde X$ with $\OO_{\tilde X}(D)\cong\mcl$, such that $f(P_i)$ is a nonsingular point of $X$ for every $i$.

Conclude that there is an invertible sheaf $\mcl_0$ on $X$ with $f^*\mcl_0\cong\mcl$.
Then use (Ex. 5.7d), (II, 7.6) and (II, 5.16.1) to show that $X$ is projective.

(c) If $X$ is reduced, but not necessarily irreducible, let $X_1,\ldots,X_r$ be its irreducible components with their reduced structures.
Use (Ex. 4.5) to show that $\Pic X\to\bigoplus_i\Pic X_i$ is surjective.
Then use (Ex. 5.7c) to show that $X$ is projective.

(d) For an arbitrary one-dimensional proper scheme $X$ over $k$, use (2.7) and (Ex. 4.6) to show that $\Pic X\to\Pic X_{\mathrm{red}}$ is surjective.
Then use (Ex. 5.7b) to show that $X$ is projective.
:::

::: {.solution}
For a proper scheme of finite type over $k$, existence of an ample invertible sheaf implies projectivity.
Indeed, a positive power is very ample by [@Har10a, Theorem II.7.6] and gives an immersion into a finite-dimensional projective space.
This immersion is proper, since its source is proper and its target is separated over $k$, and a proper immersion is a closed immersion [@Har10a, Remark II.5.16.1].
We will construct such an ample sheaf in each case.

::: pf

::: {.pf-step #s1}

A proper nonsingular integral curve over $k$ is projective, proving (a).

::: pf-proof

This is the equivalence between completeness and projectivity for nonsingular curves [@Har10a, Proposition II.6.7].
Properness is completeness for the curve, so the stated hypothesis applies.

:::

:::

::: {.pf-step #s2}

For integral $X$, its normalization is a nonsingular projective curve, and a very ample sheaf on it is represented by a reduced effective divisor supported over the nonsingular locus of $X$.

::: pf-proof

Normalization of an integral curve of finite type over a field is finite and birational [@Har10a, Exercise II.3.8].
Thus $f:\tilde X\to X$ is finite surjective, and $\tilde X$ is proper over $k$.
Its one-dimensional normal local rings are DVRs, so it is nonsingular [@Har10a, Theorem I.6.2A].
Step [](#s1){.pf-ref} makes it projective.

The nonsingular locus of $X$ is open and dense by [[P-AGH281DIFFNONCLOSED]], part (d).
Its complement is a finite set of closed points of the integral curve, and finiteness of $f$ makes its inverse image finite as well.
Choose a projective embedding of $\tilde X$ with pullback of $\OO(1)$ equal to the given very ample $\mcl$.
The hyperplanes avoiding that finite inverse image form a nonempty open subset of the dual projective space.
Bertini's theorem gives another dense open subset whose intersections with the nonsingular curve are reduced zero-dimensional divisors [@Har10a, Theorem II.8.18].
Their intersection has a $k$-point because $k$ is algebraically closed.
The resulting hyperplane section is $D=\sum P_i$ with distinct closed points and $\OO_{\tilde X}(D)\cong\mcl$.
Its support avoids the inverse image of the singular locus, as required in (b).

:::

:::

::: {.pf-step #s3}

Every proper integral curve $X$ is projective, completing (b).

::: pf-proof

The normalization is an isomorphism over the nonsingular locus, since the local rings there are normal.
Thus the points $f(P_i)$ from step [](#s2){.pf-ref} are distinct nonsingular points of $X$ and define an effective Cartier divisor $D_0=\sum f(P_i)$ on $X$.
Each has a local equation given by a uniformizer, and away from these points the divisor is zero.
Set $\mcl_0=\OO_X(D_0)$.
Pullback of its local equations through the normalization gives $f^*D_0=D$, with multiplicity one because $f$ is an isomorphism there.
Hence $f^*\mcl_0\cong\OO_{\tilde X}(D)\cong\mcl$.
The very ample $\mcl$ is ample, and finite-surjection descent in [[P-AGH357AMPLENESS]], part (d), makes $\mcl_0$ ample on $X$.
Properness and the ample-sheaf criterion preceding step [](#s1){.pf-ref} give projectivity.

:::

:::

::: {.pf-step #s4}

For a reduced proper scheme $X$ of dimension at most one, restriction $\Pic X\to\bigoplus_i\Pic X_i$ is surjective.

::: pf-proof

Induct on the finite number of irreducible components.
The one-component and empty cases are immediate.
Separate one component $Z$ from the reduced union $W$ of the others, and let $I,J$ be their ideals in $X$.
Reducedness and $Z\cup W=X$ give $I\cap J=0$.
Thus the structure sheaf is the fibre product
$$
\OO_X\cong\OO_Z\times_{\OO_T}\OO_W,
\qquad T=Z\cap W,
$$
where all three sheaves on closed subschemes are pushed forward to $X$ and $T$ has its scheme-theoretic intersection structure.
The fibre-product identity is the ring identity $B\cong B/I\times_{B/(I+J)}B/J$ for $I\cap J=0$.

The closed subset $T$ is zero-dimensional or empty, since distinct components of a curve have no common generic point.
It need not be reduced.
There is an exact sequence of abelian sheaves
$$
1\to\OO_X^\times\to\OO_Z^\times\times\OO_W^\times
\xrightarrow{(u,v)\mapsto u|_T/v|_T}\OO_T^\times\to1.
$$
The kernel assertion follows from the fibre-product identity, including invertibility because compatible inverse pairs also glue.
For surjectivity, at a point of $T$ the quotient map of local rings $\OO_{Z,x}\to\OO_{T,x}$ is surjective and lifts units: a lift of a unit lies outside the maximal ideal and is a unit.
Lift on the $Z$ side and choose $1$ on the $W$ side.
Away from $T$ the last stalk is trivial, so the sheaf sequence is exact everywhere.

The noetherian space underlying $T$ has dimension zero, so $H^1(T,\OO_T^\times)=0$ by [@Har10a, Theorem III.2.7].
Closed direct image preserves cohomology, and [[P-AGH345PICH1]] identifies degree-one unit cohomology with Picard groups.
The long exact sequence therefore makes $\Pic X\to\Pic Z\oplus\Pic W$ surjective.
Composing with the induction surjection for $W$ proves the stated map onto all component Picard groups.

:::

:::

::: {.pf-step #s5}

Every reduced one-dimensional proper scheme is projective, proving (c).

::: pf-proof

Every one-dimensional integral component is projective by step [](#s3){.pf-ref} and has an ample invertible sheaf.
A zero-dimensional integral component is a single reduced point with residue field finite over $k$, hence is $\Spec k$ and is projective; its structure sheaf is ample.
Step [](#s4){.pf-ref} allows the chosen invertible sheaves on all the components to be the restrictions of one invertible sheaf $L$ on $X$.
Ampleness on reduced components detects ampleness by [[P-AGH357AMPLENESS]], part (c), so $L$ is ample.
The proper scheme $X$ is therefore projective.
This also handles any isolated zero-dimensional components of the original one-dimensional scheme.

:::

:::

::: {.pf-step #s6}

For arbitrary $X$ in (d), the map $\Pic X\to\Pic X_{\mathrm{red}}$ is surjective and $X$ is projective.

::: pf-proof

Let $N$ be the nilradical ideal sheaf of $X$.
It is nilpotent by noetherianness and a finite affine cover, as in [[P-AGH357AMPLENESS]], step [](#s2){.pf-ref}.
Choose $e\ge1$ with $N^e=0$, and write $X_j=(|X|,\OO_X/N^j)$ for $1\le j\le e$.
Then $X_1=X_{\mathrm{red}}$ and $X_e=X$.
The ideal $N^j/N^{j+1}$ of $X_{j+1}$ has square zero, since $2j\ge j+1$.
The sequence in [[P-AGH346SQUAREZEROPIC]] gives
$$
\Pic X_{j+1}\longrightarrow\Pic X_j
\longrightarrow H^2(X_{j+1},N^j/N^{j+1}).
$$
The last group is zero by Grothendieck vanishing: the underlying space has dimension one [@Har10a, Theorem III.2.7].
Thus every transition on Picard groups is surjective, and composing them proves $\Pic X\to\Pic X_{\mathrm{red}}$ is surjective.

Step [](#s5){.pf-ref} makes the reduction projective, so choose an ample invertible sheaf on it and lift its Picard class to an invertible sheaf $L$ on $X$.
By [[P-AGH357AMPLENESS]], part (b), $L$ is ample.
The proper ample-sheaf criterion now proves that $X$ is projective, including all of its nilpotent structure.

:::

:::

::: pf-qed

Step [](#s1){.pf-ref} proves (a), steps [](#s2){.pf-ref} and [](#s3){.pf-ref} prove (b), steps [](#s4){.pf-ref} and [](#s5){.pf-ref} prove (c), and step [](#s6){.pf-ref} proves (d) and the full theorem.

:::

:::

:::
