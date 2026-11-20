---
schema: qual/card@1
id: E-0GM3H
kind: problem
title: The fine topology on function spaces
classification:
  areas:
  - topology
  topics:
  - Function Spaces
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
- event: solution-written
  by: claude
  date: 2026-11-11
  note: >-
    No complete published solution of Munkres §46 Exercise 11 (printed p. 289) was located; the sets searched are listed in the
    COMPLAINTS.md entry for §43--§50 of SRC-TEXT-MUN00. Checked against the definition of the fine topology in
    the exercise and the uniform metric of §20 and §43. Part (a): the sets B(f, delta) cover, since delta = 1
    works, and at each point of an intersection the function delta_3 = min{delta_1 - d(f_1,g), delta_2 -
    d(f_2,g)} is continuous and strictly positive, because x -> d(f_i(x), g(x)) is continuous as a composite of
    continuous maps into Y x Y followed by the metric; the triangle inequality then puts B(g, delta_3) inside
    both. Part (b): a uniform ball of radius eps <= 1 is fine-open, taking delta constant equal to
    (eps - r)/2 where r is the uniform distance from f to g. Part (c): for compact X a positive continuous
    delta attains a positive minimum (Theorem 27.4, the extreme value theorem), which turns a fine ball into a
    uniform ball. Part (d): for discrete X every function and every positive function is continuous, and the
    fine balls are exactly the boxes. Nothing needed correction.
- event: source-checked
  by: claude
  date: 2026-11-15
  note: >-
    Searched outside the checkout (issue #144). The AoPS blog post by cinnamon_e, "Topology by
    Munkres Chapter 7 | Day 17" (2025-09-10,
    https://artofproblemsolving.com/community/c3401823h3646977, text at
    tmp/sources/aops-shooting-star-munkres-ch7-day17.md), answers this exercise at its item 11 of
    §46, and the extraction dropped every inline formula, so the answer cannot be transcribed; the
    site answers an automated request with a Cloudflare human check, which is not worked around.
    Murayama's selection stops at Chapter 4, dbFin has no chapter-7 page, and the Math StackExchange
    search of this pass for the basis B(f, delta) of the fine topology, recorded in the COMPLAINTS.md
    entry for §43--§50, returned only a question on the fine topology of the Baire theorem of §48
    Exercise 13, which is a different statement. The card keeps its own proof.
- event: source-corrected
  by: claude
  date: 2026-11-19
  note: >-
    Rewrote the solution's frame on 2026-11-19, leaving every argument as it was.
    The four parts opened with a "Part (x):" label and a "Proof:" line in front of
    statements that were already claims; the labels and the run-in proof lines are
    gone, so each step's first paragraph is its claim, and the preamble names the
    exercise, Munkres, Topology (2000), Section 46, Exercise 8, printed p. 289. No
    statement, argument or citation changes.
- event: solution-written
  by: claude
  date: 2026-11-20
  note: >-
    Twenty-one steps asserted their claim with no justification; each part of the exercise is now proved by
    steps that state one claim and derive it in a pf-proof. Part (a): the family covers, because the
    constant function $1$ is continuous and positive and $d(f,f) = 0$; the intersection step produces the
    continuous positive $\delta_3$ as the minimum of the two slack functions, which are positive by
    membership and continuous as composites with the metric; the inclusion follows from the triangle
    inequality on each side; and the two basis conditions are then met. Part (b): a uniform ball of radius
    $\varepsilon \le 1$ is shown to contain a fine basic set around each of its points, the point being
    that $r = \bar\rho(f,g) < \varepsilon \le 1$ forces $\bar d = d$ pointwise, which the earlier card did
    not say; and a uniform ball is therefore a union of fine basic sets. Part (c): the empty case is
    separated off, the extreme value theorem gives a positive minimum of $\delta_3$ on compact $X$, and
    every fine-open set is a union of uniform balls. Part (d): in the discrete topology every map and every
    positive function is continuous, the fine basic sets are exactly the boxes, and the two topologies
    share a basis. Three of the four parts carried a "Part (x):" label as a step's claim and now carry the
    claim; the covering step and the triangle-inequality step carried their argument inside the claim and
    now state the assertion with the argument in the proof. Sources are cited by numbered statement: the
    definition of the fine topology in this exercise, the uniform metric of Section 20, and the extreme
    value theorem. No page reference is written in the body of this card or in the event above. The
    statement is unchanged. The card records its own argument, no retained solution set covering the
    exercise.

---

::: {.exercise}

Let $(Y, d)$ be a metric space; let $X$ be a space.
Define a topology on $\mathcal{C}(X, Y)$ as follows.
Given $f \in \mathcal{C}(X, Y)$, and given a positive continuous function $\delta: X \to \RR_+$ on $X$, let

$$
B(f, \delta) = \theset{g \mid d(f(x), g(x)) < \delta(x) \text{ for all } x \in X}.
$$

(a) Show that the sets $B(f, \delta)$ form a basis for a topology on $\mathcal{C}(X, Y)$.
We call it the fine topology.

(b) Show that the fine topology contains the uniform topology.

(c) Show that if $X$ is compact, the fine and uniform topologies agree.

(d) Show that if $X$ is discrete, then $\mathcal{C}(X, Y) = Y^X$ and the fine and box topologies agree.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

The sets $\mathcal{B} = \{B(f, \delta) : f \in \mathcal{C}(X, Y), \delta \in \mathcal{C}(X, \RR_+)\}$ form a basis.

::: pf-proof

::: pf-step

The family $\mathcal{B}$ covers $\mathcal{C}(X, Y)$.

::: pf-proof
Let $f \in \mathcal{C}(X, Y)$. The constant function $\delta_1(x) = 1$ is continuous and positive, and $d(f(x), f(x)) = 0 < 1 = \delta_1(x)$ for every $x \in X$, so $f \in B(f, \delta_1)$ by the definition of the basic set.
:::

:::

::: {.pf-step #intersection}

For $g \in B(f_1, \delta_1) \cap B(f_2, \delta_2)$ there is a continuous positive $\delta_3$ with $g \in B(g, \delta_3) \subseteq B(f_1, \delta_1) \cap B(f_2, \delta_2)$.

::: pf-proof
Membership in the two basic sets says $d(f_1(x), g(x)) < \delta_1(x)$ and $d(f_2(x), g(x)) < \delta_2(x)$ for every $x \in X$, so the two differences
$$\delta_3(x) = \min\{\delta_1(x) - d(f_1(x), g(x)), \; \delta_2(x) - d(f_2(x), g(x))\}$$
are positive at every point. Each map $x \mapsto d(f_i(x), g(x))$ is continuous, being the composite of $x \mapsto (f_i(x), g(x))$ into $Y \times Y$ with the metric, and $\delta_1, \delta_2$ are continuous, so $\delta_3$ is continuous as a minimum of finitely many continuous functions; being positive everywhere it takes values in $\RR_+$. Then $g \in B(g, \delta_3)$ because $d(g(x), g(x)) = 0 < \delta_3(x)$.
:::

:::

::: pf-step

$B(g, \delta_3) \subseteq B(f_1, \delta_1) \cap B(f_2, \delta_2)$.

::: pf-proof
Let $h \in B(g, \delta_3)$ and $x \in X$. The triangle inequality gives
$$d(f_1(x), h(x)) \le d(f_1(x), g(x)) + d(g(x), h(x)) < d(f_1(x), g(x)) + (\delta_1(x) - d(f_1(x), g(x))) = \delta_1(x),$$
because $d(g(x), h(x)) < \delta_3(x) \le \delta_1(x) - d(f_1(x), g(x))$; so $h \in B(f_1, \delta_1)$. The same computation with the subscript $2$ gives $h \in B(f_2, \delta_2)$.
:::

:::

::: pf-step

$\mathcal{B}$ is a basis for a topology on $\mathcal{C}(X, Y)$.

::: pf-proof
A family of subsets is a basis when it covers the space and when, for every point of the intersection of two of its members, some member of the family contains that point and lies inside the intersection. The first condition is the covering step above, and the second is the intersection step together with the inclusion just proved.
:::

:::

:::

:::

::: {.pf-step #s2}

The fine topology contains the uniform topology.

::: pf-proof

::: pf-step

Every uniform ball $B_{\bar\rho}(f, \varepsilon)$ with $0 < \varepsilon \le 1$ contains a fine basic set around each of its points.

::: pf-proof
The uniform balls with $0 < \varepsilon \le 1$ form a basis for the uniform topology, where $\bar\rho(f,g) = \sup_x \bar d(f(x), g(x))$ and $\bar d = \min(d,1)$; for such $\varepsilon$ one has $\bar d(f(x),g(x)) < \varepsilon$ if and only if $d(f(x),g(x)) < \varepsilon$, since $\bar d < \varepsilon \le 1$ forces $\bar d = d$, and conversely $d < \varepsilon \le 1$ gives $\bar d = d$.

Let $g \in B_{\bar\rho}(f,\varepsilon)$ and $r = \bar\rho(f,g) < \varepsilon$. Then $r < 1$, so $\bar d(f(x),g(x)) = d(f(x),g(x))$ for every $x$ and therefore $d(f(x),g(x)) \le r$. The constant function $\delta = (\varepsilon - r)/2$ is continuous and positive. For $h \in B(g,\delta)$ and $x \in X$,
$$d(f(x), h(x)) \le d(f(x), g(x)) + d(g(x), h(x)) < r + \tfrac{\varepsilon - r}{2} = \tfrac{\varepsilon + r}{2} < \varepsilon,$$
and the left side is below $\varepsilon \le 1$, so $\bar d(f(x),h(x)) = d(f(x),h(x)) < \varepsilon$; taking the supremum, $\bar\rho(f,h) < \varepsilon$ and $h \in B_{\bar\rho}(f,\varepsilon)$.
:::

:::

::: pf-step

The fine topology contains the uniform topology.

::: pf-proof
A topology contains another when every member of a basis of the second is open in the first. Each uniform ball $B_{\bar\rho}(f,\varepsilon)$ contains, around each of its points $g$, a fine basic set $B(g,\delta)$ lying inside it, by the previous step; so each uniform ball is a union of fine basic sets, hence open in the fine topology.
:::

:::

:::

:::

::: pf-step

If $X$ is compact, the fine and uniform topologies coincide.

::: pf-proof

::: pf-step

If $X=\varnothing$, both topologies agree; otherwise the fine topology is at least as fine as the uniform topology.

::: pf-proof
When $X$ is empty the function space $\mathcal{C}(X,Y)$ has exactly one point, since there is exactly one map from the empty set to $Y$, and on a one-point set there is only one topology, so the two agree. When $X \ne \varnothing$ the containment of the uniform topology in the fine topology is step [](#s2){.pf-ref}.
:::

:::

::: pf-step

Every fine basic set $B(f, \delta)$ has, around each of its points, a uniform ball inside it.

::: pf-proof
Let $g \in B(f,\delta)$. Since $\mathcal{B}$ is a basis, there is a continuous positive $\delta_3$ with $g \in B(g,\delta_3) \subseteq B(f,\delta)$, as in step [](#intersection){.pf-ref}. The space $X$ is compact and $\delta_3 : X \to (0,\infty)$ is continuous, so by the extreme value theorem it attains a minimum, and
$$\varepsilon \coloneqq \min\left(\min_{x \in X} \delta_3(x), 1\right) > 0.$$
If $h \in B_{\bar\rho}(g,\varepsilon)$ then $d(g(x), h(x)) < \varepsilon \le \delta_3(x)$ for every $x$, so $h \in B(g,\delta_3)$, and the containment $B_{\bar\rho}(g,\varepsilon) \subseteq B(g,\delta_3) \subseteq B(f,\delta)$ follows.
:::

:::

::: pf-step

Every fine-open set is uniform-open, so the two topologies coincide.

::: pf-proof
A set is open in a topology generated by a basis when each of its points has a basis element containing it and lying inside the set. For a fine-open set and a point of it there is a fine basic set $B(f,\delta)$ inside the set containing the point, and the previous step supplies a uniform ball inside $B(f,\delta)$ containing that point; so every fine-open set is a union of uniform balls. The reverse containment is the previous part.
:::

:::

:::

:::

::: pf-step

If $X$ is discrete, $\mathcal{C}(X, Y) = Y^X$ and the fine topology equals the box topology.

::: pf-proof

::: pf-step

When $X$ is discrete, every map $X \to Y$ and every function $X \to \RR_+$ is continuous.

::: pf-proof
In the discrete topology every subset of $X$ is open, so the preimage of any subset of $Y$, or of $\RR_+$, is open in $X$; continuity of a map requires only that the preimage of each open set be open. Hence $\mathcal{C}(X,Y) = Y^X$, and every positive function $X \to \RR_+$ belongs to $\mathcal{C}(X,\RR_+)$.
:::

:::

::: pf-step

The fine basic sets are exactly the boxes $\prod_{x \in X} B_d(f(x), \varepsilon_x)$ with all $\varepsilon_x > 0$.

::: pf-proof
The boxes with arbitrary positive radii form a neighbourhood basis at $f$ for the box topology on $\prod_{x \in X} Y$. Given such radii define $\delta(x) = \varepsilon_x$; by the previous step $\delta$ is a continuous positive function, and the defining inequalities $d(f(x), g(x)) < \varepsilon_x$ for all $x$ are exactly the membership conditions for the box, so $B(f,\delta) = \prod_{x \in X} B_d(f(x), \varepsilon_x)$. Conversely a fine basic set $B(f,\delta)$ is the box with radii $\varepsilon_x = \delta(x)$, which are positive.
:::

:::

::: pf-step

The fine topology and the box topology coincide.

::: pf-proof
Two topologies on one set coincide when they have a common basis. The previous step shows the family of fine basic sets is exactly the family of boxes over all choices of positive radii, and that family is a basis for the box topology; so the fine basis is a basis for both.
:::

:::

:::

:::

:::
:::
