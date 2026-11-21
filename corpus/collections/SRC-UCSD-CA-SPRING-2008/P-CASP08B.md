---
schema: qual/card@1
id: P-CASP08B
kind: problem
title: "True or False: Cauchy estimates, entire extensions, zero products, essential singularities, and bounded below harmonic functions"
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
    Restructured as a Lamport proof of the five determinations already on the card, all of which
    are correct. Added: the maximum-modulus step that turns the bound on the circle into a bound
    on the disc before Cauchy's estimate in (a); the reason 1/(1-z) is not entire in (b), namely
    that it is unbounded on the disc; the identity-theorem justification of 'choose a point
    where f is not zero' in (c), including that the zero set of a nonzero holomorphic function
    has empty interior; and in (e) the derivation of F constant from e^{-F} constant. The
    Casorati--Weierstrass route of (d) was kept and its singularity classification made
    explicit. Not claimed: a retained solution set; the collection's provenance is the
    examination paper only.
---

::: {.problem}
For each part, determine if it is always true or sometimes false.
If true give a brief proof.
If false give a counterexample.

(a) If $f \in H(\DD)$ with $\abs{f(z)} \leq 3$ for all $z$ satisfying $\abs{z} = 1/2$, then $\abs{f''(0)} \leq 24$.

(b) Suppose $f \in H(\DD)$ and there exists $C > 0$ such that $\abs{f^{(n)}(0)} \leq Cn!$ for all $n \in \NN$.
Then $f$ extends to an entire function.

(c) Let $f, g \in H(G)$, where $G$ is open and connected in $\CC$.
If $f(z)g(z) \equiv 0$, then either $f$ or $g$ is identically zero in $G$.

(d) Suppose $f \in H(\DD \setminus \{0\})$ such that for any positive integer $m$ and any constant $R > 0$, there exists $z \in B(0; 1/2) \setminus \{0\}$ with $\abs{z^m f(z)} > R$.
Then for any $c \in \CC$ and any $\epsilon > 0$ there exists $z \in \DD \setminus \{0\}$ with $\abs{f(z) - c} < \epsilon$.

(e) If $u(z)$ is a (real-valued) harmonic function defined in all of $\CC$ and satisfying $u(z) \geq -1$ for all $z \in \CC$, then $u$ is constant.
:::

::: {.solution}
Throughout $\DD$ is the open unit disc, $H(G)$ is the algebra of holomorphic functions on an open set $G$, and $B(0;r) = \theset{z \mid \abs{z} < r}$. The collection's `provenance` is the Spring 2008 examination paper, and no solutions sheet accompanies it, so the arguments below are the card's own.

::: pf

::: {.pf-step #a}
(a) True: if $f \in H(\DD)$ and $\abs{f} \le 3$ on $\abs{z} = 1/2$ then $\abs{f''(0)} \le 24$.

::: pf-proof
By the maximum modulus principle, applied to $f$ on the disc $B(0;1/2)$ whose boundary circle is $\abs{z} = 1/2$, one has $\abs{f} \le 3$ on all of $B(0;1/2)$. Cauchy's estimate for the second derivative on that disc, of radius $r = 1/2$, is $\abs{f''(0)} \le \frac{2!\\,M}{r^{2}}$ with $M = 3$, which gives $\frac{2 \cdot 3}{1/4} = 24$.

:::

:::

::: {.pf-step #b}
(b) False: the hypothesis holds for $f(z) = \frac{1}{1-z}$ while $f$ is not entire.

::: pf-proof
$f(z) = \sum_{n \ge 0}z^{n}$ on $\DD$, so $f \in H(\DD)$ with $f^{(n)}(0) = n!$, and the hypothesis holds with $C = 1$. But $\abs{f(z)} \to \infty$ as $z \to 1$ inside $\DD$, so $f$ is unbounded on $\DD$ and cannot be the restriction of an entire function, which would be continuous hence bounded on the compact set $\overline{B(0;1/2)}$ and, more decisively, would extend holomorphically across $z = 1$.

:::

:::

::: {.pf-step #c}
(c) True: if $f, g \in H(G)$ with $G$ open and connected and $fg \equiv 0$, then $f \equiv 0$ or $g \equiv 0$.

::: pf-proof
Suppose $f$ is not identically zero. Then its zero set has empty interior: if $f$ vanished on an open set $U \subseteq G$, the identity theorem would force $f \equiv 0$ on the connected $G$. So there is $z_{0} \in G$ with $f(z_{0}) \ne 0$, and by continuity $f \ne 0$ on a neighbourhood $U$ of $z_{0}$; on $U$ the identity $fg = 0$ gives $g = 0$, so $g$ vanishes on the open set $U$, and the identity theorem on the connected $G$ gives $g \equiv 0$.

:::

:::

::: {.pf-step #d-singularity}
(d) The hypothesis forces $0$ to be an essential singularity of $f$.

::: pf-proof
The hypothesis says that for every $m \ge 1$ and every $R > 0$ the function $z^{m}f(z)$ is unbounded on $B(0;1/2)\setminus\theset{0} \subseteq \DD\setminus\theset{0}$. If $0$ were removable, $f$ would be bounded near $0$ and so would every $z^{m}f(z)$, contrary to the hypothesis with $m = 1$. If $0$ were a pole of order $N$, then $z^{N}f(z)$ would tend to a finite nonzero limit at $0$, hence be bounded on $B(0;1/2)\setminus\theset{0}$, again contrary to the hypothesis. So the singularity is neither removable nor a pole.

:::

:::

::: {.pf-step #d}
(d) True: for every $c \in \CC$ and $\varepsilon > 0$ there is $z \in \DD\setminus\theset{0}$ with $\abs{f(z) - c} < \varepsilon$.

::: pf-proof
By step [](#d-singularity){.pf-ref} and the Casorati--Weierstrass theorem, the image under $f$ of every punctured neighbourhood of $0$ is dense in $\CC$. The set $B(0;1/2)\setminus\theset{0}$ is such a neighbourhood and is contained in $\DD\setminus\theset{0}$, so the image of $\DD\setminus\theset{0}$ is dense and meets the disc of radius $\varepsilon$ about any $c$.

:::

:::

::: {.pf-step #e}
(e) True: a real-valued harmonic $u$ on all of $\CC$ with $u \ge -1$ is constant.

::: pf-proof
$\CC$ is simply connected, so $u$ has a harmonic conjugate $v$ on $\CC$ and $F = u + iv$ is entire. Then $\abs{e^{-F}} = e^{-\operatorname{Re}F} = e^{-u} \le e$, since $u \ge -1$ and $e^{-u} \le e^{1}$. So $e^{-F}$ is a bounded entire function, hence constant by Liouville's theorem; then $F$ is constant, because $e^{-F}$ constant forces $F$ to take values in a single residue class modulo $2\pi i$ and $F$ is continuous on the connected set $\CC$. Hence $u = \operatorname{Re}F$ is constant.

:::

:::

::: pf-step
The five answers are: (a) true, (b) false, (c) true, (d) true, (e) true.

::: pf-proof
Steps [](#a){.pf-ref}, [](#b){.pf-ref}, [](#c){.pf-ref}, [](#d){.pf-ref} and [](#e){.pf-ref} settle the five parts, in order; the only false statement is (b), whose counterexample is $1/(1-z)$ with $C = 1$.

:::

:::

:::
:::
