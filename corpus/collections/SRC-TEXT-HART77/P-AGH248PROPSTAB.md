---
schema: qual/card@1
id: P-AGH248PROPSTAB
kind: problem
title: Stability properties of a class of morphisms
classification:
  areas:
  - algebraic-geometry
  topics:
  - Morphism Properties
  - Base Change
  - Separated Morphisms
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-17
  note: Checked against Hartshorne II.4.8 and the graph/base-change factorization in the source hint.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-17
---

::: {.problem}
Let $\mathscr{P}$ be a property of morphisms of schemes such that

a. a closed immersion has $\mathscr{P}$;

b. a composition of two morphisms having $\mathscr{P}$ has $\mathscr{P}$;

c. $\mathscr{P}$ is stable under base extension.

Then show that

d. a product of morphisms having $\mathscr{P}$ has $\mathscr{P}$;

e. if $f: X \to Y$ and $g: Y \to Z$ are two morphisms, and if $g \circ f$ has $\mathscr{P}$ and $g$ is separated, then $f$ has $\mathscr{P}$;

f. if $f: X \to Y$ has $\mathscr{P}$, then $f_{\text{red}}: X_{\text{red}} \to Y_{\text{red}}$ has $\mathscr{P}$.

*Hint:* for (e), consider the graph morphism $\Gamma_f: X \to \fiberprod{X}{Z}{Y}$ and note that it is obtained by base extension from the diagonal morphism $\Delta: Y \to \fiberprod{Y}{Z}{Y}$.
:::

::: {.solution}
Assume throughout that the property $\mathscr P$ satisfies (a), (b), and (c).

<1>1. Let
\[
f:X\to Y,
\qquad
f':X'\to Y'
\]
have $\mathscr P$.
Then the morphism
\[
f\times\id_{X'}:X\times X'\longrightarrow Y\times X'
\]
has $\mathscr P$.
::: {.proof}
The displayed morphism is the base change of
\[
f:X\to Y
\]
along the projection
\[
Y\times X'\longrightarrow Y.
\]
Property (c) says that $\mathscr P$ is stable under arbitrary base extension, so the base-changed morphism has $\mathscr P$.
:::

<1>2. The morphism
\[
\id_Y\times f':Y\times X'\longrightarrow Y\times Y'
\]
has $\mathscr P$.
::: {.proof}
This is the base change of
\[
f':X'\to Y'
\]
along the projection
\[
Y\times Y'\longrightarrow Y'.
\]
Apply property (c).
:::

<1>3. The product morphism
\[
\boxed{
f\times f':X\times X'\longrightarrow Y\times Y'
}
\]
has $\mathscr P$.
::: {.proof}
It factors as
\[
X\times X'
\xrightarrow{f\times\id_{X'}}
Y\times X'
\xrightarrow{\id_Y\times f'}
Y\times Y'.
\]
Both factors have $\mathscr P$ by <1>1--<1>2, so their composition has $\mathscr P$ by property (b).
This proves part (d).
:::

<1>4. Let
\[
X\xrightarrow{f}Y\xrightarrow{g}Z
\]
with $g\circ f$ having $\mathscr P$ and $g$ separated.
The graph
\[
\Gamma_f:X\longrightarrow X\times_ZY,
\qquad
x\longmapsto(x,f(x)),
\]
is a closed immersion.
::: {.proof}
Consider the Cartesian square
\[
\begin{array}{ccc}
X&\xrightarrow{\Gamma_f}&X\times_ZY\\
\downarrow{\scriptstyle f}&&\downarrow{\scriptstyle f\times\id_Y}\\
Y&\xrightarrow{\Delta_g}&Y\times_ZY.
\end{array}
\]
The graph is the base change of the diagonal
\[
\Delta_g:Y\to Y\times_ZY.
\]

Since $g$ is separated, $\Delta_g$ is a closed immersion.  Closed immersions are stable under base change, so $\Gamma_f$ is a closed immersion.
:::

<1>5. The graph morphism $\Gamma_f$ has $\mathscr P$.
::: {.proof}
By <1>4 it is a closed immersion.  Property (a) says every closed immersion has $\mathscr P$.
:::

<1>6. The projection
\[
p_2:X\times_ZY\longrightarrow Y
\]
has $\mathscr P$.
::: {.proof}
The projection $p_2$ is the base change of
\[
g\circ f:X\longrightarrow Z
\]
along
\[
g:Y\longrightarrow Z.
\]
Since $g\circ f$ has $\mathscr P$, property (c) gives $\mathscr P$ for $p_2$.
:::

<1>7. The morphism
\[
\boxed{f:X\to Y}
\]
has $\mathscr P$.
::: {.proof}
The factorization
\[
f=p_2\circ\Gamma_f
\]
has both factors satisfying $\mathscr P$ by <1>5--<1>6.  Property (b) gives $\mathscr P$ for their composition.
This proves part (e).
:::

<1>8. Let
\[
f:X\longrightarrow Y
\]
have $\mathscr P$.  The composite
\[
X_{\mathrm{red}}
\hookrightarrow X
\xrightarrow{f}
Y
\]
has $\mathscr P$.
::: {.proof}
The reduction morphism
\[
i_X:X_{\mathrm{red}}\hookrightarrow X
\]
is a closed immersion, hence has $\mathscr P$ by (a).
The morphism $f$ has $\mathscr P$ by hypothesis.
Therefore the composite
\[
f\circ i_X:X_{\mathrm{red}}\to Y
\]
has $\mathscr P$ by (b).
:::

<1>9. The composite in <1>8 factors uniquely as
\[
X_{\mathrm{red}}
\xrightarrow{f_{\mathrm{red}}}
Y_{\mathrm{red}}
\xrightarrow{i_Y}
Y.
\]
::: {.proof}
The scheme $X_{\mathrm{red}}$ is reduced.  By the universal property of the reduction of $Y$, every morphism from a reduced scheme to $Y$ factors uniquely through
\[
i_Y:Y_{\mathrm{red}}\hookrightarrow Y.
\]
The resulting morphism is exactly $f_{\mathrm{red}}$.
:::

<1>10. The morphism
\[
i_Y:Y_{\mathrm{red}}\hookrightarrow Y
\]
is separated.
::: {.proof}
It is a closed immersion.  Every closed immersion is separated.
:::

<1>11. The reduced morphism
\[
\boxed{
f_{\mathrm{red}}:X_{\mathrm{red}}\longrightarrow Y_{\mathrm{red}}
}
\]
has $\mathscr P$.
::: {.proof}
By <1>8--<1>9, the composite
\[
i_Y\circ f_{\mathrm{red}}
\]
has $\mathscr P$.  By <1>10, $i_Y$ is separated.
Applying part (e), proved in <1>4--<1>7, to
\[
X_{\mathrm{red}}
\xrightarrow{f_{\mathrm{red}}}
Y_{\mathrm{red}}
\xrightarrow{i_Y}
Y
\]
shows that $f_{\mathrm{red}}$ has $\mathscr P$.
This proves part (f).
:::

<1>12. Q.E.D.
::: {.proof}
Step <1>3 proves part (d), <1>7 proves part (e), and <1>11 proves part (f).
:::
:::
