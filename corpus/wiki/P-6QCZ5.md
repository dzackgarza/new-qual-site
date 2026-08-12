---
schema: qual/card@1
id: P-6QCZ5
kind: problem
title: "Prove that if $f, g: \\RR^n\\to \\CC$ is both measurable then $F(x, y) \\definedas f(x)$ and $h(x, y)\\definedas f(x-y) g(y)$ is measurable on $\\RR^n\\cross \\RR^n$."
classification:
  areas:
  - real-analysis
  topics: []
relations: []
review: draft
---
a. Prove that if $f, g: \RR^n\to \CC$ is both measurable then $F(x, y) \definedas f(x)$ and $h(x, y)\definedas f(x-y) g(y)$ is measurable on $\RR^n\cross \RR^n$.

b. Show that if $f\in L^1(\RR^n) \intersect L^\infty(\RR^n)$ and $g\in L^1(\RR^n)$, then $f\ast g \in L^1(\RR^n) \intersect L^\infty(\RR^n)$ is well defined, and carefully show that it satisfies the following properties:
\[
\norm{f\ast g}_\infty &\leq \norm{g}_1 \norm{f}_\infty
\norm{f\ast g}_1      &\leq \norm{g}_1 \norm{f}_1
\norm{f\ast g}_2      &\leq \norm{g}_1 \norm{f}_2
.\]

> Hint: first show $\abs{f\ast g}^2 \leq \norm{g}_1 \qty{ \abs{f}^2 \ast \abs{g}}$.

