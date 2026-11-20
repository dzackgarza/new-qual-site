---
schema: qual/card@1
id: P-AGH533AMPLEPULLBACK
kind: problem
title: Ampleness of $2\pi^*D - E$ on a blowup
classification:
  areas:
  - algebraic-geometry
  topics:
  - Surfaces
  - Blowups
  - Intersection Theory
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-19
  note: >-
    Read Hartshorne V.3.3, the retained Egbert companion calculation, the
    preceding blowup intersection formula, and Nakai--Moishezon. The companion
    uses the intended degree-versus-multiplicity estimate but states it
    strictly; the sharp form needed here is mu_P(C)<=deg_D(C), with equality
    possible for a line through P. This still yields strict positivity for
    2 pi^*D-E against every strict transform, while its intersection with the
    exceptional curve is 1 and its square is 4D^2-1>0.
- event: solution-written
  by: chatgpt
  date: 2026-09-19
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-19
- event: source-checked
  by: claude
  date: 2026-11-19
  note: >-
    A retained solution read at this exercise. Read Yang Pi-Yeh, Hartshorne
    Solutions (9 June 2019), Solution 5.3.3, printed p. 107,
    rendered as a page image from
    tmp/sources/lfwin-hartshorne-solutions.pdf, whose PDF page is the printed
    page. Checked against the book: Hartshorne V.3.3, whose printed page the card's earlier events
    record; this pass did not reopen it, and the comparison is against the
    statement the card carries. Recomputed
    (2 pi^*D - E)^2 = 4D^2 - 1, the intersection with a strict
    transform C-tilde = pi^*C - rE giving 2 deg C - r, and r <= deg C. Not checked: Yang's Solutions outside printed pp. 100-107; the
    book's own page in this pass; and the printed book itself.
- event: solution-written
  by: claude
  date: 2026-11-19
  note: >-
    The remark now names Yang Pi-Yeh's Solution 5.3.3 at printed
    p. 107 beside Egbert's entry, with the slips its text carries.
    No step, statement or hypothesis of the card changes.
---

::: {.problem}
Let $\pi: \tilde{X} \rightarrow X$ be a monoidal transformation, and let $D$ be a very ample divisor on $X$.
Show that $2 \pi^* D-E$ is ample on $\tilde{X}$.

Hint: Use a suitable generalization of (I, Ex.
7.5) to curves in $\PP^n$.
:::

::: {.solution}
Let
$$
P\in X
$$
be the centre of the monoidal transformation, and let
$$
E\subseteq\widetilde X
$$
be the exceptional curve. Put
$$
A=2\pi^*D-E.
$$

::: pf

::: {.pf-step #multiplicity-degree-bound}
If $C\subseteq X$ is an irreducible curve and
$$
r=\mu_P(C),
$$
where $r=0$ when $P\notin C$, then
$$
\boxed{r\le D\cdot C.}
$$

::: pf-proof
Because $D$ is very ample, its complete linear system embeds
$$
\iota_D:X\hookrightarrow\PP^N
$$
and
$$
D\cdot C=\deg\iota_D(C).
$$
The multiplicity of $C$ at $P$ is unchanged by this closed immersion.

Choose a hyperplane $H\subseteq\PP^N$ through $\iota_D(P)$ which does not
contain $\iota_D(C)$ and is general among such hyperplanes. The local
intersection multiplicity at $P$ satisfies
$$
i_P(C,H)\ge\mu_P(C)=r,
$$
while the sum of all local intersection multiplicities with $H$ is
$$
H\cdot\iota_D(C)=\deg\iota_D(C)=D\cdot C.
$$
Therefore
$$
r\le D\cdot C.
$$
This is the required projective-space generalization of the multiplicity
bound in [[P-AGH75MULTBOUND]].
:::

:::

::: {.pf-step #ample-meets-exceptional}
The divisor $A$ has positive intersection with the exceptional curve:
$$
\boxed{A\cdot E=1.}
$$

::: pf-proof
The blowup intersection formulas [[FE-SRFBLOW]] give
$$
\pi^*D\cdot E=0,
\qquad
E^2=-1.
$$
Hence
$$
A\cdot E
=(2\pi^*D-E)\cdot E
=-E^2
=1.
$$
:::

:::

::: {.pf-step #curve-is-strict-transform}
Let $\Gamma\subseteq\widetilde X$ be an irreducible curve with
$$
\Gamma\ne E.
$$
Then $\Gamma$ is the strict transform of an irreducible curve
$C\subseteq X$.

::: pf-proof
The blowup map
$$
\pi:\widetilde X\longrightarrow X
$$
is an isomorphism over $X\setminus\{P\}$. Since $\Gamma$ is not contained in
the exceptional locus $E$, its image is an irreducible curve $C\subseteq X$,
and $\Gamma$ is the closure of the inverse image of
$C\setminus\{P\}$. This is exactly the strict transform of $C$.
:::

:::

::: {.pf-step #positive-on-other-curves}
For every irreducible curve $\Gamma\ne E$ on $\widetilde X$,
$$
\boxed{A\cdot\Gamma>0.}
$$

::: pf-proof
Let $C=\pi(\Gamma)$ and put
$$
r=\mu_P(C),
$$
again taking $r=0$ if $P\notin C$. The strict-transform formula gives
$$
\Gamma\equiv\pi^*C-rE.
$$
Using the blowup intersection identities,
$$
\begin{aligned}
A\cdot\Gamma
&=(2\pi^*D-E)\cdot(\pi^*C-rE)\\
&=2D\cdot C-r.
\end{aligned}
$$
By step [](#multiplicity-degree-bound){.pf-ref},
$$
r\le D\cdot C,
$$
so
$$
A\cdot\Gamma
\ge
D\cdot C.
$$
Since $D$ is very ample, its restriction to the irreducible curve $C$ has
positive degree. Thus
$$
D\cdot C>0,
$$
and consequently $A\cdot\Gamma>0$.
:::

:::

::: {.pf-step #positive-self-intersection}
The self-intersection of $A$ is positive:
$$
\boxed{A^2=4D^2-1>0.}
$$

::: pf-proof
Again using
$$
\pi^*D\cdot E=0,
\qquad
E^2=-1,
$$
one obtains
$$
\begin{aligned}
A^2
&=(2\pi^*D-E)^2\\
&=4(\pi^*D)^2+E^2\\
&=4D^2-1.
\end{aligned}
$$
Because $D$ is very ample on the projective surface $X$, it gives an
embedding of $X$ and
$$
D^2=\deg_D(X)
$$
is a positive integer. Hence
$$
4D^2-1\ge3>0.
$$
:::

:::

::: {.pf-step #nakai-moishezon-ample}
The divisor
$$
\boxed{2\pi^*D-E}
$$
is ample on $\widetilde X$.

::: pf-proof
Step [](#ample-meets-exceptional){.pf-ref} gives positive intersection with the exceptional curve. Step
[](#positive-on-other-curves){.pf-ref} gives positive intersection with every other irreducible curve on
$\widetilde X$, and step [](#positive-self-intersection){.pf-ref} gives positive self-intersection. Therefore
the Nakai--Moishezon criterion [[T-SRFNAKAI]] applies and shows that
$$
2\pi^*D-E
$$
is ample.
:::

:::

::: pf-qed
Steps [](#multiplicity-degree-bound){.pf-ref}, [](#ample-meets-exceptional){.pf-ref}, [](#curve-is-strict-transform){.pf-ref}, [](#positive-on-other-curves){.pf-ref} and [](#positive-self-intersection){.pf-ref} verify the numerical hypotheses of Nakai--Moishezon, and
step [](#nakai-moishezon-ample){.pf-ref} gives the required ampleness.
:::

:::
:::

::: {.remark title="Published solution"}
The exercise stands on printed p. 394 of Hartshorne, read in `tmp/sources/hartshorne-1977-algebraic-geometry.pdf`, where printed p. $N$ is PDF p. $N+15$, and the statement above is that page's text, the hint including.

Andrew Egbert, *Solutions to Hartshorne's Algebraic Geometry* (October 3, 2013), text version `tmp/sources/hartshorne-solutions-egbert.md`, Exercise V.3.3: he recalls I Ex. 7.5, that an irreducible plane curve of degree $d>1$ has no point of multiplicity $\ge d$, and generalizes it to $\PP^n$; then, since $D$ is very ample, $D\cdot C$ is $\deg C$, any class on $\widetilde X$ is $\pi^*C-rE$, and
$$
(2\pi^*D-E)\cdot(\pi^*C-rE)=2\deg C-r>0,\qquad (2\pi^*D-E)^2=4D^2+E^2>0 .
$$
Step [](#multiplicity-degree-bound){.pf-ref} is his generalization of I Ex. 7.5, obtained by intersecting the embedded curve with a general hyperplane through the image of $P$; steps [](#ample-meets-exceptional){.pf-ref}, [](#positive-on-other-curves){.pf-ref} and [](#positive-self-intersection){.pf-ref} are his two positivity computations, and they are applied through Nakai--Moishezon rather than to the single curve he checks. Matches.

Yang Pi-Yeh, *Hartshorne Solutions* (9 June 2019), Solution 5.3.3, printed p. 107, verifies the Nakai--Moishezon hypotheses for $2\pi^*D-E$: its square is $4D^2-1\ge3>0$, and for a curve $\widetilde C=\pi^*C-rE$ whose image is a curve, with $r=\mu_P(C)\le\deg C$, one gets $(2\pi^*D-E)\cdot\widetilde C=2\deg C-r\ge\deg C>0$. Two things it leaves: the exceptional curve $E$ itself, on which $(2\pi^*D-E)\cdot E=1>0$, is not among the curves it checks, and its closing sentence names $D$ where the class proved ample is $2\pi^*D-E$. The card's own steps cover both.
:::
