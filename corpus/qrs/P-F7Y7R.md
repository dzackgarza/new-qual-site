---
schema: qual/card@1
id: P-F7Y7R
kind: problem
title: "Negate $\\forall x\\in \\RR,~\\exists y\\in \\RR \\suchthat \\abs{x-y} \\geq 2017$ $\\exists x\\in \\RR \\suchthat \\forall y\\in \\RR,~ \\abs{x-y} < 2017$ Note that $p\\implies q \\iff q \\vee \\neg p$, so we have\u2026"
classification:
  areas:
  - prelim
  topics:
  - logic-and-quantifiers
relations: []
review: draft
---

::: problem
1. 
   1. Negate $\forall x\in \RR,~\exists y\in \RR \suchthat \abs{x-y} \geq 2017$
   $$\exists x\in \RR \suchthat \forall y\in \RR,~ \abs{x-y} < 2017$$

   1. Note that $p\implies q \iff q \vee \neg p$, so we have $\neg(p \implies q) \iff \neg(q \vee \neg p) \iff p ~\&~ \neg q$.
$$
f: \RR \to \RR \text{ is continuous } \iff \\ 
\forall (x, y) \in \RR^2, ~\forall \varepsilon,~\exists \delta \suchthat \quad d(x,y) < \delta \implies d(f(x), f(y)) < \varepsilon \iff \\ 
\forall (x, y) \in \RR^2, ~\forall \varepsilon,~\exists \delta \suchthat \quad  d(x,y) \geq \delta ~~\vee~~   d(f(x), f(y)) < \varepsilon  ,
$$
so
$$
f: \RR \to \RR \text{ is not continuous } \iff \\ \exists (x,y) \in \RR^2, \exists \varepsilon \suchthat \forall \delta, \quad d(x,y) < \delta ~\&~ d(f(x), f(y)) \geq \varepsilon. \qed
$$
:::

::: {.solution}
> **AI-Generated Solution** (Gemini 3.7 Flash)

**Goal:** 
(a) Find the negation of the quantified statement: $\forall x \in \mathbb{R}, \, \exists y \in \mathbb{R} \text{ such that } |x - y| \ge 2017$.
(b) Formulate the standard $\varepsilon$-$\delta$ definition of continuity of $f: \mathbb{R} \to \mathbb{R}$ at a point (or globally) and derive its logical negation.

<1>1. The negation of $\forall x \in \mathbb{R}, \, \exists y \in \mathbb{R} \text{ such that } |x - y| \ge 2017$ is $\exists x \in \mathbb{R} \text{ such that } \forall y \in \mathbb{R}, \, |x - y| < 2017$.
    Proof:
    <2>1. By the duality rules for quantifiers, $\neg(\forall x, P(x)) \iff \exists x, \neg P(x)$ and $\neg(\exists y, Q(y)) \iff \forall y, \neg Q(y)$.
    <2>2. Applying these rules successively:
        $$\neg\big(\forall x \in \mathbb{R}, \, \exists y \in \mathbb{R}, \, |x - y| \ge 2017\big) \iff \exists x \in \mathbb{R}, \, \neg\big(\exists y \in \mathbb{R}, \, |x - y| \ge 2017\big)$$
        $$\iff \exists x \in \mathbb{R}, \, \forall y \in \mathbb{R}, \, \neg(|x - y| \ge 2017) \iff \exists x \in \mathbb{R}, \, \forall y \in \mathbb{R}, \, |x - y| < 2017.$$

<1>2. A function $f: \mathbb{R} \to \mathbb{R}$ is continuous on $\mathbb{R}$ if and only if:
    $$\forall x \in \mathbb{R}, \, \forall \varepsilon > 0, \, \exists \delta > 0 \text{ such that } \forall y \in \mathbb{R}, \, (|x - y| < \delta \implies |f(x) - f(y)| < \varepsilon).$$
    Proof: By the standard $\varepsilon$-$\delta$ definition of pointwise continuity at every $x \in \mathbb{R}$.

<1>3. The negation ($f$ is not continuous on $\mathbb{R}$) is:
    $$\exists x \in \mathbb{R}, \, \exists \varepsilon > 0 \text{ such that } \forall \delta > 0, \, \exists y \in \mathbb{R} \text{ such that } (|x - y| < \delta \text{ and } |f(x) - f(y)| \ge \varepsilon).$$
    Proof:
    <2>1. For propositions $p, q$, the conditional $p \implies q$ is logically equivalent to $\neg p \vee q$.
    <2>2. The negation of an implication is $\neg(p \implies q) \iff \neg(\neg p \vee q) \iff p \wedge \neg q$.
    <2>3. Applying quantifier negation rules to <1>2 interchanges each $\forall \leftrightarrow \exists$:
        $$\neg\Big(\forall x \in \mathbb{R}, \, \forall \varepsilon > 0, \, \exists \delta > 0, \, \forall y \in \mathbb{R}, \, (|x-y| < \delta \implies |f(x)-f(y)| < \varepsilon)\Big)$$
        $$\iff \exists x \in \mathbb{R}, \, \exists \varepsilon > 0, \, \forall \delta > 0, \, \exists y \in \mathbb{R}, \, \neg(|x-y| < \delta \implies |f(x)-f(y)| < \varepsilon)$$
        $$\iff \exists x \in \mathbb{R}, \, \exists \varepsilon > 0, \, \forall \delta > 0, \, \exists y \in \mathbb{R}, \, (|x-y| < \delta \wedge |f(x)-f(y)| \ge \varepsilon).$$
    Q.E.D.
:::
