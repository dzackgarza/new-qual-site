---
schema: qual/card@1
id: P-XLANN
kind: problem
title: $\norm{g}_p\to\norm{g}_\infty$ as $p\to\infty$ on $[0,1]$, and $\norm{\Lambda_g}_{(L^1)^*}=\norm{g}_\infty$
classification:
  areas:
  - real-analysis
  topics:
  - Dual Spaces
  - L∞
  - Lp Spaces
  - Riesz Representation
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-17
- event: solution-written
  by: claude
  date: 2026-11-19
  note: >-
    Every step now carries a pf-proof: the five containers state why their subclaims suffice, and the 20
    leaf steps that asserted a claim with no justification each carry a sentence deriving it. The
    mathematics is unchanged: the almost-everywhere bound by the essential supremum, monotonicity of the
    integral for the upper bound, the zero case, the superlevel set of positive measure, the lower bound
    M m(E_M)^{1/p}, linearity and the estimate for the operator norm, the unimodular test function on a
    level set, and the two suprema over M. No published solution is cited on this card, so the argument
    is the card's own; it was checked against the statements on the card only, and no retained set was
    consulted for it.
---

::: {.problem}

Let $g \in L^\infty([0, 1])$.

(a) Prove that
$$
\lim_{p \to \infty} \norm{g}_{L^p([0, 1])} = \norm{g}_{L^\infty([0, 1])}.
$$

(b) Prove that the map
$$
\Lambda_g: L^1([0, 1]) \to \CC, \qquad f \mapsto \int_0^1 f(x) g(x) \, dx
$$
defines a continuous linear functional in $(L^1([0, 1]))^*$ with $\norm{\Lambda_g}_{(L^1)^*} = \norm{g}_{L^\infty([0, 1])}$.

:::

::: {.solution}

::: pf

::: {.pf-step #s1}

(a) Upper bound: $\limsup_{p \to \infty} \norm{g}_{L^p} \le \norm{g}_{L^\infty}$.

::: pf-proof

The subclaims bound every $\norm{g}_{L^p}$ by $\norm{g}_{L^\infty}$ and then pass to the limit superior.

::: pf-step

For almost every $x \in [0, 1]$, $\abs{g(x)} \le \norm{g}_{L^\infty}$.

::: pf-proof
Let $c_k\downarrow\norm{g}_{L^\infty}$ be essential bounds for $\abs{g}$, which exist by the definition of the essential supremum as an infimum. The set $\{\abs{g}>\norm{g}_{L^\infty}\}$ is the union over $k$ of the null sets $\{\abs{g}>c_k\}$, hence null.
:::

:::

::: pf-step

Integrating over $[0, 1]$ for any $p \ge 1$:
$$\norm{g}_{L^p} = \left( \int_0^1 \abs{g(x)}^p \, dx \right)^{1/p} \le \left( \int_0^1 \norm{g}_{L^\infty}^p \, dx \right)^{1/p} = \norm{g}_{L^\infty} (m([0, 1]))^{1/p} = \norm{g}_{L^\infty} (1)^{1/p} = \norm{g}_{L^\infty}.$$

::: pf-proof
The inequality is monotonicity of the integral applied to the almost-everywhere bound of the preceding subclaim, raised to the power $p$; the remaining equalities use $m([0,1])=1$ and $(1)^{1/p}=1$.
:::

:::

::: pf-step

Taking the limit superior as $p \to \infty$:
$$\limsup_{p \to \infty} \norm{g}_{L^p} \le \norm{g}_{L^\infty}.$$

::: pf-proof
A sequence whose terms are all at most a fixed constant has limit superior at most that constant.
:::

:::

:::

:::

::: {.pf-step #s2}

(a) Lower bound: $\liminf_{p \to \infty} \norm{g}_{L^p} \ge \norm{g}_{L^\infty}$.

::: pf-proof

The first subclaim removes the case $g=0$ almost everywhere; in the remaining case the mass of $\abs{g}$ on a superlevel set of positive measure forces $\norm{g}_{L^p}$ above every $M<\norm{g}_{L^\infty}$.

::: pf-step

If $\norm{g}_{L^\infty} = 0$, then $g = 0$ almost everywhere, so $\norm{g}_{L^p} = 0$ for all $p$ and the limit is $0$.

::: pf-proof
$\abs{g}\le0$ almost everywhere, so $\int\abs{g}^p=0$ for every $p\ge1$ and hence $\norm{g}_{L^p}=0$; a sequence that is identically zero has limit $0$.
:::

:::

::: pf-step

Assume $\norm{g}_{L^\infty} > 0$. For any $0 < M < \norm{g}_{L^\infty}$, define the superlevel set $E_M = \{x \in [0, 1] : \abs{g(x)} > M\}$.

::: pf-proof
This is a definition; $E_M$ is measurable because $g$ is measurable and $(M,\infty)$ is open.
:::

:::

::: pf-step

By definition of the essential supremum, $m(E_M) > 0$.

::: pf-proof
If $m(E_M)=0$ then $\abs{g}\le M$ almost everywhere, so $M$ would be an essential bound strictly smaller than the essential supremum, which is impossible.
:::

:::

::: pf-step

Restricting the $L^p$ integral to $E_M$:
$$\norm{g}_{L^p} = \left( \int_0^1 \abs{g(x)}^p \, dx \right)^{1/p} \ge \left( \int_{E_M} \abs{g(x)}^p \, dx \right)^{1/p} \ge \left( \int_{E_M} M^p \, dx \right)^{1/p} = M (m(E_M))^{1/p}.$$

::: pf-proof
The integrand $\abs{g}^p$ is non-negative, so restricting the domain to $E_M$ can only decrease the integral; on $E_M$ the integrand exceeds $M^p$.
:::

:::

::: pf-step

Since $m(E_M) \in (0, 1]$, $(m(E_M))^{1/p} \to 1$ as $p \to \infty$.

::: pf-proof
For $a\in(0,1]$ one has $a^{1/p}=e^{(\log a)/p}$, and $(\log a)/p\to0$, so the expression tends to $e^0=1$; $m(E_M)\le m([0,1])=1$.
:::

:::

::: pf-step

Thus $\liminf_{p \to \infty} \norm{g}_{L^p} \ge M \lim_{p \to \infty} (m(E_M))^{1/p} = M$.

::: pf-proof
The bound $\norm{g}_{L^p}\ge M(m(E_M))^{1/p}$ holds for every $p\ge1$, so the limit inferior of the left side is at least the limit of the right side, which is $M$ by the preceding subclaim.
:::

:::

::: pf-step

Taking the supremum over all $M < \norm{g}_{L^\infty}$ yields $\liminf_{p \to \infty} \norm{g}_{L^p} \ge \norm{g}_{L^\infty}$.

::: pf-proof
The limit inferior is a fixed extended real number bounded below by every $M<\norm{g}_{L^\infty}$, hence by their supremum $\norm{g}_{L^\infty}$.
:::

:::

:::

:::

::: pf-step

(a) $\lim_{p \to \infty} \norm{g}_{L^p} = \norm{g}_{L^\infty}$.

::: pf-proof

Combining step [](#s1){.pf-ref} and step [](#s2){.pf-ref} gives $\lim_{p \to \infty} \norm{g}_{L^p} = \norm{g}_{L^\infty}$.

:::

:::

::: {.pf-step #s4}

(b) $\Lambda_g$ is linear and $\norm{\Lambda_g} \le \norm{g}_{L^\infty}$.

::: pf-proof

The first subclaim gives linearity and the second the estimate that produces boundedness and the upper bound for the operator norm.

::: pf-step

Linearity of $\Lambda_g$ follows directly from linearity of the Lebesgue integral.

::: pf-proof
For $f,h\in L^1$ and $\alpha,\beta\in\CC$ one has $\int(\alpha f+\beta h)g=\alpha\int fg+\beta\int hg$ by linearity of the integral, and the values lie in $\CC$; this is additivity and homogeneity of $\Lambda_g$.
:::

:::

::: pf-step

For any $f \in L^1([0, 1])$:
$$\abs{\Lambda_g(f)} = \abs{ \int_0^1 f(x) g(x) \, dx } \le \int_0^1 \abs{f(x)} \abs{g(x)} \, dx \le \norm{g}_{L^\infty} \int_0^1 \abs{f(x)} \, dx = \norm{g}_{L^\infty} \norm{f}_{L^1}.$$

::: pf-proof
The first inequality is the triangle inequality for the integral, the second uses $\abs{g}\le\norm{g}_{L^\infty}$ almost everywhere, and the last equality is the definition of the $L^1$ norm.
:::

:::

::: pf-step

Therefore $\Lambda_g$ is a bounded linear functional on $L^1([0, 1])$ with operator norm
$$\norm{\Lambda_g}_{(L^1)^*} = \sup_{f \neq 0} \frac{\abs{\Lambda_g(f)}}{\norm{f}_{L^1}} \le \norm{g}_{L^\infty}.$$

::: pf-proof
The preceding subclaim shows every quotient $\abs{\Lambda_g(f)}/\norm{f}_{L^1}$ with $f\neq0$ is at most $\norm{g}_{L^\infty}$, so the supremum of those quotients is at most $\norm{g}_{L^\infty}$ and is finite; a finite operator norm is exactly boundedness.
:::

:::

:::

:::

::: {.pf-step #s5}

(b) Lower bound: $\norm{\Lambda_g} \ge \norm{g}_{L^\infty}$.

::: pf-proof

The first subclaim removes the case $g=0$; otherwise testing against a unimodular function carried by a level set produces values arbitrarily close to $\norm{g}_{L^\infty}$.

::: pf-step

If $\norm{g}_{L^\infty} = 0$, then $\norm{\Lambda_g} = 0 = \norm{g}_{L^\infty}$.

::: pf-proof
The estimate of the preceding container gives $\abs{\Lambda_g(f)}\le\norm{g}_{L^\infty}\norm{f}_{L^1}=0$ for every $f$, so $\Lambda_g=0$ and its operator norm is $0$.
:::

:::

::: pf-step

Assume $\norm{g}_{L^\infty} > 0$. Fix $0 < M < \norm{g}_{L^\infty}$ and let $E = \{x \in [0, 1] : \abs{g(x)} \ge M\}$, so $m(E) > 0$.

::: pf-proof
$E$ contains $\{\abs{g}>M\}$, which has positive measure because $M$ is not an essential bound; so $m(E)>0$, and $E$ is measurable.
:::

:::

::: pf-step

Define the test function $f \in L^1([0, 1])$ by
$$f(x) = \frac{\overline{\operatorname{sgn}(g(x))}}{m(E)} \mathbf{1}_E(x) = \begin{cases} \frac{\overline{g(x)}}{\abs{g(x)} m(E)} & x \in E \text{ and } g(x) \neq 0, \\ 0 & \text{otherwise.} \end{cases}$$

::: pf-proof
The two formulas agree: on $E$ where $g\neq0$ one has $\overline{\operatorname{sgn}g}=\overline{g}/\abs{g}$, and where $g=0$ both give $0$. The function is measurable, supported in $E$, and bounded by $1/m(E)$.
:::

:::

::: pf-step

Compute the $L^1$ norm of $f$:
$$\norm{f}_{L^1} = \int_E \frac{1}{m(E)} \, dx = \frac{m(E)}{m(E)} = 1.$$

::: pf-proof
On $E$ the modulus of $f$ is $1/m(E)$ by construction, and $m(E)<\infty$ because $E\subseteq[0,1]$.
:::

:::

::: pf-step

Evaluate $\Lambda_g(f)$:
$$\Lambda_g(f) = \int_0^1 f(x) g(x) \, dx = \frac{1}{m(E)} \int_E \frac{\overline{g(x)} g(x)}{\abs{g(x)}} \, dx = \frac{1}{m(E)} \int_E \abs{g(x)} \, dx \ge \frac{1}{m(E)} \int_E M \, dx = M.$$

::: pf-proof
On $E$ with $g\neq0$ the product $f g$ equals $\abs{g}/m(E)$, and the exceptional set is null; the integral is therefore the average of $\abs{g}$ over $E$, which is at least $M$ because $\abs{g}\ge M$ on $E$.
:::

:::

::: pf-step

Since $\norm{f}_{L^1} = 1$, the operator norm satisfies $\norm{\Lambda_g} \ge \abs{\Lambda_g(f)} \ge M$.

::: pf-proof
The operator norm is the supremum of $\abs{\Lambda_g(h)}$ over the unit sphere of $L^1$, and $f$ is a point of that sphere, so the supremum is at least $\abs{\Lambda_g(f)}$, which is at least $M$.
:::

:::

::: pf-step

Since this holds for all $M < \norm{g}_{L^\infty}$, we conclude $\norm{\Lambda_g}_{(L^1)^*} \ge \norm{g}_{L^\infty}$.

::: pf-proof
The operator norm is a fixed number bounded below by every $M<\norm{g}_{L^\infty}$, hence by their supremum.
:::

:::

:::

:::

::: pf-step

(b) $\norm{\Lambda_g}_{(L^1)^*} = \norm{g}_{L^\infty}$.

::: pf-proof

Combining step [](#s4){.pf-ref} and step [](#s5){.pf-ref} yields $\norm{\Lambda_g}_{(L^1)^*} = \norm{g}_{L^\infty}$.

:::

:::

:::

:::
