---
schema: qual/card@1
id: P-2HIC2
kind: problem
title: $\int_0^1 Fg=F(1)G(1)-\int_0^1 fG$ for $F(x)=\int_0^x f$ and $G(x)=\int_0^x
  g$
classification:
  areas:
  - real-analysis
  topics:
  - Integrals
  - Fubini-Tonelli
relations: []
review: draft
---

::: {.problem title="?"}
Let $f, g \in L^1([0, 1])$ and for all $x\in [0, 1]$ define
\[
F(x) \definedas \int _{0}^{x} f(y) \, dy 
\qtext{and}
G(x)\definedas \int _{0}^{x} g(y) \, dy.
\]

Prove that
\[
\int _{0}^{1} F(x) g(x) \, dx = 
F(1) G(1) - \int _{0}^{1} f(x) G(x) \, dx
\]
:::

::: {.solution}
> **AI-Generated Solution**

<1>1. The double integral $\iint_{0 \le y \le x \le 1} |f(y)||g(x)|\,dy\,dx$ is finite.
Proof: Tonelli gives $\iint |f(y)||g(x)| \le \|f\|_1\|g\|_1 < \infty$; hence Fubini applies to $f(y)g(x)$.

<1>2. $\int_0^1 F(x)g(x)\,dx = \int_0^1\int_0^x f(y)g(x)\,dy\,dx$.
Proof: $F(x) = \int_0^x f(y)\,dy$ and Fubini (<1>1).

<1>3. Interchange the order: $\int_0^1\int_0^x f(y)g(x)\,dy\,dx = \int_0^1 f(y)\int_y^1 g(x)\,dx\,dy$.
Proof: the region $\{0 \le y \le x \le 1\}$ sliced vertically/horizontally; Fubini applies by <1>1.

<1>4. Q.E.D. Proof: $\int_y^1 g = G(1) - G(y)$, so $\int_0^1 Fg = \int_0^1 f(y)(G(1) - G(y))\,dy = G(1)F(1) - \int_0^1 fG$, using $F(1) = \int_0^1 f$.
:::
