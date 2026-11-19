---
schema: qual/card@1
id: P-AMD-6OJQMSOZ
kind: problem
title: Borsuk–Ulam theorem for maps $S^2\to\RR^2$
classification:
  areas:
  - topology
  topics:
  - Fixed Points
  - Degree
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-25
- event: solution-written
  by: claude
  date: 2026-11-19
  note: >-
    Every step now carries a pf-proof: the four containers state why their subclaims suffice, and the 17
    leaf steps that asserted a claim with no justification each carry a sentence deriving it. The
    trailing pf-qed, whose only content was a reference back to step s4, was removed; the last step of s4
    is now the QED step, which is what STYLE-08 asks for. The mathematics is unchanged and was re-read:
    the construction of F and of the normalized odd map g, the lift of the odd h on the equator, the
    connectedness argument making the half-period shift a constant half-integer k + 1/2, the degree
    2k + 1, the extension of h over the upper hemisphere, and the vanishing of the degree of a boundary
    that extends over the disk. No published solution is cited on this card, so the argument is the
    card's own. Nothing in the statement was changed.
---

::: {.problem}
Prove that for any $f: S^2 \to \RR^2$, there exists $x\in S^2$ such that $f(x) = f(-x)$.
:::

::: {.solution}
::: pf

::: pf-step
Reduce to showing there is no odd continuous map $g \colon S^2 \to S^1$.

::: pf-proof
The subclaims construct, from a map with no antipodal coincidence, a continuous odd map $g:S^2\to S^1$; so the absence of such a $g$ proves the theorem.

::: pf-step
Suppose for contradiction that there exists a continuous map $f \colon S^2 \to \RR^2$ such that $f(x) \neq f(-x)$ for all $x \in S^2$.

::: pf-proof
This is the negation of the statement to be proved, so a contradiction derived from it proves that statement.
:::

:::

::: pf-step
Define $F \colon S^2 \to \RR^2 \setminus \{0\}$ by $F(x) = f(x) - f(-x)$.

::: pf-proof
The values of $F$ lie in $\RR^2\setminus\{0\}$ by the supposition, and $F$ is continuous as a difference of continuous maps.
:::

:::

::: pf-step
$F$ is continuous and antipodal-preserving (odd): $F(-x) = f(-x) - f(x) = -F(x)$.

::: pf-proof
The displayed identity is the computation of $F(-x)$ from its definition, and continuity was noted in the preceding subclaim.
:::

:::

::: pf-step
Define $g \colon S^2 \to S^1$ by $g(x) = \frac{F(x)}{\norm{F(x)}}$.

::: pf-proof
The denominator never vanishes, so the formula defines a map into the unit circle; it is continuous as a composition of continuous maps.
:::

:::

::: pf-step
The map $g$ is continuous and odd: $g(-x) = \frac{-F(x)}{\norm{-F(x)}} = -g(x)$ for all $x \in S^2$.

::: pf-proof
The map $g$ is the composition of the continuous map $F$ with the continuous normalization $y \mapsto y/\norm{y}$, so it is continuous; the oddness follows from $F(-x) = -F(x)$.
:::

:::

:::

:::

::: {.pf-step #s2}
Restrict $g$ to the equatorial circle $S^1 \subset S^2$.

::: pf-proof
The subclaims produce the odd map $h$ on the equator and compute that its degree is odd.

::: pf-step
Let $h = g\restrict_{S^1} \colon S^1 \to S^1$.

::: pf-proof
This is a definition; $h$ is continuous as the restriction of a continuous map.
:::

:::

::: pf-step
Since $g$ is odd on $S^2$, $h$ is an odd map on $S^1$: $h(-x) = -h(x)$ for all $x \in S^1$.

::: pf-proof
The equator is carried to itself by $x\mapsto-x$, and on it $h$ agrees with the odd map $g$.
:::

:::

::: pf-step
Every continuous odd map $h \colon S^1 \to S^1$ has odd degree $\deg(h) \equiv 1 \pmod 2$.

::: pf-proof
The subclaims lift $h$ to the line, where oddness forces a half-integer shift over half a period, so that the total shift over a period is odd.

::: pf-step
Parameterize $S^1$ by $[0, 1] / (0 \sim 1)$ via $t \mapsto e^{2\pi i t}$.
Antipodal points correspond to $t$ and $t + 1/2$.

::: pf-proof
The map $t\mapsto e^{2\pi it}$ is a continuous bijection of the interval with endpoints identified onto $S^1$, and $e^{2\pi i(t+1/2)}=-e^{2\pi it}$.
:::

:::

::: pf-step
Lift $h$ to a continuous map $\widetilde{h} \colon \RR \to \RR$ via the covering map $p(t) = e^{2\pi i t}$.

::: pf-proof
The map $t\mapsto e^{2\pi it}$ is a covering map of $\RR$ over $S^1$ and $\RR$ is simply connected, so the lifting criterion applies to the continuous map $h\circ p$ and supplies $\widetilde h$ with $p\circ\widetilde h=h\circ p$.
:::

:::

::: pf-step
The condition $h(t + 1/2) = -h(t) = e^{i\pi} h(t)$ means $p(\widetilde{h}(t + 1/2)) = p(\widetilde{h}(t) + 1/2)$.

::: pf-proof
$-1=e^{i\pi}=p(1/2)$, so $p(\widetilde h(t)+1/2)=p(\widetilde h(t))p(1/2)=-p(\widetilde h(t))=-h\circ p(t)$, which is $p(\widetilde h(t+1/2))$ by the defining property of the lift.
:::

:::

::: pf-step
Thus $\widetilde{h}(t + 1/2) - \widetilde{h}(t) = k + 1/2$ for some fixed integer $k \in \ZZ$ (by connectedness of $\RR$).

::: pf-proof
The difference $d(t)=\widetilde h(t+1/2)-\widetilde h(t)-1/2$ is continuous and takes values in $\ZZ$ by the preceding subclaim; a continuous map from the connected space $\RR$ into the discrete space $\ZZ$ is constant, and its value is the integer $k$.
:::

:::

::: pf-step
The degree of $h$ is given by the total shift over the period 1: $$\deg(h) = \widetilde{h}(1) - \widetilde{h}(0) = (\widetilde{h}(1) - \widetilde{h}(1/2)) + (\widetilde{h}(1/2) - \widetilde{h}(0)) = 2(k + 1/2) = 2k + 1.$$

::: pf-proof
The degree of a map $S^1\to S^1$ is the shift $\widetilde h(1)-\widetilde h(0)$ of any lift, legitimate because $h(1)=h(0)$ forces that difference to be an integer. The splitting at $1/2$ and the preceding subclaim, read at $t=0$ and at $t=1/2$, give the two terms $k+1/2$.
:::

:::

::: pf-step
Thus $\deg(h) = 2k + 1$ is an odd integer, and in particular $\deg(h) \neq 0$.

::: pf-proof
The lift $\widetilde{h}$ exists by the lifting criterion for the universal cover $\RR \to S^1$; the oddness condition forces the half-period shift to be a half-integer, and the degree is the total shift over one period, which is therefore odd.
:::

:::

:::

:::

:::

:::

::: {.pf-step #s3}
Obtain a contradiction via the upper hemisphere disk.

::: pf-proof
The subclaims exhibit $h$ as the boundary values of a map of the disk, which forces its degree to vanish.

::: pf-step
Let $D_+^2 = \{(x_1, x_2, x_3) \in S^2 \mid x_3 \ge 0\}$ be the closed upper hemisphere.

::: pf-proof
This is a definition; $D_+^2$ is closed in $S^2$ as the preimage of $[0,\infty)$ under the continuous third coordinate.
:::

:::

::: pf-step
$D_+^2$ is homeomorphic to the closed 2-disk $D^2$, and its boundary is $\partial D_+^2 = S^1$ (the equator).

::: pf-proof
Orthogonal projection $(x_1,x_2,x_3)\mapsto(x_1,x_2)$ restricts to a continuous bijection of $D_+^2$ onto the closed unit disk, with continuous inverse $(u_1,u_2)\mapsto(u_1,u_2,\sqrt{1-u_1^2-u_2^2})$; it carries the equator, where $x_3=0$, onto the boundary circle.
:::

:::

::: pf-step
The restriction $g\restrict_{D_+^2} \colon D_+^2 \to S^1$ is a continuous extension of $h = g\restrict_{S^1}$ to the entire disk $D_+^2$.

::: pf-proof
It is continuous as the restriction of a continuous map, and on the equator it agrees with $h$ by the definition of $h$.
:::

:::

::: pf-step
If a continuous map $h \colon S^1 \to S^1$ extends to a continuous map $D^2 \to S^1$, then $h$ is nullhomotopic, so $\deg(h) = 0$.

::: pf-proof
The disk $D^2$ is contractible, so the inclusion $\iota \colon S^1 \hookrightarrow D^2$ induces the zero map on $\pi_1(S^1)$; hence $h_* = (g\restrict_{D^2} \circ \iota)_* = 0$, so $\deg(h) = 0$.
:::

:::

:::

:::

::: {.pf-step #s4}
Derive the final contradiction.

::: pf-proof
The two degree computations contradict each other, which rules out the map $g$ and hence the map $f$.

::: pf-step
By step [](#s2){.pf-ref}, $\deg(h)$ is odd (so $\deg(h) \neq 0$).

::: pf-proof
Step [](#s2){.pf-ref} computes the degree of the odd map $h$ on the equator as $2k+1$.
:::

:::

::: pf-step
By step [](#s3){.pf-ref}, $\deg(h) = 0$.

::: pf-proof
Step [](#s3){.pf-ref} exhibits $h$ as the boundary of a continuous map of the disk, which forces the degree to vanish.
:::

:::

::: pf-step
This contradiction shows no such odd map $g \colon S^2 \to S^1$ exists.

::: pf-proof
An integer cannot be both odd and equal to $0$, so the supposition that produced $g$ is false.
:::

:::

::: pf-step
Hence for any continuous $f \colon S^2 \to \RR^2$, there exists $x \in S^2$ such that $f(x) = f(-x)$.

::: pf-proof
Step [](#s2){.pf-ref} shows $\deg(h)$ is odd, while step [](#s3){.pf-ref} shows $\deg(h) = 0$; this contradiction rules out the existence of an odd map $g \colon S^2 \to S^1$, and hence of a map $f$ with $f(x) \neq f(-x)$ everywhere.
:::

:::

:::

:::

:::
:::
