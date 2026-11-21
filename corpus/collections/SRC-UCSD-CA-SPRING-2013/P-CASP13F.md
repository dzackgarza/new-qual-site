---
schema: qual/card@1
id: P-CASP13F
kind: problem
title: "Identity theorem from boundary vanishing on an arc of a simply connected domain"
classification:
  areas:
  - complex-analysis
  topics:
  - Complex Analysis
relations: []
review: draft
audit:
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Repaired and restructured. The card's sketch was right in outline (reflect the vanishing
    across the circle |z+i| = 2, apply Morera, then the identity theorem) but left two things
    implicit, and one premise of the printed statement is false. (i) The printed arc S = {-i +
    2e^{it} : pi/4 < t < pi/2} is not contained in the boundary of U: for t below pi/4 +
    arcsin(sqrt2/4) the point lies outside the closed disc D(-1,2), so it is not in the closure
    of U at all. The statement is kept as printed, the conclusion is unaffected because the
    hypothesis constrains only sequences in U, and the subarc S_0 that does lie on the boundary
    is computed explicitly and used. (ii) The sketch asserted Morera without the polygon
    decomposition that makes the boundary integral vanish, which is now written out, and it did
    not say why U is connected, which is now the convexity of an intersection of four discs.
    Also added: the sequential-to-neighbourhood form of the hypothesis, since continuity of F
    across the arc needs the neighbourhood statement and not just sequences. Not claimed: a
    retained solution set; the collection's provenance is the examination paper only.
---

::: {.problem}
Let $U \subset \CC$ be the "rounded square" given by the intersection of the four open disks $$U = \DD(1, 2) \cap \DD(-1, 2) \cap \DD(i, 2) \cap \DD(-i, 2).$$ Let $S \subset \partial U$ be the curve $S = \{-i + 2e^{it} : t \in (\pi/4, \pi/2)\}$.
Suppose that $f \in \operatorname{Hol}(U)$, and that for any sequence $z_n \in U$ such that $\lim_{n \to \infty} z_n \in S$, it follows that $\lim_{n \to \infty} f(z_n) = 0$.
Prove that $f \equiv 0$.
:::

::: {.solution}
Write $D(c,r)$ for the open disc of radius $r$ about $c$, so that $U = D(1,2) \cap D(-1,2) \cap D(i,2) \cap D(-i,2)$ and $C \coloneqq \partial D(-i,2)$ is the circle $\abs{z+i} = 2$. The printed arc is $S = \theset{-i + 2e^{it} \mid \pi/4 < t < \pi/2}$. One point of the statement needs care: not all of $S$ lies on $\partial U$. For $z = -i + 2e^{it}$ one computes $\abs{z-i}^{2} = 8 - 8\sin t$, $\abs{z-1}^{2} = 6 - 4(\cos t + \sin t)$ and $\abs{z+1}^{2} = 6 + 4(\cos t - \sin t)$, so $z$ lies in the closure of all four discs exactly when $\sin t \ge 1/2$, $\cos t + \sin t \ge 1/2$ and $\sin t - \cos t \ge 1/2$; the first two hold for every $t \in (\pi/4,\pi/2)$ and the third holds from $t_{0} \coloneqq \pi/4 + \arcsin(\sqrt2/4)$ on. Hence $S_{0} \coloneqq \theset{-i + 2e^{it} \mid t_{0} < t < \pi/2}$ is a nonempty relatively open subarc of $S$ contained in $\partial U$, and the argument below uses $S_{0}$. The conclusion is unaffected: the hypothesis is about sequences in $U$, so only the part of $S$ on $\partial U$ can carry information. The collection's `provenance` is the Spring 2013 examination paper, and no solutions sheet accompanies it.

::: pf

::: {.pf-step #domain}
$U$ is open, convex and connected, and $0 \in U$.

::: pf-proof
Each $D(c,2)$ is open and convex, an intersection of finitely many open sets is open, and an intersection of convex sets is convex; hence $U$ is open and convex, and a convex set is path connected. Also $\abs{0-1} = \abs{0+1} = \abs{0-i} = \abs{0+i} = 1 < 2$, so $0$ lies in each disc and hence in $U$.

:::

:::

::: {.pf-step #subarc}
$S_{0} \subseteq S \cap \partial U$, and $S_{0}$ is nonempty and open in $S$.

::: pf-proof
Let $z = -i + 2e^{it}$ with $t_{0} < t < \pi/2$. Then $\abs{z+i} = 2$, so $z \in C \subseteq \partial D(-i,2)$. The three distances computed above show $z$ is in the closed discs $D(i,2)$, $D(1,2)$ and $D(-1,2)$: indeed $\sin t > \sin(\pi/4) = \sqrt2/2 > 1/2$, and $\cos t + \sin t \ge 1$ on $(\pi/4,\pi/2)$, while $t > t_{0}$ gives $\sin t - \cos t = \sqrt2\sin(t - \pi/4) > \sqrt2\cdot\frac{\sqrt2}{4} = 1/2$. So $z$ lies in the closure of $U$ but not in $U$, since $z \notin D(-i,2)$; that is $z \in \partial U$. The interval $(t_{0},\pi/2)$ is nonempty because $t_{0} = \pi/4 + \arcsin(\sqrt2/4) < \pi/4 + \pi/4 < \pi/2$, and it is open in $(\pi/4,\pi/2)$.

:::

:::

::: {.pf-step #limit}
For each $\zeta \in S_{0}$ and each $\varepsilon > 0$ there is $\rho > 0$ with $\abs{f(z)} < \varepsilon$ for every $z \in U$ with $\abs{z - \zeta} < \rho$.

::: pf-proof
The hypothesis says that every sequence $z_{n} \in U$ with $z_{n} \to \zeta \in S$ has $f(z_{n}) \to 0$. If the assertion failed, there would be $\varepsilon > 0$ and, for each $n$, a point $z_{n} \in U$ with $\abs{z_{n}-\zeta} < 1/n$ and $\abs{f(z_{n})} \ge \varepsilon$; then $z_{n} \to \zeta \in S_{0} \subseteq S$, so $f(z_{n}) \to 0$ by the hypothesis, contradicting $\abs{f(z_{n})} \ge \varepsilon$.

:::

:::

::: {.pf-step #patch}
There are an open set $\Omega \supseteq U$ and a continuous $F$ on $\Omega$ that equals $f$ on $U$, vanishes on a nonempty open subset of $\Omega$, and is holomorphic on $\Omega$ minus $S_{0}$.

::: pf-proof
Fix $\zeta_{0} \in S_{0}$ and a disc $W$ about $\zeta_{0}$ so small that $W$ meets $C$ in a subarc of $S_{0}$ and misses the other three circles $\partial D(1,2), \partial D(-1,2), \partial D(i,2)$. Inside $W$ the circle $C$ separates $W$ into two components, one of which is $W \cap U$; let $\Omega_{0}$ be the other one, so that $W = (W \cap U) \cup (W \cap C) \cup \Omega_{0}$. Put $\Omega \coloneqq U \cup S_{0} \cup \Omega_{0}$ and define $F \coloneqq f$ on $U$ and $F \coloneqq 0$ on $\Omega_{0}$. Then $\Omega$ is open: at a point of $S_{0}$ it contains a small disc, since $W \subseteq \Omega$ and $\Omega$ contains $U$ and $\Omega_{0}$; and $\Omega$ is connected, since $U$ is connected and meets the connected set $W$. $F$ is continuous: off $W \cap C$ it is either $f$, holomorphic, or $0$; and at $\zeta \in S_{0}$ the limit from $\Omega_{0}$ is $0$ by definition and the limit from $U$ is $0$ by step [](#limit){.pf-ref}, so $F(\zeta) \coloneqq 0$ is a continuous value. Finally $F$ vanishes on the nonempty open set $\Omega_{0}$, and is holomorphic wherever it is not the arc $S_{0}$, since $f$ is holomorphic on $U$ and $0$ is holomorphic on $\Omega_{0}$.

:::

:::

::: {.pf-step #morera}
$F$ is holomorphic on $\Omega$.

::: pf-proof
By Morera's theorem it suffices that $\oint_{\partial T}F\\,dz = 0$ for every closed triangle $T \subseteq \Omega$. If $\partial T$ misses $C$, then $T$ lies in $U$, where $F = f$ is holomorphic, or in $\Omega_{0}$, where $F = 0$, or in $\Omega \setminus (U \cup \Omega_{0})$, which is empty away from the arc; so Cauchy's theorem gives $0$. Otherwise $\partial T$ meets the arc finitely often, and the part of $\partial T$ inside $U$ splits into finitely many polygonal paths $P_{1},\ldots,P_{m}$, each closed up by a subarc $\alpha_{j}$ of $C \cap S_{0}$ into a closed polygon inside $U \cup S_{0}$. On each such polygon $f$ is continuous on the closure and holomorphic inside, so $\int_{P_{j}}f + \int_{\alpha_{j}}f = 0$; and $f = 0$ on $\alpha_{j} \subseteq S_{0}$, so $\int_{P_{j}}F = 0$. The remaining part of $\partial T$ lies in $\Omega_{0}$, where $F = 0$, so its integral is $0$ as well. Summing, $\oint_{\partial T}F = 0$.

:::

:::

::: {.pf-step #zero}
$F \equiv 0$ on $\Omega$, hence $f \equiv 0$ on $U$.

::: pf-proof
$\Omega$ is open and connected by step [](#patch){.pf-ref}, $F$ is holomorphic there by step [](#morera){.pf-ref}, and $F$ vanishes on the nonempty open subset $\Omega_{0}$; the identity theorem gives $F \equiv 0$ on $\Omega$. Since $F = f$ on $U$, the function $f$ vanishes identically on $U$.

:::

:::

::: pf-step
$f \equiv 0$ on $U$.

::: pf-proof
Step [](#zero){.pf-ref} is the assertion, and it used only the values of $f$ on $U$ and its boundary behaviour on the subarc $S_{0}$ of $S \cap \partial U$.

:::

:::

:::
:::
