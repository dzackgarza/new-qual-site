---
schema: qual/card@1
id: E-F8UOA
kind: problem
title: Continuity sets are G-delta; no function continuous exactly on the rationals
classification:
  areas:
  - topology
  topics:
  - Baire Spaces
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: {.exercise}

Prove the following.

Theorem.
If $D$ is a countable dense subset of $\mathbb{R}$, there is no function $f: \mathbb{R} \to \mathbb{R}$ that is continuous precisely at the points of $D$.

(a) Show that if $f: \mathbb{R} \to \mathbb{R}$, then the set $C$ of points at which $f$ is continuous is a $G_\delta$ set in $\mathbb{R}$.
[Hint: Let $U_n$ be the union of all open sets $U$ of $\mathbb{R}$ such that $\operatorname{diam} f(U) < 1/n$. Show that $C = \bigcap U_n$.]

(b) Show that $D$ is not a $G_\delta$ set in $\mathbb{R}$.
[Hint: Suppose $D = \bigcap W_n$, where $W_n$ is open in $\mathbb{R}$. For $d \in D$, set $V_d = \mathbb{R} - \ts{d}$. Show $W_n$ and $V_d$ are dense in $\mathbb{R}$.]
:::

::: {.solution}
**Part (a).**

<1>1. For each $n \in \mathbb{Z}_+$, define:
\[
U_n = \bigcup \left\{ U \subseteq \mathbb{R} : U \text{ is open and } \operatorname{diam}(f(U)) < \frac{1}{n} \right\}.
\]
::: {.proof}
definition.
:::

<1>2. Each $U_n$ is open in $\mathbb{R}$.
::: {.proof}
an arbitrary union of open sets in a topological space is open.
:::

<1>3. Prove that $C = \bigcap_{n=1}^\infty U_n$: <2>1. ($\subseteq$) Let $x_0 \in C$, so $f$ is continuous at $x_0$.
::: {.proof}
definition of $C$.
:::
<2>2. For any $n \in \mathbb{Z}_+$, by continuity at $x_0$ there exists an open interval $U \ni x_0$ such that $f(U) \subseteq \left(f(x_0) - \frac{1}{3n}, f(x_0) + \frac{1}{3n}\right)$.
::: {.proof}
$\varepsilon$-$\delta$ definition of continuity with $\varepsilon = \frac{1}{3n}$.
:::
<2>3. $\operatorname{diam}(f(U)) \le \frac{2}{3n} < \frac{1}{n}$, so $x_0 \in U \subseteq U_n$.
::: {.proof}
diameter of an interval of length $2/(3n)$.
:::
<2>4. Since this holds for all $n \in \mathbb{Z}_+$, $x_0 \in \bigcap_{n=1}^\infty U_n$.
::: {.proof}
<2>3 for all $n$.
:::
<2>5. ($\supseteq$) Let $x_0 \in \bigcap_{n=1}^\infty U_n$.
::: {.proof}
setup.
:::
<2>6. For any $\varepsilon > 0$, choose $n \in \mathbb{Z}_+$ such that $\frac{1}{n} < \varepsilon$.
::: {.proof}
Archimedean property of $\mathbb{R}$.
:::
<2>7. Since $x_0 \in U_n$, there exists an open set $U \ni x_0$ such that $\operatorname{diam}(f(U)) < \frac{1}{n} < \varepsilon$.
::: {.proof}
definition of $U_n$ as a union.
:::
<2>8. For all $y \in U$, $|f(y) - f(x_0)| \le \operatorname{diam}(f(U)) < \varepsilon$, so $f$ is continuous at $x_0$.
::: {.proof}
definition of diameter.
:::
<2>9. Thus $x_0 \in C$.
::: {.proof}
<2>8. <2>10. Hence $C = \bigcap_{n=1}^\infty U_n$.
:::
::: {.proof}
<2>4 and <2>9.
:::

<1>4. Since each $U_n$ is open, $C$ is a countable intersection of open sets, hence a $G_\delta$ set in $\mathbb{R}$.
::: {.proof}
<1>2 and <1>3.
:::

**Part (b).**

<1>5. Let $D = \{d_k : k \in \mathbb{Z}_+\}$ be a countable dense subset of $\mathbb{R}$.
::: {.proof}
hypothesis.
:::

<1>6. Assume for contradiction that $D$ is a $G_\delta$ set in $\mathbb{R}$, so $D = \bigcap_{n=1}^\infty W_n$ for open sets $W_n \subseteq \mathbb{R}$.
::: {.proof}
proof by contradiction assumption.
:::

<1>7. Each $W_n$ is dense and open in $\mathbb{R}$: <2>1. $W_n$ is open by assumption.
::: {.proof}
<1>6. <2>2. $D \subseteq W_n$ and $D$ is dense in $\mathbb{R}$, so $W_n$ is dense in $\mathbb{R}$.
:::
::: {.proof}
a superset of a dense set is dense.
:::

<1>8. For each $k \in \mathbb{Z}_+$, define $V_k = \mathbb{R} \setminus \{d_k\}$: <2>1. $\{d_k\}$ is a closed singleton in the Hausdorff space $\mathbb{R}$, so $V_k$ is open.
::: {.proof}
complement of a closed set.
:::
<2>2. The singleton $\{d_k\}$ has empty interior, so $V_k$ is dense in $\mathbb{R}$.
::: {.proof}
$\mathbb{R}$ has no isolated points.
:::

<1>9. The countable family $\{W_n\}_{n=1}^\infty \cup \{V_k\}_{k=1}^\infty$ is a collection of dense open subsets of the complete metric space $\mathbb{R}$.
::: {.proof}
<1>7 and <1>8.
:::

<1>10. By the Baire Category Theorem, the intersection $\left(\bigcap_{n=1}^\infty W_n\right) \cap \left(\bigcap_{k=1}^\infty V_k\right)$ must be dense in $\mathbb{R}$, and in particular non-empty.
::: {.proof}
Baire Category Theorem for complete metric spaces.
:::

<1>11. Compute the intersection directly:
\[
\left(\bigcap_{n=1}^\infty W_n\right) \cap \left(\bigcap_{k=1}^\infty V_k\right) = D \cap \left(\mathbb{R} \setminus \bigcup_{k=1}^\infty \{d_k\}\right) = D \cap (\mathbb{R} \setminus D) = \emptyset.
\]
::: {.proof}
$\bigcap V_k = \mathbb{R} \setminus \bigcup \{d_k\} = \mathbb{R} \setminus D$.
:::

<1>12. The empty set $\emptyset$ is not dense, contradicting <1>10.
::: {.proof}
$\emptyset \neq \mathbb{R}$.
:::

<1>13. Therefore $D$ is not a $G_\delta$ set in $\mathbb{R}$.
::: {.proof}
<1>6 and <1>12.
:::

**Theorem.**

<1>14. There is no function $f: \mathbb{R} \to \mathbb{R}$ whose set of continuity points is precisely $D$.
<2>1. If such an $f$ existed, its continuity set $C = D$ would be a $G_\delta$ set by Part (a).
::: {.proof}
<1>4. <2>2. By Part (b), $D$ is not a $G_\delta$ set, a contradiction.
:::
::: {.proof}
<1>13. <2>3. Thus no such function $f$ exists.
:::
::: {.proof}
<2>1 and <2>2.
:::

<1>15. Q.E.D.
::: {.proof}
<1>4, <1>13, and <1>14.
:::
:::
