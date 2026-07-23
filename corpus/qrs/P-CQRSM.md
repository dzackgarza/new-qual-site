---
schema: qual/card@1
id: P-CQRSM
kind: problem
title: "Let $(X,d)$ be a metric space. A function"
classification:
  areas:
  - real-analysis
  topics: []
relations: []
review: draft
---
Let $(X,d)$ be a metric space. A function
$f \colon X \to \mathbb{R}$ is said to be lower semi-continuous
(l.s.c) if $f^{-1}(a,\infty)  = \{x \in X \, \colon \,  f(x)> a\}$
is open in $X$ for every $a \in \mathbb{R}$. Analogously, $f$ is
upper semi-continuous (u.s.c) if
$f^{-1}(-\infty, b) = \{x \in X \, \colon \,  f(x)<b\}$ is open in
$X$ for every $b \in \mathbb{R}$.


1.  
Prove that a function $f \colon X \to \mathbb{R}$ is continuous
if and only if $f$ is both l.s.c. and u.s.c.


2.  
Prove that $f$ is lower semi-continuous if and only if
$\liminf_{n \to \infty} f(x_n) \geq f(x)$ whenever
$\{x_n\}_{n=1}^\infty \subseteq X$ such that $x_n \to x$ in $X$.


