---
schema: qual/card@1
id: P-TRIV-LA48
kind: problem
title: Arranging three stars by spaceship rotations and boosts
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Linear Algebra, Problem 48, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md. The source depends on Figures 1 and 2 (ship rotations and star positions). Flash preserves only their captions/image placeholders, so the graphical data required to determine the command sequence is unresolved.
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Replaced the editorial preamble and image placeholders with the Linear Algebra Problem 48 statement and descriptions of Figures 1 and 2 from pages 7-8 of the source PDF.
---

::: {.problem}
You are a spaceship pilot carrying a lonely watch in front of the main display while the rest of the crew sleep in anabiosis.
You can operate the spaceship by sending commands to the main computer.
You can rotate the ship by typing the commands *pitch angle* $\psi$, *yaw angle* $\theta$ and *roll angle* $\phi$ as shown on Fig. 1.
Besides, you can type the command *boost time* $T$, which turns the main engine on and accelerates the ship with the constant acceleration $g$ during the time $T$.
On the display, you see three bright stars around the point $O$ that depicts the longitudinal axis of the ship, see Fig. 2.
Give a series of commands that arrange them into a perfect triangle with the center $O$ and the side $d$.

Fig. 1 (pitch, yaw and roll of the ship) shows the ship along the axis $x$ with body axes $x, y, z$.
The pitch by $\psi$ turns $x$ and $y$ by the angle $\psi$ to $x'$ and $y'$, keeping $z$ fixed; the yaw by $\theta$ turns $x$ and $z$ by the angle $\theta$ to $x'$ and $z'$, keeping $y$ fixed; the roll by $\varphi$ turns $y$ and $z$ by the angle $\varphi$ to $y'$ and $z'$, keeping the longitudinal axis $x$ fixed.

Fig. 2 (positions of the stars), left panel: the three stars lie on the display at distances $r_1, r_2, r_3$ from $O$, at angles $\varphi_1 < \varphi_2 < \varphi_3$ measured from a horizontal line through $O$, all in the upper half of the display.
Right panel: the target configuration is an equilateral triangle with side $d$ centered at $O$, with a horizontal lower side and the third vertex above $O$.
:::

::: {.remark}
The retained source does not specify the map from a star's spatial direction to
its display coordinates, nor the law by which a boost changes those display
coordinates. Those data are necessary to determine the requested command
sequence. For example, a relativistic solution would require an explicit
aberration law together with a chosen projection of the celestial sphere onto
the display (such as stereographic projection), and the relation between the
command time $T$ and rapidity. Without such a rule, different physically
reasonable display models produce different transformations of the points
$(r_i,\varphi_i)$, so the problem is underdetermined as retained.
:::

::: {.solution}

The requested command sequence is not determined by the data in the problem
statement.

::: pf

::: pf-step

The displayed initial positions determine only three planar points
$$
p_i
=
r_i
(\cos\varphi_i,\sin\varphi_i),
\qquad
i=1,2,3.
$$


::: pf-proof

The source specifies for each star only its distance
$$
r_i
$$
from the center
$$
O
$$
of the display and its planar polar angle
$$
\varphi_i.
$$
Those are exactly the polar coordinates of the displayed point.
No third spatial coordinate or direction vector is specified.

:::

:::

::: {.pf-step #s1-2}

An equilateral triangle of side
$$
d
$$
centered at
$$
O
$$
has circumradius
$$
\boxed{R=\frac d{\sqrt3}}.
$$


::: pf-proof

The centroid of an equilateral triangle is two thirds of the way from a
vertex along an altitude.
The altitude has length
$$
\frac{\sqrt3}{2}d,
$$
so the distance from the centroid to a vertex is
$$
\frac23\cdot
\frac{\sqrt3}{2}d
=
\frac d{\sqrt3}.
$$

:::

:::

::: {.pf-step #s1-3}

With the orientation shown in the source, one possible ordered target
triple is
$$
\boxed{
q_1=
\left(
-\frac d2,
-\frac d{2\sqrt3}
\right),
\quad
q_2=
\left(
\frac d2,
-\frac d{2\sqrt3}
\right),
\quad
q_3=
\left(
0,
\frac d{\sqrt3}
\right).}
$$


::: pf-proof

The lower side is horizontal and has length
$$
d.
$$
The displayed three points have centroid
$$
(0,0),
$$
and their pairwise Euclidean distances are all
$$
d.
$$
Thus they are precisely the target configuration described in the problem.

:::

:::

::: {.pf-step #s1-4}

To determine commands, the problem must specify, for every command
sequence
$$
C=(\psi_1,\theta_1,\phi_1,T_1,\ldots),
$$
a transformation
$$
\boxed{
F_C:
\text{display positions}
\longrightarrow
\text{display positions}.}
$$


::: pf-proof

A command sequence solves the problem only if the resulting displayed star
positions satisfy
$$
F_C(p_i)=q_{\sigma(i)}
$$
for some permutation
$$
\sigma\in S_3.
$$
Therefore the equations that determine
$$
C
$$
cannot even be written until the action
$$
F_C
$$
on displayed positions is defined.

:::

:::

::: {.pf-step #s1-5}

The source does not determine the spatial direction of a star from its
displayed radius
$$
r.
$$


::: pf-proof

Let
$$
\alpha
$$
be the angle between a star's spatial direction and the longitudinal axis.
Two standard central projections give different relations between
$$
r
$$
and
$$
\alpha.
$$

For a gnomonic projection onto a display plane one may have
$$
r=\tan\alpha.
$$
For a stereographic projection one may instead have
$$
r=2\tan\frac\alpha2.
$$
Thus the same displayed radius
$$
r
$$
corresponds respectively to
$$
\alpha
=
\arctan r
$$
and
$$
\alpha
=
2\arctan\frac r2,
$$
which are unequal for generic
$$
r.
$$

The source specifies neither projection.
Hence the displayed data
$$
(r_i,\varphi_i)
$$
do not determine the three spatial directions on which the stated
three-dimensional pitch, yaw, and roll rotations act.

:::

:::

::: {.pf-step #s1-6}

Consequently, even the effect of a pure rotation on the displayed
points is not uniquely determined.


::: pf-proof

Take a star with displayed radius
$$
r>0.
$$
By step [](#s1-5){.pf-ref}, two projection conventions compatible with the source assign
different spatial polar angles to that same point.

Apply the same nontrivial pitch or yaw rotation in
$$
\RR^3.
$$
The two resulting rotated spatial directions are different because they
started from different directions.
Projecting them back with their respective display maps therefore gives, in
general, different new displayed positions.

Thus the numerical command
$$
(\psi,\theta,\phi)
$$
does not induce a uniquely determined transformation of the given
$$
(r_i,\varphi_i)
$$
from the information in the source.

:::

:::

::: {.pf-step #s1-7}

The effect of the boost command is even less determined by the source.


::: pf-proof

The statement gives only a proper-time or clock-time duration
$$
T
$$
and an acceleration magnitude
$$
g.
$$
It supplies no law relating a change of observer velocity to the apparent
directions of incoming light.

For example, a relativistic interpretation requires the aberration formula
relating the old and new celestial directions and a convention relating the
specified acceleration and time to the resulting rapidity.
A nonrelativistic display model would use a different rule.
Neither rule appears in the problem.

Hence there is no defined map
$$
F_T
$$
on displayed star positions associated to the command
$$
\text{boost time }T.
$$

:::

:::

::: {.pf-step #s1-8}

Therefore the equations
$$
F_C(p_i)=q_{\sigma(i)}
$$
that would determine a successful command sequence have no specified
left-hand side.


::: pf-proof

Step [](#s1-6){.pf-ref} shows that the rotational part of
$$
F_C
$$
depends on an unspecified projection convention.
Step [](#s1-7){.pf-ref} shows that the boost part is also unspecified.
Thus the source does not define the transformation
$$
F_C
$$
needed in step [](#s1-4){.pf-ref}.

:::

:::

::: {.pf-step #s1-9}

Hence no unique series of pitch, yaw, roll, and boost commands can be
deduced from
$$
r_1,r_2,r_3,
\varphi_1,\varphi_2,\varphi_3,
d,
g
$$
as the problem is written.


::: pf-proof

The target coordinates are completely determined by
$$
d
$$
up to a permutation and overall orientation, as steps [](#s1-2){.pf-ref} through [](#s1-3){.pf-ref} show.
But steps [](#s1-4){.pf-ref} through [](#s1-8){.pf-ref} prove that the transformation from the initial displayed
points to the displayed points after a command sequence is absent from the
mathematical data.

Adding a particular projection and boost/aberration law would define a new,
well-posed problem, but different such additions give different command
equations.
Therefore the original source does not determine the requested sequence.

:::

:::

::: pf-qed

Step [](#s1-9){.pf-ref} is the complete resolution of the problem as retained.

:::

:::

:::
