---
schema: qual/card@1
id: P-CAF08B
kind: problem
title: "True or False: meromorphic extensions, Schwarz reflection, simple connectivity, minimum modulus, and analytic continuation"
classification:
  areas:
  - complex-analysis
  topics:
  - Complex Analysis
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Repaired and restructured. All five verdicts are correct (T, T, F, T, F) and are kept; what
    was wrong was the form: each of the five 'steps' carried both the verdict and the entire
    argument inside its claim, with no pf-proof anywhere, and there was no closing step. Each
    part now has its argument as a proof: Riemann's removable singularity applied to (z-1)f(z)
    in (a); the reflected function -conj(f(-conj z)) with the check that it is continuous across
    the segment I and holomorphic off it, hence holomorphic by Morera, in (b); the
    counterexample e^z with the integral of 1/z around the circle exhibiting non-simple-
    connectivity in (c); the minimum-modulus argument through 1/f in (d); and in (e) the
    logarithm on B(1/2;1/4) with the derivative argument 0 = ∮F' = 2 pi i showing no single-
    valued extension exists. Not claimed: a retained solution set; the collection's provenance
    is the examination paper only.
---

::: {.problem}
For each part, determine if it is always true or sometimes false.
If true give a brief proof.
If false give a counterexample.

(a) If $f \in H(B(1; 1) \setminus \{1\})$ with $\abs{f(z)} \leq \frac{1}{\abs{z - 1}}$ for all $z \in B(1; 1) \setminus \{1\}$, then $f$ extends to a meromorphic (or possibly analytic) function on $B(1; 1)$.

(b) Suppose that $f \in H(\{z \in B(0; 1) : \operatorname{Re} z > 0\})$ and extends continuously to the line segment $I = \{it : -1 < t < 1\}$.
If $f(I) \subset i\RR$, then $f$ extends to an analytic function in $B(0; 1)$.

(c) If $G \subset \CC$ is open, connected, and simply connected, and $f \in H(G)$ with $f'(z) \neq 0$ for all $z \in G$, then $f(G)$ is also open, connected, and simply connected.

(d) Let $G \subset \CC$ be connected and open and $f \in H(G)$ nonconstant.
If $f(z) \neq 0$ for all $z \in G$, then $\abs{f}$ does not reach a minimum at any point in $G$.

(e) Let $f$ be an analytic function element defined in $B(1/2; 1/4)$.
Suppose that $f$ continues analytically along any path $\gamma$ from $\gamma(0) \in B(1/2; 1/4)$ to $\gamma(1) \in B(0; 1) \setminus \{0\}$.
Then there is a function $F \in H(B(0; 1) \setminus \{0\})$ such that $F\restrict_{B(1/2; 1/4)} = f$.
:::

::: {.solution}
Throughout $H(\Omega)$ is the algebra of holomorphic functions on an open set $\Omega$, $B(a;r)$ is the open disc of radius $r$ about $a$, and the statements are the five of the examination question. The collection's `provenance` is the Fall 2008 examination paper, and no solutions sheet accompanies it, so the arguments below are the card's own.

::: pf

::: {.pf-step #a}
(a) True.

::: pf-proof
Put $g(z) \coloneqq (z-1)f(z)$ on $B(1;1)\setminus\theset{1}$; the hypothesis gives $\abs{g(z)} = \abs{z-1}\abs{f(z)} \le 1$ there, so $g$ is bounded near $1$ and $1$ is a removable singularity of $g$ by Riemann's theorem. Hence $g$ extends holomorphically to $B(1;1)$, and $f = \widetilde{g}/(z-1)$ is meromorphic on $B(1;1)$, analytic where $\widetilde{g}$ does not vanish, with at worst a simple pole at $1$.

:::

:::

::: {.pf-step #b}
(b) True.

::: pf-proof
Let $\Omega^{+} \coloneqq \theset{z \in B(0;1) \mid \operatorname{Re} z > 0}$ be the given half-disc and $\Omega^{-} \coloneqq \theset{z \in B(0;1) \mid \operatorname{Re} z < 0}$ its reflection. Define $F \coloneqq f$ on $\Omega^{+}$ and $F(z) \coloneqq -\overline{f(-\bar z)}$ on $\Omega^{-}$. The map $z \mapsto -\bar z$ carries $\Omega^{-}$ biholomorphically onto $\Omega^{+}$, so $F$ is holomorphic on $\Omega^{-}$, and the two definitions agree on $I$: for $z = it$ one has $-\bar z = z$, and $f(it) \in i\RR$ gives $-\overline{f(it)} = f(it)$. So $F$ is continuous on $\Omega^{+}\cup I \cup \Omega^{-}$, which is an open disc, and holomorphic off $I$; Morera's theorem applied to triangles crossing $I$ — splitting each along $I$ into a piece in $\Omega^{+}$ and a piece in $\Omega^{-}$ — makes $F$ holomorphic on $B(0;1)$.

:::

:::

::: {.pf-step #c}
(c) False.

::: pf-proof
Take $G = \CC$, which is open, connected and simply connected, and $f(z) \coloneqq e^{z}$, holomorphic with $f'(z) = e^{z} \ne 0$ everywhere. Then $f(G) = \CC^{\times}$, which is connected and open but not simply connected: $z \mapsto 1/z$ is holomorphic on $\CC^{\times}$ with integral $2\pi i$ around the unit circle, so that circle is not null-homotopic; equivalently $\CC^{\times}$ has universal cover $\CC \to \CC^{\times}$, $z \mapsto e^{z}$, which is not a homeomorphism. So the conclusion fails and the implication is false.

:::

:::

::: {.pf-step #d}
(d) True.

::: pf-proof
$f$ does not vanish on the connected open set $G$, so $1/f$ is holomorphic on $G$. If $\abs f$ attained a minimum at $z_{0} \in G$, then on a neighbourhood $U \subseteq G$ of $z_{0}$ one would have $\abs{1/f(z)} \le \abs{1/f(z_{0})}$ for all $z \in U$, so $\abs{1/f}$ would have a local maximum at an interior point; the maximum modulus principle forces $1/f$, hence $f$, to be constant on $G$, contrary to the hypothesis. So no interior point is a minimum of $\abs f$.

:::

:::

::: pf-step
(e) False.

::: pf-proof
Take $f$ to be the principal branch of the logarithm on $B(1/2;1/4)$, a disc that does not contain $0$, so $f$ is an analytic function element there. Along any path $\gamma$ in $B(0;1)\setminus\theset{0}$ starting in $B(1/2;1/4)$ one continues $f$ by integrating $1/\zeta\,d\zeta$ along $\gamma$ and exponentiating from the germ at $\gamma(0)$; this continuation exists along every such path, which is the hypothesis of (e). But no $F \in H(B(0;1)\setminus\theset{0})$ restricts to $f$: such an $F$ would satisfy $F'(z) = 1/z$ and hence $\oint_{\abs{z} = 1/2}F'(z)\,dz = 2\pi i$, while the integral of a derivative along a closed curve is $0$, a contradiction. So the statement is false.

:::

:::

:::
:::
