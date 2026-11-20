---
schema: qual/card@1
id: P-AMD-DX7L7EFB
kind: problem
title: $\pi_1$ of the Möbius strip and the class of the boundary
classification:
  areas:
  - topology
  topics:
  - Fundamental Group
  - Surfaces
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-25
- event: source-checked
  by: claude
  date: 2026-11-20
  note: >-
    The statement matches Problem 4 of the second sheet, printed page 249 of
    `assets/attachments/UCSD_290_F14_sheet2.pdf`: identify the fundamental group of the Möbius strip
    $M$ based at the point $[(1, \tfrac{1}{2})]$, and say what class the boundary curve represents.
    The sheet uses the model of the Möbius strip that its first sheet defines, $I \times I$ with
    $(x, 0) \sim (1-x, 1)$; the card computes in the model obtained by the quarter turn, and the
    solution now says so and names the homeomorphism. The set is problem sheets only, so no retained
    published solution covers this card and the argument on it is the card's own.
- event: solution-written
  by: claude
  date: 2026-11-20
  note: >-
    Fifteen steps asserted their claim with no justification; each now carries a pf-proof. The new
    sentences verify that the core curve is a well-defined continuous loop, that the core circle is
    homeomorphic to $S^1$ (the curve is injective on $[0,1)$), that the vertical gluing makes $H$ well
    defined, that $H$ fixes $C$ pointwise and so is a strong deformation retraction, and that the
    induced maps $r_* i_*$ and $i_* r_*$ are identities, which is what makes $\pi_1(M, x_0) \cong \ZZ$.
    On the boundary side they identify $\partial M$ with the image of the horizontal edges by looking at
    a neighbourhood of each kind of point, verify the two corner identifications, check that $\beta$ is
    a loop passing through both corners, and compute $H(\beta(\cdot), 1)$ branch by branch. One
    correction of substance: the last step now records that the sign of $2$ is fixed by the orientation
    $\beta$ gives the boundary, so the invariant statement is that the boundary is twice a generator.
    The statement is unchanged. Not checked: the repository retains no solution to these sheets, so the
    argument was verified here rather than against a published one.
---

::: {.problem}
Identify $\pi_1(M, [(1, \frac{1}{2})])$, and identify the class of $\partial M$.
:::

::: {.solution}
Let $M = ([0, 1] \times [0, 1]) / ((0, y) \sim (1, 1-y))$ be the standard Möbius strip with basepoint $x_0 = [(1, 1/2)] = [(0, 1/2)]$.
The first sheet of this set defines the Möbius strip as $I \times I$ with $(x, 0) \sim (1-x, 1)$; the quarter turn $(x, y) \mapsto (y, x)$ of the square carries that relation to $(0, y) \sim (1, 1-y)$, so the two models are homeomorphic and the computation below is carried out in the second.

::: pf

::: {.pf-step #s1}
Compute $\pi_1(M, x_0)$.

::: pf-proof

::: {.pf-step #core-curve}
Define the center circle / core curve $\gamma_0 \colon [0, 1] \to M$ by $\gamma_0(t) = [(t, 1/2)]$.

::: pf-proof
The formula assigns to each $t$ the class of a point of the square, and $\gamma_0$ is continuous as the composite of the continuous map $t \mapsto (t, 1/2)$ with the quotient map $[0,1]^2 \to M$.
:::

:::

::: pf-step
$\gamma_0(0) = [(0, 1/2)] = [(1, 1/2)] = \gamma_0(1) = x_0$, so $\gamma_0$ is a continuous loop based at $x_0$.

::: pf-proof
The two endpoints are $\gamma_0(0) = [(0,1/2)]$ and $\gamma_0(1) = [(1,1/2)]$, and these are one point of $M$ because the gluing relation identifies $(0,1/2)$ with $(1, 1 - 1/2) = (1, 1/2)$. Since $\gamma_0$ is continuous by step [](#core-curve){.pf-ref}, it is a loop based at that point $x_0$.
:::

:::

::: {.pf-step #core-circle}
Let $C = \gamma_0([0, 1]) \subset M$ be the core circle, homeomorphic to $S^1$.

::: pf-proof
The map $\gamma_0$ is injective on $[0,1)$: if $[(t,1/2)] = [(t',1/2)]$ with $0 \le t, t' < 1$ then either $t = t'$, or $t = 0$ and $t' = 1$ because the only identification reverses the second coordinate and $1/2 = 1 - 1/2$. So $\gamma_0$ induces a continuous bijection from $[0,1]$ with its endpoints identified, which is compact, onto $C$, which is Hausdorff, and such a bijection is a homeomorphism.
:::

:::

::: {.pf-step #retraction-map}
Define $H \colon M \times [0, 1] \to M$ by $H([(x, y)], s) = [(x, (1-s)y + s(1/2))]$.

::: pf-proof
For fixed $s$ the pair $(x, (1-s)y + s/2)$ again lies in the square, and it is a continuous function of $((x,y), s)$; so the formula defines a continuous map $[0,1]^2 \times [0,1] \to M$ after composing with the quotient map on the square, provided it agrees on identified pairs, which step [](#retraction-well-defined){.pf-ref} verifies. What it defines on the quotient $M \times [0,1]$ is then $H$.
:::

:::

::: {.pf-step #retraction-well-defined}
$H$ is well-defined: $H([(1, 1-y)], s) = [(1, (1-s)(1-y) + s/2)] = [(1, 1 - ((1-s)y + s/2))] = H([(0, y)], s)$.

::: pf-proof
On an identified pair the two values are $[(1, (1-s)(1-y) + s/2)]$ and $[(0, (1-s)y + s/2)]$, and $(1-s)(1-y) + s/2 = 1 - y + sy + s/2 = 1 - ((1-s)y + s/2)$; so the first value is the glued image of the second under the relation $(0,a) \sim (1, 1-a)$, and $H$ is well defined.
:::

:::

::: pf-step
$H$ is a strong deformation retraction of $M$ onto the core circle $C$.

::: pf-proof
At $s = 0$ the second coordinate is $y$, so $H(\cdot, 0)$ is the identity. At $s = 1$ it is $1/2$, so $H$ lands in $C$; and on $C$ the coordinate $(1-s)/2 + s/2 = 1/2$ is fixed throughout, so $H$ fixes $C$ pointwise. With continuity from steps [](#retraction-map){.pf-ref} and [](#retraction-well-defined){.pf-ref}, this is a strong deformation retraction of $M$ onto $C$.
:::

:::

::: pf-step
Thus $\pi_1(M, x_0) \cong \pi_1(C, x_0) \cong \ZZ$, generated by the homotopy class $[\gamma_0]$.

::: pf-proof
Let $r = H(\cdot, 1) \colon M \to C$ and let $i \colon C \to M$ be the inclusion. Then $r \circ i = \id_C$, and $i \circ r = H(\cdot, 1) \simeq \id_M$ relative to $C$, hence relative to $x_0$. So $r_* \circ i_* = \id$ and $i_* \circ r_* = \id$ on the fundamental groups, $r_*$ is an isomorphism, and $\pi_1(M, x_0) \cong \pi_1(C, x_0) \cong \pi_1(S^1) \cong \ZZ$ by step [](#core-circle){.pf-ref}. The generator is the class of the loop that $\gamma_0$ names, that is $[\gamma_0]$.
:::

:::

::: pf-qed
The map $H$ is a strong deformation retraction of $M$ onto the core circle $C \cong S^1$, and a deformation retraction induces an isomorphism on fundamental groups, so $\pi_1(M, x_0) \cong \pi_1(S^1) \cong \ZZ$.
:::

:::

:::

::: {.pf-step #s2}
Identify the homotopy class of the boundary $\partial M$.

::: pf-proof

::: {.pf-step #boundary-edges}
The boundary of $M$ comes from the horizontal edges $y = 0$ and $y = 1$ in $[0, 1] \times [0, 1]$.

::: pf-proof
Every point of $M$ with a representative $(x,y)$ where $0 < x < 1$ is interior to the square, and a representative with $x \in \{0,1\}$ and $0 < y < 1$ has two half-disc neighbourhoods, one from each vertical edge, glued along their diameters with the orientation reversed by $y \mapsto 1-y$, which makes a disc; so those are interior points too. A representative with $y \in \{0,1\}$ and $0 < x < 1$ has only one half-disc beside it, so its class is a boundary point, and the two corner classes have two quarter-discs that glue to a half-disc, so they are boundary points as well. Hence $\partial M$ is the image of the two horizontal edges.
:::

:::

::: {.pf-step #corner-gluing}
Under the gluing $(0, y) \sim (1, 1-y)$, $(0, 0) \sim (1, 1)$ and $(0, 1) \sim (1, 0)$.

::: pf-proof
The relation $(0,y) \sim (1, 1-y)$ at $y = 0$ gives $(0,0) \sim (1,1)$, and at $y = 1$ it gives $(0,1) \sim (1,0)$; those are the two corner identifications.
:::

:::

::: pf-step
A continuous parameterization of the single boundary loop $\partial M$ starting and ending at $p_0 = [(0, 0)] = [(1, 1)]$ is given by: $$\beta(t) = \begin{cases} [(2t, 0)] & \text{for } t \in [0, 1/2], \\ [(2t-1, 1)] & \text{for } t \in [1/2, 1]. \end{cases}$$

::: pf-proof
Each branch is continuous, and the first ends at $[(1,0)]$ while the second starts at $[(0,1)]$, which is the same point of $M$ by step [](#corner-gluing){.pf-ref}; the second branch ends at $[(1,1)]$, which is $[(0,0)]$ by the same step, so $\beta$ is a loop at $p_0$. By step [](#boundary-edges){.pf-ref} its image is the whole of $\partial M$, and the two branches together run along the boundary circle once.
:::

:::

::: pf-step
To compare with basepoint $x_0 = [(0, 1/2)]$, connect $x_0$ to $p_0$ by the straight segment $\eta(s) = [(0, (1-s)/2)]$ for $s \in [0, 1]$.

::: pf-proof
$\eta(0) = [(0, 1/2)] = x_0$ and $\eta(1) = [(0,0)] = p_0$, and $\eta$ is continuous as the composite of the continuous map $s \mapsto (0, (1-s)/2)$ with the quotient map.
:::

:::

::: pf-step
The based boundary loop is $\alpha = \eta \cdot \beta \cdot \eta^{-1}$.

::: pf-proof
The concatenation $\eta \cdot \beta \cdot \eta^{-1}$ is defined because $\eta$ runs from $x_0$ to $p_0$, $\beta$ is a loop at $p_0$, and $\eta^{-1}$ runs from $p_0$ back to $x_0$; so $\alpha$ is a loop at $x_0$, and it represents the class of the boundary curve in $\pi_1(M, x_0)$ once $\beta$ is read as a parameterization of that curve.
:::

:::

::: {.pf-step #boundary-retracted}
Applying the deformation retraction $H$ from step [](#s1){.pf-ref} to $\beta$:

- On $t \in [0, 1/2]$, $H([(2t, 0)], 1) = [(2t, 1/2)] = \gamma_0(2t)$, which traverses the core loop once.

- On $t \in [1/2, 1]$, $H([(2t-1, 1)], 1) = [(2t-1, 1/2)] = \gamma_0(2t-1)$, which traverses the core loop a second time in the same direction.

::: pf-proof
By construction $H([(x,y)], 1) = [(x, 1/2)]$, so $H(\beta(t), 1) = [(2t, 1/2)] = \gamma_0(2t)$ for $t \le 1/2$ and $H(\beta(t),1) = [(2t-1, 1/2)] = \gamma_0(2t-1)$ for $t \ge 1/2$. On the first half $2t$ runs through $[0,1]$ and on the second half $2t-1$ does, both in the increasing direction, so each branch traces the core circle once in the direction of $\gamma_0$.
:::

:::

::: {.pf-step #boundary-image}
Thus $H(\alpha, 1) \simeq \gamma_0 \cdot \gamma_0 = \gamma_0^2$.

::: pf-proof
Applying $H(\cdot, 1)$ to the concatenation applies it to each piece: the two end pieces become $H(\eta(s), 1) = [(0, 1/2)] = x_0$, the constant loop, and the middle piece becomes $\gamma_0 \cdot \gamma_0$ by step [](#boundary-retracted){.pf-ref}. Concatenating a loop with a constant loop gives a homotopic loop, so $H(\alpha, 1) \simeq \gamma_0 \cdot \gamma_0 = \gamma_0^2$.
:::

:::

::: pf-step
Therefore, the class of the boundary loop is $[\partial M] = [\gamma_0]^2 = 2 \in \ZZ \cong \pi_1(M, x_0)$ (i.e. twice the generator).

::: pf-proof
The loop $\alpha$ is homotopic to $H(\alpha, 1)$ through $H(\alpha, s)$, and $H(\alpha, 1) \simeq \gamma_0^2$ by step [](#boundary-image){.pf-ref}, so $[\partial M] = [\gamma_0]^2$ in $\pi_1(M, x_0)$, which under the isomorphism of step [](#s1){.pf-ref} is $a^2 = 2$ for $a = [\gamma_0]$. The class of the boundary curve is therefore twice a generator of $\ZZ$; the sign of the $2$ is fixed by the orientation that $\beta$ gives the boundary, and reversing that orientation replaces $2$ by $-2$.
:::

:::

::: pf-qed
Applying the deformation retraction $H$ to the based boundary loop $\alpha$ sends it to $\gamma_0 \cdot \gamma_0 = \gamma_0^2$, and $H$ is a homotopy equivalence, so $[\partial M] = [\gamma_0]^2 = 2$ in $\pi_1(M, x_0) \cong \ZZ$.
:::

:::

:::

::: pf-step
Conclusion.

::: pf-proof

::: pf-step
$\pi_1(M, x_0) \cong \ZZ = \langle a \rangle$, and $[\partial M] = a^2 = 2 \in \ZZ$.

::: pf-proof
Step [](#s1){.pf-ref} identifies $\pi_1(M, x_0)$ with $\ZZ$ generated by $a = [\gamma_0]$, and step [](#s2){.pf-ref} shows $[\partial M] = a^2$.
:::

:::

:::

:::

:::
:::
