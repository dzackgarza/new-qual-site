---
schema: qual/card@1
id: E-HAT-1.3-24
kind: problem
title: Covering spaces from subgroups of deck transformation groups
classification:
  areas:
  - topology
  topics:
  - Covering Spaces
  - Fundamental Group
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-30
- event: source-corrected
  by: claude-opus-5.5
  date: 2026-10-31
  note: Parts (b) and (c) are 'iff' in the book; the stored statement had 'if'.
- event: solution-reviewed
  by: claude-opus-5.5
  date: 2026-10-31
  note: The old solution assumed X simply connected; rewritten with unique lifting and freeness of the action, proving both directions of (b) and (c).
---

::: {.problem}
Given a covering space action of a group $G$ on a path-connected, locally path-connected space $X$, then each subgroup $H \subset G$ determines a composition of covering spaces $X \to X/H \to X/G$.
Show:

(a) Every path-connected covering space between $X$ and $X/G$ is isomorphic to $X/H$ for some subgroup $H \subset G$.

(b) Two such covering spaces $X/H_1$ and $X/H_2$ of $X/G$ are isomorphic iff $H_1$ and $H_2$ are conjugate subgroups of $G$.

(c) The covering space $X/H \to X/G$ is normal iff $H$ is a normal subgroup of $G$, in which case the group of deck transformations of this cover is $G/H$.
:::

::: {.solution}
Write $q:X\to X/G$, $p_H:X\to X/H$ and $q_H:X/H\to X/G$ for the quotient maps, so $q=q_H\circ p_H$.
The space $X$ need not be simply connected; the proof uses only that $X$ is connected, so that two lifts of one map that agree at a point are equal, and that $G$ acts freely.

::: pf

::: {.pf-step #s1}
Let $f:X\to Y$ and $p:Y\to X/G$ be covering spaces with $p\circ f=q$ and $Y$ path-connected.
Put $H=\theset{g\in G\st f\circ g=f}$.
Then $H$ is a subgroup of $G$, and $f(x)=f(x')$ if and only if $x'=hx$ for some $h\in H$.

::: pf-proof
$H$ is clearly a subgroup.
If $x'=hx$ with $h\in H$, then $f(x')=f(hx)=f(x)$.
Conversely, let $f(x)=f(x')$.
Then $q(x)=q(x')$, so $x'=gx$ for some $g\in G$.
The maps $f$ and $f\circ g$ are both lifts of $q$ through $p$, since $p\circ f\circ g=q\circ g=q$, and they agree at $x$ because $f(gx)=f(x')=f(x)$.
Since $X$ is connected, the unique lifting property gives $f\circ g=f$, so $g\in H$.
:::

:::

::: {.pf-step #s2}
In the situation of step [](#s1){.pf-ref}, $f$ induces a homeomorphism $X/H\to Y$ over $X/G$.
This proves (a).

::: pf-proof
The image of a covering map is open, because $f$ is a local homeomorphism, and its complement is open, because a point with an evenly covered neighborhood whose preimage is empty has that whole neighborhood outside the image.
Since $Y$ is connected and $X$ is nonempty, $f$ is surjective.
By step [](#s1){.pf-ref}, $f$ factors through a continuous bijection $\bar f:X/H\to Y$ with $\bar f\circ p_H=f$, and $p\circ\bar f=q_H$.
A covering map is open, so $f$ is a quotient map, and $\bar f$ is open: for $W\subseteq X/H$ open, $\bar f(W)=f(p_H^{-1}(W))$.
Hence $\bar f$ is a homeomorphism commuting with the projections to $X/G$.
:::

:::

::: {.pf-step #s3}
If $\varphi:X/H_1\to X/H_2$ is a map over $X/G$, then there is $g\in G$ with $\varphi\circ p_{H_1}=p_{H_2}\circ g$ and $gH_1g^{-1}\subseteq H_2$.
Conversely, every $g\in G$ with $gH_1g^{-1}\subseteq H_2$ defines a map $\varphi_g([x])=[gx]$ over $X/G$.

::: pf-proof
Fix $x_0\in X$ and write $\varphi(p_{H_1}(x_0))=p_{H_2}(x_1)$.
Since $\varphi$ is over $X/G$, $q(x_1)=q(x_0)$, so $x_1=gx_0$ for some $g\in G$.
The maps $\varphi\circ p_{H_1}$ and $p_{H_2}\circ g$ are lifts of $q$ through $q_{H_2}$ that agree at $x_0$, so they are equal because $X$ is connected.
Let $h\in H_1$ and $x\in X$.
Then $p_{H_2}(ghx)=\varphi(p_{H_1}(hx))=\varphi(p_{H_1}(x))=p_{H_2}(gx)$, so $ghx=h'gx$ for some $h'\in H_2$.
Thus $h'^{-1}ghg^{-1}$ fixes the point $gx$, and since the action is free, $ghg^{-1}=h'\in H_2$.

For the converse, $\varphi_g$ is well defined because $ghx=(ghg^{-1})gx$ with $ghg^{-1}\in H_2$.
It is continuous because $\varphi_g\circ p_{H_1}=p_{H_2}\circ g$ is continuous and $p_{H_1}$ is a quotient map, and $q_{H_2}\circ\varphi_g=q_{H_1}$ because $q(gx)=q(x)$.
:::

:::

::: {.pf-step #s4}
$X/H_1$ and $X/H_2$ are isomorphic over $X/G$ if and only if $H_1$ and $H_2$ are conjugate in $G$.
This proves (b).

::: pf-proof
If $H_2=gH_1g^{-1}$, then by step [](#s3){.pf-ref} the maps $\varphi_g$ and $\varphi_{g^{-1}}$ are defined and are inverse to each other.
Conversely, let $\varphi$ be an isomorphism over $X/G$ and choose $g$ for $\varphi$ as in step [](#s3){.pf-ref}, so $gH_1g^{-1}\subseteq H_2$.
From $\varphi\circ p_{H_1}=p_{H_2}\circ g$ we get $\varphi^{-1}\circ p_{H_2}=p_{H_1}\circ g^{-1}$, and the argument of step [](#s3){.pf-ref} applied to $\varphi^{-1}$ with the element $g^{-1}$ gives $g^{-1}H_2g\subseteq H_1$.
Hence $gH_1g^{-1}=H_2$.
:::

:::

::: {.pf-step #s5}
The deck group of $q_H:X/H\to X/G$ is isomorphic to $N_G(H)/H$, through $g\mapsto\varphi_g$.

::: pf-proof
By steps [](#s3){.pf-ref} and [](#s4){.pf-ref} with $H_1=H_2=H$, every deck transformation is $\varphi_g$ for some $g$ with $gHg^{-1}=H$, that is $g\in N_G(H)$, and every such $g$ gives one.
Clearly $\varphi_{gg'}=\varphi_g\circ\varphi_{g'}$.
If $\varphi_g$ is the identity, then $gx=hx$ for some $x$ and some $h\in H$, so $g=h\in H$ by freeness; conversely $\varphi_h=\mathrm{id}$ for $h\in H$.
:::

:::

::: {.pf-step #s6}
$q_H$ is normal if and only if $H$ is normal in $G$, and then its deck group is $G/H$.
This proves (c).

::: pf-proof
The fiber of $q_H$ over $q(x_0)$ is $\theset{[gx_0]\st g\in G}$, and by step [](#s5){.pf-ref} the deck orbit of $[x_0]$ is $\theset{[nx_0]\st n\in N_G(H)}$.
Now $[gx_0]=[nx_0]$ means $gx_0=hnx_0$ for some $h\in H$, that is $g=hn\in HN_G(H)=N_G(H)$ by freeness.
So the deck group is transitive on this fiber if and only if $N_G(H)=G$, that is $H\trianglelefteq G$.
Since $x_0$ is arbitrary, this holds for every fiber, and then the deck group is $G/H$ by step [](#s5){.pf-ref}.
:::

:::

:::
:::
