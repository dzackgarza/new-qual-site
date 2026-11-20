---
schema: qual/card@1
id: E-2TY2B
kind: problem
title: Completion via Cauchy sequences
classification:
  areas:
  - topology
  topics:
  - Metric Spaces
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
    No complete published solution of Munkres §43 Exercise 9 (printed p. 271) was located in any set searched; the search
    is recorded in the COMPLAINTS.md entry for §43--§50 of SRC-TEXT-MUN00, and the proof on the card is
    checked line by line against the book. Checked against Munkres, Topology (2000), §43 Exercise 9,
    printed p. 271, with the definition of Cauchy sequence and the triangle inequality: part (a) the
    three axioms of an equivalence relation and the independence of the limit of d(x_n,y_n) from the
    representatives, using |d(x_n,y_n) - d(x'_n,y'_n)| <= d(x_n,x'_n) + d(y_n,y'_n); part (b) D(h(x),h(y))
    = d(x,y) for constant sequences; part (c) D(h(x_k), [x]) = lim_n d(x_k,x_n) <= eps for k >= N, which
    is the exercise's own assertion; part (d) the standard dense-subset criterion, with the interleaved
    approximation 1/k; part (e) every Cauchy sequence of the dense subspace h(X) converges in Y by part
    (c), so part (d) applies to the complete space Y itself. Nothing on the card needed correction.
- event: source-checked
  by: claude
  date: 2026-11-15
  note: >-
    Searched outside the checkout for a published solution of this exercise and found none
    (issue #144). Math StackExchange through the API, site math: the queries "completion metric
    space Cauchy sequences equivalence classes", "isometric embedding complete metric space
    Cauchy sequences", "equivalence classes of Cauchy sequences completion" and "completion of a
    metric space construction" return questions 3254928, 4865381, 604070, 1053685, 2243047 and
    2671069, and none of them works the five parts of the exercise, 604070 discussing the idea of
    the construction only. dbFin has no chapter-7 page (404, checked 2026-11-15), and none of the
    twelve GitHub Munkres repositories named in the COMPLAINTS.md entry for §30--§36 reaches
    Chapter 7. The card keeps its own proof, which this pass did not re-read; the search is
    recorded in the COMPLAINTS.md entry for §43--§50 with every query.

- event: source-checked
  by: claude
  date: 2026-11-15
  note: >-
    Searched outside the checkout (issue #144). The AoPS blog post by cinnamon_e, "Topology by
    Munkres Chapter 6 + 7 | Day 15" (2025-09-08,
    https://artofproblemsolving.com/community/c3401823h3645909, text at
    tmp/sources/aops-shooting-star-munkres-ch6-7-day15.md), answers this exercise, at its item 9 of
    §43. The text is held, but the formulas are not: the extraction drops every inline formula, so
    the answer reads as the words between blanks and cannot be transcribed or checked. It is
    recorded here and in the COMPLAINTS.md entry for §43--§50 as located with its formulas
    unreadable, the site answering an automated request with a Cloudflare human check, which is not
    worked around. The card keeps its own proof.
- event: solution-written
  by: claude
  date: 2026-11-19
  note: >-
    Every step now carries a pf-proof. The five containers keep their nested steps and now say why those
    subclaims suffice, and the 20 leaf steps that asserted a claim with no justification each carry a
    sentence deriving it. The mathematics is unchanged: the three properties of the relation, the
    quadrilateral bound giving convergence of d(x_n,y_n), independence of representatives, the metric
    axioms by passage to the limit, the computation D(h(x),h(y))=d(x,y), openness of h on balls,
    D(h(x_k),[x]) equal to lim d(x_k,x_n) and at most eps, the 1/k approximation in the dense subset, and
    the application of part (d) to h(X). Checked against Munkres, Topology (2000), section 43 Exercise 9,
    printed p. 271. The trailing Q.E.D. sentence was dropped from the last step because the filter
    labels that step itself. Nothing in the statement was changed.
- event: solution-reviewed
  by: claude
  date: 2026-11-20
  note: >-
    Issue #169 read, all five parts. (a) is correct: the quadrilateral bound gives both the
    convergence of $d(x_n,y_n)$ in $\RR$ and its independence of the representatives, and the
    metric axioms pass to the limit. (b): $D(h(x),h(y))=d(x,y)$ on constant sequences, so $h$ is
    injective and carries balls to traces of balls. (c): $D(h(x_k),[\mathbf x])=\lim_nd(x_k,x_n)$,
    which the Cauchy condition bounds by $\varepsilon$ for $k\ge N$. (d) is correct, the
    approximating sequence $a_k$ being Cauchy in $A$ and converging in $Z$. (e) applies (d) to
    $A=h(X)$: a Cauchy sequence in $h(X)$ is the image of a Cauchy sequence of $X$ and converges
    to its class by (c). No numbered theorem is cited beyond the completeness of $\RR$ in (a). The
    solution had no provenance sentence; one now says the construction is the exercise's own
    outline carried out. Citation by number: §43 Exercise 9, read in
    `tmp/sources/munkres-2000-topology.md`.

- event: source-corrected
  by: claude
  date: 2026-11-20
  note: >-
    Issue #169 second read, on the verification member's report of this card. The last step of
    part (c) drew membership of $h(x_k)$ in the open ball of radius $\varepsilon$ about
    $[\mathbf x]$ from the bound $D\le\varepsilon$, and an open ball asks for strict inequality.
    The Cauchy condition is now run at $\varepsilon/2$, so the limit satisfies
    $D(h(x_k),[\mathbf x])\le\varepsilon/2<\varepsilon$. Convergence and density stand. Not
    changed: the five part headings read as labels rather than claims; each of their proofs
    carries the corresponding assertions.

---

::: {.exercise}

Let $(X, d)$ be a metric space.
Show that there is an isometric imbedding $h$ of $X$ into a complete metric space $(Y, D)$, as follows.
Let $\tilde{X}$ denote the set of all Cauchy sequences

$$
\mathbf{x} = (x_1, x_2, \dots)
$$

of points of $X$.
Define $\mathbf{x} \sim \mathbf{y}$ if

$$
d(x_n, y_n) \to 0.
$$

Let $[\mathbf{x}]$ denote the equivalence class of $\mathbf{x}$; and let $Y$ denote the set of these equivalence classes.
Define a metric $D$ on $Y$ by the equation

$$
D([\mathbf{x}], [\mathbf{y}]) = \lim_{n \to \infty} d(x_n, y_n).
$$

(a) Show that $\sim$ is an equivalence relation, and show that $D$ is a well-defined metric.

(b) Define $h: X \to Y$ by letting $h(x)$ be the equivalence class of the constant sequence $(x, x, \ldots)$:

$$
h(x) = [(x, x, \dots)].
$$

Show that $h$ is an isometric imbedding.

(c) Show that $h(X)$ is dense in $Y$; indeed, given $\mathbf{x} = (x_1, x_2, \ldots) \in \tilde{X}$, show the sequence $h(x_n)$ of points of $Y$ converges to the point $[\mathbf{x}]$ of $Y$.

(d) Show that if $A$ is a dense subset of a metric space $(Z, \rho)$, and if every Cauchy sequence in $A$ converges in $Z$, then $Z$ is complete.

(e) Show that $(Y, D)$ is complete.
:::

::: {.solution}

The construction is the exercise's outline carried out step by step; the argument is the card's own, and the audit records what was searched.

::: pf

::: pf-step
Part (a): Equivalence relation and well-defined metric $D$.

::: pf-proof
The subclaims establish the three properties of $\sim$, the existence of the limit that defines $D$, its independence of the chosen representatives, and the three metric axioms.

::: pf-step
**Equivalence relation:**
- Reflexivity: $d(x_n, x_n) = 0 \to 0$.
- Symmetry: $d(x_n, y_n) = d(y_n, x_n) \to 0$.
- Transitivity: $d(x_n, z_n) \le d(x_n, y_n) + d(y_n, z_n) \to 0 + 0 = 0$.

::: pf-proof
Reflexivity and symmetry are the two displayed identities, and the symmetry of $d$ gives the second. For transitivity, the triangle inequality in $X$ gives the displayed bound, and a sum of two sequences tending to $0$ tends to $0$; so $d(x_n,z_n)\to0$ and $\mathbf{x}\sim\mathbf{z}$.
:::

:::

::: pf-step
**Limit existence in $\RR$:** For Cauchy sequences $\mathbf{x}, \mathbf{y}$, the triangle inequality gives $\abs{d(x_n, y_n) - d(x_m, y_m)} \le d(x_n, x_m) + d(y_n, y_m) \to 0$. Thus $(d(x_n, y_n))_{n=1}^\infty$ is a Cauchy sequence in $\RR$, hence converges to a unique real limit.

::: pf-proof
The displayed inequality is the quadrilateral bound: $d(x_n,y_n)\le d(x_n,x_m)+d(x_m,y_m)+d(y_m,y_n)$ and the same with $n$ and $m$ exchanged. Given $\varepsilon>0$, the Cauchy property of $\mathbf x$ and of $\mathbf y$ supplies $N$ with $d(x_n,x_m)<\varepsilon/2$ and $d(y_n,y_m)<\varepsilon/2$ for $n,m\ge N$, so the left side is less than $\varepsilon$ and the real sequence is Cauchy. The real line is complete, so the sequence has a limit, and limits of real sequences are unique.
:::

:::

::: pf-step
**Independence of representatives:** If $\mathbf{x} \sim \mathbf{x}'$ and $\mathbf{y} \sim \mathbf{y}'$, then $\abs{d(x_n, y_n) - d(x'_n, y'_n)} \le d(x_n, x'_n) + d(y_n, y'_n) \to 0$, so $\lim d(x_n, y_n) = \lim d(x'_n, y'_n)$.

::: pf-proof
The bound is again the quadrilateral inequality, through $x'_n$ and $y'_n$. Its right side tends to $0$ by the two equivalences, so the two real sequences differ by a null sequence; two convergent sequences that differ by a null sequence have the same limit.
:::

:::

::: pf-step
**Metric axioms:**
- $D([\mathbf{x}], [\mathbf{y}]) \ge 0$ and $D([\mathbf{x}], [\mathbf{y}]) = 0 \iff \lim d(x_n, y_n) = 0 \iff \mathbf{x} \sim \mathbf{y} \iff [\mathbf{x}] = [\mathbf{y}]$.
- Symmetry: $D([\mathbf{x}], [\mathbf{y}]) = D([\mathbf{y}], [\mathbf{x}])$.
- Triangle inequality: $D([\mathbf{x}], [\mathbf{z}]) = \lim d(x_n, z_n) \le \lim (d(x_n, y_n) + d(y_n, z_n)) = D([\mathbf{x}], [\mathbf{y}]) + D([\mathbf{y}], [\mathbf{z}])$.

::: pf-proof
Each bullet takes the limit of the corresponding property of $d$ along the sequences: $d\ge0$ gives non-negativity, and $D=0$ is exactly the relation $\sim$, whose classes are the points of $Y$; symmetry is the symmetry of $d$; and the triangle inequality follows by passing to the limit in $d(x_n,z_n)\le d(x_n,y_n)+d(y_n,z_n)$, legitimate because limits respect sums and order.
:::

:::

:::

:::

::: pf-step
Part (b): Isometric embedding $h: X \to Y$.

::: pf-proof
The first subclaim computes $D$ on the image of $h$, and the second draws the consequence that $h$ is an isometry onto its image.

::: pf-step
For $x, y \in X$, $D(h(x), h(y)) = \lim_{n \to \infty} d(x, y) = d(x, y)$.

::: pf-proof
The constant sequences $(x,x,\dots)$ and $(y,y,\dots)$ are Cauchy, and $d(x,y)$ is the constant value of the sequence $d(x_n,y_n)$ whose limit defines $D$.
:::

:::

::: pf-step
Thus $h$ preserves all pairwise distances, which proves $h$ is an isometric embedding (injective and topological embedding).

::: pf-proof
If $h(x)=h(y)$ then $d(x,y)=D(h(x),h(y))=0$, so $x=y$ and $h$ is injective. For $r>0$ one has $h(B_r(x))=B_r(h(x))\cap h(X)$, because $h$ preserves distances, so $h$ carries the open balls of $X$ onto the traces of the open balls of $Y$; a bijection onto its image with that property is a homeomorphism onto $h(X)$.
:::

:::

:::

:::

::: {.pf-step #part-c}
Part (c): Density of $h(X)$ in $Y$.

::: pf-proof
The subclaims compute the distance from $h(x_k)$ to $[\mathbf{x}]$ and show that it tends to $0$ with $k$.

::: pf-step
Let $[\mathbf{x}] \in Y$ where $\mathbf{x} = (x_1, x_2, \dots) \in \tilde{X}$.

::: pf-proof
Every point of $Y$ is the class of a Cauchy sequence in $X$ by the construction of $Y$.
:::

:::

::: pf-step
For each fixed $k \in \ZZ_+$, $D(h(x_k), [\mathbf{x}]) = \lim_{n \to \infty} d(x_k, x_n)$.

::: pf-proof
This is the definition of $D$ applied to the constant sequence at $x_k$ and to $\mathbf{x}$; the limit exists by the second subclaim of part (a).
:::

:::

::: pf-step
Given $\varepsilon > 0$, choose $N$ such that $d(x_k, x_n) < \varepsilon/2$ for all $k, n \ge N$.

::: pf-proof
This is the Cauchy condition for the sequence $\mathbf{x}$, read with $\varepsilon$ as the bound.
:::

:::

::: pf-step
Taking $n \to \infty$ yields $D(h(x_k), [\mathbf{x}]) \le \varepsilon/2 < \varepsilon$ for all $k \ge N$.

::: pf-proof
For fixed $k\ge N$ every term $d(x_k,x_n)$ with $n\ge N$ is less than $\varepsilon$, and a limit of real numbers all less than $\varepsilon$ is at most $\varepsilon$; the limit is $D(h(x_k),[\mathbf{x}])$ by the second subclaim.
:::

:::

::: pf-step
Hence $\lim_{k \to \infty} h(x_k) = [\mathbf{x}]$ in $(Y, D)$, proving $h(X)$ is dense in $Y$.

::: pf-proof
The preceding subclaim is precisely the statement that for every $\varepsilon>0$ the points $h(x_k)$ with $k\ge N$ lie in the ball of radius $\varepsilon$ about $[\mathbf{x}]$. As $[\mathbf{x}]$ was arbitrary, every ball in $Y$ meets $h(X)$.
:::

:::

:::

:::

::: pf-step
Part (d): Density criterion for completeness.

::: pf-proof
The subclaims approximate an arbitrary Cauchy sequence of $Z$ by a Cauchy sequence of the dense subset $A$ and transfer the limit back.

::: pf-step
Let $(z_k)$ be a Cauchy sequence in $(Z, \rho)$.

::: pf-proof
This is the arbitrary Cauchy sequence for which a limit has to be produced.
:::

:::

::: pf-step
Since $A$ is dense, for each $k$ choose $a_k \in A$ with $\rho(a_k, z_k) < \frac{1}{k}$.

::: pf-proof
Density of $A$ means that every ball about a point of $Z$ contains a point of $A$; apply this to the ball of radius $1/k$ about $z_k$.
:::

:::

::: pf-step
Then $\rho(a_j, a_k) \le \rho(a_j, z_j) + \rho(z_j, z_k) + \rho(z_k, a_k) < \frac{1}{j} + \rho(z_j, z_k) + \frac{1}{k} \to 0$, so $(a_k)$ is Cauchy in $A$.

::: pf-proof
The displayed inequality is the triangle inequality through $z_j$ and $z_k$. Given $\varepsilon>0$, choose $N$ with $1/N<\varepsilon/3$ and $\rho(z_j,z_k)<\varepsilon/3$ for $j,k\ge N$; then $\rho(a_j,a_k)<\varepsilon$ for $j,k\ge N$, which is the Cauchy condition.
:::

:::

::: pf-step
By hypothesis, $(a_k)$ converges to some $z \in Z$.

::: pf-proof
The hypothesis on $A$ is that every Cauchy sequence of points of $A$ converges in $Z$, and $(a_k)$ is such a sequence by the preceding subclaim.
:::

:::

::: pf-step
Then $\rho(z_k, z) \le \rho(z_k, a_k) + \rho(a_k, z) < \frac{1}{k} + \rho(a_k, z) \to 0$, so $z_k \to z$, proving $Z$ is complete.

::: pf-proof
The bound is the triangle inequality through $a_k$, together with the choice $\rho(z_k,a_k)<1/k$. Both terms on the right tend to $0$, so $\rho(z_k,z)\to0$. Every Cauchy sequence of $Z$ thus converges, which is the definition of completeness.
:::

:::

:::

:::

::: pf-step
Part (e): Completeness of $(Y, D)$.

::: pf-proof
The subclaims verify the hypothesis of part (d) for the dense subset $h(X)$ of $Y$.

::: pf-step
Let $(h(x_k))_{k=1}^\infty$ be a Cauchy sequence in $h(X)$.

::: pf-proof
This is an arbitrary Cauchy sequence in the subspace $h(X)$ of $Y$.
:::

:::

::: pf-step
Since $h$ is an isometry, $d(x_j, x_k) = D(h(x_j), h(x_k)) \to 0$, so $\mathbf{x} = (x_1, x_2, \dots) \in \tilde{X}$.

::: pf-proof
The equality is the isometry of part (b); a Cauchy sequence of points of $X$ is by definition an element of $\tilde X$, the set of all Cauchy sequences.
:::

:::

::: pf-step
By step [](#part-c){.pf-ref}, $h(x_k) \to [\mathbf{x}] \in Y$.

::: pf-proof
Part (c) states that $h(x_n)\to[\mathbf{x}]$ for $\mathbf{x}=(x_1,x_2,\dots)$, which is exactly the sequence at hand.
:::

:::

::: pf-step
Since $h(X)$ is dense in $Y$ and every Cauchy sequence in $h(X)$ converges in $Y$, part (d) implies $(Y, D)$ is complete.

::: pf-proof
Part (d) applies with $A=h(X)$, $Z=Y$ and $\rho=D$: $h(X)$ is dense in $Y$ by part (c), and the preceding subclaims show that every Cauchy sequence in $h(X)$ converges in $Y$.
:::

:::

:::

:::

:::

:::
