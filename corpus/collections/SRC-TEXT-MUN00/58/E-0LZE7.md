---
schema: qual/card@1
id: E-0LZE7
kind: problem
title: The figure eight and the theta space are homotopy equivalent
classification:
  areas:
  - topology
  topics:
  - Homotopy Equivalence
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
- event: source-checked
  by: claude
  date: 2026-11-11
  note: >-
    Checked line by line against Munkres, Topology (2000), Section 58 Exercise 4, printed p. 366,
    with Example 3 of Section 58 and the homotopy invariance of $\pi_1$. The card describes $f$ and $g$ explicitly and proves $g\circ f\simeq\mathrm{id}_X$ by cancelling the constant loops. For $f\circ g$ it uses that the quotient of the theta space by its central segment, a contractible subcomplex, is a homotopy equivalence, so that $g$ is one and $f$, being a one-sided inverse, is the other; an explicit homotopy exists as well, by sliding each of $f\circ g$'s trips along the central segment, and the card's route is correct on the book's definitions. No complete published solution was located for this exercise: dbFin's Chapter 9 pages run from Section 51 to Section 56 only, and every set searched is listed in the COMPLAINTS.md entry for Sections 57 to 60. The proof is the card's own and every step was checked against the book.
- event: source-checked
  by: claude
  date: 2026-11-14
  note: >-
    A published answer has now been located: Pearse, *Topology (2nd ed.) — James R. Munkres*,
    solutions, Cornell 2005, §58 Exercise 4, his pp. 22-23, read in the MinerU extraction
    tmp/sources/cornell-erin-munkres.md. The solution transcribes the source's description of the
    two maps — the figure eight collapsed onto the vertical bar of the theta, and the bar collapsed
    to the join point — and states what the source gives only in words with its Figure 7, namely
    the two homotopies. Those are supplied here from the book rather than asserted: the figure
    eight and the theta space are both deformation retracts of the doubly punctured plane by
    Examples 2 and 3 on printed p. 362, and composing the inclusion of one space with the
    retraction onto the other gives maps homotopy inverse by §51 Exercise 1 (printed p. 330). So
    the part of the exercise with no written source is the existence of the two homotopies, and
    the card says so. Checked against the book: the exercise on printed p. 367 (the earlier note
    above gave printed p. 366, which is where the exercise list begins; this exercise is on the
    second page of it), the definition of homotopy inverse on printed p. 363, and Examples 2 and 3
    on printed p. 362. Correction to the note of 2026-11-11: that proof rested on the quotient of
    the theta by its central segment being a homotopy equivalence through a contractible
    subcomplex, which is a later chapter's result and was not available in Section 58; the
    argument now on the card uses only Examples 2 and 3.
- event: solution-written
  by: claude
  date: 2026-11-14
  note: >-
    The solution was rewritten as the description plus the check above, in Lamport form.
- event: solution-written
  by: claude
  date: 2026-11-14
  note: >-
    The closing step claimed that $f=r_Y\circ i_X$ and $g=r_X\circ i_Y$ *are* the maps the source
    describes, "a map into the plane followed by a retraction collapses a region to a graph", and
    called what is collapsed "the region the figure eight encloses". Both are unsupported: the
    retractions of Examples 2 and 3 are given by a picture and by "we leave it to you to sketch the
    maps involved", so no text fixes where a point of the figure eight goes, and the source's own
    words collapse the points of the figure eight that lie inside its dotted line, the lens between
    the two crossing points, not the interior of either loop. The step now states the description
    of the two composites, records the source's picture-level description with that correction, and
    says plainly that the agreement of the composites with the drawn maps is not something either
    text settles; what is proved, and all the exercise asks, is that the composites are homotopy
    inverse. The two homotopies and the argument from Examples 2 and 3 are unchanged. Checked
    against the book: the exercise on printed p. 367, the definition of homotopy inverse on printed
    p. 363, and Examples 2 and 3 on printed p. 362; read in Pearse's extraction with his Figure 7 on
    his p. 23.
- event: solution-written
  by: claude
  date: 2026-11-15
  note: >-
    Two repairs, from a second reader's report on this card. (1) The description of
    Pearse's Figure 7 is deleted. The card had said that the figure draws the figure
    eight as two circles crossing in two points with a lens between the crossing
    points; the figure eight is two circles meeting in a single point (Lemma 60.5,
    printed p. 373, "Let X be the union of two circles A and B whose intersection
    consists of the single point x0"), and Pearse's text has no words for that
    figure at all, only "Define the maps as indicated in Figure 7" followed by two
    sentences about which points go to the bar. (2) The exercise asks for maps, and
    the card described none: it named the composites of the two retractions of the
    doubly punctured plane, which the book gives by pictures and, for Example 3,
    says only "we leave it to you to sketch the maps involved", and then said that
    no text fixes where a point goes. The solution now defines g on the three closed
    pieces of the theta space — the two semicircles by the two loops of the figure
    eight and the bar to x0 — and f on each loop by a formula, proves both
    continuous, and proves the two homotopies: g o f is alpha o phi with
    phi = min(2t,1), the straight-line homotopy of phi to the identity gives
    g o f homotopic to the identity, and f o g is homotoped by an explicit H on
    Y x I given piecewise on the bar and the two semicircles. Both were checked at
    u = 0, at u = 1 and on the three pairwise intersections of the closed pieces.
    The reader's own formulas were checked and corrected in one place: with f
    traversing the semicircle against the sense in which g reads it, the composite
    g o f runs each loop backwards and is not homotopic to the identity, so f here
    traverses R and L in the direction of the parametrizations rho and lambda and
    closes each loop along the bar. Checked against the book: the exercise on
    printed p. 366 -- the earlier notes on this card gave p. 367, and the exercise
    list of §58, exercises 1 to 8, is on printed p. 366, read on the page image of
    the PDF -- Examples 2 and 3 on printed p. 362, the definition of homotopy
    inverse on printed p. 363, Lemma 60.5 on printed p. 373, Theorem 18.3 on
    printed p. 108, Theorem 22.1 on printed p. 140, Theorem 22.2 on printed p. 142
    and §29 Exercise *11(a) on printed p. 186. Not claimed: that the formulas
    reproduce Pearse's drawn maps point by point, which neither text settles.
---

::: {.exercise}

Let $X$ be the figure eight and let $Y$ be the theta space.
Describe maps $f: X \to Y$ and $g: Y \to X$ that are homotopy inverse to each other.
:::

::: {.solution}
The exercise is §58 Exercise 4. It asks for maps $f:X\to Y$ and
$g:Y\to X$ that are homotopy inverse to each other, and both maps and both
homotopies are written out below.

Fix the spaces. Let
$$
Y=S^1\cup\bigl(\theset 0\times[-1,1]\bigr)\ \subseteq\ \RR^2
$$
be the theta space of Example 3, write $J=\theset
0\times[-1,1]$ for its bar, $y_1=(0,1)$ and $y_2=(0,-1)$ for the two points where
the bar meets the circle, and $R$, $L$ for the closed right and left semicircles,
so that $Y=R\cup L\cup J$ and $R\cap L=\theset{y_1,y_2}$. Parametrize the two
semicircles from $y_2$ to $y_1$ by
$$
\rho(t)=(\sin\pi t,-\cos\pi t),\qquad
\lambda(t)=(-\sin\pi t,-\cos\pi t)\qquad(t\in I),
$$
so that $\rho(I)=R$, $\lambda(I)=L$, $\rho(0)=\lambda(0)=y_2$ and
$\rho(1)=\lambda(1)=y_1$. Let $X=A\cup B$ be the figure eight, the union of two
circles of $\RR^2$ whose intersection is the single point $x_0$ (Lemma 60.5,
printed p. 373), and let $\alpha,\beta:I\to X$ be loops with $\alpha(I)=A$ and
$\beta(I)=B$, each injective off the endpoints and carrying $0$ and $1$ to $x_0$;
such loops exist, a circle being a continuous image of $I$ that identifies the two
endpoints.

Pearse, *Topology (2nd ed.) — James R. Munkres*, solutions, Cornell 2005, §58
Exercise 4, his pp. 22--23, read in `tmp/sources/cornell-erin-munkres.md`,
describes the two maps in words: its $f$ maps the points of the figure eight
inside its dotted line to the vertical bar of the theta space, and its $g$ maps
the vertical bar to the "centre point" of the figure eight where the two loops
connect. It gives no formula for either map, and states the two homotopies only as
a description of a motion.

::: pf

::: {.pf-step #mapg}
$g(\rho(t))=\alpha(t)$ and $g(\lambda(t))=\beta(t)$ for $t\in I$, together with
$g(y)=x_0$ for $y\in J$, define a continuous map $g:Y\to X$.

::: pf-proof
$R$, $L$ and $J$ are closed subsets of $Y$ with union $Y$. On $R\cap
L=\theset{y_1,y_2}$ the prescriptions agree, because $\rho(0)=\lambda(0)=y_2$ and
$\rho(1)=\lambda(1)=y_1$ give $g(y_2)=\alpha(0)=x_0=\beta(0)$ and
$g(y_1)=\alpha(1)=x_0=\beta(1)$, and $x_0$ is the value prescribed on $J$ as well;
and $R\cap J=\theset{y_1}$, $L\cap J=\theset{y_2}$, where the value prescribed on
the semicircle is again $x_0$. So $g$ is well defined, and it is continuous by the
pasting lemma (Theorem 18.3).
:::

:::

::: {.pf-step #mapf}
$f(x_0)=y_2$ together with
$$
f(\alpha(t))=\begin{cases}\rho(2t), & 0\le t\le\tfrac12,\\[2pt]
(0,\,3-4t), & \tfrac12\le t\le1,\end{cases}
\qquad
f(\beta(t))=\begin{cases}\lambda(2t), & 0\le t\le\tfrac12,\\[2pt]
(0,\,3-4t), & \tfrac12\le t\le1,\end{cases}
$$
defines a continuous map $f:X\to Y$.

::: pf-proof
The two lines for $\alpha$ agree at $t=\tfrac12$, where $\rho(1)=y_1=(0,1)$ and
$3-4t=1$, and the second line ends at $(0,-1)=y_2$; so they give a well-defined
map of $A=\alpha(I)$ into $Y$, and the two lines for $\beta$ a map of
$B=\beta(I)$. Each is continuous: $I$ is compact and $A$ is Hausdorff, so
$\alpha:I\to A$ is a closed surjection and therefore a quotient map, and by
Theorem 22.2 a map out of $A$ is continuous as soon as its
composite with $\alpha$ is; the composite here is the piecewise formula, which is
continuous on the two closed halves of $I$, agrees at their common point, and
takes the value $y_2$ at both $t=0$ and $t=1$, so it is constant on the fibre
$\alpha^{-1}(x_0)=\theset{0,1}$. Finally $A\cap B=\theset{x_0}$
and both prescriptions give $y_2$ at $x_0$, so $f$ is continuous on
$X=A\cup B$ by the pasting lemma.
:::

:::

::: {.pf-step #left}
$g\circ f\simeq\operatorname{id}_X$.

::: pf-proof
For $x=\alpha(t)$ the composite is
$$
(g\circ f)\bigl(\alpha(t)\bigr)=g\bigl(f(\alpha(t))\bigr)=
\begin{cases}\alpha(2t), & 0\le t\le\tfrac12,\\ x_0, & \tfrac12\le t\le1,\end{cases}
=\alpha\bigl(\varphi(t)\bigr),
$$
where $\varphi(t)=\min(2t,1)$; the second line uses that $g$ carries the whole bar
$J$ to $x_0$ and that $x_0=\alpha(1)$. The same computation with $\beta$ in place
of $\alpha$ gives $(g\circ f)(\beta(t))=\beta(\varphi(t))$, and
$(g\circ f)(x_0)=g(y_2)=x_0=\alpha(\varphi(0))$.

The map $\varphi:I\to I$ satisfies $\varphi(0)=0$ and $\varphi(1)=1$, and
$\Phi(t,u)=(1-u)\varphi(t)+ut$ is a homotopy of $\varphi$ to
$\operatorname{id}_I$ through maps of $I$ into $I$, because $I$ is convex. Put
$H(x,u)=\alpha(\Phi(t,u))$ for $x=\alpha(t)\in A$ and $H(x,u)=\beta(\Phi(t,u))$
for $x=\beta(t)\in B$. The two prescriptions give $x_0$ on
$A\cap B=\theset{x_0}$, and on $A$ alone the two parameters over $x_0$ also give a
single value, $\alpha(\Phi(0,u))=\alpha(0)=x_0=\alpha(1)=\alpha(\Phi(1,u))$, so
$H$ is well defined; and each prescription is continuous: $\alpha\times\operatorname{id}_I$
is a quotient map, since $\alpha$ is one and $I$ is compact Hausdorff and
therefore locally compact Hausdorff (§29 Exercise *11(a)), and
the composite $H\circ(\alpha\times\operatorname{id}_I)$, namely
$(t,u)\mapsto\alpha(\Phi(t,u))$, is continuous. So $H:X\times I\to X$ is
continuous by the pasting lemma on the closed cover
$X\times I=(A\times I)\cup(B\times I)$. Also $H(x,0)=(g\circ f)(x)$ and $H(x,1)=x$
for every $x\in X$. Hence $g\circ f\simeq\operatorname{id}_X$.
:::

:::

::: {.pf-step #right}
$f\circ g\simeq\operatorname{id}_Y$.

::: pf-proof
Write $k=f\circ g$. By step [](#mapf){.pf-ref} and the definition of $g$,
$$
k\bigl(\rho(t)\bigr)=f\bigl(\alpha(t)\bigr)=
\begin{cases}\rho(2t), & 0\le t\le\tfrac12,\\ (0,\,3-4t), & \tfrac12\le t\le1,\end{cases}
$$
$k(\lambda(t))$ is the same with $\lambda$ in place of $\rho$, and
$k(y)=f(x_0)=y_2$ for $y\in J$.

Define $H:Y\times I\to Y$ on the three closed pieces of $Y\times I$ as follows:
$$
H\bigl((0,y),u\bigr)=(0,\,u(y+1)-1)
$$
on $J\times I$, and on $R\times I$
$$
H\bigl(\rho(t),u\bigr)=
\begin{cases}
\rho\Bigl(\dfrac{2t}{1+u}\Bigr), & 2t\le 1+u,\\[8pt]
(0,\,3+2u-4t), & 2t\ge 1+u,
\end{cases}
$$
with $\lambda$ in place of $\rho$ on $L\times I$. Each piece is continuous and
takes its values in $Y$: on the bar, $u(y+1)-1$ lies between $-1$ and $1$; on the
semicircle the two lines agree where $2t=1+u$, both giving $\rho(1)=(0,1)$, since
$3+2u-4t=1$ there, the first line maps into $R$, and on the second the parameter
$t$ runs over $[\tfrac{1+u}{2},1]$, so the second coordinate $3+2u-4t$ runs over
$[2u-1,1]\subseteq[-1,1]$ and the image lies in the bar.

The pieces agree on the pairwise intersections of those three closed sets.
$R\cap L=\theset{y_1,y_2}$: at $y_2=(0,-1)$ the value is $\rho(0)=\lambda(0)=y_2$,
from the first line since $0\le1+u$, and it equals $H(y_2,u)=(0,-1)$; at
$y_1=(0,1)$ the value is $(0,2u-1)$ for $u<1$, from the second line, and
$\rho(1)=(0,1)=(0,2u-1)$ for $u=1$ from the first, which equals
$H(y_1,u)=(0,2u-1)$. And $R\cap J=\theset{y_1}$, $L\cap J=\theset{y_2}$ are the
two points just computed, where the bar formula gives the same values. So $H$ is
continuous by the pasting lemma on the closed cover
$Y\times I=(R\times I)\cup(L\times I)\cup(J\times I)$.

Finally $H(y,0)=k(y)$ on each of the three pieces, by the computation of $k$, and
$H(y,1)=y$: on the bar $H((0,y),1)=(0,y)$; on $R$ the condition $2t\le1+u$ holds
at $u=1$ for every $t$, so $H(\rho(t),1)=\rho(t)$; and likewise on $L$. Hence
$f\circ g\simeq\operatorname{id}_Y$.
:::

:::

::: {.pf-step #conclusion}
$\boxed{f\ \text{and}\ g\ \text{are homotopy inverse, so the figure eight and the
theta space are homotopy equivalent}.}$

::: pf-proof
$f$ is continuous by step [](#mapf){.pf-ref}, $g$ by step
[](#mapg){.pf-ref}, and the two composites are homotopic to the respective
identities by steps [](#left){.pf-ref} and [](#right){.pf-ref}; that is the
definition of homotopy inverse on printed p. 363, and the exercise's two maps are
described.

What the formulas say, in the source's terms: $g$ collapses the bar of the theta
space to $x_0$ and reads the two semicircles as the two loops of the figure eight;
$f$ carries each loop of the figure eight once along the corresponding semicircle
and back along the bar to $y_2$. The direction is part of the description, since
$f$ traverses $R$ and $L$ in the direction of $\rho$ and $\lambda$, which is the
direction $g$ reads them: that is what makes $g\circ f$ run along each loop
monotonically, as step [](#left){.pf-ref} computes. The source states the two
homotopies only as a motion, and steps [](#left){.pf-ref} and
[](#right){.pf-ref} are the homotopies themselves. Nothing here asserts that the
formulas reproduce Pearse's drawing point by point; the exercise asks for maps
that are homotopy inverse, and the steps supply them.
:::

:::

:::
:::
