---
schema: qual/card@1
id: E-LYXHE
kind: exercise
title: "If $f, g$ are compactly supported, is it necessarily the case that\u2026"
classification:
  areas:
  - real-analysis
  topics:
  - convolution
  - l1
relations: []
review: draft
solved: true
---

::: exercise
- If $f, g$ are compactly supported, is it necessarily the case that $f\ast g$ is compactly supported?

- Show that under any of the following assumptions, $f\ast g$ vanishes at infinity:

  - $f, g\in L^1$ are both bounded.

  - $f, g\in L^1$ with just $g$ bounded.

  - $f, g$ smooth and compactly supported (and in fact $f\ast g$ is smooth)
:::

::: {.solution}
> **AI-Generated Solution**

<1>1. Yes: if $f$ and $g$ are compactly supported, then $f \ast g$ is compactly supported.
<2>1. $\supp(f \ast g) \subseteq \overline{\supp f + \supp g}$.
Proof: if $x \notin \overline{\supp f + \supp g}$, then $(x - \supp g) \cap \supp f = \emptyset$, so $f(x-y) = 0$ for every $y \in \supp g$ and $f \ast g(x) = \int f(x-y)g(y)\,dy = 0$.
<2>2. $\overline{\supp f + \supp g}$ is compact.
Proof: $\supp f \times \supp g$ is compact and $(a,b) \mapsto a+b$ is continuous, so $\supp f + \supp g$ is compact (its image), hence closed and bounded; $\overline{\supp f + \supp g} = \supp f + \supp g$ is compact.
<2>3. Q.E.D. Proof: <2>1 and <2>2.

<1>2. If $f, g \in L^1$ are both bounded, then $f \ast g$ vanishes at infinity.
<2>1. Fix $x$ and split $f \ast g(x) = \int_{|y| \le |x|/2} f(x-y)g(y)\,dy + \int_{|y| > |x|/2} f(x-y)g(y)\,dy$.
Proof: additivity of the integral.
<2>2. The first term is at most $\|g\|_\infty \int_{|z| \ge |x|/2} |f(z)|\,dz$, which tends to $0$ as $|x| \to \infty$.
Proof: on $\{|y| \le |x|/2\}$ one has $|x-y| \ge |x|/2$; substituting $z = x - y$ and using $|g| \le \|g\|_\infty$ gives the bound, and the $L^1$ tail integral tends to $0$ by dominated convergence.
<2>3. The second term is at most $\|f\|_\infty \int_{|y| > |x|/2} |g(y)|\,dy$, which tends to $0$ as $|x| \to \infty$.
Proof: $|f| \le \|f\|_\infty$ since $f$ is bounded; the $L^1$ tail of $g$ tends to $0$.
<2>4. Q.E.D. Proof: <2>2 and <2>3 show $|f \ast g(x)| \to 0$ as $|x| \to \infty$.

<1>3. If $f, g \in L^1$ with only $g$ bounded, then $f \ast g$ vanishes at infinity.
<2>1. For each $M > 0$ write $f = f_M + r_M$, where $f_M = f \chi_{\{|f| \le M\}}$ is bounded and $\|r_M\|_1 \to 0$ as $M \to \infty$.
Proof: $|f_M| \le M$ pointwise, and $\int |r_M| = \int_{|f| > M} |f| \to 0$ by dominated convergence since $|f| \in L^1$ and $\chi_{|f| > M} \to 0$ pointwise.
<2>2. $\|r_M \ast g\|_\infty \le \|r_M\|_1 \|g\|_\infty \to 0$.
Proof: $|r_M \ast g(x)| \le \int |r_M(x-y)||g(y)|\,dy \le \|g\|_\infty \|r_M\|_1$.
<2>3. $f_M \ast g$ vanishes at infinity.
Proof: $f_M$ and $g$ are both bounded and in $L^1$, so <1>2 applies.
<2>4. Q.E.D. Proof: given $\eps > 0$, choose $M$ with $\|r_M \ast g\|_\infty < \eps/2$ by <2>2, then $|x|$ large with $|f_M \ast g(x)| < \eps/2$ by <2>3; then $|f \ast g(x)| \le |f_M \ast g(x)| + |r_M \ast g(x)| < \eps$.

<1>4. If $f, g$ are smooth and compactly supported, then $f \ast g$ is smooth and vanishes at infinity.
<2>1. $f \ast g$ is $C^\infty$, with $D^\alpha(f \ast g) = (D^\alpha f) \ast g$ for every multi-index $\alpha$.
Proof: $(D^\alpha f) \ast g$ is well defined and continuous, and differentiation under the integral is justified because $D^\alpha f$ is bounded (continuous and compactly supported) while $g$ is integrable.
<2>2. $f \ast g$ is compactly supported.
Proof: <1>1 applies since both $f$ and $g$ are compactly supported.
<2>3. $f \ast g$ vanishes at infinity.
Proof: by <2>2, $f \ast g$ is identically zero outside a bounded set.
<2>4. Q.E.D. Proof: <2>1–<2>3.

<1>5. Q.E.D. Proof: <1>1 answers the first question; <1>2, <1>3, and <1>4 establish vanishing at infinity under the three listed assumptions.
:::
