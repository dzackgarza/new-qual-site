---
schema: qual/card@1
id: P-CASP11A
kind: problem
title: "True or False: bounded functions on slit planes, analytic extensions, essential singularities, Schwarz reflection, and polynomial approximation"
classification:
  areas:
  - complex-analysis
  topics:
  - Complex Analysis
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: problem
For each of the following, determine if the statement is always true or if it is false.

(a) Let $G = \{z \in \mathbb{C} : \operatorname{Re} z \notin \mathbb{Z}\}$.
Suppose $f \in H(G)$ such that $|f(z)| \leq 1$ for all $z \in G$.
Then $f$ is constant.

(b) There exists $g \in H(B(0; 2))$ with $|g(z)| < 1$ for all $|z| < 2$, with $z + g(z) \neq 0$ for all $z \in \mathbb{D}$.

(c) There is an analytic function $f$ on $\mathbb{D} \setminus \{0\}$ with an essential singularity at $z = 0$ such that $f$ can be extended as a continuous function from the whole disk $\mathbb{D}$ to the extended plane $\mathbb{C}_\infty$.

(d) Suppose that $f$ is a continuous function on $\mathbb{D} \cap \{z : \operatorname{Im} z \leq 0\}$ and analytic in $\mathbb{D} \cap \{z : \operatorname{Im} z < 0\}$.
If $\operatorname{Re} f(x) = 0$ for all $x$ with $-1 < x < 1$, then $f$ admits an analytic extension to $\mathbb{D}$.

(e) If $G \subset \mathbb{C}$ is a region and $G \cap B(0; r) = \emptyset$ for some $r > 0$, there is a 1-1 analytic function $f$ on $G$ such that $f(G) \subset \mathbb{D}$.

(f) If $f: \mathbb{C} \to \mathbb{C}$ is analytic and $\operatorname{Re} f(z) \geq c$ for some real constant $c$, then $f$ is constant.

(g) There is a polynomial $p(z)$ such that $|p(z) - 1/z| < 1$ for all $z$ in the annulus $1/2 < |z| < 3/2$.

::: {.solution}
**(a) False.**

<1>1. $G = \bigsqcup_{k \in \mathbb{Z}} \{k < \operatorname{Re} z < k+1\}$ is a disjoint union of vertical strips.
Proof: $\operatorname{Re} z \notin \mathbb{Z}$ means $z$ lies strictly between consecutive integers.

<1>2. Define $f(z) = 0$ on the strip $0 < \operatorname{Re} z < 1$ and $f(z) = 1$ on all other strips; this $f$ is analytic on $G$ (locally constant) and bounded by $1$ but not constant.
Proof: <1>1.

**(b) False.**

<1>1. Suppose such $g$ exists and set $h(z) = z + g(z)$.
Proof: assume for contradiction.

<1>2. On $|z| = 1$, $|g(z)| < 1 = |z|$.
Proof: hypothesis.

<1>3. By Rouché, $h(z) = z + g(z)$ and $z$ have the same number of zeros in $\mathbb{D}$, namely one.
Proof: <1>2 and Rouché's theorem.

<1>4. Hence $h$ has a zero in $\mathbb{D}$, contradicting $z + g(z) \neq 0$.
Proof: <1>3.

**(c) False.**

<1>1. If $f$ has an essential singularity at $0$, then by Casorati–Weierstrass (or Picard) the image of any punctured neighborhood of $0$ is dense in $\mathbb{C}$.
Proof: essential singularity.

<1>2. A continuous extension $F : \mathbb{D} \to \mathbb{C}_\infty$ would satisfy $F(0) = \lim_{z \to 0} f(z)$, so $f(z) \to F(0)$ as $z \to 0$.
Proof: continuity at $0$.

<1>3. This contradicts <1>1 (which implies $f$ has no limit at $0$, finite or $\infty$).
Proof: <1>1 and <1>2.

**(d) True.**

<1>1. The condition $\operatorname{Re} f = 0$ on $(-1,1)$ means $f$ maps the interval into $i\mathbb{R}$.
Proof: hypothesis.

<1>2. Schwarz reflection for the lower half-disk: define $F(z) = f(z)$ for $\operatorname{Im} z \le 0$ and $F(z) = -\overline{f(\bar z)}$ for $\operatorname{Im} z > 0$.
Proof: reflection principle (the map $w \mapsto -\bar w$ reflects across $i\mathbb{R}$).

<1>3. $F$ is continuous on $\mathbb{D}$ and analytic on $\mathbb{D} \setminus (-1,1)$, hence analytic on $\mathbb{D}$ (Morera).
Proof: <1>2 and Morera's theorem (or the Schwarz reflection principle).

**(e) True.**

<1>1. After translation, assume $G \subset \{|z| \ge r\}$.
Proof: hypothesis $G \cap B(0;r) = \varnothing$.

<1>2. Define $f(z) = \frac{r}{2z}$.
Proof: candidate.

<1>3. $f$ is analytic and $1$-$1$ on $G$ (it is injective on $\mathbb{C} \setminus \{0\}$).
Proof: $f(z_1) = f(z_2) \Rightarrow z_1 = z_2$.

<1>4. For $z \in G$, $|f(z)| = \frac{r}{2|z|} \le \frac{1}{2} < 1$, so $f(G) \subset \mathbb{D}$.
Proof: <1>2 and $|z| \ge r$.

**(f) True.**

<1>1. Set $g(z) = e^{-f(z)}$.
Proof: definition.

<1>2. $g$ is entire and $|g(z)| = e^{-\operatorname{Re} f(z)} \le e^{-c}$, so $g$ is bounded.
Proof: <1>1 and $\operatorname{Re} f \ge c$.

<1>3. By Liouville, $g$ is constant, hence $f$ is constant.
Proof: <1>2.

**(g) False.**

<1>1. Suppose such $p$ exists. Then $|p(z) - 1/z| < 1$ on the circle $|z| = 1$.
Proof: hypothesis (the annulus contains the unit circle).

<1>2. $\int_{|z|=1} p(z)\,dz = 0$ and $\int_{|z|=1} \frac{dz}{z} = 2\pi i$.
Proof: $p$ is entire, and $\int_{|z|=1} z^{-1}dz = 2\pi i$.

<1>3. Hence $\left|\int_{|z|=1} (p(z) - 1/z)\,dz\right| = 2\pi$.
Proof: <1>2.

<1>4. But $\left|\int_{|z|=1} (p - 1/z)\,dz\right| \le \int_{|z|=1} |p - 1/z|\,|dz| < \int_{|z|=1} 1\,|dz| = 2\pi$.
Proof: <1>1 and ML-estimate, with strict inequality since $|p - 1/z| < 1$.

<1>5. Contradiction ($2\pi < 2\pi$ impossible), so no such $p$ exists.
Proof: <1>3 and <1>4.
:::
:::
