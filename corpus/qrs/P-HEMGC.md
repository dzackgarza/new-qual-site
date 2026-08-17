---
schema: qual/card@1
id: P-HEMGC
kind: problem
title: "Prove that if $xf(x) \\in L^1(\\RR)$, then $F(y) \\da \\int f(x) \\cos(yx)\\, dx$ defines a $C^1$ function."
classification:
  areas:
  - real-analysis
  topics:
  - differentiation
  - integrals
relations: []
review: draft
solved: true
---

::: problem
Prove that if $xf(x) \in L^1(\RR)$, then
\[  
F(y) \da \int f(x) \cos(yx)\,  dx
\]
defines a $C^1$ function.
:::

::: {.solution}
> **AI-Generated Solution**

**Setup:** $F(y) = \int f(x)\cos(yx)\,dx$ is defined for all $y$ once $f \in L^1$; the hypothesis $xf \in L^1$ supplies the integrable majorant needed for differentiability.

<1>1. $F$ is well defined and continuous.
    <2>1. $|\cos(yx)| \le 1$, so $|f(x)\cos(yx)| \le |f(x)| \in L^1$.
        Proof: $f \in L^1$ by hypothesis (the problem's hypothesis is $xf \in L^1$; together with the implicit integrability of $f$ needed for $F$ to be defined).
    <2>2. $F$ is continuous.
        Proof: for $y_k \to y$, $f(x)\cos(y_k x) \to f(x)\cos(yx)$ pointwise with domination by $|f| \in L^1$; dominated convergence gives $F(y_k) \to F(y)$.

<1>2. $F$ is differentiable with $F'(y) = -\int x f(x)\sin(yx)\,dx$.
    <2>1. The candidate derivative $G(y) = -\int x f(x)\sin(yx)\,dx$ is well defined for all $y$.
        Proof: $|x f(x)\sin(yx)| \le |x f(x)| \in L^1$.
    <2>2. The difference quotient converges: $\frac{F(y + h) - F(y)}{h} \to G(y)$ as $h \to 0$.
        Proof: $\frac{F(y+h) - F(y)}{h} = \int f(x)\frac{\cos((y+h)x) - \cos(yx)}{h}\,dx$; the difference quotient of cosine converges pointwise to $-x\sin(yx)$, and is bounded by $|x|$ (mean value theorem applied to $\cos$), so the integrand is dominated by $|x f(x)| \in L^1$; dominated convergence passes the limit under the integral.
    <2>3. Q.E.D.
        Proof: <2>1 and <2>2.

<1>3. $F'$ is continuous.
    Proof: $G(y) = -\int x f(x)\sin(yx)\,dx$ is continuous by the argument of <1>1<2>2 with domination by $|xf| \in L^1$ (since $|\sin(yx)| \le 1$ and $x f(x)\sin(y_k x) \to x f(x)\sin(yx)$ pointwise).

<1>4. Q.E.D.
    Proof: <1>1 shows $F$ is continuous, <1>2 shows $F$ is differentiable, and <1>3 shows the derivative is continuous — i.e. $F \in C^1$.
:::
