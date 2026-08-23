---
schema: qual/card@1
id: P-RASP06A
kind: problem
title: "True/false on functions of bounded variation, measures, and Banach space duals"
classification:
  areas:
  - real-analysis
  topics:
  - Real Analysis
relations: []
review: draft
solved: false
---

::: problem
Determine if the statements below are True or False.
If True, give a brief proof.
If False, give a counterexample.

(a) If $f \in C([0,1])$, $f'$ exists a.e. ($m$) and $f' = 0$ a.e. ($m$), then $f$ is constant.

(b) If $E_1 \supset E_2 \supset \cdots$ are measurable sets such that $\mu(E_j) = 0$ for some $j$, then $\lim_{j \to \infty} \mu(E_j) = 0$.

(c) Suppose $\{f_j\}$ is a sequence in $L^1(X, \mu)$ with $f_1 \geq f_2 \geq \cdots \geq 0$ a.e. ($\mu$), and let $f(x) = \lim_{j \to \infty} f_j(x)$ a.e. ($\mu$). Then $\int_X f\,d\mu = \lim_{j \to \infty} \int_X f_j\,d\mu$.

(d) Let $\nu$ be a finite signed measure on $X$, and $|\nu|$ its total variation.
Then there is $f \in \mathcal{L}^1(X, |\nu|)$ such that for every $g \in L^1(X, \nu)$, $\int_X g\,d\nu = \int_X gf\,d|\nu|$.

(e) Let $X$ be a Banach space and $X^*$ its dual.
Let $\{x_j^*\}$ be a sequence in $X^*$ such that $\lim_{j \to \infty} x_j^*(x)$ exists (as a complex number) for every $x \in X$.
Then there is $x^* \in X^*$ such that $x^*(x) = \lim_{j \to \infty} x_j^*(x)$ for every $x \in X$.
:::
