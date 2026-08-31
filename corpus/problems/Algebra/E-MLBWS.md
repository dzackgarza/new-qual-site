---
schema: qual/card@1
id: E-MLBWS
kind: problem
title: Finite extension with infinitely many intermediate fields
classification:
  areas:
  - algebra
  topics:
  - Field Extensions
  - Counterexamples
  - Separability
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: problem
Give an example of a finite extension of fields that has infinitely many intermediate fields.
:::

::: {.solution}
<1>1. Define the base field and extension: Let $p$ be a prime.
Let $k = \mathbb{F}_p(u, v)$ be the rational function field in two indeterminates $u, v$ over $\mathbb{F}_p$, and let $K = \mathbb{F}_p(u^p, v^p) \subset k$.
::: {.proof}
definition of the fields.
:::

<1>2. The extension $k/K$ is finite of degree $p^2$.
<2>1. $u^p \in K$ and $v^p \in K$, so $u$ and $v$ satisfy $X^p - u^p = 0$ and $X^p - v^p = 0$ over $K$.
::: {.proof}
definition of $K$.
:::
<2>2. The set $\{u^i v^j : 0 \le i \le p-1,\ 0 \le j \le p-1\}$ forms a basis for $k$ over $K$.
::: {.proof}
$u$ and $v$ are algebraically independent over $\mathbb{F}_p$, so $[K(u):K] = p$ with basis $\{1, u, \dots, u^{p-1}\}$ and $[K(u,v):K(u)] = p$ with basis $\{1, v, \dots, v^{p-1}\}$.
:::
<2>3. Thus $[k : K] = [k : K(u)][K(u) : K] = p \cdot p = p^2 < \infty$.
::: {.proof}
tower law for field extension degrees.
:::

<1>3. For each $c \in K$, define the intermediate field $E_c = K(u + c v)$.
<2>1. By the Frobenius endomorphism in characteristic $p$, $(u + c v)^p = u^p + c^p v^p \in K$.
::: {.proof}
$(a + b)^p = a^p + b^p$ in characteristic $p$, and $u^p, v^p, c^p \in K$.
:::
<2>2. Since $u + cv \notin K$ (as $\{1, u, v\}$ are linearly independent over $K$), the minimal polynomial of $u + cv$ over $K$ is $X^p - (u^p + c^p v^p)$, which has degree $p$.
::: {.proof}
$[E_c : K]$ divides $[k : K] = p^2$ and is strictly greater than 1, while $(u+cv)^p \in K$, so $[E_c : K] = p$.
:::

<1>4. For distinct $c_1, c_2 \in K$ with $c_1 \neq c_2$, the fields $E_{c_1}$ and $E_{c_2}$ are distinct.
<2>1. Suppose $E_{c_1} = E_{c_2}$.
::: {.proof}
hypothesis for contradiction.
:::
<2>2. Then $u + c_1 v \in E_{c_1}$ and $u + c_2 v \in E_{c_1}$.
::: {.proof}
definition of $E_{c_1}$ and assumption $E_{c_2} \subseteq E_{c_1}$.
:::
<2>3. Subtracting gives $(c_1 - c_2) v \in E_{c_1}$.
Since $c_1 - c_2 \in K^\times$, $v = (c_1 - c_2)^{-1}(c_1 - c_2)v \in E_{c_1}$.
::: {.proof}
$E_{c_1}$ is a field containing $K$.
:::
<2>4. Then $u = (u + c_1 v) - c_1 v \in E_{c_1}$.
::: {.proof}
<2>2 and <2>3. <2>5. Thus $k = K(u, v) \subseteq E_{c_1}$, which implies $[E_{c_1} : K] = [k : K] = p^2$.
:::
::: {.proof}
<2>3 and <2>4. <2>6. This contradicts $[E_{c_1} : K] = p$ established in <1>3.
::: {.proof}
$p < p^2$ for any prime $p$.
:::
:::
<2>7. Hence $E_{c_1} \neq E_{c_2}$ whenever $c_1 \neq c_2$.
::: {.proof}
<2>1–<2>6.
:::

<1>5. Since $K = \mathbb{F}_p(u^p, v^p)$ is an infinite field, the family $\{E_c : c \in K\}$ contains infinitely many distinct intermediate fields between $K$ and $k$.
::: {.proof}
the set of powers $\{u^{pn} : n \ge 1\} \subset K$ provides infinitely many distinct choices of $c \in K$.
:::

<1>6. Conclusion: $k/K = \mathbb{F}_p(u, v) / \mathbb{F}_p(u^p, v^p)$ is a finite field extension of degree $p^2$ with infinitely many distinct intermediate fields.
::: {.proof}
<1>2 and <1>5.
:::
Q.E.D.
:::
