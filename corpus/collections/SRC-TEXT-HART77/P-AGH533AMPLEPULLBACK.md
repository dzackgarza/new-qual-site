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

<1>1. If $C\subseteq X$ is an irreducible curve and
$$
r=\mu_P(C),
$$
where $r=0$ when $P\notin C$, then
$$
\boxed{r\le D\cdot C.}
$$

::: {.proof}
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

<1>2. The divisor $A$ has positive intersection with the exceptional curve:
$$
\boxed{A\cdot E=1.}
$$

::: {.proof}
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

<1>3. Let $\Gamma\subseteq\widetilde X$ be an irreducible curve with
$$
\Gamma\ne E.
$$
Then $\Gamma$ is the strict transform of an irreducible curve
$C\subseteq X$.

::: {.proof}
The blowup map
$$
\pi:\widetilde X\longrightarrow X
$$
is an isomorphism over $X\setminus\{P\}$. Since $\Gamma$ is not contained in
the exceptional locus $E$, its image is an irreducible curve $C\subseteq X$,
and $\Gamma$ is the closure of the inverse image of
$C\setminus\{P\}$. This is exactly the strict transform of $C$.
:::

<1>4. For every irreducible curve $\Gamma\ne E$ on $\widetilde X$,
$$
\boxed{A\cdot\Gamma>0.}
$$

::: {.proof}
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
By step <1>1,
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

<1>5. The self-intersection of $A$ is positive:
$$
\boxed{A^2=4D^2-1>0.}
$$

::: {.proof}
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

<1>6. The divisor
$$
\boxed{2\pi^*D-E}
$$
is ample on $\widetilde X$.

::: {.proof}
Step <1>2 gives positive intersection with the exceptional curve. Step
<1>4 gives positive intersection with every other irreducible curve on
$\widetilde X$, and step <1>5 gives positive self-intersection. Therefore
the Nakai--Moishezon criterion [[T-SRFNAKAI]] applies and shows that
$$
2\pi^*D-E
$$
is ample.
:::

<1>7. Q.E.D.

::: {.proof}
Steps <1>1--<1>5 verify the numerical hypotheses of Nakai--Moishezon, and
step <1>6 gives the required ampleness.
:::
:::
