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

For an open book $B=(L,\pi)$ of $S^3$, orient each page so that a vector $v$ with $d\pi(v)>0$ followed by an oriented basis of the page is an oriented basis of $S^3$, and orient $L$ as the boundary of the pages.
Let $\mathcal C(B)$ be the set of nowhere-zero vector fields $R$ on $S^3$ with $d\pi(R)>0$ on $S^3-L$ and $R$ a positive multiple of the oriented tangent of $L$ at each point of $L$.
Any two elements $R_0,R_1$ of $\mathcal C(B)$ are joined by the path $R_\tau=(1-\tau)R_0+\tau R_1$, $0\le\tau\le1$, in $\mathcal C(B)$.

::: pf-proof

At a point off $L$, both $d\pi(R_0)$ and $d\pi(R_1)$ are positive, so $d\pi(R_\tau)>0$; in particular $R_\tau\ne0$ there.
At a point of $L$, both $R_0$ and $R_1$ are positive multiples of the oriented tangent of $L$, so $R_\tau$ is a positive multiple of it as well.

:::

:::

::: {.pf-step #s1-21}

Let $\xi=\ker\alpha$ be a plane field co-oriented by $\alpha$.
If $\alpha(R')>0$ for some $R'\in\mathcal C(B)$, then for every $R\in\mathcal C(B)$ the oriented plane field $\xi$ is homotopic to $R^\perp$, the orthogonal complement of $R$ in the round metric co-oriented by $R$.

::: pf-proof

An oriented plane field is the same datum as its positive unit normal, so it suffices to join the unit normal $n$ of $\xi$ to $R/\abs{R}$ through nowhere-zero vector fields.
Since $\alpha(R')>0$, the field $R'$ lies on the positive side of $\xi$, so $\langle n,R'\rangle>0$ and the fields $(1-\tau)n+\tau R'$ have positive inner product with $n$; they never vanish.
Step [](#s1-20){.pf-ref} joins $R'$ to $R$ through nowhere-zero fields.
Normalizing the concatenated path gives the homotopy of plane fields.

:::

:::

::: {.pf-step #s1-22}

Let $R_+(z_1,z_2)=(iz_1,iz_2)=\partial_{\theta_1}+\partial_{\theta_2}$.
Then $R_+\in\mathcal C(H_+)$, and $\xi_{\mathrm{std}}$ is homotopic to $R_+^\perp$.

::: pf-proof

Steps [](#s1-9){.pf-ref} and [](#s1-10){.pf-ref} at $t=0$, for the positive contact form $\alpha_{\mathrm{std}}$, show that $ds\wedge d\theta_1\wedge d\theta_2$ is positive.
For $H_+$ one has $d\pi_+=d\theta_1+d\theta_2$, so $d\pi_+(R_+)=2>0$, and the page tangent vectors $\partial_s$, $\partial_{\theta_1}-\partial_{\theta_2}$ satisfy
$$
ds\wedge d\theta_1\wedge d\theta_2\bigl(R_+,\partial_s,\partial_{\theta_1}-\partial_{\theta_2}\bigr)=2>0,
$$
so $(\partial_s,\partial_{\theta_1}-\partial_{\theta_2})$ is an oriented basis of the page.
At the binding circle $\{z_2=0\}$, where $s=1$, the outward normal of the page is $\partial_s$, and the boundary orientation is $\partial_{\theta_1}-\partial_{\theta_2}$, which equals $\partial_{\theta_1}$ on that circle because $\partial_{\theta_2}$ vanishes there.
At $\{z_1=0\}$, where $s=0$, the outward normal is $-\partial_s$, and the boundary orientation is $-(\partial_{\theta_1}-\partial_{\theta_2})=\partial_{\theta_2}$ there.
On both circles $R_+$ is the oriented tangent, so $R_+\in\mathcal C(H_+)$.
Finally $\alpha_{\mathrm{std}}(R_+)=s+(1-s)=1>0$, and step [](#s1-21){.pf-ref} applies with $R'=R=R_+$.

:::

:::

::: {.pf-step #s1-23}

Model $H_-$ by the binding $L_-=\{z_1=0\}\cup\{z_2=0\}$ and
$$
\pi_-(z_1,z_2)=\frac{z_1\overline{z_2}}{\abs{z_1z_2}}=e^{i(\theta_1-\theta_2)}.
$$
With the orientations of step [](#s1-20){.pf-ref}, the binding is oriented by $-\partial_{\theta_1}$ on $\{z_2=0\}$ and by $\partial_{\theta_2}$ on $\{z_1=0\}$, and the vector field
$$
R_-=\Bigl(\tfrac32-2s\Bigr)\partial_{\theta_1}+\Bigl(\tfrac12-2s\Bigr)\partial_{\theta_2}
$$
lies in $\mathcal C(H_-)$.

::: pf-proof

The pages $\theta_1-\theta_2=\mathrm{const}$ are open annuli with ends on the two coordinate circles, exactly as in step [](#s1-3){.pf-ref}.
Here $d\pi_-=d\theta_1-d\theta_2$, the vector $\partial_{\theta_1}-\partial_{\theta_2}$ has $d\pi_-$-value $2$, and
$$
ds\wedge d\theta_1\wedge d\theta_2\bigl(\partial_{\theta_1}-\partial_{\theta_2},\partial_s,\partial_{\theta_1}+\partial_{\theta_2}\bigr)=-2,
$$
so $\bigl(\partial_s,-(\partial_{\theta_1}+\partial_{\theta_2})\bigr)$ is an oriented basis of the page.
At $s=1$ the outward normal is $\partial_s$ and the boundary orientation is $-(\partial_{\theta_1}+\partial_{\theta_2})=-\partial_{\theta_1}$; at $s=0$ the outward normal is $-\partial_s$ and the boundary orientation is $\partial_{\theta_1}+\partial_{\theta_2}=\partial_{\theta_2}$.
Compared with the orientations $\partial_{\theta_1}$, $\partial_{\theta_2}$ of $H_+$, exactly one component is reversed, so the binding is the Hopf link of linking number $-1$, and this open book is $H_-$.

Write $u(s)=\tfrac32-2s$ and $v(s)=\tfrac12-2s$.
In coordinates $R_-(z_1,z_2)=(iu\,z_1,iv\,z_2)$; since $u$ and $v$ are polynomials in $s=\abs{z_1}^2$, $R_-$ is smooth on $S^3$, and $\abs{R_-}^2=u^2s+v^2(1-s)$.
On $0<s<1$ this vanishes only if $u=v=0$, which is impossible since $u-v=1$; at $s=1$ it equals $u(1)^2=\tfrac14$, and at $s=0$ it equals $v(0)^2=\tfrac14$.
Off the binding $d\pi_-(R_-)=u-v=1>0$.
On $\{z_2=0\}$, $R_-=u(1)\partial_{\theta_1}=\tfrac12(-\partial_{\theta_1})$, and on $\{z_1=0\}$, $R_-=v(0)\partial_{\theta_2}=\tfrac12\partial_{\theta_2}$; both are positive multiples of the oriented binding tangent.

:::

:::

::: {.pf-step #s1-24}

The contact structure $\xi_-$ supported by $H_-$ is homotopic to $R_-^\perp$.

::: pf-proof

By Theorem 4.52, $\xi_-$ is, up to isotopy, the Thurston--Winkelkemper structure $\ker\alpha$ of the notes.
On the mapping torus of the monodromy, with circle coordinate $z$ and $d\pi=dz$, one has $\alpha=dz+\epsilon\eta$ with $\epsilon$ small, so $\alpha(\partial_z)>0$ and $d\pi(\partial_z)=1>0$.
Near a binding component, in coordinates $(r,\theta,z')$ with the binding $\{r=0\}$ oriented by $\partial_{z'}$ and the pages $\{\theta=\mathrm{const}\}$, one has $\alpha=dz'+\tfrac{r^2}{2}d\theta$; the field $\partial_{z'}+\kappa(r)\partial_\theta$, with $\kappa$ smooth, $\kappa(r)=r^2$ for small $r$, gives $\alpha$-value $1+\tfrac{r^2}{2}\kappa>0$, $d\theta$-value $\kappa>0$ off the binding, and equals $\partial_{z'}$ on it.
At each point off the binding the set of vectors $w$ with $\alpha(w)>0$ and $d\pi(w)>0$ is convex, and each of the two local fields lies in it on its domain, so a partition of unity subordinate to these two regions glues them to a field $R'\in\mathcal C(H_-)$ with $\alpha(R')>0$.
Step [](#s1-21){.pf-ref} with $R=R_-$, which lies in $\mathcal C(H_-)$ by step [](#s1-23){.pf-ref}, gives $\xi_-\simeq R_-^\perp$.
An isotopy of contact structures is a homotopy of plane fields, so the choice within the isotopy class does not matter.

:::

:::

::: {.pf-step #frame-maps}

Identify $S^3$ with the unit quaternions $q=z_1+z_2j$ in $\quaternions$, and trivialize $TS^3$ by the frame $(qi,qj,qk)$, so that an oriented plane field corresponds to the map $S^3\to S^2\subset\operatorname{Im}\quaternions$ sending $q$ to $\overline q\,n(q)$, where $n$ is its unit normal.
Let $h(q)=\overline q\,i\,q$ be the Hopf map, and for $x\in S^2$ write $x=t(x)\,i+y$ with $y\in\operatorname{span}(j,k)$.
Then $R_+^\perp$ corresponds to $h$, and $R_-^\perp$ corresponds to $g\circ h$, where
$$
g(x)=\frac{-t(x)\,x+\tfrac12 i}{\abs{-t(x)\,x+\tfrac12 i}}.
$$

::: pf-proof

Multiplication by the complex scalar $i$ is left multiplication, $iq=iz_1+(iz_2)j$, and right multiplication is $qi=iz_1+z_2(ji)=iz_1-(iz_2)j$.
Hence $R_+(q)=iq$ and $\partial_{\theta_1}-\partial_{\theta_2}=qi$.
Both are unit vectors, so $\overline q R_+(q)=\overline q\,i\,q=h(q)$.
Writing $u=\tfrac32-2s$, $v=\tfrac12-2s$ as in step [](#s1-23){.pf-ref},
$$
R_-=\tfrac{u+v}{2}(\partial_{\theta_1}+\partial_{\theta_2})+\tfrac{u-v}{2}(\partial_{\theta_1}-\partial_{\theta_2})=(1-2s)\,iq+\tfrac12\,qi,
$$
so $\overline q R_-(q)=(1-2s)h(q)+\tfrac12 i$.
Using $\overline q=\overline{z_1}-z_2j$ and $jw=\overline w j$ for $w\in\CC$, a direct expansion gives
$$
h(z_1+z_2j)=\bigl(\abs{z_1}^2-\abs{z_2}^2\bigr)i+2i\,\overline{z_1}z_2\,j,
$$
whose $i$-coordinate is $2s-1$ and whose second term lies in $\operatorname{span}(j,k)$.
Thus $1-2s=-t(h(q))$, and normalizing gives $g(h(q))$.

:::

:::

::: {.pf-step #degree-zero}

The map $g:S^2\to S^2$ has degree $0$, so $g\circ h$ is null-homotopic, while $h$ generates $\pi_3(S^2)\cong\ZZ$.

::: pf-proof

For $x=ti+y$ the vector $-tx+\tfrac12 i$ has $i$-coordinate $\tfrac12-t^2$ and $(j,k)$-part $-ty$; these vanish together only if $t^2=\tfrac12$ and $y=0$, which is impossible, so $g$ is smooth.
Compute the preimages of $-i$: $g(x)=-i$ forces $-ty=0$ and $\tfrac12-t^2<0$, so $y=0$ and $x=\pm i$, and both points do map to $-i$.
Near $x=-i$ write $x=-i+y+O(\abs{y}^2)$ with $y\in\operatorname{span}(j,k)$; then $-tx+\tfrac12i=-\tfrac12i+y+O(\abs{y}^2)$, so $g(x)=-i+2y+O(\abs{y}^2)$.
The derivative $T_{-i}S^2\to T_{-i}S^2$ is multiplication by $2$, so the local degree is $+1$.
Near $x=i$ write $x=i+y+O(\abs{y}^2)$; then $-tx+\tfrac12i=-\tfrac12i-y+O(\abs{y}^2)$, so $g(x)=-i-2y+O(\abs{y}^2)$.
The tangent planes $T_iS^2$ and $T_{-i}S^2$ are both $\operatorname{span}(j,k)$ but carry opposite orientations, since their outward normals $i$ and $-i$ are opposite, and $-2\,\mathrm{id}$ preserves the orientation of a plane; so this local degree is $-1$.
Thus $-i$ is a regular value and $\deg g=1-1=0$.
By the Hopf degree theorem $g$ is null-homotopic, hence so is $g\circ h$.
The Hopf map $h$ has Hopf invariant $1$ and generates $\pi_3(S^2)\cong\ZZ$, so it is not null-homotopic.

:::

:::

::: {.pf-step #s1-25}

Consequently, the plane field supported by $H_-$ is not homotopic to the standard contact plane field:
$$
\boxed{
\xi_-\not\simeq\xi_{\mathrm{std}}}.
$$

::: pf-proof

By steps [](#s1-22){.pf-ref} and [](#s1-24){.pf-ref}, $\xi_{\mathrm{std}}\simeq R_+^\perp$ and $\xi_-\simeq R_-^\perp$.
Under the bijection between homotopy classes of oriented plane fields and $[S^3,S^2]$ given by the fixed frame, step [](#frame-maps){.pf-ref} sends these to the classes of $h$ and $g\circ h$, which differ by step [](#degree-zero){.pf-ref}.

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

:::

:::
