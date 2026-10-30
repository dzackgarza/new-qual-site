---
schema: qual/card@1
id: P-UTCT-4-53
kind: problem
title: Positive and negative Hopf band open books of $S^3$ and their contact structures
classification:
  areas:
  - topology
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-12
  note: Checked against Exercise 4.53 of the retained George D. Torres notes from Bob Gompf's M392C Contact Topology course, Fall 2017.
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Stated the definitions of open books, H_+ and H_-, support, and T(M) from pp. 37-41 of Gompf Contact Topology.pdf.
---

::: {.problem}
An open book decomposition of a $3$-manifold $M$ is a link $L \subset M$ (the binding) and a bundle structure $\pi : M \setminus L \to S^1$ by Seifert surfaces.
The Hopf decomposition $H_+$ of $S^3$ is the open book along positive Hopf links; the negative Hopf decomposition $H_-$ is the same but along negative Hopf links.
An open book decomposition $B$ supports a contact structure $\xi$ if there exists a one-parameter family of plane fields $\xi_t$, $0 \leq t \leq 1$, such that $\xi_0 = \xi$, for all $t < 1$, $\xi_t$ is a contact structure transverse to the binding, and $\xi_1$ defines the foliation away from the link of $B$.
Let $\mathcal{T}(M)$ denote the set of tight, positive, oriented contact structures on $M$ modulo isotopy.

Show that $H_+$ supports the standard contact structure $\xi$ on $S^3$ using the Hopf fibration.
Show also that $H_-$ supports a different homotopy class of contact structure, which must therefore be overtwisted because $\#\mathcal{T}(S^3) = 1$.
:::

::: {.solution}

Write
$$
S^3
=
\left\{
(z_1,z_2)\in\CC^2:
\abs{z_1}^2+\abs{z_2}^2=1
\right\},
$$
and on the complement of the two coordinate circles use Hopf coordinates
$$
z_1=\sqrt{s}\,e^{i\theta_1},
\qquad
z_2=\sqrt{1-s}\,e^{i\theta_2},
\qquad
0<s<1.
$$

The standard contact form is
$$
\boxed{
\alpha_{\mathrm{std}}
=
s\,d\theta_1+(1-s)\,d\theta_2}.
$$

## The positive Hopf open book

::: pf

::: pf-step

The positive Hopf binding is
$$
\boxed{
L_+
=
\{z_1=0\}\cup\{z_2=0\}}.
$$


::: pf-proof

The two coordinate circles are fibers of the Hopf fibration and form the
positive Hopf link with their complex orientations.

:::

:::

::: pf-step

On $S^3-L_+$, define
$$
\boxed{
\pi_+(z_1,z_2)
=
\frac{z_1z_2}{\abs{z_1z_2}}
=
e^{i(\theta_1+\theta_2)}}.
$$


::: pf-proof

Away from the coordinate circles,
$$
z_1z_2\ne0,
$$
so its argument defines a map to $S^1$.

:::

:::

::: {.pf-step #s1-3}

The fibers of $\pi_+$ are the interiors of annuli whose boundary is
$L_+$, so $(L_+,\pi_+)$ is the positive Hopf open book $H_+$.


::: pf-proof

Fixing
$$
\theta_1+\theta_2=\vartheta
$$
leaves the radial parameter $s\in(0,1)$ and one angular parameter free,
giving an open annulus. As $s\to0$ and $s\to1$, its two ends approach
the two coordinate circles. The induced boundary orientations give linking
number $+1$.

:::

:::

::: {.pf-step #s1-4}

For $0\le t<1$, define
$$
f_t(s)
=
\frac{s}{1-t+ts}
$$
and
$$
g_t(s)
=
\frac{1-s}{1-t+t(1-s)}.
$$


::: pf-proof

For $t<1$, both denominators are strictly positive on $[0,1]$.

:::

:::

::: {.pf-step #s1-5}

Define
$$
\boxed{
\alpha_t
=
f_t(s)\,d\theta_1
+
g_t(s)\,d\theta_2}.
$$


::: pf-proof

Near $s=0$,
$$
f_t(s)
=
\frac{s}{1-t+O(s)},
$$
so $f_t(s)d\theta_1$ has the standard smooth polar form
$O(r_1^2)d\theta_1$. Likewise near $s=1$,
$$
g_t(s)=O(r_2^2),
$$
so $\alpha_t$ extends smoothly across both binding circles for every
$t<1$.

:::

:::

::: {.pf-step #s1-6}

At $t=0$,
$$
\boxed{
\alpha_0
=
s\,d\theta_1+(1-s)\,d\theta_2
=
\alpha_{\mathrm{std}}}.
$$


::: pf-proof

Substitute $t=0$ into the functions in step [](#s1-4){.pf-ref}.

:::

:::

::: {.pf-step #s1-7}

The derivatives are
$$
\boxed{
f_t'(s)
=
\frac{1-t}{(1-t+ts)^2}>0}
$$
and
$$
\boxed{
g_t'(s)
=
-\frac{1-t}
{(1-t+t(1-s))^2}<0}.
$$


::: pf-proof

Differentiate the two quotient expressions from step [](#s1-4){.pf-ref}. Since $t<1$,
the numerator $1-t$ is positive.

:::

:::

::: pf-step

One has
$$
d\alpha_t
=
f_t'(s)\,ds\wedge d\theta_1
+
g_t'(s)\,ds\wedge d\theta_2.
$$


::: pf-proof

The coefficient functions depend only on $s$, and the angular
$1$-forms are closed on the complement of the binding.

:::

:::

::: {.pf-step #s1-9}

The contact volume form is
$$
\boxed{
\alpha_t\wedge d\alpha_t
=
\left(
g_t f_t'-f_t g_t'
\right)
ds\wedge d\theta_1\wedge d\theta_2}.
$$


::: pf-proof

Expand the wedge product. The terms involving
$$
d\theta_1\wedge ds\wedge d\theta_1
$$
or
$$
d\theta_2\wedge ds\wedge d\theta_2
$$
vanish, and the two cross terms combine with the displayed coefficient.

:::

:::

::: {.pf-step #s1-10}

For every $t<1$,
$$
\boxed{
g_t f_t'-f_t g_t'>0}.
$$


::: pf-proof

On $0<s<1$,
$$
f_t>0,\qquad g_t>0
$$
by step [](#s1-4){.pf-ref}. Step [](#s1-7){.pf-ref} gives
$$
f_t'>0,\qquad g_t'<0.
$$
Hence
$$
g_tf_t'>0
$$
and
$$
-f_tg_t'>0,
$$
so their sum is positive.

:::

:::

::: {.pf-step #s1-11}

Thus
$$
\boxed{
\xi_t=\ker\alpha_t}
$$
is a positive contact structure for every $0\le t<1$.


::: pf-proof

Steps [](#s1-9){.pf-ref} through [](#s1-10){.pf-ref} show
$$
\alpha_t\wedge d\alpha_t
$$
is a positive volume form on the complement of the binding, and the smooth
local models from step [](#s1-5){.pf-ref} extend this positivity across the binding.

:::

:::

::: {.pf-step #s1-12}

For $0<s<1$,
$$
\lim_{t\to1^-}f_t(s)=1
\qquad\text{and}\qquad
\lim_{t\to1^-}g_t(s)=1.
$$


::: pf-proof

For fixed $s\in(0,1)$,
$$
1-t+ts\to s
$$
and
$$
1-t+t(1-s)\to1-s.
$$
Divide numerator by the corresponding limit.

:::

:::

::: {.pf-step #s1-13}

Hence away from the binding,
$$
\boxed{
\alpha_t
\longrightarrow
d\theta_1+d\theta_2}.
$$


::: pf-proof

Apply step [](#s1-12){.pf-ref} coefficientwise.

:::

:::

::: {.pf-step #s1-14}

The plane field
$$
\ker(d\theta_1+d\theta_2)
$$
is tangent to the pages of $H_+$.


::: pf-proof

The pages are the level sets of
$$
\theta_1+\theta_2.
$$
Their tangent spaces are exactly the kernel of its differential
$$
d\theta_1+d\theta_2.
$$

:::

:::

::: {.pf-step #s1-15}

The contact structures $\xi_t$ are transverse to the binding for
every $t<1$.


::: pf-proof

At the component $s=1$, the binding tangent is
$$
\partial_{\theta_1}
$$
and
$$
\alpha_t(\partial_{\theta_1})
=
f_t(1)
=
1.
$$
At the component $s=0$, the binding tangent is
$$
\partial_{\theta_2}
$$
and
$$
\alpha_t(\partial_{\theta_2})
=
g_t(0)
=
1.
$$
Thus neither binding tangent lies in $\xi_t$.

:::

:::

::: {.pf-step #s1-16}

Therefore
$$
\boxed{
H_+\text{ supports }\xi_{\mathrm{std}}}.
$$


::: pf-proof

By step [](#s1-6){.pf-ref},
$$
\xi_0=\ker\alpha_{\mathrm{std}}.
$$
Steps [](#s1-11){.pf-ref} and [](#s1-15){.pf-ref} give contact structures transverse to the binding for
all $t<1$. Steps [](#s1-13){.pf-ref} through [](#s1-14){.pf-ref} show that the limiting plane field away
from the binding is the page foliation. This is exactly Definition 4.51.

:::

:::

::: pf-step

This construction is the Hopf-fibration construction: the binding
components are Hopf fibers, and the pages are inverse images of meridional
arcs in
$$
S^2-\{\text{north},\text{south}\}.
$$


::: pf-proof

The Hopf fibration
$$
h:S^3\to\CP^1\cong S^2
$$
has the coordinate circles as fibers over $0$ and $\infty$. The angular
coordinate on the punctured base is represented in Hopf coordinates by
$$
\theta_1+\theta_2,
$$
so its level arcs lift to the pages in step [](#s1-3){.pf-ref}.

:::

:::

::: pf-step

The negative Hopf open book $H_-$ has annular pages whose two
boundary components form a Hopf link of linking number
$$
\boxed{-1}.
$$


::: pf-proof

This is the defining difference between the positive and negative Hopf
bands: the annulus has the opposite full twist.

:::

:::

::: pf-step

By Theorem 4.52, $H_-$ supports a unique positive contact structure
up to isotopy; denote it by
$$
\boxed{\xi_-}.
$$


::: pf-proof

Theorem 4.52 states that every open book supports a unique positive contact
structure up to isotopy.

:::

:::

::: {.pf-step #s1-20}

By Definition 4.51, $\xi_-$ is homotopic as an oriented plane field
to the canonical plane field obtained by smoothing the tangent planes to the
pages of $H_-$ near the binding.


::: pf-proof

A supporting family begins at $\xi_-$ and ends, away from the binding, at
the page foliation. The standard local smoothing near each binding component
extends this limiting page plane field to a nonsingular plane field on all of
$S^3$. The family itself supplies the homotopy.

:::

:::

::: {.pf-step #s1-21}

Under the Pontryagin--Thom correspondence from Section 1.3, the
canonical plane field of an open book is represented by a binding component
with its page framing.


::: pf-proof

Near a binding component, the smoothed page plane field rotates from the
page tangent plane to a nonsingular plane. Choose a regular value of the
associated Gauss map in this local rotation. Its inverse image is the binding
circle, and the derivative identifies its normal bundle with the framing
given by the inward normal direction in the page. This is precisely the page
framing.

:::

:::

::: {.pf-step #s1-22}

For a Hopf band, the framing number of either binding component with
its page framing equals the linking number of the two boundary components.


::: pf-proof

Push one binding component slightly into the annulus in the page-framing
direction. The pushed-off curve is isotopic through the annulus complement
of the original component to the other boundary component. Therefore the
linking number of the original component with its page-framed push-off is
the linking number of the two Hopf-link components.

:::

:::

::: {.pf-step #s1-23}

Hence the Pontryagin--Thom framing integer is
$$
\boxed{+1}
$$
for $H_+$ and
$$
\boxed{-1}
$$
for $H_-$, with the same choice of orientation convention.


::: pf-proof

Step [](#s1-22){.pf-ref} identifies the framing integer with the Hopf-link linking number.
The positive and negative Hopf links have linking numbers $+1$ and $-1$,
respectively.

:::

:::

::: {.pf-step #s1-24}

Framed links in $S^3$ with different framing integers are not
framed cobordant.


::: pf-proof

The Pontryagin--Thom correspondence identifies framed-cobordism classes of
framed $1$-manifolds in $S^3$ with
$$
[S^3,S^2]
\cong
\pi_3(S^2)
\cong
\ZZ.
$$
The integer can be computed as the linking number of a framed link with a
small framed push-off. Distinct integers therefore represent distinct
classes.

:::

:::

::: {.pf-step #s1-25}

Consequently, the plane field supported by $H_-$ is not homotopic
to the standard contact plane field:
$$
\boxed{
\xi_-\not\simeq\xi_{\mathrm{std}}}.
$$


::: pf-proof

By steps [](#s1-16){.pf-ref} and [](#s1-20){.pf-ref} through [](#s1-23){.pf-ref}, the two plane fields correspond under
Pontryagin--Thom to framed links with different integer invariants. Step
[](#s1-24){.pf-ref} says they cannot be homotopic.

:::

:::

::: {.pf-step #s1-26}

If $\xi_-$ were tight, then it would be isotopic to
$\xi_{\mathrm{std}}$.


::: pf-proof

Corollary 4.32 gives
$$
\#\mathcal T(S^3)=1.
$$
Thus every positive tight contact structure on $S^3$ is isotopic to the
standard one.

:::

:::

::: {.pf-step #s1-27}

Isotopic contact structures are homotopic as oriented plane fields.


::: pf-proof

An isotopy is, in particular, a continuous one-parameter family of contact
plane fields.

:::

:::

::: {.pf-step #s1-28}

Therefore $\xi_-$ is not tight.


::: pf-proof

If it were tight, step [](#s1-26){.pf-ref} would make it isotopic to
$\xi_{\mathrm{std}}$, and step [](#s1-27){.pf-ref} would make the two plane fields
homotopic. This contradicts step [](#s1-25){.pf-ref}.

:::

:::

::: {.pf-step #s1-29}

Hence
$$
\boxed{
H_-\text{ supports an overtwisted contact structure on }S^3}.
$$


::: pf-proof

A contact structure in dimension $3$ is either tight or overtwisted.
Step [](#s1-28){.pf-ref} rules out tightness.

:::

:::

::: pf-qed

Step [](#s1-16){.pf-ref} proves that $H_+$ supports the standard contact structure.
Steps [](#s1-25){.pf-ref} and [](#s1-29){.pf-ref} show that $H_-$ supports a different homotopy class
and that its supported contact structure is overtwisted.

:::

:::

:::
