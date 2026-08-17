---
schema: qual/card@1
id: P-RFJRS
kind: problem
title: $\int_0^1 Fg=F(1)G(1)-\int_0^1 fG$ for $F(x)=\int_0^x f$ and $G(x)=\int_0^x g$ with $f,g\in L^1([0,1])$
classification:
  areas:
  - real-analysis
  topics:
  - integrals
  - fubini-tonelli
relations: []
review: draft
solved: true
---

::: problem
Let $f, g\in L^1([0, 1])$, define $F(x) = \int_0^x f(y)\dy$ and $G(x) = \int_0^x g(y)\dy$, and show
\[
\int_0^1 F(x)g(x) \,dx = F(1)G(1) - \int_0^1 f(x) G(x) \, dx
.\]
:::
::: {.solution}
> **AI-Generated Solution**

<1>1. Write the product of the integrals as a double integral and apply Tonelli.
    Proof: since $f, g \in L^1$, $|f(y)g(x)|$ is integrable over the triangle $0 \le y \le x \le 1$ by Tonelli:
    \[
    \int_0^1 \int_0^x |f(y)g(x)|\,dy\,dx \le \int_0^1 \int_0^1 |f(y)g(x)|\,dy\,dx = \norm{f}_1 \norm{g}_1 < \infty .
    \]
<1>2. Expand $\int_0^1 F(x)g(x)\,dx$.
    Proof: substituting $F(x) = \int_0^x f(y)\,dy$ and using Fubini (<1>1),
    \[
    \int_0^1 F(x)g(x)\,dx = \int_0^1 \int_0^x f(y)g(x)\,dy\,dx = \int_0^1 f(y) \int_y^1 g(x)\,dx\,dy .
    \]
<1>3. Evaluate the inner integral.
    Proof: $\int_y^1 g(x)\,dx = G(1) - G(y)$, so by <1>2,
    \[
    \int_0^1 F(x)g(x)\,dx = \int_0^1 f(y)\big(G(1) - G(y)\big)\,dy = G(1)\int_0^1 f - \int_0^1 f(y)G(y)\,dy .
    \]
<1>4. Conclude.
    Proof: $\int_0^1 f = F(1)$, so <1>3 gives $\int_0^1 F g = F(1)G(1) - \int_0^1 f G$, as claimed. (The same identity is the integration-by-parts formula for absolutely continuous functions $F, G$ with derivatives $f, g$ a.e.)
<1>5. Q.E.D.
:::
