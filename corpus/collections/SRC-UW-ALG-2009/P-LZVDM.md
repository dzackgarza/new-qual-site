---
schema: qual/card@1
id: P-LZVDM
kind: problem
title: The valuation ring of a discrete valuation, and the $p$-adic valuation on $\QQ$
classification:
  areas:
  - algebra
  topics:
  - Valuation Rings
  - Discrete Valuation Rings
  - Commutative Algebra
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
---

::: {.problem}
Let $K$ be a field.
A discrete valuation on $K$ is a function $\nu: K\setminus\{0\}\rightarrow\ZZ$ such that

(i) $\nu(ab)=\nu(a)+\nu(b)$

(ii) $\nu$ is surjective

(iii) $\nu(a+b)\geq\min\{\nu(a),\nu(b)\}$ for all $a,b\in K\setminus\{0\}$ with $a+b\neq 0$.

Let $R\coloneqq\{x\in K\setminus\{0\}:\nu(x)\geq0\}\cup\{0\}$.
Then $R$ is called the valuation ring of $\nu$.

Prove the following:

(a) $R$ is a subring of $K$ containing the 1 in $K$.

(b) for all $x\in K\setminus\{0\}$, either $x$ or $\inverseof{x}$ is in $R$.

(c) $x$ is a unit of $R$ if and only if $\nu(x)=0$.

(d) Let $p$ be a prime number, $K=\QQ$ and $\nu_p:\QQ\setminus\{0\}\rightarrow\ZZ$ be the function defined by $\nu_p(\frac ab)=n$ where $\frac ab=p^n\frac cd$ and $p$ does not divide $c$ and $d$.
Prove that the corresponding valuation ring $R$ is the ring of all rational numbers whose denominators are relatively prime to $p$.
:::

::: {.solution}
**Goal:** Prove the foundational properties of the valuation ring $R$ associated with a discrete valuation $\nu$ on a field $K$, and determine the valuation ring of the $p$-adic valuation $\nu_p$ on $\QQ$.

::: pf

::: {.pf-step #s1}
We have $\nu(1)=0$; $\nu(-1)=0$ and $\nu(-x)=\nu(x)$ for all $x\in K^\times$; and $\nu(x^{-1})=-\nu(x)$ for all $x\in K^\times$.

::: pf-proof

::: pf-step
In $K$, $1 \cdot 1 = 1 \implies \nu(1) = \nu(1 \cdot 1) = \nu(1) + \nu(1)$.
Subtracting $\nu(1) \in \ZZ$ gives $\nu(1) = 0$.

:::

::: pf-step
$(-1)^2 = 1 \implies 2\nu(-1) = \nu(1) = 0 \implies \nu(-1) = 0$.
For any $x \in K^\times$, $\nu(-x) = \nu(-1 \cdot x) = \nu(-1) + \nu(x) = \nu(x)$.

:::

::: pf-step
For $x \in K^\times$, $x \cdot x^{-1} = 1 \implies \nu(x) + \nu(x^{-1}) = \nu(1) = 0 \implies \nu(x^{-1}) = -\nu(x)$.

:::

:::

:::

::: pf-step
$R$ is a subring of $K$ containing $1$:

::: pf-proof

::: pf-step
By step [](#s1){.pf-ref}, $\nu(1) = 0 \ge 0$, so $1 \in R$.
Also $0 \in R$ by definition.

:::

::: pf-step
Let $x, y \in R$.
If $x = 0$ or $y = 0$, then $xy = 0 \in R$.
If $x, y \neq 0$, then $\nu(x) \ge 0$ and $\nu(y) \ge 0$, so $\nu(xy) = \nu(x) + \nu(y) \ge 0 + 0 = 0$, hence $xy \in R$.

:::

::: pf-step
Let $x, y \in R$.
If $x - y = 0$, then $x - y \in R$.
If $x - y \neq 0$: if $x = 0$, $\nu(x - y) = \nu(-y) = \nu(y) \ge 0$; if $y = 0$, $\nu(x - y) = \nu(x) \ge 0$; if $x, y \neq 0$, $\nu(x - y) = \nu(x + (-y)) \ge \min\{\nu(x), \nu(-y)\} = \min\{\nu(x), \nu(y)\} \ge 0$.
In all cases $x - y \in R$.

:::

::: pf-step
By the subring criterion, $R$ is a subring of $K$ containing $1$.

:::

:::

:::

::: pf-step
For all $x \in K^\times$, either $x \in R$ or $x^{-1} \in R$:

::: pf-proof
Let $x \in K^\times$.
Since $\nu(x) \in \ZZ$, either $\nu(x) \ge 0$ or $\nu(x) < 0$.
If $\nu(x) \ge 0$, then $x \in R$.
If $\nu(x) < 0$, then $\nu(x^{-1}) = -\nu(x) > 0 \ge 0$ by step [](#s1){.pf-ref}, so $x^{-1} \in R$.
:::

:::

::: pf-step
$x \in R$ is a unit of $R$ if and only if $\nu(x) = 0$:

::: pf-proof

::: pf-step
$x$ is a unit of $R \iff x \in R$ and $x^{-1} \in R$.

:::

::: pf-step
$x \in R$ and $x^{-1} \in R \iff \nu(x) \ge 0$ and $\nu(x^{-1}) \ge 0$.

:::

::: pf-step
By step [](#s1){.pf-ref}, $\nu(x^{-1}) = -\nu(x)$, so $\nu(x) \ge 0$ and $-\nu(x) \ge 0 \iff \nu(x) = 0$.

:::

::: pf-step
Thus $R^\times = \{x \in K^\times : \nu(x) = 0\}$.

:::

:::

:::

::: pf-step
For $K = \QQ$ and $\nu_p$, the valuation ring is $R = \{\frac{a}{b} \in \QQ : \gcd(a, b) = 1, p \nmid b\}$:

::: pf-proof

::: pf-step
Any nonzero rational $x \in \QQ^\times$ can be written uniquely in lowest terms as $x = \frac{u}{v}$ where $u, v \in \ZZ$, $v > 0$, and $\gcd(u, v) = 1$.

:::

::: pf-step
Factoring prime powers of $p$ from $u$ and $v$, write $u = p^k c$ and $v = p^m d$ with $k, m \ge 0$ and $p \nmid c$, $p \nmid d$.
Since $\gcd(u, v) = 1$, at least one of $k, m$ is $0$.

:::

::: pf-step
Then $x = p^{k-m} \frac{c}{d}$, so by definition $\nu_p(x) = k - m$.

:::

::: pf-step
$x \in R \iff \nu_p(x) \ge 0 \iff k - m \ge 0$.

:::

::: pf-step
Since at least one of $k, m$ is $0$, $k - m \ge 0 \iff m = 0 \iff p \nmid v$.

:::

::: pf-step
For $x = 0$, $0 = \frac{0}{1}$ and $p \nmid 1$, which also satisfies the condition.

:::

::: pf-qed
Thus $R = \{\frac{u}{v} \in \QQ : \gcd(u, v) = 1, p \nmid v\}$, which is the ring of rational numbers whose denominators (in lowest terms) are relatively prime to $p$ (i.e., the localization $\ZZ_{(p)}$).
:::

:::

:::

:::

:::
