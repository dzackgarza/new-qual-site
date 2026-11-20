---
schema: qual/card@1
id: P-AGH466PROJECTIVELYNORMALGENERA
kind: problem
title: Possible genera of projectively normal curves of degree $6$ and $7$ in $\PP^3$
classification:
  areas:
  - algebraic-geometry
  topics:
  - Genus
  - Embeddings
  - Very Ample Divisors
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-18
  note: >-
    Read Hartshorne IV.6.6, its references to II.8.4 and III.5.6, the
    repository's Castelnuovo bound, and the retained Egbert working notes.
    The source statement needs no correction. The proof below is independent
    of those incomplete notes: projective normality and nondegeneracy give
    h^0(H)=4, Riemann--Roch gives the lower genus bound, Castelnuovo gives the
    upper bound, and projective normality in degree two excludes the lone
    extra case (d,g)=(7,4).
- event: solution-written
  by: chatgpt
  date: 2026-09-18
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-18
- event: source-checked
  by: claude
  date: 2026-11-20
  note: >-
    Citation form (#184). The two results the proof uses are now named by number: Riemann--Roch is
    Theorem IV.1.3, in steps s1 and s4, and Castelnuovo's bound is Theorem IV.6.4, in steps s2 and
    s3. The inference from projective normality to the surjectivity of the restriction map
    H^0(P^3, O(n)) -> H^0(X, O_X(n)), which s1 and s4 make, is the one Hartshorne makes in Example
    IV.6.4.3, and the definition of projective normality the card uses is the one of Exercise
    II.5.14; both are named on the card now. No page, PDF page or page offset appears in its text.

    The mathematics is unchanged: s1's h^0(H) = 4 and g >= d-3, s2's 3 <= g <= 4 at d = 6, s3's
    4 <= g <= 6 at d = 7, and s4's exclusion of g = 4 at d = 7 by h^0(X, 2H) = 11 > 10 =
    h^0(P^3, O(2)) were each read and are correct.

    Not verified in this pass: the parts of Exercise II.5.14, because the retained copy of the book
    in this checkout is its text extraction, which drops the numbered parts of that exercise; the
    criterion is therefore attributed through the book's own use of it in Example IV.6.4.3 rather
    than to a numbered part.

---

::: {.problem}
Let $X$ be a projectively normal curve in $\PP^3$, not contained in any plane.
If $d=6$, then $g=3$ or 4. If $d=7$, then $g=5$ or 6. Cf. (II, Ex. 8.4) and (III, Ex. 5.6).
:::

::: {.solution}
Put
$$
H=\OO_X(1).
$$

::: pf

::: {.pf-step #s1}

One has
$$
h^0(X,H)=4
$$
and therefore
$$
g\ge d-3.
$$

::: pf-proof

Because $X$ is not contained in a plane, no nonzero linear form on $\PP^3$
vanishes identically on $X$.  Thus the restriction map
$$
H^0(\PP^3,\OO_{\PP^3}(1))
\longrightarrow
H^0(X,H)
$$
is injective.  Projective normality makes the same restriction map
surjective, so it is an isomorphism: this is the inference Hartshorne draws from
projective normality in Example IV.6.4.3, and the definition of projective
normality is the one of Exercise II.5.14.  Hence
$$
h^0(X,H)=h^0(\PP^3,\OO_{\PP^3}(1))=4.
$$

Riemann--Roch, Theorem IV.1.3, gives
$$
h^0(X,H)-h^0(X,K-H)=d+1-g.
$$
Substituting $h^0(X,H)=4$ yields
$$
g=d-3+h^0(X,K-H)\ge d-3.
$$

:::

:::

::: {.pf-step #s2}

If $d=6$, then
$$
\boxed{g=3\text{ or }4}.
$$

::: pf-proof

Step [](#s1){.pf-ref} gives
$$
g\ge6-3=3.
$$
Since $X$ is a nonplanar smooth space curve of degree $6$,
[[T-CRVCAST|Castelnuovo's bound]], Theorem IV.6.4, gives
$$
g\le\frac{6^2}{4}-6+1=4.
$$
Thus $3\le g\le4$.

:::

:::

::: {.pf-step #s3}

If $d=7$, then Castelnuovo and step [](#s1){.pf-ref} give
$$
4\le g\le6.
$$

::: pf-proof

Step [](#s1){.pf-ref} gives
$$
g\ge7-3=4.
$$
For odd degree $7$, [[T-CRVCAST|Castelnuovo's bound]], Theorem IV.6.4, gives
$$
g
\le
\frac{7^2-1}{4}-7+1
=6.
$$

:::

:::

::: {.pf-step #s4}

When $d=7$, the case $g=4$ is impossible.

::: pf-proof

Suppose $d=7$ and $g=4$.  Then
$$
\deg(2H)=14>2g-2=6,
$$
so $2H$ is nonspecial.  Riemann--Roch, Theorem IV.1.3, gives
$$
h^0(X,2H)=14+1-4=11.
$$

Projective normality requires the degree-two restriction map
$$
H^0(\PP^3,\OO_{\PP^3}(2))
\longrightarrow
H^0(X,2H)
$$
to be surjective.  But
$$
h^0(\PP^3,\OO_{\PP^3}(2))=10<11=h^0(X,2H),
$$
which is impossible.  Hence $g\ne4$.

:::

:::

::: {.pf-step #s5}

If $d=7$, then
$$
\boxed{g=5\text{ or }6}.
$$

::: pf-proof

Step [](#s3){.pf-ref} gives $4\le g\le6$, and step [](#s4){.pf-ref} excludes $g=4$.

:::

:::

::: pf-qed

Step [](#s2){.pf-ref} proves the degree-$6$ assertion, and step [](#s5){.pf-ref} proves the
degree-$7$ assertion.

:::

:::

:::
