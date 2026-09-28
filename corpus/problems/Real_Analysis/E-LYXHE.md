---
schema: qual/card@1
id: E-LYXHE
kind: problem
title: Compact support and vanishing at infinity of convolutions
classification:
  areas:
  - real-analysis
  topics:
  - Convolution
  - L¹
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-17
---

::: {.exercise}
- If $f, g$ are compactly supported, is it necessarily the case that $f\ast g$ is compactly supported?

- Show that under any of the following assumptions, $f\ast g$ vanishes at infinity:

  - $f, g\in L^1$ are both bounded.

  - $f, g\in L^1$ with just $g$ bounded.

  - $f, g$ smooth and compactly supported (and in fact $f\ast g$ is smooth)
:::

::: {.solution}
<1>1. If $f$ and $g$ are compactly supported, then $f \ast g$ is compactly supported.

<2>1. $\supp(f \ast g) \subseteq \supp f + \supp g$.

::: {.proof}
If $x \notin \supp f + \supp g$, then $(x - \supp g) \cap \supp f = \emptyset$, so $f(x-y) = 0$ for every $y \in \supp g$ and $f \ast g(x) = \int f(x-y)g(y)\,dy = 0$. Since $\supp f + \supp g$ is closed by step <2>2, the support of $f\ast g$, the closure of $\theset{f\ast g \neq 0}$, is contained in it.
:::

<2>2. $\supp f + \supp g$ is compact.

::: {.proof}
It is the image of the compact set $\supp f \times \supp g$ under the continuous map $(a,b) \mapsto a+b$.
:::

<2>3. Q.E.D.

::: {.proof}
A closed subset of a compact set is compact; apply steps <2>1 and <2>2.
:::

<1>2. If $f, g \in L^1$ are both bounded, then $f \ast g$ vanishes at infinity.

<2>1. $\abs{\int_{|y| \le |x|/2} f(x-y)g(y)\,dy} \leq \|g\|_\infty \int_{|z| \ge |x|/2} |f(z)|\,dz$, which tends to $0$ as $|x| \to \infty$.

::: {.proof}
On $\theset{|y| \le |x|/2}$, $|x-y| \ge |x|/2$. Substitute $z = x - y$ and use $|g| \le \|g\|_\infty$. The tail integral of $|f| \in L^1$ tends to $0$ by dominated convergence.
:::

<2>2. $\abs{\int_{|y| > |x|/2} f(x-y)g(y)\,dy} \leq \|f\|_\infty \int_{|y| > |x|/2} |g(y)|\,dy$, which tends to $0$ as $|x| \to \infty$.

::: {.proof}
Use $|f| \le \|f\|_\infty$; the tail integral of $|g| \in L^1$ tends to $0$.
:::

<2>3. Q.E.D.

::: {.proof}
$f\ast g(x)$ is the sum of the two integrals in steps <2>1 and <2>2, and both tend to $0$ as $|x| \to \infty$.
:::

<1>3. If $f, g \in L^1$ with only $g$ bounded, then $f \ast g$ vanishes at infinity.

<2>1. For $M > 0$ write $f = f_M + r_M$ with $f_M = f \chi_{\theset{|f| \le M}}$. Then $|f_M| \le M$ and $\|r_M\|_1 \to 0$ as $M \to \infty$.

::: {.proof}
$\int |r_M| = \int_{\theset{|f| > M}} |f| \to 0$ by dominated convergence, since $|f| \in L^1$ and $\chi_{\theset{|f| > M}} \to 0$ a.e.
:::

<2>2. $\|r_M \ast g\|_\infty \le \|r_M\|_1 \|g\|_\infty$.

::: {.proof}
$|r_M \ast g(x)| \le \int |r_M(x-y)||g(y)|\,dy \le \|g\|_\infty \|r_M\|_1$.
:::

<2>3. $f_M \ast g$ vanishes at infinity.

::: {.proof}
$f_M$ and $g$ are bounded and in $L^1$, so step <1>2 applies.
:::

<2>4. Q.E.D.

::: {.proof}
Given $\eps > 0$, choose $M$ with $\|r_M \ast g\|_\infty < \eps/2$ by steps <2>1 and <2>2, then $R$ with $|f_M \ast g(x)| < \eps/2$ for $|x| > R$ by step <2>3. For $|x| > R$, $|f \ast g(x)| \le |f_M \ast g(x)| + |r_M \ast g(x)| < \eps$.
:::

<1>4. If $f, g$ are smooth and compactly supported, then $f \ast g$ is smooth and vanishes at infinity.

<2>1. $f \ast g$ is $C^\infty$, with $D^\alpha(f \ast g) = (D^\alpha f) \ast g$ for every multi-index $\alpha$.

::: {.proof}
Each $D^\alpha f$ is continuous and compactly supported, hence bounded, and $g$ is integrable, so dominated convergence justifies differentiating under the integral in $f\ast g(x) = \int f(x-y)g(y)\,dy$. Each $(D^\alpha f) \ast g$ is continuous.
:::

<2>2. $f \ast g$ vanishes at infinity.

::: {.proof}
By step <1>1, $f \ast g$ is zero outside a compact set.
:::

<2>3. Q.E.D.

::: {.proof}
Steps <2>1 and <2>2.
:::

<1>5. Q.E.D.

::: {.proof}
Step <1>1 answers the first question affirmatively; steps <1>2, <1>3, and <1>4 prove vanishing at infinity under the three listed assumptions.
:::
:::
