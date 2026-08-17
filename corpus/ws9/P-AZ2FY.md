---
schema: qual/card@1
id: P-AZ2FY
kind: problem
title: For a Radon measure $\mu$, with $\int_{\mathbb{R}^n} d\mu = C$. Prove…
classification:
  areas:
  - real-analysis
  topics:
  - measure-theory
relations: []
review: draft
solved: true
---

::: {.problem title="?"}
For a Radon measure $\mu$, with $\int_{\mathbb{R}^n} d\mu = C$.
Prove that for all $\epsilon > 0$, there exists a set $E_\epsilon \subset \mathbb{R}^n$ s.t. $\mathcal{M}^1(E_\epsilon) := \inf_{E_\epsilon \subset \cup B_i}\{\sum_i \operatorname{diam} B_i\} < 10\epsilon$ and for any $x \notin E_\epsilon$, $r > 0$ $$\int_{B_r(x)} d\mu \le \frac{Cr}{\epsilon}.$$ (Hint: use Vitali covering lemma.)
:::
::: {.solution}
> **AI-Generated Solution**

<1>1. Define the set where the desired inequality fails.
Proof: let $E_\eps = \Big\{x : \exists r > 0 \text{ with } \int_{B_r(x)}d\mu > \frac{Cr}{\eps}\Big\}$.
For $x \notin E_\eps$, the inequality $\int_{B_r(x)}d\mu \le Cr/\eps$ holds for every $r > 0$ by construction.
<1>2. For each $x \in E_\eps$ pick a ball with the strict inequality.
Proof: by definition of $E_\eps$, for each $x \in E_\eps$ there is $r_x > 0$ with $\mu(B_{r_x}(x)) > Cr_x/\eps$, i.e. $r_x < \eps\,\mu(B_{r_x}(x))/C$.
<1>3. Apply the Vitali covering lemma.
Proof: by the Vitali covering lemma, from the family $\{B_{r_x}(x) : x \in E_\eps\}$ (balls of bounded radius, e.g. restrict to those with $r_x \le 1$, which suffices by <1>2 as $\mu(B_{r_x}(x)) \le \mu(\RR^n) = C$) we can extract a countable disjoint subfamily $\{B_i = B_{r_i}(x_i)\}$ with $E_\eps \subseteq \cup_i B_{5r_i}(x_i)$ (the $5$-times covering).
<1>4. Bound $\mathcal{M}^1(E_\eps)$.
Proof: using <1>3 and disjointness, \[ \mathcal{M}^1(E_\eps) \le \sum_i \operatorname{diam}\big(B_{5r_i}(x_i)\big) = \sum_i 10 r_i \le \frac{10\eps}{C}\sum_i \mu(B_i) \le \frac{10\eps}{C}\,\mu(\RR^n) = 10\eps , \] where the middle inequality uses $r_i < \eps\mu(B_i)/C$ from <1>2, and the last equality uses $\int d\mu = C$.
<1>5. Conclude.
Proof: $E_\eps$ satisfies $\mathcal{M}^1(E_\eps) \le 10\eps$ (<1>4) and the pointwise inequality holds off $E_\eps$ (<1>1). <1>6. Q.E.D.
:::
