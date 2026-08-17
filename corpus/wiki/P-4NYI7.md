---
schema: qual/card@1
id: P-4NYI7
kind: problem
title: $\int_{\RR} f=\int_0^\infty m(\{f>t\})\,dt$ for nonnegative measurable $f$
classification:
  areas:
  - real-analysis
  topics:
  - measure-theory
  - integrals
  - fubini-tonelli
relations: []
review: draft
solved: true
---
Let $f \geq 0$ be a measurable function on $\RR$.
Show that
\[
\int _{\RR} f = \int _{0}^{\infty} m(\{x: f(x)>t\}) dt
\]

:::{.concept}
\envlist
- Claim: If $E\subseteq \RR^a \cross \RR^b$ is a measurable set, then for almost every $y\in \RR^b$, the slice $E^y$ is measurable and
\[
m(E) = \int_{\RR^b} m(E^y) \,dy
.\]
  - Set $g = \chi_E$, which is non-negative and measurable, so apply Tonelli.
  - Conclude that $g^y = \chi_{E^y}$ is measurable, the function $y\mapsto \int g^y(x)\, dx$ is measurable, and $\int \int g^y(x)\,dx \,dy = \int g$.
  - But $\int g = m(E)$ and $\int\int g^y(x) \,dx\,dy = \int m(E^y)\,dy$.
:::

:::{.solution}
\envlist

> Note: $f$ is a function $\RR\to \RR$ in the original problem, but here I've assumed $f:\RR^n\to \RR$.

- Since $f\geq 0$, set 
$$
E\definedas \theset{(x, t) \in \RR^{n} \cross \RR \suchthat f(x) > t}
= \theset{(x, t) \in \RR^n \cross \RR \suchthat 0 \leq t < f(x)}
.$$
- Claim: since $f$ is measurable, $E$ is measurable and thus $m(E)$ makes sense.
  - Since $f$ is measurable, $F(x, t) \definedas t - f(x)$ is measurable on $\RR^n \cross \RR$.
  - Then write $E = \theset{F < 0} \intersect \theset{t\geq 0}$ as an intersection of measurable sets.
- We have slices 
\[
E^t &\definedas \theset{x\in \RR^n \suchthat (x, t) \in E} = \theset{x\in \RR^n \suchthat 0 \leq t < f(x)} \\
E^x &\definedas \theset{t\in \RR \suchthat (x, t) \in E} = \theset{t\in \RR \suchthat 0 \leq t \leq f(x)} = [0, f(x)]
.\]
  - $E_t$ is precisely the set that appears in the original RHS integrand.
  - $m(E^x) = f(x)$.
- Claim: $\chi_E$ satisfies the conditions of Tonelli, and thus $m(E) = \int \chi_E$ is equal to any iterated integral.
  - Non-negative: clear since $0\leq \chi_E \leq 1$
  - Measurable: characteristic functions of measurable sets are measurable.

- Conclude:
  1. For almost every $x$, $E^x$ is a measurable set, $x\mapsto m(E^x)$ is a measurable function, and $m(E) = \int_{\RR^n} m(E^x) \, dx$ 
  2. For almost every $t$, $E^t$ is a measurable set, $t\mapsto m(E^t)$ is a measurable function, and $m(E) = \int_{\RR} m(E^t) \, dt$ 
- On one hand,
\[
m(E) 
&= \int_{\RR^{n+1}} \chi_E(x, t) \\
&= \int_{\RR} \int_{\RR^n} \chi_E(x, t) \,dt \,dx \quad\text{by Tonelli}\\
&= \int_{\RR^n} m(E^x) \,dx \quad\text{first conclusion}\\
&= \int_{\RR^n} f(x) \,dx 
.\]
- On the other hand,
\[
m(E) 
&= \int_{\RR^{n+1}} \chi_E(x, t) \\
&= \int_\RR \int_{\RR^n} \chi_E(x, t) \, dx \,dt \quad\text{by Tonelli} \\
&= \int_\RR m(E^t) \,dt \quad\text{second conclusion}
.\]

- Thus
\[
\int_{\RR^n} f \,dx = m(E) = \int_\RR m(E^t) \,dt = \int_\RR m\qty{\theset{x\suchthat f(x) > t}}
.\]

:::



