---
schema: qual/card@1
id: P-AGH2411DVRCRIT
kind: problem
title: Valuative criteria using discrete valuation rings
classification:
  areas:
  - algebraic-geometry
  topics:
  - Valuative Criteria
  - Discrete Valuation Rings
  - Krull-Akizuki
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-17
  note: Checked against Hartshorne II.4.11. Part (a) has a field/finite-algebraic edge-case exception; the corrected statement is proved below. Part (b) is unaffected.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-17
---

::: problem
If we are willing to do harder commutative algebra and stick to noetherian schemes, then the valuative criteria of separatedness and properness can be expressed using only **discrete** valuation rings.

a. If $\OO, \mfm$ is a noetherian local domain with quotient field $K$, and if $L$ is a finitely generated field extension of $K$, then there exists a discrete valuation ring $R$ of $L$ dominating $\OO$.
   Prove this in the following steps.

    - By taking a polynomial ring over $\OO$, reduce to the case where $L$ is a finite extension field of $K$.
    - Show that for a suitable choice of generators $x_1, \ldots, x_n$ of $\mfm$, the ideal $\mfa = (x_1)$ in $\OO' = \OO[x_2/x_1, \ldots, x_n/x_1]$ is not the unit ideal.
    - Let $\mfp$ be a minimal prime ideal of $\mfa$, and let $\OO'_\mfp$ be the localization of $\OO'$ at $\mfp$. This is a noetherian local domain of dimension $1$ dominating $\OO$.
    - Let $\widetilde{\OO'_\mfp}$ be the integral closure of $\OO'_\mfp$ in $L$. Use the Krull-Akizuki theorem (Nagata, p. 115) to show that $\widetilde{\OO'_\mfp}$ is noetherian of dimension $1$.
    - Finally, take $R$ to be a localization of $\widetilde{\OO'_\mfp}$ at one of its maximal ideals.

b. Let $f: X \to Y$ be a morphism of finite type of noetherian schemes.
   Show that $f$ is separated, respectively proper, if and only if the criterion of (4.3), respectively (4.7), holds for all discrete valuation rings.
:::

::: {.solution}
Let
\[
(\OO,\mathfrak m)
\]
be a noetherian local domain with fraction field $K$, and let $L/K$ be finitely generated.

::: pf

::: {.pf-step #s1}

In the exceptional case $\mathfrak m=0$ and $L/K$ finite algebraic, no DVR of $L$ dominates $\OO=K$.

::: pf-proof

Suppose $R\subseteq L$ is a valuation ring containing $K$ and with
\[
\mathfrak m_R\cap K=(0).
\]
Let $v$ be its valuation.  Then $v(c)=0$ for every $c\in K^\times$.

If $0\ne\alpha\in L$ is algebraic over $K$, write a polynomial relation
\[
c_0+c_1\alpha+\cdots+c_n\alpha^n=0
\]
with $c_0c_n\ne0$.
If $v(\alpha)>0$, the term $c_0$ has strictly smaller value than every other term, impossible in a vanishing sum.  If $v(\alpha)<0$, the term $c_n\alpha^n$ has strictly smaller value than every other term, again impossible.  Hence
\[
v(\alpha)=0.
\]
Thus the valuation is trivial on all of $L$, so $R=L$ is a field rather than a DVR.

:::

:::

::: {.pf-step #s2}

Apart from the exceptional case of step [](#s1){.pf-ref}, it is enough to prove part (a) when $L/K$ is finite and $\mathfrak m\ne0$.

::: pf-proof

Choose a transcendence basis
\[
t_1,\ldots,t_r
\]
of $L/K$.  Then
\[
L/K(t_1,\ldots,t_r)
\]
is finite.

If $r=0$, then $L/K$ is already finite.  Since we have excluded step [](#s1){.pf-ref}, $\mathfrak m\ne0$.

If $r>0$, put
\[
\OO_1
=
\OO[t_1,\ldots,t_r]_{\mathfrak n},
\qquad
\mathfrak n
=
\mathfrak m\OO[t_1,\ldots,t_r]+(t_1,\ldots,t_r).
\]
Then $\OO_1$ is a noetherian local domain, its fraction field is
\[
K(t_1,\ldots,t_r),
\]
and its maximal ideal $\mathfrak n\OO_1$ is nonzero.  Moreover $\OO_1$ dominates $\OO$ because
\[
\mathfrak n\cap\OO=\mathfrak m.
\]

If a DVR of $L$ dominates $\OO_1$, it also dominates $\OO$.  Thus replacing $(\OO,K)$ by $(\OO_1,K(t_1,\ldots,t_r))$ reduces to a finite extension and a nonzero maximal ideal.

:::

:::

::: {.pf-step #s3}

Assume now that $L/K$ is finite and $\mathfrak m\ne0$.  Choose generators
\[
\mathfrak m=(x_1,\ldots,x_n)
\]
and reorder them so that for some valuation ring $V$ of $K$ dominating $\OO$, the value of $x_1$ is minimal among the values of the $x_i$.

::: pf-proof

The maximal ideal is finitely generated because $\OO$ is noetherian.

Hartshorne I.6.1A says that every local subring of a field is dominated by a valuation ring of that field.  Hence there is a valuation ring
\[
V\subseteq K
\]
dominating $\OO$.

All $x_i$ lie in the maximal ideal of $V$, so their values are positive.  Among the finite set of values choose a minimum and relabel the corresponding generator as $x_1$.

:::

:::

::: {.pf-step #s4}

Put
\[
\OO'
=
\OO\left[\frac{x_2}{x_1},\ldots,\frac{x_n}{x_1}\right]
\subseteq K.
\]
Then the ideal
\[
\mathfrak a=(x_1)\subseteq\OO'
\]
is proper.

::: pf-proof

By minimality of $v(x_1)$,
\[
v(x_i/x_1)\ge0
\]
for every $i$.  Hence
\[
\OO'\subseteq V.
\]

Because $V$ dominates $\OO$ and $x_1\in\mathfrak m$, one has
\[
x_1\in\mathfrak m_V.
\]
If $(x_1)=\OO'$, then $x_1$ would be a unit of $\OO'$, hence a unit of $V$, contradiction.  Thus $(x_1)$ is not the unit ideal.

:::

:::

::: {.pf-step #s5}

Let $\mathfrak p$ be a prime ideal minimal over $(x_1)$ in $\OO'$.  Then
\[
\OO'_{\mathfrak p}
\]
is a one-dimensional noetherian local domain which dominates $\OO$ and has fraction field $K$.

::: pf-proof

The ring $\OO'$ is a finitely generated $\OO$-algebra, hence noetherian, and it is a subring of the field $K$, hence a domain.

Krull's principal ideal theorem gives
\[
\operatorname{ht}\mathfrak p\le1.
\]
Since $x_1\ne0$ and $x_1\in\mathfrak p$, one has $\mathfrak p\ne(0)$, so
\[
\operatorname{ht}\mathfrak p=1.
\]
Therefore
\[
\dim\OO'_{\mathfrak p}=1.
\]

For every $j$,
\[
x_j=x_1(x_j/x_1)\in\mathfrak p.
\]
Thus
\[
\mathfrak m=(x_1,\ldots,x_n)
\subseteq
\mathfrak p\cap\OO.
\]
The contraction is a proper ideal of the local ring $\OO$, so maximality of $\mathfrak m$ gives
\[
\mathfrak p\cap\OO=\mathfrak m.
\]
Hence the local inclusion
\[
\OO\subseteq\OO'_{\mathfrak p}
\]
is a domination.

Finally $\OO'$ lies between $\OO$ and its fraction field $K$, so its fraction field, and that of its localization, is $K$.

:::

:::

::: {.pf-step #s6}

Let
\[
C
\]
be the integral closure of $\OO'_{\mathfrak p}$ in the finite extension field $L/K$.  Then $C$ is a noetherian one-dimensional domain.

::: pf-proof

The ring $\OO'_{\mathfrak p}$ is a one-dimensional noetherian domain.  The Krull--Akizuki theorem says that its integral closure in any finite extension of its fraction field is a noetherian domain of dimension one.
Thus $C$ has the asserted properties.

:::

:::

::: {.pf-step #s7}

Choose a maximal ideal $\mathfrak q\subseteq C$ lying over the maximal ideal of $\OO'_{\mathfrak p}$ and put
\[
R=C_{\mathfrak q}.
\]
Then $R$ is a DVR of $L$ dominating $\OO$.

::: pf-proof

The extension
\[
\OO'_{\mathfrak p}\subseteq C
\]
is integral, so lying over provides a prime $\mathfrak q$ over the maximal ideal of $\OO'_{\mathfrak p}$.  Since $C$ is one-dimensional, such a nonzero prime is maximal.

The localization $R=C_{\mathfrak q}$ is a noetherian local domain of dimension one.  It is integrally closed because $C$ is integrally closed and localization preserves integral closedness.  Hence Hartshorne I.6.2A implies that $R$ is a discrete valuation ring.

Its fraction field is $L$, and the contraction of its maximal ideal to $\OO'_{\mathfrak p}$ is the maximal ideal there.  Thus $R$ dominates $\OO'_{\mathfrak p}$, which by step [](#s5){.pf-ref} dominates $\OO$.  Therefore $R$ dominates $\OO$.

:::

:::

::: {.pf-step #s8}

This proves the corrected statement of part (a).

::: pf-proof

Step [](#s2){.pf-ref} reduces to the finite-extension, nonfield case; steps [](#s3){.pf-ref}, [](#s4){.pf-ref}, [](#s5){.pf-ref}, [](#s6){.pf-ref} and [](#s7){.pf-ref} construct the required DVR.  Step [](#s1){.pf-ref} records the unique excluded case in the source statement.

:::

:::

::: {.pf-step #s9}

Now let
\[
f:X\longrightarrow Y
\]
be of finite type with $X$ and $Y$ noetherian.  If $f$ is separated, then every DVR-valuative diagram has at most one lift; if $f$ is proper, every such diagram has exactly one lift.

::: pf-proof

These are immediate special cases of Hartshorne II.4.3 and II.4.7, whose valuative criteria are stated for arbitrary valuation rings.

:::

:::

::: {.pf-step #s10}

Conversely, suppose every DVR-valuative diagram for $f$ has at most one lift.  Then $f$ is separated.

::: pf-proof

Consider the diagonal
\[
\Delta_f:X\longrightarrow X\times_YX.
\]
It is always an immersion.  It is enough to show its image is closed.

Suppose it were not closed.  Since $X\times_YX$ is noetherian and the image of an immersion is locally closed, choose a point
\[
z\in\overline{\Delta_f(X)}\setminus\Delta_f(X)
\]
and an irreducible closed subset
\[
T\subseteq\overline{\Delta_f(X)}
\]
containing $z$ whose generic point $\xi$ lies in $\Delta_f(X)$.  Give $T$ its reduced induced structure.

The local ring
\[
\OO_{T,z}
\]
is a noetherian local domain.  Since $z\ne\xi$, it is not a field.  Its fraction field is
\[
\kappa(\xi).
\]
Part (a) supplies a DVR
\[
R\subseteq\kappa(\xi)
\]
dominating $\OO_{T,z}$.

The corresponding morphism
\[
\Spec R\longrightarrow T\subseteq X\times_YX
\]
has two projections
\[
u_1,u_2:\Spec R\rightrightarrows X.
\]
At the generic point these agree because $\xi$ lies on the diagonal.  They are morphisms over $Y$ because they come from the fibre product.

If $u_1=u_2$, the whole morphism $\Spec R\to X\times_YX$ would factor through the diagonal, so its closed point $z$ would lie in $\Delta_f(X)$, contradiction.  Thus the same DVR-valuative diagram has two distinct lifts, contrary to hypothesis.

Hence the image of the diagonal is closed.  An immersion with closed image is a closed immersion, so $f$ is separated.

:::

:::

::: {.pf-step #s11}

Suppose every DVR-valuative diagram for $f$ has a unique lift.  Then $f$ is separated.

::: pf-proof

Uniqueness in particular gives the ``at most one'' condition.  Apply step [](#s10){.pf-ref}.

:::

:::

::: {.pf-step #s12}

Under the hypothesis of step [](#s11){.pf-ref}, the morphism $f$ is universally closed.

::: pf-proof

Because $Y$ is noetherian and $f$ is of finite type, $f$ is of finite presentation.  In checking universal closedness, the standard noetherian-approximation step in the proof of the valuative criterion reduces arbitrary base changes to base changes
\[
Y'\longrightarrow Y
\]
with $Y'$ noetherian and of finite type over $Y$.  Universal closedness of a quasi-compact morphism may be tested after base changes locally of finite presentation (Stacks Project, Tag 05JX); restricting around a point witnessing failure of closedness then gives the noetherian affine case used here.

Fix such a base change and put
\[
X'=X\times_YY'.
\]
Let $Z\subseteq X'$ be closed.  Suppose its image in $Y'$ were not closed.  Since
\[
Z\longrightarrow Y'
\]
is of finite type between noetherian schemes, Chevalley's theorem makes its image constructible.  Choose
\[
y\in\overline{p(Z)}\setminus p(Z).
\]
There is an irreducible closed subset
\[
C\subseteq\overline{p(Z)}
\]
containing $y$ whose generic point
\[
\eta
\]
lies in $p(Z)$; this follows from the generic-point characterization of dense constructible subsets.
Give $C$ its reduced induced scheme structure.

Choose a point
\[
z\in Z
\]
over $\eta$.  The residue-field extension
\[
L=\kappa(z)
\quad/\quad
K=\kappa(\eta)
\]
is finitely generated because $Z\to Y'$ is of finite type.

The local ring
\[
\OO_{C,y}
\]
is a noetherian local domain with fraction field $K$.  Since $y\ne\eta$, it is not a field.  Part (a) gives a DVR
\[
R\subseteq L
\]
dominating $\OO_{C,y}$.

The generic point gives a morphism
\[
\Spec L\longrightarrow Z\subseteq X'=X\times_YY',
\]
and domination gives
\[
\Spec R\longrightarrow C\subseteq Y'.
\]
Composing the former with $X'\to X$ and the latter with $Y'\to Y$ produces a DVR-valuative diagram for $f$.  By hypothesis it has a lift
\[
\Spec R\longrightarrow X.
\]

Together with the fixed morphism $\Spec R\to Y'$, this lift gives by the fibre-product property a morphism
\[
\Spec R\longrightarrow X'.
\]
Its generic point is the chosen point of $Z$.  Since $Z$ is closed and the generic point of $\Spec R$ is dense, the entire morphism factors through $Z$.  The closed point therefore maps to a point of $Z$ lying over $y$, contradicting
\[
y\notin p(Z).
\]

Thus every such base change is closed, and the noetherian-approximation reduction gives universal closedness.

:::

:::

::: {.pf-step #s13}

Under the hypothesis of step [](#s11){.pf-ref}, the morphism $f$ is proper.

::: pf-proof

The morphism is of finite type by assumption, separated by step [](#s11){.pf-ref}, and universally closed by step [](#s12){.pf-ref}.  These are exactly the defining conditions for properness.

:::

:::

::: {.pf-step #s14}

Hence for finite-type morphisms of noetherian schemes,
\[
\boxed{
f\text{ separated}
\iff
\text{the valuative criterion has at most one lift for every DVR},
}
\]
and
\[
\boxed{
f\text{ proper}
\iff
\text{the valuative criterion has exactly one lift for every DVR}.
}
\]

::: pf-proof

The forward implications are step [](#s9){.pf-ref}.  The converse separatedness implication is step [](#s10){.pf-ref}, and the converse properness implication is steps [](#s11){.pf-ref}, [](#s12){.pf-ref} and [](#s13){.pf-ref}.

:::

:::

::: pf-qed

Steps [](#s1){.pf-ref}, [](#s2){.pf-ref}, [](#s3){.pf-ref}, [](#s4){.pf-ref}, [](#s5){.pf-ref}, [](#s6){.pf-ref}, [](#s7){.pf-ref} and [](#s8){.pf-ref} prove the corrected form of part (a), and steps [](#s9){.pf-ref}, [](#s10){.pf-ref}, [](#s11){.pf-ref}, [](#s12){.pf-ref}, [](#s13){.pf-ref} and [](#s14){.pf-ref} prove part (b).

:::

:::

:::

::: {.remark title="Erratum"}
Part (a), as stated in the source, has one exceptional case.  If $\OO=K$ is a field and $L/K$ is finite algebraic, then no nontrivial discrete valuation ring of $L$ can dominate $K$: any valuation of $L$ which is trivial on $K$ is trivial on the algebraic extension $L/K$, so its valuation ring is the field $L$.

The intended statement is correct provided either $\OO$ is not a field or
\[
\operatorname{trdeg}_K L>0.
\]
This is the form proved in the solution.  It is exactly the form needed in the nontrivial specialization arguments of part (b).
:::
