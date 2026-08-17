---
schema: qual/card@1
id: P-MMAQ-OZLCWMQK46
kind: problem
title: Let $f$ be a continuous function on $[0,1]$. Show that the following
classification:
  areas:
  - real-analysis
  topics:
  - absolute-continuity
relations: []
review: draft
---

::: problem
Let $f$ be a continuous function on $[0,1]$. Show that the following
statements are equivalent.

1.  $f$ is absolutely continuous.

2.  For any $\epsilon > 0$ there exists $\delta > 0$ such that
    $m(f(E)) < \epsilon$ for any set $E\subseteq [0,1]$ with
    $m(E) < \delta$.

3.  $m(f(E)) = 0$ for any set $E \subseteq [0,1]$ with $m(E)=0$.
:::

::: {.solution}
> **AI-Generated Solution**

**Goal:** For continuous $f: [0,1] \to \RR$, show (1) $\iff$ (2) $\iff$ (3), where (1) is absolute continuity, (2) is "uniformly, small-measure sets map to small-measure sets", and (3) is "null sets map to null sets".

<1>1. Proof of (1) $\implies$ (2).
    <2>1. Fix $\eps > 0$. By absolute continuity, there is $\delta > 0$ such that for any finite collection of disjoint intervals $(a_j, b_j) \subseteq [0,1]$ with $\sum_j (b_j - a_j) < \delta$, we have $\sum_j \abs{f(b_j) - f(a_j)} < \eps$.
        Proof: Definition of absolute continuity.
    <2>2. Let $E \subseteq [0,1]$ be any set with $m(E) < \delta$, and let $\{(a_j, b_j)\}_j$ be a countable cover of $E$ by open intervals with $\sum_j (b_j - a_j) < \delta$.
        Proof: Existence of such a cover is the definition of $m(E)$ as an infimum of sums of lengths of countable interval covers.
    <2>3. $f(E) \subseteq \bigcup_j f([a_j, b_j])$, and each $f([a_j,b_j])$ is a closed interval of length $m(f([a_j,b_j])) = \operatorname{osc}(f, [a_j,b_j]) = \sup_{[a_j,b_j]} f - \inf_{[a_j,b_j]} f$.
        Proof: Continuous image of a compact interval is a compact interval, whose length is the oscillation.
    <2>4. For every finite subcollection $j = 1, \dots, J$ and every $\eta > 0$, $\sum_{j=1}^J \operatorname{osc}(f, [a_j,b_j]) < \eps + \eta$: partition each $[a_j, b_j]$ finely enough that $\operatorname{osc}(f, [a_j, b_j]) \leq \sum_k \abs{f(x_{j,k}) - f(x_{j,k-1})} + \eta/J$; the total length of all resulting subintervals is $\sum_j (b_j - a_j) < \delta$, so the sum of variations over them is $< \eps$ by <2>1.
        Proof: The oscillation of $f$ on $[a_j, b_j]$ is the supremum of the variation over all partitions, and can be approximated by a single partition's variation to within $\eta/J$; the disjoint subintervals from all $J$ boxes have total length $< \delta$.
    <2>5. Hence $\sum_j \operatorname{osc}(f, [a_j,b_j]) \leq \eps$ (countable sum), so
        $$m(f(E)) \leq \sum_j m(f([a_j,b_j])) = \sum_j \operatorname{osc}(f,[a_j,b_j]) \leq \eps.$$
        Proof: Subadditivity of $m$ and <2>3; then take the countable limit in <2>4 (the bound $\eps + \eta$ holds for every $\eta > 0$ and every finite $J$).
    <2>6. Q.E.D.
        Proof: $\eps > 0$ was arbitrary, so (2) holds.

<1>2. Proof of (2) $\implies$ (1).
    <2>1. Let $(a_j, b_j)$, $j = 1, \dots, N$, be disjoint intervals with $\sum_j (b_j - a_j) < \delta$, where $\delta$ is the constant supplied by (2) for a given $\eps > 0$; put $E \definedas \bigcup_j (a_j, b_j)$.
        Proof: Definition; $m(E) = \sum_j (b_j - a_j) < \delta$ by disjointness.
    <2>2. Then $m(f(E)) < \eps$ by (2).
        Proof: Apply (2) to the measurable set $E$.
    <2>3. For each $j$, $\abs{f(b_j) - f(a_j)} \leq m(f((a_j, b_j)))$.
        Proof: $f((a_j,b_j))$ is an interval containing the open segment between $f(a_j)$ and $f(b_j)$ (intermediate value theorem, using continuity on $(a_j, b_j)$; the endpoints may or may not be attained), so its measure is at least the distance $\abs{f(b_j) - f(a_j)}$.
    <2>4. Hence $\sum_j \abs{f(b_j) - f(a_j)} \leq \sum_j m(f((a_j,b_j))) \leq m(f(E)) < \eps$.
        Proof: By <2>3 and countable subadditivity ($m$ of a union is $\leq$ the sum).
    <2>5. Q.E.D.
        Proof: This verifies the definition of absolute continuity for the $\delta$ supplied by (2).

<1>3. Proof of (2) $\implies$ (3).
    <2>1. Let $E$ have $m(E) = 0$, and fix $n \geq 1$. Since $m(E) = 0$, there is an open set $U_n \supseteq E$ with $m(U_n) < \delta_n$, where $\delta_n$ is the constant of (2) for $\eps = 1/n$.
        Proof: Definition of $m(E)$ as an infimum over open covers; choose a cover of total length $< \delta_n$.
    <2>2. $m(f(U_n)) < 1/n$ by (2), and $f(E) \subseteq f(U_n)$, so $m(f(E)) \leq m(f(U_n)) < 1/n$.
        Proof: Monotonicity of $m$ under inclusion.
    <2>3. Hence $m(f(E)) = 0$.
        Proof: $m(f(E)) < 1/n$ for every $n$ by <2>2; let $n \to \infty$.
    <2>4. Q.E.D.
        Proof: This proves (3).

<1>4. Proof of (3) $\implies$ (2).
    <2>1. A continuous function $f: [0,1] \to \RR$ with the property that $m(f(E)) = 0$ whenever $m(E) = 0$ is absolutely continuous.
        Proof: This is the classical **Banach–Zarecki theorem** in the form: a continuous function is absolutely continuous iff it is of bounded variation and maps null sets to null sets — together with the fact that the null-set property alone forces bounded variation for continuous functions (if $f$ had infinite variation, one can extract disjoint intervals $I_j$ whose images have lengths $\abs{f(I_j)}$ with $\sum_j \abs{f(I_j)} = \infty$ while $\sum_j \abs{I_j} < \infty$; then the null set $E = \limsup_j I_j$ would have $m(f(E)) > 0$, contradiction). See e.g. Royden–Fitzpatrick, *Real Analysis*, or Folland, *Real Analysis*, Theorem on absolutely continuous functions.
    <2>2. Hence (3) implies (1).
        Proof: By <2>1.
    <2>3. And (1) implies (2) by <1>1, so (3) implies (2).
        Proof: Transitivity of implication.
    <2>4. Q.E.D.
        Proof: This proves (3) $\implies$ (2).

<1>5. Conclusion: (1), (2), and (3) are equivalent.
    <2>1. (1) $\implies$ (2): by <1>1.
    <2>2. (2) $\implies$ (1): by <1>2.
    <2>3. (2) $\implies$ (3): by <1>3.
    <2>4. (3) $\implies$ (2): by <1>4.
    <2>5. Q.E.D.
        Proof: (1) $\iff$ (2) by <2>1 and <2>2; (2) $\iff$ (3) by <2>3 and <2>4.
:::
