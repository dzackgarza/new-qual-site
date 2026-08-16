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
