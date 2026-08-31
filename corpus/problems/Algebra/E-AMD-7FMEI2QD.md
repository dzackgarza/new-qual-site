---
schema: qual/card@1
id: E-AMD-7FMEI2QD
kind: exercise
title: A ring is local iff $x$ or $1-x$ is a unit for every $x$
classification:
  areas:
  - algebra
  topics:
  - Local Rings
  - Maximal Ideals
  - Rings
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-16
---

::: {.exercise}
Show that $R$ is a local ring iff for every $x\in R$, either $x$ or $1-x$ is a unit.
:::

::: {.solution}
**Goal:** Let $R$ be a commutative ring with identity $1 \neq 0$.
Prove that $R$ is a local ring (i.e., has a unique maximal ideal) if and only if for every $x \in R$, either $x \in R^\times$ or $1 - x \in R^\times$.

<1>1. Definition and standard characterization of a local ring: <2>1. Definition: A commutative ring $R$ is local if it has exactly one maximal ideal $\mathfrak{m}$.
::: {.proof}
Standard definition.
:::
<2>2. Characterization lemma: A commutative ring $R$ is local if and only if the set of non-units $R \setminus R^\times$ forms an ideal of $R$.
<3>1. Direction $\implies$: If $R$ is local with unique maximal ideal $\mathfrak{m}$, then $R \setminus R^\times = \mathfrak{m}$, which is an ideal.
::: {.proof}
Every proper ideal is contained in a maximal ideal (by Krull's Theorem / Zorn's Lemma).
:::
If $x \notin R^\times$, the principal ideal $(x)$ is proper, so $(x) \subseteq \mathfrak{m}$, implying $x \in \mathfrak{m}$.
Conversely, $\mathfrak{m} \subsetneq R$ contains no units, so $\mathfrak{m} \subseteq R \setminus R^\times$.
Thus $R \setminus R^\times = \mathfrak{m}$.
<3>2. Direction $\impliedby$: If $I = R \setminus R^\times$ is an ideal, then $I$ is the unique maximal ideal of $R$.
::: {.proof}
Any proper ideal $J \subsetneq R$ contains no units, so $J \subseteq R \setminus R^\times = I$.
:::
Thus $I$ contains every proper ideal, making $I$ the unique maximal ideal.
<3>3. Q.E.D.
::: {.proof}
Follows from <3>1 and <3>2.
:::

<1>2. Direction 1 ($\implies$): If $R$ is a local ring, then for every $x \in R$, either $x \in R^\times$ or $1 - x \in R^\times$.
<2>1. Assume $R$ is a local ring with unique maximal ideal $\mathfrak{m}$.
::: {.proof}
Hypothesis.
:::
<2>2. Let $x \in R$.
Suppose for contradiction that $x \notin R^\times$ and $1 - x \notin R^\times$.
::: {.proof}
Assumption for contrapositive/contradiction.
:::
<2>3. Since $R \setminus R^\times = \mathfrak{m}$ by <1>1.<2>1, $x \in \mathfrak{m}$ and $1 - x \in \mathfrak{m}$.
::: {.proof}
Non-units in a local ring belong to the unique maximal ideal $\mathfrak{m}$.
:::
<2>4. Since $\mathfrak{m}$ is an ideal, it is closed under addition, so $1 = x + (1 - x) \in \mathfrak{m}$.
::: {.proof}
Closure of ideals under addition.
:::
<2>5. Contradiction: A maximal ideal is proper, so $1 \notin \mathfrak{m}$.
::: {.proof}
If $1 \in \mathfrak{m}$, then $\mathfrak{m} = R$, contradicting that maximal ideals are proper.
:::
<2>6. Therefore, at least one of $x$ or $1 - x$ is a unit in $R$.
::: {.proof}
The assumption that neither is a unit led to the contradiction $1 \in \mathfrak{m}$.
:::
<2>7. Q.E.D.
::: {.proof}
Follows from <2>1 through <2>6.
:::

<1>3. Direction 2 ($\impliedby$): If for every $x \in R$, either $x \in R^\times$ or $1 - x \in R^\times$, then $R$ is a local ring.
<2>1. Assume that for every $x \in R$, either $x \in R^\times$ or $1 - x \in R^\times$.
::: {.proof}
Hypothesis.
:::
<2>2. Let $N = R \setminus R^\times$ be the set of all non-units of $R$.
We will show that $N$ is an ideal of $R$.
::: {.proof}
Strategy using the characterization lemma <1>1.<2>2. <2>3. $0 \in N$ and $N \neq \emptyset$.
:::
::: {.proof}
$1 \neq 0$ implies $0$ is not a unit, so $0 \in N$.
:::
<2>4. For any $a \in N$ and $r \in R$, $r a \in N$.
::: {.proof}
If $r a \in R^\times$, there exists $u \in R$ such that $(r a) u = 1$, which gives $a(r u) = 1$, implying $a \in R^\times$, a contradiction to $a \in N$.
:::
<2>5. For any $a, b \in N$, $a + b \in N$.
<3>1. Suppose for contradiction that $a, b \in N$ but $u = a + b \in R^\times$.
::: {.proof}
Assumption for contradiction.
:::
<3>2. Since $u \in R^\times$, $1 = u^{-1}(a + b) = u^{-1}a + u^{-1}b$.
::: {.proof}
Multiplying by $u^{-1}$.
:::
<3>3. Set $y = u^{-1}a$.
Then $1 - y = u^{-1}b$.
::: {.proof}
Algebraic rearrangement.
:::
<3>4. By hypothesis, either $y \in R^\times$ or $1 - y \in R^\times$.
::: {.proof}
Applying the problem hypothesis to $y \in R$.
:::
<3>5. If $y = u^{-1}a \in R^\times$, then $a = u \cdot (u^{-1}a)$ is the product of two units, so $a \in R^\times$, contradicting $a \in N$.
::: {.proof}
Units form a group under multiplication.
:::
<3>6. If $1 - y = u^{-1}b \in R^\times$, then $b = u \cdot (u^{-1}b)$ is the product of two units, so $b \in R^\times$, contradicting $b \in N$.
::: {.proof}
Units form a group under multiplication.
:::
<3>7. In either case, we reach a contradiction.
Thus $a + b \in N$.
::: {.proof}
By <3>4, <3>5, and <3>6. <2>6. By <2>3, <2>4, and <2>5, $N = R \setminus R^\times$ is an ideal of $R$.
:::
::: {.proof}
$N$ is closed under addition, absorption of ring elements, and contains $0$.
:::
<2>7. By <1>1.<2>2, $R$ is a local ring with unique maximal ideal $N$.
::: {.proof}
Since $R \setminus R^\times$ is an ideal.
:::
<2>8. Q.E.D.
::: {.proof}
Follows from <2>1 through <2>7.
:::

<1>4. Conclusion: $R$ is a local ring if and only if for every $x \in R$, either $x$ or $1 - x$ is a unit.
::: {.proof}
By <1>2 and <1>3.
:::
:::
