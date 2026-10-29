---
schema: qual/card@1
id: P-TOPS05A
kind: problem
title: Free involutions of $S^{2n}$ and spaces covered by $S^{2n}$
classification:
  areas:
  - topology
  topics:
  - Covering Spaces
  - Group Actions
  - Spheres
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: {.problem}
(a) Let $G$ be a group of homeomorphisms of $S^{2n}$ such that for all $g \in G$, $gx = x$ if and only if $g = 1$.
Prove if $G$ has $2$ elements, then one of them is the antipodal map.

(b) If $S^{2n} \to X$ is a covering space, prove $X$ is homeomorphic to $S^{2n}$ or $\RP^{2n}$.
:::

::: {.solution}

Let $n \geq 1$, and let $a(x) = -x$ be the antipodal map of $S^{2n}$.
As stated, (a) and (b) are false; the remark below gives counterexamples.
The proof establishes what is true: in (a) the nonidentity element is homotopic to $a$, and in (b) $X$ is $S^{2n}$ or the quotient of $S^{2n}$ by a free involution, with $\pi_1(X) \cong \ZZ/2$.

::: pf

::: {.pf-step #deg}

Every nonidentity $g \in G$ has $\deg g = -1$.

::: pf-proof

::: pf-step

$\Lambda(g) = 1 + \deg g$.

::: pf-proof

The rational homology of $S^{2n}$ is $\QQ$ in degrees $0$ and $2n$ and zero otherwise.
The homeomorphism $g$ acts on $H_0$ by $1$ and on $H_{2n}$ by $\deg g$, and $(-1)^{2n} = 1$.

:::

:::

::: pf-step

$\deg g = -1$.

::: pf-proof

Since $g \neq 1$, $g$ has no fixed point, so $\Lambda(g) = 0$ by the Lefschetz fixed point theorem [@Hat02, Thm. 2C.3].

:::

:::

:::

:::

::: {.pf-step #a}

(a) If $G = \theset{1, \tau}$, then $\tau$ is homotopic to $a$.

::: pf-proof

$\deg a = (-1)^{2n+1} = -1 = \deg \tau$ by step [](#deg){.pf-ref}.
Two self-maps of $S^{2n}$ of the same degree are homotopic by the Hopf degree theorem [@Hat02, Cor. 4.25].

:::

:::

::: {.pf-step #order}

If $G$ acts freely on $S^{2n}$, then $\abs{G} \leq 2$.

::: pf-proof

Degree is a homomorphism $G \to \theset{\pm 1}$, and by step [](#deg){.pf-ref} its kernel is trivial.

:::

:::

::: pf-step

(b) $X$ is homeomorphic to $S^{2n}$, or $X = S^{2n}/\tau$ for a free involution $\tau$ and $\pi_1(X) \cong \ZZ/2$.

::: pf-proof

Since $S^{2n}$ is simply connected, $p\colon S^{2n} \to X$ is a universal cover, so the deck group $G \cong \pi_1(X)$ acts freely on $S^{2n}$ and $X \cong S^{2n}/G$.
By step [](#order){.pf-ref}, $\abs{G} \leq 2$.
If $G = 1$, then $p$ is a homeomorphism.
Otherwise $G = \theset{1, \tau}$ and $\pi_1(X) \cong \ZZ/2$.

:::

:::

:::

:::

::: {.remark title="Correction to the source"}
(a) fails as stated: let $h$ be a homeomorphism of $S^{2n}$ that is the identity near a point $-p$ and fixes $p$ but moves points near $p$.
Then $\tau = h a h^{-1}$ is a free involution, and for $y$ near $p$ with $x = h^{-1}(y) \neq y$, $\tau(y) = -x \neq -y = a(y)$, so neither element of $\theset{1, \tau}$ is $a$.
The true statement is that the nonidentity element is homotopic to $a$.

(b) holds when $\tau$ is conjugate to $a$, and for $n = 1$ by the classification of surfaces, since $X$ is then a closed nonorientable surface with $\chi(X) = 1$.
In general $S^{2n}/\tau$ need not be homeomorphic to $\RP^{2n}$; the conclusion that holds is that $X$ is $S^{2n}$ or has $\pi_1(X) \cong \ZZ/2$ with universal cover $S^{2n}$.
:::
